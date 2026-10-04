"""Paso 4 — red oficial BMW en España (localizador de concesionarios de bmw.es).

Se usa el mismo servicio que alimenta el buscador de concesionarios de
https://www.bmw.es (c2b-localsearch). Solo se guardan puntos con taller de
servicio oficial: rama de distribución "T" (las fichas solo-taller llevan
dominio *.tallerautorizadobmw.es, lo que confirma el significado).
Filtros (04-oct-2026, tras la revisión de las tandas 7-12):
- Fuera de España: el localizador de bmw.es incluye Pyrénées Motors (Sant
  Julià de Lòria, Andorra) con país «ES» y CP 00600. Se descarta todo CP que
  no sea español (01-52) o que caiga en Andorra.
- Centros de ocasión (`outletTypes` = UC, razón social con «Vehículo de
  Ocasión Certificado»): el localizador les da rama «T», pero no todos tienen
  taller. Solo cuentan como servicio oficial los comprobados en la web del
  concesionario (VERIFICADOS_UC); el resto se descarta. AutoPremier tiene en
  Alcalá dos puntos distintos: Vía Complutense 131 (concesionario con taller,
  outlet FU) y C/ Argentina 7, P. I. La Garena (centro de vehículos de ocasión
  BMW Premium Selection, sin taller acreditado): el segundo queda fuera.
- La coletilla «Vehículo de Ocasión Certificado» se quita de la razón social.
- Topónimos con la forma oficial (el localizador usa «Tárrega», «Terrasa»,
  «Castellar del Vallés», «Figueras», «Lérida»…).
El texto de la web NUNCA desprestigia al servicio oficial: se cita como
referencia («el servicio oficial más cercano está en X, a N km»).
Salida: cache/bmw_oficial.json (lista)
"""
import json
import re

from comun import guardar, http_get

URL = ("https://c2b-services.bmw.com/c2b-localsearch/services/api/v4/clients/BMWSTAGE2_DLO/-/pois"
       "?brand=BMW_BMWM&cached=off&category=BM&country=ES&language=es&lat=40.4&lng=-3.7"
       "&maxResults=700&showAll=true&unit=km")
FUENTE = "Localizador oficial de concesionarios BMW España (bmw.es), consultado {fecha}"


# Centros de ocasión (outlet UC) con rama «T»: solo cuentan los que tienen taller
# comprobado en fuente pública (comprobación 04-oct-2026). El resto se descarta.
VERIFICADOS_UC = {
    ("51827", "2"): "BYmyCAR Madrid (Algete): la instalación de ocasión y el taller autorizado se trasladaron de "
                    "Alcalá a Algete; horario de taller propio (bymycar.madrid, noticia «Algete»)",
    ("08552", "1"): "AutoPremier Guadalajara (Paseo de la Estación 23): concesionario con taller y horario de taller propio",
    ("39200", "3"): "Unicars Ponent Tàrrega: «talleres oficiales en Lleida y Tárrega» (grupmibec.com/es/bmw/)",
    ("39349", "2"): "Oliva Motor Tortosa: taller BMW/MINI con correo y horario de taller propios (grupolivamotor.com)",
}
# Comprobados y descartados (centro de ocasión sin taller acreditado):
# - AutoPremier La Garena (C/ Argentina 7, Alcalá): bmwpremiumselection.es la lista como punto de venta
#   de ocasión; el taller de AutoPremier en Alcalá es el de Vía Complutense 131.
# - Movilnorte El Carralero (C/ Fresa 13, Majadahonda): punto de venta BMW Premium Selection; el taller
#   de Movilnorte en Majadahonda es el de Ctra. El Plantío 62.
# Sin comprobar (fuera de la zona de la red): San Rafael Lucena, Canaauto Las Chafiras, Ceres Plasencia y
# Don Benito, Ilbira Motril, Celtamotor Lalín, Marcos Lorca, Benigar Petrer.
TOPONIMOS = {
    "Tárrega": "Tàrrega", "Terrasa": "Terrassa", "Castellar del Vallés": "Castellar del Vallès",
    "Sant Cugat del Vallés": "Sant Cugat del Vallès", "Figueras": "Figueres", "Lérida": "Lleida",
    "L Hospitalet de Llobregat": "L'Hospitalet de Llobregat", "Gerona": "Girona",
}


def topo(s: str) -> str:
    import re
    for a, b in TOPONIMOS.items():
        s = re.sub(rf"(?<![\w]){re.escape(a)}(?![\w])", b, s)
    return s


def es_espana(p) -> bool:
    cp = str(p.get("postalCode") or "")
    if not (len(cp) == 5 and cp.isdigit() and 1 <= int(cp[:2]) <= 52):
        return False
    # Andorra (42,43-42,66 N; 1,41-1,79 E)
    return not (42.42 < p["lat"] < 42.66 and 1.40 < p["lng"] < 1.79)


def main():
    import datetime
    d = json.loads(http_get(URL, "bmw_locator.json", timeout=90))
    pois = d["data"]["pois"]
    out, descartes = [], []
    for p in pois:
        a = p.get("attributes") or {}
        if "T" not in (a.get("distributionBranches") or []):
            continue
        if not es_espana(p):
            descartes.append(f"fuera de España: {p['name']} ({p['city']})")
            continue
        clave = (a.get("distributionPartnerId"), a.get("outletId"))
        verif = None
        if "UC" in (a.get("outletTypes") or []):
            verif = VERIFICADOS_UC.get(clave)
            if not verif:
                descartes.append(f"centro de ocasión sin taller comprobado: {a.get('nicknameLocal')} — {p['street']}, {p['city']}")
                continue
        out.append({
            "nombre": topo((a.get("nicknameLocal") or p["name"]).strip()),
            "razon_social": re.sub(r"\s+AutoPremier$", "", re.sub(r"\s*\(?Veh[ií]culo de Ocasi[oó]n Ce.*$", "", p["name"].strip())).strip(" ,"),
            "direccion": p["street"].strip(),
            "cp": p["postalCode"],
            "municipio": topo(p["city"]),
            "lat": p["lat"], "lng": p["lng"],
            "web": a.get("homepage"),
            "solo_taller": a.get("distributionBranches") == ["T"],
            **({"centro_ocasion_con_taller": verif} if verif else {}),
        })
    guardar("bmw_oficial.json", {"fuente": FUENTE.format(fecha=datetime.date.today().isoformat()), "puntos": out,
                                 "descartados": descartes})
    print(f"puntos BMW con servicio oficial: {len(out)} de {len(pois)}")
    for x in descartes:
        print("  descartado:", x)


if __name__ == "__main__":
    main()
