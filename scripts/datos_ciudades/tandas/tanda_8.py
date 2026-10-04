# Tanda 8: Torrelles de Foix, Gurb, Calldetenes, Albinyana, Sant Llorenç Savall, Sant Quintí de Mediona,
# Fresno de Torote, Bellvei, Castellgalí, Santa Eugènia de Berga, Avinyó, Folgueroles, Bagà, Batres
# y Valdeavero.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py.
# META: metaDescription nueva para las 15 (todas con 0 impresiones en GSC y con promesas
# o presencia falsa en la descripción anterior: «diagnosis oficial», ISTA, «recogida a
# domicilio», «garantía escrita», «Taller BMW en X»...). Se aplica con un script aparte.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
META = {}

# ---------------------------------------------------------------------------
CIUDADES["torrelles-de-foix"] = {
    "h1": "Torrelles de Foix: un 22 % más de vecinos y el taller BMW a 59 km por la AP-7",
    "entradilla": "Entre viñas del Alt Penedès y sin autovía a la puerta, Torrelles de Foix depende de carreteras comarcales para casi todo. Aquí tienes dónde queda la ITV, el servicio oficial BMW y el taller especialista de la red, con distancias reales.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 59.2},
    "secciones": [
        {"id": "comarcales", "h2": "Solo comarcales a menos de tres kilómetros",
         "parrafos": [
             "Las únicas carreteras con matrícula que pasan cerca del centro son la BV-2122, a 1,7 km, y la BP-2121, a 2,2 km. Para un diésel moderno eso tiene una consecuencia práctica: si casi todos los trayectos son cortos y por carretera revirada, el filtro de partículas no llega a la temperatura que necesita para limpiarse solo.",
             "Si el testigo del filtro aparece a menudo, no basta con borrarlo. Lo sensato es revisar el sensor de presión diferencial y el historial de regeneraciones antes de pensar en cambiar nada caro.",
         ]},
        {"id": "ruta-ap7", "h2": "59,2 km hasta el carrer del Tambor del Bruc",
         "parrafos": [
             "La ruta a Dasercars Barcelona baja por la BV-2122 y la BP-2121 hasta la AP-7 y entra al Baix Llobregat por la B-23: 59,2 km por carretera, 40,9 en línea recta. Torrelles no forma parte del área metropolitana, así que el servicio de recogida del taller no llega hasta aquí.",
             "El taller trabaja de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00. Con esa distancia, lo cómodo es entrar a primera hora y volver por la tarde, o dejar el coche si el trabajo es de varios días.",
         ]},
        {"id": "itv-olerdola", "h2": "La ITV del Penedès, en Olèrdola",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es ITV Olèrdola (B09), en la avinguda de l'Hostal Nou, a 17,2 km. El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en l'avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 29,6 km.",
         ]},
        {"id": "torrelles-crece", "h2": "De 2.246 a 2.746 habitantes",
         "parrafos": [
             "El padrón del INE suma 500 vecinos en diez años: un 22,3 % más que en 2015, en un término de 36,72 km² a 367 metros de altitud. Idescat, a partir de la DGT, contaba 1.493 turismos en 2024, es decir, 544 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿A cuánto queda vuestro taller desde Torrelles de Foix?",
         "a": "A 59,2 km por carretera, por la AP-7 y la B-23, en Sant Joan Despí."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No. La recogida solo cubre el área metropolitana de Barcelona y Torrelles queda fuera."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima por carretera es la de Olèrdola (B09), a 17,2 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.746 habitantes (+22,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("082883")},
        {"etiqueta": "Turismos (2024)", "valor": "1.493 · 544 por cada 1.000 hab.", **F.idescat("082883")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 17,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 29,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 59,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082883"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["torrelles-de-foix"] = "BMW en Torrelles de Foix: ITV en Olèrdola a 17,2 km, servicio oficial en Vilanova i la Geltrú y taller especialista de la red a 59,2 km por la AP-7."

# ---------------------------------------------------------------------------
CIUDADES["gurb"] = {
    "h1": "Gurb: 693 turismos por cada mil vecinos y Vic a un paso",
    "entradilla": "En un término de más de 51 km² con masías repartidas, en Gurb casi todo se hace en coche. Lo oficial de BMW y la ITV están en Vic; el taller especialista de la red, a 81,5 km. Te explicamos qué conviene resolver en cada sitio.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 81.5},
    "secciones": [
        {"id": "parque-gurb", "h2": "Un municipio disperso con mucho coche por vecino",
         "parrafos": [
             "Gurb tenía 2.741 habitantes en 2025, un 7,7 % más que en 2015, repartidos en 51,57 km²: 53 por kilómetro cuadrado. Idescat, con datos de la DGT, registraba 1.900 turismos en 2024, 693 por cada 1.000 vecinos. En Calldetenes, a pocos kilómetros, la proporción es de 552.",
             "Cuando el coche es la única forma de moverse, una avería pesa más. Merece la pena no dejar para luego un aviso de servicio ni una fuga pequeña de refrigerante o de aceite.",
         ]},
        {"id": "vic-cerca", "h2": "Concesionario e ITV, en Vic",
         "parrafos": [
             "El servicio oficial BMW más cercano según el localizador de bmw.es es Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 5,9 km por carretera. La ITV que te toca por cercanía es ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22, también en Vic, a 7,8 km según el registro de la Generalitat.",
             "Con la C-17 a 1,5 km y la C-25 a 1,8 km del centro, salir a autovía es fácil, algo que agradece cualquier diésel que necesite regenerar el filtro de partículas.",
         ]},
        {"id": "cuando-bajar", "h2": "81,5 km por la C-17: para qué sí",
         "parrafos": [
             "Hasta la nave de Dasercars Barcelona, en Sant Joan Despí, hay 81,5 km por la C-17, la C-33 y la B-20. No tiene sentido hacerlos por un cambio de pastillas. Sí lo tiene por una avería electrónica que no se ha localizado, un fallo de AdBlue con la cuenta atrás en marcha o un ruido de distribución en un N47.",
             "Antes de mover el coche, una llamada con el modelo, el año y los kilómetros permite saber si el viaje compensa. La recogida del taller no llega a Osona.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Gurb o en Vic?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 81,5 km."},
        {"q": "¿Dónde está el servicio oficial BMW?",
         "a": "Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 5,9 km según bmw.es."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "ITV Osona (B04), en Vic, a 7,8 km por carretera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.741 habitantes (+7,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081000")},
        {"etiqueta": "Turismos (2024)", "valor": "1.900 · 693 por cada 1.000 hab.", **F.idescat("081000")},
        {"etiqueta": "Superficie del término", "valor": "51,57 km²", **F.cartociudad},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 7,8 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 81,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081000"), F.cartociudad_f, F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["gurb"] = "BMW en Gurb (Osona): servicio oficial e ITV en Vic, a menos de 8 km, y el taller especialista de la red en Sant Joan Despí, a 81,5 km. Cuándo compensa el viaje."

# ---------------------------------------------------------------------------
CIUDADES["calldetenes"] = {
    "h1": "Calldetenes: el concesionario BMW a 4,1 km y un especialista independiente a 79",
    "entradilla": "Si buscas el concesionario BMW desde Calldetenes, lo tienes en Vic. Nosotros somos otra cosa: un taller independiente especializado en BMW y MINI, con la nave en Sant Joan Despí. Así se reparten los papeles.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 79.1},
    "secciones": [
        {"id": "concesionario-vic", "h2": "Quadis Munich, a 4,1 km",
         "parrafos": [
             "El punto oficial BMW que el localizador de bmw.es sitúa más cerca es Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic: 4,1 km por carretera, 2,9 en línea recta. Para una reparación cubierta por la garantía de BMW, esa cita es con ellos.",
             "Para el mantenimiento puedes elegir. El Reglamento (UE) 461/2010 impide que el fabricante condicione la garantía a revisar el coche en su red, siempre que se sigan los intervalos y se usen aceites y recambios con la especificación correcta.",
         ]},
        {"id": "segunda-opinion", "h2": "Dónde encaja un taller a 79 kilómetros",
         "parrafos": [
             "Con todo lo oficial a menos de cinco kilómetros, la razón para bajar a Sant Joan Despí tiene que ser concreta: un segundo diagnóstico antes de aceptar una reparación cara, un testigo que vuelve una y otra vez, o un problema de los diésel N47, N57 o B47 que ya conocemos bien.",
             "La ruta va por la C-17, la C-33 y la B-20: 79,1 km. Como Calldetenes queda fuera del área metropolitana, el viaje lo haces tú.",
         ]},
        {"id": "itv-osona", "h2": "La ITV de Osona, a 4,8 km",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22 de Vic, a 4,8 km.",
         ]},
        {"id": "calldetenes-en-cifras", "h2": "Un término de 5,8 km² y 471 vecinos por kilómetro cuadrado",
         "parrafos": [
             "Calldetenes es pequeño en superficie: 2.733 habitantes en 2025, un 12,6 % más que diez años antes, a 489 metros de altitud. En 2024 tenía 1.509 turismos (Idescat, con datos de la DGT), 552 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Vic?",
         "a": "No. El servicio oficial es Quadis Munich, en el carrer Perot Rocaguinarda 1. Nosotros somos Dasercars, taller independiente en Sant Joan Despí."},
        {"q": "¿Pierdo la garantía si reviso el coche con vosotros?",
         "a": "No, mientras se respeten los intervalos y especificaciones del plan de mantenimiento."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "79,1 km por la C-17, la C-33 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.733 habitantes (+12,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("080370")},
        {"etiqueta": "Turismos (2024)", "valor": "1.509 · 552 por cada 1.000 hab.", **F.idescat("080370")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 4,1 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 4,8 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 79,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080370"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}
META["calldetenes"] = "Calldetenes: concesionario BMW e ITV en Vic, a menos de 5 km, y taller especialista independiente BMW y MINI en Sant Joan Despí, a 79,1 km."

# ---------------------------------------------------------------------------
CIUDADES["albinyana"] = {
    "h1": "Albinyana, en el Baix Penedès: ITV a 7,8 km y especialista BMW a 65 km",
    "entradilla": "Con la AP-7 a menos de tres kilómetros y la ITV de la comarca en Bellvei, desde Albinyana casi todo está a mano salvo el taller especialista de la red, que queda en Sant Joan Despí. Esto es lo que te conviene saber.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 65.1},
    "secciones": [
        {"id": "itv-els-massets", "h2": "La ITV del Baix Penedès, en el polígono Els Massets",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la del Baix Penedès (T07), en el polígono industrial Els Massets de Bellvei, a 7,8 km del centro de Albinyana.",
             "Si el coche tiene un aviso pendiente —una luz fundida, una rótula con holgura— es mejor resolverlo antes de la cita. Un rechazo por algo pequeño obliga a volver.",
         ]},
        {"id": "c51-c32", "h2": "Por la C-51 y la C-32 hasta el Baix Llobregat",
         "parrafos": [
             "Hasta la nave de Dasercars Barcelona hay 65,1 km por carretera y 49,4 en línea recta. El recorrido sale por la C-51, enlaza con la C-31 y la C-32 y termina por la B-25 en Sant Joan Despí. La recogida del taller se limita al área metropolitana de Barcelona, así que aquí no llega.",
             "Para que el viaje compense, que sea por algo que de verdad pide un especialista en la marca: electrónica, diagnosis de un fallo intermitente, cadena de distribución o el sistema de AdBlue.",
         ]},
        {"id": "oficial-vilanova", "h2": "El servicio oficial más cercano, en Vilanova i la Geltrú",
         "parrafos": [
             "Según bmw.es, el punto oficial BMW más próximo es Quadis Munich, en l'avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 29,6 km. Es el concesionario de referencia para la comarca, aunque queda más lejos que la ITV.",
         ]},
        {"id": "albinyana-cifras", "h2": "593 turismos por cada mil habitantes",
         "parrafos": [
             "Albinyana tenía 2.718 vecinos en 2025, un 17,2 % más que en 2015. Idescat contaba 1.612 turismos en 2024, a partir de la DGT. La costa queda a unos 7 km del centro: lo bastante lejos para que el salitre no sea el problema principal, aunque un lavado de bajos después del verano nunca sobra.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Albinyana?",
         "a": "En la estación del Baix Penedès (T07), en el polígono Els Massets de Bellvei, a 7,8 km."},
        {"q": "¿Hay recogida del coche en Albinyana?",
         "a": "No: el servicio de recogida del taller no llega fuera del área metropolitana de Barcelona."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 65,1 km por carretera, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.718 habitantes (+17,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Penedès", **F.idescat("430022")},
        {"etiqueta": "Turismos (2024)", "valor": "1.612 · 593 por cada 1.000 hab.", **F.idescat("430022")},
        {"etiqueta": "ITV más cercana", "valor": "Baix Penedès (T07), Bellvei · 7,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 29,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 65,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("430022"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["albinyana"] = "BMW en Albinyana: ITV del Baix Penedès a 7,8 km, servicio oficial en Vilanova i la Geltrú y taller especialista de la red a 65,1 km por la C-32."

# ---------------------------------------------------------------------------
CIUDADES["sant-llorenc-savall"] = {
    "h1": "Sant Llorenç Savall: taller autorizado BMW en Castellar y especialista por la C-16",
    "entradilla": "Sant Llorenç Savall está bien comunicado solo por la B-124. Por eso importa saber qué queda más a mano: un taller autorizado BMW en Castellar del Vallès, la ITV en Sabadell y nuestro taller, a 53,1 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 53.1},
    "secciones": [
        {"id": "sin-autovia", "h2": "Ninguna autovía a menos de tres kilómetros",
         "parrafos": [
             "En el entorno inmediato del pueblo no pasa ninguna carretera principal: para salir a la red rápida hay que bajar por la B-124. Un coche que hace casi siempre trayectos cortos de montaña trabaja de otra manera que uno de autopista: más frenada, más calor en los discos y, en los diésel, menos ocasiones de regenerar el filtro de partículas.",
             "El líquido de frenos, que absorbe humedad con el tiempo, y las pastillas son lo primero que conviene vigilar con ese uso.",
         ]},
        {"id": "tallcar", "h2": "Lo autorizado: Tallcar, a 13,3 km",
         "parrafos": [
             "El punto de servicio BMW más próximo en el localizador de bmw.es es Tallcar, un taller autorizado sin venta en la calle Suiza 6 de Castellar del Vallès, a 13,3 km por carretera. Para lo que depende de la marca, es la referencia más cercana.",
         ]},
        {"id": "itv-sabadell", "h2": "La ITV, a 24,9 km en Can Roqueta",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Sabadell (B24), en el polígono Can Roqueta, a 24,9 km. Con casi 25 km hasta la estación, conviene llegar con el coche revisado y no tener que repetir el viaje.",
         ]},
        {"id": "b124-c16", "h2": "Por la B-124 y la C-16 hasta Sant Joan Despí",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona baja por la B-124 y la C-1415a, toma la C-16 y acaba por la B-20: 53,1 km por carretera, 35,6 en línea recta. El municipio no pertenece al área metropolitana, de modo que la recogida del taller no llega hasta aquí.",
             "Sant Llorenç tenía 2.587 vecinos en 2025 (un 8,7 % más que en 2015) y 1.351 turismos en 2024 según Idescat, 522 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el taller BMW autorizado más cercano?",
         "a": "Tallcar, en la calle Suiza 6 de Castellar del Vallès, a 13,3 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de Sabadell (B24), en el polígono Can Roqueta, a 24,9 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "53,1 km por la B-124, la C-16 y la B-20, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.587 habitantes (+8,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082233")},
        {"etiqueta": "Turismos (2024)", "valor": "1.351 · 522 por cada 1.000 hab.", **F.idescat("082233")},
        {"etiqueta": "Taller autorizado BMW", "valor": "Tallcar, Castellar del Vallès · 13,3 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sabadell (B24) · 24,9 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 53,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082233"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["sant-llorenc-savall"] = "BMW en Sant Llorenç Savall: taller autorizado en Castellar del Vallès a 13,3 km, ITV en Sabadell y taller especialista de la red a 53,1 km."

# ---------------------------------------------------------------------------
CIUDADES["sant-quinti-de-mediona"] = {
    "h1": "Sant Quintí de Mediona: oficial a 31 km, especialista BMW a 48,6",
    "entradilla": "Desde Sant Quintí de Mediona, el servicio oficial BMW y el taller especialista de la red quedan a distancias parecidas. Lo que decide cuál te conviene no son los kilómetros, sino qué le pasa al coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 48.6},
    "secciones": [
        {"id": "dos-distancias", "h2": "31,2 km a Vilanova, 48,6 a Sant Joan Despí",
         "parrafos": [
             "El punto oficial BMW más próximo según el localizador de bmw.es es Quadis Munich, en l'avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 31,2 km por carretera. La nave de Dasercars Barcelona, en el carrer del Tambor del Bruc 3, está a 48,6 km.",
             "Una campaña de la marca o una reparación cubierta por la garantía de BMW van a Vilanova. Un taller independiente especializado tiene sentido cuando buscas otra forma de trabajar el mantenimiento o cuando una avería no se ha resuelto donde la llevaste.",
         ]},
        {"id": "c15-ap7", "h2": "La C-15 al lado y la AP-7 de camino",
         "parrafos": [
             "La C-15 pasa a 1,3 km del centro y la BP-2151 a 1,2 km. La ruta al taller sigue la BP-2151 y la BV-2244 hasta la AP-7 y entra por la B-23: 34,2 km en línea recta, 48,6 por carretera. El municipio está fuera del área metropolitana y la recogida del taller no llega.",
             "Antes de bajar, llama con modelo, año y kilometraje y cuenta el síntoma con detalle. A veces basta para saber qué pieza hará falta y tenerla pedida.",
         ]},
        {"id": "itv-olerdola", "h2": "La ITV, en Olèrdola",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Olèrdola (B09), en la avinguda de l'Hostal Nou, a 16,6 km.",
         ]},
        {"id": "sant-quinti-crece", "h2": "Un 21,9 % más de población",
         "parrafos": [
             "Sant Quintí pasó de 2.116 habitantes en 2015 a 2.580 en 2025, en 13,84 km² a 326 metros de altitud. Idescat, con datos de la DGT, contaba 1.351 turismos en 2024: 524 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué queda más cerca, el oficial o vuestro taller?",
         "a": "El servicio oficial de Vilanova i la Geltrú, a 31,2 km. Nuestro taller de Sant Joan Despí está a 48,6 km."},
        {"q": "¿Recogéis el coche en Sant Quintí?",
         "a": "No: el servicio de recogida del taller solo cubre el área metropolitana de Barcelona."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Olèrdola (B09), a 16,6 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.580 habitantes (+21,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("082362")},
        {"etiqueta": "Turismos (2024)", "valor": "1.351 · 524 por cada 1.000 hab.", **F.idescat("082362")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 31,2 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 16,6 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 48,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082362"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["sant-quinti-de-mediona"] = "BMW en Sant Quintí de Mediona: servicio oficial en Vilanova i la Geltrú a 31,2 km, ITV en Olèrdola y taller especialista de la red a 48,6 km."

# ---------------------------------------------------------------------------
CIUDADES["fresno-de-torote"] = {
    "h1": "Fresno de Torote: el taller BMW de Alcobendas, a 27,8 km por la R-2",
    "entradilla": "Fresno de Torote tiene el taller de la red a 27,8 km, una distancia razonable incluso para trabajos de un solo día. Ruta, ITV, servicio oficial y lo que hay que preguntar sobre la recogida.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 27.8},
    "secciones": [
        {"id": "m113-r2", "h2": "Por la M-113, la R-2 y la M-50",
         "parrafos": [
             "Desde el núcleo urbano hasta la calle Valgrande 17 de Alcobendas hay 27,8 km por carretera y 21,1 en línea recta. La ruta sale por la M-113, toma la R-2 y entra por la M-50.",
             "Si el trabajo dura varios días, pregunta al reservar por el vehículo de cortesía y por la recogida y entrega: existen dentro del área metropolitana de Madrid y están sujetos a disponibilidad, así que confirma si tu dirección entra.",
         ]},
        {"id": "presupuesto", "h2": "Cómo se decide qué se hace",
         "parrafos": [
             "Nada se toca sin que hayas visto antes el presupuesto por escrito y lo hayas aceptado. La diagnosis también tiene su presupuesto, porque es trabajo técnico.",
             "Si el coche es un MINI, el procedimiento es el mismo: comparte electrónica y buena parte de los motores con BMW.",
         ]},
        {"id": "itv-y-oficial", "h2": "ITV en Paracuellos, servicio oficial en Algete",
         "parrafos": [
             "Para la inspección, la estación oficial más cercana por carretera es la de DEKRA (estación 2808), en el camino Viejo de Cobeña 36 de Paracuellos de Jarama, a 17,9 km según el listado de la Comunidad de Madrid. El servicio oficial BMW más cercano según bmw.es es BYmyCAR Madrid, en la calle Tejera 2 de Algete, a 20,7 km.",
         ]},
        {"id": "fresno-cifras", "h2": "703 turismos por cada mil vecinos",
         "parrafos": [
             "Fresno tenía 2.561 habitantes en 2025, un 25,5 % más que en 2015. La Comunidad de Madrid, a partir de la DGT, contaba 1.800 turismos en 2025: 703 por cada 1.000 habitantes, casi el doble que en Madrid capital (388). Sin ninguna carretera principal a menos de tres kilómetros del centro, el coche se usa sobre todo en carreteras locales.",
         ]},
    ],
    "faq": [
        {"q": "¿A qué distancia está el taller?",
         "a": "A 27,8 km por la M-113, la R-2 y la M-50, en la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Hay recogida del coche en Fresno de Torote?",
         "a": "La recogida y entrega se ofrece dentro del área metropolitana de Madrid, sujeta a disponibilidad. Pregunta al reservar si tu dirección entra."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación 2808 de DEKRA, en el camino Viejo de Cobeña 36 de Paracuellos de Jarama, a 17,9 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.561 habitantes (+25,5 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "1.800 · 703 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "DEKRA (2808), Paracuellos de Jarama · 17,9 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid, Algete · 20,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 27,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["fresno-de-torote"] = "BMW en Fresno de Torote: taller especialista de la red en Alcobendas a 27,8 km por la R-2, ITV en Paracuellos de Jarama y servicio oficial en Algete."

# ---------------------------------------------------------------------------
CIUDADES["bellvei"] = {
    "h1": "Bellvei: la ITV del Baix Penedès en casa y el taller BMW a 58,6 km",
    "entradilla": "En el polígono Els Massets de Bellvei está la estación de ITV que usan buena parte de los pueblos de alrededor. El taller especialista de la red queda en Sant Joan Despí; aquí tienes la ruta y lo que conviene saber.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 58.6},
    "secciones": [
        {"id": "itv-propia", "h2": "La estación T07, dentro del término",
         "parrafos": [
             "El registro de estaciones de la Generalitat sitúa la ITV del Baix Penedès (T07) en el polígono industrial Els Massets, en el propio municipio. Es la más próxima por carretera también para Albinyana y para El Vendrell.",
             "Tenerla tan cerca simplifica las cosas: si la inspección sale desfavorable por algo menor, volver no cuesta nada. Lo que conviene es no llevar el coche con testigos encendidos en el cuadro.",
         ]},
        {"id": "n340", "h2": "La N-340 cruza el pueblo",
         "parrafos": [
             "La N-340 pasa a 0,1 km del centro y la TV-2126 a 0,5 km; en un radio de tres kilómetros están también la TP-2125, la C-51 y la C-31. La costa queda a unos 5,2 km.",
             "Con tanta carretera alrededor, es fácil dar a un diésel recorridos largos que ayudan a mantener limpio el filtro de partículas. Lo que sí castiga el uso diario por travesías y rotondas es el embrague y los frenos.",
         ]},
        {"id": "ruta-c32", "h2": "58,6 km por la C-32",
         "parrafos": [
             "Hasta la nave de Dasercars Barcelona se va por la TV-2126, la C-32 y la B-25: 58,6 km por carretera, 43,6 en línea recta. Bellvei no está en el área metropolitana y la recogida del taller no llega aquí.",
             "El servicio oficial BMW más próximo según bmw.es es Quadis Munich, en l'avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 23,1 km.",
         ]},
        {"id": "bellvei-cifras", "h2": "604 turismos por cada mil habitantes",
         "parrafos": [
             "Bellvei tenía 2.460 vecinos en 2025, un 12,6 % más que en 2015, en un término de 8,27 km². Idescat, con datos de la DGT, registraba 1.486 turismos en 2024.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Bellvei?",
         "a": "Sí: la estación del Baix Penedès (T07), en el polígono Els Massets, según el registro de la Generalitat."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "58,6 km por la C-32 y la B-25, hasta Sant Joan Despí."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Vilanova i la Geltrú, a 23,1 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.460 habitantes (+12,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Penedès", **F.idescat("430249")},
        {"etiqueta": "Turismos (2024)", "valor": "1.486 · 604 por cada 1.000 hab.", **F.idescat("430249")},
        {"etiqueta": "ITV en el municipio", "valor": "Baix Penedès (T07), polígono Els Massets", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 23,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 58,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("430249"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["bellvei"] = "BMW en Bellvei: ITV del Baix Penedès en el propio municipio, servicio oficial en Vilanova i la Geltrú y taller especialista de la red a 58,6 km."

# ---------------------------------------------------------------------------
CIUDADES["castellgali"] = {
    "h1": "Castellgalí: entre la C-55 y la C-16, a 51,7 km del taller BMW",
    "entradilla": "Castellgalí ha ganado un 20,9 % de población en diez años y tiene dos vías rápidas casi en la puerta. Para la inspección y el concesionario se mira hacia Manresa y Sant Fruitós; para un especialista independiente, hacia el Baix Llobregat.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 51.7},
    "secciones": [
        {"id": "c55-c16", "h2": "La C-55 a 0,6 km, la C-16 a 2,4 km",
         "parrafos": [
             "Las dos vías principales del eje quedan cerca: la C-55 pasa a 0,6 km del centro y la C-16 a 2,4 km. Para el coche eso significa trayectos de carretera abierta con frecuencia, que es justo lo que necesita un diésel para quemar el hollín del filtro de partículas.",
             "Lo que no perdona ese uso es el aceite pasado de intervalo: con muchos kilómetros a régimen sostenido, respeta el indicador de servicio y la especificación que pide tu motor.",
         ]},
        {"id": "manresa-y-sant-fruitos", "h2": "Inspección en Bufalvent, concesionario a 13,1 km",
         "parrafos": [
             "Para pasar la ITV, la opción lógica desde el núcleo urbano es la B06 de Manresa, en el polígono Bufalvent: 7,2 km por carretera y 4,5 en línea recta, según las coordenadas del registro de la Generalitat.",
             "El concesionario con taller que el buscador de bmw.es pone más cerca es Quadis Munich, junto a la carretera de Manresa a Berga en Sant Fruitós de Bages, a 13,1 km. Las llamadas a revisión que convoca BMW se atienden en su red; para el resto del mantenimiento, el taller lo eliges tú.",
         ]},
        {"id": "ruta-taller", "h2": "51,7 km hasta el Tambor del Bruc",
         "parrafos": [
             "La nave de Dasercars Barcelona, en Sant Joan Despí, queda a 51,7 km por carretera y 38,9 en línea recta: se baja por la C-55 hasta la C-16 y se entra por la B-20. Castellgalí no está en el área metropolitana, así que la recogida del taller no cubre el municipio.",
             "El padrón pasó de 1.996 vecinos en 2015 a 2.413 en 2025, en 17,21 km². Idescat, a partir de la DGT, contaba 1.354 turismos en 2024: 561 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV me queda más cerca en Castellgalí?",
         "a": "La de Manresa (B06), en el polígono Bufalvent, a 7,2 km por carretera."},
        {"q": "¿Y el concesionario BMW?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 13,1 km según bmw.es."},
        {"q": "¿Llega la recogida del taller a Castellgalí?",
         "a": "No: solo cubre el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.413 habitantes (+20,9 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "17,21 km²", **F.cartociudad},
        {"etiqueta": "Turismos (2024)", "valor": "1.354 · 561 por cada 1.000 hab.", **F.idescat("080615")},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 51,7 km", **F.osrm},
        {"etiqueta": "ITV (Manresa, B06)", "valor": "polígono Bufalvent · 7,2 km", **F.itv_cat},
        {"etiqueta": "Concesionario BMW", "valor": "Sant Fruitós de Bages · 13,1 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080615"), F.cartociudad_f, F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["castellgali"] = "BMW en Castellgalí: ITV en Manresa a 7,2 km, servicio oficial en Sant Fruitós de Bages y taller especialista de la red a 51,7 km por la C-16."

# ---------------------------------------------------------------------------
CIUDADES["santa-eugenia-de-berga"] = {
    "h1": "Santa Eugènia de Berga: qué revisar en un BMW que hace pocos kilómetros",
    "entradilla": "Con Vic a 3,1 km y Calldetenes casi pegado, muchos coches de Santa Eugènia de Berga se mueven poco y en recorridos cortos. Eso cambia lo que hay que vigilar. Y si hace falta un especialista, el de la red está a 80,3 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 80.3},
    "secciones": [
        {"id": "por-tiempo", "h2": "Lo que caduca aunque el coche no ruede",
         "parrafos": [
             "En un coche que hace pocos kilómetros, el plan de mantenimiento salta antes por fecha que por distancia. El aceite envejece y acumula condensación en trayectos fríos; el líquido de frenos absorbe humedad; la batería sufre si el motor apenas llega a cargarla.",
             "En un BMW, además, cuando se cambia la batería hay que registrarla en la centralita para que la carga se ajuste a la nueva. Es un paso que se olvida a menudo y acorta su vida.",
         ]},
        {"id": "vic-al-lado", "h2": "Servicio oficial e ITV, en Vic",
         "parrafos": [
             "El localizador de bmw.es da como punto oficial más cercano Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 5,2 km. Es donde se gestionan las campañas que convoca el fabricante. La ITV más próxima por carretera según la Generalitat es ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22, a 6,2 km.",
         ]},
        {"id": "b520-c17", "h2": "De la B-520 a la C-17",
         "parrafos": [
             "La ruta a Dasercars Barcelona sale por la B-520, enlaza con la C-17 y sigue por la C-33 y la B-20: 80,3 km por carretera, 63,1 en línea recta. Cerca del centro pasan la C-25, a 2,1 km, y la C-17, a 2,6 km: una salida por autovía de vez en cuando le sienta bien a un diésel que hace poca distancia.",
             "La recogida del taller no llega fuera del área metropolitana, así que el viaje solo compensa para una avería de BMW que no se resuelve en la comarca.",
         ]},
        {"id": "santa-eugenia-cifras", "h2": "629 turismos por cada mil habitantes",
         "parrafos": [
             "Santa Eugènia de Berga tenía 2.348 vecinos en 2025, un 6,5 % más que en 2015, en 7,01 km² a 538 metros de altitud. Idescat registraba 1.476 turismos en 2024, a partir de la DGT.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay que registrar la batería nueva en un BMW?",
         "a": "Sí. Sin registrarla, la centralita sigue cargando como si fuera la vieja y la nueva dura menos."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Vic, a 5,2 km según bmw.es."},
        {"q": "¿A cuánto queda vuestro taller?",
         "a": "A 80,3 km por carretera, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.348 habitantes (+6,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082460")},
        {"etiqueta": "Turismos (2024)", "valor": "1.476 · 629 por cada 1.000 hab.", **F.idescat("082460")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 5,2 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 6,2 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 80,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082460"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["santa-eugenia-de-berga"] = "BMW en Santa Eugènia de Berga: servicio oficial e ITV en Vic y taller especialista de la red en Sant Joan Despí, a 80,3 km. Qué revisar si el coche rueda poco."

# ---------------------------------------------------------------------------
CIUDADES["avinyo"] = {
    "h1": "Avinyó: 63 km² de término, la C-25 al lado y el taller BMW a 79 km",
    "entradilla": "Avinyó reparte a sus vecinos en un término de 63,23 km²: 37 habitantes por kilómetro cuadrado. Para un BMW o un MINI de aquí, lo más cercano está en Sant Fruitós de Bages; el taller especialista de la red, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 79.2},
    "secciones": [
        {"id": "sant-fruitos", "h2": "Concesionario e ITV, los dos en Sant Fruitós",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, a 18,1 km. La ITV más cercana por carretera en el registro de la Generalitat también está en Sant Fruitós de Bages: la B25, en el polígono industrial El Grau, a 23,1 km.",
             "Con las dos cosas en el mismo municipio, se pueden encajar el mismo día si el coche tiene que pasar por ambas.",
         ]},
        {"id": "c25", "h2": "La C-25, a 0,7 km del centro",
         "parrafos": [
             "La C-25 pasa a 0,7 km y la B-431 a 0,5 km. En un término de 63,23 km², con masías y núcleos separados, muchos recorridos empiezan por caminos y pistas antes de llegar al asfalto. Ese uso se nota en neumáticos, silentblocks y protecciones de bajos, más que en el motor.",
         ]},
        {"id": "ruta-taller", "h2": "79,2 km por la C-25 y la C-16",
         "parrafos": [
             "Hasta la nave de Dasercars Barcelona hay 79,2 km por la BP-4313, la C-25, la C-16 y la B-20; 55,1 en línea recta. La recogida del taller no llega aquí: solo cubre el área metropolitana de Barcelona.",
             "Si decides bajar, el presupuesto se entrega por escrito y no se empieza nada sin tu visto bueno. Así sabes a qué atenerte antes de dejar el coche tan lejos de casa.",
         ]},
        {"id": "avinyo-cifras", "h2": "2.322 vecinos y 1.351 turismos",
         "parrafos": [
             "El padrón de 2025 da a Avinyó 2.322 habitantes, un 3,3 % más que en 2015. Idescat, con datos de la DGT, contaba 1.351 turismos en 2024: 582 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Avinyó?",
         "a": "La más próxima por carretera es la de Sant Fruitós (B25), en el polígono El Grau, a 23,1 km."},
        {"q": "¿Dónde está el servicio oficial BMW?",
         "a": "Quadis Munich, en la carretera de Manresa a Berga, km 34,5 (Sant Fruitós de Bages), a 18,1 km."},
        {"q": "¿Me dais presupuesto antes de reparar?",
         "a": "Sí, por escrito, y no se empieza ningún trabajo sin tu aprobación."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.322 habitantes (+3,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("080121")},
        {"etiqueta": "Superficie del término", "valor": "63,23 km²", **F.cartociudad},
        {"etiqueta": "Turismos (2024)", "valor": "1.351 · 582 por cada 1.000 hab.", **F.idescat("080121")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Fruitós (B25) · 23,1 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 79,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080121"), F.cartociudad_f, F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["avinyo"] = "BMW en Avinyó (Bages): servicio oficial e ITV en Sant Fruitós de Bages y taller especialista de la red en Sant Joan Despí, a 79,2 km por la C-16."

# ---------------------------------------------------------------------------
CIUDADES["folgueroles"] = {
    "h1": "Folgueroles: ITV a 6,7 km en Vic y el especialista BMW a 89,4",
    "entradilla": "Folgueroles tiene hoy algo menos de población que hace diez años. Para el coche, lo esencial está en Vic; nuestro taller queda a 89,4 km, y te contamos cuándo merece la pena.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 89.4},
    "secciones": [
        {"id": "en-vic", "h2": "Lo que se resuelve en Vic",
         "parrafos": [
             "Vic lo concentra casi todo. Hasta la estación de inspección de Osona (B04), que la Generalitat sitúa en Sant Llorenç Desmunts 22, hay 6,7 km; hasta Quadis Munich, el concesionario con servicio oficial que da bmw.es en Perot Rocaguinarda 1, otros 7,2.",
             "Inspección, revisiones sencillas y pequeñas reparaciones: nada de eso justifica salir de la comarca.",
         ]},
        {"id": "cuando-89-km", "h2": "Cuándo sí merecen la pena 89,4 km",
         "parrafos": [
             "Cuando hay una avería propia de BMW que no se ha solucionado cerca: un fallo eléctrico intermitente, una válvula EGR o un filtro de partículas que vuelven a dar guerra, una caja automática que da tirones. O cuando quieres un segundo diagnóstico antes de una reparación cara.",
             "En ese caso, recibirás el presupuesto por escrito antes de cualquier intervención, y sin tu aprobación no se empieza. Mejor saberlo antes de hacer el viaje.",
         ]},
        {"id": "ruta-c25", "h2": "C-25, C-17, C-33 y B-20",
         "parrafos": [
             "Desde el pueblo se coge la C-25, a kilómetro y medio del centro; después vienen la C-17 hacia el sur, la C-33 y, para acabar, la B-20 hasta la nave de Sant Joan Despí. En total, 89,4 km de carretera (66,9 a vuelo de pájaro). Folgueroles queda fuera del área metropolitana, así que el coche lo tendrías que traer tú.",
         ]},
        {"id": "folgueroles-cifras", "h2": "2.262 vecinos, 23 menos que en 2015",
         "parrafos": [
             "El padrón del INE da a Folgueroles 2.285 habitantes en 2015 y 2.262 en 2025, un 1 % menos. En 2024 había 1.312 turismos según Idescat a partir de la DGT, 580 por cada 1.000 vecinos, en un término de 10,47 km² a 552 metros de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay algún taller vuestro en Osona?",
         "a": "No. Nuestro único taller en Cataluña es Dasercars Barcelona, en Sant Joan Despí: 89,4 km desde Folgueroles."},
        {"q": "¿Y para la inspección técnica?",
         "a": "La estación B04 de Vic, a 6,7 km. Es la de Osona en el registro de la Generalitat."},
        {"q": "¿Trabajáis también MINI?",
         "a": "Sí. MINI y BMW comparten electrónica y buena parte de los motores."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.262 habitantes (-1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("080832")},
        {"etiqueta": "Turismos (2024)", "valor": "1.312 · 580 por cada 1.000 hab.", **F.idescat("080832")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 6,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 7,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 89,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080832"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["folgueroles"] = "BMW en Folgueroles: ITV y servicio oficial en Vic, a unos 7 km, y el taller especialista de la red en Sant Joan Despí, a 89,4 km. Cuándo compensa."

# ---------------------------------------------------------------------------
CIUDADES["baga"] = {
    "h1": "Bagà: 123,6 km de C-16 hasta el taller BMW, y lo que tienes antes",
    "entradilla": "Desde Bagà, el taller especialista de la red queda a más de cien kilómetros en línea recta. No vamos a disimularlo: para casi todo hay opciones más cerca. Esta página te dice cuáles y para qué sí compensa bajar.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 123.6},
    "secciones": [
        {"id": "toda-la-c16", "h2": "Una sola carretera: la C-16",
         "parrafos": [
             "La C-16 pasa a 0,3 km del núcleo urbano y es prácticamente toda la ruta: desde Bagà hasta la B-20 y la nave de Dasercars Barcelona en Sant Joan Despí hay 123,6 km por carretera, 100,1 en línea recta. La recogida del taller no llega aquí: solo cubre el área metropolitana de Barcelona.",
             "Con esa distancia, haz primero una llamada: con modelo, año, kilometraje y el síntoma bien descrito se puede orientar si el problema justifica el viaje o se resuelve en el Berguedà.",
         ]},
        {"id": "itv-berga", "h2": "La ITV, en el polígono La Valldan de Berga",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Berga (B13), en el camí de Sant Bartomeu del polígono industrial La Valldan, a 24,4 km.",
         ]},
        {"id": "oficial-sant-fruitos", "h2": "El servicio oficial, bajando al Bages",
         "parrafos": [
             "Entre los puntos de la red oficial en España que da el localizador de bmw.es, el más próximo por carretera es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 62,5 km, casi todos por la C-16. Es la referencia para lo que cubre la garantía de BMW y para las campañas de revisión.",
         ]},
        {"id": "frio-y-montana", "h2": "Invierno a 785 metros",
         "parrafos": [
             "Bagà está a 785 metros de altitud. Las mañanas de invierno ponen a prueba la batería, sobre todo en BMW con arranque y parada automático; si notas que el motor de arranque gira con pereza, revísala antes de que falle. Y en los puertos de montaña, el líquido de frenos en buen estado no es opcional.",
             "El municipio tenía 2.161 vecinos en 2025, un 1,2 % menos que en 2015, y 1.116 turismos en 2024 según Idescat.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller cerca de Bagà?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 123,6 km por la C-16."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En ITV Berga (B13), en el polígono La Valldan, a 24,4 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 62,5 km por carretera según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.161 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080168")},
        {"etiqueta": "Altitud", "valor": "785 m", **F.idescat("080168")},
        {"etiqueta": "Turismos (2024)", "valor": "1.116 · 516 por cada 1.000 hab.", **F.idescat("080168")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 24,4 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 123,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080168"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["baga"] = "BMW en Bagà (Berguedà): ITV en Berga a 24,4 km y taller especialista de la red en Sant Joan Despí, a 123,6 km por la C-16. Cuándo compensa el viaje."

# ---------------------------------------------------------------------------
CIUDADES["batres"] = {
    "h1": "Batres: ITV en Humanes o Navalcarnero, oficial en Getafe o Leganés y especialista BMW",
    "entradilla": "Batres ha crecido un 26 % en diez años. Para un BMW o un MINI de aquí, esto es lo que hay cerca y lo que supone subir hasta Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 56.5},
    "secciones": [
        {"id": "itv-humanes-navalcarnero", "h2": "Dos ITV casi a la par: Humanes y Navalcarnero",
         "parrafos": [
             "En el listado de la Comunidad de Madrid, las dos estaciones más cercanas por carretera quedan casi a la par: la de Alcaravan ITV (estación 2829), en la avenida de Fuenlabrada 15 de Humanes, a 15,1 km, y la de TÜV Rheinland Ibérica (estación 2845), en el paseo de Alparrache 26 del polígono El Alparrache de Navalcarnero, a 15,5.",
         ]},
        {"id": "garantia", "h2": "Garantía de BMW y taller independiente",
         "parrafos": [
             "Según bmw.es, los dos puntos oficiales BMW más próximos son de Vehinter y quedan casi a la misma distancia: el de la carretera Madrid-Toledo, km 14,700, en Getafe, a 22,7 km, y Momentum Leganés, a 23. Si el coche está en garantía, revisarlo fuera de la red no la anula: la normativa europea de distribución de vehículos (Reglamento UE 461/2010) lo protege mientras se cumplan los intervalos y las especificaciones del fabricante.",
         ]},
        {"id": "ap41-r5", "h2": "Por la AP-41, la R-5 y la M-30",
         "parrafos": [
             "Desde el núcleo urbano hasta la calle Valgrande 17 de Alcobendas hay 56,5 km por carretera y 43,1 en línea recta. La ruta sale por la M-404, que pasa a 0,5 km, toma la AP-41 y la R-5, cruza Madrid por la M-30 y termina por la A-1.",
             "Para trabajos largos, pregunta al reservar por el vehículo de cortesía y por la recogida: los dos se ofrecen solo dentro del área metropolitana de Madrid y sujetos a disponibilidad, así que confirma si Batres entra.",
         ]},
        {"id": "batres-cifras", "h2": "De 1.568 a 1.976 vecinos",
         "parrafos": [
             "El padrón del INE sitúa a Batres en 1.976 habitantes en 2025, un 26 % más que en 2015, en 21,2 km² a 596 metros de altitud. La Comunidad de Madrid, a partir de la DGT, contaba 1.358 turismos en 2025: 687 por cada 1.000 vecinos.",
             "Con la AP-41 a 2,3 km, un diésel tiene a mano el recorrido largo y constante que necesita de vez en cuando para que el filtro de partículas se regenere.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Batres?",
         "a": "Hay dos casi a la par: la estación 2829, en la avenida de Fuenlabrada 15 de Humanes, a 15,1 km, y la 2845, en el polígono El Alparrache de Navalcarnero, a 15,5."},
        {"q": "¿Pierdo la garantía si reviso el BMW con vosotros?",
         "a": "No, si se siguen los intervalos y especificaciones del plan de mantenimiento."},
        {"q": "¿Recogéis el coche en Batres?",
         "a": "La recogida existe dentro del área metropolitana de Madrid, sujeta a disponibilidad. Confirma al pedir cita si tu dirección entra."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.976 habitantes (+26 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "1.358 · 687 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "Estación 2829, Humanes · 15,1 km (2845, Navalcarnero · 15,5)", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe · 22,7 km; Leganés · 23 km)", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 56,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}
META["batres"] = "BMW en Batres: ITV en Humanes o Navalcarnero, a unos 15 km, servicio oficial en Getafe o Leganés y taller especialista de la red en Alcobendas, a 56,5 km."

# ---------------------------------------------------------------------------
CIUDADES["valdeavero"] = {
    "h1": "Valdeavero: un 30,7 % más de vecinos y el taller BMW a 54,8 km",
    "entradilla": "En línea recta, Alcobendas está a 28,7 km de Valdeavero; por carretera, casi el doble. Conviene saberlo antes de planificar una visita al taller. También te contamos dónde quedan la ITV y el servicio oficial.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 54.8},
    "secciones": [
        {"id": "rodeo", "h2": "28,7 km en línea recta, 54,8 por carretera",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 de Alcobendas sale por la N-320, que pasa a 1,3 km del centro, baja a la R-2 y entra por la M-50. El trayecto no va directo: rodea y suma 54,8 km.",
             "El vehículo de cortesía y la recogida se ofrecen dentro del área metropolitana de Madrid, sujetos a disponibilidad: pregunta al reservar si Valdeavero entra.",
         ]},
        {"id": "alcala", "h2": "ITV y servicio oficial, en Alcalá de Henares",
         "parrafos": [
             "La estación oficial más cercana por carretera es ITVERSIA (estación 2891), en la Vía Complutense 105 de Alcalá de Henares, a 19,7 km. Para el servicio oficial, AutoPremier tiene dos puntos en el localizador de bmw.es casi a la misma distancia: el del Paseo de la Estación 23 de Guadalajara, a 19,2 km, y el de la Vía Complutense 131 de Alcalá, a 19,4.",
             "Están a una distancia parecida, así que puedes hacer la inspección y una gestión en el concesionario en la misma mañana.",
         ]},
        {"id": "valdeavero-crece", "h2": "De 1.451 a 1.896 habitantes",
         "parrafos": [
             "Valdeavero tenía 1.451 vecinos en 2015 y 1.896 en 2025, según el padrón: un 30,7 % más. La Comunidad de Madrid, a partir de la DGT, registraba 1.233 turismos en 2025, 650 por cada 1.000 habitantes, en un término de 18,6 km² a 722 metros de altitud.",
             "En un pueblo así, el coche hace muchos trayectos cortos hasta los municipios de alrededor. Si es diésel, conviene que de vez en cuando haga un tramo largo de autovía para que el filtro de partículas complete la regeneración.",
         ]},
    ],
    "faq": [
        {"q": "¿Por qué hay tanta diferencia entre línea recta y carretera?",
         "a": "Porque la ruta baja por la N-320 hasta la R-2 y la M-50 en lugar de ir directa: 54,8 km frente a 28,7 en línea recta."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es ITVERSIA, en la Vía Complutense 105 de Alcalá de Henares, a 19,7 km."},
        {"q": "¿Dónde está el servicio oficial BMW?",
         "a": "AutoPremier, en Guadalajara (19,2 km) o en la Vía Complutense de Alcalá (19,4 km)."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. Comparte electrónica y motores con BMW y se diagnostica con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.896 habitantes (+30,7 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "1.233 · 650 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "ITVERSIA, Alcalá de Henares · 19,7 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Guadalajara · 19,2 km (Alcalá, 19,4)", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 54,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["valdeavero"] = "BMW en Valdeavero: ITV en Alcalá de Henares, servicio oficial en Alcalá o Guadalajara y taller especialista de la red en Alcobendas, a 54,8 km por la R-2."
