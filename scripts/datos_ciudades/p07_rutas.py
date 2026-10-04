"""Paso 7 — distancias reales por carretera (OSRM sobre OpenStreetMap).

Para cada ciudad:
- ruta al taller real que la atiende (si tiene dirección): km, y las vías por
  las que va la ruta (refs de carretera con más de 2 km de recorrido);
- servicio oficial BMW más cercano por carretera (de los 6 más próximos en
  línea recta) — solo como referencia comparativa;
- estación ITV: las que hay DENTRO del municipio y, si no hay, la más cercana
  por carretera (de las 8 más próximas en línea recta).
«Más cercano por carretera» = la ruta más corta entre las que propone OSRM.
La tabla de OSRM da la distancia de la ruta MÁS RÁPIDA, que a veces da un
rodeo por autopista: de Rellinars a Terrassa la tabla da 33,6 km (por la C-16)
y la ruta directa por la B-122 tiene 21,1 km; con solo la tabla, el servicio
oficial «más cercano» salía Sant Fruitós (25,1 km). Por eso, para cada
candidata que pueda ganar (línea recta menor que la ganadora de la tabla y
tabla < 1,8 veces la ganadora) se piden las rutas alternativas y se toma la
más corta. Con 3 candidatas BMW, Sant Julià de Cerdanyola daba Vic (71 km)
porque Sant Fruitós era la 4.ª en línea recta; ahora son 6 (BMW) y 8 (ITV).
Origen de las rutas: el punto de la página del repo, salvo que caiga fuera del
casco urbano y a más de 1 km de él (paso 3b, `paso_nucleo.json`): entonces el
centro del núcleo que da nombre al municipio. Vilassar de Dalt tenía el punto
en un camino de la sierra y OSRM llevaba la ruta por la montaña (ITV
«más cercana» Granollers, 11,5 km, en vez de Argentona, a 10,1 km del casco).
Se guardan km en línea recta y por carretera. NO se publica el tiempo de
OSRM: es una estimación sin tráfico y se presta a promesas falsas.
Servidor: router.project-osrm.org (demo pública, 1 petición/s). Caché por ciudad.
Salida: cache/paso_rutas.json
"""
import json
import time

from comun import CACHE, SOCIOS, cargar, guardar, haversine_km, http_get, norm
from p03_geo import dentro, parse_multipolygon


def poligono(ine):
    f = CACHE / f"cc_mun_{str(ine).zfill(5)}.json"
    try:
        return [p[0] for p in parse_multipolygon(json.loads(f.read_text())["geom"])]
    except Exception:  # noqa: BLE001
        return []

OSRM = "https://router.project-osrm.org"


def osrm(path: str, cache: str):
    for i in range(4):
        try:
            d = json.loads(http_get(f"{OSRM}{path}", cache, timeout=60))
            if d.get("code") == "Ok":
                return d
        except Exception:  # noqa: BLE001
            pass
        time.sleep(2 + i * 3)
    return None


N_BMW, N_ITV = 6, 8


def km_mas_corta(s, lat, lng, p):
    """Distancia (km) de la ruta más corta entre las alternativas de OSRM."""
    clave = f"{p['lat']:.5f}_{p['lng']:.5f}".replace("-", "m")
    d = osrm(f"/route/v1/driving/{lng},{lat};{p['lng']},{p['lat']}?overview=false&alternatives=3", f"osrm_a_{s}_{clave}.json")
    if not d:
        return None
    return round(min(r["distance"] for r in d["routes"]) / 1000, 1)


def elegir(s, lat, lng, filas):
    """filas: (tipo, punto, km_tabla, km_linea). Devuelve (punto, km, km_linea, km_ruta_rapida)."""
    if not filas:
        return None
    con = [f for f in filas if f[2] is not None]
    if not con:
        f = min(filas, key=lambda f: f[3])
        return f[1], None, f[3], None, []
    gana = min(con, key=lambda f: f[2])
    res = []
    for f in con:
        km = f[2]
        if f is gana or (f[3] < gana[2] and f[2] <= 1.8 * gana[2]):
            alt = km_mas_corta(s, lat, lng, f[1])
            if alt is not None:
                km = min(km, alt)
        res.append((f[1], km, f[3], f[2]))
    res.sort(key=lambda x: (x[1], x[2]))
    # otras a menos de 1 km de diferencia: la «más cercana» es un empate práctico
    # (Santa Maria d'Oló: ITV de Sant Fruitós y de Vic, las dos a 27,2 km)
    empates = [{"nombre": x[0].get("nombre"), "municipio": x[0].get("municipio"), "km_carretera": x[1]}
               for x in res[1:] if x[1] - res[0][1] < 1.0]
    return (*res[0], empates)


def main():
    base = cargar("paso_base.json")
    geo = cargar("paso_geo.json")
    nucleo = cargar("paso_nucleo.json", {}) or {}
    bmw = cargar("bmw_oficial.json")["puntos"]
    itv = cargar("itv.json")
    oficiales = [e for e in itv["cataluna"] + itv["madrid"] if e.get("lat")]
    munis_mad = {norm(e["municipio"]) for e in itv["madrid"]}
    # OSM solo fuera de Cataluña y Madrid, y nunca un punto que diga estar en
    # un municipio madrileño con estación oficial (sería la misma, mal geocodificada)
    osm = [e for e in itv["osm"] if not (e.get("municipio") and norm(e["municipio"]) in munis_mad)]
    import sys
    out = {} if "--todo" in sys.argv else (cargar("paso_rutas.json", {}) or {})
    for n, (s, c) in enumerate(base.items()):
        if s in out:
            continue
        g = geo.get(s, {})
        lat, lng = g.get("lat", c["lat"]), g.get("lng", c["lng"])
        nu = nucleo.get(s) or {}
        r = {"origen": [lat, lng]}
        if nu.get("usar_como_origen"):
            lat, lng = nu["lat"], nu["lng"]
            r = {"origen": [lat, lng], "origen_nucleo": nu["nombre"], "punto_repo": [g.get("lat", c["lat"]), g.get("lng", c["lng"])]}
        if c["ccaa"].startswith("Catalu") or c["provincia"] == "Madrid":
            estaciones = oficiales  # red oficial completa publicada por la comunidad
        else:
            estaciones = oficiales + osm
        # ── ITV en el propio municipio ──
        # Listas oficiales (Generalitat, Comunidad de Madrid): manda el
        # municipio que da la propia lista (código INE en Cataluña, nombre en
        # Madrid). NO el polígono: varias estaciones de Madrid solo se pueden
        # situar en el centro de su término, y ese punto puede caer en el
        # vecino (la 2818 de Algete salía «en» Fuente el Saz de Jarama).
        # OSM: dentro del término municipal (polígono de CartoCiudad) o, sin
        # polígono, mismo nombre. Para barrios no aplica.
        poly = poligono(c["ine"]) if c.get("tipo") == "municipio" else []
        nc = norm(c["nombre"])

        def mismo_municipio(e):
            if e.get("ine5"):
                return e["ine5"] == str(c["ine"]).zfill(5)
            nm = norm(e.get("municipio") or "")
            return bool(nm) and (nm == nc or nc.startswith(nm + " "))  # «Humanes» = Humanes de Madrid
        en_mun = [] if c.get("tipo") != "municipio" else [
            e for e in estaciones
            if (e.get("oficial") and mismo_municipio(e))
            or (not e.get("oficial") and ((poly and any(dentro(e["lng"], e["lat"], r) for r in poly))
                                          or (not poly and mismo_municipio(e))))]
        r["itv_en_municipio"] = [{k: e.get(k) for k in ("nombre", "operador", "direccion", "municipio", "fuente", "oficial", "verificar", "precision")} for e in en_mun]
        destinos = []
        soc = SOCIOS.get(c["socio"] or "", {})
        if soc.get("direccion"):
            destinos.append(("socio", soc))
        cerca_bmw = sorted(bmw, key=lambda p: haversine_km(lat, lng, p["lat"], p["lng"]))[:N_BMW]
        destinos += [("bmw", p) for p in cerca_bmw]
        cerca_itv = [] if en_mun else sorted(estaciones, key=lambda p: haversine_km(lat, lng, p["lat"], p["lng"]))[:N_ITV]
        destinos += [("itv", p) for p in cerca_itv]
        coords = f"{lng},{lat};" + ";".join(f"{p['lng']},{p['lat']}" for _, p in destinos)
        t = osrm(f"/table/v1/driving/{coords}?sources=0&annotations=distance", f"osrm_t2_{s}.json")
        if t and len(t.get("destinations", [])) != len(destinos) + 1:
            # caché de una ejecución con otros destinos: se vuelve a pedir
            (CACHE / f"osrm_t2_{s}.json").unlink()
            t = osrm(f"/table/v1/driving/{coords}?sources=0&annotations=distance", f"osrm_t2_{s}.json")
        dist = (t or {}).get("distances", [[None]])[0][1:] if t else [None] * len(destinos)

        def km(i):
            return round(dist[i] / 1000, 1) if dist and dist[i] is not None else None
        filas = [(tipo, p, km(i), round(haversine_km(lat, lng, p["lat"], p["lng"]), 1)) for i, (tipo, p) in enumerate(destinos)]
        if soc.get("direccion"):
            _, p, kc, kl = filas[0]
            r["socio"] = {"id": c["socio"], "km_carretera": kc, "km_linea": kl}
            ru = osrm(f"/route/v1/driving/{lng},{lat};{p['lng']},{p['lat']}?overview=false&steps=true", f"osrm_r2_{s}.json")
            if ru:
                acc = {}
                for st in ru["routes"][0]["legs"][0]["steps"]:
                    ref = (st.get("ref") or "").split(";")[0].strip()
                    if ref:
                        acc[ref] = acc.get(ref, 0) + st["distance"]
                r["socio"]["vias_ruta"] = [k for k, v in acc.items() if v > 2000]
        e = elegir(s, lat, lng, [f for f in filas if f[0] == "bmw"])
        if e:
            p, kc, kl, kr, emp = e
            r["bmw_oficial"] = {**{k: p.get(k) for k in ("nombre", "razon_social", "direccion", "cp", "municipio", "web", "solo_taller", "centro_ocasion_con_taller") if p.get(k) is not None or k in ("web", "solo_taller")},
                                "km_carretera": kc, "km_linea": kl}
            if kr is not None and kc is not None and kr - kc >= 0.5:
                r["bmw_oficial"]["km_ruta_mas_rapida"] = kr
            if emp:
                r["bmw_oficial"]["casi_igual_de_cerca"] = emp
        e = elegir(s, lat, lng, [f for f in filas if f[0] == "itv"])
        if e:
            p, kc, kl, kr, emp = e
            r["itv_cercana"] = {**{k: p.get(k) for k in ("nombre", "operador", "direccion", "municipio", "fuente", "oficial", "verificar", "precision")},
                                "km_carretera": kc, "km_linea": kl}
            if kr is not None and kc is not None and kr - kc >= 0.5:
                r["itv_cercana"]["km_ruta_mas_rapida"] = kr
            if emp:
                r["itv_cercana"]["casi_igual_de_cerca"] = emp
        r["fuente"] = "Distancias por carretera: OSRM (router.project-osrm.org) sobre datos de OpenStreetMap; servicio oficial e ITV: ruta más corta entre las alternativas de OSRM"
        out[s] = r
        if n % 20 == 0:
            guardar("paso_rutas.json", out)
            print(n, s, flush=True)
    guardar("paso_rutas.json", out)
    print(f"rutas: {len(out)}; sin distancia al socio: {[s for s, v in out.items() if 'socio' in v and v['socio']['km_carretera'] is None]}")


if __name__ == "__main__":
    main()
