# Tanda 17: Sant Quirze del Vallès, Malgrat de Mar, Cardedeu, Tordera, Sant Celoni,
# Parets del Vallès, San Lorenzo de El Escorial, Villanueva del Pardillo, Piera,
# Guadarrama, Berga, Canovelles, la Garriga, El Escorial y Arenys de Mar.
# Ninguna ciudad de la tanda está en la lista de exclusiones del coordinador
# (todas son municipio y tienen taller de la red con dirección).
#
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_17
# Las 15 tienen impresiones en GSC (cache/paso_gsc.json): no se tocan ni metaTitle
# ni metaDescription, así que META y TITLES quedan vacíos. El script de abajo
# los aplicaría igual que en las tandas anteriores si algún día se rellenan:
#   python3 scripts/datos_ciudades/tandas/tanda_17.py
import json
import sys
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI.parent / "piloto"))
sys.path.insert(0, str(_AQUI.parent))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
META = {}
TITLES = {}

# ---------------------------------------------------------------- Sant Quirze del Vallès
CIUDADES["sant-quirze-del-valles"] = {
    "h1": "Sant Quirze del Vallès: dos puntos BMW en Sabadell y el especialista a 27,5 km",
    "entradilla": "A menos de cuatro kilómetros de Sant Quirze tienes dos puntos de servicio oficial BMW, los dos en Sabadell. El taller especialista independiente de la red está más lejos, en Sant Joan Despí. Qué hace cada uno y cuándo te conviene uno u otro.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 27.5},
    "secciones": [
        {"id": "que-es-un-especialista", "h2": "Qué quiere decir «taller especializado» aquí",
         "parrafos": [
             "Dasercars no es un taller multimarca que de vez en cuando ve un BMW: trabaja BMW y MINI, con especialidad en los diésel N47, N57, M47, M57, B47 y B57, y está homologado en REDISTA para escape y gases. No es servicio oficial ni lo pretende.",
             "La diferencia con el concesionario es de papel, no de oficio: el servicio oficial tramita la garantía del fabricante y las llamadas a revisión; el especialista independiente hace mantenimiento, diagnosis y reparaciones con el mismo plan de marca, y la diagnosis se presupuesta antes de conectar el equipo."
         ]},
        {"id": "sabadell-a-tres-km", "h2": "Sitjas y Quadis Munich, los dos en Sabadell",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo al centro de Sant Quirze es Sitjas Motor, taller autorizado en la calle Quintana 64 de Sabadell, a 2,4 km por carretera. Quadis Munich, también en Sabadell, queda a 3,2 km: prácticamente lo mismo.",
             "Si BMW te ha escrito por una campaña de revisión, esa cita es con uno de ellos: las campañas del fabricante no salen de la red oficial."
         ]},
        {"id": "c16-b20", "h2": "Hasta Sant Joan Despí por la C-16",
         "parrafos": [
             "La ruta más corta sale por la C-1413a, enlaza con la C-16 y termina por la B-20 hasta el carrer del Tambor del Bruc: 27,5 km por carretera, 18,7 en línea recta. Sant Quirze no forma parte del Área Metropolitana de Barcelona, de modo que la recogida del taller no llega; el coche lo traes tú.",
             "A cambio, la C-58 pasa a medio kilómetro del centro. Un diésel que aquí solo hace recados por el pueblo tiene a mano la autopista para completar de vez en cuando la regeneración del filtro de partículas."
         ]},
        {"id": "itv-can-roqueta", "h2": "La ITV, en Can Roqueta",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sabadell (B24), en el polígono Can Roqueta, a 6,4 km. Sant Quirze tenía 20.209 vecinos en 2025 y 10.708 turismos en 2024 según Idescat a partir de la DGT: 530 por cada 1.000 habitantes, muy por encima de los 281 de Barcelona ciudad."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el taller autorizado BMW de Sabadell?",
         "a": "No. Los puntos oficiales cercanos son Sitjas Motor y Quadis Munich, en Sabadell. Dasercars es un taller independiente en Sant Joan Despí."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "27,5 km por la C-16 y la B-20."},
        {"q": "¿Recogéis el coche en Sant Quirze?",
         "a": "No: la recogida solo cubre el Área Metropolitana de Barcelona, y Sant Quirze queda fuera."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Sabadell (B24), en Can Roqueta, a 6,4 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "20.209 habitantes (+3,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082384")},
        {"etiqueta": "Turismos (2024)", "valor": "10.708 · 530 por cada 1.000 hab.", **F.idescat("082384")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Sitjas Motor (Sabadell) · 2,4 km; Quadis Munich · 3,2 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sabadell (B24) · 6,4 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 27,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082384"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Malgrat de Mar
CIUDADES["malgrat-de-mar"] = {
    "h1": "Malgrat de Mar: un BMW a 1,3 km del mar y a 73 km del taller especialista",
    "entradilla": "En el extremo norte del Maresme, la ITV te queda en Blanes y el servicio oficial BMW más próximo está en Mataró. El taller de la red, en Sant Joan Despí, está a 73,1 km. Lo que conviene saber antes de decidir.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 73.1},
    "secciones": [
        {"id": "mar-al-lado", "h2": "Con la costa a 1,3 km del centro",
         "parrafos": [
             "El centro de Malgrat queda a 1,3 km de la línea de costa. La humedad salina trabaja despacio, pero trabaja: primero en lo que va por debajo del coche (soportes del escape, anclajes, tornillería de la suspensión), después en los discos de freno de un coche que pasa semanas aparcado y, con los años, en los conectores eléctricos expuestos.",
             "Un manguerazo con agua dulce a los bajos al acabar el verano y mirar frenos tras un periodo largo sin mover el coche evitan buena parte de esas averías. Si el BMW tiene un fallo eléctrico que aparece y desaparece, en un coche de costa los conectores son sospechosos antes que las centralitas."
         ]},
        {"id": "blanes-y-mataro", "h2": "ITV en Blanes, servicio oficial en Mataró",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Blanes (G07), en la avinguda de l'Estació 47, a 5,5 km. Para la inspección no hace falta ir hacia Barcelona.",
             "El punto oficial BMW más cercano según bmw.es es Pruna Motor, en la Via Sergia 2 de Mataró, a 35,9 km. Allí van las reparaciones en garantía; las revisiones puedes hacerlas en un taller independiente sin perderla siempre que se respete el plan de mantenimiento, como establece el Reglamento (UE) 461/2010."
         ]},
        {"id": "n-ii-c-32", "h2": "73 kilómetros por la N-II y la C-32",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc de Sant Joan Despí sale por la N-II, sigue por la C-32 a lo largo de la costa y entra por la B-20: 73,1 km por carretera. Malgrat no está en el Área Metropolitana de Barcelona y la recogida del taller no llega aquí.",
             "Con esa distancia, el viaje se justifica para lo que es propio de BMW y no ha tenido arreglo cerca: un diésel N47 o N57 con ruido de distribución, un fallo de AdBlue o una diagnosis que no termina de cerrar."
         ]},
        {"id": "malgrat-cifras", "h2": "19.714 vecinos en 8,8 km²",
         "parrafos": [
             "Malgrat tenía 18.371 habitantes en 2015 y 19.714 en 2025, un 7,3 % más, en un término de solo 8,82 km². Idescat, a partir de la DGT, contaba 8.458 turismos en 2024: 429 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Malgrat?",
         "a": "La estación más próxima por carretera es la de Blanes (G07), en la avinguda de l'Estació 47, a 5,5 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sergia 2 de Mataró, a 35,9 km según bmw.es."},
        {"q": "¿Afecta el mar a mi BMW?",
         "a": "Acelera la corrosión de bajos y anclajes, el óxido en discos de un coche parado y la sulfatación de conectores."},
        {"q": "¿Pasáis a recoger el coche?",
         "a": "No: la recogida del taller solo cubre el Área Metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "19.714 habitantes (+7,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("081108")},
        {"etiqueta": "Turismos (2024)", "valor": "8.458 · 429 por cada 1.000 hab.", **F.idescat("081108")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 1,3 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Blanes (G07) · 5,5 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 73,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081108"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Cardedeu
CIUDADES["cardedeu"] = {
    "h1": "Desde Cardedeu: taller especialista BMW para Barcelona, a 46,9 km por la AP-7",
    "entradilla": "Quien busca un taller BMW «en Barcelona» desde Cardedeu suele acabar en el Baix Llobregat: el taller de la red está en Sant Joan Despí. Antes de hacer los 46,9 km, mira lo que tienes en Granollers.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 46.9},
    "secciones": [
        {"id": "barcelona-no-es-barcelona", "h2": "«Taller BMW Barcelona» no es Barcelona ciudad",
         "parrafos": [
             "Dasercars Barcelona está en el carrer del Tambor del Bruc 3 de Sant Joan Despí, al otro lado de Barcelona viniendo desde el Vallès Oriental. Desde Cardedeu la ruta es BV-5103, AP-7, C-33 y B-20: 46,9 km por carretera y 39,1 en línea recta.",
             "Abre de lunes a viernes de 9:00 a 14:00 y de 15:00 a 18:00, sin sábados. Con ese viaje, lo razonable es dejar el coche por la mañana y volver por la tarde,; no compensa para un trabajo menor. La recogida solo cubre el Área Metropolitana de Barcelona y Cardedeu queda fuera."
         ]},
        {"id": "autorizado-en-granollers", "h2": "Si buscas un taller autorizado",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la carretera C-17, km 19,060, en Granollers: 14 km por carretera. Para una reparación en garantía o un aviso del fabricante es el sitio. Dasercars es independiente: hace mantenimiento, diagnosis y reparación de BMW y MINI, pero no tramita la garantía de la marca."
         ]},
        {"id": "itv-el-congost", "h2": "La ITV, en el polígono El Congost",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Granollers (B18), en la avinguda de Sant Julià, polígono El Congost: 13,5 km por la ruta más corta. Por la vía más rápida son algo más de 15.",
             "Como la ITV y el servicio oficial quedan en la misma ciudad, un mismo viaje a Granollers puede resolver las dos cosas."
         ]},
        {"id": "cardedeu-cifras", "h2": "Un municipio de 19.046 habitantes entre la AP-7 y la C-35",
         "parrafos": [
             "Cardedeu tenía 19.046 vecinos en 2025, un 6,2 % más que en 2015, y 9.182 turismos en 2024 (Idescat, a partir de la DGT): 482 por cada 1.000 habitantes. La AP-7, la C-35 y la C-251 pasan a menos de tres kilómetros del centro, así que el coche puede alternar ciudad y vía rápida sin desvíos, algo que agradecen los diésel con filtro de partículas."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Barcelona ciudad?",
         "a": "No. El taller de la red para la provincia está en Sant Joan Despí, a 46,9 km de Cardedeu."},
        {"q": "¿Cuál es el taller autorizado BMW más cercano a Cardedeu?",
         "a": "Pruna Motor, en la C-17, km 19,060, en Granollers, a 14 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de Granollers (B18), en el polígono El Congost, a 13,5 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "19.046 habitantes (+6,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080462")},
        {"etiqueta": "Turismos (2024)", "valor": "9.182 · 482 por cada 1.000 hab.", **F.idescat("080462")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 14 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 13,5 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 46,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080462"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Tordera
CIUDADES["tordera"] = {
    "h1": "Talleres en Tordera: el especialista BMW queda a 75,8 km y lo oficial, hacia Girona",
    "entradilla": "No tenemos taller en Tordera, y desde aquí casi todo lo relacionado con BMW mira hacia Girona, no hacia Barcelona. Te damos los kilómetros reales para que decidas qué te compensa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 75.8},
    "secciones": [
        {"id": "sin-taller-en-tordera", "h2": "Lo que no encontrarás en Tordera",
         "parrafos": [
             "Si buscabas un taller dentro del municipio, esta página no lo es. El taller especialista de la red es Dasercars Barcelona, en Sant Joan Despí, a 75,8 km por la N-II, la C-32 y la B-20. Para un cambio de pastillas o unos neumáticos, un taller de la zona es la opción sensata.",
             "El viaje tiene sentido para lo específico de BMW: un testigo que vuelve después de borrarlo, una avería electrónica sin diagnóstico claro o el mantenimiento de un diésel B47 o N47 por plan de marca. En ese caso, una llamada previa con modelo, año, kilometraje y síntoma ahorra kilómetros: a veces basta para saber si hay que bajar."
         ]},
        {"id": "salt-no-mataro", "h2": "El servicio oficial más cercano está en Salt",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo a Tordera por carretera es Oliva Motor Girona, en el carrer de Lingen 9-11 de Salt: 34,8 km. Las reparaciones en garantía se resuelven allí, sin pasar por Barcelona."
         ]},
        {"id": "itv-blanes", "h2": "La ITV, en Blanes",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Blanes (G07), en la avinguda de l'Estació 47, a 7,6 km del centro. Aquí la pre-ITV la hará quien te haga el mantenimiento habitual; no es motivo para un viaje largo."
         ]},
        {"id": "termino-grande", "h2": "Casi 84 km² y un 15,9 % más de vecinos",
         "parrafos": [
             "Tordera tiene un término de 83,97 km², grande para el Maresme, y ha pasado de 16.433 habitantes en 2015 a 19.039 en 2025. Idescat, con datos de la DGT, contaba 9.684 turismos en 2024: 509 por cada 1.000 habitantes. La N-II, la C-32, la GI-512 y la GI-600 pasan a menos de tres kilómetros del centro.",
             "En un término así, muchos coches hacen a diario trayectos cortos entre núcleos. Si el tuyo es diésel, vigila los avisos del filtro de partículas: es el tipo de uso que peor lleva."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Tordera?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 75,8 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Oliva Motor Girona, en Salt, a 34,8 km por carretera según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de Blanes (G07), a 7,6 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "19.039 habitantes (+15,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082845")},
        {"etiqueta": "Superficie del término", "valor": "83,97 km²", **F.idescat("082845")},
        {"etiqueta": "Turismos (2024)", "valor": "9.684 · 509 por cada 1.000 hab.", **F.idescat("082845")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Oliva Motor Girona (Salt) · 34,8 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Blanes (G07) · 7,6 km", **F.itv_cat},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082845"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sant Celoni
CIUDADES["sant-celoni"] = {
    "h1": "Sant Celoni: ITV en la carretera de Gualba y especialista BMW a 57,8 km",
    "entradilla": "Sant Celoni tiene ITV propia; el servicio oficial BMW está en Granollers y el taller especialista de la red, en Sant Joan Despí. Si has buscado un «taller BMW Barcelona», esto es lo que hay de verdad y a cuántos kilómetros.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 57.8},
    "secciones": [
        {"id": "itv-gualba", "h2": "La ITV la tienes en casa",
         "parrafos": [
             "El registro de estaciones de la Generalitat incluye una ITV dentro del municipio: la de Sant Celoni (B26), en la carretera de Gualba 41-43, que gestiona TÜV SÜD. Para inspeccionar el coche no hace falta salir del término."
         ]},
        {"id": "lo-que-no-es", "h2": "Ni oficial ni en Barcelona: lo que somos",
         "parrafos": [
             "Dasercars es un taller independiente especializado en BMW y MINI, sin relación con la red oficial ni con talleres de cadena. Su nave de la provincia está en Sant Joan Despí, no en Barcelona ciudad.",
             "El punto oficial BMW más cercano según bmw.es es Pruna Motor, en la carretera C-17, km 19,060, en Granollers: 26,6 km por la ruta más corta. Por la vía más rápida son unos 31,7. Para la garantía del fabricante, ese es el sitio."
         ]},
        {"id": "ap7-c33", "h2": "Por la AP-7 y la C-33 hasta el Baix Llobregat",
         "parrafos": [
             "Desde el centro de Sant Celoni hasta el carrer del Tambor del Bruc hay 57,8 km por carretera: AP-7, C-33 y B-20. Sant Celoni no forma parte del Área Metropolitana de Barcelona, así que la recogida del taller no llega.",
             "Para que el viaje compense, que sea por algo que justifique un especialista: un ruido de cadena en un diésel, un fallo del sistema SCR con la cuenta atrás de AdBlue, un consumo de aceite que no cuadra."
         ]},
        {"id": "sant-celoni-cifras", "h2": "65 km² de término y 8.710 turismos",
         "parrafos": [
             "Sant Celoni tenía 17.317 habitantes en 2015 y 18.977 en 2025, un 9,6 % más. Su término mide 65,23 km² y en 2024 había 8.710 turismos censados según Idescat a partir de la DGT, 459 por cada 1.000 vecinos. La C-35 y la AP-7 pasan a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Sant Celoni?",
         "a": "Sí: la estación B26, en la carretera de Gualba 41-43, según el registro de la Generalitat."},
        {"q": "¿Sois servicio oficial BMW?",
         "a": "No. Somos un taller independiente especializado. El servicio oficial más cercano es Pruna Motor, en Granollers, a 26,6 km."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 57,8 km, en Sant Joan Despí, por la AP-7, la C-33 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "18.977 habitantes (+9,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("082021")},
        {"etiqueta": "Turismos (2024)", "valor": "8.710 · 459 por cada 1.000 hab.", **F.idescat("082021")},
        {"etiqueta": "ITV en el municipio", "valor": "Sant Celoni (B26), ctra. de Gualba 41-43", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 26,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 57,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082021"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Parets del Vallès
CIUDADES["parets-del-valles"] = {
    "h1": "Parets del Vallès: Granollers a 5 km para lo oficial, Sant Joan Despí para el especialista",
    "entradilla": "Desde Parets, la ITV y el servicio oficial BMW están a menos de cinco kilómetros, los dos en Granollers. El taller especialista de la red queda a 33,2 km. Cómo repartir el trabajo entre unos y otro.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 33.2},
    "secciones": [
        {"id": "granollers-al-lado", "h2": "Todo lo oficial, a un paso",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo es Pruna Motor, en la carretera C-17, km 19,060, en Granollers: 4,2 km por carretera. La ITV más cercana en el registro de la Generalitat, también en Granollers: la estación B18, en el polígono El Congost, a 4,9 km.",
             "Con las dos cosas tan cerca, no tiene sentido cruzar Barcelona para una inspección o para una reparación en garantía."
         ]},
        {"id": "donde-encaja-el-especialista", "h2": "Dónde encaja un taller independiente",
         "parrafos": [
             "En el mantenimiento y en las averías fuera de garantía. El Reglamento (UE) 461/2010 permite revisar el coche fuera de la red oficial sin perder la garantía, con una condición: respetar los intervalos y especificaciones del plan de mantenimiento, con aceite y recambios de la homologación correcta.",
             "Dasercars Barcelona está en Sant Joan Despí, a 33,2 km por la BV-1604, la C-17, la C-33 y la B-20 (27,2 en línea recta). Parets no pertenece al Área Metropolitana de Barcelona, así que la recogida del taller no cubre el municipio."
         ]},
        {"id": "parets-cifras", "h2": "La misma población que hace diez años, más de un coche por cada dos vecinos",
         "parrafos": [
             "Parets tenía 18.901 habitantes en 2015 y 18.885 en 2025: prácticamente igual. Lo que sí destaca es el parque: 10.255 turismos en 2024 según Idescat a partir de la DGT, 543 por cada 1.000 habitantes, frente a los 281 de Barcelona ciudad.",
             "Con la C-17, la C-33, la C-35 y la AP-7 a menos de tres kilómetros, muchos de esos coches hacen vía rápida a diario. Es buen uso para un diésel, pero exige vigilar neumáticos y frenos con más frecuencia que el indicador de servicio."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Parets?",
         "a": "Pruna Motor, en la C-17, km 19,060, en Granollers, a 4,2 km."},
        {"q": "¿Pierdo la garantía si hago las revisiones fuera del concesionario?",
         "a": "No, si se respeta el plan de mantenimiento del fabricante."},
        {"q": "¿Recogéis el coche en Parets?",
         "a": "No: la recogida del taller cubre solo el Área Metropolitana de Barcelona."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Granollers (B18), en el polígono El Congost, a 4,9 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "18.885 habitantes (−0,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("081593")},
        {"etiqueta": "Turismos (2024)", "valor": "10.255 · 543 por cada 1.000 hab.", **F.idescat("081593")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 4,2 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 4,9 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 33,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081593"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- San Lorenzo de El Escorial
CIUDADES["san-lorenzo-de-el-escorial"] = {
    "h1": "San Lorenzo de El Escorial: concesionario BMW en Las Rozas, especialista en Alcobendas",
    "entradilla": "A más de mil metros de altitud y sin concesionario BMW en el municipio, lo oficial más cercano está en Las Rozas. Nosotros no somos ese concesionario: somos el taller especialista independiente de Alcobendas, a 56,1 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 56.1},
    "secciones": [
        {"id": "concesionario-mas-cercano", "h2": "El concesionario que buscas está en la A-6",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo es Movilnorte, en la A-6, km 23,100, en Las Rozas: 28,5 km por la ruta más corta. Por la vía más rápida son unos 33,9.",
             "Ese es el sitio para lo que cubre la garantía. Para el mantenimiento, el Reglamento (UE) 461/2010 deja elegir taller: puedes revisar el coche en un independiente sin perder la garantía mientras se siga el plan del fabricante."
         ]},
        {"id": "a-1047-metros", "h2": "Un BMW a 1.047 metros",
         "parrafos": [
             "El centro urbano está a 1.047 m de altitud. Con las heladas, lo primero que falla es una batería cansada, y en un BMW con arranque y parada automático trabaja más que en un coche sencillo; cuando se cambia, hay que registrarla en la centralita para que el sistema de carga la trate como nueva.",
             "Las bajadas largas hacia la A-6 castigan los frenos. El líquido absorbe humedad con el tiempo y pierde punto de ebullición, así que se cambia por fecha, no por kilómetros."
         ]},
        {"id": "ruta-y-recogida", "h2": "56 kilómetros hasta la calle Valgrande",
         "parrafos": [
             "La ruta baja por la M-505 hasta la A-6, toma la M-40 y sale por la A-1 hasta Alcobendas: 56,1 km por carretera, 42,4 en línea recta. La recogida y el vehículo de cortesía, sujetos a disponibilidad, se ofrecen dentro del área metropolitana de Madrid: pregunta antes si tu dirección entra, no lo des por hecho."
         ]},
        {"id": "itv-collado-villalba", "h2": "Dos ITV en Collado Villalba, casi a la misma distancia",
         "parrafos": [
             "En el listado de la Comunidad de Madrid, las estaciones más cercanas por carretera están en Collado Villalba: la de ITV P-29 (estación 2883), en la calle Buril 10, a 18,1 km, y la de TÜV SÜD ATISAE (estación 2813), a 18,3. Elige por horario.",
             "San Lorenzo tenía 18.872 vecinos en 2025 y 9.121 turismos censados ese año: 483 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de la zona?",
         "a": "No. El servicio oficial más cercano es Movilnorte, en la A-6, km 23,100, en Las Rozas. Dasercars es un taller independiente en Alcobendas."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Collado Villalba: la estación 2883, en la calle Buril 10, a 18,1 km, o la 2813, a 18,3."},
        {"q": "¿Hace falta registrar la batería nueva?",
         "a": "Sí. Sin registrarla, la centralita la carga como si fuera la vieja y dura menos."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "18.872 habitantes (+3,7 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "9.121 · 483 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "1.047 m", **F.copernicus},
        {"etiqueta": "ITV más cercanas", "valor": "Collado Villalba (2883 y 2813) · 18,1 y 18,3 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Las Rozas) · 28,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 56,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Villanueva del Pardillo
CIUDADES["villanueva-del-pardillo"] = {
    "h1": "Taller en Villanueva del Pardillo: lo que hay cerca y el especialista BMW a 36,4 km",
    "entradilla": "Si buscas un taller dentro de Villanueva del Pardillo, nosotros no lo somos: el taller especialista BMW de la red está en Alcobendas. Te contamos qué tienes en Las Rozas y Majadahonda y cuándo merece la pena el viaje.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 36.4},
    "secciones": [
        {"id": "no-es-un-taller-del-pueblo", "h2": "Esto no es un taller del pueblo",
         "parrafos": [
             "Dasercars Madrid está en la calle Valgrande 17 de Alcobendas. Desde Villanueva la ruta sale por la M-509 y la M-851, pasa a la M-505 y la A-6, rodea por la M-40 y entra por la A-1: 36,4 km por carretera, 27 en línea recta.",
             "Para un pinchazo o una revisión básica, un taller del municipio te sirve igual. Para una avería de BMW o MINI que no se ha resuelto, el mantenimiento por plan de marca o un diésel N47 o B47 que da avisos, sí compensa."
         ]},
        {"id": "presupuesto", "h2": "Cómo se presupuesta",
         "parrafos": [
             "Antes de tocar el coche recibes un presupuesto por escrito, y no se empieza nada hasta que lo apruebas. La diagnosis también se presupuesta: es trabajo técnico, no un trámite.",
             "La recogida y el vehículo de cortesía existen dentro del área metropolitana de Madrid, sujetos a disponibilidad. Pregunta al pedir cita si tu calle entra."
         ]},
        {"id": "las-rozas-y-majadahonda", "h2": "ITV en Las Rozas, servicio oficial en Majadahonda",
         "parrafos": [
             "La estación de ITV oficial más próxima por carretera es la de TÜV SÜD ATISAE (estación 2816), en la calle Cabo Rufino Lázaro 14D del polígono Európolis de Las Rozas, a 8,5 km. El servicio oficial BMW más cercano según bmw.es es Movilnorte, en la carretera de El Plantío 62 de Majadahonda, a 13,6 km."
         ]},
        {"id": "pardillo-cifras", "h2": "18.466 vecinos y 506 turismos por cada mil",
         "parrafos": [
             "El padrón dio a Villanueva del Pardillo 16.797 habitantes en 2015 y 18.466 en 2025, un 9,9 % más. La Comunidad de Madrid, a partir de la DGT, contaba 9.336 turismos en 2025: 506 por cada 1.000 habitantes, frente a 388 en Madrid capital.",
             "Con la M-509 y la M-503 como únicas vías principales a menos de tres kilómetros, casi todo trayecto empieza por carretera autonómica antes de llegar a la A-6."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Villanueva del Pardillo?",
         "a": "No. El taller que atiende la zona está en Alcobendas, a 36,4 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima es la de TÜV SÜD ATISAE en el polígono Európolis de Las Rozas, a 8,5 km."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Movilnorte, en la carretera de El Plantío 62 de Majadahonda, a 13,6 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "18.466 habitantes (+9,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "9.336 · 506 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE (Las Rozas) · 8,5 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Majadahonda) · 13,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 36,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Piera
CIUDADES["piera"] = {
    "h1": "Piera: el taller especialista BMW a 39 km por la AP-7 y lo oficial en Terrassa",
    "entradilla": "Piera ha ganado casi 2.900 vecinos en diez años. Para el dueño de un BMW o un MINI, el mapa es poco intuitivo: ITV en Igualada, servicio oficial en Terrassa y el taller especialista de la red en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 39.0},
    "secciones": [
        {"id": "autorizado-o-independiente", "h2": "Taller autorizado o especialista independiente",
         "parrafos": [
             "El punto oficial BMW más próximo por carretera según bmw.es es Quadis Munich, en el carrer Anoia 9 de Terrassa, a 34,1 km. Es allí donde se tramita una reparación en garantía.",
             "Dasercars no es un taller autorizado: es independiente y especializado en BMW y MINI. Te da presupuesto por escrito y no empieza ningún trabajo sin tu visto bueno, con la diagnosis presupuestada aparte."
         ]},
        {"id": "b224-ap7", "h2": "Por la B-224 y la AP-7",
         "parrafos": [
             "Hasta el carrer del Tambor del Bruc de Sant Joan Despí hay 39 km por carretera (31,3 en línea recta): la B-224, la AP-7 y la B-23. Piera no pertenece al Área Metropolitana de Barcelona, así que la recogida del taller no llega.",
             "Como el servicio oficial y nuestro taller quedan a distancias parecidas, la decisión no depende de los kilómetros sino del trabajo: garantía de la marca, en la red oficial; mantenimiento y averías fuera de garantía, donde prefieras."
         ]},
        {"id": "itv-les-comes", "h2": "La ITV, en Igualada",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Igualada (B12), en el carrer Països Baixos del polígono Les Comes, a 21,6 km. Hacia Igualada se va en dirección contraria a Barcelona, así que conviene no juntar ITV y taller el mismo día."
         ]},
        {"id": "piera-crece", "h2": "Un 19,3 % más de población desde 2015",
         "parrafos": [
             "Piera pasó de 14.991 habitantes en 2015 a 17.880 en 2025. Su término mide 57,2 km² y en 2024 había 9.729 turismos según Idescat a partir de la DGT: 544 por cada 1.000 vecinos.",
             "En un municipio extenso, con varios núcleos y la B-224 y la C-54 cerca, el coche es casi imprescindible. Los recorridos cortos entre urbanizaciones son los que menos le gustan a un diésel moderno: si el testigo del filtro de partículas se enciende a menudo, ese es el motivo más probable."
         ]},
    ],
    "faq": [
        {"q": "¿Sois taller autorizado BMW?",
         "a": "No. El autorizado más cercano es Quadis Munich, en Terrassa, a 34,1 km. Dasercars es un especialista independiente."},
        {"q": "¿Dónde paso la ITV desde Piera?",
         "a": "La más próxima por carretera es la de Igualada (B12), en el polígono Les Comes, a 21,6 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "39 km por la B-224, la AP-7 y la B-23, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.880 habitantes (+19,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("081614")},
        {"etiqueta": "Turismos (2024)", "valor": "9.729 · 544 por cada 1.000 hab.", **F.idescat("081614")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 21,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Terrassa) · 34,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 39 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081614"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Guadarrama
CIUDADES["guadarrama"] = {
    "h1": "Diagnosis BMW para Guadarrama: el especialista está en Alcobendas, a 56,6 km",
    "entradilla": "Mucha gente de Guadarrama busca diagnosis antes que taller. Nuestro taller especialista está en Alcobendas, al otro lado de la sierra; te contamos cómo funciona una diagnosis allí y qué tienes más cerca.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 56.6},
    "secciones": [
        {"id": "diagnosis", "h2": "Qué es una diagnosis y cómo se cobra",
         "parrafos": [
             "Leer los códigos de avería es solo el principio. Una diagnosis en un BMW consiste en interpretar esos códigos con los valores reales de los sensores, comprobar el cableado y descartar causas hasta dar con la pieza, y por eso lleva tiempo.",
             "En Dasercars la diagnosis se presupuesta antes de conectar el equipo, igual que la reparación que salga de ella. Desde esta distancia, antes de nada, llama: con modelo, año, kilometraje y lo que hace el coche muchas veces se puede orientar el problema y saber si hay que bajar."
         ]},
        {"id": "n6-a6-a1", "h2": "De Guadarrama a Alcobendas: 56,6 km",
         "parrafos": [
             "La ruta toma la N-6 y la AP-6, sigue por la A-6, enlaza con la M-40 y termina por la A-1 hasta la calle Valgrande: 56,6 km por carretera, 40 en línea recta. La recogida, sujeta a disponibilidad, es para el área metropolitana de Madrid; confirma antes si llega hasta aquí."
         ]},
        {"id": "a-963-metros", "h2": "963 metros: qué revisar antes del invierno",
         "parrafos": [
             "El centro de Guadarrama está a 963 m. En invierno conviene comprobar el anticongelante por concentración y no solo por nivel, revisar el precalentamiento si el coche es diésel y mirar la batería antes de la primera helada, no después."
         ]},
        {"id": "lo-que-hay-cerca", "h2": "ITV y servicio oficial, hacia la A-6",
         "parrafos": [
             "En el listado de la Comunidad de Madrid hay dos estaciones casi empatadas, las dos en Collado Villalba: ITV P-29 (estación 2883), en la calle Buril 10, a 9 km, y TÜV SÜD ATISAE (estación 2813), a 9,1 km. El servicio oficial BMW más próximo según bmw.es es Movilnorte, en la A-6, km 23,100, en Las Rozas, a 25,3 km.",
             "Guadarrama tenía 17.547 vecinos en 2025, un 12,9 % más que en 2015, y 9.297 turismos censados en 2025: 530 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Hacéis diagnosis de BMW en Guadarrama?",
         "a": "No en el municipio: la diagnosis se hace en el taller de Alcobendas, a 56,6 km, y se presupuesta antes de empezar."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Collado Villalba: la estación 2883 está a 9 km y la 2813, a 9,1."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Movilnorte, en la A-6, km 23,100, en Las Rozas, a 25,3 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.547 habitantes (+12,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "9.297 · 530 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "963 m", **F.copernicus},
        {"etiqueta": "ITV más cercanas", "valor": "Collado Villalba (2883 y 2813) · 9 y 9,1 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Las Rozas) · 25,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 56,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Berga
CIUDADES["berga"] = {
    "h1": "BMW en Berga: ITV en La Valldan y el taller especialista a 104,5 km",
    "entradilla": "Berga, capital del Berguedà, tiene su propia ITV, pero el servicio oficial BMW más cercano está en el Bages y nuestro taller, a más de cien kilómetros. Sin rodeos: para qué te sirve y para qué no.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 104.5},
    "secciones": [
        {"id": "itv-la-valldan", "h2": "La ITV, en el polígono La Valldan",
         "parrafos": [
             "El registro de la Generalitat incluye una estación dentro del municipio: la de Berga (B13), en el camí de Sant Bartomeu, polígono industrial La Valldan, gestionada por TÜV Rheinland. Para la inspección no hace falta salir de la ciudad."
         ]},
        {"id": "bages", "h2": "Lo oficial, a 43,3 km por la C-16",
         "parrafos": [
             "Según bmw.es, el servicio oficial BMW más próximo es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 43,3 km. Lo que cubre la garantía de BMW, allí."
         ]},
        {"id": "cuando-bajar", "h2": "Cuándo merece la pena hacer 104,5 km",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc de Sant Joan Despí es casi toda la C-16 y, al final, la B-20: 104,5 km por carretera. Para un cambio de aceite no tiene sentido. Lo tiene para una avería concreta de BMW que no se ha resuelto en la comarca, un fallo intermitente que nadie encuentra o un segundo diagnóstico antes de aceptar una reparación cara.",
             "Antes de coger el coche, llama con modelo, año, kilometraje y el síntoma. El presupuesto llega por escrito y no se toca nada sin tu aprobación, así que sabes a qué vas antes de salir."
         ]},
        {"id": "704-metros", "h2": "704 metros y la batería",
         "parrafos": [
             "Berga está a 704 m de altitud. No es alta montaña, pero las mañanas frías de invierno descubren las baterías al límite. En un BMW, la batería nueva debe registrarse en la centralita; sin ese paso, el sistema la carga como si fuera la vieja.",
             "Berga tenía 17.473 vecinos en 2025, un 7,6 % más que en 2015, y 8.965 turismos en 2024 según Idescat a partir de la DGT: 513 por cada 1.000 habitantes. La C-16, la C-26 y la C-17 pasan a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Berga?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 104,5 km."},
        {"q": "¿Dónde paso la ITV en Berga?",
         "a": "En la estación B13, en el polígono La Valldan, dentro del municipio."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 43,3 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.473 habitantes (+7,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080229")},
        {"etiqueta": "Altitud", "valor": "704 m", **F.idescat("080229")},
        {"etiqueta": "Turismos (2024)", "valor": "8.965 · 513 por cada 1.000 hab.", **F.idescat("080229")},
        {"etiqueta": "ITV en el municipio", "valor": "Berga (B13), polígono La Valldan", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 43,3 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080229"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Canovelles
CIUDADES["canovelles"] = {
    "h1": "Canovelles, pegada a Granollers: ITV y servicio oficial a 6 km, especialista BMW a 40",
    "entradilla": "Canovelles comparte casi calle con Granollers, que está a un kilómetro de su centro. Ahí tienes la ITV y el servicio oficial BMW. El taller especialista de la red está en Sant Joan Despí, a 40,2 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 40.2},
    "secciones": [
        {"id": "granollers-al-lado", "h2": "Granollers, a la vuelta de la esquina",
         "parrafos": [
             "La ITV más próxima por carretera en el registro de la Generalitat es la de Granollers (B18), en la avinguda de Sant Julià, polígono El Congost, a 5,4 km. El servicio oficial BMW más cercano según bmw.es es Pruna Motor, en la C-17, km 19,060, también en Granollers, a 5,9 km.",
             "Las llamadas a revisión que envía BMW se atienden en la red oficial. Si te llega una, es con ellos."
         ]},
        {"id": "independiente", "h2": "Lo que hace un especialista independiente",
         "parrafos": [
             "Mantenimiento por plan de marca, diagnosis y reparación de BMW y MINI, con especial oficio en los diésel de la casa. Dasercars Barcelona está en el carrer del Tambor del Bruc 3 de Sant Joan Despí: 40,2 km por la C-17, la C-33 y la B-20, 33,4 en línea recta.",
             "Canovelles no es municipio del Área Metropolitana de Barcelona, así que la recogida que ofrece el taller no llega aquí."
         ]},
        {"id": "denso-y-con-carreteras", "h2": "6,66 km² rodeados de carreteras",
         "parrafos": [
             "Canovelles es pequeño de término, 6,66 km², y muy denso: 2.624 habitantes por km². A menos de tres kilómetros del centro pasan la C-17, la C-352, la C-251, la C-155 y la C-1415, entre otras. Es un entorno de rotondas y arranques constantes, el que más desgasta embrague, frenos y silentblocks.",
             "Tenía 15.906 habitantes en 2015 y 17.473 en 2025, un 9,9 % más. Idescat, a partir de la DGT, contaba 7.772 turismos en 2024: 445 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Canovelles?",
         "a": "En Granollers (B18), en el polígono El Congost, a 5,4 km."},
        {"q": "¿Sois el servicio oficial BMW de Granollers?",
         "a": "No. Ese es Pruna Motor, en la C-17. Dasercars es un taller independiente en Sant Joan Despí."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI comparte electrónica y motores con BMW y se diagnostica con el mismo equipo."},
        {"q": "¿A cuánto está vuestro taller desde Canovelles?",
         "a": "A 40,2 km por carretera, en el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.473 habitantes (+9,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080410")},
        {"etiqueta": "Superficie del término", "valor": "6,66 km²", **F.idescat("080410")},
        {"etiqueta": "Turismos (2024)", "valor": "7.772 · 445 por cada 1.000 hab.", **F.idescat("080410")},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 5,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 5,9 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080410"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- la Garriga
CIUDADES["la-garriga"] = {
    "h1": "La Garriga y la C-17: tu BMW entre Granollers y Sant Joan Despí",
    "entradilla": "En la Garriga casi todo pasa por la C-17: el servicio oficial BMW de Granollers, la ITV y la ruta hasta nuestro taller. Lo que hay en cada punto y los kilómetros reales.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 46.5},
    "secciones": [
        {"id": "una-sola-carretera", "h2": "Una sola carretera principal",
         "parrafos": [
             "La única vía con referencia que pasa a menos de tres kilómetros del centro es la C-17. Hacia el sur te lleva a Granollers; hacia Barcelona enlaza con la C-33 y, desde ahí, con la B-20 hasta Sant Joan Despí. En total, 46,5 km por carretera hasta el carrer del Tambor del Bruc (39,8 en línea recta).",
             "La Garriga no forma parte del Área Metropolitana de Barcelona, así que queda fuera de la recogida que ofrece el taller."
         ]},
        {"id": "granollers", "h2": "Lo oficial y la ITV, en Granollers",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la propia C-17, km 19,060, en Granollers: 12,6 km. La ITV más cercana por carretera en el registro de la Generalitat es la estación B18 de Granollers, en el polígono El Congost, a 15,3 km.",
             "Lo que paga la garantía, en la red oficial. Lo demás, donde elijas."
         ]},
        {"id": "para-que-bajar", "h2": "Para qué bajar hasta Sant Joan Despí",
         "parrafos": [
             "Para trabajos en los que un especialista BMW marca la diferencia: un N47 o N57 con ruido de cadena, un error del sistema SCR, un consumo eléctrico en reposo que vacía la batería, o el mantenimiento por plan de marca con el indicador de servicio puesto a cero como corresponde.",
             "Para un trabajo de un día, lo práctico es entrar temprano y recogerlo por la tarde."
         ]},
        {"id": "la-garriga-cifras", "h2": "17.426 vecinos y 8.723 turismos",
         "parrafos": [
             "La Garriga tenía 15.740 habitantes en 2015 y 17.426 en 2025, un 10,7 % más. El centro está a 252 m de altitud y el término mide 18,8 km². En 2024 había 8.723 turismos censados según Idescat a partir de la DGT, 501 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a la Garriga?",
         "a": "Pruna Motor, en la C-17, km 19,060, en Granollers, a 12,6 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Granollers (B18), a 15,3 km."},
        {"q": "¿A cuánto queda vuestro taller?",
         "a": "A 46,5 km, en Sant Joan Despí, por la C-17, la C-33 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.426 habitantes (+10,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080885")},
        {"etiqueta": "Turismos (2024)", "valor": "8.723 · 501 por cada 1.000 hab.", **F.idescat("080885")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 12,6 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 15,3 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 46,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080885"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- El Escorial
CIUDADES["el-escorial"] = {
    "h1": "Taller BMW para El Escorial: especialista independiente en Alcobendas, a 53,7 km",
    "entradilla": "Desde El Escorial se busca mucho «taller BMW Madrid» y lo oficial de la marca. Nosotros somos lo primero, pero no lo segundo: somos el taller especialista independiente de Alcobendas. Aquí tienes también lo oficial y la ITV.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 53.7},
    "secciones": [
        {"id": "oficial-o-no", "h2": "No somos servicio oficial, y lo decimos",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es Movilnorte, en la A-6, km 23,100, en Las Rozas: 26,1 km por carretera. Las campañas que convoca el fabricante se hacen allí, igual que las reparaciones que paga la garantía de BMW.",
             "Dasercars es un taller independiente especializado en BMW y MINI. Mantenimiento, diagnosis y reparaciones sí; garantía de fábrica, no."
         ]},
        {"id": "m505-a6", "h2": "Por la M-505 y la A-6 hasta Alcobendas",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 baja por la M-505 a la A-6, sigue por la M-40 y entra por la A-1: 53,7 km por carretera, 40,6 en línea recta. La recogida y el vehículo de cortesía, ambos sujetos a disponibilidad, están pensados para el área metropolitana de Madrid; pregunta al reservar si alcanzan a tu dirección."
         ]},
        {"id": "tres-itv-villalba", "h2": "Tres ITV en Collado Villalba, a unos 18 km",
         "parrafos": [
             "En el listado de la Comunidad de Madrid, las tres estaciones más próximas por carretera están en Collado Villalba y a distancias casi idénticas: la de Itevelesa (estación 2832), en la A-6, km 37,6, a 18 km; la de ITV P-29 (2883), a 18,2, y la de TÜV SÜD ATISAE (2813), a 18,3. Escoge la que tenga mejor cita."
         ]},
        {"id": "sierra-y-coche", "h2": "918 metros y 579 coches por cada mil vecinos",
         "parrafos": [
             "El centro de El Escorial está a 918 m de altitud y el término mide 68,5 km². En 2025 tenía 17.171 vecinos, un 11,9 % más que en 2015, y 9.948 turismos censados: 579 por cada 1.000 habitantes, frente a 388 en Madrid capital.",
             "Entre el frío del invierno y las cuestas, frenos y batería son lo que más trabaja. El líquido de frenos se cambia por tiempo porque absorbe humedad aunque el coche ruede poco."
         ]},
    ],
    "faq": [
        {"q": "¿Sois servicio oficial BMW?",
         "a": "No. El servicio oficial más cercano es Movilnorte, en Las Rozas, a 26,1 km. Dasercars es un especialista independiente en Alcobendas."},
        {"q": "¿Dónde paso la ITV desde El Escorial?",
         "a": "En cualquiera de las tres estaciones de Collado Villalba, todas a unos 18 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "53,7 km por la M-505, la A-6, la M-40 y la A-1."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.171 habitantes (+11,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "9.948 · 579 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "918 m", **F.copernicus},
        {"etiqueta": "ITV más cercanas", "valor": "Collado Villalba (2832, 2883, 2813) · unos 18 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Las Rozas) · 26,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 53,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.cartociudad_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Arenys de Mar
CIUDADES["arenys-de-mar"] = {
    "h1": "Arenys de Mar: BMW junto al puerto, servicio oficial en Mataró y especialista a 54,5 km",
    "entradilla": "Con el mar a poco más de un kilómetro del centro, un coche de Arenys pide algunos cuidados que uno de interior no necesita. Te contamos cuáles, dónde está lo oficial y qué supone llevar el BMW a Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 54.5},
    "secciones": [
        {"id": "aire-salino", "h2": "Lo que hace el aire salino",
         "parrafos": [
             "La costa queda a 1,3 km del centro. La sal no se ve, pero se acumula: en los pasos de rueda, en los soportes y abrazaderas del escape y en los conectores que van más expuestos. Un coche que duerme en la calle cerca del puerto lo nota antes que uno de garaje.",
             "Lo práctico: aclarar los bajos con agua dulce de vez en cuando, sobre todo después del invierno, y si el coche ha estado parado varias semanas, frenar suave los primeros kilómetros para limpiar el óxido superficial de los discos."
         ]},
        {"id": "mataro-y-argentona", "h2": "Mataró para lo oficial, Argentona para la ITV",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la Via Sergia 2 de Mataró, a 12,9 km. La ITV más cercana por carretera en el registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 16,9 km."
         ]},
        {"id": "c32-b20", "h2": "54,5 kilómetros por la C-32",
         "parrafos": [
             "Hasta el carrer del Tambor del Bruc de Sant Joan Despí se va por la C-32 y la B-20: 54,5 km por carretera, 47,1 en línea recta. Arenys de Mar no forma parte del Área Metropolitana de Barcelona, de modo que la recogida del taller no llega hasta aquí.",
             "El viaje compensa para un diagnóstico que no ha salido en el Maresme o para el mantenimiento de un diésel BMW con el plan de marca, no para lo que cualquier taller de confianza te resuelve cerca."
         ]},
        {"id": "arenys-cifras", "h2": "17.042 vecinos en 6,75 km²",
         "parrafos": [
             "Arenys de Mar tenía 15.289 habitantes en 2015 y 17.042 en 2025, un 11,5 % más, en un término de 6,75 km². Idescat, a partir de la DGT, contaba 7.239 turismos en 2024: 425 por cada 1.000 vecinos, con la N-II y la C-32 a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Arenys de Mar?",
         "a": "Pruna Motor, en la Via Sergia 2 de Mataró, a 12,9 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima por carretera es la de Argentona (B08), a 16,9 km."},
        {"q": "¿Qué le hace el mar a mi coche?",
         "a": "Acelera la corrosión de bajos y escape, el óxido de los discos si el coche está parado y la sulfatación de conectores."},
        {"q": "¿Recogéis el coche en Arenys?",
         "a": "No: la recogida solo cubre el Área Metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.042 habitantes (+11,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("080060")},
        {"etiqueta": "Turismos (2024)", "valor": "7.239 · 425 por cada 1.000 hab.", **F.idescat("080060")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 1,3 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 12,9 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 16,9 km", **F.itv_cat},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080060"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}


def aplicar_meta_y_titles():
    from comun import CIUDADES_DIR
    for slug, desc in META.items():
        assert len(desc) <= 160, (slug, len(desc))
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        cj["metaDescription"] = desc
        f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
        print("metaDescription", slug)
    for slug, title in TITLES.items():
        assert len(title) <= 65, (slug, len(title))
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        cj["metaTitle"] = title
        f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
        print("metaTitle", slug)
    if not META and not TITLES:
        print("tanda_17: las 15 ciudades tienen impresiones en GSC; no se cambia ni metaTitle ni metaDescription")


if __name__ == "__main__":
    aplicar_meta_y_titles()
