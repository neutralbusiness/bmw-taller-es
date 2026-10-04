# Tanda 2 (producción): 14 ciudades. Texto escrito a mano a partir de datos/<slug>.json.
# Utebo se salta (zona de Zaragoza sin dirección de taller: pendiente de decisión de Martin).
# Se carga con piloto/aplicar.py tanda_2. META_DESCRIPTIONS se aplica aparte (ciudades sin
# impresiones en GSC cuya metaDescription prometía «hasta un 50 %», «oficial» o ISTA).
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

CIUDADES["barbera-del-valles"] = {
    "h1": "Barberà del Vallès: taller BMW de la red a 28 km y recogida dentro del AMB",
    "entradilla": "Barberà forma parte del Área Metropolitana de Barcelona, y eso cambia las cosas: el taller especialista de la red está en Sant Joan Despí, pero el coche puede viajar sin ti. Además, en Sabadell tienes un taller autorizado BMW y una ITV a pocos kilómetros.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 28.1},
    "secciones": [
        {"id": "recogida-desde-barbera", "h2": "Que el coche haga el viaje solo",
         "parrafos": [
             "Al estar dentro del área metropolitana, Barberà entra en la zona donde Dasercars Barcelona ofrece recogida y entrega del vehículo y coche de cortesía. Las dos cosas dependen de la disponibilidad de cada día, así que se piden al reservar y no con el coche ya parado en la puerta de casa.",
             "Si prefieres llevarlo tú, la ruta desde el centro sale a la B-30, toma un tramo de AP-7 y baja por la B-23 hasta el carrer del Tambor del Bruc: 28,1 km por carretera, 17,5 en línea recta.",
         ]},
        {"id": "sitjas-autorizado", "h2": "Sitjas Motor: el autorizado BMW está a 4 km, en Sabadell",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto de servicio oficial más próximo en la calle Quintana 64 de Sabadell: Sitjas Motor, que figura como taller autorizado, sin exposición de venta, a 4 km por carretera. Si buscabas dónde comprar un coche, no es ese; si necesitas una reparación que pague la garantía de BMW, es la referencia más cercana.",
             "Un taller independiente como el nuestro no compite con eso: atiende mantenimiento, averías fuera de garantía y diagnósticos que no han terminado de resolverse en otro sitio.",
         ]},
        {"id": "itv-sabadell-desde-barbera", "h2": "La ITV, al otro lado del límite municipal",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera al centro de Barberà es la de Sabadell (B24), gestionada por Applus, en el polígono Can Roqueta: 5,2 km por carretera y solo 2,1 en línea recta. La diferencia entre las dos cifras la ponen los accesos, no la distancia real.",
         ]},
        {"id": "ocho-kilometros-cuadrados", "h2": "33.987 vecinos en 8,31 km²",
         "parrafos": [
             "El término municipal es pequeño y está muy poblado: 33.987 habitantes en el padrón de 2025, unos 4.090 por kilómetro cuadrado. En 2024 había 16.008 turismos censados según Idescat a partir de la DGT, 471 por cada 1.000 habitantes.",
             "La N-150 cruza prácticamente el centro y la AP-7, la C-58 y la B-30 quedan a menos de dos kilómetros, así que muchos trayectos empiezan en autopista. Para un diésel es buena noticia: los recorridos a velocidad sostenida son los que permiten al filtro de partículas completar la regeneración. Lo que más sufre con ese uso son los neumáticos y los frenos en incorporaciones y retenciones.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Barberà del Vallès?",
         "a": "Sí: Barberà está dentro del área metropolitana de Barcelona, donde hay recogida y entrega sujeta a disponibilidad. Pídela al reservar."},
        {"q": "¿Cuál es el taller autorizado BMW más cercano?",
         "a": "Sitjas Motor, en la calle Quintana 64 de Sabadell, a 4 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima por carretera en el registro de la Generalitat es la de Sabadell (B24), en el polígono Can Roqueta, a 5,2 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "33.987 habitantes (+4,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082520")},
        {"etiqueta": "Turismos (2024)", "valor": "16.008 · 471 por cada 1.000 hab.", **F.idescat("082520")},
        {"etiqueta": "ITV más cercana", "valor": "Sabadell (B24) · 5,2 km", **F.itv_cat},
        {"etiqueta": "Taller autorizado BMW", "valor": "Sitjas Motor, Sabadell · 4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 28,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082520"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["sant-pere-de-ribes"] = {
    "h1": "Sant Pere de Ribes: BMW cerca del mar y especialista a 34 km por la C-32",
    "entradilla": "Con el servicio oficial y la ITV a un paso, en Vilanova i la Geltrú, la pregunta en Sant Pere de Ribes no es dónde hay un taller, sino cuándo merece la pena uno especializado en BMW. El nuestro está en Sant Joan Despí, a 34 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 34.0},
    "secciones": [
        {"id": "vilanova-a-mano", "h2": "Lo oficial y la inspección, en Vilanova i la Geltrú",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 6 km por carretera. En la misma ciudad está la ITV que el registro de la Generalitat da como más cercana por carretera: Vilanova (B17), de Applus, en la Ronda Europa, a 7 km.",
             "Tenerlo todo en el municipio vecino simplifica la rutina: la inspección y lo que dependa de la marca se resuelven sin salir del Garraf.",
         ]},
        {"id": "c32-garraf", "h2": "34 kilómetros por la C-32 y la B-25",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona sigue la C-32 hacia Barcelona y entra por la B-25 en el Baix Llobregat: 34 km por carretera y 26,5 en línea recta. Sant Pere de Ribes no pertenece al Área Metropolitana de Barcelona y la recogida del taller no llega hasta aquí; el coche lo traes tú.",
             "Ese trayecto compensa para lo que exige conocer la marca a fondo: una distribución que suena en un N47, el sistema de AdBlue que entra en cuenta atrás, un fallo eléctrico intermitente. Un cambio de pastillas, en cambio, no justifica el viaje.",
         ]},
        {"id": "a-tres-km-del-mar", "h2": "A 3,6 km de la costa: frenos y bajos",
         "parrafos": [
             "El centro del municipio queda a unos 3,6 km del mar. No es primera línea, pero el aire húmedo y salino llega. El efecto más visible está en los discos de freno de un coche que pasa varios días parado: aparece una capa de óxido que se va en las primeras frenadas o, si se repite mucho, deja marcas y vibración. Menos visible es lo de abajo: soportes de escape, anclajes y tornillería envejecen antes.",
             "Si el coche duerme en la calle, merece la pena mirar los bajos una vez al año y, ante un testigo eléctrico que aparece y desaparece, empezar por conectores y masas.",
         ]},
        {"id": "ribes-en-cifras", "h2": "Un 10,2 % más de vecinos que en 2015",
         "parrafos": [
             "El padrón pasó de 29.666 habitantes en 2015 a 32.705 en 2025, en un término de 40,8 km². Idescat, con datos de la DGT, contaba 13.853 turismos en 2024, 424 por cada 1.000 habitantes. La C-32 pasa a 1,4 km del centro y la C-31, a 2,5.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Sant Pere de Ribes?",
         "a": "Quadis Munich, en Vilanova i la Geltrú, a 6 km por carretera según bmw.es."},
        {"q": "¿Recogéis el coche en Sant Pere de Ribes?",
         "a": "No. La recogida del taller solo cubre el área metropolitana de Barcelona, y el Garraf queda fuera."},
        {"q": "¿Qué conviene revisar en un coche que vive cerca del mar?",
         "a": "Los discos de freno si pasa días parado, los bajos y los anclajes del escape, y los conectores ante cualquier fallo eléctrico intermitente."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "32.705 habitantes (+10,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Garraf", **F.idescat("082310")},
        {"etiqueta": "Turismos (2024)", "valor": "13.853 · 424 por cada 1.000 hab.", **F.idescat("082310")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 3,6 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Vilanova (B17) · 7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 6 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082310"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["villaviciosa-de-odon"] = {
    "h1": "Villaviciosa de Odón: tu BMW, del oeste de Madrid a Alcobendas por la M-40",
    "entradilla": "Desde Villaviciosa, Alcobendas queda en el extremo contrario del área metropolitana: 40,9 km. Antes de hacerlos, conviene saber qué tienes en Alcorcón, a menos de diez kilómetros, y para qué trabajos compensa cruzar.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 40.9},
    "secciones": [
        {"id": "alcorcon-al-lado", "h2": "Concesionario e ITV, en el término de Alcorcón",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es Vehinter, en la avenida de San Martín de Valdeiglesias 14-16 de Alcorcón, a 8,1 km por carretera. La estación de ITV oficial más cercana está en el p.k. 4,200 de la M-506, a 6,7 km; la explota ITV Villaviciosa, S.L. (estación 2871), aunque el listado de la Comunidad de Madrid la asigna al municipio de Alcorcón.",
         ]},
        {"id": "m40-hasta-alcobendas", "h2": "Al otro lado de la M-40",
         "parrafos": [
             "La ruta hasta la calle Valgrande sale por la M-501 y enlaza con la M-40 para rodear Madrid por el oeste y el norte: 40,9 km por carretera, 30,5 en línea recta. Villaviciosa está dentro del área metropolitana de Madrid, donde el taller ofrece recogida y entrega y vehículo de cortesía, ambos sujetos a disponibilidad. Con esta distancia, es lo primero que conviene preguntar al pedir cita.",
         ]},
        {"id": "garantia-y-plan", "h2": "Revisar fuera del concesionario con el coche en garantía",
         "parrafos": [
             "Muchos dueños de un BMW reciente dan por hecho que salir de la red oficial anula la garantía. No es así: el Reglamento (UE) 461/2010 protege la libertad de elegir taller siempre que el mantenimiento siga los intervalos y especificaciones del fabricante, con recambios y aceites de calidad equivalente.",
             "Lo que sí se queda en el concesionario son las reparaciones que paga la propia garantía de BMW.",
         ]},
        {"id": "parque-villaviciosa", "h2": "564 turismos por cada mil habitantes",
         "parrafos": [
             "Villaviciosa de Odón tenía 30.127 vecinos en el padrón de 2025, un 11,3 % más que diez años antes, repartidos en un término de 67,8 km². La Comunidad de Madrid contaba en 2025 16.994 turismos censados a partir de la DGT: 564 por cada 1.000 habitantes, una proporción muy superior a la de Madrid capital (388).",
             "Con la M-506 a 0,7 km del centro y la M-501 a 1,6, casi cualquier salida empieza en carretera interurbana, con rotondas en cada enlace. Pastillas, discos y neumáticos delanteros son lo que antes acusa ese uso; revisarlos cuando el coche entra por otra cosa ahorra una segunda visita.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano a Villaviciosa?",
         "a": "Vehinter, en la avenida de San Martín de Valdeiglesias 14-16 de Alcorcón, a 8,1 km según bmw.es."},
        {"q": "¿Pierdo la garantía si reviso el coche en un taller independiente?",
         "a": "No, si se siguen los intervalos y especificaciones del plan de mantenimiento del fabricante."},
        {"q": "¿Hay recogida del coche en Villaviciosa de Odón?",
         "a": "Está dentro del área metropolitana de Madrid: la recogida y entrega existe, sujeta a disponibilidad. Pregúntalo al reservar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "30.127 habitantes (+11,3 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "16.994 · 564 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "M-506 p.k. 4,200 (estación 2871) · 6,7 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Alcorcón) · 8,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 40,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

CIUDADES["premia-de-mar"] = {
    "h1": "Premià de Mar: un BMW en 2,11 km² junto al mar y el especialista a 38,4 km",
    "entradilla": "En Premià de Mar viven 13.948 personas por kilómetro cuadrado y el centro está a 0,6 km de la costa. Eso marca cómo vive un coche aquí, y de eso va esta página, además de la ruta hasta nuestro taller de Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 38.4},
    "secciones": [
        {"id": "calle-y-salitre", "h2": "Coche en la calle y a 0,6 km del mar",
         "parrafos": [
             "Con 29.431 habitantes en un término de 2,11 km², el garaje propio no es lo habitual y muchos coches pasan la noche al aire, cerca de la playa. El salitre trabaja despacio pero sin pausa: picadura en juntas de pintura y molduras, anclajes del escape y de la protección inferior que se oxidan y empiezan a vibrar, y bornes y conectores con sulfato verde.",
             "Lo que funciona es sencillo: agua dulce a presión en los bajos de vez en cuando, cera en la carrocería antes del invierno y, si el coche pasa días sin moverse, unas frenadas suaves al arrancar para limpiar el óxido de los discos antes de que marque la superficie.",
         ]},
        {"id": "maresme-oficial", "h2": "Servicio oficial en Mataró, ITV en Argentona",
         "parrafos": [
             "El punto de servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la Via Sergia 2 de Mataró, a 8,4 km por carretera. Para la ITV, la estación que el registro de la Generalitat da como más próxima por carretera es la de Argentona (B08), en el polígono El Cros, a 9,3 km.",
         ]},
        {"id": "por-la-c32", "h2": "Hasta Sant Joan Despí por la C-32 y las rondas",
         "parrafos": [
             "Premià de Mar no forma parte del Área Metropolitana de Barcelona, así que la recogida que ofrece el taller no llega hasta aquí. El trayecto suma 38,4 km por la C-32, la B-20 y la B-23; con la N-II pasando junto al centro y la C-32 a 1,4 km, salir hacia Barcelona es directo.",
             "Tiene sentido para una avería que pida diagnosis específica de BMW o para un mantenimiento hecho con el plan de la marca. Una revisión de bajos por el salitre, en cambio, te la puede hacer cualquier buen taller del Maresme.",
         ]},
        {"id": "premia-en-cifras", "h2": "29.431 vecinos y 11.996 turismos",
         "parrafos": [
             "El padrón de 2025 da 29.431 habitantes, un 5,3 % más que en 2015 (27.944). En 2024 había 11.996 turismos según Idescat a partir de la DGT: 408 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué le hace el salitre a un coche aparcado en Premià?",
         "a": "Acelera el óxido en anclajes de escape, bajos y discos de freno, y la sulfatación de conectores. Aclarar los bajos con agua dulce ayuda."},
        {"q": "¿Recogéis el coche en Premià de Mar?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sergia 2 de Mataró, a 8,4 km por carretera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "29.431 habitantes (+5,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("081727")},
        {"etiqueta": "Turismos (2024)", "valor": "11.996 · 408 por cada 1.000 hab.", **F.idescat("081727")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 0,6 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 9,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 8,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 38,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081727"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["martorell"] = {
    "h1": "Martorell, entre la AP-7 y la A-2: el taller BMW de la red a 19,8 km",
    "entradilla": "Desde Martorell, nuestro taller y el servicio oficial BMW más próximo quedan casi a la misma distancia, en direcciones opuestas. La ITV, en cambio, está a la vuelta de la esquina, en Sant Andreu de la Barca.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 19.8},
    "secciones": [
        {"id": "empate-de-distancias", "h2": "19,8 km a un lado, 18,4 km al otro",
         "parrafos": [
             "El servicio oficial BMW más próximo que recoge el localizador de bmw.es es Quadis Munich, en el carrer Vallespir 19 de Sant Cugat del Vallès, a 18,4 km por carretera. Dasercars Barcelona, en Sant Joan Despí, queda a 19,8 km por la N-IIa y la A-2, y a 15,9 en línea recta.",
             "Con la distancia prácticamente empatada, lo que decide es el tipo de trabajo. Lo que paga la garantía de BMW, en la red oficial; mantenimiento, averías de un coche con años o un segundo diagnóstico antes de aceptar una reparación cara, en un taller independiente especializado.",
         ]},
        {"id": "itv-sant-andreu", "h2": "La ITV, a 3,1 km por la N-II",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera al centro de Martorell es la de Sant Andreu de la Barca (B21), de Applus, en la N-II, p.k. 592,5: 3,1 km. Está tan cerca que lo práctico es repasar luces, frenos y emisiones antes de pedir cita, y no ir a ciegas.",
         ]},
        {"id": "nudo-de-autopistas", "h2": "Cinco carreteras en tres kilómetros",
         "parrafos": [
             "A menos de tres kilómetros del centro pasan la AP-7 (a 0,2 km), la A-2, la B-224, la C-54 y la N-IIa. Un coche que sale a diario por esas vías trabaja a temperatura estable y regenera el filtro de partículas sin problemas, pero acumula kilómetros deprisa: los intervalos de aceite, frenos y neumáticos llegan antes de lo que uno espera.",
         ]},
        {"id": "martorell-688", "h2": "688 turismos por cada mil habitantes",
         "parrafos": [
             "Idescat, con datos de la DGT, contaba en Martorell 20.081 turismos en 2024 para 29.175 habitantes en 2025: 688 por cada 1.000, más del doble que en Barcelona ciudad (281). La población ha crecido un 5,3 % desde los 27.694 vecinos de 2015.",
             "Martorell está en el Baix Llobregat pero no forma parte del Área Metropolitana de Barcelona, así que la recogida del taller no llega hasta aquí.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué está más cerca de Martorell, vuestro taller o el concesionario?",
         "a": "Casi lo mismo: 19,8 km hasta Dasercars Barcelona (Sant Joan Despí) y 18,4 km hasta Quadis Munich (Sant Cugat del Vallès)."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Sant Andreu de la Barca (B21), en la N-II, a 3,1 km según el registro de la Generalitat."},
        {"q": "¿Cómo se presupuesta un trabajo?",
         "a": "Por escrito y antes de tocar nada: no se empieza sin tu visto bueno. La diagnosis también lleva su propio presupuesto."},
        {"q": "¿Recogéis el coche en Martorell?",
         "a": "No. La recogida cubre el área metropolitana de Barcelona, y Martorell queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "29.175 habitantes (+5,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("081141")},
        {"etiqueta": "Turismos (2024)", "valor": "20.081 · 688 por cada 1.000 hab.", **F.idescat("081141")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu de la Barca (B21) · 3,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Cugat del Vallès · 18,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 19,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081141"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["sant-vicenc-dels-horts"] = {
    "h1": "Sant Vicenç dels Horts: el especialista BMW queda más cerca que el concesionario",
    "entradilla": "Hay 8,2 km por la A-2 desde Sant Vicenç dels Horts hasta nuestro taller de Sant Joan Despí, y 10,3 hasta el servicio oficial BMW de Sant Boi. Aquí la opción independiente es la que tienes más a mano; te contamos qué ofrece cada una.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 8.2},
    "secciones": [
        {"id": "ocho-kilometros-por-la-a2", "h2": "8,2 kilómetros por la A-2",
         "parrafos": [
             "La nave de Dasercars Barcelona, en el carrer del Tambor del Bruc 3, está a 5,1 km en línea recta del centro de Sant Vicenç y a 8,2 por carretera, siguiendo la A-2. A esa distancia se puede dejar el coche por la mañana y organizar el día sin depender de él.",
             "Sant Vicenç dels Horts pertenece al Área Metropolitana de Barcelona, de modo que también puedes pedir que recojan y devuelvan el coche, o un vehículo de cortesía mientras dura la reparación. Ambas cosas están sujetas a disponibilidad: mejor solicitarlas al reservar.",
         ]},
        {"id": "sant-boi-oficial", "h2": "El oficial, en la carretera del Prat de Sant Boi",
         "parrafos": [
             "El punto de servicio oficial BMW más próximo según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 10,3 km por carretera. Las campañas de revisión que convoque BMW para tu bastidor se hacen en la red oficial, y conviene no dejarlas pasar.",
             "Para el resto —mantenimiento, desgaste, averías fuera de garantía— la decisión es tuya, y la cercanía juega a favor del taller especializado.",
         ]},
        {"id": "itv-sant-just", "h2": "La ITV de referencia, en Sant Just Desvern",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sant Just Desvern (B05), de Applus, en la avinguda de la Riera, dentro de un polígono industrial: 9,6 km por carretera, 4,7 en línea recta.",
         ]},
        {"id": "ocho-vias", "h2": "Ocho carreteras a menos de tres kilómetros",
         "parrafos": [
             "Desde el centro tienes cerca la BV-2002, la A-2, la BV-2005, la B-23, la N-IIa, la N-340, la C-1413a y la B-24. Es un municipio de 9,12 km² con 28.746 vecinos en 2025, un 2,7 % más que en 2015, y 13.342 turismos en 2024: 464 por cada 1.000 habitantes según Idescat.",
             "Entre travesías, semáforos y rotondas, un BMW con arranque y parada automático hace trabajar mucho a su batería AGM. Cuando toque cambiarla, la nueva hay que registrarla en la centralita para que la carga se ajuste a ella.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué queda más cerca de Sant Vicenç, vuestro taller o el concesionario?",
         "a": "Nuestro taller: 8,2 km por la A-2, frente a 10,3 km hasta el servicio oficial de Sant Boi."},
        {"q": "¿Hay recogida del coche en Sant Vicenç dels Horts?",
         "a": "Sí, dentro del área metropolitana de Barcelona, sujeta a disponibilidad."},
        {"q": "¿Por qué hay que registrar la batería nueva de un BMW?",
         "a": "Porque, si no se registra, la centralita sigue cargando como si fuera la vieja y la nueva se degrada antes de tiempo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "28.746 habitantes (+2,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082634")},
        {"etiqueta": "Turismos (2024)", "valor": "13.342 · 464 por cada 1.000 hab.", **F.idescat("082634")},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 8,2 km", **F.osrm},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Boi · 10,3 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 9,6 km", **F.itv_cat},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082634"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["molins-de-rei"] = {
    "h1": "Molins de Rei: 9,6 km por la B-23 hasta el taller especialista BMW",
    "entradilla": "La B-23 pasa a medio kilómetro del centro de Molins de Rei y deja casi en la puerta de nuestro taller de Sant Joan Despí. Aquí va lo práctico: distancias, servicio oficial, ITV y lo que suele pedir un coche que hace pocos kilómetros.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 9.6},
    "secciones": [
        {"id": "b23-directa", "h2": "Una sola carretera hasta el Tambor del Bruc",
         "parrafos": [
             "Entre Molins de Rei y Dasercars Barcelona hay 9,6 km por carretera, 6,5 en línea recta, y prácticamente todo por la B-23. El taller abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00.",
             "Molins forma parte del Área Metropolitana de Barcelona, así que, si no puedes acercar el coche, pide la recogida y entrega al reservar: existe, pero está sujeta a disponibilidad.",
         ]},
        {"id": "pocos-kilometros", "h2": "Si el coche apenas sale del pueblo",
         "parrafos": [
             "Si tu BMW hace sobre todo trayectos cortos, el desgaste es más traicionero que el de la autopista: el aceite no alcanza su temperatura el tiempo suficiente y acumula condensación, la batería no llega a recuperarse de cada arranque y, en los diésel, el filtro de partículas se llena sin completar la regeneración.",
             "Tres hábitos ayudan: cambiar el aceite por tiempo aunque no se agote el intervalo de kilómetros, sacar el coche a la B-23 o a la A-2 de vez en cuando a velocidad sostenida y vigilar la batería antes del invierno.",
         ]},
        {"id": "sant-boi-y-sant-just", "h2": "Servicio oficial e ITV, a poco más de 10 km",
         "parrafos": [
             "Según el localizador de bmw.es, el punto de servicio oficial BMW más próximo es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 11,7 km por carretera: más lejos que nuestro taller. La estación de ITV más próxima por carretera en el registro de la Generalitat es la de Sant Just Desvern (B05), en la avinguda de la Riera, a 10,9 km.",
         ]},
        {"id": "molins-crece", "h2": "27.300 vecinos, un 8,5 % más que en 2015",
         "parrafos": [
             "Molins de Rei tenía 25.155 habitantes en 2015 y 27.300 en 2025 según el padrón, en un término de 15,94 km². En 2024 había 11.771 turismos censados (Idescat, a partir de la DGT): 431 por cada 1.000 habitantes. A menos de tres kilómetros del centro pasan, además de la B-23, la C-1413a, la N-340, la A-2 y la B-24.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuánto hay desde Molins de Rei hasta vuestro taller?",
         "a": "9,6 km por carretera, casi todo por la B-23, hasta Sant Joan Despí."},
        {"q": "¿Recogéis el coche en Molins?",
         "a": "Sí, dentro del área metropolitana de Barcelona hay recogida y entrega, sujeta a disponibilidad."},
        {"q": "¿Por qué cambiar el aceite por tiempo si hago pocos kilómetros?",
         "a": "Porque en trayectos cortos acumula humedad y restos de combustible y se degrada aunque el cuentakilómetros apenas avance."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "27.300 habitantes (+8,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("081234")},
        {"etiqueta": "Turismos (2024)", "valor": "11.771 · 431 por cada 1.000 hab.", **F.idescat("081234")},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 9,6 km", **F.osrm},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Boi · 11,7 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 10,9 km", **F.itv_cat},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081234"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["castellar-del-valles"] = {
    "h1": "Castellar del Vallès: autorizado BMW en el pueblo, especialista independiente a 47 km",
    "entradilla": "Lo decimos de entrada: en Castellar del Vallès tienes un taller autorizado BMW a poco más de un kilómetro del centro, y nuestro taller queda a 47 km, en Sant Joan Despí. Para la mayoría de cosas gana lo cercano; aquí explicamos cuándo no.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 47.0},
    "secciones": [
        {"id": "tallcar-calle-suiza", "h2": "Tallcar, en la calle Suiza",
         "parrafos": [
             "En el localizador de bmw.es aparece Tallcar, taller autorizado BMW, en la calle Suiza 6 del propio municipio, a 1,1 km del centro. Es un punto de servicio, no una exposición de venta. Allí se hacen las campañas que convoca la marca y las reparaciones que paga la garantía del fabricante.",
             "Nosotros no somos Tallcar. Somos Dasercars, un taller independiente especializado en BMW y MINI, y lo aclaramos porque es fácil confundirse al buscar «taller BMW» desde Castellar.",
         ]},
        {"id": "cuando-47-km", "h2": "Cuándo tiene sentido hacer 47 kilómetros",
         "parrafos": [
             "El trayecto hasta Dasercars Barcelona es largo y encadena muchas carreteras: C-1415a, BV-1248, C-58C, C-58, AP-7 y B-23, 47 km en total y 27,8 en línea recta. Castellar no está en el Área Metropolitana de Barcelona, y la recogida del taller no llega.",
             "Compensa cuando quieres un taller independiente para un BMW fuera de garantía, o cuando una avería ya ha pasado por otras manos sin solución:",
         ],
         "lista": [
             "un consumo de aceite que nadie ha sabido explicar;",
             "un diésel N57 o B57 que pierde potencia a ratos;",
             "una homologación de escape o de gases que necesite REDISTA.",
         ]},
        {"id": "itv-desde-castellar", "h2": "Para la ITV, a Sabadell",
         "parrafos": [
             "La estación más próxima por carretera según el registro de la Generalitat es la de Sabadell (B24), gestionada por Applus, en el polígono Can Roqueta: 12,8 km por carretera y 10 en línea recta.",
         ]},
        {"id": "castellar-en-cifras", "h2": "25.422 vecinos y 516 turismos por cada mil",
         "parrafos": [
             "El padrón de 2025 da a Castellar 25.422 habitantes, un 8,4 % más que en 2015 (23.442). Idescat, con datos de la DGT, contaba 13.111 turismos en 2024: 516 por cada 1.000 vecinos. El término mide 44,91 km², con una densidad de 566 habitantes por kilómetro cuadrado, y el núcleo está a 331 metros de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay taller autorizado BMW en Castellar del Vallès?",
         "a": "Sí: Tallcar, en la calle Suiza 6, según el localizador de bmw.es."},
        {"q": "¿Sois Tallcar?",
         "a": "No. Somos Dasercars, taller independiente especializado en BMW, con nave en Sant Joan Despí, a 47 km."},
        {"q": "¿Recogéis el coche en Castellar?",
         "a": "No: la recogida solo cubre el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "25.422 habitantes (+8,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("080517")},
        {"etiqueta": "Turismos (2024)", "valor": "13.111 · 516 por cada 1.000 hab.", **F.idescat("080517")},
        {"etiqueta": "Taller autorizado BMW", "valor": "Tallcar, c. Suiza 6 · 1,1 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sabadell (B24) · 12,8 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 47 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080517"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["mejorada-del-campo"] = {
    "h1": "Mejorada del Campo: ITV en el polígono y taller BMW a 33,4 km por la R-3",
    "entradilla": "Para pasar la inspección, en Mejorada del Campo no hace falta salir del municipio: la estación está en su polígono industrial. El taller especialista de la red, en cambio, queda en Alcobendas, a 33,4 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 33.4},
    "secciones": [
        {"id": "itv-calle-levante", "h2": "La ITV, en la calle Levante",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid incluye una estación dentro del término: la de ITV Barbastro (estación 2819), en la calle Levante 10 del polígono industrial de Mejorada del Campo.",
             "Antes de ir, una vuelta alrededor del coche evita un rechazo por detalles: todas las luces, incluida la de la matrícula, el estado de las escobillas, el dibujo de los neumáticos y que no quede ningún testigo encendido en el cuadro.",
         ]},
        {"id": "r3-m40-m12", "h2": "Por la R-3, la M-40 y la M-12",
         "parrafos": [
             "Hasta la calle Valgrande de Alcobendas hay 33,4 km por carretera y 21,6 en línea recta: R-3, M-40 y M-12. Mejorada forma parte del área metropolitana de Madrid, donde el taller ofrece recogida y entrega del coche y vehículo de cortesía, siempre según disponibilidad.",
         ]},
        {"id": "oficial-la-garena", "h2": "El servicio oficial, en La Garena de Alcalá",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo es AutoPremier, en la calle Argentina 7 del polígono La Garena de Alcalá de Henares, a 15,5 km por carretera. Para lo que dependa de la garantía de BMW, esa es la referencia.",
             "El taller independiente entra en juego para el resto: mantenimiento, desgaste y averías concretas de la marca, como la cadena de un N47 o el sistema SCR de los diésel con AdBlue.",
         ]},
        {"id": "mejorada-en-cifras", "h2": "Un 9,4 % más de vecinos en diez años",
         "parrafos": [
             "Mejorada del Campo pasó de 22.902 habitantes en 2015 a 25.049 en 2025. En 2025 tenía 13.888 turismos según la Comunidad de Madrid a partir de la DGT: 554 por cada 1.000 vecinos. La M-208, la M-203 y la R-3 pasan a poco más de un kilómetro del centro, que está a 580 metros de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Mejorada del Campo?",
         "a": "Sí: la estación 2819 de ITV Barbastro, en la calle Levante 10 del polígono industrial, según la Comunidad de Madrid."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 33,4 km, en la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. Se diagnostican y mantienen con el mismo equipo que los BMW, con los que comparten buena parte de motores y electrónica."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "25.049 habitantes (+9,4 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "13.888 · 554 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "ITV Barbastro (2819), c/ Levante 10", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 15,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 33,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

CIUDADES["el-masnou"] = {
    "h1": "El Masnou: lo oficial, hacia Barcelona; el especialista BMW, a 31,9 km",
    "entradilla": "Desde El Masnou, lo que tiene que ver con BMW queda hacia el sur: el servicio oficial en Sant Adrià de Besòs, la ITV en Badalona y nuestro taller en Sant Joan Despí. Las distancias, sin adornos, y lo que conviene saber de la garantía.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 31.9},
    "secciones": [
        {"id": "hacia-el-besos", "h2": "Servicio oficial en Sant Adrià, ITV en Badalona",
         "parrafos": [
             "El punto de servicio oficial BMW más próximo según bmw.es es Barcelona Premium, en la calle Juan de Austria 1 de Sant Adrià de Besòs, junto a la Ronda Litoral, a 12,9 km por carretera. La ITV más próxima por carretera en el registro de la Generalitat es la de Badalona (B02), en el carrer de la Indústria 427-449, a 11,9 km.",
         ]},
        {"id": "b20-b23", "h2": "31,9 km por la B-20 y la B-23",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona rodea la ciudad por la Ronda de Dalt (B-20) y sale por la B-23: 31,9 km por carretera, 25,1 en línea recta. El Masnou no forma parte del Área Metropolitana de Barcelona —Montgat, su vecino, sí—, así que la recogida del taller no llega hasta aquí.",
         ]},
        {"id": "garantia-sin-concesionario", "h2": "La garantía no te ata al concesionario",
         "parrafos": [
             "Una duda frecuente con un BMW de pocos años: si lo reviso fuera de la red, ¿la pierdo? La norma europea que regula la posventa, el Reglamento (UE) 461/2010, dice que no, mientras el mantenimiento respete los intervalos y especificaciones del fabricante. Guarda la factura con el detalle de piezas y aceites: es tu prueba.",
             "Lo que pague la propia garantía de BMW, eso sí, se repara en la red oficial.",
         ]},
        {"id": "masnou-junto-al-mar", "h2": "A 0,9 km del mar",
         "parrafos": [
             "El centro de El Masnou queda a 0,9 km de la costa, con la N-II pegada al núcleo y la C-32 a 0,9 km. Un coche que duerme cerca de la playa agradece algo tan simple como aclarar los bajos con agua dulce de vez en cuando y no dejar pasar un ruido metálico en el escape: muchas veces es un soporte oxidado.",
             "El municipio tenía 24.761 habitantes en 2025, un 8 % más que en 2015, y 11.161 turismos en 2024 según Idescat a partir de la DGT: 451 por cada 1.000 vecinos, en un término de 3,39 km².",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano a El Masnou?",
         "a": "Barcelona Premium, en la calle Juan de Austria 1 de Sant Adrià de Besòs, a 12,9 km según bmw.es."},
        {"q": "¿Recogéis el coche en El Masnou?",
         "a": "No: la recogida cubre solo el área metropolitana de Barcelona, y El Masnou queda fuera."},
        {"q": "¿Puedo hacer las revisiones fuera del concesionario sin perder la garantía?",
         "a": "Sí, siguiendo los intervalos y especificaciones del plan de mantenimiento de BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "24.761 habitantes (+8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("081189")},
        {"etiqueta": "Turismos (2024)", "valor": "11.161 · 451 por cada 1.000 hab.", **F.idescat("081189")},
        {"etiqueta": "ITV más cercana", "valor": "Badalona (B02) · 11,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Adrià de Besòs · 12,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 31,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081189"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["vilassar-de-mar"] = {
    "h1": "Vilassar de Mar: oficial e ITV a 5 km, especialista BMW a 42,1 km",
    "entradilla": "Si vives en Vilassar de Mar, el servicio oficial BMW y la ITV te quedan a unos cinco kilómetros, en Mataró y Argentona. Nuestro taller está a 42,1 km, en Sant Joan Despí. Preferimos ayudarte a decidir antes que venderte un viaje.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 42.1},
    "secciones": [
        {"id": "mataro-y-argentona", "h2": "Mataró y Argentona, a un paso",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial más próximo es Pruna Motor, en la Via Sergia 2 de Mataró, a 4,8 km por carretera. La estación de ITV más próxima por carretera en el registro de la Generalitat es la de Argentona (B08), de Applus, en el polígono El Cros, a 5,4 km.",
         ]},
        {"id": "que-justifica-el-viaje", "h2": "Qué justifica 42 kilómetros y qué no",
         "parrafos": [
             "La ruta, por la C-32, la B-20 y la B-23, suma 42,1 km. Antes de hacerla, llama con el modelo, el año, los kilómetros y el síntoma: muchas veces se puede orientar el problema por teléfono y decidir si conviene bajar. Vilassar de Mar no está en el Área Metropolitana de Barcelona, que es lo que cubre la recogida del taller, así que el coche lo traes tú.",
         ],
         "lista": [
             "Sí: una avería eléctrica que ha vuelto después de repararla.",
             "Sí: el aviso de AdBlue con cuenta atrás o un fallo del SCR sin diagnóstico claro.",
             "Sí: ruido de distribución en un diésel N47, N57 o B47.",
             "No: neumáticos, escobillas, una lámpara o una revisión sencilla.",
             "No: lo que cubra la garantía de BMW, que va a la red oficial.",
         ]},
        {"id": "medio-kilometro-de-playa", "h2": "A medio kilómetro de la playa",
         "parrafos": [
             "El centro de Vilassar de Mar está a 0,5 km de la costa, y la N-II lo recorre a 0,3 km. En un coche que vive aquí, lo que más acusa el ambiente salino es lo que no se ve: la tornillería de los bajos, los tubos de freno, los soportes del escape. Al cambiar neumáticos o pastillas es buen momento para que alguien eche un vistazo con el coche elevado.",
         ]},
        {"id": "vilassar-en-cifras", "h2": "21.227 vecinos en 4 km²",
         "parrafos": [
             "Vilassar de Mar tenía 21.227 habitantes en el padrón de 2025, frente a 20.447 en 2015 (un 3,8 % más). En 2024 había 9.638 turismos según Idescat a partir de la DGT, 454 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Vilassar de Mar?",
         "a": "La estación más próxima por carretera en el registro de la Generalitat es la de Argentona (B08), a 5,4 km."},
        {"q": "¿Merece la pena llevar el coche hasta Sant Joan Despí?",
         "a": "Para una avería específica de BMW que no se ha resuelto cerca, sí; para mantenimiento sencillo, no."},
        {"q": "¿Recogéis el coche en Vilassar?",
         "a": "No: la recogida cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "21.227 habitantes (+3,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082191")},
        {"etiqueta": "Turismos (2024)", "valor": "9.638 · 454 por cada 1.000 hab.", **F.idescat("082191")},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 5,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 4,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 42,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082191"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["san-martin-de-la-vega"] = {
    "h1": "San Martín de la Vega: 104,6 km² de término y el taller BMW a 45,3 km",
    "entradilla": "Con 104,6 km² de término y 201 habitantes por kilómetro cuadrado, en San Martín de la Vega las distancias se hacen en coche. El taller especialista de la red queda a 45,3 km, en Alcobendas; esto es lo que te pilla más cerca y cómo plantear el viaje.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 45.3},
    "secciones": [
        {"id": "valdemoro-y-getafe", "h2": "Valdemoro para la ITV, Getafe para lo oficial",
         "parrafos": [
             "La estación de ITV oficial más próxima por carretera es la de ITV Valdemoro (estación 2863), en la calle Vereda de la Solana 43-45 del polígono Las Canteras, en Valdemoro: 11,5 km. El servicio oficial BMW más cercano según bmw.es es Vehinter, en la carretera de Madrid a Toledo, en Getafe, a 22,4 km.",
         ]},
        {"id": "m301-a4-a1", "h2": "Hasta Alcobendas por la M-301, la A-4, la M-30 y la A-1",
         "parrafos": [
             "La ruta sale por la M-301 hacia la A-4, cruza Madrid por la M-30 y sale por la A-1: 45,3 km por carretera, 38 en línea recta. Es un trayecto que se plantea para un trabajo concreto, no para una revisión de rutina.",
             "Como el desplazamiento cuesta, el método importa: el presupuesto se entrega por escrito y no se hace nada que no hayas aprobado antes, de modo que sabes a qué vas. Si la reparación va a durar más de un día, pregunta al reservar por el vehículo de cortesía; depende de la disponibilidad.",
         ]},
        {"id": "parque-san-martin", "h2": "577 turismos por cada mil habitantes",
         "parrafos": [
             "San Martín de la Vega tenía 21.010 vecinos en el padrón de 2025, un 11,5 % más que en 2015 (18.835), y 12.125 turismos censados en 2025 según la Comunidad de Madrid a partir de la DGT: 577 por cada 1.000 habitantes, cuando en Madrid capital son 388.",
             "Las carreteras que rodean el núcleo —M-307, M-506 y M-301, todas a poco más de un kilómetro— son autonómicas, con rotondas y travesías. Ese uso castiga frenos, silentblocks y amortiguadores; si notas golpes secos en los baches o el coche se va hacia un lado al frenar, conviene revisarlo antes de que el desgaste llegue a neumáticos y rótulas.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde San Martín de la Vega?",
         "a": "La estación oficial más próxima por carretera está en Valdemoro: la 2863, en el polígono Las Canteras, a 11,5 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Vehinter, en la carretera de Madrid a Toledo (Getafe), a 22,4 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "45,3 km por carretera hasta la calle Valgrande de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "21.010 habitantes (+11,5 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "104,6 km²", **F.cartociudad},
        {"etiqueta": "Turismos (2025)", "valor": "12.125 · 577 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "Valdemoro (estación 2863) · 11,5 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 22,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 45,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

CIUDADES["les-franqueses-del-valles"] = {
    "h1": "Les Franqueses del Vallès: lo cercano, en Granollers; el especialista BMW, por la C-17",
    "entradilla": "Desde les Franqueses, Granollers queda a 1,7 km en línea recta y concentra lo que el coche necesita a diario: servicio oficial BMW e ITV. Nuestro taller está más lejos, a 44,6 km en Sant Joan Despí, y sirve para otra cosa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 44.6},
    "secciones": [
        {"id": "granollers-al-lado", "h2": "Pruna Motor y la ITV del Congost",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo es Pruna Motor, en la carretera C-17, km 19,060, en Granollers, a 8,1 km por carretera. La estación de ITV que el registro de la Generalitat da como más próxima por carretera es la de Granollers (B18), de Applus, en la avinguda de Sant Julià, polígono El Congost: 6,3 km.",
         ]},
        {"id": "c17-c33", "h2": "44,6 km por la C-17, la C-33 y las rondas",
         "parrafos": [
             "El recorrido hasta Dasercars Barcelona baja por la C-17 y la C-33, enlaza con la B-20 y termina por la B-23: 44,6 km por carretera, 34,5 en línea recta. Les Franqueses queda fuera del Área Metropolitana de Barcelona, así que la recogida del taller no llega.",
             "Para que el viaje rinda, llama antes y cuenta qué le pasa al coche, con el modelo y el año delante. Así se valora si el problema encaja con lo que hacemos —diésel N47, N57 o B47, electrónica, homologaciones de escape y gases con REDISTA— y si conviene tener alguna pieza pedida.",
         ]},
        {"id": "c352-por-el-centro", "h2": "La C-352 por el centro, la C-17 a 2,1 km",
         "parrafos": [
             "La C-352 pasa a 0,1 km del centro y la C-17 a 2,1. El término mide 29,14 km² y el núcleo está a 181 metros de altitud.",
             "Un diésel que alterna salidas a la C-17 con trayectos cortos suele llevar bien el filtro de partículas; el que solo hace lo segundo, no tanto. Si se enciende el testigo del filtro, no lo ignores: una regeneración a tiempo es mucho más sencilla que un filtro colmatado.",
         ]},
        {"id": "franqueses-en-cifras", "h2": "20.881 vecinos y 10.992 turismos",
         "parrafos": [
             "El padrón de 2025 da 20.881 habitantes, un 7,4 % más que diez años antes (19.446). En 2024 había 10.992 turismos según Idescat a partir de la DGT: 526 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a les Franqueses?",
         "a": "Pruna Motor, en la C-17, km 19,060, en Granollers, a 8,1 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de Granollers (B18), en el polígono El Congost, a 6,3 km por carretera."},
        {"q": "¿Recogéis el coche en les Franqueses del Vallès?",
         "a": "No: la recogida cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "20.881 habitantes (+7,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080863")},
        {"etiqueta": "Turismos (2024)", "valor": "10.992 · 526 por cada 1.000 hab.", **F.idescat("080863")},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 6,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 8,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 44,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080863"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["villalbilla"] = {
    "h1": "Villalbilla, un 51,3 % más grande que en 2015: tu BMW entre Alcalá y Alcobendas",
    "entradilla": "Villalbilla ha pasado de 12.351 a 18.687 habitantes entre 2015 y 2025. Para quien tiene un BMW o un MINI aquí, lo útil a diario está en Alcalá de Henares, a menos de ocho kilómetros, y el taller especialista de la red, en Alcobendas, a 35,7 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 35.7},
    "secciones": [
        {"id": "itv-la-garena", "h2": "La ITV, a 3,9 km en La Garena",
         "parrafos": [
             "La estación oficial más próxima por carretera es la de TÜV SÜD ATISAE (estación 2878), en la avenida Juan Carlos I, junto al centro comercial La Garena de Alcalá de Henares: 3,9 km según el listado de la Comunidad de Madrid.",
             "A esa distancia, lo cómodo es hacer una pre-ITV en el taller cuando el coche vaya por otra cosa y pasar la inspección esa misma semana.",
         ]},
        {"id": "autopremier-complutense", "h2": "Servicio oficial en la Vía Complutense",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 7,7 km por carretera. Si tu coche está en garantía y la avería la cubre BMW, ese es tu sitio.",
         ]},
        {"id": "m300-r2", "h2": "35,7 km por la M-300, la M-100 y la R-2",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas sale por la M-300, sigue por la M-100, toma la R-2 y entra por la M-50: 35,7 km por carretera, 27,2 en línea recta. Si el trabajo va a durar más de un día, pregunta al reservar por el vehículo de cortesía, que está sujeto a disponibilidad.",
             "La M-300, a 2,6 km, es la única carretera con número a menos de tres kilómetros del centro, así que los primeros kilómetros de cada salida suelen ser urbanos. Un motor frío al que se le exige pronto sufre más que uno que ya ha cogido temperatura: deja que el aceite se caliente antes de pisar a fondo, sobre todo en invierno, a 687 metros de altitud.",
         ]},
        {"id": "villalbilla-crece", "h2": "596 turismos por cada mil vecinos",
         "parrafos": [
             "El padrón da 18.687 habitantes en 2025, un 51,3 % más que en 2015, en un término de 34,3 km². La Comunidad de Madrid, con datos de la DGT, contaba 11.136 turismos en 2025: 596 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Villalbilla?",
         "a": "La estación oficial más próxima por carretera es la de TÜV SÜD ATISAE (2878), en La Garena de Alcalá de Henares, a 3,9 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 7,7 km."},
        {"q": "¿Dónde está vuestro taller?",
         "a": "En Alcobendas, en la calle Valgrande 17, a 35,7 km por carretera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "18.687 habitantes (+51,3 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "11.136 · 596 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "687 m", **F.copernicus},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE (2878), Alcalá de Henares · 3,9 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 7,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 35,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# metaDescription nuevas (solo ciudades sin impresiones en GSC cuya descripción prometía
# «hasta un 50 %», diagnosis «oficial» o ISTA). Se aplican aparte; no van al bloque `local`.
META_DESCRIPTIONS = {
    "barbera-del-valles": "Especialista independiente BMW y MINI para Barberà del Vallès: taller en Sant Joan Despí a 28,1 km y recogida en el área metropolitana, sujeta a disponibilidad.",
    "sant-pere-de-ribes": "BMW en Sant Pere de Ribes: servicio oficial e ITV en Vilanova i la Geltrú y taller especialista independiente a 34 km por la C-32. Cuándo compensa el viaje.",
    "villaviciosa-de-odon": "Taller especialista BMW para Villaviciosa de Odón en Alcobendas, a 40,9 km por la M-40. Concesionario e ITV cercanos y mantenimiento sin perder la garantía.",
    "premia-de-mar": "BMW en Premià de Mar: qué le hace el salitre a un coche aparcado junto al mar, dónde está el servicio oficial y la ruta al taller especialista de Sant Joan Despí.",
    "martorell": "Martorell: taller especialista BMW a 19,8 km en Sant Joan Despí, servicio oficial a 18,4 km en Sant Cugat e ITV a 3,1 km en Sant Andreu de la Barca.",
    "sant-vicenc-dels-horts": "Desde Sant Vicenç dels Horts, el taller especialista BMW está a 8,2 km por la A-2, más cerca que el concesionario. Recogida en el AMB sujeta a disponibilidad.",
    "molins-de-rei": "Molins de Rei: 9,6 km por la B-23 hasta el taller especialista BMW y MINI de Sant Joan Despí. Servicio oficial, ITV y recogida en el área metropolitana.",
    "castellar-del-valles": "Castellar del Vallès tiene taller autorizado BMW en el pueblo. Cuándo compensa llevar el coche a un especialista independiente, a 47 km en Sant Joan Despí.",
    "mejorada-del-campo": "Mejorada del Campo: ITV en el propio polígono, servicio oficial BMW en Alcalá y taller especialista independiente en Alcobendas, a 33,4 km por la R-3.",
    "el-masnou": "BMW en El Masnou: servicio oficial en Sant Adrià, ITV en Badalona y taller especialista independiente a 31,9 km. Revisiones fuera del concesionario y garantía.",
    "vilassar-de-mar": "Vilassar de Mar: servicio oficial BMW e ITV a unos 5 km y taller especialista a 42,1 km. Qué averías justifican el viaje y cuáles se resuelven cerca.",
    "san-martin-de-la-vega": "San Martín de la Vega: ITV en Valdemoro, servicio oficial BMW en Getafe y taller especialista independiente en Alcobendas, a 45,3 km. Presupuesto por escrito.",
    "les-franqueses-del-valles": "les Franqueses del Vallès: servicio oficial BMW e ITV en Granollers y taller especialista independiente a 44,6 km por la C-17. Diésel, electrónica y REDISTA.",
    "villalbilla": "Villalbilla: ITV a 3,9 km en La Garena, servicio oficial BMW en Alcalá de Henares y taller especialista independiente en Alcobendas, a 35,7 km.",
}
