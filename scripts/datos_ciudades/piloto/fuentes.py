"""Fuentes reutilizables para los bloques `datos` y `fuentes` del contenido local.

`F.x`  → dict {fuente, url} para un dato de la ficha (se expande con **F.x)
`F.x_f` → dict {texto, url} para la lista «Fuentes de esta página»
"""


class _F:
    ine = {"fuente": "INE, padrón", "url": "https://www.ine.es/jaxiT3/Tabla.htm?t=29005"}
    ine_f = {"texto": "INE, padrón municipal", "url": "https://www.ine.es/jaxiT3/Tabla.htm?t=29005"}
    cam_parque = {"fuente": "Comunidad de Madrid / DGT", "url": "https://datos.comunidad.madrid/catalogo/dataset/parque_vehiculos_por_tipo"}
    cam_parque_f = {"texto": "Comunidad de Madrid, parque de vehículos (DGT)", "url": "https://datos.comunidad.madrid/catalogo/dataset/parque_vehiculos_por_tipo"}
    itv_madrid = {"fuente": "Comunidad de Madrid", "url": "https://www.comunidad.madrid/servicios/consumo/inspeccion-tecnica-vehiculos-itv"}
    itv_madrid_f = {"texto": "Comunidad de Madrid, estaciones ITV", "url": "https://www.comunidad.madrid/servicios/consumo/inspeccion-tecnica-vehiculos-itv"}
    itv_cat = {"fuente": "Generalitat de Catalunya", "url": "https://analisi.transparenciacatalunya.cat/d/7dyp-y4dd"}
    itv_cat_f = {"texto": "Generalitat, estacions ITV", "url": "https://analisi.transparenciacatalunya.cat/d/7dyp-y4dd"}
    itv_aragon = {"fuente": "Gobierno de Aragón", "url": "https://www.aragon.es/itv/directorio-de-estaciones"}
    itv_aragon_f = {"texto": "Gobierno de Aragón, estaciones ITV", "url": "https://www.aragon.es/itv/directorio-de-estaciones"}
    bmw = {"fuente": "Localizador de bmw.es", "url": "https://www.bmw.es/es/topics/accesorios-servicios/bmw-service/listado-talleres.html"}
    bmw_f = {"texto": "bmw.es, talleres oficiales", "url": "https://www.bmw.es/es/topics/accesorios-servicios/bmw-service/listado-talleres.html"}
    osrm = {"fuente": "OpenStreetMap (OSRM)", "url": "https://www.openstreetmap.org/"}
    osrm_f = {"texto": "OpenStreetMap (distancias, OSRM)", "url": "https://www.openstreetmap.org/"}
    cartociudad = {"fuente": "CartoCiudad (IGN)", "url": "https://www.cartociudad.es/"}
    cartociudad_f = {"texto": "CartoCiudad (IGN)", "url": "https://www.cartociudad.es/"}
    copernicus = {"fuente": "MDT Copernicus", "url": "https://open-meteo.com/en/docs/elevation-api"}
    rd920_f = {"texto": "RD 920/2017 (ITV)", "url": "https://www.boe.es/eli/es/rd/2017/10/23/920"}
    r461_f = {"texto": "Reglamento (UE) 461/2010", "url": "https://eur-lex.europa.eu/eli/reg/2010/461/oj"}
    dasercars_madrid_f = {"texto": "Dasercars Madrid", "url": "https://www.bmw-taller.es/taller-bmw-madrid/"}
    dasercars_bcn_f = {"texto": "Dasercars Barcelona", "url": "https://www.bmw-taller.es/taller-bmw-barcelona/"}

    @staticmethod
    def idescat(idm: str) -> dict:
        return {"fuente": "Idescat", "url": f"https://www.idescat.cat/emex/?id={idm}&lang=es"}

    @staticmethod
    def idescat_f(idm: str) -> dict:
        return {"texto": "Idescat, el municipio en cifras", "url": f"https://www.idescat.cat/emex/?id={idm}&lang=es"}


F = _F()
