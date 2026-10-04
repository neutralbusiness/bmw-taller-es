"""Paso 7 — distancias reales por carretera (OSRM sobre OpenStreetMap).

Para cada ciudad:
- ruta al taller real que la atiende (si tiene dirección): km, y las vías por
  las que va la ruta (refs de carretera con más de 2 km de recorrido);
- servicio oficial BMW más cercano por carretera (de los 3 más próximos en
  línea recta) — solo como referencia comparativa;
- estación ITV: las que hay DENTRO del municipio y, si no hay, la más cercana
  por carretera (de las 3 más próximas en línea recta).
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


def main():
    base = cargar("paso_base.json")
    geo = cargar("paso_geo.json")
    bmw = cargar("bmw_oficial.json")["puntos"]
    itv = cargar("itv.json")
    oficiales = [e for e in itv["cataluna"] + itv["madrid"] if e.get("lat")]
    munis_mad = {norm(e["municipio"]) for e in itv["madrid"]}
    # OSM solo fuera de Cataluña y Madrid, y nunca un punto que diga estar en
    # un municipio madrileño con estación oficial (sería la misma, mal geocodificada)
    osm = [e for e in itv["osm"] if not (e.get("municipio") and norm(e["municipio"]) in munis_mad)]
    out = cargar("paso_rutas.json", {}) or {}
    for n, (s, c) in enumerate(base.items()):
        if s in out:
            continue
        g = geo.get(s, {})
        lat, lng = g.get("lat", c["lat"]), g.get("lng", c["lng"])
        r = {"origen": [lat, lng]}
        if c["ccaa"].startswith("Catalu") or c["provincia"] == "Madrid":
            estaciones = oficiales  # red oficial completa publicada por la comunidad
        else:
            estaciones = oficiales + osm
        # ── ITV en el propio municipio (por nombre de municipio) ──
        # Dentro del término municipal (polígono oficial de CartoCiudad) o, si
        # no hay polígono, mismo nombre de municipio. Para barrios no aplica:
        # el polígono sería el del municipio entero.
        poly = poligono(c["ine"]) if c.get("tipo") == "municipio" else []
        en_mun = [e for e in estaciones
                  if (poly and any(dentro(e["lng"], e["lat"], r) for r in poly))
                  or (not poly and c.get("tipo") == "municipio" and e.get("municipio") and norm(e["municipio"]) == norm(c["nombre"]))]
        r["itv_en_municipio"] = [{k: e.get(k) for k in ("nombre", "operador", "direccion", "municipio", "fuente", "oficial", "verificar")} for e in en_mun]
        destinos = []
        soc = SOCIOS.get(c["socio"] or "", {})
        if soc.get("direccion"):
            destinos.append(("socio", soc))
        cerca_bmw = sorted(bmw, key=lambda p: haversine_km(lat, lng, p["lat"], p["lng"]))[:3]
        destinos += [("bmw", p) for p in cerca_bmw]
        cerca_itv = [] if en_mun else sorted(estaciones, key=lambda p: haversine_km(lat, lng, p["lat"], p["lng"]))[:3]
        destinos += [("itv", p) for p in cerca_itv]
        coords = f"{lng},{lat};" + ";".join(f"{p['lng']},{p['lat']}" for _, p in destinos)
        t = osrm(f"/table/v1/driving/{coords}?sources=0&annotations=distance", f"osrm_t_{s}.json")
        dist = (t or {}).get("distances", [[None]])[0][1:] if t else [None] * len(destinos)

        def km(i):
            return round(dist[i] / 1000, 1) if dist and dist[i] is not None else None
        filas = [(tipo, p, km(i), round(haversine_km(lat, lng, p["lat"], p["lng"]), 1)) for i, (tipo, p) in enumerate(destinos)]
        if soc.get("direccion"):
            _, p, kc, kl = filas[0]
            r["socio"] = {"id": c["socio"], "km_carretera": kc, "km_linea": kl}
            ru = osrm(f"/route/v1/driving/{lng},{lat};{p['lng']},{p['lat']}?overview=false&steps=true", f"osrm_r_{s}.json")
            if ru:
                acc = {}
                for st in ru["routes"][0]["legs"][0]["steps"]:
                    ref = (st.get("ref") or "").split(";")[0].strip()
                    if ref:
                        acc[ref] = acc.get(ref, 0) + st["distance"]
                r["socio"]["vias_ruta"] = [k for k, v in acc.items() if v > 2000]
        b = [f for f in filas if f[0] == "bmw"]
        b.sort(key=lambda f: f[2] if f[2] is not None else f[3] * 1.3)
        if b:
            _, p, kc, kl = b[0]
            r["bmw_oficial"] = {**{k: p.get(k) for k in ("nombre", "razon_social", "direccion", "cp", "municipio", "web", "solo_taller")},
                                "km_carretera": kc, "km_linea": kl}
        it = [f for f in filas if f[0] == "itv"]
        it.sort(key=lambda f: f[2] if f[2] is not None else f[3] * 1.3)
        if it:
            _, p, kc, kl = it[0]
            r["itv_cercana"] = {**{k: p.get(k) for k in ("nombre", "operador", "direccion", "municipio", "fuente", "oficial", "verificar", "precision")},
                                "km_carretera": kc, "km_linea": kl}
        r["fuente"] = "Distancias por carretera: OSRM (router.project-osrm.org) sobre datos de OpenStreetMap"
        out[s] = r
        if n % 20 == 0:
            guardar("paso_rutas.json", out)
            print(n, s, flush=True)
    guardar("paso_rutas.json", out)
    print(f"rutas: {len(out)}; sin distancia al socio: {[s for s, v in out.items() if 'socio' in v and v['socio']['km_carretera'] is None]}")


if __name__ == "__main__":
    main()
