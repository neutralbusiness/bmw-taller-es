"""Paso 4 — red oficial BMW en España (localizador de concesionarios de bmw.es).

Se usa el mismo servicio que alimenta el buscador de concesionarios de
https://www.bmw.es (c2b-localsearch). Solo se guardan puntos con taller de
servicio oficial: rama de distribución "T" (las fichas solo-taller llevan
dominio *.tallerautorizadobmw.es, lo que confirma el significado).
El texto de la web NUNCA desprestigia al servicio oficial: se cita como
referencia («el servicio oficial más cercano está en X, a N km»).
Salida: cache/bmw_oficial.json (lista)
"""
import json

from comun import guardar, http_get

URL = ("https://c2b-services.bmw.com/c2b-localsearch/services/api/v4/clients/BMWSTAGE2_DLO/-/pois"
       "?brand=BMW_BMWM&cached=off&category=BM&country=ES&language=es&lat=40.4&lng=-3.7"
       "&maxResults=700&showAll=true&unit=km")
FUENTE = "Localizador oficial de concesionarios BMW España (bmw.es), consultado {fecha}"


def main():
    import datetime
    d = json.loads(http_get(URL, "bmw_locator.json", timeout=90))
    pois = d["data"]["pois"]
    out = []
    for p in pois:
        a = p.get("attributes") or {}
        if "T" not in (a.get("distributionBranches") or []):
            continue
        out.append({
            "nombre": (a.get("nicknameLocal") or p["name"]).strip(),
            "razon_social": p["name"].strip(),
            "direccion": p["street"].strip(),
            "cp": p["postalCode"],
            "municipio": p["city"],
            "lat": p["lat"], "lng": p["lng"],
            "web": a.get("homepage"),
            "solo_taller": a.get("distributionBranches") == ["T"],
        })
    guardar("bmw_oficial.json", {"fuente": FUENTE.format(fecha=datetime.date.today().isoformat()), "puntos": out})
    print(f"puntos BMW con servicio oficial: {len(out)} de {len(pois)}")


if __name__ == "__main__":
    main()
