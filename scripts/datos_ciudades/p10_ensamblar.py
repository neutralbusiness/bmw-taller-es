"""Paso 10 — ensambla un fichero de datos verificados por ciudad.

Entrada: cache/paso_*.json (pasos 1-9) + src/content/cities/*.json.
Salida:
  datos/<slug>.json   — todos los datos de la ciudad con su fuente
  datos/_indice.csv   — una fila por ciudad con perfil y prioridad de redacción
  COBERTURA.md        — cobertura de cada campo (se regenera siempre)
Los agentes de redacción leen SOLO datos/<slug>.json: lo que no está ahí, no
existe para el texto.
"""
import csv
import datetime as dt
import json

from comun import DATOS, RAIZ, SOCIOS, cargar, ciudades_repo, haversine_km

CAPITALES = {
    "a-coruna", "albacete", "alicante", "almeria", "badajoz", "barcelona", "bilbao", "burgos", "cadiz",
    "castello-de-la-plana", "cordoba", "gasteiz-vitoria", "girona", "granada", "guadalajara", "huelva", "jaen",
    "las-palmas-de-gran-canaria", "leon", "lleida", "logrono", "madrid", "malaga", "murcia", "oviedo", "palma",
    "pamplona", "salamanca", "san-sebastian", "santa-cruz-de-tenerife", "santander", "segovia", "sevilla",
    "tarragona", "toledo", "valencia", "valladolid", "zaragoza",
}


def tamano(p):
    if p is None:
        return "desconocido"
    if p >= 200000:
        return "gran ciudad (200.000+)"
    if p >= 50000:
        return "ciudad (50.000-200.000)"
    if p >= 10000:
        return "municipio medio (10.000-50.000)"
    if p >= 1000:
        return "pueblo (1.000-10.000)"
    return "pueblo pequeño (<1.000)"


def banda_km(k):
    if k is None:
        return "sin taller con dirección"
    if k < 15:
        return "muy cerca (<15 km)"
    if k < 40:
        return "cerca (15-40 km)"
    if k < 80:
        return "media distancia (40-80 km)"
    return "lejos (80+ km)"


def main():
    base = cargar("paso_base.json")
    ine = cargar("paso_ine.json", {})
    geo = cargar("paso_geo.json", {})
    reg = cargar("paso_regional.json", {})
    rut = cargar("paso_rutas.json", {})
    vias = cargar("paso_vias.json", {})
    gsc = cargar("paso_gsc.json", {})
    bmwf = (cargar("bmw_oficial.json", {}) or {}).get("fuente")
    repo = {c["slug"]: c for c in ciudades_repo()}
    coords = {s: (geo.get(s, {}).get("lat", c["lat"]), geo.get(s, {}).get("lng", c["lng"])) for s, c in base.items()}
    filas = []
    for s, c in base.items():
        rc = repo[s]
        p, g, r, ru, v, gs = ine.get(s, {}), geo.get(s, {}), reg.get(s, {}), rut.get(s, {}), vias.get(s, {}), gsc.get(s, {})
        es_mun = c.get("tipo") == "municipio"
        pob = p.get("poblacion") if es_mun else None
        sup = r.get("superficie_km2") or g.get("superficie_km2")
        soc = SOCIOS.get(c["socio"] or "", {})
        d = {
            "slug": s,
            "nombre": c["nombre"],
            "tipo": c.get("tipo"),
            "pertenece_a": c.get("pertenece_a"),
            "provincia": c["provincia"],
            "ccaa": c["ccaa"],
            "comarca": r.get("comarca"),
            "capital_provincia": s in CAPITALES,
            "activa_panel": c["activa_panel"],
            "telefono_pagina": c["telefono"],
            "codigo_ine": c["ine"],
            "coordenadas": {"lat": coords[s][0], "lng": coords[s][1],
                            "comprobadas": g.get("coord_en_municipio"), "fuente": g.get("fuente")},
            "poblacion": ({"valor": pob, "anio": p.get("anio"), "valor_hace_10": p.get("poblacion_10"),
                           "anio_hace_10": p.get("anio_10"),
                           "variacion_10_pct": round((pob - p["poblacion_10"]) / p["poblacion_10"] * 100, 1) if pob and p.get("poblacion_10") else None,
                           "fuente": p.get("fuente")} if pob else
                          {"valor": None, "nota": f"No es municipio: la cifra del INE sería la de {c.get('pertenece_a')}. No publicar población.",
                           "fuente": p.get("fuente")}),
            "superficie_km2": {"valor": sup if es_mun else None, "fuente": r.get("fuente") or g.get("fuente")} if sup else None,
            "densidad_hab_km2": round(pob / sup) if pob and sup and es_mun else None,
            "altitud_m": {"valor": r.get("altitud_m") if r.get("altitud_m") is not None else g.get("altitud_m"),
                          "fuente": r.get("fuente") if r.get("altitud_m") is not None else g.get("altitud_fuente")},
            "turismos": ({"valor": r["turismos"], "anio": r.get("turismos_anio"),
                          "por_1000_hab": round(r["turismos"] / pob * 1000) if pob else None,
                          "fuente": r.get("turismos_fuente")} if r.get("turismos") and es_mun else None),
            "taller_que_atiende": ({"id": c["socio"], "nombre": soc.get("nombre"), "direccion": soc.get("direccion"),
                                    "cp": soc.get("cp"), "municipio": soc.get("municipio"), "horario": soc.get("horario"),
                                    "km_carretera": (ru.get("socio") or {}).get("km_carretera"),
                                    "km_linea_recta": (ru.get("socio") or {}).get("km_linea"),
                                    "vias_de_la_ruta": (ru.get("socio") or {}).get("vias_ruta"),
                                    "fuente": soc.get("fuente")} if c["socio"] else
                                   {"id": None, "nota": "Sin taller de la red en la zona: no afirmar que hay taller en la ciudad. Pendiente de decisión de Martin."}),
            "itv": {"en_el_municipio": ru.get("itv_en_municipio") or [], "mas_cercana": ru.get("itv_cercana")},
            "bmw_servicio_oficial_mas_cercano": ({**ru["bmw_oficial"], "fuente": bmwf} if ru.get("bmw_oficial") else None),
            "vias_cercanas": v.get("vias") or [],
            "vias_fuente": v.get("fuente"),
            "costa": {"km": v.get("costa_km"), "a_menos_de_5km": v.get("costa_5km")} if v else None,
            "distancias_fuente": ru.get("fuente"),
            "cercanas_red": [
                {"slug": o, "nombre": base[o]["nombre"], "km_linea_recta": round(haversine_km(*coords[s], *coords[o]), 1)}
                for o in sorted((o for o in base if o != s), key=lambda o: haversine_km(*coords[s], *coords[o]))[:8]
            ],
            "pagina_actual": {"metaTitle": rc.get("metaTitle"), "tiene_contenido_v3": bool(rc.get("local")),
                              "poblacion_en_json": rc.get("population")},
            "generado": dt.date.today().isoformat(),
        }
        alt = d["altitud_m"]["valor"]
        d["perfil"] = {
            "tamano": tamano(pob) if es_mun else c.get("tipo"),
            "capital_provincia": s in CAPITALES,
            "costa": bool(v.get("costa_5km")),
            "altitud": ("montaña (>800 m)" if alt and alt > 800 else "interior alto (600-800 m)" if alt and alt > 600 else "baja (<600 m)") if alt is not None else None,
            "distancia_taller": banda_km(d["taller_que_atiende"].get("km_carretera")),
            "itv_en_municipio": bool(d["itv"]["en_el_municipio"]),
            # El tráfico de Search Console NO se escribe en datos/ (repo público):
            # se consulta en cache/paso_gsc.json con resumen.py.
        }
        (DATOS / f"{s}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), "utf-8")
        filas.append(d)

    # Prioridad de redacción: activas primero; dentro, sin impresiones y más población primero
    def prio(d):
        imp = (gsc.get(d["slug"]) or {}).get("imp_mes") or 0
        return (not d["activa_panel"], imp > 0, -(d["poblacion"].get("valor") or 0))
    filas.sort(key=prio)
    with open(DATOS / "_indice.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["orden", "slug", "nombre", "provincia", "activa_panel", "tipo", "poblacion", "tamano", "costa", "altitud",
                    "distancia_taller", "km_taller", "itv_en_municipio", "v3"])
        for i, d in enumerate(filas, 1):
            w.writerow([i, d["slug"], d["nombre"], d["provincia"], d["activa_panel"], d["tipo"], d["poblacion"].get("valor"),
                        d["perfil"]["tamano"], d["perfil"]["costa"], d["perfil"]["altitud"], d["perfil"]["distancia_taller"],
                        d["taller_que_atiende"].get("km_carretera"), d["perfil"]["itv_en_municipio"],
                        d["pagina_actual"]["tiene_contenido_v3"]])

    # Cobertura
    def cub(nombre, pred, conjunto):
        n = sum(1 for d in conjunto if pred(d))
        return f"| {nombre} | {n}/{len(conjunto)} | {round(100 * n / len(conjunto))} % |"
    act = [d for d in filas if d["activa_panel"]]
    campos = [
        ("Código INE comprobado contra el nombre oficial", lambda d: bool(d["codigo_ine"])),
        ("Población INE (último padrón)", lambda d: bool(d["poblacion"].get("valor"))),
        ("Evolución de población a 10 años", lambda d: d["poblacion"].get("variacion_10_pct") is not None),
        ("Coordenadas dentro del término municipal (CartoCiudad)", lambda d: d["coordenadas"]["comprobadas"] is True),
        ("Superficie", lambda d: bool(d["superficie_km2"] and d["superficie_km2"]["valor"])),
        ("Altitud", lambda d: d["altitud_m"]["valor"] is not None),
        ("Comarca oficial (solo Cataluña)", lambda d: bool(d["comarca"])),
        ("Parque de turismos municipal (DGT vía Idescat / CAM)", lambda d: bool(d["turismos"])),
        ("Taller que atiende con dirección real", lambda d: bool(d["taller_que_atiende"].get("direccion"))),
        ("Distancia por carretera al taller", lambda d: d["taller_que_atiende"].get("km_carretera") is not None),
        ("Vías de la ruta al taller", lambda d: bool(d["taller_que_atiende"].get("vias_de_la_ruta"))),
        ("ITV oficial en el propio municipio", lambda d: any(e.get("oficial") for e in d["itv"]["en_el_municipio"])),
        ("ITV en el municipio o cercana con fuente oficial", lambda d: any(e.get("oficial") for e in d["itv"]["en_el_municipio"]) or bool((d["itv"]["mas_cercana"] or {}).get("oficial"))),
        ("ITV cercana solo en OSM (verificar a mano)", lambda d: not d["itv"]["en_el_municipio"] and bool((d["itv"]["mas_cercana"] or {}).get("verificar"))),
        ("Servicio oficial BMW más cercano (bmw.es)", lambda d: bool(d["bmw_servicio_oficial_mas_cercano"])),
        ("Vías principales a < 3 km (OSM)", lambda d: bool(d["vias_cercanas"])),
        ("Costa a < 5 km", lambda d: bool(d["costa"] and d["costa"]["a_menos_de_5km"])),
        ("Con consultas de Search Console (90 días, en cache/, no versionado)", lambda d: bool((gsc.get(d["slug"]) or {}).get("consultas"))),
    ]
    lin = ["# Cobertura de los datos por ciudad", "",
           f"Generado por `p10_ensamblar.py` el {dt.date.today().isoformat()}. No editar a mano.", "",
           "| Campo | Activas en panel | % | ", "|---|---|---|"]
    lin += [cub(n, f, act) for n, f in campos]
    lin += ["", "| Campo | Todas las del repo (575) | % |", "|---|---|---|"]
    lin += [cub(n, f, filas) for n, f in campos]
    lin += ["", "## Subdominios que no son municipios", ""]
    lin += [f"- `{d['slug']}`: {d['tipo']} de {d['pertenece_a']}" for d in filas if d["tipo"] != "municipio"]
    lin += ["", "## Ciudades sin taller de la red en su zona", "",
            "Activas o publicadas cuyo teléfono es el general y están fuera de Cataluña, zona centro y Zaragoza:", ""]
    lin += [f"- `{d['slug']}` ({d['provincia']}) · activa en panel: {d['activa_panel']}"
            for d in filas if not d["taller_que_atiende"].get("id")]
    (RAIZ / "COBERTURA.md").write_text("\n".join(lin) + "\n", "utf-8")
    print("\n".join(lin[:30]))


if __name__ == "__main__":
    main()
