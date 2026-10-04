"""Paso 9 — búsquedas reales de Google Search Console por subdominio.

Usa el endpoint interno del panel (Bearer $AGENT_RUN_SECRET):
  cd ~/Sites/neutralb-panel && set -a && . ./.env.local && set +a
Guarda, por ciudad: impresiones y clics de los últimos 90 días y del último
mes natural, posición media y las consultas (página+consulta) con impresiones.
Las consultas orientan el contenido; NO se meten como lista de palabras clave.
Salida: cache/paso_gsc.json

Solo cuenta la página de ciudad (la raíz «/» del subdominio). Hasta el
04-oct-2026 se sumaban también las filas de <slug>.bmw-taller.es/blog/ (Cádiz
49 impresiones, Guadalajara 126, Valdeaveruelo 18…), que inflaban las
impresiones de la ciudad y le colgaban consultas de otra página. Ahora el blog
del subdominio va aparte (`imp_blog_90d`, `consultas_blog`) y no decide si una
ciudad «tiene impresiones».

Ojo: que una ciudad tenga de consulta principal la de otro municipio («taller
bmw getafe» en Torrelodones) NO es un fallo de asignación: la URL viene en la
fila de GSC y Google sí mostró esa página (en la posición 90-97, ruido de
ranking). Comprobado el 04-oct-2026 con filtro por consulta.
"""
import datetime as dt
import json
import os
import re

from comun import cargar, guardar, http_post

API = "https://panel.neutralb.es/api/internal/gsc"


def pedir(desde, hasta, dims):
    tok = os.environ.get("AGENT_RUN_SECRET")
    if not tok:
        raise SystemExit("Falta AGENT_RUN_SECRET (carga .env.local del panel)")
    body = json.dumps({"sitio": "sc-domain:bmw-taller.es", "desde": desde, "hasta": hasta,
                       "dimensiones": dims, "limite": 25000}).encode()
    return json.loads(http_post(API, body, {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}))["filas"]


def slug_de(url):
    """(slug, es_pagina_de_ciudad) de una URL de GSC; slug None si no es de un subdominio."""
    m = re.match(r"https?://([a-z0-9-]+)\.bmw-taller\.es(/[^?#]*)?", url)
    if not m or m.group(1) == "www":
        return None, False
    return m.group(1), (m.group(2) or "/") == "/"


def main():
    base = cargar("paso_base.json")
    hoy = dt.date.today()
    hasta = (hoy - dt.timedelta(days=2)).isoformat()
    desde90 = (hoy - dt.timedelta(days=92)).isoformat()
    fin_mes = hoy.replace(day=1) - dt.timedelta(days=1)
    ini_mes = fin_mes.replace(day=1)
    pq = pedir(desde90, hasta, ["page", "query"])
    p90 = pedir(desde90, hasta, ["page"])
    pm = pedir(ini_mes.isoformat(), fin_mes.isoformat(), ["page"])
    out = {s: {"imp_90d": 0, "clics_90d": 0, "imp_mes": 0, "clics_mes": 0, "consultas": [], "_pos": [],
               "imp_blog_90d": 0, "consultas_blog": []} for s in base}
    for r in p90:
        s, ciudad = slug_de(r["keys"][0])
        if s in out and not ciudad:
            out[s]["imp_blog_90d"] += r["impressions"]
        elif s in out:
            out[s]["imp_90d"] += r["impressions"]
            out[s]["clics_90d"] += r["clicks"]
            out[s]["_pos"].append((r["position"], r["impressions"]))
    for r in pm:
        s, ciudad = slug_de(r["keys"][0])
        if s in out and ciudad:
            out[s]["imp_mes"] += r["impressions"]
            out[s]["clics_mes"] += r["clicks"]
    for r in pq:
        s, ciudad = slug_de(r["keys"][0])
        if s in out:
            out[s]["consultas" if ciudad else "consultas_blog"].append({"q": r["keys"][1], "imp": r["impressions"], "clics": r["clicks"],
                                        "pos": round(r["position"], 1), "url": r["keys"][0]})
    for s, v in out.items():
        pos = v.pop("_pos")
        tot = sum(i for _, i in pos)
        v["pos_media_90d"] = round(sum(p * i for p, i in pos) / tot, 1) if tot else None
        v["consultas"].sort(key=lambda x: -x["imp"])
        v["consultas_blog"].sort(key=lambda x: -x["imp"])
        v["periodo_90d"] = f"{desde90}/{hasta}"
        v["periodo_mes"] = f"{ini_mes}/{fin_mes}"
    guardar("paso_gsc.json", out)
    con = sum(1 for v in out.values() if v["imp_mes"] > 0)
    print(f"GSC: {con} ciudades con impresiones en {ini_mes:%m/%Y}; {sum(1 for v in out.values() if v['consultas'])} con consultas visibles (90 d)")


if __name__ == "__main__":
    main()
