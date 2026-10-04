"""Paso 8 — vías de acceso y costa (OpenStreetMap vía Overpass, en bloque).

Dos consultas para toda España (la API pública limita a una petición cada
vez; ir ciudad a ciudad tarda horas):
- carreteras con referencia (motorway, trunk, primary): se guarda el centro de
  cada tramo y, por ciudad, las referencias con algún tramo a < 3 km del centro;
- línea de costa (natural=coastline) con geometría: costa a < 5 km.
Solo con costa a < 5 km se puede hablar de salitre; si no, nada de «clima
costero».
Salida: cache/paso_vias.json
"""
import json
import time

from comun import CACHE, cargar, guardar, haversine_km, http_post, q

SRV = "https://overpass-api.de/api/interpreter"
Q_VIAS = """[out:json][timeout:600];area["ISO3166-1"="ES"][admin_level=2]->.es;
way[highway~"^(motorway|trunk|primary)$"][ref](area.es);out tags center qt;"""
# Costa: Natural Earth 10m (dominio público). Toda la costa de España por
# Overpass da 504; para «¿hay mar a menos de 5 km?» basta esta escala.
NE_COSTA = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_coastline.geojson"


def bloque(nombre, query):
    f = CACHE / nombre
    if f.exists() and f.stat().st_size > 1000:
        return json.loads(f.read_text())
    for k in range(5):
        try:
            data = http_post(SRV, ("data=" + q(query)).encode(), {"Content-Type": "application/x-www-form-urlencoded"}, timeout=900)
            f.write_bytes(data)
            return json.loads(data)
        except Exception as e:  # noqa: BLE001
            print("reintento", nombre, e, flush=True)
            time.sleep(60 * (k + 1))
    raise SystemExit(f"Overpass no responde para {nombre}")


def main():
    base = cargar("paso_base.json")
    geo = cargar("paso_geo.json")
    vias = bloque("ovp_vias_es.json", Q_VIAS)["elements"]
    tramos = [(e["center"]["lat"], e["center"]["lon"], e["tags"]) for e in vias if e.get("center")]
    from comun import http_get
    ne = json.loads(http_get(NE_COSTA, "ne_10m_coastline.geojson", timeout=180))
    pts_costa = []
    for f in ne["features"]:
        g = f["geometry"]
        lineas = g["coordinates"] if g["type"] == "MultiLineString" else [g["coordinates"]]
        for ln in lineas:
            # densifica tramos largos para no saltarse la costa entre vértices
            for (x1, y1), (x2, y2) in zip(ln, ln[1:]):
                if 26 < y1 < 45 and -19 < x1 < 5:
                    n = max(1, int(max(abs(x2 - x1), abs(y2 - y1)) / 0.01))
                    pts_costa += [(y1 + (y2 - y1) * k / n, x1 + (x2 - x1) * k / n) for k in range(n)]
    out = {}
    for s, c in base.items():
        g = geo.get(s, {})
        lat, lng = g.get("lat", c["lat"]), g.get("lng", c["lng"])
        refs = {}
        for la, lo, tg in tramos:
            if abs(la - lat) > 0.04 or abs(lo - lng) > 0.05:
                continue
            d = haversine_km(lat, lng, la, lo)
            if d > 3:
                continue
            for ref in (tg.get("ref") or "").split(";"):
                ref = ref.strip()
                if ref and (ref not in refs or d < refs[ref]["km"]):
                    refs[ref] = {"ref": ref, "tipo": tg.get("highway"), "km": round(d, 1)}
        dc = min((haversine_km(lat, lng, la, lo) for la, lo in pts_costa
                  if abs(la - lat) < 0.1 and abs(lo - lng) < 0.13), default=None)
        out[s] = {
            "vias": sorted(refs.values(), key=lambda v: (v["km"], v["ref"])),
            "costa_km": round(dc, 1) if dc is not None else None,
            "costa_5km": dc is not None and dc <= 5,
            "fuente": "Vías: OpenStreetMap (Overpass API), tramos con referencia a < 3 km del centro. Costa: Natural Earth 10m",
        }
    guardar("paso_vias.json", out)
    print(f"vías: {sum(1 for v in out.values() if v['vias'])}/{len(out)}; costa a <5 km: {sum(1 for v in out.values() if v['costa_5km'])}")


if __name__ == "__main__":
    main()
