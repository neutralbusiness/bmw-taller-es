"""Paso 1 — lista base: ciudades del repo + estado y código INE del panel.

Requiere las variables del panel:
  cd ~/Sites/neutralb-panel && set -a && . ./.env.local && set +a
Salida: cache/paso_base.json  {slug: {...}}
"""
import json
import os

from comun import INE_CORRECCIONES, NO_MUNICIPIO, ciudades_repo, guardar, http_get, socio_para

NETWORK_ID = "bd619acd-48fd-4068-b6f4-e072052f99c1"  # networks.slug = bmw-taller


def panel():
    url = os.environ.get("NEXT_PUBLIC_SUPABASE_URL") or os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not (url and key):
        raise SystemExit("Faltan NEXT_PUBLIC_SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY (carga .env.local del panel)")
    h = {"apikey": key, "Authorization": f"Bearer {key}"}
    filas = []
    for off in range(0, 5000, 1000):
        u = (f"{url}/rest/v1/network_sites?network_id=eq.{NETWORK_ID}"
             "&select=enabled,custom_phone,gsc_impressions_28d,gsc_clicks_28d,city_class,"
             "network_cities(slug,name,province,ccaa,ine_code,population,lat,lng)"
             f"&offset={off}&limit=1000")
        lote = json.loads(http_get(u, headers=h))
        filas += lote
        if len(lote) < 1000:
            break
    out = {}
    for f in filas:
        nc = f.get("network_cities")
        if not nc:
            continue
        # Si hay dos filas para la misma ciudad, manda la activa.
        if nc["slug"] not in out or f.get("enabled"):
            out[nc["slug"]] = f
    # Ciudades del repo sin fila en esta red (capitales con dominio propio
    # antiguo): el código INE sale de network_cities directamente.
    cs = json.loads(http_get(f"{url}/rest/v1/network_cities?select=slug,ine_code,lat,lng&limit=20000", headers=h))
    return out, {c["slug"]: c for c in cs}


def main():
    p, todas = panel()
    base = {}
    for c in ciudades_repo():
        s = c["slug"]
        f = p.get(s) or {}
        nc = f.get("network_cities") or {}
        base[s] = {
            "slug": s,
            "nombre": c["name"],
            "provincia": c["province"],
            "ccaa": c["ccaa"],
            "ine": INE_CORRECCIONES.get(s) or nc.get("ine_code") or (todas.get(s) or {}).get("ine_code"),
            "tipo": NO_MUNICIPIO[s][0] if s in NO_MUNICIPIO else "municipio",
            "pertenece_a": NO_MUNICIPIO[s][1] if s in NO_MUNICIPIO else None,
            "lat": c.get("lat") or nc.get("lat"),
            "lng": c.get("lng") or nc.get("lng"),
            "activa_panel": bool(f.get("enabled")),
            "telefono": ((c.get("tenant") or {}).get("phone")) or None,
            "socio": socio_para(c),
            "clase": f.get("city_class"),
        }
    guardar("paso_base.json", base)
    sin_ine = [s for s, v in base.items() if not v["ine"]]
    print(f"{len(base)} ciudades; activas en panel: {sum(v['activa_panel'] for v in base.values())}; sin INE: {sin_ine}")


if __name__ == "__main__":
    main()
