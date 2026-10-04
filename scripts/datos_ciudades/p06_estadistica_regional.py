"""Paso 6 — datos estadísticos oficiales regionales (municipio a municipio).

- Cataluña — Idescat, El municipio en cifras (API EMEX):
  comarca, altitud oficial, superficie y parque de vehículos (turismos), este
  último elaborado por Idescat a partir de la DGT.
- Comunidad de Madrid — Instituto de Estadística, «Transporte por carretera.
  Parque de vehículos por tipo de vehículo. Municipios» (datos.comunidad.madrid),
  elaborado a partir de la DGT: turismos del último año.
Fuera de estas dos comunidades no hay fuente municipal abierta equivalente
cargada todavía: el campo queda vacío (no se estima).
Salida: cache/paso_regional.json
"""
import csv
import io
import json
import concurrent.futures as cf

from comun import cargar, guardar, http_get, norm

NODOS = "https://api.idescat.cat/emex/v1/nodes.json?tipus=cat,com,mun&lang=es"
EMEX = "https://api.idescat.cat/emex/v1/dades.json?id={id}&lang=es"
CAM_PARQUE = ("https://datos.comunidad.madrid/dataset/e241373e-685b-48c0-8f43-15aa549218dc/resource/"
              "3ee4e302-1def-496a-96bf-e4574302c7f6/download/"
              "transporte-por-carretera.-parque-de-vehiculos-por-tipo-de-vehiculo.-municipios.csv")


def idescat_mapa():
    d = json.loads(http_get(NODOS, "idescat_nodos.json"))
    out = {}
    for com in d["fitxes"]["v"]["v"]:
        for m in com["v"] if isinstance(com["v"], list) else [com["v"]]:
            out[m["id"][:5]] = {"id": m["id"], "comarca": com["content"]}
    return out


def emex_campos(idm: str):
    d = json.loads(http_get(EMEX.format(id=idm), f"emex_{idm}.json"))
    res = {}

    def walk(o, tabla=None):
        if isinstance(o, dict):
            if "f" in o and isinstance(o["f"], (list, dict)):
                fs = o["f"] if isinstance(o["f"], list) else [o["f"]]
                for f in fs:
                    res.setdefault(f.get("id"), (f, tabla))
            for k, v in o.items():
                walk(v, o if "r" in o and "c" in o else tabla)
        elif isinstance(o, list):
            for x in o:
                walk(x, tabla)
    walk(d)

    def val(fid):
        if fid not in res:
            return None, None
        f, t = res[fid]
        v = (f.get("v") or "").split(",")[0]
        anio = f.get("r") or (t or {}).get("r")
        try:
            return float(v), anio
        except ValueError:
            return None, anio
    alt, _ = val("f258")
    sup, anio_sup = val("f271")
    tur, anio_tur = val("f19")
    return {
        "altitud_m": int(alt) if alt is not None else None,
        "superficie_km2": sup,
        "turismos": int(tur) if tur is not None else None,
        "turismos_anio": anio_tur,
        "fuente": f"Idescat, El municipio en cifras (https://www.idescat.cat/emex/?id={idm})",
        "turismos_fuente": "Idescat a partir de la DGT" if tur is not None else None,
    }


def madrid_parque():
    raw = http_get(CAM_PARQUE, "cam_parque.csv", timeout=120).decode("latin-1")
    filas = list(csv.reader(io.StringIO(raw), delimiter=";"))
    hdr = filas[0]
    i_a, i_t, i_tipo, i_v = hdr.index("Año"), hdr.index("Territorio"), hdr.index("Tipo"), hdr.index("Valor")
    i_c = hdr.index("Código territorio")
    ult = {}
    for r in filas[1:]:
        if len(r) <= i_v or r[i_tipo] != "Turismos":
            continue
        try:
            a, v = int(r[i_a]), int(r[i_v])
        except ValueError:
            continue
        cod = "28" + r[i_c][:3]  # el CSV usa el código INE de 4 cifras con dígito de control
        if cod not in ult or a > ult[cod][0]:
            ult[cod] = (a, v, r[i_t])
    return ult


def main():
    base = cargar("paso_base.json")
    mapa = idescat_mapa()
    cam = madrid_parque()
    out = {}
    cat = {s: c for s, c in base.items() if c["ccaa"].startswith("Catalu")}

    def uno(item):
        s, c = item
        m = mapa.get(str(c["ine"]).zfill(5))
        if not m:
            return s, None
        r = emex_campos(m["id"])
        r["comarca"] = m["comarca"]
        return s, r
    with cf.ThreadPoolExecutor(8) as ex:
        for s, r in ex.map(uno, cat.items()):
            if r:
                out[s] = r
    for s, c in base.items():
        if c["provincia"] == "Madrid":
            v = cam.get(str(c["ine"]).zfill(5))
            if v:
                out[s] = {
                    "turismos": v[1], "turismos_anio": str(v[0]),
                    "turismos_fuente": "Instituto de Estadística de la Comunidad de Madrid a partir de la DGT (datos.comunidad.madrid)",
                }
    guardar("paso_regional.json", out)
    print(f"Idescat: {sum(1 for s in out if 'comarca' in out[s])}/{len(cat)} catalanas; "
          f"turismos: {sum(1 for v in out.values() if v.get('turismos'))}")


if __name__ == "__main__":
    main()
