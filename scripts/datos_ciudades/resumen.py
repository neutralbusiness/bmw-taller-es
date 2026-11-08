"""Imprime un resumen legible de datos/<slug>.json para redactar (uso: python3 resumen.py slug...)."""
import json, sys
from comun import DATOS
for s in sys.argv[1:]:
    d = json.loads((DATOS / f"{s}.json").read_text())
    p = d["poblacion"]; t = d["taller_que_atiende"]; b = d["bmw_servicio_oficial_mas_cercano"] or {}
    print(f"=== {d['nombre']} ({s}) · {d['provincia']} · {d['tipo']}{' de '+d['pertenece_a'] if d['pertenece_a'] else ''} · comarca {d['comarca']} · capital {d['capital_provincia']}")
    print(f" población {p.get('valor')} ({p.get('anio')}) · hace 10: {p.get('valor_hace_10')} ({p.get('variacion_10_pct')} %) · sup {(d['superficie_km2'] or {}).get('valor')} km² · dens {d['densidad_hab_km2']} · alt {d['altitud_m']['valor']} m")
    if d["turismos"]: print(f" turismos {d['turismos']['valor']} ({d['turismos']['anio']}) · {d['turismos']['por_1000_hab']}/1000 hab")
    print(f" taller: {t.get('nombre')} {t.get('municipio')} · {t.get('km_carretera')} km carretera / {t.get('km_linea_recta')} línea · vías {t.get('vias_de_la_ruta')}")
    print(f" BMW oficial: {b.get('nombre')} | {b.get('razon_social')} | {b.get('direccion')} {b.get('municipio')} · {b.get('km_carretera')} km · solo taller {b.get('solo_taller')}")
    for e in d["itv"]["en_el_municipio"]: print(f" ITV mun: {e['nombre']} | {e.get('direccion')} | oficial {e['oficial']}")
    c = d["itv"]["mas_cercana"]
    if c: print(f" ITV cercana: {c['nombre']} | {c.get('direccion')} | {c.get('municipio')} · {c.get('km_carretera')} km · oficial {c['oficial']}")
    print(f" vías <3km: {[v['ref'] for v in d['vias_cercanas']]} · costa {d['costa']}")
    g = (json.loads((DATOS.parent / "cache" / "paso_gsc.json").read_text()).get(s) if (DATOS.parent / "cache" / "paso_gsc.json").exists() else None) or {"imp_mes": "?", "clics_mes": "?", "imp_90d": "?", "clics_90d": "?", "pos_media_90d": "?", "consultas": []}
    print(f" GSC mes {g['imp_mes']} imp/{g['clics_mes']} clics · 90d {g['imp_90d']}/{g['clics_90d']} pos {g['pos_media_90d']}")
    print("  consultas:", "; ".join(f"{q['q']} ({q['imp']})" for q in g["consultas"][:12]))
    print(" cercanas:", ", ".join(f"{c['nombre']} {c['km_linea_recta']}" for c in d["cercanas_red"]))
    print(" title actual:", d["pagina_actual"]["metaTitle"])
