"""Paso 5 — estaciones ITV (redes oficiales por comunidad).

Fuentes, en orden de preferencia:
- Cataluña: Generalitat, dataset «Estacions d'Inspecció Tècnica de Vehicles
  (ITV)» (analisi.transparenciacatalunya.cat, 7dyp-y4dd). Trae dirección y
  coordenadas oficiales.
- Comunidad de Madrid: listado oficial de estaciones en
  comunidad.madrid/servicios/consumo/inspeccion-tecnica-vehiculos-itv
  (número de estación, titular, dirección). Se geocodifica con CartoCiudad.
- Aragón: directorio oficial aragon.es/itv/directorio-de-estaciones (da los
  municipios con estación); la dirección se toma de OpenStreetMap solo si el
  punto OSM está en uno de esos municipios.
- Resto (Castilla-La Mancha, Castilla y León y capitales de otras
  comunidades): OpenStreetMap (amenity=vehicle_inspection). NO es oficial:
  se marca `verificar: true` y el redactor debe confirmarla en la web del
  operador antes de publicarla (ver GUIA-REDACCION.md).
Salida: cache/itv.json (lista de estaciones normalizadas)
"""
import html as H
import json
import re

from comun import guardar, haversine_km, http_get, http_post, norm, q

CAT_URL = "https://analisi.transparenciacatalunya.cat/resource/7dyp-y4dd.json?$limit=5000"
MAD_URL = "https://www.comunidad.madrid/servicios/consumo/inspeccion-tecnica-vehiculos-itv"
ARA_URL = "https://www.aragon.es/itv/directorio-de-estaciones"
OVERPASS = "https://overpass-api.de/api/interpreter"


def centro_municipio(ine5: str):
    from comun import haversine_km  # noqa: F401
    try:
        d = json.loads(http_get(f"https://www.cartociudad.es/geocoder/api/geocoder/find?type=Municipio&id={int(ine5)}&q=x",
                                f"cc_mun_{ine5}.json", timeout=90))
        pts = [tuple(map(float, p.split()[:2])) for p in re.findall(r"-?\d+\.\d+ -?\d+\.\d+", d["geom"])]
        return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)
    except Exception:  # noqa: BLE001
        return None


def cataluna():
    out = []
    for e in json.loads(http_get(CAT_URL, "itv_cat.json")):
        # El dataset guarda grados×10^n como entero y pierde dígitos (Olèrdola
        # sale con long=173028, Viladecans con lat=413028): se prueba cada
        # escala y se elige la que cae más cerca del centro del municipio.
        try:
            cen = centro_municipio(e["codi_municipi"][:5])
            cands = [(int(e["lat"]) / 10 ** a, int(e["long"]) / 10 ** b) for a in range(3, 8) for b in range(3, 8)]
            cands = [c for c in cands if 40.4 < c[0] < 42.95 and 0.1 < c[1] < 3.4]
            lat, lng = min(cands, key=lambda c: haversine_km(c[0], c[1], *cen)) if cen and cands else (None, None)
            if lat is None or (cen and haversine_km(lat, lng, *cen) > 12):
                lat, lng = cen  # sin escala creíble: centro del municipio
        except (KeyError, ValueError, TypeError):
            continue
        out.append({
            "nombre": f"ITV {e.get('denominaci', '').strip()} ({e.get('estaci', '')})",
            "operador": e.get("operador"),
            "direccion": e.get("adre_a"), "cp": e.get("cp"), "municipio": e.get("municipi"),
            "lat": lat, "lng": lng, "horario": e.get("horari_de_servei"),
            "fuente": "Generalitat de Catalunya, dades obertes 7dyp-y4dd", "oficial": True, "verificar": False,
        })
    return out


def geocodifica(direccion: str, municipio: str):
    txt = re.sub(r"Tel[^\n]*", "", direccion).strip(" .")
    url = f"https://www.cartociudad.es/geocoder/api/geocoder/candidates?q={q(txt + ', ' + municipio)}&limit=5"
    try:
        cands = json.loads(http_get(url, "cc_geo_" + __import__("hashlib").md5((txt + municipio).encode()).hexdigest() + ".json"))
    except Exception:  # noqa: BLE001
        cands = []
    for c in cands:
        if c.get("lat") and norm(c.get("muni", "")).startswith(norm(municipio)[:6]):
            return c["lat"], c["lng"], "CartoCiudad (dirección)"
    # sin portal: centroide del término municipal (precisión de municipio)
    try:
        c = json.loads(http_get(
            f"https://www.cartociudad.es/geocoder/api/geocoder/candidates?q={q(municipio + ', Madrid')}&limit=5",
            f"cc_mun_name_{norm(municipio)}.json"))
        for x in c:
            if x.get("type") == "Municipio":
                d = json.loads(http_get(f"https://www.cartociudad.es/geocoder/api/geocoder/find?type=Municipio&id={x['id']}&q=x",
                                        f"cc_mun_{x['id']}.json"))
                pts = [tuple(map(float, p.split()[:2])) for p in re.findall(r"-?\d+\.\d+ -?\d+\.\d+", d["geom"])]
                return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts), "CartoCiudad (centro del municipio)"
    except Exception:  # noqa: BLE001
        pass
    return None, None, None


def madrid():
    h = http_get(MAD_URL, "itv_madrid.html").decode("utf-8", "ignore")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    t = re.sub(r"\n\s*\n+", "\n", t)
    ini = t.index("listado de las Estaciones de ITV")
    fin = t.index("Web de la Asociación de ITV")
    lineas = [x.strip() for x in t[ini:fin].split("\n")[1:] if x.strip() and x.strip() != "."]
    out, muni = [], None
    i = 0
    while i < len(lineas):
        ln = lineas[i]
        m = re.match(r"^(\d{4})\s+(.+)$", ln)
        if m and i + 1 < len(lineas):
            dire = lineas[i + 1]
            if dire.startswith(".") and i + 2 < len(lineas):
                dire = lineas[i + 2]
                i += 1
            tel = re.search(r"Tel[.:]?\s*([\d .\-/]+)", dire)
            calle = re.split(r"\s*Tel[.:]", dire)[0].strip(" .")
            lat, lng, prec = geocodifica(calle, muni.title())
            out.append({
                "nombre": f"ITV {m.group(2).strip().rstrip('.')} (estación {m.group(1)})",
                "operador": m.group(2).strip().rstrip("."),
                "direccion": calle, "municipio": muni.title(), "telefono": tel.group(1).strip() if tel else None,
                "lat": lat, "lng": lng, "precision": prec,
                "fuente": "Comunidad de Madrid, listado oficial de estaciones ITV (" + MAD_URL + ")",
                "oficial": True, "verificar": False,
            })
            i += 2
            continue
        if ln.isupper() or ln.upper() == ln:
            muni = ln.strip()
        i += 1
    return out


def osm():
    query = """[out:json][timeout:180];area["ISO3166-1"="ES"][admin_level=2]->.es;
nwr[amenity=vehicle_inspection](area.es);out center tags;"""
    data = http_post(OVERPASS, ("data=" + q(query)).encode(), {"Content-Type": "application/x-www-form-urlencoded"}, timeout=240)
    (__import__("comun").CACHE / "itv_osm.json").write_bytes(data)
    out = []
    for e in json.loads(data)["elements"]:
        tg = e.get("tags", {})
        lat = e.get("lat") or (e.get("center") or {}).get("lat")
        lng = e.get("lon") or (e.get("center") or {}).get("lon")
        if not lat:
            continue
        nombre_op = " ".join(str(tg.get(k, "")) for k in ("name", "operator", "brand"))
        # amenity=vehicle_inspection también se usa para básculas y talleres:
        # solo se aceptan puntos que se identifican como estación ITV
        if not re.search(r"\bITV\b|inspecci|itevelesa|applus|dekra|t[üu]v|atisae|veiasa|sgs|revisi[oó]n t[eé]cnica", nombre_op, re.I):
            continue
        calle = " ".join(x for x in [tg.get("addr:street"), tg.get("addr:housenumber")] if x)
        out.append({
            "nombre": tg.get("name") or tg.get("operator") or "Estación ITV",
            "operador": tg.get("operator") or tg.get("brand"),
            "direccion": calle or None, "cp": tg.get("addr:postcode"), "municipio": tg.get("addr:city"),
            "lat": lat, "lng": lng,
            "fuente": f"OpenStreetMap ({e['type']}/{e['id']}) — NO oficial, verificar",
            "oficial": False, "verificar": True,
        })
    return out


def osm_cache():
    # reutiliza la descarga previa aplicando el mismo filtrado
    from comun import CACHE
    import types
    data = (CACHE / "itv_osm.json").read_bytes()
    global http_post
    real = http_post
    http_post = lambda *a, **k: data  # noqa: E731
    try:
        return osm()
    finally:
        http_post = real


def aragon_municipios():
    h = http_get(ARA_URL, "itv_aragon.html").decode("utf-8", "ignore")
    t = H.unescape(re.sub(r"<[^>]+>", "\n", h))
    t = re.sub(r"\n\s*\n+", "\n", t)
    bloque = t[t.index("Municipio"):t.index("Eliminar filtros")]
    return {norm(x.strip()) for x in bloque.split("\n")[1:] if x.strip() and not x.strip().startswith("(")}


def main():
    cat, mad = cataluna(), madrid()
    o = osm() if not (__import__("comun").CACHE / "itv_osm.json").exists() else osm_cache()
    ara = aragon_municipios()
    # OSM: se descartan los puntos a menos de 1,5 km de una estación oficial
    # (son la misma estación); en Cataluña y Madrid manda la lista oficial.
    from comun import haversine_km
    ofi = [e for e in cat + mad if e["lat"]]
    resto = [e for e in o if all(haversine_km(e["lat"], e["lng"], x["lat"], x["lng"]) > 1.5 for x in ofi)]
    for e in resto:
        if e.get("municipio") and norm(e["municipio"]) in ara:
            e["fuente"] += "; municipio con estación según aragon.es"
    guardar("itv.json", {"cataluna": cat, "madrid": mad, "osm": resto, "aragon_municipios": sorted(ara)})
    print(f"ITV Cataluña {len(cat)}, Madrid {len(mad)} (sin coordenadas: {sum(1 for e in mad if not e['lat'])}), OSM resto {len(resto)}")


if __name__ == "__main__":
    main()
