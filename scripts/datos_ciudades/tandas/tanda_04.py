# Tanda 4 (producción): Griñón, Torrejón de la Calzada, Alella, Bigues i Riells,
# Santa Maria de Palautordera, Matadepera, Cervelló, Arenys de Munt,
# l'Ametlla del Vallès, Sant Fost de Campsentelles, Vilassar de Dalt, Tiana, Loeches.
# Saltadas por decisión del coordinador: tarazona y caspe (zona de Zaragoza sin dirección de taller).
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

# metaDescription nueva (las 13 tienen 0 impresiones y la antigua prometía ISTA,
# «diagnóstico oficial», recogida fuera del área metropolitana o «hasta un 50 %»).
# aplicar.py no toca metaDescription: se vuelca aparte (ver informe de la tanda).
META = {}

# ---------------------------------------------------------------- Griñón
CIUDADES["grinon"] = {
    "h1": "BMW en Griñón: ITV en Humanes, servicio oficial en Getafe y especialista en Alcobendas",
    "entradilla": "Para un BMW o un MINI de Griñón, lo más cercano está en los pueblos de al lado: la ITV en Humanes y el concesionario en Getafe. El taller especialista de la red queda al norte, a 51,2 km. Así se reparte cada cosa.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 51.2},
    "secciones": [
        {"id": "itv-humanes", "h2": "La inspección, a 8,1 km en la avenida de Fuenlabrada",
         "parrafos": [
             "Griñón no aparece con estación propia en el listado de la Comunidad de Madrid. La más próxima es la de Alcaravan ITV (estación 2829), en la avenida de Fuenlabrada 15 de Humanes: 8,1 km por carretera, poco más de seis en línea recta.",
             "Si el coche tiene que pasar por el taller antes, aprovecha esa visita para revisar luces, holguras y emisiones, y pide la cita en Humanes con el margen justo para corregir lo que salga.",
         ]},
        {"id": "vehinter-getafe", "h2": "Vehinter, en la carretera de Toledo, es el oficial más cercano",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto oficial más próximo en Vehinter, en la carretera Madrid-Toledo, término de Getafe, a 18,7 km. Lo que cubra la garantía de BMW se tramita allí.",
             "Lo demás —mantenimiento, una avería fuera de garantía, un segundo diagnóstico— lo puedes llevar a quien prefieras. Nosotros somos un taller independiente especializado en la marca, no parte de esa red.",
         ]},
        {"id": "r5-hasta-alcobendas", "h2": "51 kilómetros, con la R-5 como atajo",
         "parrafos": [
             "La ruta que da OpenStreetMap sale por la M-405 y la M-407, toma la R-5 hasta la M-30 y termina por la A-1 en la calle Valgrande de Alcobendas: 51,2 km. Es casi una diagonal completa de la región, así que tiene sentido para trabajos de especialista y no para cambiar unas escobillas.",
             "El taller trabaja de lunes a viernes en horario partido, de 9:00 a 14:00 y de 15:00 a 18:00. Si el trabajo dura más de un día, pregunta por el vehículo de cortesía al reservar: depende de disponibilidad.",
         ]},
        {"id": "parque-grinon", "h2": "611 turismos por cada mil vecinos",
         "parrafos": [
             "Griñón tenía 10.799 habitantes en el padrón de 2025, un 8,9 % más que en 2015, y 6.597 turismos censados según la Comunidad de Madrid con datos de la DGT. La proporción, 611 por cada 1.000, es muy superior a la de Madrid capital (388).",
             "Con la M-405 a menos de medio kilómetro del centro y la M-407 a menos de un kilómetro y medio, buena parte del uso diario es carretera autonómica con rotondas. Ahí sufren más frenos, silentblocks y embrague que en autovía.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Griñón?",
         "a": "En el listado oficial no figura ninguna dentro del municipio. La más cercana es Alcaravan ITV, en Humanes, a 8,1 km."},
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "Vehinter, en la carretera Madrid-Toledo (Getafe), a 18,7 km según bmw.es."},
        {"q": "¿Dónde está vuestro taller?",
         "a": "En la calle Valgrande 17 de Alcobendas, a 51,2 km de Griñón por la R-5 y la A-1."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "10.799 habitantes (+8,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "6.597 · 611 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "Alcaravan ITV, Humanes · 8,1 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 18,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 51,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["grinon"] = "Griñón: ITV más cercana en Humanes, servicio oficial BMW en Getafe y taller especialista independiente en Alcobendas, a 51,2 km. Ruta y datos."

# ---------------------------------------------------------------- Torrejón de la Calzada
CIUDADES["torrejon-de-la-calzada"] = {
    "h1": "Torrejón de la Calzada: tu BMW, de la A-42 al taller de Alcobendas",
    "entradilla": "En diez años, Torrejón de la Calzada ha pasado de 7.901 a 10.653 vecinos. Casi todo lo que necesita un BMW está en el corredor de la A-42: la ITV en Parla, el concesionario en Getafe y, por la misma autovía, el camino hacia nuestro taller.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 46.2},
    "secciones": [
        {"id": "un-tercio-mas", "h2": "Un 34,8 % más de vecinos en un término de 8,9 km²",
         "parrafos": [
             "El padrón del INE da 10.653 habitantes en 2025, frente a 7.901 en 2015. Con un término de solo 8,9 km², la densidad ronda los 1.197 habitantes por km², alta para un municipio de este tamaño.",
             "La Comunidad de Madrid contaba 6.095 turismos en 2025 a partir de la DGT, 572 por cada 1.000 vecinos. La A-42 pasa a menos de tres kilómetros del centro.",
         ]},
        {"id": "itv-parla", "h2": "La ITV, a 8,5 km en Parla",
         "parrafos": [
             "La estación oficial más próxima en el listado de la Comunidad es la de DEKRA ITV España (estación 2897), en la calle Roma 9 de Parla: 8,5 km por carretera. Queda mucho más cerca que Alcobendas, así que no compensa juntarla con ese viaje; mejor resolverla aparte.",
         ]},
        {"id": "getafe-o-alcobendas", "h2": "Getafe a 11,5 km, Alcobendas a 46,2",
         "parrafos": [
             "El servicio oficial BMW más cercano según bmw.es es Vehinter, en la carretera Madrid-Toledo, en Getafe, a 11,5 km. Para una reparación en garantía es la opción evidente.",
             "Hasta la nave de Dasercars hay 46,2 km: A-42, M-40, M-30 y A-1. Ese viaje encaja cuando quieres un especialista independiente para el mantenimiento o una avería que se resiste. Antes de moverte, el presupuesto se entrega por escrito y no se toca nada sin tu visto bueno.",
         ]},
        {"id": "a42-y-dpf", "h2": "Lo que hace la A-42 por un diésel",
         "parrafos": [
             "Un BMW diésel que solo hace trayectos de pocos kilómetros acumula hollín en el filtro de partículas sin llegar a quemarlo. Tener la A-42 al lado es una ventaja: un tramo de autovía a ritmo constante cada cierto tiempo permite que la regeneración termine. Si el testigo del filtro se enciende a menudo, no lo ignores; suele avisar antes de que el coche entre en modo de emergencia.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Torrejón de la Calzada?",
         "a": "La estación oficial más cercana es la de DEKRA ITV España, en la calle Roma 9 de Parla, a 8,5 km."},
        {"q": "¿A cuánto está vuestro taller?",
         "a": "A 46,2 km por carretera, en Alcobendas, por la A-42, la M-40, la M-30 y la A-1."},
        {"q": "¿Cuál es el servicio oficial BMW más próximo?",
         "a": "Vehinter, en Getafe, a 11,5 km según el localizador de bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "10.653 habitantes (+34,8 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "8,9 km²", **F.cartociudad},
        {"etiqueta": "Turismos (2025)", "valor": "6.095 · 572 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "DEKRA ITV España, Parla · 8,5 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 11,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 46,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["torrejon-de-la-calzada"] = "Torrejón de la Calzada: ITV en Parla a 8,5 km, servicio oficial BMW en Getafe y taller especialista independiente en Alcobendas por la A-42."

# ---------------------------------------------------------------- Alella
CIUDADES["alella"] = {
    "h1": "Alella: un BMW a 3 km del mar y a 29,1 km del taller especialista",
    "entradilla": "A tres kilómetros de la costa del Maresme, Alella tiene la B-20 y la C-32 casi en la puerta. Eso acerca Barcelona y también nuestro taller de Sant Joan Despí. Aquí tienes los datos para decidir.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 29.1},
    "secciones": [
        {"id": "b20", "h2": "Por la B-20, sin cruzar Barcelona",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc de Sant Joan Despí va entera por la B-20: 29,1 km por carretera, 23,9 en línea recta. Con la C-32 a menos de un kilómetro del centro y la B-20 a menos de dos, la salida es inmediata.",
             "Alella no forma parte del Área Metropolitana de Barcelona, que es el ámbito de la recogida del taller, así que esa opción no cubre el municipio: cuenta con traer el coche.",
         ]},
        {"id": "aire-salino", "h2": "El mar a 3,1 km: dónde se nota",
         "parrafos": [
             "La costa queda a unos 3,1 km del centro del municipio. No es primera línea, pero la humedad salina llega y trabaja despacio: en los tornillos y soportes del escape, en las tuberías de freno que van por los bajos y en los discos de un coche que pasa varios días sin moverse, que amanecen con una capa de óxido.",
             "Si notas vibración al frenar las primeras veces después de un fin de semana parado, suele ser eso y se va sola. Si no se va, toca revisar discos y pastillas.",
         ]},
        {"id": "sant-adria-y-badalona", "h2": "Concesionario en Sant Adrià, ITV en Badalona",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más cercano es Barcelona Premium en la calle Juan de Austria 1 de Sant Adrià de Besòs, junto a la Ronda Litoral, a 12,6 km. Es la referencia para todo lo que dependa de la garantía de BMW.",
             "En el registro de la Generalitat, la estación de ITV más próxima por carretera es la de Badalona (B02), en el carrer Indústria 427-449, a 11,6 km.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Alella?",
         "a": "No. La recogida del taller cubre solo el Área Metropolitana de Barcelona, y Alella queda fuera."},
        {"q": "¿Qué distancia hay hasta el taller?",
         "a": "29,1 km por la B-20 hasta Sant Joan Despí."},
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Badalona, estación B02 del carrer Indústria, a 11,6 km según el registro de la Generalitat."},
        {"q": "¿Afecta el aire del mar a los frenos?",
         "a": "Un coche parado varios días cerca de la costa acumula óxido superficial en los discos; con el uso desaparece, y si no, hay que revisarlos."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "10.262 habitantes (+6,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("080039")},
        {"etiqueta": "Turismos (2024)", "valor": "5.193 · 506 por cada 1.000 hab.", **F.idescat("080039")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 3,1 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Badalona (B02) · 11,6 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 29,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080039"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["alella"] = "Alella, en el Maresme: ruta por la B-20 al taller especialista BMW de Sant Joan Despí, ITV en Badalona y servicio oficial en Sant Adrià."

# ---------------------------------------------------------------- Bigues i Riells
CIUDADES["bigues-i-riells"] = {
    "h1": "Bigues i Riells: un BMW lejos de las autovías y a 52 km del taller",
    "entradilla": "La única carretera que pasa a menos de tres kilómetros del centro de Bigues i Riells es la C-59, y no hay autovía cerca. Todo queda a cierta distancia: el concesionario a 17,6 km, la ITV a 20,3 y nuestro taller a 51,6. Te contamos qué conviene resolver cerca y qué no.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 51.6},
    "secciones": [
        {"id": "municipio-disperso", "h2": "28,6 km² y 581 turismos por cada mil vecinos",
         "parrafos": [
             "Con 10.139 habitantes en 2025 (un 14,5 % más que en 2015) repartidos en 28,64 km², la densidad es de unos 354 por km². Idescat, con datos de la DGT, contaba 5.888 turismos en 2024: 581 por cada 1.000 vecinos, el doble que en Barcelona ciudad (281).",
             "Sin autovía al lado, los trayectos cortos por carretera local son habituales hasta llegar a la C-17. Un diésel con ese uso tiene difícil completar la regeneración del filtro de partículas, y la batería no siempre llega a cargarse del todo entre arranques.",
         ]},
        {"id": "granollers", "h2": "Lo oficial, en Granollers",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto oficial más próximo en Pruna Motor, en la C-17, km 19,060, en Granollers, a 17,6 km. La ITV más cercana por carretera en el registro de la Generalitat también está allí: Granollers (B18), en la avinguda Sant Julià del polígono El Congost, a 20,3 km.",
         ]},
        {"id": "cuando-bajar", "h2": "Cuándo merece la pena hacer 52 km",
         "parrafos": [
             "La ruta hasta Sant Joan Despí va por la BP-1432 hasta la C-17, sigue por la C-33 y entra en las rondas por la B-20. Son 51,6 km, y no tiene sentido recorrerlos por un cambio de neumáticos.",
             "Sí lo tiene para una avería concreta de BMW que no se ha resuelto cerca, un problema de distribución en un diésel N47 o B47, o un fallo eléctrico intermitente. El presupuesto llega por escrito y nada se empieza sin que lo apruebes, así que puedes decidir antes de mover el coche.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Bigues i Riells?",
         "a": "No. La recogida cubre solo el Área Metropolitana de Barcelona y el municipio queda fuera."},
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "Pruna Motor, en la C-17, km 19,060, en Granollers, a 17,6 km según bmw.es."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de Granollers (B18), en el polígono El Congost, a 20,3 km por carretera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "10.139 habitantes (+14,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080235")},
        {"etiqueta": "Turismos (2024)", "valor": "5.888 · 581 por cada 1.000 hab.", **F.idescat("080235")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 17,6 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 20,3 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 51,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080235"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["bigues-i-riells"] = "Bigues i Riells: concesionario BMW e ITV en Granollers y taller especialista independiente en Sant Joan Despí, a 51,6 km. Cuándo compensa el viaje."

# ---------------------------------------------------------------- Santa Maria de Palautordera
CIUDADES["santa-maria-de-palautordera"] = {
    "h1": "Santa Maria de Palautordera: ITV a 9,1 km y especialista BMW a 61,7 km",
    "entradilla": "Desde Santa Maria de Palautordera, lo que tienes cerca es la ITV de Sant Celoni. El servicio oficial BMW más próximo está en Mataró y nuestro taller, en Sant Joan Despí. Mejor saber de antemano qué se resuelve dónde.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 61.7},
    "secciones": [
        {"id": "itv-sant-celoni", "h2": "La inspección, en la carretera de Gualba",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es la de Sant Celoni (B26), en la carretera de Gualba 41-43, a 9,1 km. Es lo único de esta lista que tienes realmente a mano, y conviene aprovecharlo: la inspección, aquí; los viajes largos, solo cuando haga falta.",
         ]},
        {"id": "mataro-31-km", "h2": "El concesionario más cercano, a 30,7 km en Mataró",
         "parrafos": [
             "Según bmw.es, el punto oficial más próximo es Pruna Motor, en la Via Sèrgia 2 de Mataró, a 30,7 km por carretera. Para una reparación cubierta por la garantía de BMW, ese es el sitio.",
             "Entre Mataró y Sant Joan Despí, la decisión depende del trabajo: lo que es de garantía, al oficial; un mantenimiento por plan o un problema que necesita un especialista independiente, a nosotros.",
         ]},
        {"id": "ap7-hasta-el-taller", "h2": "61,7 km por la AP-7: para qué sí",
         "parrafos": [
             "La ruta sale por la BV-5301 a la AP-7, sigue por la C-33 y entra por la B-20 hasta el Tambor del Bruc: 61,7 km por carretera, 48,4 en línea recta. El municipio no está en el Área Metropolitana de Barcelona, así que la recogida del taller no llega.",
             "Con esa distancia, lo sensato es una llamada previa: modelo, año, kilómetros y lo que hace el coche. Muchas veces se puede orientar el problema y que el día que bajes ya esté la pieza.",
         ]},
        {"id": "palautordera-en-cifras", "h2": "10.080 vecinos y 5.439 turismos",
         "parrafos": [
             "El padrón de 2025 da 10.080 habitantes, un 10,7 % más que en 2015. Idescat contaba 5.439 turismos en 2024 a partir de la DGT, 540 por cada 1.000 vecinos. La BV-5301 pasa junto al centro y es la que lleva a la AP-7.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Santa Maria de Palautordera?",
         "a": "La estación más próxima en el registro de la Generalitat es Sant Celoni (B26), en la carretera de Gualba, a 9,1 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 30,7 km."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No: la recogida del taller cubre solo el Área Metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "10.080 habitantes (+10,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("082592")},
        {"etiqueta": "Turismos (2024)", "valor": "5.439 · 540 por cada 1.000 hab.", **F.idescat("082592")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 9,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 30,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 61,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082592"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["santa-maria-de-palautordera"] = "Santa Maria de Palautordera: ITV en Sant Celoni, servicio oficial BMW en Mataró y taller especialista independiente en Sant Joan Despí, a 61,7 km."

# ---------------------------------------------------------------- Matadepera
CIUDADES["matadepera"] = {
    "h1": "Matadepera: por la B-40 y la C-16, camino del especialista BMW",
    "entradilla": "Desde Matadepera, lo básico para un BMW queda cerca: el concesionario más próximo está en Terrassa, a 8,5 km, y la ITV de Viladecavalls, a 8. Nuestro taller queda a 39,4 km, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 39.4},
    "secciones": [
        {"id": "salir-por-terrassa", "h2": "Tres carreteras hasta Sant Joan Despí",
         "parrafos": [
             "La ruta toma la B-40, sigue por la C-16 y entra por la B-20: 39,4 km por carretera para 26,1 en línea recta.",
             "La B-40 pasa a un kilómetro y medio del centro y la BV-1221, a algo más de dos, así que la vía rápida queda a mano. Para un diésel que hace sobre todo trayectos cortos por el pueblo, conviene que de vez en cuando el viaje siga por autovía.",
         ]},
        {"id": "anoia-9", "h2": "Quadis Munich, en el carrer Anoia de Terrassa",
         "parrafos": [
             "El punto oficial más próximo según bmw.es es Quadis Munich, en el carrer Anoia 9 de Terrassa, a 8,5 km. Si tu BMW está en garantía y tiene una avería cubierta, la reparación se tramita allí.",
             "Si buscas un taller independiente especializado para el mantenimiento o un segundo diagnóstico, esa es nuestra parte. Trabajamos también MINI, que comparte electrónica y buena parte de los motores con BMW.",
         ]},
        {"id": "itv-can-trias", "h2": "ITV en el polígono Can Trias",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Viladecavalls (B03), en el carrer Joan Lluís Vives del polígono Can Trias, a 8 km. Matadepera tenía 9.776 habitantes en 2025, un 9,8 % más que diez años antes, y 5.047 turismos en 2024 según Idescat: 516 por cada 1.000.",
         ]},
    ],
    "faq": [
        {"q": "¿A qué distancia está el taller desde Matadepera?",
         "a": "A 39,4 km por carretera, por la B-40, la C-16 y la B-20."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima en el registro de la Generalitat es Viladecavalls (B03), a 8 km."},
        {"q": "¿Recogéis el coche en Matadepera?",
         "a": "No. La recogida del taller cubre solo el Área Metropolitana de Barcelona y Matadepera queda fuera."},
        {"q": "¿Reparáis MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.776 habitantes (+9,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("081206")},
        {"etiqueta": "Turismos (2024)", "valor": "5.047 · 516 por cada 1.000 hab.", **F.idescat("081206")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Terrassa) · 8,5 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Viladecavalls (B03) · 8 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 39,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081206"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["matadepera"] = "Matadepera: servicio oficial BMW en Terrassa, ITV en Viladecavalls y taller especialista independiente BMW y MINI en Sant Joan Despí, a 39,4 km."

# ---------------------------------------------------------------- Cervelló
CIUDADES["cervello"] = {
    "h1": "Cervelló: el taller especialista BMW queda más cerca que el concesionario",
    "entradilla": "Desde Cervelló, nuestro taller de Sant Joan Despí está a 15,8 km y el servicio oficial BMW más próximo, en Sant Boi, a 17,8. Es poco habitual que sea así, y además el municipio entra en el área de recogida del taller.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 15.8},
    "secciones": [
        {"id": "b24-a2", "h2": "15,8 km por la B-24 y la A-2",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc sale por la B-24 y sigue por la A-2: 15,8 km por carretera, 9,9 en línea recta. La B-24 y la N-340 pasan a menos de tres kilómetros del centro, así que el acceso es directo.",
         ]},
        {"id": "recogida-amb", "h2": "Dentro del Área Metropolitana de Barcelona",
         "parrafos": [
             "Cervelló es uno de los 36 municipios del Área Metropolitana de Barcelona. Para esos municipios, el taller ofrece recogida y entrega del coche y vehículo de cortesía, siempre sujetos a disponibilidad. Si te interesa, pídelo al concertar la cita y no el mismo día.",
         ]},
        {"id": "oficial-sant-boi", "h2": "Barcelona Premium, en la carretera del Prat",
         "parrafos": [
             "El punto oficial más cercano según el localizador de bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 17,8 km. Las llamadas a revisión de la marca y las reparaciones en garantía se hacen allí.",
             "El mantenimiento periódico no tiene por qué: la normativa europea de distribución de vehículos (Reglamento UE 461/2010) permite hacerlo en un taller independiente sin que el coche pierda la garantía, con dos condiciones: respetar los intervalos y usar recambios y aceites de la especificación correcta.",
         ]},
        {"id": "itv-sant-andreu", "h2": "La ITV, en la N-II a la altura de Sant Andreu de la Barca",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sant Andreu (B21), en la carretera N-II, punto kilométrico 592,5, en Sant Andreu de la Barca: 14,3 km. Cervelló tenía 9.743 habitantes en 2025 y 5.255 turismos en 2024 (Idescat a partir de la DGT), 539 por cada 1.000.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Cervelló?",
         "a": "Sí, Cervelló está en el Área Metropolitana de Barcelona. La recogida y entrega está sujeta a disponibilidad: pídela al reservar."},
        {"q": "¿Pierdo la garantía si hago la revisión con vosotros?",
         "a": "No, si se siguen los intervalos y especificaciones del plan de mantenimiento de BMW."},
        {"q": "¿Qué ITV tengo más cerca?",
         "a": "La de Sant Andreu de la Barca (B21), en la N-II, a 14,3 km por carretera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.743 habitantes (+10,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080689")},
        {"etiqueta": "Turismos (2024)", "valor": "5.255 · 539 por cada 1.000 hab.", **F.idescat("080689")},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 15,8 km", **F.osrm},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 17,8 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu de la Barca (B21) · 14,3 km", **F.itv_cat},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080689"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}
META["cervello"] = "Cervelló: taller especialista independiente BMW a 15,8 km en Sant Joan Despí, con recogida en el área metropolitana sujeta a disponibilidad. ITV y datos."

# ---------------------------------------------------------------- Arenys de Munt
CIUDADES["arenys-de-munt"] = {
    "h1": "Arenys de Munt: BMW en el Maresme interior, con el taller a 57 km",
    "entradilla": "La C-61 une Arenys de Munt con la C-32, que pasa a menos de tres kilómetros del centro. Por ahí empieza cualquier viaje con el coche: a Mataró, donde está el concesionario, o a Sant Joan Despí, donde está nuestro taller.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 56.6},
    "secciones": [
        {"id": "c61-c32", "h2": "C-61, C-32 y B-20: 56,6 km",
         "parrafos": [
             "La ruta hasta el taller baja por la C-61 hasta la C-32 y sigue por la B-20: 56,6 km por carretera, 47,5 en línea recta. El municipio no forma parte del Área Metropolitana de Barcelona, de modo que la recogida del taller no lo cubre.",
             "Antes de hacer ese trayecto, una llamada ayuda: con el modelo, el año, los kilómetros y el síntoma se puede orientar la avería y saber si hay que pedir alguna pieza.",
         ]},
        {"id": "pruna-mataro", "h2": "El concesionario, en la Via Sèrgia de Mataró",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto oficial más cercano en Pruna Motor, Via Sèrgia 2, Mataró, a 19,4 km. Para lo que cubre la garantía, esa es la dirección. Para un especialista independiente en BMW y MINI, la nuestra queda casi tres veces más lejos, y conviene que el trabajo lo justifique: un fallo que no se ha encontrado, una distribución ruidosa, un sistema de AdBlue que da guerra.",
         ]},
        {"id": "itv-sant-celoni", "h2": "La ITV del registro, en Sant Celoni",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera a Arenys de Munt es la de Sant Celoni (B26), en la carretera de Gualba 41-43, a 17,1 km.",
         ]},
        {"id": "arenys-en-cifras", "h2": "9.558 vecinos en 21,3 km²",
         "parrafos": [
             "El padrón de 2025 da 9.558 habitantes, un 9,4 % más que en 2015, en un término de 21,29 km². En 2024 había 4.675 turismos censados según Idescat, 489 por cada 1.000 vecinos. La línea de costa queda a unos 5 km del centro, lo bastante lejos para que el salitre no sea el problema principal del coche, pero no para olvidarse de los bajos si se aparca cerca del mar.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "56,6 km por carretera hasta Sant Joan Despí, por la C-61, la C-32 y la B-20."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 19,4 km según bmw.es."},
        {"q": "¿Recogéis el coche en Arenys de Munt?",
         "a": "No. La recogida cubre solo el Área Metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.558 habitantes (+9,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("080076")},
        {"etiqueta": "Turismos (2024)", "valor": "4.675 · 489 por cada 1.000 hab.", **F.idescat("080076")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 19,4 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 17,1 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 56,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080076"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["arenys-de-munt"] = "Arenys de Munt: servicio oficial BMW en Mataró, ITV en Sant Celoni y taller especialista independiente BMW y MINI en Sant Joan Despí, a 56,6 km."

# ---------------------------------------------------------------- l'Ametlla del Vallès
CIUDADES["l-ametlla-del-valles"] = {
    "h1": "L'Ametlla del Vallès: todo por la C-17, hasta el especialista BMW",
    "entradilla": "La C-17 pasa a menos de tres kilómetros de l'Ametlla y es el eje de todo lo que necesita un BMW: el concesionario está en esa misma carretera, la ITV en Granollers y nuestro taller, siguiendo hacia Barcelona, a 44,7 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 44.7},
    "secciones": [
        {"id": "c17-km-19", "h2": "El concesionario, en la misma C-17",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo es Pruna Motor, en la C-17, km 19,060, en Granollers: 10,7 km por carretera. Si el coche está en garantía, las reparaciones que cubre BMW pasan por allí.",
             "Para el mantenimiento y las averías fuera de garantía puedes elegir taller. Nosotros somos independientes y solo trabajamos BMW y MINI.",
         ]},
        {"id": "itv-el-congost", "h2": "La ITV, en el polígono El Congost",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es Granollers (B18), en la avinguda Sant Julià del polígono El Congost, a 13,4 km. Un consejo práctico: si la inspección cae cerca de una visita al taller, haz la revisión previa allí y la ITV a la vuelta.",
         ]},
        {"id": "ruta-al-taller", "h2": "44,7 km por la C-17, la C-33 y la B-20",
         "parrafos": [
             "La ruta hasta el Tambor del Bruc de Sant Joan Despí sigue la C-17, enlaza con la C-33 y entra por la B-20: 44,7 km. L'Ametlla queda fuera del Área Metropolitana de Barcelona, que es lo que cubre la recogida del taller.",
             "Compensa para trabajos que necesitan diagnosis específica de la marca o un especialista en los diésel N47, N57, B47 o B57. Para el día a día, el taller de confianza del pueblo sigue siendo lo más práctico.",
         ]},
        {"id": "ametlla-crece", "h2": "Un 14,1 % más de vecinos en diez años",
         "parrafos": [
             "L'Ametlla del Vallès tenía 8.303 habitantes en 2015 y 9.474 en 2025, según el padrón. En 2024, Idescat contaba 5.459 turismos: 576 por cada 1.000 vecinos, bastante más que los 281 de Barcelona ciudad.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano a l'Ametlla?",
         "a": "Pruna Motor, en la C-17, km 19,060 (Granollers), a 10,7 km según bmw.es."},
        {"q": "¿Qué ITV tengo más cerca?",
         "a": "La de Granollers (B18), en el polígono El Congost, a 13,4 km."},
        {"q": "¿A cuánto está vuestro taller?",
         "a": "A 44,7 km, en Sant Joan Despí, por la C-17, la C-33 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.474 habitantes (+14,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080057")},
        {"etiqueta": "Turismos (2024)", "valor": "5.459 · 576 por cada 1.000 hab.", **F.idescat("080057")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 10,7 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 13,4 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 44,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080057"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["l-ametlla-del-valles"] = "L'Ametlla del Vallès: concesionario BMW en la C-17, ITV en Granollers y taller especialista independiente BMW y MINI en Sant Joan Despí, a 44,7 km."

# ---------------------------------------------------------------- Sant Fost de Campsentelles
CIUDADES["sant-fost-de-campsentelles"] = {
    "h1": "Sant Fost de Campsentelles: por la B-500 hasta el taller BMW, 30,4 km",
    "entradilla": "Desde Sant Fost hay dos salidas naturales: por la B-500 hacia Badalona y las rondas, o hacia la C-33 y la C-17. Lo que te interesa de cada una si tienes un BMW.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 30.4},
    "secciones": [
        {"id": "b500", "h2": "La B-500, la C-33 y la B-20: 30,4 km",
         "parrafos": [
             "La ruta más corta hasta el carrer del Tambor del Bruc sale por la B-500, enlaza con la C-33 y sigue por la B-20: 30,4 km por carretera, 22,1 en línea recta. Aunque varios municipios vecinos sí están en el Área Metropolitana de Barcelona, Sant Fost no, y la recogida del taller no lo cubre.",
         ]},
        {"id": "itv-les-minetes", "h2": "La ITV, a 5,8 km en Santa Perpètua",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es CIM Vallès (B20), en el carrer Pont Vell del polígono Les Minetes, dentro del Centre Integral de Mercaderies de Santa Perpètua de Mogoda: 5,8 km. Con la C-33 y la C-17 a menos de tres kilómetros del centro, se llega sin complicaciones.",
         ]},
        {"id": "granollers-oficial", "h2": "Pruna Motor, a 10,6 km",
         "parrafos": [
             "El punto oficial BMW más cercano según bmw.es es Pruna Motor, en la C-17, km 19,060, en Granollers. Allí van las reparaciones que paga la garantía de la marca.",
             "Lo que no dependa de la garantía puedes hacerlo en un taller independiente. En el nuestro, la diagnosis se presupuesta antes de conectar el equipo, y la reparación también: nada se hace sin que sepas antes qué es y qué supone.",
         ]},
        {"id": "sant-fost-en-cifras", "h2": "553 turismos por cada mil vecinos",
         "parrafos": [
             "Sant Fost tenía 9.419 habitantes en 2025, un 9,5 % más que en 2015, y 5.213 turismos en 2024 según Idescat a partir de la DGT. La proporción, 553 por cada 1.000, casi dobla la de Barcelona ciudad (281).",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Sant Fost?",
         "a": "No. La recogida cubre solo el Área Metropolitana de Barcelona, y Sant Fost no forma parte de ella."},
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Santa Perpètua de Mogoda: CIM Vallès (B20), polígono Les Minetes, a 5,8 km."},
        {"q": "¿Cobráis la diagnosis?",
         "a": "Se presupuesta antes de hacerla, igual que la reparación."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.419 habitantes (+9,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("082093")},
        {"etiqueta": "Turismos (2024)", "valor": "5.213 · 553 por cada 1.000 hab.", **F.idescat("082093")},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20), Santa Perpètua · 5,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 10,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 30,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082093"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["sant-fost-de-campsentelles"] = "Sant Fost de Campsentelles: ITV en Santa Perpètua, servicio oficial BMW en Granollers y taller especialista independiente en Sant Joan Despí, a 30,4 km."

# ---------------------------------------------------------------- Vilassar de Dalt
CIUDADES["vilassar-de-dalt"] = {
    "h1": "Vilassar de Dalt: BMW cerca del mar, concesionario en Mataró y taller a 35,9 km",
    "entradilla": "El centro de Vilassar de Dalt queda a unos 2,8 km de la costa. El servicio oficial BMW de la comarca está en Mataró, a 8,5 km; nuestro taller, por la C-32, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 35.9},
    "secciones": [
        {"id": "via-sergia", "h2": "En Mataró, Pruna Motor",
         "parrafos": [
             "Según bmw.es, el punto oficial más cercano es Pruna Motor, en la Via Sèrgia 2 de Mataró, a 8,5 km por carretera y 5,7 en línea recta. Es donde se resuelve lo que cubre la garantía del fabricante.",
             "Para revisiones fuera de garantía, averías que ya han pasado por otro taller o un segundo diagnóstico antes de una reparación grande, puedes contar con un especialista independiente como nosotros.",
         ]},
        {"id": "a-28-km-del-mar", "h2": "A 2,8 km de la costa: bajos y conectores",
         "parrafos": [
             "La humedad que sube del mar no se queda en primera línea. En los coches que duermen en la calle, lo primero que lo acusa son las piezas metálicas sin pintar de los bajos —abrazaderas, soportes del escape, tornillería— y los conectores eléctricos expuestos, donde la sulfatación provoca fallos que aparecen y desaparecen.",
             "Si tu BMW enciende un testigo un día y al siguiente no, antes de cambiar sensores conviene mirar el conector y su masa. Y una vez al año, un lavado de bajos con agua dulce no está de más.",
         ]},
        {"id": "c32-al-taller", "h2": "35,9 km por la C-32",
         "parrafos": [
             "La ruta hasta el Tambor del Bruc va por la C-32, que pasa a un kilómetro del centro, y luego por la B-20: 35,9 km. El municipio no está en el Área Metropolitana de Barcelona, así que la recogida del taller no llega hasta aquí.",
         ]},
        {"id": "itv-y-cifras", "h2": "ITV en Argentona según el registro",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Argentona (B08), en el polígono El Cros, zona industrial sector sud, a 9,4 km. Vilassar de Dalt tenía 9.404 habitantes en 2025, un 4,9 % más que en 2015, y 4.657 turismos en 2024 según Idescat: 495 por cada 1.000.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el concesionario BMW más cercano a Vilassar de Dalt?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 8,5 km según bmw.es."},
        {"q": "¿Por qué falla la electrónica en coches cerca del mar?",
         "a": "La humedad salina sulfata los conectores expuestos y provoca fallos intermitentes; es lo primero que hay que revisar."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No: la recogida del taller cubre solo el Área Metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.404 habitantes (+4,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082140")},
        {"etiqueta": "Turismos (2024)", "valor": "4.657 · 495 por cada 1.000 hab.", **F.idescat("082140")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 2,8 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 8,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 35,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082140"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["vilassar-de-dalt"] = "Vilassar de Dalt: servicio oficial BMW en Mataró, ITV en Argentona y taller especialista independiente BMW en Sant Joan Despí, a 35,9 km por la C-32."

# ---------------------------------------------------------------- Tiana
CIUDADES["tiana"] = {
    "h1": "Tiana: especialista BMW a 25,7 km con recogida en el área metropolitana",
    "entradilla": "Tiana es del Maresme por comarca y del Área Metropolitana de Barcelona por pertenencia. Para quien tiene un BMW o un MINI, eso último importa: el taller ofrece recogida dentro de ese ámbito, sujeta a disponibilidad.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 25.7},
    "secciones": [
        {"id": "maresme-y-amb", "h2": "Maresme, pero dentro del área metropolitana",
         "parrafos": [
             "De los municipios del Maresme, Tiana es uno de los pocos que forman parte del Área Metropolitana de Barcelona. Es la razón por la que la recogida y entrega del coche, y el vehículo de cortesía, sí aplican aquí: siempre sujetos a disponibilidad, así que lo mejor es pedirlos al fijar la cita.",
             "Si prefieres traerlo tú, la ruta hasta Sant Joan Despí va por la B-20: 25,7 km por carretera, 22,1 en línea recta.",
         ]},
        {"id": "ronda-litoral", "h2": "El oficial, junto a la Ronda Litoral",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto oficial más cercano en Barcelona Premium, calle Juan de Austria 1, en Sant Adrià de Besòs: 12,2 km. Las campañas de revisión que convoque la marca se hacen en su red; para el resto del mantenimiento la elección de taller es tuya.",
         ]},
        {"id": "costa-tiana", "h2": "3,2 km hasta el mar",
         "parrafos": [
             "El centro de Tiana está a unos 3,2 km de la línea de costa. Con esa proximidad, el ambiente salino acaba notándose en el escape y en las fijaciones de los bajos con los años. No hace falta obsesionarse; sí revisar esas zonas cuando el coche sube al elevador por otro motivo.",
         ]},
        {"id": "itv-badalona", "h2": "La ITV de Badalona, a 9,2 km",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Badalona (B02), en el carrer Indústria 427-449, a 9,2 km. Tiana tenía 9.331 habitantes en 2025, un 10,9 % más que en 2015, en un término de 7,95 km², y 4.414 turismos en 2024 según Idescat (473 por cada 1.000).",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Tiana?",
         "a": "Sí. Tiana está en el Área Metropolitana de Barcelona y la recogida y entrega se ofrece sujeta a disponibilidad."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Barcelona Premium, en la calle Juan de Austria 1 de Sant Adrià de Besòs, a 12,2 km."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de Badalona (B02), a 9,2 km por carretera según la Generalitat."},
        {"q": "¿Atendéis MINI?",
         "a": "Sí. Comparten electrónica y buena parte de los motores con BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.331 habitantes (+10,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082824")},
        {"etiqueta": "Turismos (2024)", "valor": "4.414 · 473 por cada 1.000 hab.", **F.idescat("082824")},
        {"etiqueta": "ITV más cercana", "valor": "Badalona (B02) · 9,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Adrià de Besòs) · 12,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 25,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082824"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["tiana"] = "Tiana: taller especialista independiente BMW y MINI a 25,7 km, con recogida en el área metropolitana sujeta a disponibilidad. ITV en Badalona."

# ---------------------------------------------------------------- Loeches
CIUDADES["loeches"] = {
    "h1": "Loeches: 641 turismos por cada mil vecinos y el taller BMW a 40,4 km",
    "entradilla": "En Loeches hay 641 turismos por cada 1.000 vecinos, muchos más que en Madrid capital. Lo que necesitas cerca está en Arganda del Rey y Alcalá; el taller especialista de la red, en Alcobendas, por la M-50.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 40.4},
    "secciones": [
        {"id": "parque-loeches", "h2": "Un término de 44 km² y 5.936 turismos",
         "parrafos": [
             "Loeches tenía 9.261 habitantes en el padrón de 2025, un 12,8 % más que en 2015, repartidos en un término de 44,1 km². La Comunidad de Madrid, a partir de la DGT, contaba 5.936 turismos ese año: 641 por cada 1.000 vecinos, frente a 388 en Madrid capital.",
             "Con la M-300 y la M-206 como vías más próximas, el uso típico es carretera convencional. Ahí el desgaste se reparte entre frenos, neumáticos y amortiguación, y conviene no alargar los intervalos que marca el indicador de servicio del coche.",
         ]},
        {"id": "arganda-y-alcala", "h2": "ITV en Arganda, oficial en Alcalá",
         "parrafos": [
             "La estación oficial de ITV más próxima en el listado de la Comunidad es la de Laboratorio e Inspección de Vehículos (estación 2807), en el camino de San Martín de la Vega 8, en Arganda del Rey, a 11 km.",
             "Para la red de la marca, el localizador de bmw.es remite a Alcalá de Henares: AutoPremier tiene su punto de servicio en la calle Argentina 7, a 17,4 km de Loeches por carretera. Pasar las revisiones en otro sitio no deja el coche sin garantía; el Reglamento (UE) 461/2010 lo ampara mientras se siga el plan de mantenimiento con piezas y aceites de la especificación correcta.",
         ]},
        {"id": "m206-m50-r2", "h2": "Por la M-206, la M-50 y la R-2",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas sale por la M-206, toma la M-50 y termina por la R-2: 40,4 km por carretera, 26 en línea recta. Si el trabajo va a llevar varios días, pregunta por el vehículo de cortesía al reservar; depende de disponibilidad.",
             "Un término tan amplio tiene otra lectura: buena parte de los desplazamientos empiezan y terminan con el motor frío. Si tu BMW es diésel y apenas sale de la M-206, una vuelta larga por la M-50 cada pocas semanas ayuda a que el filtro de partículas complete su regeneración.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Loeches?",
         "a": "En Laboratorio e Inspección de Vehículos (estación 2807), camino de San Martín de la Vega 8, Arganda del Rey, a 11 km."},
        {"q": "Si llevo el coche a revisar con vosotros, ¿mantengo la garantía de BMW?",
         "a": "Sí, mientras se cumplan los intervalos y especificaciones del plan de mantenimiento."},
        {"q": "¿Qué carreteras se cogen desde Loeches hasta el taller?",
         "a": "La M-206, la M-50 y la R-2 hasta la calle Valgrande 17 de Alcobendas: 40,4 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.261 habitantes (+12,8 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "44,1 km²", **F.cartociudad},
        {"etiqueta": "Turismos (2025)", "valor": "5.936 · 641 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "Laboratorio e Inspección de Vehículos, Arganda del Rey · 11 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, c. Argentina 7 (Alcalá) · 17,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 40,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}
META["loeches"] = "Loeches: ITV en Arganda del Rey, servicio oficial BMW en Alcalá de Henares y taller especialista independiente en Alcobendas, a 40,4 km."
