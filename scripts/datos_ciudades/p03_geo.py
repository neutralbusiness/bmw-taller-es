"""Paso 3 — geografía oficial del municipio.

- CartoCiudad (IGN/CNIG, geocodificador oficial): polígono del término
  municipal por código INE. Con él se comprueba que las coordenadas del JSON
  caen dentro del municipio (si no, se sustituyen por el centroide del
  polígono y se marca) y se calcula la superficie aproximada.
- Altitud del punto: API de elevación de Open-Meteo (MDT Copernicus GLO-90).
  En Cataluña se sobrescribe después con la altitud oficial de Idescat (paso 6).
Salida: cache/paso_geo.json
"""
import json
import math

from comun import cargar, guardar, http_get

CC = "https://www.cartociudad.es/geocoder/api/geocoder/find?type=Municipio&id={ine}&q=x"


def parse_multipolygon(wkt: str):
    wkt = wkt.strip()
    body = wkt[wkt.index("("):]
    polys = []
    for poly in body.split(")),"):
        rings = []
        for ring in poly.split("),"):
            pts = []
            for par in ring.replace("(", " ").replace(")", " ").split(","):
                xy = par.split()
                if len(xy) >= 2:
                    pts.append((float(xy[0]), float(xy[1])))
            if pts:
                rings.append(pts)
        if rings:
            polys.append(rings)
    return polys


def dentro(x, y, ring):
    ins = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi:
            ins = not ins
        j = i
    return ins


def area_km2(ring):
    # proyección equirrectangular local: suficiente para un dato redondeado
    lat0 = math.radians(sum(p[1] for p in ring) / len(ring))
    kx, ky = 111.32 * math.cos(lat0), 110.57
    a = 0.0
    for i in range(len(ring)):
        x1, y1 = ring[i - 1]
        x2, y2 = ring[i]
        a += (x1 * kx) * (y2 * ky) - (x2 * kx) * (y1 * ky)
    return abs(a) / 2


def main():
    base = cargar("paso_base.json")
    out = cargar("paso_geo.json", {}) or {}
    for s, c in base.items():
        if s in out and "error" not in out[s]:
            continue
        ine = str(c["ine"]).zfill(5)
        try:
            d = json.loads(http_get(CC.format(ine=ine.lstrip("0")), f"cc_mun_{ine}.json", timeout=60))  # CartoCiudad no acepta el cero inicial
            polys = parse_multipolygon(d["geom"])
        except Exception as e:  # noqa: BLE001
            out[s] = {"error": str(e)[:120]}
            continue
        ext = [p[0] for p in polys]
        sup = sum(area_km2(r) for r in ext) - sum(area_km2(h) for p in polys for h in p[1:])
        ok = any(dentro(c["lng"], c["lat"], r) for r in ext)
        big = max(ext, key=len)
        cx, cy = sum(p[0] for p in big) / len(big), sum(p[1] for p in big) / len(big)
        out[s] = {
            "superficie_km2": round(sup, 1),
            "coord_en_municipio": ok,
            "lat": c["lat"] if ok else round(cy, 5),
            "lng": c["lng"] if ok else round(cx, 5),
            "fuente": f"CartoCiudad (IGN), término municipal INE {ine}",
        }
    # altitud en lotes de 100
    pend = [s for s in base if "lat" in out.get(s, {}) and "altitud_m" not in out[s]]
    for i in range(0, len(pend), 100):
        lote = pend[i:i + 100]
        la = ",".join(str(out[s]["lat"]) for s in lote)
        lo = ",".join(str(out[s]["lng"]) for s in lote)
        d = json.loads(http_get(f"https://api.open-meteo.com/v1/elevation?latitude={la}&longitude={lo}", timeout=60))
        for s, e in zip(lote, d["elevation"]):
            out[s]["altitud_m"] = round(e)
            out[s]["altitud_fuente"] = "Open-Meteo Elevation API (MDT Copernicus GLO-90)"
    guardar("paso_geo.json", out)
    malas = [s for s, v in out.items() if v.get("coord_en_municipio") is False]
    err = [s for s, v in out.items() if "error" in v]
    print(f"geo: {len(out)}; coordenadas fuera del municipio (corregidas): {malas}; errores: {err}")


if __name__ == "__main__":
    main()
