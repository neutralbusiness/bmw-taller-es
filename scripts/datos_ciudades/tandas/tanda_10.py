# Tanda 10: Pozuelo del Rey, Cercs, Olost, Montesquiu, Calders, Santa Maria d'Oló, Quer,
# Santorcaz, Rellinars, Ribatejada, Santa Maria de Martorelles, Jorba, Carme, Òrrius y Castellcir.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py tanda_10.
# Ninguna ciudad de la tanda está en la lista de exclusiones del coordinador.
# Omisiones deliberadas por dudas en los datos:
#  - quer: la ITV más cercana es de OpenStreetMap (verificar: true) y sin dirección → no se publica.
#  - rellinars: el servicio oficial «más cercano» del fichero (Sant Fruitós, 25,1 km) parece
#    erróneo (Vacarisses, a 4,4 km, da Terrassa a 17,5 km) → no se cita servicio oficial.
# META: metaDescription nueva para las 15 (todas con 0 impresiones en GSC y descripción con
# promesas: recogida a domicilio, «diagnosis original», «garantía escrita», presencia en el pueblo).
# Se aplica aparte: python3 scripts/datos_ciudades/tandas/tanda_10.py
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
META = {}

# ---------------------------------------------------------------- Pozuelo del Rey
CIUDADES["pozuelo-del-rey"] = {
    "h1": "Pozuelo del Rey: tu BMW a 820 metros, con Alcalá a 20 km y Alcobendas a 55",
    "entradilla": "Para un BMW o un MINI de Pozuelo del Rey, casi todo lo práctico está en Alcalá de Henares: la ITV y el servicio oficial. El taller especialista de la red, Dasercars Madrid, queda más lejos, en Alcobendas. Estas son las distancias reales.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 55.0},
    "secciones": [
        {"id": "lo-que-queda-en-alcala", "h2": "Alcalá de Henares, la referencia para ITV y servicio oficial",
         "parrafos": [
             "El punto de servicio oficial BMW más próximo según el localizador de bmw.es es AutoPremier, en la calle Argentina 7 del polígono La Garena, en Alcalá de Henares: 20 km por carretera desde el núcleo urbano. En la misma zona de Alcalá está la estación de ITV de TÜV SÜD ATISAE (estación 2878 del listado de la Comunidad de Madrid), en la avenida Juan Carlos I, junto al centro comercial La Garena.",
             "La distancia a esa ITV es aproximada, unos 16 km hasta Alcalá, porque el listado oficial solo la sitúa a nivel de municipio.",
         ]},
        {"id": "r3-m30-a1", "h2": "55 kilómetros hasta la calle Valgrande, entrando por la R-3",
         "parrafos": [
             "La ruta más corta hasta el taller de Alcobendas encadena la M-224, la M-209, la R-3, la M-30 y la A-1: 55 km por carretera, aunque en línea recta son 33,9. Compensa para un trabajo propio de la marca —diagnosis electrónica, distribución de un diésel N47 o B47—, no para unas escobillas.",
         ]},
        {"id": "frio-820", "h2": "Lo que pide el invierno a 820 metros",
         "parrafos": [
             "El núcleo urbano está a unos 820 metros según el modelo de elevación Copernicus. A esa altura, las mañanas de helada destapan las baterías débiles, sobre todo en un BMW con arranque y parada automático, que la somete a muchos más ciclos que un coche sin ese sistema. Mídela en otoño, y revisa la concentración del anticongelante, no solo el nivel.",
         ]},
        {"id": "plan-de-mantenimiento", "h2": "Mantenimiento fuera del concesionario sin tocar la garantía",
         "parrafos": [
             "Un coche en garantía no está obligado a revisarse en la red oficial: el Reglamento (UE) 461/2010 permite hacerlo en un taller independiente si se siguen los intervalos y especificaciones del plan de BMW.",
             "Pozuelo del Rey tenía 1.302 vecinos en el padrón de 2025, un 21,6 % más que en 2015, y 781 turismos censados según la Comunidad de Madrid a partir de la DGT: 600 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay un taller vuestro en Pozuelo del Rey?",
         "a": "No. El taller que atiende el municipio es Dasercars Madrid, en la calle Valgrande 17 de Alcobendas, a 55 km por carretera."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación 2878 de Alcalá de Henares (TÜV SÜD ATISAE), en la avenida Juan Carlos I, a unos 16 km."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "AutoPremier, en la calle Argentina 7 de Alcalá de Henares (polígono La Garena), a 20 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.302 habitantes (+21,6 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "781 · 600 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 820 m", **F.copernicus},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE (2878), Alcalá de Henares · unos 16 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 20 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 55 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}
META["pozuelo-del-rey"] = "Pozuelo del Rey: ITV y servicio oficial BMW en Alcalá de Henares, y el taller especialista de la red en Alcobendas, a 55 km. Qué revisar a 820 metros."

# ---------------------------------------------------------------- Cercs
CIUDADES["cercs"] = {
    "h1": "Cercs, en el Berguedà: ITV en Berga y el especialista BMW a 110 km por la C-16",
    "entradilla": "Lo primero que hay que saber desde Cercs: el taller de la red está en Sant Joan Despí, a 109,6 km. Por eso empezamos por lo que te queda cerca en el Berguedà y después vemos cuándo merece la pena bajar.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 109.6},
    "secciones": [
        {"id": "berga-al-lado", "h2": "La ITV, en el polígono La Valldan de Berga",
         "parrafos": [
             "Según el registro de estaciones de la Generalitat, la más próxima por carretera es la de Berga (B13), en el camí de Sant Bartomeu, dentro del polígono industrial La Valldan: 10,4 km. Berga es la capital del Berguedà, y la inspección y el mantenimiento corriente de un coche de Cercs se resuelven allí sin salir de la comarca.",
         ]},
        {"id": "lo-oficial-en-el-bages", "h2": "El servicio oficial más cercano está ya en el Bages",
         "parrafos": [
             "En el localizador de bmw.es, el punto oficial más próximo es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, término de Sant Fruitós de Bages: 48,4 km por carretera. Es la referencia si el coche está en garantía y lo que necesita depende directamente de BMW.",
         ]},
        {"id": "c16-entera", "h2": "Casi toda la C-16 hasta Sant Joan Despí",
         "parrafos": [
             "La C-16 pasa a doscientos metros del núcleo urbano, y la ruta hasta el taller la sigue prácticamente entera antes de enlazar con la B-20: 109,6 km por carretera, 88,4 en línea recta. Cercs no forma parte del área metropolitana de Barcelona, así que la recogida del coche que ofrece el taller no llega aquí.",
             "Con más de cien kilómetros por delante, el orden lógico es el inverso al de un pueblo cercano: primero una llamada contando modelo, año, kilómetros y qué hace exactamente el coche; después, si el problema lo justifica, una cita con la pieza ya localizada. Una avería repetida de un diésel N47 o N57 es buen motivo; un cambio de aceite, no.",
         ]},
        {"id": "cercs-en-cifras", "h2": "1.236 vecinos y 788 turismos en 47 km²",
         "parrafos": [
             "Cercs tenía 1.236 habitantes en 2025, casi los mismos que en 2015 (1.209), repartidos en un término de 47,35 km² a unos 650 metros de altitud. Idescat, con datos de la DGT, contaba 788 turismos en 2024: 638 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV me toca desde Cercs?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Berga (B13), en el polígono La Valldan, a 10,4 km."},
        {"q": "¿Recogéis el coche en el Berguedà?",
         "a": "No. La recogida del taller se limita al área metropolitana de Barcelona, y Cercs queda fuera."},
        {"q": "¿Merece la pena ir a Sant Joan Despí desde aquí?",
         "a": "Para una avería concreta de BMW sin resolver, sí; para el mantenimiento corriente, no."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.236 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("082687")},
        {"etiqueta": "Turismos (2024)", "valor": "788 · 638 por cada 1.000 hab.", **F.idescat("082687")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 10,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 48,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 109,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082687"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["cercs"] = "BMW en Cercs: ITV en Berga a 10,4 km, servicio oficial en Sant Fruitós de Bages y el taller especialista de la red a 109,6 km. Cuándo compensa bajar."

# ---------------------------------------------------------------- Olost
CIUDADES["olost"] = {
    "h1": "BMW en Olost: Vic a 19 km para lo oficial, Sant Joan Despí a 102 para el especialista",
    "entradilla": "Desde el Lluçanès, Vic es la ciudad de referencia para casi todo lo que tiene que ver con el coche. El taller especialista de la red queda a 102,5 km, y conviene saber qué tiene sentido hacer en cada sitio.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 102.5},
    "secciones": [
        {"id": "vic-ciudad-de-referencia", "h2": "Servicio oficial e ITV, los dos en Vic",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 19,4 km por carretera. La ITV que el registro de la Generalitat da como más próxima también está en Vic: Osona (B04), en el carrer Sant Llorenç Desmunts 22, a 25,7 km.",
         ]},
        {"id": "garantia-y-taller", "h2": "Revisar el coche en garantía fuera de la red",
         "parrafos": [
             "Tener el concesionario a 19 km no obliga a hacer allí las revisiones. La normativa europea de distribución de vehículos (Reglamento UE 461/2010) permite que un taller independiente haga el mantenimiento de un coche en garantía, siempre que respete el plan del fabricante: intervalos, aceite con la homologación BMW correcta y recambios de calidad equivalente.",
         ]},
        {"id": "c62-c25-c16", "h2": "De la C-62 a la B-20: 102,5 kilómetros",
         "parrafos": [
             "La C-62 pasa a menos de un kilómetro del núcleo. Desde ahí, la ruta más corta hasta la nave de Dasercars Barcelona enlaza con la C-25, baja por la C-16 y entra por la B-20 en Sant Joan Despí: 102,5 km por carretera, 69 en línea recta.",
             "Olost no está en el área metropolitana de Barcelona y la recogida que ofrece el taller no llega hasta aquí. Por eso el viaje se reserva para lo que de verdad pide un especialista en la marca: una avería electrónica sin localizar, un problema del sistema de AdBlue o un segundo diagnóstico antes de aceptar una reparación cara.",
         ]},
        {"id": "olost-parque", "h2": "650 turismos por cada mil vecinos",
         "parrafos": [
             "Olost tenía 1.209 habitantes en 2025 (1.182 en 2015) y, según Idescat a partir de la DGT, 786 turismos en 2024: 650 por cada 1.000 vecinos, más del doble que en Barcelona ciudad (281). El término mide 29,37 km² y el núcleo está a 572 metros.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Olost?",
         "a": "Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 19,4 km según bmw.es."},
        {"q": "¿Qué estación de ITV me queda más cerca?",
         "a": "Osona (B04), en Vic, a 25,7 km por carretera según el registro de la Generalitat."},
        {"q": "¿Pierdo la garantía si no voy al concesionario?",
         "a": "No, mientras el mantenimiento siga el plan de BMW con recambios y aceites de la especificación correcta."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.209 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Lluçanès", **F.idescat("081496")},
        {"etiqueta": "Turismos (2024)", "valor": "786 · 650 por cada 1.000 hab.", **F.idescat("081496")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 25,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 19,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 102,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081496"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}
META["olost"] = "BMW y MINI en Olost: servicio oficial e ITV en Vic, a 19,4 y 25,7 km, y el taller especialista de la red en Sant Joan Despí, a 102,5 km."

# ---------------------------------------------------------------- Montesquiu
CIUDADES["montesquiu"] = {
    "h1": "Montesquiu: ITV en Ripoll, servicio oficial en Vic y taller BMW a 103 km por la C-17",
    "entradilla": "Montesquiu es pequeño en superficie —menos de cinco kilómetros cuadrados— y ha ganado casi un 20 % de vecinos en diez años. Para tu BMW o tu MINI, la ITV queda hacia el norte, en Ripoll, y el servicio oficial hacia el sur, en Vic.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 103.1},
    "secciones": [
        {"id": "ripoll-o-vic", "h2": "Al norte para la ITV, al sur para el concesionario",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Ripoll (G08), en el passeig d'Ordina: 14,9 km. El servicio oficial BMW más cercano según bmw.es está en dirección contraria, en Vic: Quadis Munich, carrer Perot Rocaguinarda 1, a 27,5 km.",
             "Las llamadas a revisión que hace BMW por un defecto de fabricación solo las atiende la red oficial, así que si te llega una carta de la marca, esa cita es en Vic.",
         ]},
        {"id": "c17-c33", "h2": "La C-17 casi en la puerta y 103 km hasta Sant Joan Despí",
         "parrafos": [
             "La C-17 pasa a menos de un kilómetro del centro, y es la que lleva hacia Barcelona: la ruta hasta la nave de Dasercars Barcelona sigue por la C-17 y la C-33 y termina en la B-20, con 103,1 km por carretera y 84,1 en línea recta.",
             "Es una distancia que no compensa para una revisión rutinaria. Sí para un problema que un taller de Osona no ha conseguido cerrar o para un recambio que exige programar la centralita. Montesquiu no forma parte del área metropolitana, de modo que la recogida del taller no cubre el municipio.",
         ]},
        {"id": "montesquiu-crece", "h2": "De 943 a 1.131 vecinos",
         "parrafos": [
             "Según el padrón del INE, Montesquiu ha pasado de 943 habitantes en 2015 a 1.131 en 2025, un 19,9 % más, en un término de 4,94 km² a 577 metros de altitud. Idescat contaba 598 turismos en 2024 a partir de la DGT: 529 por cada 1.000 vecinos.",
             "Tener una autovía tan cerca ayuda a un diésel moderno: el filtro de partículas se limpia solo cuando el motor trabaja un rato caliente y a carga estable, algo que los trayectos cortos por el pueblo no le dan.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Montesquiu?",
         "a": "En la estación de Ripoll (G08), en el passeig d'Ordina, a 14,9 km: la más próxima por carretera en el registro de la Generalitat."},
        {"q": "¿Hay servicio oficial BMW en Osona?",
         "a": "Sí: Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 27,5 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "103,1 km por la C-17, la C-33 y la B-20, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.131 habitantes (+19,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081311")},
        {"etiqueta": "Turismos (2024)", "valor": "598 · 529 por cada 1.000 hab.", **F.idescat("081311")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 14,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 27,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 103,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081311"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["montesquiu"] = "BMW en Montesquiu: ITV en Ripoll a 14,9 km, servicio oficial en Vic y el taller especialista de la red a 103,1 km por la C-17 y la C-33."

# ---------------------------------------------------------------- Calders
CIUDADES["calders"] = {
    "h1": "Calders, en el Moianès: lo oficial a 12 km en Sant Fruitós y el especialista BMW a 71",
    "entradilla": "Sant Fruitós de Bages lo concentra casi todo para un coche de Calders: servicio oficial BMW e ITV, a 12,4 y 15,7 km. Nuestro taller está en Sant Joan Despí, a 70,7 km por la C-16. Lo que conviene hacer en cada sitio.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 70.7},
    "secciones": [
        {"id": "sant-fruitos-cerca", "h2": "Concesionario e ITV en el mismo municipio vecino",
         "parrafos": [
             "En el localizador de bmw.es, el punto oficial más próximo es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 12,4 km por carretera. En el mismo término está la ITV que el registro de la Generalitat da como más próxima, Sant Fruitós (B25), en el carrer Les Malloles del polígono industrial El Grau, a 15,7 km.",
             "Si recibes una carta de BMW para una revisión de seguridad, esa intervención solo la hace la red oficial, y lo lógico es hacerla en Sant Fruitós.",
         ]},
        {"id": "n141c-c16", "h2": "De la N-141c a la C-16",
         "parrafos": [
             "La N-141c pasa a cien metros del centro, y por ahí empieza la ruta hasta la nave de Dasercars Barcelona; después vienen la C-16 y la B-20 hasta Sant Joan Despí. En total, 70,7 km por carretera y 47,3 en línea recta.",
             "Calders queda fuera del área metropolitana y la recogida del taller no llega. El viaje compensa cuando buscas una alternativa independiente al concesionario para un trabajo concreto: un ruido de distribución, una caja automática que ya ha dado problemas, una avería eléctrica intermitente.",
         ]},
        {"id": "moianes-cifras", "h2": "Un 15,9 % más de vecinos en diez años",
         "parrafos": [
             "Calders tenía 968 habitantes en 2015 y 1.122 en 2025, según el padrón, en un término de 33,09 km² a 552 metros de altitud. Idescat, con datos de la DGT, contaba 668 turismos en 2024: 595 por cada 1.000 habitantes.",
             "Un coche que pasa días parado y luego hace solo trayectos cortos sufre más por la batería y por un aceite que no llega a coger temperatura que por los kilómetros. Si es tu caso, el intervalo de cambio de aceite por tiempo importa tanto como el de kilometraje.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano a Calders?",
         "a": "Quadis Munich, en la carretera de Manresa a Berga, km 34,5 (Sant Fruitós de Bages), a 12,4 km."},
        {"q": "¿Y la ITV?",
         "a": "En el polígono El Grau de Sant Fruitós de Bages (estación B25), a 15,7 km."},
        {"q": "¿Calders es del Bages?",
         "a": "No: según Idescat, Calders pertenece al Moianès. Los servicios que tienes más cerca, eso sí, están en el Bages."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.122 habitantes (+15,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Moianès", **F.idescat("080348")},
        {"etiqueta": "Turismos (2024)", "valor": "668 · 595 por cada 1.000 hab.", **F.idescat("080348")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 12,4 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sant Fruitós (B25) · 15,7 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 70,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080348"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["calders"] = "BMW en Calders (Moianès): servicio oficial e ITV en Sant Fruitós de Bages, a 12,4 y 15,7 km, y taller especialista de la red a 70,7 km por la C-16."

# ---------------------------------------------------------------- Santa Maria d'Oló
CIUDADES["santa-maria-d-olo"] = {
    "h1": "Santa Maria d'Oló: 66 km² de término y el taller BMW de la red a 83 km",
    "entradilla": "Con 66,21 km² y 17 habitantes por kilómetro cuadrado, Santa Maria d'Oló es un municipio extenso y poco denso. Te contamos qué te queda más cerca para el BMW o el MINI y qué supone bajar a Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 83.3},
    "secciones": [
        {"id": "termino-extenso", "h2": "Un término grande en el que todo se hace en coche",
         "parrafos": [
             "El padrón de 2025 da a Santa Maria d'Oló 1.099 vecinos, casi los mismos que en 2015 (1.063). En 2024 había 643 turismos según Idescat a partir de la DGT, 585 por cada 1.000 habitantes. Con 17 habitantes por km², la distancia forma parte del día a día.",
             "Para un coche que suma muchos kilómetros por carretera secundaria, lo que más agradece es que se respeten los avisos del indicador de servicio y que neumáticos y amortiguadores se revisen por su estado, no solo por el cuentakilómetros.",
         ]},
        {"id": "vic-y-sant-fruitos", "h2": "Servicio oficial en Vic, ITV en Sant Fruitós de Bages",
         "parrafos": [
             "El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 21 km por carretera. Para la inspección, la estación más próxima por carretera en el registro de la Generalitat es la de Sant Fruitós (B25), en el polígono El Grau, a 27,2 km.",
             "Son dos direcciones distintas, una hacia Osona y otra hacia el Bages, así que no cuentes con resolver las dos cosas en una sola salida.",
         ]},
        {"id": "c25-hacia-el-sur", "h2": "Por la BP-4313 y la C-25 hasta la C-16",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona sale por la BP-4313, toma la C-25, que pasa a menos de un kilómetro del pueblo, y baja por la C-16 y la B-20: 83,3 km por carretera y 56,8 en línea recta.",
             "A esa distancia, y fuera del área metropolitana —la recogida del taller no llega aquí—, el desplazamiento se justifica por un trabajo que necesite un especialista en la marca: un diagnóstico que no se ha cerrado, un fallo de inyección o de turbo en un diésel M57 o N57, un testigo que vuelve una y otra vez.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller cerca de Santa Maria d'Oló?",
         "a": "No. El de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 83,3 km."},
        {"q": "¿Qué ITV queda más cerca?",
         "a": "La de Sant Fruitós de Bages (B25), a 27,2 km por carretera."},
        {"q": "¿Dónde está el servicio oficial BMW?",
         "a": "En Vic: Quadis Munich, carrer Perot Rocaguinarda 1, a 21 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.099 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Moianès", **F.idescat("082589")},
        {"etiqueta": "Superficie del término", "valor": "66,21 km² · 17 hab./km²", **F.cartociudad},
        {"etiqueta": "Turismos (2024)", "valor": "643 · 585 por cada 1.000 hab.", **F.idescat("082589")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Fruitós (B25) · 27,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 21 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082589"), F.cartociudad_f, F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["santa-maria-d-olo"] = "BMW en Santa Maria d'Oló: servicio oficial en Vic a 21 km, ITV en Sant Fruitós de Bages y el taller especialista de la red a 83,3 km por la C-25."

# ---------------------------------------------------------------- Quer
CIUDADES["quer"] = {
    "h1": "Quer: un 44,6 % más de vecinos, la R-2 al lado y el taller BMW a 50 km",
    "entradilla": "Quer ha pasado de 747 a 1.080 habitantes en diez años. Está en la provincia de Guadalajara, pero el taller que lo atiende es el de Alcobendas, a 50,2 km por la R-2. Esto es lo que tienes cerca y lo que no te vamos a prometer.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 50.2},
    "secciones": [
        {"id": "pueblo-que-crece", "h2": "De 747 a 1.080 habitantes",
         "parrafos": [
             "Según el padrón del INE, Quer tenía 747 habitantes en 2015 y 1.080 en 2025: un 44,6 % más, en un término de 14,2 km² a unos 727 metros de altitud. No tenemos una cifra municipal de turismos para Castilla-La Mancha, así que no la damos.",
         ]},
        {"id": "carreteras-de-quer", "h2": "N-320, R-2 y dos autonómicas a menos de 3 km",
         "parrafos": [
             "La N-320a pasa casi por el centro, y a menos de tres kilómetros están también la N-320, la autopista R-2 y las autonómicas CM-1007 y CM-1008. Con la R-2 tan a mano, se llega a Alcobendas sin cruzar Madrid.",
         ]},
        {"id": "autopremier-guadalajara", "h2": "El servicio oficial, en el Paseo de la Estación de Guadalajara",
         "parrafos": [
             "El punto oficial BMW más próximo según el localizador de bmw.es es AutoPremier, en el Paseo de la Estación 23 de Guadalajara, a 14,6 km por carretera. Es la referencia para las reparaciones que cubre la garantía de BMW.",
             "Sobre la ITV preferimos no darte una dirección: la estación más cercana que aparece en nuestros datos procede de OpenStreetMap y no la hemos podido contrastar con la web del operador. Consulta la red de estaciones de Castilla-La Mancha antes de pedir cita.",
         ]},
        {"id": "cuando-ir-a-alcobendas", "h2": "50 kilómetros: para qué compensa",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas usa la N-320a, la N-320, la R-2 y la M-50: 50,2 km por carretera, 32,4 en línea recta. La recogida y entrega del taller se limita al área metropolitana de Madrid, y Quer queda fuera: el coche lo llevas tú.",
             "Antes de hacer el viaje, cuéntanos por teléfono qué coche es, de qué año, cuántos kilómetros lleva y qué síntoma tiene. Así se sabe si el problema justifica el desplazamiento.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Quer o en el Corredor del Henares?",
         "a": "No. El taller que atiende Quer es Dasercars Madrid, en Alcobendas, a 50,2 km por carretera."},
        {"q": "¿Recogéis el coche en Quer?",
         "a": "No: la recogida y entrega del taller solo cubre el área metropolitana de Madrid."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "AutoPremier, en el Paseo de la Estación 23 de Guadalajara, a 14,6 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.080 habitantes (+44,6 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "14,2 km²", **F.cartociudad},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 727 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Guadalajara · 14,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 50,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["quer"] = "BMW en Quer (Guadalajara): servicio oficial en Guadalajara a 14,6 km y el taller especialista de la red en Alcobendas, a 50,2 km por la R-2."

# ---------------------------------------------------------------- Santorcaz
CIUDADES["santorcaz"] = {
    "h1": "Santorcaz, a 880 metros: frío, batería y el taller BMW a 46 km por la R-2",
    "entradilla": "El núcleo urbano de Santorcaz está a unos 880 metros de altitud, y eso cambia lo que hay que vigilar en un BMW antes del invierno. Lo demás —ITV, servicio oficial y taller— está en Alcalá de Henares y en Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 46.3},
    "secciones": [
        {"id": "880-metros", "h2": "Antes de la primera helada",
         "parrafos": [
             "A 880 metros, el frío pone a prueba tres cosas. La batería, que pierde capacidad con la temperatura y en un BMW alimenta muchos consumos incluso con el coche parado; el anticongelante, que debe tener la concentración correcta y no solo el nivel; y los calentadores de un diésel, que cuando fallan se notan en arranques largos y humo blanco las primeras mañanas.",
             "Si cambias la batería, que la registren en el coche: la gestión de carga del BMW ajusta la tensión al tipo y a la capacidad que tiene anotados, y una batería sin registrar se carga mal.",
         ]},
        {"id": "alcala-cerca", "h2": "Vía Complutense y La Garena: lo que tienes en Alcalá",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 18 km por carretera. La estación oficial de ITV más cercana es la de TÜV SÜD ATISAE (estación 2878), en la avenida Juan Carlos I, junto al centro comercial La Garena, también en Alcalá.",
             "El listado de la Comunidad de Madrid solo permite situar esa estación en el municipio, así que la distancia es orientativa: unos 15,5 km por carretera hasta Alcalá.",
         ]},
        {"id": "m226-r2", "h2": "46,3 km hasta Alcobendas por la M-226 y la R-2",
         "parrafos": [
             "La ruta hasta la calle Valgrande sale por la M-226, toma la R-2 y entra por la M-50: 46,3 km por carretera y 36 en línea recta. El taller abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00; con ese horario, lo cómodo es dejar el coche al empezar el día.",
             "Santorcaz tenía 1.011 vecinos en 2025, un 19,1 % más que diez años antes, y 652 turismos según la Comunidad de Madrid a partir de la DGT: 645 por cada 1.000 habitantes. La M-213 pasa a menos de medio kilómetro del centro.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué revisar en el BMW antes del invierno en Santorcaz?",
         "a": "Batería, concentración del anticongelante y, en los diésel, el estado de los calentadores."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación 2878 de Alcalá de Henares, en la avenida Juan Carlos I (La Garena), a unos 15,5 km."},
        {"q": "¿A cuánto está vuestro taller?",
         "a": "A 46,3 km por la M-226, la R-2 y la M-50, en Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.011 habitantes (+19,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "652 · 645 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 880 m", **F.copernicus},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE (2878), Alcalá de Henares · unos 15,5 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Vía Complutense 131 (Alcalá) · 18 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 46,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["santorcaz"] = "Santorcaz, a 880 m: qué revisar en tu BMW antes del invierno, ITV y servicio oficial en Alcalá y taller especialista en Alcobendas, a 46,3 km."

# ---------------------------------------------------------------- Rellinars
CIUDADES["rellinars"] = {
    "h1": "Rellinars: ITV en Viladecavalls a 16,8 km y taller especialista BMW a 48,6 km",
    "entradilla": "Rellinars ha ganado casi un 24 % de población en diez años, y casi todo lo que necesita un coche está fuera del término. Para un BMW o un MINI, estas son las distancias que cuentan y así se trabaja en el taller de Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 48.6},
    "secciones": [
        {"id": "itv-can-trias", "h2": "La inspección, en el polígono Can Trias",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera al núcleo de Rellinars es la de Viladecavalls (B03), en el carrer Joan Lluís Vives del polígono industrial Can Trias: 16,8 km, aunque en línea recta son 9,9.",
             "Una pre-ITV antes de pedir cita repasa luces, holguras de dirección, frenos y emisiones, y te ahorra una segunda visita a la estación.",
         ]},
        {"id": "bv1212-a2", "h2": "De la BV-1212 a la A-2",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona sale por la BV-1212, sigue por la C-58 y termina por la A-2 hasta Sant Joan Despí: 48,6 km por carretera y 32,4 en línea recta.",
             "Rellinars pertenece al Vallès Occidental, pero no al área metropolitana de Barcelona, que es donde el taller ofrece recogida y entrega: aquí no llega.",
         ]},
        {"id": "como-se-presupuesta", "h2": "Cómo se presupuesta un trabajo",
         "parrafos": [
             "Antes de tocar el coche recibes un presupuesto por escrito, y el trabajo no empieza hasta que lo apruebas. La diagnosis también tiene su presupuesto, porque es trabajo técnico de un mecánico con el equipo conectado, no una lectura rápida de códigos de avería.",
             "Viniendo desde casi cincuenta kilómetros, es la manera de saber a qué te comprometes antes de mover el coche.",
         ]},
        {"id": "rellinars-cifras", "h2": "926 vecinos y 487 turismos",
         "parrafos": [
             "El padrón pasó de 748 habitantes en 2015 a 926 en 2025, un 23,8 % más, en un término de 17,79 km² a 322 metros de altitud. Idescat, a partir de la DGT, contaba 487 turismos en 2024: 526 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Rellinars?",
         "a": "En la estación de Viladecavalls (B03), en el polígono Can Trias, a 16,8 km por carretera."},
        {"q": "¿Recogéis el coche en Rellinars?",
         "a": "No. La recogida del taller cubre solo el área metropolitana de Barcelona."},
        {"q": "¿Me dais el presupuesto antes de empezar?",
         "a": "Sí, por escrito y antes de cualquier intervención, incluida la diagnosis."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "926 habitantes (+23,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("081799")},
        {"etiqueta": "Turismos (2024)", "valor": "487 · 526 por cada 1.000 hab.", **F.idescat("081799")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecavalls (B03) · 16,8 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 48,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081799"), F.itv_cat_f, F.osrm_f, F.dasercars_bcn_f],
}
META["rellinars"] = "BMW y MINI en Rellinars: ITV en Viladecavalls a 16,8 km y taller especialista de la red en Sant Joan Despí, a 48,6 km. Presupuesto por escrito."

# ---------------------------------------------------------------- Ribatejada
CIUDADES["ribatejada"] = {
    "h1": "Ribatejada: Alcobendas a 36,6 km, ITV en Algete y servicio oficial en Alcalá",
    "entradilla": "Ribatejada mira a dos lados: la ITV oficial más cercana está en Algete y el servicio oficial BMW, en Alcalá de Henares. El taller especialista de la red, Dasercars Madrid, queda a 36,6 km, en Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 36.6},
    "secciones": [
        {"id": "itv-algete", "h2": "ITV en el polígono Sector 8 de Algete",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid da como estación más cercana por carretera la 2818, de ITV Barbastro, en la avenida Nicasio Martín 4, dentro del polígono industrial Sector 8 de Algete: 25,3 km desde el núcleo de Ribatejada.",
             "Si el coche tiene que pasar antes por el taller para poner a punto luces, frenos o emisiones, deja la cita de la estación para unos días después.",
         ]},
        {"id": "alcala-oficial", "h2": "El concesionario más próximo, en La Garena",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial más cercano es AutoPremier, en la calle Argentina 7 del polígono La Garena de Alcalá de Henares, a 24,2 km. Para reparaciones en garantía que dependen directamente de BMW, es tu sitio; el mantenimiento puedes llevarlo donde prefieras.",
         ]},
        {"id": "m113-r2", "h2": "Por la M-113 y la R-2: 36,6 km",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas sale por la M-113, enlaza con la M-50 y usa la R-2: 36,6 km por carretera, 26,4 en línea recta. La N-320 pasa a menos de dos kilómetros del centro.",
             "El taller ofrece recogida y entrega del coche y vehículo de cortesía dentro del área metropolitana de Madrid, siempre sujetos a disponibilidad. Si te interesa, pregunta al pedir la cita si Ribatejada entra en la zona; no lo des por hecho.",
         ]},
        {"id": "ribatejada-cifras", "h2": "Un 28 % más de vecinos desde 2015",
         "parrafos": [
             "Ribatejada pasó de 707 habitantes en 2015 a 905 en 2025, según el padrón del INE. En 2025 tenía 567 turismos censados según la Comunidad de Madrid a partir de la DGT, 627 por cada 1.000 vecinos, en un término de 32 km² a unos 820 metros de altitud.",
             "A esa altura, el otoño es buen momento para medir la batería: es la pieza que antes avisa cuando llega el frío.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Ribatejada?",
         "a": "La recogida del taller está limitada al área metropolitana de Madrid y sujeta a disponibilidad; confirma al reservar si tu dirección entra."},
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Algete: estación 2818 (ITV Barbastro), avenida Nicasio Martín 4, a 25,3 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "36,6 km por carretera hasta la calle Valgrande 17 de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "905 habitantes (+28 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "567 · 627 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITV Barbastro (2818), Algete · 25,3 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 24,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 36,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["ribatejada"] = "BMW en Ribatejada: ITV en Algete, servicio oficial en Alcalá de Henares y el taller especialista de la red en Alcobendas, a 36,6 km por la R-2."

# ---------------------------------------------------------------- Santa Maria de Martorelles
CIUDADES["santa-maria-de-martorelles"] = {
    "h1": "Santa Maria de Martorelles: el especialista BMW a 33 km y la ITV a 8,4",
    "entradilla": "Con 4,51 km² de término y 868 vecinos, Santa Maria de Martorelles tiene la ITV a 8,4 km y el taller especialista de la red a 33 km, en Sant Joan Despí. Esto es lo que te sirve para un BMW o un MINI.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 33.0},
    "secciones": [
        {"id": "cim-valles", "h2": "La ITV del CIM Vallès, en Santa Perpètua",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es la del CIM Vallès (B20), en el carrer Pont Vell, dentro del polígono Les Minetes de Santa Perpètua de Mogoda: 8,4 km.",
             "El municipio tenía 868 habitantes en 2025 (853 en 2015) y 444 turismos en 2024 según Idescat a partir de la DGT: 512 por cada 1.000 vecinos. La costa queda a unos 6,7 km en línea recta, demasiado lejos para que el salitre sea un problema habitual.",
         ]},
        {"id": "granollers-c17", "h2": "Pruna Motor, en la C-17 a la altura de Granollers",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la carretera C-17, km 19,060, en Granollers: 12 km por carretera. Es donde corresponde una reparación cubierta por la garantía de BMW.",
         ]},
        {"id": "bv5006-c33", "h2": "33 kilómetros por la C-33 y la B-20",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona baja por la BV-5006 y sigue por la C-33 y la B-20 hasta Sant Joan Despí: 33 km por carretera y 23,6 en línea recta. Santa Maria de Martorelles no está entre los municipios del área metropolitana de Barcelona, de modo que la recogida del taller no llega hasta aquí.",
             "A esta distancia, el taller no es solo una opción para averías raras: también encaja para el mantenimiento programado si prefieres una alternativa independiente al concesionario.",
         ]},
        {"id": "antes-de-tocar-el-coche", "h2": "Qué recibes antes de que se toque el coche",
         "parrafos": [
             "El taller entrega un presupuesto escrito antes de cualquier intervención y no empieza sin que des el visto bueno. La diagnosis se presupuesta igual que una reparación, porque lleva horas de trabajo técnico.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV?",
         "a": "En el CIM Vallès (B20), en Santa Perpètua de Mogoda, a 8,4 km por carretera."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No: la recogida cubre solo el área metropolitana de Barcelona y el municipio queda fuera."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la C-17, km 19,060, en Granollers, a 12 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "868 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("082567")},
        {"etiqueta": "Turismos (2024)", "valor": "444 · 512 por cada 1.000 hab.", **F.idescat("082567")},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20), Santa Perpètua de Mogoda · 8,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 12 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 33 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082567"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["santa-maria-de-martorelles"] = "BMW en Santa Maria de Martorelles: ITV en Santa Perpètua a 8,4 km, servicio oficial en Granollers y taller especialista de la red a 33 km."

# ---------------------------------------------------------------- Jorba
CIUDADES["jorba"] = {
    "h1": "Jorba, junto a la A-2: ITV en Igualada y el taller BMW a 62 km por la misma autovía",
    "entradilla": "Del núcleo de Jorba a nuestro taller hay una sola vía en la ruta: la A-2, que pasa junto al pueblo. La ITV queda en Igualada y el servicio oficial BMW más cercano, ya en la provincia de Lleida, en Tàrrega.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 62.2},
    "secciones": [
        {"id": "una-sola-autovia", "h2": "62,2 kilómetros de A-2",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona va entera por la A-2 hasta Sant Joan Despí: 62,2 km por carretera y 50,5 en línea recta. Junto al pueblo pasan también la N-II y la C-1412a, y a menos de tres kilómetros, la C-241c y la B-222.",
             "Jorba no forma parte del área metropolitana, así que la recogida que ofrece el taller no llega aquí. A cambio, el viaje es de autovía de principio a fin, lo que facilita dejar el coche a primera hora y volver a por él cuando el trabajo cabe en el día.",
         ]},
        {"id": "itv-les-comes", "h2": "La ITV, en el polígono Les Comes de Igualada",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Igualada (B12), en el carrer Països Baixos 18 del polígono Les Comes: 11,5 km. Igualada es la capital de la Anoia, y para la inspección y el mantenimiento corriente no hace falta ir más lejos.",
         ]},
        {"id": "tarrega", "h2": "El servicio oficial más cercano mira hacia Lleida",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo es Unicars Ponent, en el carrer de la Conca de Barberà de Tàrrega, a 38,2 km por carretera. Para una reparación en garantía que dependa de la marca, es la referencia, aunque esté en otra provincia.",
         ]},
        {"id": "presupuesto-jorba", "h2": "Saber a qué vas antes de coger la autovía",
         "parrafos": [
             "Con más de sesenta kilómetros de viaje, conviene llegar con todo claro. El presupuesto se da por escrito y nada se toca sin tu conformidad; también la diagnosis se presupuesta antes de empezar.",
             "Jorba tenía 850 habitantes en 2025, prácticamente los mismos que en 2015 (838), y 543 turismos en 2024 según Idescat a partir de la DGT: 639 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV me queda más cerca desde Jorba?",
         "a": "Igualada (B12), en el polígono Les Comes, a 11,5 km por carretera."},
        {"q": "¿Cómo se llega a vuestro taller?",
         "a": "Por la A-2 todo el trayecto: 62,2 km hasta Sant Joan Despí."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "En Tàrrega: Unicars Ponent, a 38,2 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "850 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("081038")},
        {"etiqueta": "Turismos (2024)", "valor": "543 · 639 por cada 1.000 hab.", **F.idescat("081038")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 11,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent, Tàrrega · 38,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 62,2 km por la A-2", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081038"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["jorba"] = "BMW en Jorba: ITV en Igualada a 11,5 km, servicio oficial en Tàrrega y el taller especialista de la red a 62,2 km, todo por la A-2."

# ---------------------------------------------------------------- Carme
CIUDADES["carme"] = {
    "h1": "Carme, en la Anoia: ITV a 10,3 km y el taller BMW de la red a 63,8 km",
    "entradilla": "Desde Carme, el servicio oficial BMW más cercano queda a 50 km y el taller especialista de la red, a 63,8. La diferencia no es tan grande, y eso cambia la manera de decidir dónde llevar el coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 63.8},
    "secciones": [
        {"id": "oficial-a-50", "h2": "Servicio oficial a 50 km, especialista a 63,8",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 50 km por carretera. Dasercars Barcelona, en Sant Joan Despí, queda a 63,8 km. Con distancias parecidas, la elección depende más del trabajo que del mapa.",
             "Si el coche está en garantía, el Reglamento (UE) 461/2010 te deja hacer las revisiones fuera de la red de la marca sin perderla, con dos condiciones: cumplir el plan de mantenimiento y montar piezas y aceites que cumplan la especificación de BMW. Las reparaciones que paga la propia garantía siguen siendo cosa del concesionario.",
         ]},
        {"id": "bv2131-c244", "h2": "BV-2131, C-244 y A-2",
         "parrafos": [
             "La ruta hasta el taller sale por la BV-2131, sigue por la C-244 y entra en la A-2 hasta Sant Joan Despí: 63,8 km por carretera, 41,6 en línea recta. La C-37 queda a 2,4 km del centro.",
             "Carme no pertenece al área metropolitana de Barcelona: la recogida del taller no cubre el municipio.",
         ]},
        {"id": "igualada-itv", "h2": "Diez kilómetros hasta la ITV de Igualada",
         "parrafos": [
             "La estación más próxima por carretera según la Generalitat es la de Igualada (B12), en el polígono Les Comes, a 10,3 km. No compensa guardar la inspección para la vuelta del taller: Igualada queda a mano, y una pre-ITV la puede hacer cualquier taller de confianza de la comarca.",
         ]},
        {"id": "carme-en-cifras", "h2": "847 vecinos en 11,68 km²",
         "parrafos": [
             "Carme tenía 847 habitantes en 2025 y 792 en 2015, según el padrón, a 351 metros de altitud. Idescat contaba 508 turismos en 2024, a partir de la DGT: 600 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Por qué ir a un taller independiente si el concesionario está a 50 km?",
         "a": "Porque desde Carme las dos distancias se parecen, y para mantenimiento o averías fuera de garantía puedes elegir. Lo que cubre la garantía de BMW se repara en la red oficial."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Igualada (B12), polígono Les Comes, a 10,3 km."},
        {"q": "¿Pierdo la garantía si hago las revisiones con vosotros?",
         "a": "No, si se sigue el plan de mantenimiento con piezas y aceites de la especificación correcta."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "847 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("080484")},
        {"etiqueta": "Turismos (2024)", "valor": "508 · 600 por cada 1.000 hab.", **F.idescat("080484")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 10,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 50 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 63,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080484"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}
META["carme"] = "BMW en Carme (Anoia): ITV en Igualada a 10,3 km, servicio oficial a 50 km y el taller especialista de la red a 63,8 km. Garantía y mantenimiento."

# ---------------------------------------------------------------- Òrrius
CIUDADES["orrius"] = {
    "h1": "Òrrius: concesionario BMW en Mataró, ITV en Argentona y especialista a 48,9 km",
    "entradilla": "Para salir de Òrrius hacia cualquier sitio, primero hay que tomar la BV-5106. Desde ahí, Mataró y Argentona quedan a unos 11 km y el taller especialista de la red, en Sant Joan Despí, a 48,9 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 48.9},
    "secciones": [
        {"id": "mataro-argentona", "h2": "Mataró para el concesionario, Argentona para la ITV",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la Via Sèrgia 2 de Mataró, a 11,4 km por carretera. La estación de ITV más cercana por carretera en el registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 11 km.",
             "Las revisiones que la marca convoca por un posible defecto se hacen en su red; si recibes ese aviso, la cita será en Mataró.",
         ]},
        {"id": "bv5106-c32", "h2": "Por la BV-5106 y la C-32 hasta Sant Joan Despí",
         "parrafos": [
             "En los tres kilómetros alrededor del centro no pasa ninguna autovía ni carretera principal. La ruta hasta la nave de Dasercars Barcelona baja por la BV-5106 y la C-1415c hasta la C-32, y sigue por la B-20: 48,9 km por carretera, 31,7 en línea recta.",
             "Òrrius está en el Maresme y no en el área metropolitana de Barcelona, así que la recogida del taller no cubre el municipio. Lo práctico es reservar el viaje para lo que pide un especialista: una caja automática que da tirones, un turbo que pierde empuje o un fallo de climatización que nadie ha localizado.",
         ]},
        {"id": "orrius-cifras", "h2": "812 vecinos, un 18 % más que en 2015",
         "parrafos": [
             "El padrón de 2025 da a Òrrius 812 habitantes, frente a 688 diez años antes, en un término de 5,66 km² a 259 metros de altitud. Idescat contaba 449 turismos en 2024, a partir de la DGT: 553 por cada 1.000 vecinos.",
             "El mar queda a unos 7 km en línea recta: lo bastante lejos para que el salitre no sea la preocupación principal, aunque no está de más un lavado de bajos después del verano si el coche baja a menudo a la costa.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano a Òrrius?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 11,4 km según bmw.es."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de Argentona (B08), en el polígono El Cros, a 11 km por carretera."},
        {"q": "¿Recogéis el coche en Òrrius?",
         "a": "No: la recogida del taller solo cubre el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "812 habitantes (+18 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("081537")},
        {"etiqueta": "Turismos (2024)", "valor": "449 · 553 por cada 1.000 hab.", **F.idescat("081537")},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 11 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 11,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 48,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081537"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["orrius"] = "BMW en Òrrius: servicio oficial en Mataró a 11,4 km, ITV en Argentona y el taller especialista de la red en Sant Joan Despí, a 48,9 km."

# ---------------------------------------------------------------- Castellcir
CIUDADES["castellcir"] = {
    "h1": "Castellcir: un BMW a 773 metros, ITV a 36 km y el taller de la red a 63",
    "entradilla": "Castellcir está en el Moianès, a 773 metros de altitud, y todo lo relacionado con el coche queda a más de treinta kilómetros: el taller autorizado BMW, la ITV y el taller especialista de la red. Ordenamos las tres opciones.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 63.1},
    "secciones": [
        {"id": "tres-destinos", "h2": "Tallcar, el CIM Vallès y Sant Joan Despí",
         "parrafos": [
             "El punto oficial BMW más próximo según bmw.es es Tallcar, un taller autorizado en la calle Suiza 6 de Castellar del Vallès, a 35 km por carretera. La estación de ITV más próxima por carretera en el registro de la Generalitat es la del CIM Vallès (B20), en Santa Perpètua de Mogoda, a 36,1 km. Y Dasercars Barcelona, el taller especialista de la red, está a 63,1 km.",
         ]},
        {"id": "c59-c33", "h2": "Seis carreteras hasta el Baix Llobregat",
         "parrafos": [
             "La ruta más corta encadena la BV-1310, la C-59, la BV-1341, la C-1413b, la C-33 y la B-20: 63,1 km por carretera y 43,8 en línea recta. La C-59 pasa a 1,9 km del centro del pueblo. Castellcir está fuera del área metropolitana de Barcelona y la recogida del taller no llega.",
             "Para no hacer el viaje en balde, conviene una llamada previa en la que digas el modelo, el año, los kilómetros y cómo se comporta la avería. Con esos datos se valora si es un caso de especialista o algo que un taller cercano puede resolver.",
         ]},
        {"id": "773-metros", "h2": "Casi ochocientos metros de altitud",
         "parrafos": [
             "A 773 metros, el frío del invierno exige más al arranque: un diésel necesita los calentadores en buen estado, y cualquier BMW, una batería con capacidad suficiente para todos sus consumos eléctricos.",
             "El líquido de frenos merece atención aparte en carreteras con pendiente: absorbe humedad con el tiempo y pierde eficacia al calentarse, y por eso el plan de BMW lo cambia por años y no por kilómetros.",
         ]},
        {"id": "castellcir-cifras", "h2": "804 vecinos y 405 turismos",
         "parrafos": [
             "Castellcir tenía 694 habitantes en 2015 y 804 en 2025, un 15,9 % más, en un término de 34,18 km². Idescat, a partir de la DGT, contaba 405 turismos en 2024: 504 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el taller BMW autorizado más cercano a Castellcir?",
         "a": "Tallcar, en la calle Suiza 6 de Castellar del Vallès, a 35 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la del CIM Vallès (B20), en Santa Perpètua de Mogoda, a 36,1 km."},
        {"q": "¿A cuánto queda vuestro taller?",
         "a": "A 63,1 km, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "804 habitantes (+15,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Moianès", **F.idescat("080556")},
        {"etiqueta": "Altitud", "valor": "773 m", **F.idescat("080556")},
        {"etiqueta": "Turismos (2024)", "valor": "405 · 504 por cada 1.000 hab.", **F.idescat("080556")},
        {"etiqueta": "Taller autorizado BMW", "valor": "Tallcar, Castellar del Vallès · 35 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20) · 36,1 km", **F.itv_cat},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080556"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["castellcir"] = "BMW en Castellcir (Moianès): taller autorizado en Castellar del Vallès, ITV en Santa Perpètua y el taller especialista de la red a 63,1 km."


def aplicar_meta():
    from comun import CIUDADES_DIR
    for slug, desc in META.items():
        assert len(desc) <= 160, (slug, len(desc))
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        cj["metaDescription"] = desc
        f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
        print("metaDescription", slug)


if __name__ == "__main__":
    aplicar_meta()
