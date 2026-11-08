"""Paso 3b — núcleo urbano principal de cada municipio (origen de las rutas).

Las coordenadas de las páginas del repo no siempre caen en el casco urbano:
en Vilassar de Dalt estaban en un camino de la sierra (Camí de la Carena) y
OSRM sacaba la ruta por la montaña, con lo que la ITV «más cercana» salía en
Granollers en vez de Argentona. Aquí se toma de CartoCiudad (IGN) la entidad
de población («poblacion») del municipio con su mismo nombre —o, si no la
hay, la más grande del municipio— y se calcula el centroide de su polígono.
p07 la usa como origen de las rutas cuando el punto del repo está a más de
UMBRAL_KM del centroide del núcleo.
Salida: cache/paso_nucleo.json
"""
import json

from comun import cargar, guardar, haversine_km, http_get, norm, q
from p03_geo import area_km2, dentro, parse_multipolygon

CAND = "https://www.cartociudad.es/geocoder/api/geocoder/candidates?q={q}&limit=30"
FIND = "https://www.cartociudad.es/geocoder/api/geocoder/find?type=poblacion&id={id}&q=x"
UMBRAL_KM = 1.0


def centroide(ring):
    # centroide de área (fórmula del polígono) en grados; suficiente a esta escala
    a = cx = cy = 0.0
    for i in range(len(ring)):
        x1, y1 = ring[i - 1]
        x2, y2 = ring[i]
        f = x1 * y2 - x2 * y1
        a += f
        cx += (x1 + x2) * f
        cy += (y1 + y2) * f
    if abs(a) < 1e-14:
        return sum(p[1] for p in ring) / len(ring), sum(p[0] for p in ring) / len(ring)
    return cy / (3 * a), cx / (3 * a)


def nucleo(nombre, ine5):
    cands = json.loads(http_get(CAND.format(q=q(nombre)), f"cc_pob_c_{ine5}.json", timeout=60))
    pobs = [c for c in cands if c.get("type") == "poblacion" and norm(c.get("muni", "")) == norm(nombre)]
    if not pobs:
        return None
    # preferencia: mismo nombre que el municipio
    pobs.sort(key=lambda c: 0 if norm(c.get("address", "").split(",")[0]) == norm(nombre) else 1)
    mejor = None
    for c in pobs[:3]:
        d = json.loads(http_get(FIND.format(id=c["id"]), f"cc_pob_{c['id']}.json", timeout=60))
        if str(d.get("muniCode", "")).zfill(5) != ine5:
            continue
        rings = [p[0] for p in parse_multipolygon(d["geom"])]
        r = max(rings, key=area_km2)
        lat, lng = centroide(r)
        cand = {"lat": round(lat, 5), "lng": round(lng, 5), "nombre": d.get("poblacion") or d.get("address"),
                "area_km2": round(area_km2(r), 2), "id": c["id"], "_rings": rings}
        if norm(cand["nombre"] or "") == norm(nombre):
            return cand
        if not mejor or cand["area_km2"] > mejor["area_km2"]:
            mejor = cand
    return mejor


def main():
    base = cargar("paso_base.json")
    geo = cargar("paso_geo.json")
    out = cargar("paso_nucleo.json", {}) or {}
    for s, c in base.items():
        if s in out or c.get("tipo") != "municipio":
            continue
        try:
            n = nucleo(c["nombre"], str(c["ine"]).zfill(5))
        except Exception as e:  # noqa: BLE001
            n = {"error": str(e)[:120]}
        if n and "lat" in n:
            g = geo.get(s, {})
            la, lo = g.get("lat", c["lat"]), g.get("lng", c["lng"])
            n["km_desde_punto_repo"] = round(haversine_km(la, lo, n["lat"], n["lng"]), 2)
            n["punto_repo_en_nucleo"] = any(dentro(lo, la, r) for r in n.pop("_rings"))
            n["mismo_nombre"] = norm(n["nombre"] or "") == norm(c["nombre"])
            # se usa como origen de rutas solo si el punto del repo está fuera
            # del casco, a más de UMBRAL_KM, y el núcleo es el que da nombre
            # al municipio (si no, no hay certeza de cuál es «el pueblo»)
            n["usar_como_origen"] = (not n["punto_repo_en_nucleo"]) and n["km_desde_punto_repo"] > UMBRAL_KM and n["mismo_nombre"]
        out[s] = n
    guardar("paso_nucleo.json", out)
    lejos = sorted(((v["km_desde_punto_repo"], s) for s, v in out.items() if v and v.get("usar_como_origen")), reverse=True)
    print(f"núcleos: {sum(1 for v in out.values() if v and 'lat' in v)} de {len(out)}; origen corregido al núcleo (punto del repo fuera del casco y a > {UMBRAL_KM} km): {len(lejos)}")
    for k, s in lejos:
        print(f"  {s}: {k} km")


if __name__ == "__main__":
    main()
