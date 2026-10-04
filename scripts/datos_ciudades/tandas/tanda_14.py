# Tanda 14: Badalona, Parla, Mataró, Reus, Rivas-Vaciamadrid, Las Rozas de Madrid,
# San Sebastián de los Reyes, Cornellà de Llobregat, Pozuelo de Alarcón, Valdemoro,
# Majadahonda, Vilanova i la Geltrú, Castelldefels y Viladecans.
#
# Saltada: vilaseca (núcleo de población de Orís, tipo ≠ municipio; el coordinador
# pide no escribir barrios ni núcleos hasta que Martin decida).
#
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_14
# Las 14 ciudades tienen impresiones en GSC (paso_gsc.json): no se tocan ni
# metaTitle ni metaDescription. META y TITLES quedan vacíos a propósito; el
# script (python3 scripts/datos_ciudades/tandas/tanda_14.py) no hace nada.
#
# Majadahonda: 190.185 turismos para 73.625 vecinos (2.583 por 1.000): flotas
# domiciliadas. No se usa la cifra en el texto.
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

# ---------------------------------------------------------------- Badalona
CIUDADES["badalona"] = {
    "h1": "BMW en Badalona: el servicio oficial en Sant Adrià y el especialista independiente a 24,5 km",
    "entradilla": "Con el servicio oficial BMW a 5,1 km y una ITV en el carrer de la Indústria, a quien vive en Badalona le sobran opciones cerca. Nosotros somos otra: un taller independiente dedicado a BMW y MINI, al otro lado de Barcelona, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 24.5},
    "secciones": [
        {"id": "no-somos-el-concesionario", "h2": "Si buscabas el taller de la marca, está en Sant Adrià de Besòs",
         "parrafos": [
             "El localizador de bmw.es da como punto oficial más próximo al centro de Badalona el de Barcelona Premium junto a la Ronda Litoral, en la calle Juan de Austria 1 de Sant Adrià de Besòs: 5,1 km por carretera. Si tu coche tiene una avería que cubre la garantía de fábrica, esa es la puerta a la que llamar.",
             "Dasercars no forma parte de la red de la marca y no lo aparenta. Lo que ofrecemos es especialización: diésel N47, N57 y B47, electrónica de a bordo, cajas automáticas, mantenimiento según el indicador de servicio. Y el teléfono de esta página es el nuestro, no el del concesionario."
         ]},
        {"id": "ronda-litoral", "h2": "Por la C-31 y la Ronda Litoral hasta el Baix Llobregat",
         "parrafos": [
             "Entre el centro de Badalona y la nave del carrer del Tambor del Bruc hay 24,5 km por carretera y 18 en línea recta. El trazado más corto sale a la C-31, sigue la B-10 bordeando el litoral de Barcelona y entra en la B-20 hacia Sant Joan Despí.",
             "Los dos municipios están en el Área Metropolitana de Barcelona, así que existe la opción de no hacer el viaje: el taller recoge y devuelve el coche dentro del área metropolitana, y para reparaciones largas tiene vehículo de cortesía. Ambas cosas dependen de disponibilidad, de modo que se piden al cerrar la cita."
         ]},
        {"id": "itv-industria", "h2": "La ITV de Badalona, en el carrer de la Indústria",
         "parrafos": [
             "La estación B02 del registro de la Generalitat, operada por Applus, está en el carrer de la Indústria 427-449, dentro del término. Si al coche le toca inspección y además arrastra un aviso en el cuadro, merece la pena resolver primero el aviso: un testigo de airbag o de motor encendido puede acabar en defecto en la inspección."
         ]},
        {"id": "ciudad-junto-al-mar", "h2": "Ciudad densa y a 1,7 km del mar",
         "parrafos": [
             "Badalona reúne 231.542 vecinos (padrón de 2025) en 21,18 km²: unos 10.932 por kilómetro cuadrado. Idescat, con datos de la DGT, contaba 77.081 turismos en 2024, 333 por cada 1.000 habitantes; más que los 281 de Barcelona, pero lejos de lo que se ve en el interior.",
             "El centro está a 1,7 km de la línea de costa. Para un coche que duerme en la calle cerca del paseo marítimo, la humedad salina se nota en los bajos, en los anclajes del escape y en los discos de freno de un coche que pasa días sin moverse. Y con la N-II atravesando la ciudad y la C-31 a medio kilómetro, también es fácil sacar un diésel a carretera para que el filtro de partículas complete la regeneración."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Badalona?",
         "a": "No. El servicio oficial más próximo según bmw.es es Barcelona Premium, en la calle Juan de Austria 1 de Sant Adrià de Besòs. Dasercars es un taller independiente en Sant Joan Despí."},
        {"q": "¿Podéis pasar a buscar el coche a Badalona?",
         "a": "Badalona está dentro del área metropolitana, que es donde funciona la recogida y entrega del taller, sujeta a disponibilidad."},
        {"q": "¿Dónde está la ITV de Badalona?",
         "a": "En el carrer de la Indústria 427-449: es la estación B02 del registro de la Generalitat."},
        {"q": "¿Atendéis también MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "231.542 habitantes (+7,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Barcelonès", **F.idescat("080155")},
        {"etiqueta": "Turismos (2024)", "valor": "77.081 · 333 por cada 1.000 hab.", **F.idescat("080155")},
        {"etiqueta": "ITV en el municipio", "valor": "Badalona (B02), c. de la Indústria 427-449", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Adrià de Besòs) · 5,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 24,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080155"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Parla
CIUDADES["parla"] = {
    "h1": "Parla: dos ITV en el municipio, servicio oficial BMW en Getafe y especialista en Alcobendas",
    "entradilla": "De Parla al taller de Alcobendas hay que atravesar Madrid de sur a norte: 41,8 km. Antes de decidir si compensa, esto es lo que tienes a mano en el propio municipio y en Getafe.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 41.8},
    "secciones": [
        {"id": "dos-estaciones", "h2": "Calle Roma o polígono industrial: las dos ITV de Parla",
         "parrafos": [
             "El listado de la Comunidad de Madrid recoge dos estaciones dentro del término: la de DEKRA (estación 2897), en la calle Roma 9, y la de TÜV Rheinland (estación 2841), en la calle Berlín 1 del polígono industrial de Parla. Con dos estaciones tan cerca, la inspección no tiene por qué coincidir con el viaje al taller."
         ]},
        {"id": "vehinter-getafe", "h2": "Lo oficial queda en Getafe, a 7,1 km",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial más cercano es Vehinter, en la carretera de Madrid a Toledo, en Getafe: 7,1 km por carretera. Para una avería cubierta por la garantía de fábrica, es la opción lógica por cercanía.",
             "La alternativa independiente somos nosotros, y la diferencia de distancia es grande. Por eso conviene saber antes de mover el coche qué se va a hacer y cuánto va a costar: el presupuesto llega por escrito y el taller no toca nada hasta que lo apruebas."
         ]},
        {"id": "a42-a1", "h2": "41,8 kilómetros por la A-42, la M-40, la M-30 y la A-1",
         "parrafos": [
             "La ruta más corta desde el centro de Parla sale por la A-42 hacia Madrid, toma la M-40, cruza por la M-30 y sube por la A-1 hasta la calle Valgrande de Alcobendas. En línea recta son 34,9 km.",
             "Parla está en la corona sur del área metropolitana. El taller ofrece recogida y entrega y vehículo de cortesía dentro de esa área, siempre sujetos a disponibilidad; al pedir cita, confirma si tu dirección entra."
         ]},
        {"id": "parla-crece", "h2": "137.471 vecinos y 55.377 turismos",
         "parrafos": [
             "El padrón de 2025 da a Parla 137.471 habitantes, un 9,9 % más que los 125.056 de 2015, en un término de 24,9 km²: unos 5.521 vecinos por kilómetro cuadrado. La Comunidad de Madrid, con datos de la DGT, contaba 55.377 turismos en 2025: 403 por cada 1.000 habitantes, una proporción parecida a la de Madrid capital (388).",
             "La A-42 y la R-4 pasan a menos de tres kilómetros del centro. Si tu BMW con caja automática hace a diario el atasco de entrada a Madrid, ese uso de parar y arrancar castiga la caja más que la autovía libre: conviene no olvidar su aceite en el plan de mantenimiento."
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV hay en Parla?",
         "a": "Dos: DEKRA, en la calle Roma 9, y TÜV Rheinland, en la calle Berlín 1 del polígono industrial, según la Comunidad de Madrid."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Parla?",
         "a": "Vehinter, en la carretera de Madrid a Toledo (Getafe), a 7,1 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "41,8 km por carretera hasta la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Tenéis taller en Madrid capital o en el sur?",
         "a": "No. El taller de Madrid de la red es el de Alcobendas, al norte; desde Parla no hay otro más próximo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "137.471 habitantes (+9,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "55.377 · 403 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "2 estaciones (c. Roma 9 y c. Berlín 1)", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 7,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 41,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Mataró
CIUDADES["mataro"] = {
    "h1": "Taller BMW y Mataró: Pruna Motor en Via Sergia o el especialista independiente a 42 km",
    "entradilla": "Quien escribe «BMW Mataró taller» suele buscar el concesionario de Via Sergia. Te lo situamos, y te contamos también qué ofrece un especialista independiente a 42,3 km y dónde pasa la ITV un coche de la capital del Maresme.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 42.3},
    "secciones": [
        {"id": "pruna-via-sergia", "h2": "Pruna Motor, en Via Sergia 2",
         "parrafos": [
             "El servicio oficial BMW de la ciudad, según el localizador de bmw.es, es Pruna Motor, en Via Sergia 2, a 3,1 km del centro. Si lo que necesitas es una reparación en garantía de fábrica o una campaña que te haya comunicado BMW, la tienes ahí.",
             "Para el resto —revisiones, frenos, distribución, diagnosis de un fallo que va y viene— puedes elegir taller. El Reglamento (UE) 461/2010 impide que la marca condicione la garantía a revisar el coche en su red, con una condición: que se cumplan los intervalos y las especificaciones de su plan."
         ]},
        {"id": "c32-maresme", "h2": "Por la C-32 hasta Sant Joan Despí",
         "parrafos": [
             "Desde el centro de Mataró se llega a la nave de Dasercars Barcelona por la C-31D, la autopista C-32 del Maresme y la B-20: 42,3 km por carretera, 37,3 en línea recta. Mataró no está en el Área Metropolitana de Barcelona y la recogida del taller no cubre la ciudad, así que el coche lo llevas tú.",
             "Con esa distancia, tiene sentido para trabajos que piden a alguien que trabaje BMW todos los días; para un cambio de pastillas, no hace falta salir del Maresme.",
             "Salir de la ciudad es fácil: la C-32, la N-II, la C-60 y la C-31D pasan a menos de tres kilómetros del centro, así que el viaje hasta el Baix Llobregat es casi entero por autopista."
         ]},
        {"id": "itv-el-cros", "h2": "La ITV, en el polígono El Cros de Argentona",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 3,2 km del centro de Mataró."
         ]},
        {"id": "salitre-maresme", "h2": "Una ciudad a 0,9 km del mar",
         "parrafos": [
             "El centro de Mataró queda a 0,9 km de la costa. A esa distancia el ambiente salino trabaja sin prisa sobre los bajos, las grapas del escape y los conectores eléctricos expuestos. Un aclarado de bajos con agua dulce al final del verano y mirar los conectores cuando aparece un aviso eléctrico intermitente son dos costumbres baratas.",
             "La ciudad tenía 131.683 habitantes en 2025, un 5,5 % más que en 2015, y 52.397 turismos en 2024 según Idescat a partir de la DGT: 398 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Sois Pruna Motor?",
         "a": "No. Pruna Motor es el servicio oficial BMW de Mataró, en Via Sergia 2. Dasercars es un taller independiente con nave en Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV si vivo en Mataró?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 3,2 km."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI y BMW comparten motores y electrónica, y se diagnostican con el mismo equipo."},
        {"q": "¿Recogéis coches en Mataró?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona, y Mataró queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "131.683 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("081213")},
        {"etiqueta": "Turismos (2024)", "valor": "52.397 · 398 por cada 1.000 hab.", **F.idescat("081213")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Via Sergia 2 · 3,1 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 3,2 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 42,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081213"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Reus
CIUDADES["reus"] = {
    "h1": "Reus y tu BMW: diagnosis, servicio oficial en Tarragona y un especialista a 99 km",
    "entradilla": "Nuestro taller más próximo a Reus está a 99,2 km, en Sant Joan Despí. Es mucha distancia, y conviene decirlo antes que nada. Lo que sí podemos darte es una idea clara de qué tienes en el Baix Camp y cuándo merece la pena el viaje.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 99.2},
    "secciones": [
        {"id": "en-el-camp", "h2": "Lo que tienes en Reus y en Tarragona",
         "parrafos": [
             "La ITV la tienes en casa: la estación de Reus (T02) del registro de la Generalitat, gestionada por Applus, está en la carretera de València a Tarragona, dentro del término. El servicio oficial BMW más cercano según bmw.es es Oliva Motor, en el carrer Josep Maria Folch i Torres 2 de Tarragona, a 10,3 km.",
             "Con eso cerca, para la inspección o una revisión de rutina no tiene sentido hacer cien kilómetros."
         ]},
        {"id": "diagnosis-electronica", "h2": "Diagnosis electrónica: qué es y cómo se presupuesta",
         "parrafos": [
             "Leer los códigos de avería es la parte fácil. Diagnosticar es interpretar esos códigos con los valores reales que dan los sensores mientras el motor trabaja, descartar causas y localizar la pieza o el cable que falla. En un BMW, con decenas de centralitas conectadas entre sí, un fallo en una puede encender avisos en otras.",
             "Por eso en Dasercars la diagnosis se presupuesta como un trabajo más, antes de empezar, y el resultado se explica: qué falla, por qué y qué cuesta repararlo. Ninguna reparación arranca sin que la hayas aceptado."
         ]},
        {"id": "cuando-viajar", "h2": "Cuándo sí compensa subir por la AP-7",
         "parrafos": [
             "Desde el centro de Reus, la ruta sale por la N-420a, toma la AP-7 y la C-32 y entra por la B-25 hasta el carrer del Tambor del Bruc: 99,2 km por carretera, 83,3 en línea recta. No hay recogida: el servicio del taller no llega fuera del área metropolitana.",
             "Compensa para lo que no se ha resuelto cerca: un aviso que reaparece tras varias visitas, un fallo de inyección o de turbo en un diésel N47 o N57, un problema de la caja automática. Antes, una llamada con modelo, año, kilómetros y el síntoma permite saber si el viaje tiene sentido."
         ]},
        {"id": "reus-en-cifras", "h2": "111.601 habitantes y 50.998 turismos",
         "parrafos": [
             "Reus, capital del Baix Camp, tenía 111.601 vecinos en 2025, un 8,1 % más que en 2015. Idescat, con datos de la DGT, contaba 50.998 turismos en 2024: 457 por cada 1.000 habitantes.",
             "El término mide 52,82 km² y está a solo 117 metros de altitud y a 9,5 km de la costa: ni frío de montaña ni salitre de primera línea. Aquí lo que más castiga a un coche es el calor del verano, que acelera el envejecimiento de la batería y de los manguitos del circuito de refrigeración."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Reus?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 99,2 km por carretera."},
        {"q": "¿Dónde está la ITV de Reus?",
         "a": "En la carretera de València a Tarragona, dentro del municipio: es la estación T02 de la Generalitat."},
        {"q": "¿Cobráis la diagnosis?",
         "a": "Sí, se presupuesta antes de conectar el equipo, igual que cualquier otro trabajo."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Oliva Motor, en Tarragona, a 10,3 km según el localizador de bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "111.601 habitantes (+8,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Camp", **F.idescat("431233")},
        {"etiqueta": "Turismos (2024)", "valor": "50.998 · 457 por cada 1.000 hab.", **F.idescat("431233")},
        {"etiqueta": "ITV en el municipio", "valor": "Reus (T02)", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Oliva Motor (Tarragona) · 10,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 99,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("431233"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Rivas-Vaciamadrid
CIUDADES["rivas-vaciamadrid"] = {
    "h1": "Rivas-Vaciamadrid: averías eléctricas de BMW y un taller independiente a 34 km",
    "entradilla": "Rivas ha ganado más de 21.000 vecinos en diez años y ya pasa de 100.000. Si tienes un BMW o un MINI aquí, te contamos qué es un taller autorizado y qué no, dónde están tus dos ITV y cómo se llega a Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 34.0},
    "secciones": [
        {"id": "autorizado-o-independiente", "h2": "Taller autorizado BMW y taller independiente no son lo mismo",
         "parrafos": [
             "Un taller autorizado forma parte de la red de BMW. El más próximo a Rivas por carretera, según bmw.es, es AutoPremier, en la carretera de Valencia, km 7,3, ya en Madrid: 13,5 km. Dasercars no es autorizado; es un taller independiente que solo trabaja BMW y MINI.",
             "En la práctica, lo que cubre la garantía de fábrica pasa por la red de la marca. El mantenimiento y las reparaciones fuera de garantía, por el taller que elijas."
         ]},
        {"id": "averias-electricas", "h2": "Cuando el fallo es eléctrico",
         "parrafos": [
             "Un BMW actual reparte sus funciones entre decenas de centralitas que hablan por el mismo bus. Una tensión de batería baja, un conector con humedad o un módulo que se reinicia pueden encender avisos que no tienen que ver con la avería real. Por eso cambiar piezas por intuición sale caro.",
             "El trabajo empieza por la batería —en los BMW, además, una batería nueva se registra en la centralita— y sigue por medir, no por sustituir. Si la avería ya ha pasado por otro taller, trae lo que te hayan dicho y lo que se ha cambiado: ahorra horas de diagnosis."
         ]},
        {"id": "itv-rivas", "h2": "Dos estaciones de ITV dentro del municipio",
         "parrafos": [
             "La Comunidad de Madrid lista dos estaciones en Rivas: ITV Rivas (estación 2869), en la calle Cincel 2 bis del polígono Santa Ana, y TÜV Rheinland (estación 2848), en la calle Mariano Barbacid 8."
         ]},
        {"id": "a3-m30-a1", "h2": "Por la A-3, la M-30 y la A-1",
         "parrafos": [
             "Desde el centro de Rivas hasta la calle Valgrande de Alcobendas hay 34 km por carretera (26,3 en línea recta): A-3 hacia Madrid, M-30 y A-1. Rivas está en el área metropolitana de Madrid, donde el taller ofrece recogida y entrega y coche de cortesía, ambos sujetos a disponibilidad.",
             "Según la Comunidad de Madrid, en 2025 había 52.643 turismos en el municipio, 510 por cada 1.000 habitantes; en Madrid capital son 388. La población ha pasado de 81.473 en 2015 a 103.148 en 2025, un 26,6 % más."
         ]},
    ],
    "faq": [
        {"q": "¿Sois taller autorizado BMW?",
         "a": "No. Somos un taller independiente especializado en BMW y MINI, en Alcobendas. El punto oficial más cercano a Rivas es AutoPremier, en la carretera de Valencia, km 7,3."},
        {"q": "¿Dónde paso la ITV en Rivas?",
         "a": "En la calle Cincel 2 bis (polígono Santa Ana) o en la calle Mariano Barbacid 8, según la Comunidad de Madrid."},
        {"q": "¿Recogéis el coche en Rivas?",
         "a": "Rivas está en el área metropolitana de Madrid; la recogida existe y depende de disponibilidad."},
        {"q": "¿Por dónde se llega al taller desde Rivas?",
         "a": "Por la A-3 hacia Madrid, la M-30 y la A-1: 34 km hasta la calle Valgrande 17 de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "103.148 habitantes (+26,6 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "52.643 · 510 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "2 estaciones", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, ctra. de Valencia km 7,3 · 13,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 34 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Las Rozas de Madrid
CIUDADES["las-rozas-de-madrid"] = {
    "h1": "Concesionario o taller BMW en Las Rozas: Movilnorte a 4,7 km, Dasercars a 27,5 km",
    "entradilla": "Casi todo el que llega aquí desde Las Rozas busca el concesionario. No lo somos, y preferimos dejarlo claro arriba: te indicamos dónde está el punto oficial más próximo y qué ofrece un taller independiente de BMW en Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 27.5},
    "secciones": [
        {"id": "movilnorte-el-plantio", "h2": "El servicio oficial más próximo: Movilnorte, en El Plantío",
         "parrafos": [
             "En el localizador de bmw.es, el punto de servicio oficial más cercano al centro de Las Rozas es Movilnorte, en la carretera de El Plantío 62, ya en Majadahonda: 4,7 km por carretera. Su horario y sus citas los gestiona Movilnorte; el teléfono de esta página no es el suyo.",
             "Dasercars es un taller independiente. Te puede interesar si quieres contrastar un presupuesto, un especialista en los diésel de BMW o mantener el coche fuera de la red sin perder la garantía: el Reglamento (UE) 461/2010 lo permite mientras se respeten intervalos y especificaciones del plan."
         ]},
        {"id": "a6-m40", "h2": "27,5 km por la A-6, la M-40 y la A-1",
         "parrafos": [
             "Desde el centro de Las Rozas hasta la calle Valgrande de Alcobendas se va por la A-6, se rodea Madrid por la M-40 y se sube por la A-1: 27,5 km por carretera, 19,5 en línea recta.",
             "Al estar en el área metropolitana de Madrid, el municipio entra en la zona de recogida y entrega del taller y de vehículo de cortesía, siempre según disponibilidad."
         ]},
        {"id": "solo-bmw-y-mini", "h2": "Mecánica y electrónica, pero solo de BMW y MINI",
         "parrafos": [
             "También llega gente de Las Rozas buscando un taller de electrónica o de mecánica general. Conviene saberlo antes de llamar: Dasercars trabaja únicamente BMW y MINI. Si tu coche es de otra marca, te ahorramos el viaje.",
             "Si es un BMW, la electrónica es precisamente donde más se nota la especialización: un fallo de una centralita puede encender avisos en otras, y localizar el origen pide conocer cómo se comunican entre sí en cada serie."
         ]},
        {"id": "itv-las-rozas", "h2": "Dos ITV: en la A-6 y en Európolis",
         "parrafos": [
             "La Comunidad de Madrid sitúa dos estaciones en el término: la de ITEVELESA (estación 2831), en la A-6, km 20,4, y la de TÜV SÜD ATISAE (estación 2816), en la calle Cabo Rufino Lázaro 14D del polígono Európolis."
         ]},
        {"id": "las-rozas-coches", "h2": "543 turismos por cada mil vecinos",
         "parrafos": [
             "Las Rozas tenía 99.037 habitantes en el padrón de 2025, un 5,9 % más que en 2015, y 53.807 turismos censados en 2025 según la Comunidad de Madrid a partir de la DGT: 543 por cada 1.000 habitantes, bastante por encima de los 388 de Madrid capital.",
             "Con el centro urbano a unos 716 metros de altitud, el frío de enero castiga las baterías de los coches que duermen fuera, sobre todo en BMW con arranque y parada automático."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Las Rozas?",
         "a": "No. El punto oficial más próximo según bmw.es es Movilnorte, en la carretera de El Plantío 62 (Majadahonda). Nosotros somos Dasercars, taller independiente en Alcobendas."},
        {"q": "¿Dónde paso la ITV en Las Rozas?",
         "a": "En la A-6, km 20,4 (ITEVELESA) o en el polígono Európolis (TÜV SÜD ATISAE)."},
        {"q": "¿Reparáis averías electrónicas?",
         "a": "Sí, en BMW y MINI. La diagnosis se presupuesta antes de empezar y después se explica qué falla y por qué."},
        {"q": "¿Trabajáis otras marcas?",
         "a": "No. El taller está dedicado a BMW y MINI."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "99.037 habitantes (+5,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "53.807 · 543 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "2 estaciones (A-6 km 20,4 y Európolis)", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Majadahonda) · 4,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 27,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- San Sebastián de los Reyes
CIUDADES["san-sebastian-de-los-reyes"] = {
    "h1": "San Sebastián de los Reyes: el taller BMW está en Alcobendas, a 4,5 km",
    "entradilla": "Pocas ciudades de la red tienen el taller tan cerca. El centro de Alcobendas está a 1,5 km en línea recta, y la nave de Dasercars Madrid, a 4,5 km por carretera desde el centro de San Sebastián de los Reyes.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 4.5},
    "secciones": [
        {"id": "al-lado", "h2": "A 4,5 km: entrar por la mañana, salir por la tarde",
         "parrafos": [
             "Entre el centro de Sanse y la calle Valgrande 17 de Alcobendas hay 4,5 km por carretera y 2,9 en línea recta. Con esa distancia, lo más cómodo suele ser dejar el coche por la mañana y recogerlo por la tarde: el taller abre de lunes a viernes de 9:00 a 14:00 y de 15:00 a 18:00.",
             "Si la reparación va a durar días, pregunta por el vehículo de cortesía al reservar. Igual que la recogida y entrega dentro del área metropolitana, está sujeto a disponibilidad."
         ]},
        {"id": "dos-itv-sanse", "h2": "Una ITV junto a la A-1 y otra en Plaza Norte",
         "parrafos": [
             "La Comunidad de Madrid recoge dos estaciones en el municipio: INTECTRA (estación 2821), en la A-1, km 23, en el desvío de Algete, y TÜV Rheinland (estación 2850), en la avenida Fuente Nueva 7, en el centro comercial Plaza Norte.",
             "Con el taller y las dos estaciones en un radio tan corto, se puede hacer la pre-ITV un día y pasar la inspección al siguiente sin apenas mover el coche."
         ]},
        {"id": "las-tablas", "h2": "El servicio oficial, en Las Tablas",
         "parrafos": [
             "El punto oficial BMW más cercano por carretera, según bmw.es, es BYmyCAR Madrid, en la avenida de Burgos 133 (Las Tablas), a 8,9 km. Si lo que tienes es una avería en garantía, ese es el sitio; para el mantenimiento y lo que ya no cubre BMW, la elección es tuya."
         ]},
        {"id": "sanse-en-cifras", "h2": "Un 14,2 % más de vecinos que hace diez años",
         "parrafos": [
             "San Sebastián de los Reyes ha pasado de 84.944 habitantes en 2015 a 96.992 en 2025. La Comunidad de Madrid, con datos de la DGT, contaba 46.458 turismos en 2025: 479 por cada 1.000 habitantes. A menos de tres kilómetros del centro pasan la A-1, la N-I, la M-12, la M-603 y la M-616."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en San Sebastián de los Reyes?",
         "a": "No dentro del municipio: está en la calle Valgrande 17 de Alcobendas, a 4,5 km del centro de Sanse."},
        {"q": "¿Qué ITV me queda más a mano?",
         "a": "Hay dos en el municipio: INTECTRA, en la A-1 km 23, y TÜV Rheinland, en la avenida Fuente Nueva 7."},
        {"q": "¿Tenéis coche de cortesía?",
         "a": "Sí, para trabajos largos y sujeto a disponibilidad. Pídelo al reservar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "96.992 habitantes (+14,2 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "46.458 · 479 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "2 estaciones (A-1 km 23 y Plaza Norte)", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid (Las Tablas) · 8,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 4,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Cornellà de Llobregat
CIUDADES["cornella-de-llobregat"] = {
    "h1": "Cornellà de Llobregat: taller especialista BMW a 1,5 km, en Sant Joan Despí",
    "entradilla": "Desde el casco urbano de Cornellà, la nave de Dasercars Barcelona está a 1,5 km. Es la distancia más corta de toda la red, y cambia la forma de usar el taller.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 1.5},
    "secciones": [
        {"id": "kilometro-y-medio", "h2": "Kilómetro y medio hasta el Tambor del Bruc",
         "parrafos": [
             "El carrer del Tambor del Bruc 3 de Sant Joan Despí queda a 1,5 km por carretera del centro del núcleo urbano de Cornellà, 1,3 en línea recta. Se puede dejar el coche al abrir, a las 9:00, y pasar a recogerlo antes de las 18:00, de lunes a viernes.",
             "Cornellà forma parte del Área Metropolitana de Barcelona, así que también hay recogida y entrega y vehículo de cortesía, sujetos a disponibilidad. A esta distancia es más útil el coche de cortesía, para trabajos de varios días, que la recogida."
         ]},
        {"id": "itv-campsa", "h2": "La ITV, en el passeig de la Campsa",
         "parrafos": [
             "El registro de la Generalitat sitúa una estación dentro del municipio: Cornellà (B11), de Applus, en el passeig de la Campsa 64. Taller e inspección quedan tan cerca que la pre-ITV y la cita en la estación caben en la misma semana sin planificar nada."
         ]},
        {"id": "nudo-de-autopistas", "h2": "Doce carreteras a menos de tres kilómetros",
         "parrafos": [
             "En un término de 6,99 km² se cruzan la A-2, la B-10, la B-20, la B-23, la B-25, la C-32, la C-245 o la N-340, entre otras. Para un diésel que se mueve poco por ciudad, eso es una ventaja: tiene a mano un tramo de autopista para completar la regeneración del filtro de partículas.",
             "Cornellà tenía 92.237 habitantes en 2025 y 29.985 turismos en 2024 según Idescat: 325 por cada 1.000 vecinos."
         ]},
        {"id": "oficial-sant-boi", "h2": "El servicio oficial, en Sant Boi",
         "parrafos": [
             "Según bmw.es, el punto oficial más cercano es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 4,9 km. Es donde se tramitan las garantías de fábrica."
         ]},
    ],
    "faq": [
        {"q": "¿A qué distancia está el taller de Cornellà?",
         "a": "A 1,5 km por carretera, en el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
        {"q": "¿Dónde está la ITV de Cornellà?",
         "a": "En el passeig de la Campsa 64: es la estación B11 del registro de la Generalitat."},
        {"q": "¿Trabajáis BMW M y cajas automáticas?",
         "a": "Sí. Pide cita con el modelo y el síntoma y se prepara el diagnóstico antes de que llegue el coche."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "92.237 habitantes (+6,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080734")},
        {"etiqueta": "Turismos (2024)", "valor": "29.985 · 325 por cada 1.000 hab.", **F.idescat("080734")},
        {"etiqueta": "ITV en el municipio", "valor": "Cornellà (B11), pg. de la Campsa 64", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 4,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 1,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080734"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Pozuelo de Alarcón
CIUDADES["pozuelo-de-alarcon"] = {
    "h1": "BMW en Pozuelo de Alarcón: ITV en la calle Virgilio y especialista a 24,7 km por la M-40",
    "entradilla": "Pozuelo tiene la ITV dentro del municipio y el servicio oficial BMW más próximo en Majadahonda. El taller especialista que atiende la zona está en Alcobendas, a 24,7 km por la M-40 y la A-1.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 24.7},
    "secciones": [
        {"id": "m40-hacia-el-norte", "h2": "Por la M-40 hasta Alcobendas",
         "parrafos": [
             "La ruta más corta desde el centro de Pozuelo enlaza con la M-40, rodea Madrid por el oeste y el norte y sale a la A-1 hasta la calle Valgrande: 24,7 km por carretera, 18 en línea recta.",
             "Pozuelo está en el área metropolitana de Madrid. El taller ofrece recogida y entrega y vehículo de cortesía en esa zona, siempre que haya disponibilidad; para trabajos de más de un día es lo que más se agradece."
         ]},
        {"id": "movilnorte-por-carretera", "h2": "Movilnorte: 5,6 km en el mapa, 11,4 por carretera",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo es Movilnorte, en la carretera de El Plantío 62 de Majadahonda. En línea recta está a 5,6 km, pero por carretera la ruta más corta da 11,4. Para una reparación en garantía, la cita es allí.",
             "Lo que no entra en garantía —desgaste, averías posteriores, mantenimiento por plan— puedes hacerlo donde quieras. Si eliges un especialista, pide que te expliquen el diagnóstico antes de reparar."
         ]},
        {"id": "itv-virgilio", "h2": "La ITV de Pozuelo",
         "parrafos": [
             "El listado de la Comunidad de Madrid incluye una estación en el municipio: INTECTRA (estación 2823), en la calle Virgilio 8."
         ]},
        {"id": "pozuelo-en-cifras", "h2": "566 turismos por cada mil habitantes",
         "parrafos": [
             "Pozuelo tenía 89.770 vecinos en 2025, un 6,2 % más que diez años antes, y 50.841 turismos censados ese año según la Comunidad de Madrid a partir de la DGT. Son 566 por cada 1.000 habitantes, frente a 388 en Madrid capital.",
             "Un coche que solo hace trayectos cortos por el municipio es justo el uso que peor llevan la batería y el filtro de partículas de un diésel. Con la M-40 a menos de tres kilómetros del centro, una salida larga de vez en cuando lo compensa."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Pozuelo?",
         "a": "Movilnorte, en la carretera de El Plantío 62 (Majadahonda), a 11,4 km por carretera según bmw.es."},
        {"q": "¿Dónde paso la ITV en Pozuelo?",
         "a": "En INTECTRA, calle Virgilio 8, dentro del municipio."},
        {"q": "¿Recogéis el coche en Pozuelo?",
         "a": "Sí, dentro del área metropolitana de Madrid hay recogida y entrega, sujeta a disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "89.770 habitantes (+6,2 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "50.841 · 566 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "INTECTRA, c. Virgilio 8", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Majadahonda) · 11,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 24,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Valdemoro
CIUDADES["valdemoro"] = {
    "h1": "Valdemoro: servicio oficial BMW en Getafe y taller independiente en Alcobendas",
    "entradilla": "Si buscas el servicio oficial BMW más cercano a Valdemoro, está en Getafe. Nosotros somos un taller independiente, a 43,5 km por la A-4. Esta página separa una cosa de la otra.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 43.5},
    "secciones": [
        {"id": "vehinter-16-km", "h2": "La red de la marca, a 16 km",
         "parrafos": [
             "El localizador de bmw.es da como punto oficial más próximo a Valdemoro el de Vehinter, en la carretera de Madrid a Toledo, en Getafe: 16 km por carretera. Las campañas de revisión que convoca BMW se hacen en su red, y si tu coche tiene una, ese es el sitio.",
             "Dasercars no pertenece a esa red. Somos especialistas en BMW y MINI con taller propio en Alcobendas, y trabajamos lo que no depende de la garantía de fábrica: mantenimiento, diagnosis, reparaciones de motor, caja o electrónica."
         ]},
        {"id": "a4-hacia-el-norte", "h2": "De la A-4 a la A-1 cruzando Madrid",
         "parrafos": [
             "La ruta desde el centro de Valdemoro sube por la A-4, atraviesa por la M-30 y sale por la A-1: 43,5 km por carretera hasta la calle Valgrande, 38,6 en línea recta.",
             "El taller tiene recogida y entrega dentro del área metropolitana de Madrid, sujeta a disponibilidad; al pedir cita, confirma si tu dirección de Valdemoro entra."
         ]},
        {"id": "itv-las-canteras", "h2": "La ITV, en el polígono Las Canteras",
         "parrafos": [
             "La estación de ITV Valdemoro (2863 en el listado de la Comunidad de Madrid) está en la calle Vereda de la Solana 43-45, en el polígono industrial Las Canteras, dentro del municipio."
         ]},
        {"id": "valdemoro-crece", "h2": "Un 18 % más de habitantes desde 2015",
         "parrafos": [
             "Valdemoro tenía 72.854 vecinos en 2015 y 85.972 en 2025. En 2025 había 40.383 turismos censados, 470 por cada 1.000 habitantes según la Comunidad de Madrid a partir de la DGT. La A-4 y la R-4 pasan a menos de tres kilómetros del centro.",
             "Para un BMW que hace muchos kilómetros de autovía, el indicador de servicio marca bien los cambios de aceite; lo que se suele olvidar es lo que va por tiempo, como el líquido de frenos."
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Valdemoro?",
         "a": "Vehinter, en la carretera de Madrid a Toledo (Getafe), a 16 km según bmw.es."},
        {"q": "¿Sois servicio oficial?",
         "a": "No. Somos un taller independiente especializado en BMW y MINI, en Alcobendas."},
        {"q": "¿Dónde paso la ITV en Valdemoro?",
         "a": "En la calle Vereda de la Solana 43-45, polígono Las Canteras."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "85.972 habitantes (+18 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "40.383 · 470 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "ITV Valdemoro, polígono Las Canteras", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 16 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 43,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Majadahonda
CIUDADES["majadahonda"] = {
    "h1": "Taller BMW en Majadahonda: Movilnorte a 2,4 km o Dasercars a 27,5 km",
    "entradilla": "El concesionario BMW que buscas probablemente sea Movilnorte, en la carretera de El Plantío. Nosotros somos otra cosa: un taller independiente de BMW y MINI en Alcobendas. Aquí tienes las dos opciones con sus datos.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 27.5},
    "secciones": [
        {"id": "movilnorte", "h2": "Movilnorte, el servicio oficial dentro del municipio",
         "parrafos": [
             "Según el localizador de bmw.es, Movilnorte, en la carretera de El Plantío 62, es el punto oficial BMW más próximo: 2,4 km desde el centro de Majadahonda. Allí van las reparaciones en garantía de fábrica y las campañas del fabricante.",
             "Si has llegado aquí buscando su teléfono, no es este. El número de esta página es el de Dasercars Madrid."
         ]},
        {"id": "para-que-un-independiente", "h2": "Para qué sirve un especialista independiente",
         "parrafos": [
             "Para todo lo que no depende de BMW como fabricante: el mantenimiento que marca el indicador de servicio, los frenos, la distribución de un diésel N47 o N57, un turbo, una caja automática que da tirones o una avería eléctrica que no se ha localizado. También para contrastar un diagnóstico antes de aceptar una reparación cara.",
             "La diagnosis se presupuesta antes de conectar el equipo, y la reparación no empieza sin tu visto bueno."
         ]},
        {"id": "ruta-a6", "h2": "A-6, M-40 y A-1: 27,5 km",
         "parrafos": [
             "Desde el centro de Majadahonda, la ruta más corta a la calle Valgrande de Alcobendas va por la A-6, la M-40 y la A-1: 27,5 km por carretera y 20 en línea recta.",
             "Majadahonda está dentro del área metropolitana de Madrid, donde el taller ofrece recogida y entrega y coche de cortesía, ambos sujetos a disponibilidad.",
             "A menos de tres kilómetros del centro pasan la A-6, la M-50, la M-503, la M-505 y la M-509. Las Rozas, a 2,2 km en línea recta, comparte con Majadahonda el mismo punto oficial de referencia en el localizador: Movilnorte."
         ]},
        {"id": "itv-el-carralero", "h2": "La ITV, en El Carralero",
         "parrafos": [
             "La Comunidad de Madrid recoge una estación en el municipio: IDV Madrid (estación 2862), en la calle De la Fresa 12, en el polígono industrial El Carralero.",
             "Majadahonda tenía 73.625 habitantes en 2025, un 4 % más que en 2015, y su centro está a unos 741 metros de altitud: en invierno, la batería de un coche que duerme en la calle es lo primero que conviene revisar."
         ]},
    ],
    "faq": [
        {"q": "¿Sois Movilnorte?",
         "a": "No. Movilnorte es el servicio oficial BMW de la carretera de El Plantío 62. Dasercars es un taller independiente en Alcobendas."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 27,5 km por carretera desde el centro de Majadahonda, por la A-6, la M-40 y la A-1."},
        {"q": "¿Dónde paso la ITV en Majadahonda?",
         "a": "En la calle De la Fresa 12, polígono El Carralero, según la Comunidad de Madrid."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, comparte motores y electrónica con BMW."},
        {"q": "¿Podéis venir a por el coche a Majadahonda?",
         "a": "Majadahonda entra en el área metropolitana, donde hay recogida y entrega sujeta a disponibilidad. Pídela al reservar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "73.625 habitantes (+4 % desde 2015)", **F.ine},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 741 m", **F.copernicus},
        {"etiqueta": "ITV en el municipio", "valor": "IDV Madrid, polígono El Carralero", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte, ctra. de El Plantío 62 · 2,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 27,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Vilanova i la Geltrú
CIUDADES["vilanova-i-la-geltru"] = {
    "h1": "BMW en Vilanova i la Geltrú: Quadis en la ciudad, especialista independiente a 39 km",
    "entradilla": "La capital del Garraf tiene servicio oficial BMW e ITV propios, y el mar a menos de un kilómetro del centro. Nuestro taller está a 39,3 km, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 39.3},
    "secciones": [
        {"id": "quadis-eduard-toldra", "h2": "Quadis Munich, en la avinguda d'Eduard Toldrà",
         "parrafos": [
             "En el localizador de bmw.es, el punto oficial de la ciudad es Quadis Munich, en la avinguda d'Eduard Toldrà 69, a 2,1 km del centro. Es también el que el localizador da como más cercano a Vilafranca del Penedès y a El Vendrell.",
             "No somos ese taller. Dasercars es independiente y está especializado en BMW y MINI; por eso esta página explica cuándo encaja cada uno, en lugar de hacerse pasar por el concesionario."
         ]},
        {"id": "garraf-c32", "h2": "Por la C-31 y la C-32 hasta Sant Joan Despí",
         "parrafos": [
             "La ruta más corta desde el centro sale por la C-31, sigue por la C-32 y entra por la B-25: 39,3 km por carretera, 32,4 en línea recta. Vilanova no está en el Área Metropolitana de Barcelona; la recogida del taller no llega.",
             "Si el viaje es por una avería concreta, una llamada previa con el modelo, el año, los kilómetros y lo que hace el coche sirve para saber si hace falta bajar y para tener el recambio pedido."
         ]},
        {"id": "itv-ronda-europa", "h2": "La ITV de Vilanova, en la Ronda Europa",
         "parrafos": [
             "La estación de Vilanova (B17) del registro de la Generalitat, de Applus, está en la Ronda Europa, dentro del término municipal."
         ]},
        {"id": "aire-salino", "h2": "Novecientos metros de mar",
         "parrafos": [
             "El centro de Vilanova queda a 0,9 km de la costa. En coches que viven junto al mar, los primeros síntomas del salitre suelen ser óxido en los discos tras unos días parado, grapas del escape que se pican y conectores que dan fallos intermitentes. Nada es urgente, pero sí conviene revisarlo cada año.",
             "La ciudad tenía 71.641 vecinos en 2025, un 9,1 % más que en 2015, y 29.954 turismos en 2024 según Idescat a partir de la DGT: 418 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Sois Quadis Munich Vilanova?",
         "a": "No. Quadis Munich es el servicio oficial BMW de la avinguda d'Eduard Toldrà 69. Nosotros somos Dasercars, taller independiente en Sant Joan Despí."},
        {"q": "¿Dónde está la ITV de Vilanova i la Geltrú?",
         "a": "En la Ronda Europa: es la estación B17 del registro de la Generalitat."},
        {"q": "¿Recogéis el coche en Vilanova?",
         "a": "No: la recogida del taller no llega fuera del área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "71.641 habitantes (+9,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Garraf", **F.idescat("083073")},
        {"etiqueta": "Turismos (2024)", "valor": "29.954 · 418 por cada 1.000 hab.", **F.idescat("083073")},
        {"etiqueta": "ITV en el municipio", "valor": "Vilanova (B17), Ronda Europa", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, av. d'Eduard Toldrà 69 · 2,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 39,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("083073"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Castelldefels
CIUDADES["castelldefels"] = {
    "h1": "Castelldefels: tu BMW junto a la playa y el taller especialista a 15,9 km por la C-32",
    "entradilla": "A 1,8 km del mar y dentro del área metropolitana, Castelldefels tiene el taller especialista de la red a 15,9 km. Lo que conviene saber sobre ruta, recogida, ITV y salitre.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 15.9},
    "secciones": [
        {"id": "playa-y-coche", "h2": "Lo que el aire de playa le hace a un coche",
         "parrafos": [
             "El centro de Castelldefels queda a 1,8 km de la costa, y buena parte del municipio vive todavía más cerca de la arena. El salitre no rompe nada de golpe: corroe poco a poco los bajos y los soportes, cubre de óxido los discos si el coche pasa la semana aparcado y sulfata los conectores que no están bien sellados.",
             "En un BMW, ese último punto se nota como avisos eléctricos que aparecen y desaparecen. Antes de cambiar una centralita, hay que revisar conectores y masas."
         ]},
        {"id": "c32-b25", "h2": "15,9 km por la C-32 y la B-25",
         "parrafos": [
             "La ruta desde el centro hasta el carrer del Tambor del Bruc de Sant Joan Despí va por la C-32 y la B-25: 15,9 km por carretera, 12,5 en línea recta.",
             "Castelldefels está en la lista de municipios del Área Metropolitana de Barcelona, que es la zona donde el taller ofrece recogida y entrega del coche y vehículo de cortesía, sujetos a disponibilidad."
         ]},
        {"id": "itv-viladecans", "h2": "La ITV más próxima, en Viladecans",
         "parrafos": [
             "En el registro de la Generalitat, la estación más cercana por carretera es la de Viladecans (B07), en el carrer Jocelyn Bell 16, a 7,6 km del centro de Castelldefels."
         ]},
        {"id": "oficial-y-cifras", "h2": "El servicio oficial, en Sant Boi",
         "parrafos": [
             "El punto oficial BMW más cercano según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 12,2 km. Red de la marca y especialista independiente quedan, por tanto, a una distancia parecida; la elección depende del trabajo.",
             "Castelldefels tenía 70.057 habitantes en 2025, un 9,7 % más que en 2015, y 29.433 turismos en 2024 según Idescat: 420 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Castelldefels?",
         "a": "Sí: el municipio está en el área metropolitana de Barcelona y hay recogida y entrega sujeta a disponibilidad."},
        {"q": "¿Dónde paso la ITV si vivo en Castelldefels?",
         "a": "La más cercana por carretera es la de Viladecans (B07), en el carrer Jocelyn Bell 16, a 7,6 km."},
        {"q": "¿El salitre afecta a la electrónica del BMW?",
         "a": "Puede sulfatar conectores expuestos y provocar avisos intermitentes. Es lo primero que se revisa en un coche que vive junto al mar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "70.057 habitantes (+9,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080569")},
        {"etiqueta": "Turismos (2024)", "valor": "29.433 · 420 por cada 1.000 hab.", **F.idescat("080569")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 1,8 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Viladecans (B07) · 7,6 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 15,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080569"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Viladecans
CIUDADES["viladecans"] = {
    "h1": "Viladecans: ITV en la ciudad y taller especialista BMW a 11,3 km",
    "entradilla": "En Viladecans tienes ITV dentro del municipio, el servicio oficial BMW en Sant Boi y el taller especialista de la red en Sant Joan Despí, a 11,3 km. Tres datos, tres distancias.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 11.3},
    "secciones": [
        {"id": "jocelyn-bell", "h2": "La ITV del carrer Jocelyn Bell",
         "parrafos": [
             "La estación de Viladecans (B07), de Applus, está en el carrer Jocelyn Bell 16, dentro del término, según el registro de la Generalitat. Es también la más cercana por carretera para Castelldefels.",
             "Si el coche tiene que pasar por el taller antes de la inspección, lo lógico es hacer allí la pre-ITV y pedir cita en la estación para la semana siguiente."
         ]},
        {"id": "once-kilometros", "h2": "Once kilómetros por la C-32 y la B-25",
         "parrafos": [
             "Desde el centro de Viladecans hasta la nave de Dasercars Barcelona hay 11,3 km por carretera, aunque en línea recta son solo 7,1: la ruta más corta da la vuelta por la C-32 y la B-25.",
             "Viladecans pertenece al Área Metropolitana de Barcelona. Dentro de ella, el taller puede recoger y devolver el coche y dejarte uno de cortesía en reparaciones largas, si hay disponibilidad."
         ]},
        {"id": "sant-boi-oficial", "h2": "Barcelona Premium, en la carretera del Prat",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 7,6 km por carretera y 3,9 en línea recta. Es donde corresponde llevar el coche para una reparación cubierta por la garantía del fabricante; para todo lo demás, puedes comparar."
         ]},
        {"id": "viladecans-en-cifras", "h2": "67.587 vecinos y 28.520 turismos",
         "parrafos": [
             "El padrón de 2025 da a Viladecans 67.587 habitantes, un 3,1 % más que en 2015. Idescat, con datos de la DGT, contaba 28.520 turismos en 2024: 422 por cada 1.000 vecinos. Con la C-32 a mano, un diésel puede hacer sin esfuerzo los kilómetros a ritmo constante que necesita para limpiar el filtro de partículas."
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Viladecans?",
         "a": "Sí: la estación B07, en el carrer Jocelyn Bell 16, según la Generalitat."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 11,3 km por carretera, en el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
        {"q": "¿Podéis recoger el coche en Viladecans?",
         "a": "Sí, Viladecans está en el área metropolitana; la recogida depende de disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "67.587 habitantes (+3,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("083015")},
        {"etiqueta": "Turismos (2024)", "valor": "28.520 · 422 por cada 1.000 hab.", **F.idescat("083015")},
        {"etiqueta": "ITV en el municipio", "valor": "Viladecans (B07), c. Jocelyn Bell 16", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 7,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 11,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("083015"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}


def aplicar_meta():
    """Aplica META y TITLES (vacíos en esta tanda: las 14 ciudades tienen impresiones)."""
    from comun import CIUDADES_DIR
    for campo, dic in (("metaDescription", META), ("metaTitle", TITLES)):
        for slug, txt in dic.items():
            f = CIUDADES_DIR / f"{slug}.json"
            cj = json.loads(f.read_text("utf-8"))
            cj[campo] = txt
            f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
            print(campo, slug, len(txt))
    print(f"{len(META)} meta, {len(TITLES)} titles")


if __name__ == "__main__":
    aplicar_meta()
