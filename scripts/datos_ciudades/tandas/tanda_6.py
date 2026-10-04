# Tanda 6: Súria, Torrelles de Llobregat, Ugena, Sant Pol de Mar, l'Arboç, Vilanova del Vallès,
# Valdetorres de Jarama, Gironella, Torrejón de Velasco, Collbató, Serranillos del Valle, Cardona,
# el Papiol, el Pont de Vilomara i Rocafort.
# Borja se salta (zona de Zaragoza sin dirección de taller; pendiente de decisión de Martin).
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py.
# META: metaDescription nueva para ciudades sin impresiones cuya descripción actual
# contenía promesas («hasta un 50 %», ISTA, «oficial», garantía por escrito, recogida).
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
NATURAL_EARTH = {"fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"}

META = {
    "suria": "BMW y MINI en Súria: servicio oficial e ITV en Sant Fruitós de Bages, a 20 km, y el taller especialista de la red en Sant Joan Despí, a 78,6 km.",
    "torrelles-de-llobregat": "Taller especialista BMW a 12,5 km de Torrelles de Llobregat, en Sant Joan Despí. Recogida en el área metropolitana sujeta a disponibilidad.",
    "ugena": "BMW en Ugena (Toledo): servicio oficial en Leganés, a 26,4 km, y el taller especialista de la red en Alcobendas, a 62,2 km por la A-42.",
    "sant-pol-de-mar": "BMW en Sant Pol de Mar: qué hace el salitre al coche, servicio oficial en Mataró, ITV en Argentona y taller especialista a 62,6 km por la C-32.",
    "l-arboc": "BMW en l'Arboç: ITV del Baix Penedès a 10 km, servicio oficial en Vilanova i la Geltrú y taller especialista de la red a 60,2 km por la AP-7.",
    "vilanova-del-valles": "BMW en Vilanova del Vallès: ITV y servicio oficial en Granollers y taller especialista de la red en Sant Joan Despí, a 41,1 km por la AP-7.",
    "valdetorres-de-jarama": "BMW en Valdetorres de Jarama: ITV y servicio oficial en Algete y taller especialista de la red en Alcobendas, a 27,3 km por la A-1.",
    "gironella": "BMW en Gironella: ITV en Berga a 14,2 km, servicio oficial en Sant Fruitós de Bages y taller especialista a 94,3 km. Cuándo compensa el viaje.",
    "torrejon-de-velasco": "BMW en Torrejón de Velasco: ITV en Parla, servicio oficial en Getafe y taller especialista de la red en Alcobendas, a 48,7 km.",
    "serranillos-del-valle": "BMW en Serranillos del Valle: ITV en Arroyomolinos, servicio oficial en Leganés y taller especialista de la red en Alcobendas, a 53,4 km.",
    "cardona": "BMW en Cardona: ITV en Solsona, servicio oficial en Sant Fruitós de Bages y taller especialista de la red en Sant Joan Despí, a 92,5 km.",
    "el-papiol": "Taller especialista BMW a 12,9 km del Papiol por la B-23, en Sant Joan Despí. Recogida en el área metropolitana sujeta a disponibilidad.",
    "el-pont-de-vilomara-i-rocafort": "BMW en el Pont de Vilomara i Rocafort: ITV en Manresa a 9,1 km, servicio oficial en Sant Fruitós y taller especialista a 63,3 km.",
}

CIUDADES["suria"] = {
    "h1": "Súria y su BMW: Sant Fruitós para lo cercano, Sant Joan Despí para lo específico",
    "entradilla": "Desde Súria, el concesionario y la ITV caen en el mismo municipio, Sant Fruitós de Bages, a unos 20 km. El taller especialista de la red está bastante más lejos, a 78,6 km. Así se reparte el trabajo con sentido.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 78.6},
    "secciones": [
        {"id": "sant-fruitos-a-20-km", "h2": "Concesionario e ITV, los dos en Sant Fruitós de Bages",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo a Súria es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, a 20 km por carretera. Prácticamente a la misma distancia, 20,1 km, está la estación ITV Sant Fruitós (B25), que gestiona Itevelesa en el polígono El Grau, según el registro de la Generalitat.",
         ]},
        {"id": "c55-hacia-el-sur", "h2": "78,6 km hasta el taller: C-55, C-16 y AP-7",
         "parrafos": [
             "La nave de Dasercars Barcelona está en el carrer del Tambor del Bruc 3 de Sant Joan Despí. Desde Súria se sale por la C-55, que pasa a 2,1 km del centro, se enlaza con la C-16 y la B-30 y se termina por la AP-7 y la B-23: 78,6 km por carretera, 57,7 en línea recta.",
             "Súria no forma parte del área metropolitana de Barcelona, así que no entra en la recogida de coches del taller.",
         ]},
        {"id": "que-vale-el-viaje", "h2": "Qué justifica bajar y qué no",
         "parrafos": [
             "Un cambio de aceite o unas pastillas los resuelve cualquier taller del Bages. Bajar a Sant Joan Despí tiene sentido para lo que pide conocer la marca a fondo: un diésel N47 o B47 con ruido de distribución, un problema de emisiones o del escape (el taller tiene homologación REDISTA) o un fallo electrónico que vuelve tras cada borrado.",
         ]},
        {"id": "suria-en-cifras", "h2": "6.200 vecinos y algo más de un coche por cada dos",
         "parrafos": [
             "El padrón de 2025 da a Súria 6.200 habitantes, un 4,6 % más que los 5.927 de 2015, en un término de 23,6 km² a 326 metros de altitud. Idescat, con datos de la DGT, contaba 3.303 turismos en 2024: 533 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano a Súria?",
         "a": "Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 20 km según bmw.es."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La más próxima por carretera en el registro de la Generalitat es Sant Fruitós (B25), en el polígono El Grau, a 20,1 km."},
        {"q": "¿Recogéis el coche en Súria?",
         "a": "No. La recogida del taller cubre solo el área metropolitana de Barcelona y Súria queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "6.200 habitantes (+4,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("082747")},
        {"etiqueta": "Turismos (2024)", "valor": "3.303 · 533 por cada 1.000 hab.", **F.idescat("082747")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Fruitós (B25) · 20,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 20 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 78,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082747"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["torrelles-de-llobregat"] = {
    "h1": "Torrelles de Llobregat: taller BMW a 12,5 km y recogida en el área metropolitana",
    "entradilla": "Por la BV-2005 y la A-2, el taller especialista de la red queda a 12,5 km de Torrelles, más cerca que el concesionario. Y como el municipio pertenece al Área Metropolitana de Barcelona, puedes pedir que pasen a por el coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 12.5},
    "secciones": [
        {"id": "mas-cerca-que-el-concesionario", "h2": "El especialista, más cerca que el concesionario",
         "parrafos": [
             "Desde el centro de Torrelles hasta la nave de Dasercars Barcelona, en el carrer del Tambor del Bruc de Sant Joan Despí, hay 12,5 km por carretera y 7 en línea recta. Se baja por la BV-2005, que pasa a menos de un kilómetro del centro, y se sigue por la A-2.",
             "El servicio oficial BMW más próximo según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 14,6 km. Para reparaciones en garantía de BMW es la dirección; para el mantenimiento puedes elegir taller, porque el Reglamento (UE) 461/2010 impide que se pierda la garantía por revisar fuera de la red si se cumple el plan del fabricante.",
         ]},
        {"id": "recogida-amb", "h2": "Dentro del AMB: recogida y vehículo de cortesía",
         "parrafos": [
             "Torrelles de Llobregat es uno de los municipios del Área Metropolitana de Barcelona, y el taller ofrece recogida y entrega del coche y vehículo de cortesía dentro del área metropolitana. Las dos cosas dependen de disponibilidad, así que lo correcto es pedirlas al reservar y no el mismo día.",
         ]},
        {"id": "itv-sant-just", "h2": "Para la ITV, Sant Just Desvern",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sant Just Desvern (B05), de Applus, en la avinguda de la Riera del polígono industrial número 1, a 13,8 km. Como queda hacia el mismo lado que el taller, la pre-ITV y la inspección pueden hacerse con pocos días de diferencia.",
         ]},
        {"id": "torrelles-en-cifras", "h2": "Un pueblo de 6.170 habitantes con 3.403 turismos",
         "parrafos": [
             "Torrelles tenía 6.170 vecinos en el padrón de 2025, frente a 5.883 en 2015 (un 4,9 % más), en 13,56 km² a 126 metros de altitud. Idescat contaba 3.403 turismos en 2024 a partir de la DGT: 552 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Torrelles de Llobregat?",
         "a": "Sí, dentro del área metropolitana de Barcelona hay recogida y entrega, sujetas a disponibilidad."},
        {"q": "¿Qué está más cerca, vuestro taller o el concesionario?",
         "a": "El taller: 12,5 km hasta Sant Joan Despí, frente a 14,6 km hasta Barcelona Premium en Sant Boi."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es Sant Just Desvern (B05), a 13,8 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "6.170 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082896")},
        {"etiqueta": "Turismos (2024)", "valor": "3.403 · 552 por cada 1.000 hab.", **F.idescat("082896")},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 12,5 km", **F.osrm},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 13,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Boi · 14,6 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082896"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["ugena"] = {
    "h1": "Ugena (Toledo): el taller BMW de la red, a 62 km en Alcobendas",
    "entradilla": "Aunque Ugena es provincia de Toledo, lo que tiene que ver con BMW le queda en Madrid: el servicio oficial, en Leganés, y el taller especialista de la red, en Alcobendas. Te contamos distancias y rutas sin adornos.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 62.2},
    "secciones": [
        {"id": "toledo-mirando-a-madrid", "h2": "Un municipio toledano que mira a Madrid",
         "parrafos": [
             "Ugena tenía 5.988 habitantes en 2025 frente a los 5.282 de 2015: un 13,4 % más en diez años, en un término de 15,4 km² a 656 metros de altitud.",
             "Para el dueño de un BMW o un MINI, la consecuencia es sencilla: los servicios de marca más cercanos están al otro lado del límite autonómico, y la distancia se cuenta en decenas de kilómetros. Merece la pena saber de antemano qué se resuelve en cada sitio.",
         ]},
        {"id": "oficial-leganes", "h2": "El servicio oficial, a 26,4 km en Leganés",
         "parrafos": [
             "En el localizador de bmw.es, el punto oficial más próximo es Vehinter (Momentum Leganés), en la esquina de las calles Palier y Bastidor de un polígono de Leganés, a 26,4 km por carretera. Si el coche está en garantía y lo que toca es una reparación cubierta por BMW, ese es el sitio lógico.",
         ]},
        {"id": "ruta-a42", "h2": "62,2 km por la CM-4008, la A-42 y la M-40",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 de Alcobendas sale por la CM-4008, toma la A-42 hacia Madrid y rodea la ciudad por la M-40 y la M-30 hasta la A-1: 62,2 km por carretera, 46,8 en línea recta. Ugena queda fuera del área metropolitana de Madrid, de modo que la recogida del taller no llega aquí.",
             "Con esa distancia, hazte una idea antes de mover el coche: cuenta el síntoma por teléfono junto con el modelo, el año y los kilómetros, y decide con esa primera orientación si el viaje compensa.",
         ]},
        {"id": "itv-ugena", "h2": "Sobre la ITV",
         "parrafos": [
             "No te indicamos una estación concreta: la que aparece cerca de Ugena en la cartografía abierta no figura en un registro oficial que hayamos podido comprobar. Para pedir cita, consulta el listado de estaciones de la Junta de Comunidades de Castilla-La Mancha.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Ugena o en la provincia de Toledo?",
         "a": "No. El taller de la red que atiende Ugena es Dasercars Madrid, en Alcobendas, a 62,2 km."},
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "Vehinter (Momentum Leganés), a 26,4 km, según el localizador de bmw.es."},
        {"q": "¿Recogéis el coche en Ugena?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Madrid."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "5.988 habitantes (+13,4 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "15,4 km²", **F.cartociudad},
        {"etiqueta": "Altitud del centro urbano", "valor": "656 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Leganés) · 26,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 62,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

CIUDADES["sant-pol-de-mar"] = {
    "h1": "Sant Pol de Mar: un BMW a 1,7 km del mar y a 62,6 del taller",
    "entradilla": "Con la playa a menos de dos kilómetros del centro y la C-32 al lado, en Sant Pol el coche convive con el salitre. Lo que conviene vigilar, dónde está lo oficial en el Maresme y qué supone ir al taller de Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 62.6},
    "secciones": [
        {"id": "aire-del-maresme", "h2": "Lo que el aire del Maresme le hace al coche",
         "parrafos": [
             "El centro de Sant Pol queda a unos 1,7 km de la costa. La humedad salina trabaja despacio y por debajo: soportes del escape, anclajes de los trenes y tornillería de los bajos son los primeros en mostrar óxido. Y los discos de un coche que pasa una semana parado amanecen con una capa marrón que, repetida, acaba picando la superficie.",
             "En los BMW, además, hay bastante electrónica con conectores en los pasos de rueda y bajo el coche. Si aparece un aviso intermitente de un sensor de ABS o de aparcamiento, antes de cambiar la pieza hay que limpiar y revisar el conector.",
         ]},
        {"id": "mataro-y-argentona", "h2": "Servicio oficial en Mataró, ITV en Argentona",
         "parrafos": [
             "El punto oficial BMW más próximo según bmw.es es Pruna Motor, en la Via Sergia 2 de Mataró, a 22,8 km por carretera. Para la ITV, la estación más cercana por carretera en el registro de la Generalitat es Argentona (B08), de Applus, en el polígono El Cros, a 22,4 km.",
         ]},
        {"id": "c32-al-taller", "h2": "Por la C-32, la B-20 y la B-23",
         "parrafos": [
             "La C-32 pasa a unos cientos de metros del centro y la N-II a menos de un kilómetro. Hasta la nave de Dasercars Barcelona, en Sant Joan Despí, la ruta es C-32, B-20 y B-23: 62,6 km por carretera, 54,1 en línea recta.",
             "Sant Pol no está en el área metropolitana de Barcelona, así que el coche lo traes tú: la recogida del taller no llega hasta aquí.",
         ]},
        {"id": "sant-pol-crece", "h2": "5.793 vecinos en 7,53 km²",
         "parrafos": [
             "El padrón pasó de 5.012 habitantes en 2015 a 5.793 en 2025, un 15,6 % más, en un término pequeño de 7,53 km². Idescat registraba 2.597 turismos en 2024 a partir de la DGT: 448 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Le afecta al coche vivir tan cerca del mar?",
         "a": "Acelera el óxido de bajos y escape, marca los discos de un coche parado y puede dar fallos de conectores. Lavar los bajos con agua dulce de vez en cuando ayuda."},
        {"q": "¿Dónde paso la ITV desde Sant Pol?",
         "a": "La más próxima por carretera en el registro de la Generalitat es Argentona (B08), a 22,4 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "62,6 km por la C-32, la B-20 y la B-23 hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "5.793 habitantes (+15,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082359")},
        {"etiqueta": "Turismos (2024)", "valor": "2.597 · 448 por cada 1.000 hab.", **F.idescat("082359")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 1,7 km desde el centro", **NATURAL_EARTH},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 22,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 22,8 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082359"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["l-arboc"] = {
    "h1": "L'Arboç: tu BMW junto a la AP-7, a 60 km del taller de la red",
    "entradilla": "Es provincia de Tarragona, pero el taller de la red que atiende l'Arboç está en la de Barcelona, en Sant Joan Despí. Con la N-340 y la AP-7 a menos de dos kilómetros, la ruta es directa; lo que tienes cerca está en Bellvei y en Vilanova i la Geltrú.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 60.2},
    "secciones": [
        {"id": "ap7-a-la-puerta", "h2": "Tres carreteras a menos de dos kilómetros",
         "parrafos": [
             "La N-340 y la TP-2124 pasan a menos de un kilómetro del centro, y la AP-7 a 1,7 km. Hasta la nave de Dasercars Barcelona, la ruta es N-340, AP-7 y B-23: 60,2 km por carretera, 39 en línea recta. L'Arboç no está en el área metropolitana de Barcelona, así que la recogida del taller no llega aquí.",
             "Un diésel que hace a menudo tramos de autopista a velocidad constante regenera el filtro de partículas sin que te enteres. El problema llega cuando el uso cambia a trayectos cortos por el pueblo: si el testigo del filtro se enciende, no lo dejes para el día que toque bajar.",
         ]},
        {"id": "itv-bellvei", "h2": "La ITV, a 10 km en Bellvei",
         "parrafos": [
             "La estación ITV del Baix Penedès (T07), que gestiona Itevelesa en el polígono Els Massets de Bellvei, es la más próxima por carretera según el registro de la Generalitat: 10 km. Es otra razón para resolver la inspección en la comarca y reservar el viaje a Sant Joan Despí para lo que lo merece.",
         ]},
        {"id": "vilanova-oficial", "h2": "El concesionario más cercano, en Vilanova i la Geltrú",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 19,6 km por carretera. Nosotros somos un taller independiente: no tramitamos garantías del fabricante, pero sí el mantenimiento y las reparaciones que no dependen de BMW.",
         ]},
        {"id": "arboc-en-cifras", "h2": "5.721 vecinos y 3.041 turismos",
         "parrafos": [
             "L'Arboç tenía 5.721 habitantes en 2025 y 5.513 en 2015, según el padrón. En 2024, Idescat contaba 3.041 turismos a partir de la DGT, 532 por cada 1.000 habitantes, en un término de 14,13 km².",
         ]},
    ],
    "faq": [
        {"q": "¿Por qué os atiende un taller de Barcelona si l'Arboç es de Tarragona?",
         "a": "Porque el taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 60,2 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación del Baix Penedès (T07), en Bellvei, a 10 km."},
        {"q": "¿Recogéis el coche en l'Arboç?",
         "a": "No. La recogida cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "5.721 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Penedès", **F.idescat("430167")},
        {"etiqueta": "Turismos (2024)", "valor": "3.041 · 532 por cada 1.000 hab.", **F.idescat("430167")},
        {"etiqueta": "ITV más cercana", "valor": "Baix Penedès (T07), Bellvei · 10 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 19,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 60,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("430167"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["vilanova-del-valles"] = {
    "h1": "Vilanova del Vallès: ITV y concesionario en Granollers, especialista BMW a 41 km",
    "entradilla": "Desde Vilanova del Vallès, Granollers lo concentra casi todo: la ITV a 5,8 km y el servicio oficial BMW a 11,1. El taller especialista de la red está en Sant Joan Despí, a 41,1 km por la AP-7.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 41.1},
    "secciones": [
        {"id": "granollers", "h2": "Lo que tienes en Granollers",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la ITV Granollers (B18), de Applus, en la avinguda de Sant Julià del polígono El Congost, a 5,8 km. El punto oficial BMW más cercano según bmw.es es Pruna Motor, en la carretera C-17, km 19,060, también en Granollers, a 11,1 km.",
             "Con las dos cosas tan a mano, la inspección y lo que dependa de la marca se resuelven sin salir del Vallès Oriental.",
         ]},
        {"id": "ap7-c33", "h2": "41,1 km por la AP-7 y la C-33",
         "parrafos": [
             "La AP-7 pasa a 2,1 km del centro y la C-35 a 2,5. Hacia Sant Joan Despí se toma la AP-7, se enlaza con la C-33 y la B-20 y se sale por la B-23: 41,1 km por carretera, 29,6 en línea recta.",
             "Vilanova del Vallès no forma parte del área metropolitana de Barcelona, así que la recogida del taller no la cubre. Si vas a bajar, ten a mano el número de bastidor: con él se identifica la referencia exacta de cada pieza y se puede tener todo pedido antes de que llegue el coche.",
         ]},
        {"id": "cuando-compensa", "h2": "Cuándo merece la pena hacer los 41 km",
         "parrafos": [
             "Para un BMW con una avería que se repite, una distribución ruidosa en un diésel de las familias N47 o N57, un testigo de emisiones que vuelve o un fallo eléctrico que nadie localiza. Para el mantenimiento del día a día, la cercanía de Granollers pesa más.",
         ]},
        {"id": "vilanova-en-cifras", "h2": "Un 8,6 % más de vecinos en diez años",
         "parrafos": [
             "El padrón pasó de 5.241 habitantes en 2015 a 5.693 en 2025, en un término de 15,2 km². Idescat, a partir de la DGT, contaba 3.076 turismos en 2024: 540 por cada 1.000 vecinos, casi el doble que los 281 de Barcelona ciudad.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Vilanova del Vallès?",
         "a": "La más próxima por carretera es Granollers (B18), en el polígono El Congost, a 5,8 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la C-17 a la altura de Granollers, a 11,1 km según bmw.es."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No: la recogida del taller se limita al área metropolitana de Barcelona, y Vilanova del Vallès queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "5.693 habitantes (+8,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("089024")},
        {"etiqueta": "Turismos (2024)", "valor": "3.076 · 540 por cada 1.000 hab.", **F.idescat("089024")},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 5,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 11,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 41,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("089024"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["valdetorres-de-jarama"] = {
    "h1": "Valdetorres de Jarama: un 22 % más de vecinos y el taller BMW a 27 km",
    "entradilla": "Valdetorres ha pasado de 4.234 a 5.175 habitantes en diez años. Para quien tiene aquí un BMW o un MINI, lo útil está en Algete —ITV y servicio oficial— y en Alcobendas, donde está el taller especialista de la red.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 27.3},
    "secciones": [
        {"id": "algete", "h2": "Algete: la ITV a 10,6 km y el servicio oficial a 14,6",
         "parrafos": [
             "La estación oficial más cercana por carretera, según el listado de la Comunidad de Madrid, es la de ITV Barbastro (estación 2818), en la avenida Nicasio Martín 4 del polígono industrial Sector 8 de Algete, a 10,6 km. En el mismo municipio está el punto oficial BMW más próximo según bmw.es, BYmyCAR Madrid, en la calle Tejera 2, junto a la carretera de Algete, a 14,6 km.",
             "Si toca una reparación cubierta por la garantía de BMW, es ahí. El mantenimiento periódico, en cambio, no tiene por qué: el Reglamento (UE) 461/2010 permite hacerlo en un taller independiente sin que el fabricante pueda negar la garantía, siempre que se respete el plan.",
         ]},
        {"id": "m103-a1", "h2": "Por la M-103, la M-111 y la M-100 hasta la A-1",
         "parrafos": [
             "La ruta desde el centro de Valdetorres hasta la calle Valgrande de Alcobendas encadena la M-103, la M-111 y la M-100 antes de entrar en la A-1: 27,3 km por carretera, 19,5 en línea recta.",
             "Para trabajos de varios días, pregunta al reservar por el vehículo de cortesía y por la recogida: los dos están sujetos a disponibilidad y solo dentro del área metropolitana de Madrid, así que confirma si tu dirección entra.",
         ]},
        {"id": "parque-valdetorres", "h2": "584 turismos por cada mil habitantes",
         "parrafos": [
             "La Comunidad de Madrid, con datos de la DGT, contaba 3.020 turismos en Valdetorres en 2025: 584 por cada 1.000 vecinos, muy por encima de los 388 de Madrid capital. El término mide 34,9 km² y el casco está a 643 metros de altitud.",
             "Cuando en casa hay más de un coche, el que menos se mueve es el que antes avisa: batería descargada, discos con óxido y neumáticos que pierden presión. Moverlo un rato cada semana evita la mayoría de esos sustos.",
         ]},
    ],
    "faq": [
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 27,3 km por carretera, en la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Dónde paso la ITV desde Valdetorres de Jarama?",
         "a": "La estación oficial más cercana es la de ITV Barbastro en Algete (estación 2818), a 10,6 km."},
        {"q": "¿Pierdo la garantía si no voy al concesionario?",
         "a": "No, si las revisiones siguen el plan de mantenimiento de BMW con las especificaciones correctas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "5.175 habitantes (+22,2 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "3.020 · 584 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITV Barbastro, Algete · 10,6 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid, Algete · 14,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 27,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

CIUDADES["gironella"] = {
    "h1": "Gironella, en el Berguedà: ITV en Berga y taller BMW a 94 km",
    "entradilla": "Desde Gironella, el taller de la red queda a 94,3 km, en Sant Joan Despí. No vamos a fingir que está cerca: lo razonable es resolver en la zona casi todo y bajar solo cuando de verdad haga falta un especialista en BMW.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 94.3},
    "secciones": [
        {"id": "berga-y-sant-fruitos", "h2": "Berga para la ITV, Sant Fruitós para lo oficial",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la ITV Berga (B13), de TÜV Rheinland, en el camí de Sant Bartomeu del polígono La Valldan, a 14,2 km. El servicio oficial BMW más cercano según bmw.es queda hacia el sur: Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 32,3 km.",
         ]},
        {"id": "c16-hacia-el-sur", "h2": "La C-16 a la puerta, 94 km hasta el taller",
         "parrafos": [
             "La C-16 pasa a menos de un kilómetro del centro, y la C-154 y la C-62 a 2,8. La ruta hasta la nave de Dasercars Barcelona es casi toda esa C-16, seguida de la B-30, la AP-7 y la B-23: 94,3 km por carretera, 74,3 en línea recta.",
             "La recogida del taller solo cubre el área metropolitana, así que el viaje es tuyo. Antes de hacerlo, pide presupuesto: se entrega por escrito y no se toca nada sin que lo apruebes; la diagnosis también se presupuesta, de modo que sabes a qué vas.",
         ]},
        {"id": "cuando-bajar", "h2": "Qué justifica casi doscientos kilómetros entre ida y vuelta",
         "parrafos": [
             "Una avería que ya han mirado sin éxito, un ruido de cadena en un diésel N47 o N57, un fallo del sistema de AdBlue con la cuenta atrás en marcha, o una reparación cara que quieres contrastar antes de aceptarla. Para aceite, frenos o neumáticos, un taller del Berguedà te ahorra el viaje.",
         ]},
        {"id": "gironella-en-cifras", "h2": "5.083 vecinos en 6,78 km²",
         "parrafos": [
             "El término de Gironella mide 6,78 km² y el padrón de 2025 le da 5.083 habitantes, unos 750 por kilómetro cuadrado; en 2015 eran 4.925. Idescat contaba 2.854 turismos en 2024 a partir de la DGT: 561 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en el Berguedà?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 94,3 km."},
        {"q": "¿Dónde paso la ITV desde Gironella?",
         "a": "La más próxima por carretera es Berga (B13), en el polígono La Valldan, a 14,2 km."},
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 32,3 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "5.083 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080924")},
        {"etiqueta": "Turismos (2024)", "valor": "2.854 · 561 por cada 1.000 hab.", **F.idescat("080924")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 14,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 32,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 94,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080924"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["torrejon-de-velasco"] = {
    "h1": "Torrejón de Velasco: ITV en Parla, servicio oficial en Getafe y taller BMW a 48,7 km",
    "entradilla": "No confundas Torrejón de Velasco con Torrejón de Ardoz: este está al sur, con la R-4 a 2,4 km, y el taller de la red le queda a 48,7 km. Te dejamos lo que hay cerca y lo que implica cruzar Madrid.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 48.7},
    "secciones": [
        {"id": "termino-amplio", "h2": "51,9 km² para 4.900 vecinos",
         "parrafos": [
             "Torrejón de Velasco tiene un término amplio para su población: 51,9 km² y 4.900 habitantes en 2025, unos 94 por kilómetro cuadrado. Ha crecido un 16 % desde los 4.224 de 2015. La Comunidad de Madrid, a partir de la DGT, registraba 2.966 turismos en 2025: 605 por cada 1.000 vecinos.",
         ]},
        {"id": "parla-y-getafe", "h2": "ITV en Parla y servicio oficial en Getafe",
         "parrafos": [
             "La estación oficial más cercana por carretera es la de TÜV Rheinland Ibérica (estación 2841), en la calle Berlín 1 del polígono industrial de Parla, a 10,1 km según el listado de la Comunidad de Madrid. El punto oficial BMW más próximo según bmw.es es Vehinter, en la carretera de Madrid a Toledo, en Getafe, a 17,5 km.",
             "Si BMW te convoca para una campaña de revisión, la cita es en la red oficial; eso no lo hace un taller independiente. Lo demás —mantenimiento, averías, diagnosis— lo eliges tú.",
         ]},
        {"id": "cruzar-madrid", "h2": "48,7 km por la A-4, la M-30 y la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas va por la M-404, que pasa a menos de un kilómetro del centro, y la M-423 hasta la A-4; cruza por la M-30 y sale por la A-1: 48,7 km por carretera, 41,8 en línea recta.",
             "La recogida del taller se limita al área metropolitana de Madrid y está sujeta a disponibilidad: confirma al reservar si tu dirección entra. Si vas a llevarlo tú, apunta antes cuándo aparece el problema —en frío o en caliente, a qué velocidad, con qué testigo— porque ayuda más al diagnóstico que cualquier descripción vaga.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Torrejón de Velasco?",
         "a": "En la estación 2841 de TÜV Rheinland Ibérica, en el polígono industrial de Parla, a 10,1 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "48,7 km por carretera hasta la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, con el mismo equipo que los BMW: comparten electrónica y buena parte de los motores."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.900 habitantes (+16 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "2.966 · 605 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Superficie del término", "valor": "51,9 km²", **F.cartociudad},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV Rheinland, Parla · 10,1 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 17,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 48,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.cartociudad_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

CIUDADES["collbato"] = {
    "h1": "Collbató: un BMW junto a la A-2, a 34,5 km del taller de Sant Joan Despí",
    "entradilla": "Desde Collbató se llega al taller especialista de la red sin cambiar de autovía: toda la ruta es la A-2. Aunque es Baix Llobregat, el municipio no está dentro del área metropolitana, y eso cambia algo importante.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 34.5},
    "secciones": [
        {"id": "fuera-del-amb", "h2": "Baix Llobregat, pero fuera del área metropolitana",
         "parrafos": [
             "Collbató pertenece a la comarca del Baix Llobregat, pero no figura entre los municipios del Área Metropolitana de Barcelona. La consecuencia práctica: la recogida y entrega del coche que ofrece el taller dentro del área metropolitana no llega hasta aquí, y el viaje lo haces tú.",
             "Lo bueno es que es un viaje sencillo. La A-2 pasa a 1,3 km del centro y lleva hasta Sant Joan Despí: 34,5 km por carretera, 29,9 en línea recta. Para un trabajo de un día, lo cómodo es dejar el coche a primera hora y recogerlo por la tarde.",
         ]},
        {"id": "terrassa-y-viladecavalls", "h2": "Lo oficial y la ITV quedan hacia el Vallès",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es no está en el Baix Llobregat sino en Terrassa: Quadis Munich, en la calle Anoia 9, a 25,1 km. La ITV más cercana por carretera en el registro de la Generalitat también queda por ese lado: Viladecavalls (B03), de TÜV Rheinland, en el polígono Can Trias, a 20,7 km.",
             "El concesionario está, por tanto, algo más cerca que nuestro taller, pero no mucho. Si el trabajo es una reparación en garantía de BMW, ve a Terrassa; si es mantenimiento o una avería fuera de garantía, la A-2 te deja en el taller sin desvíos.",
         ]},
        {"id": "collbato-en-cifras", "h2": "Un 10 % más de vecinos desde 2015",
         "parrafos": [
             "Collbató ha pasado de 4.389 habitantes en 2015 a 4.828 en 2025, en un término de 18,07 km² a 388 metros de altitud. Idescat contaba 2.717 turismos en 2024, a partir de la DGT: 563 por cada 1.000 vecinos, el doble que los 281 de Barcelona ciudad.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Collbató?",
         "a": "No. Collbató no forma parte del Área Metropolitana de Barcelona, y la recogida del taller se limita a ella."},
        {"q": "¿Cómo llego al taller?",
         "a": "Por la A-2 todo el trayecto: 34,5 km hasta el carrer del Tambor del Bruc, en Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera en el registro de la Generalitat es Viladecavalls (B03), a 20,7 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.828 habitantes (+10 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080692")},
        {"etiqueta": "Turismos (2024)", "valor": "2.717 · 563 por cada 1.000 hab.", **F.idescat("080692")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecavalls (B03) · 20,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Terrassa · 25,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 34,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080692"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["serranillos-del-valle"] = {
    "h1": "Serranillos del Valle: 731 turismos por cada mil vecinos y el taller BMW a 53 km",
    "entradilla": "En Serranillos hay casi el doble de turismos por habitante que en Madrid capital, y la AP-41 pasa a un paso del centro. Lo que tienes cerca está en Arroyomolinos y Leganés; el taller especialista de la red, en Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 53.4},
    "secciones": [
        {"id": "parque-serranillos", "h2": "Casi el doble de coches por vecino que en Madrid",
         "parrafos": [
             "La Comunidad de Madrid, con datos de la DGT, contaba 3.414 turismos en Serranillos en 2025 para 4.670 habitantes: 731 por cada 1.000, frente a 388 en Madrid capital. La población ha crecido un 16,9 % desde los 3.994 vecinos de 2015, en un término de 13,2 km².",
             "Cuando hay más de un coche en casa, el que se mueve poco es el que da problemas de batería y de discos oxidados. Arrancarlo y hacer con él algún trayecto cada semana evita la mayoría.",
         ]},
        {"id": "arroyomolinos-y-leganes", "h2": "ITV en Arroyomolinos, servicio oficial en Leganés",
         "parrafos": [
             "La estación oficial más cercana por carretera es la de TÜV SÜD ATISAE (estación 2873), en la calle Fresadores 3 del polígono Valdefuentes de Arroyomolinos, a 13,2 km según la Comunidad de Madrid. El punto oficial BMW más próximo según bmw.es es Vehinter (Momentum Leganés), a 22,2 km.",
         ]},
        {"id": "ap41-r5", "h2": "53,4 km por la AP-41, la R-5 y la M-30",
         "parrafos": [
             "Con la AP-41 y la M-404 casi al lado del centro, la salida es inmediata. Hasta la calle Valgrande de Alcobendas se va por la AP-41 y la R-5, se cruza por la M-30 y se termina en la A-1: 53,4 km por carretera, 43,2 en línea recta.",
             "Antes de bajar, pide el presupuesto: llega por escrito y nada se empieza sin tu aprobación; la diagnosis también se presupuesta. La recogida del taller se limita al área metropolitana y depende de disponibilidad, así que pregunta si tu calle entra antes de contar con ella.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Serranillos del Valle?",
         "a": "En la estación 2873 de TÜV SÜD ATISAE, en el polígono Valdefuentes de Arroyomolinos, a 13,2 km."},
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "Vehinter (Momentum Leganés), a 22,2 km según el localizador de bmw.es."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "53,4 km por carretera hasta Alcobendas, por la AP-41, la R-5, la M-30 y la A-1."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.670 habitantes (+16,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "3.414 · 731 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE, Arroyomolinos · 13,2 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Leganés) · 22,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 53,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

CIUDADES["cardona"] = {
    "h1": "Cardona: ITV en Solsona, concesionario en Sant Fruitós y taller BMW a 92,5 km",
    "entradilla": "Para un BMW de Cardona, la ITV más cercana está en Solsona, el servicio oficial en Sant Fruitós de Bages y el taller especialista de la red a 92,5 km, en Sant Joan Despí. Esto es lo que conviene hacer en cada sitio.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 92.5},
    "secciones": [
        {"id": "itv-solsona", "h2": "La ITV, en Solsona",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera a Cardona no está en el Bages sino en Solsona: ITV Solsona (L06), de TÜV Rheinland, en la plaça de les Filadores del polígono Els Ametllers, a 18,6 km. Al pedir cita, búscala por su código; es una estación de la provincia de Lleida.",
         ]},
        {"id": "c55-c16", "h2": "Por la C-55 hasta la C-16",
         "parrafos": [
             "La C-55 pasa a menos de un kilómetro del centro y es el primer tramo de la ruta al taller: C-55, C-16, B-30, AP-7 y B-23, 92,5 km por carretera hasta Sant Joan Despí, 68,5 en línea recta. La recogida del taller no llega hasta aquí, porque solo cubre el área metropolitana.",
             "Con esa distancia, empieza por el teléfono: explica el síntoma, desde cuándo pasa y el modelo con su año y kilometraje. Así se ve si el problema necesita al especialista o se puede resolver en la comarca.",
         ]},
        {"id": "concesionario-sant-fruitos", "h2": "El concesionario, a 33,9 km",
         "parrafos": [
             "El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 33,9 km. Para una reparación cubierta por la garantía de BMW es el destino natural; el taller independiente encaja en lo que va fuera de ella, y sobre todo en las averías concretas de la marca que no se han resuelto cerca.",
         ]},
        {"id": "cardona-en-cifras", "h2": "De 4.898 a 4.553 habitantes en diez años",
         "parrafos": [
             "Según el padrón, Cardona tenía 4.898 habitantes en 2015 y 4.553 en 2025, un 7 % menos. El término es amplio, 66,7 km², y la densidad baja: 68 habitantes por km², a 507 metros de altitud. Idescat registraba 2.583 turismos en 2024 a partir de la DGT, 567 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller cerca de Cardona?",
         "a": "No. El de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 92,5 km."},
        {"q": "¿Dónde paso la ITV desde Cardona?",
         "a": "La más próxima por carretera es Solsona (L06), en el polígono Els Ametllers, a 18,6 km."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 33,9 km según el localizador de bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.553 habitantes (−7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("080478")},
        {"etiqueta": "Turismos (2024)", "valor": "2.583 · 567 por cada 1.000 hab.", **F.idescat("080478")},
        {"etiqueta": "ITV más cercana", "valor": "Solsona (L06) · 18,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 33,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 92,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080478"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["el-papiol"] = {
    "h1": "El Papiol: taller BMW a 12,9 km, entre la B-23 y la AP-7",
    "entradilla": "Cinco carreteras con número pasan a menos de tres kilómetros del Papiol, y una de ellas, la B-23, lleva directa al taller de la red en Sant Joan Despí. Además, el municipio está dentro del área metropolitana.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 12.9},
    "secciones": [
        {"id": "cinco-carreteras", "h2": "B-23, AP-7, A-2, N-IIa y B-30 en tres kilómetros",
         "parrafos": [
             "Desde el centro del Papiol, la B-23 queda a 1,2 km, la AP-7 a 1,4, la A-2 a 1,9, la N-IIa a 2 y la B-30 a 2,4. Para llegar a la nave de Dasercars Barcelona basta con la C-1413a y la B-23: 12,9 km por carretera, 9,2 en línea recta.",
             "Tanta autopista cerca tiene una ventaja para los diésel: un recorrido de vez en cuando a velocidad sostenida permite que el filtro de partículas complete su regeneración, cosa que no ocurre si el coche solo va al pueblo de al lado.",
         ]},
        {"id": "recogida-papiol", "h2": "Dentro del área metropolitana: recogida y coche de cortesía",
         "parrafos": [
             "El Papiol forma parte del Área Metropolitana de Barcelona, y el taller ofrece recogida y entrega del coche y vehículo de cortesía dentro de ella, siempre según disponibilidad. Pídelo al reservar.",
             "El taller trabaja de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00; los fines de semana no abre.",
         ]},
        {"id": "sant-cugat-y-sant-andreu", "h2": "Sant Cugat para lo oficial, Sant Andreu de la Barca para la ITV",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es Quadis Munich, en el carrer Vallespir 19 de Sant Cugat del Vallès, a 14,1 km: algo más lejos que nuestro taller. La ITV más cercana por carretera en el registro de la Generalitat es Sant Andreu (B21), de Applus, en la N-II, punto kilométrico 592,5, en Sant Andreu de la Barca, a 10,7 km.",
         ]},
        {"id": "papiol-en-cifras", "h2": "4.404 vecinos en 8,95 km²",
         "parrafos": [
             "El padrón de 2025 da al Papiol 4.404 habitantes, un 8,2 % más que los 4.071 de 2015. Idescat contaba 2.290 turismos en 2024 a partir de la DGT: 520 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en el Papiol?",
         "a": "Sí: el Papiol está dentro del área metropolitana y hay recogida y entrega, sujetas a disponibilidad."},
        {"q": "¿Cuánto hay hasta el taller?",
         "a": "12,9 km por la C-1413a y la B-23 hasta el carrer del Tambor del Bruc, en Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es Sant Andreu (B21), en Sant Andreu de la Barca, a 10,7 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.404 habitantes (+8,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("081580")},
        {"etiqueta": "Turismos (2024)", "valor": "2.290 · 520 por cada 1.000 hab.", **F.idescat("081580")},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 12,9 km", **F.osrm},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu (B21) · 10,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Cugat · 14,1 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081580"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["el-pont-de-vilomara-i-rocafort"] = {
    "h1": "El Pont de Vilomara i Rocafort: ITV a 9 km en Manresa, taller BMW a 63",
    "entradilla": "Con Manresa a 7,4 km en línea recta, el Pont de Vilomara i Rocafort tiene cerca la ITV y el concesionario del Bages. El taller especialista de la red, en cambio, queda a 63,3 km. Así encaja cada cosa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 63.3},
    "secciones": [
        {"id": "itv-bufalvent", "h2": "La ITV de Manresa, a 9,1 km",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Manresa (B06), de TÜV Rheinland, en el carrer Esteve Terrades del polígono Bufalvent, a 9,1 km. Para una inspección no tiene sentido ir más lejos.",
         ]},
        {"id": "quadis-sant-fruitos", "h2": "El servicio oficial, a 15,2 km en Sant Fruitós",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más cercano es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 15,2 km. Allí van las reparaciones en garantía de BMW.",
             "Nosotros somos un taller independiente especializado en BMW y MINI. Encajamos cuando quieres una alternativa al concesionario para mantenimiento y averías, o cuando un problema concreto de la marca no se ha resuelto en la comarca.",
         ]},
        {"id": "bv1224-c16", "h2": "Por la BV-1224 y la C-16 hasta Sant Joan Despí",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona sale por la BV-1224 hasta la C-16 y sigue por la B-30, la AP-7 y la B-23: 63,3 km por carretera, 39,8 en línea recta.",
             "El municipio no está en el área metropolitana de Barcelona y la recogida del taller no llega aquí. Con 63 km por delante, lo que más ahorra es contar bien el problema por teléfono: síntomas, cuándo aparecen y si hay algún testigo encendido.",
         ]},
        {"id": "pont-en-cifras", "h2": "Un 12,9 % más de vecinos en diez años",
         "parrafos": [
             "El padrón pasó de 3.715 habitantes en 2015 a 4.193 en 2025, en un término de 27,41 km² a 202 metros de altitud. Idescat contaba 2.226 turismos en 2024 a partir de la DGT: 531 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de Manresa (B06), en el polígono Bufalvent, a 9,1 km: es la más próxima por carretera en el registro de la Generalitat."},
        {"q": "¿A cuánto queda vuestro taller?",
         "a": "A 63,3 km por carretera, en Sant Joan Despí."},
        {"q": "¿Reparáis también MINI?",
         "a": "Sí. Comparten electrónica y motores con BMW y se trabajan con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.193 habitantes (+12,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("081825")},
        {"etiqueta": "Turismos (2024)", "valor": "2.226 · 531 por cada 1.000 hab.", **F.idescat("081825")},
        {"etiqueta": "ITV más cercana", "valor": "Manresa (B06) · 9,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 15,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 63,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081825"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
