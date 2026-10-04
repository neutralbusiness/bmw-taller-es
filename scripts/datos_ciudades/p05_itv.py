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


def _coords_cat(e):
    """Coordenadas de una estación del dataset de la Generalitat.

    Los campos `lat`/`long` guardan los grados sin punto decimal y sin ceros
    (Viladecans lat=413028 → 41.3028; Lleida long=66082 → 0.66082), así que
    la escala no se puede deducir con seguridad. El campo
    `localitzador_a_google_maps` trae las mismas coordenadas CON punto decimal
    («q=41.3028+2.019474»): es la fuente buena. Solo si faltara se reconstruye
    con la parte entera conocida (lat 40-42, long 0-3).
    """
    url = (e.get("localitzador_a_google_maps") or {}).get("url", "")
    m = re.search(r"q=(-?\d+\.\d+)\+(-?\d+\.\d+)", url)
    if m:
        return float(m.group(1)), float(m.group(2))
    la, lo = str(int(e["lat"])), str(int(e["long"]))
    lat = float(la[:2] + "." + la[2:])
    lng = float(lo[0] + "." + lo[1:]) if lo[0] in "123" else float("0." + lo)
    return lat, lng


def limpia_texto(s):
    """Arregla la codificación del dataset de la Generalitat.

    - comillas escapadas varias veces: `\\\\\\"Bufalvent\\\\\\"` → «Bufalvent»;
    - apóstrofo perdido en la exportación: «l¿estació» → «l'estació»;
    - espacios repetidos."""
    if not s:
        return s
    s = re.sub(r'\\*"([^"\\]+?)\\*"', r"«\1»", s)
    s = s.replace("\\", "")
    s = re.sub(r"(?<=\w)¿(?=\w)", "'", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def nombre_oficial_cat(m):
    """«Borges Blanques, les» → «les Borges Blanques» (forma oficial del nomenclátor)."""
    m = (m or "").strip()
    x = re.match(r"^(.+?),\s*(el|la|els|les|l'|l’)$", m, re.I)
    if x:
        art = x.group(2)
        return (art + x.group(1)) if art.endswith(("'", "’")) else f"{art} {x.group(1)}"
    return m


def cataluna():
    out = []
    for e in json.loads(http_get(CAT_URL, "itv_cat.json")):
        try:
            lat, lng = _coords_cat(e)
        except (KeyError, ValueError, TypeError):
            continue
        if not (40.4 < lat < 42.95 and 0.1 < lng < 3.4):
            continue
        out.append({
            "nombre": limpia_texto(f"ITV {e.get('denominaci', '').strip()} ({e.get('estaci', '')})"),
            "operador": e.get("operador"),
            "direccion": limpia_texto(e.get("adre_a")), "cp": e.get("cp"), "municipio": nombre_oficial_cat(e.get("municipi")),
            "ine5": (e.get("codi_municipi") or "")[:5] or None,
            "lat": lat, "lng": lng, "horario": e.get("horari_de_servei"), "precision": "Generalitat (coordenadas de la estación)",
            "fuente": "Generalitat de Catalunya, dades obertes 7dyp-y4dd", "oficial": True, "verificar": False,
        })
    return out


ABREV = [(r"^Avda[.,]?\s*", "Avenida "), (r"^C/\s*", "Calle "), (r"^Ctra[.,]?\s*", "Carretera "),
         (r"^P[º°][.]?\s*", "Paseo "), (r"^Pol[.]?\s*Ind[.]?\s*", "Polígono Industrial "), (r"^C[º°][.]?\s*", "Camino "), (r"\bn[º°]\s*", "")]


def _variantes(txt: str):
    """Formas de la dirección a probar en CartoCiudad, de más a menos literal."""
    v = []
    # punto kilométrico: «A-6, km 37,6», «Ctra. M-506 p.k. 4,200», «Carretera A1, km 40,200»
    m = re.search(r"\b([AMN])-?(\d+)\b.*?(?:km|p\.\s*k)\.?\s*(\d+)", txt, re.I)
    if m:
        v.append(("pk", f"{m.group(1).upper()}-{m.group(2)} km {m.group(3)}"))
        v.append(("pk", f"{m.group(1).upper()}-{m.group(2)} {m.group(3)}"))
    calle = re.split(r"(?<=\d)\.\s+|\s+(?=Centro Comercial|Pol\.)|,\s*P\d|\s+-\s+|\.\s+(?=Pol|Parque|Centro|C\.\s*C|Parc|Tel|\()|\(|\s{2,}", txt)[0]
    calle = re.sub(r",?\s*Parcela.*$", "", calle, flags=re.I)
    calle = re.sub(r"(\d+)\s*-\s*\d+", r"\1", calle)       # «43-45» → 43
    for a, b in ABREV:
        calle = re.sub(a, b, calle, flags=re.I)
    calle = re.sub(r"^Avenida,\s*", "Avenida ", calle).strip(" .,")
    v.append(("calle", txt))          # tal cual viene en el listado
    v.append(("calle", calle))
    v.append(("calle", re.sub(r",?\s*s/n$", "", calle, flags=re.I)))
    return v


def geocodifica(direccion: str, municipio: str):
    import hashlib
    txt = re.sub(r"Tel[^\n]*", "", direccion).strip(" .")
    for tipo, var in _variantes(txt):
        qq = var if tipo == "pk" else f"{var}, {municipio}"
        url = f"https://www.cartociudad.es/geocoder/api/geocoder/candidates?q={q(qq)}&limit=5"
        try:
            cands = json.loads(http_get(url, "cc_geo2_" + hashlib.md5(qq.encode()).hexdigest() + ".json"))
        except Exception:  # noqa: BLE001
            cands = []
        for c in cands:
            if not c.get("lat") or c.get("type") != "portal":
                continue
            # un p.k. es único en la red de la comunidad (puede caer en el
            # término vecino: la 2871 está en el M-506 p.k. 4,2, junto a
            # Móstoles); una calle tiene que estar en el municipio del listado
            if tipo == "pk" or norm(c.get("muni", "")).startswith(norm(municipio)[:6]):
                return c["lat"], c["lng"], "CartoCiudad (punto kilométrico)" if tipo == "pk" else "CartoCiudad (dirección)"
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


def ine_madrid(municipio: str):
    """Código INE del municipio madrileño del listado (CartoCiudad, tipo Municipio).

    El listado oficial da el nombre abreviado («Humanes», «Paracuellos»,
    «Lozoyuela»); con el código se empareja sin depender de cómo escriba el
    repo el nombre («Molar, El», «Arganda»)."""
    try:
        c = json.loads(http_get(
            f"https://www.cartociudad.es/geocoder/api/geocoder/candidates?q={q(municipio + ', Madrid')}&limit=5",
            f"cc_mun_name_{norm(municipio)}.json"))
    except Exception:  # noqa: BLE001
        return None
    nm = norm(municipio)
    # el listado usa nombres de núcleo: Cerceda es del municipio de El Boalo
    # (El Boalo, Cerceda y Mataelpino) y Lozoyuela de Lozoyuela-Navas-Sieteiglesias
    alias = {"cerceda": "28023", "lozoyuela": "28901"}
    if nm in alias:
        return alias[nm]
    for x in c:
        if x.get("type") == "Municipio" and str(x.get("id", "")).startswith("28"):
            mx = norm(x.get("muni", ""))
            if mx == nm or mx.startswith(nm + " ") or mx.replace(" ", "").startswith(nm.replace(" ", "")):
                return str(x["id"]).zfill(5)
    return None


def madrid():
    h = http_get(MAD_URL, "itv_madrid.html").decode("utf-8", "ignore")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = H.unescape(re.sub(r"<[^>]+>", "\n", t)).replace("\xa0", " ")  # «San Sebastián\xa0De Los Reyes»: norm() se comía el espacio
    t = re.sub(r"[ \t]{2,}", " ", t)
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
                "direccion": calle, "municipio": muni.title(), "ine5": ine_madrid(muni.title()),
                "telefono": tel.group(1).strip() if tel else None,
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
