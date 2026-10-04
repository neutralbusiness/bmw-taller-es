"""Paso 8 — vías de acceso y costa (OpenStreetMap vía Overpass, en bloque).

- carreteras con referencia (motorway, trunk, primary, secondary) CON SU
  GEOMETRÍA, en consultas por lotes de recuadros alrededor de cada ciudad;
  por ciudad, las referencias con algún punto del trazado a < 3 km del centro.
  (Antes se usaba solo el centro de cada tramo de OSM: un tramo largo que
  pasa por el pueblo tiene el centro lejos, y 161 de 575 ciudades salían sin
  ninguna carretera —Castellar del Vallès, Corbera, Valdetorres, el Pont de
  Vilomara—. Las secundarias recogen las C- y BV- catalanas y las M- de
  segundo orden.)
- línea de costa (natural=coastline) con geometría: costa a < 5 km.
Solo con costa a < 5 km se puede hablar de salitre; si no, nada de «clima
costero».
Salida: cache/paso_vias.json
"""
import json
import time

from comun import CACHE, cargar, guardar, haversine_km, http_post, q

SRV = "https://overpass-api.de/api/interpreter"
TIPOS = "^(motorway|trunk|primary|secondary)$"
LOTE = 60
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


def origen(s, c, geo, nucleo):
    nu = nucleo.get(s) or {}
    if nu.get("usar_como_origen"):  # mismo criterio que p07
        return nu["lat"], nu["lng"]
    g = geo.get(s, {})
    return g.get("lat", c["lat"]), g.get("lng", c["lng"])


def dist_segmento(lat, lng, a, b):
    """km del punto al segmento a-b (proyección equirrectangular local)."""
    import math
    kx, ky = 111.32 * math.cos(math.radians(lat)), 110.57
    ax, ay = (a[1] - lng) * kx, (a[0] - lat) * ky
    bx, by = (b[1] - lng) * kx, (b[0] - lat) * ky
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, -(ax * dx + ay * dy) / L))
    return math.hypot(ax + t * dx, ay + t * dy)


def main():
    base = cargar("paso_base.json")
    geo = cargar("paso_geo.json")
    nucleo = cargar("paso_nucleo.json", {}) or {}
    puntos = {s: origen(s, c, geo, nucleo) for s, c in base.items()}
    slugs = sorted(puntos)
    tramos = {}
    for i in range(0, len(slugs), LOTE):
        cajas = "".join(f'way[highway~"{TIPOS}"][ref]({la - 0.035},{lo - 0.045},{la + 0.035},{lo + 0.045});'
                        for la, lo in (puntos[x] for x in slugs[i:i + LOTE]))
        d = bloque(f"ovp_vias_geom_{i // LOTE:02d}.json", f"[out:json][timeout:600];({cajas});out tags geom qt;")
        for e in d["elements"]:
            if e.get("geometry"):
                tramos[e["id"]] = ([(p["lat"], p["lon"]) for p in e["geometry"]], e["tags"])
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
        lat, lng = puntos[s]
        refs = {}
        for pts, tg in tramos.values():
            if all(abs(la - lat) > 0.04 or abs(lo - lng) > 0.05 for la, lo in pts):
                continue
            d = min(dist_segmento(lat, lng, a, b) for a, b in zip(pts, pts[1:] or pts))
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
            "fuente": "Vías: OpenStreetMap (Overpass API), carreteras con referencia (autopista, autovía, nacional/primaria, secundaria) cuyo trazado pasa a < 3 km del centro. Costa: Natural Earth 10m",
        }
    guardar("paso_vias.json", out)
    print(f"vías: {sum(1 for v in out.values() if v['vias'])}/{len(out)}; costa a <5 km: {sum(1 for v in out.values() if v['costa_5km'])}")


if __name__ == "__main__":
    main()
