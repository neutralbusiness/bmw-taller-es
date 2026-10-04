# Tanda 15: Collado-Villalba, Boadilla del Monte, El Prat de Llobregat, Arganda del Rey,
# Colmenar Viejo, Cerdanyola del Vallès, Pinto, Tres Cantos, Vic, Gavà, Ripollet,
# Sant Adrià de Besòs, Galapagar, Azuqueca de Henares y Navalcarnero.
#
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_15
#
# Exclusiones del coordinador: ninguna ciudad de la tanda está en la lista. La lista
# excluye «arganda» (el subdominio duplicado); «arganda-del-rey» es el municipio
# canónico y sí se escribe.
#
# META / TITLES: las 15 ciudades tienen impresiones en paso_gsc.json, así que no se
# toca ni metaDescription ni metaTitle (aunque varias prometen ISTA, «hasta un 50 %»
# o «diagnosis oficial»: queda anotado en el informe para Martin).
#
# Decisiones sobre los datos:
# - Azuqueca de Henares: la ITV del fichero viene de OpenStreetMap (verificar: true,
#   sin dirección) y no hay parque de turismos: no se publica ninguna de las dos cosas.
# - Boadilla del Monte: 1.274 turismos por cada 1.000 habitantes (flotas domiciliadas).
#   No se usa la proporción; solo la cifra absoluta, advirtiendo que supera a la población.
# - Pinto (estación 2864) y Arganda del Rey (estación 2852): ITV con precisión de
#   municipio; no se da distancia, solo dirección del listado.
# - Tres Cantos: el listado escribe «TÜV SÜV ATISAE»; se publica el nombre del operador
#   como «TÜV SÜD ATISAE» (el mismo operador de Collado-Villalba y Lozoyuela).
import sys
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI.parent / "piloto"))
sys.path.insert(0, str(_AQUI.parent))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

# ---------------------------------------------------------------- Collado-Villalba
CIUDADES["collado-villalba"] = {
    "h1": "BMW en Collado-Villalba: tres ITV en el municipio y el especialista a 49 km",
    "entradilla": "Quien busca «BMW Villalba» suele querer el concesionario, y en el localizador de la marca no aparece ninguno dentro del municipio. Aquí tienes qué hay cerca, dónde pasar la ITV sin salir de Villalba y qué supone llevar el coche a nuestro taller de Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 49.1},
    "secciones": [
        {"id": "concesionario-las-rozas", "h2": "El punto oficial de BMW más cercano está en Las Rozas",
         "parrafos": [
             "Según bmw.es, el servicio oficial con taller más próximo a Collado-Villalba es Movilnorte, en el kilómetro 23,100 de la A-6, en Las Rozas: 17,8 km por carretera. Si te llega una carta de la marca para una llamada a revisión, esa cita se pide allí.",
             "Nosotros somos otra cosa: Dasercars, un taller independiente que solo trabaja BMW y MINI. Lo que cambia es quién hace el mantenimiento, no la garantía: el Reglamento (UE) 461/2010 impide que el fabricante la condicione a pasar por su red, siempre que se sigan los intervalos y se usen piezas y aceites con su especificación.",
         ]},
        {"id": "tres-estaciones-itv", "h2": "Tres estaciones de ITV, dos de ellas en el polígono P-29",
         "parrafos": [
             "El listado de la Comunidad de Madrid recoge tres estaciones dentro del término: la de TÜV SÜD ATISAE (2813) en la calle Escofina 3 y la de ITV P-29 Collado Villalba (2883) en la calle Buril 10, ambas en el polígono industrial P-29, y la de Itevelesa (2832), junto a la A-6 en el kilómetro 37,6.",
             "Si te toca la inspección, no hace falta bajar a Madrid: lo que sí conviene es revisar antes luces, escobillas y el nivel de emisiones si el coche es diésel y ha hecho mucho trayecto corto.",
         ]},
        {"id": "883-metros", "h2": "A 883 metros, el invierno empieza por la batería",
         "parrafos": [
             "El centro urbano está a 883 m de altitud. Las mañanas de helada son las que descubren una batería floja, sobre todo en los BMW con arranque y parada automático, que piden más a la batería que un coche sin ese sistema. Cuando se cambia, hay que registrarla en la centralita para que la carga se ajuste a la nueva.",
             "El otro punto es el refrigerante: no basta con que esté a nivel, tiene que tener la concentración de anticongelante correcta. Se mide en un momento y evita un susto en enero.",
         ]},
        {"id": "a6-m40-a1", "h2": "49 kilómetros por la A-6, la M-40 y la A-1",
         "parrafos": [
             "Desde el centro de Collado-Villalba hasta la nave de la calle Valgrande, en Alcobendas, la ruta baja por la A-6, rodea Madrid por la M-40 y sube por la A-1: 49,1 km por carretera, 31,8 en línea recta. Con la A-6 y la AP-6 pasando junto al casco urbano, la salida es directa.",
             "Esa distancia pesa. Tiene sentido para lo que pide un especialista —un fallo de inyección en un diésel N57, un aviso de AdBlue que vuelve, una avería eléctrica que no se ha encontrado— más que para un cambio de neumáticos. La recogida y el vehículo de cortesía existen dentro del área metropolitana de Madrid y están sujetos a disponibilidad: pregunta al reservar si tu dirección entra.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay concesionario BMW en Collado-Villalba?",
         "a": "El localizador de bmw.es no muestra ninguno con taller en el municipio. El más próximo es Movilnorte, en la A-6, km 23,100, en Las Rozas, a 17,8 km."},
        {"q": "¿Dónde paso la ITV en Collado-Villalba?",
         "a": "Hay tres estaciones en el término: dos en el polígono P-29 (calle Escofina 3 y calle Buril 10) y una en la A-6, km 37,6."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 49,1 km por carretera, en la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "67.274 habitantes (+8,4 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "34.592 · 514 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Estaciones ITV en el municipio", "valor": "3", **F.itv_madrid},
        {"etiqueta": "Altitud del centro urbano", "valor": "883 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Las Rozas) · 17,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 49,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Boadilla del Monte
CIUDADES["boadilla-del-monte"] = {
    "h1": "Boadilla del Monte y tu BMW: dos concesionarios casi a la par y el taller a 31 km",
    "entradilla": "Boadilla ha crecido un 36 % en diez años, frente al 11,6 % de Madrid capital. Si tienes un BMW o un MINI en Boadilla, te resumimos qué servicio oficial te queda más a mano, dónde está la ITV más próxima y cómo se llega a nuestro taller de Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 31.4},
    "secciones": [
        {"id": "alcorcon-o-majadahonda", "h2": "Alcorcón o Majadahonda: 200 metros de diferencia",
         "parrafos": [
             "En el localizador de bmw.es, los dos servicios oficiales más próximos quedan prácticamente igual de lejos: Vehinter, en la avenida de San Martín de Valdeiglesias 14-16 de Alcorcón, a 11,6 km por carretera, y Movilnorte, en Majadahonda, a 11,8 km. Elige el que te pille de camino.",
             "Tener dos opciones a la par permite elegir por horario o por la ruta de cada día. Y si prefieres un especialista independiente para el aceite, los frenos, la distribución o una avería que no termina de aparecer en el diagnóstico, la decisión es tuya.",
         ]},
        {"id": "itv-carralero", "h2": "La ITV, en El Carralero o en Pozuelo",
         "parrafos": [
             "En el listado oficial de la Comunidad de Madrid, la estación más próxima por carretera al centro de Boadilla es la de Entidad IDV Madrid (2862), en la calle De la Fresa 12 del polígono El Carralero, en Majadahonda: 8,2 km. Muy cerca le sigue la de Intectra (2823), en Pozuelo de Alarcón, a 8,9 km.",
         ]},
        {"id": "m513-m40", "h2": "De la M-513 a la M-40 y la A-1",
         "parrafos": [
             "Hasta la calle Valgrande de Alcobendas hay 31,4 km por carretera y 24,2 en línea recta: se sale por la M-513, se toma la M-40 por el oeste y el norte y se termina en la A-1. Con la M-50 y la M-501 también a menos de tres kilómetros del centro, hay alternativas si la M-40 está cargada.",
             "Boadilla forma parte del área metropolitana, donde el taller ofrece recogida y entrega del coche y vehículo de cortesía para reparaciones largas. Los dos dependen de disponibilidad, así que pídelos al reservar y no el mismo día.",
         ]},
        {"id": "boadilla-crece", "h2": "De 48.775 a 66.349 vecinos",
         "parrafos": [
             "Ese es el salto del padrón entre 2015 y 2025. La Comunidad de Madrid, a partir de la DGT, cuenta además 84.524 turismos censados en el municipio en 2025: más turismos que habitantes, lo que indica que la cifra incluye vehículos de empresas con domicilio en Boadilla y no sirve para medir cuántos coches tiene cada familia.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Boadilla?",
         "a": "Dos casi empatados: Vehinter, en Alcorcón (11,6 km), y Movilnorte, en Majadahonda (11,8 km), según bmw.es."},
        {"q": "¿Dónde paso la ITV si vivo en Boadilla del Monte?",
         "a": "La más próxima por carretera es la de la calle De la Fresa 12, en el polígono El Carralero de Majadahonda, a 8,2 km; la de Pozuelo queda a 8,9."},
        {"q": "¿Recogéis el coche en Boadilla?",
         "a": "Hay recogida y entrega dentro del área metropolitana de Madrid, sujeta a disponibilidad. Confírmalo al pedir cita."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "31,4 km por la M-513, la M-40 y la A-1 hasta Alcobendas."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí: MINI comparte motores y electrónica con BMW, y se diagnostica con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "66.349 habitantes (+36 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos censados (2025)", "valor": "84.524 (incluye flotas de empresa)", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "El Carralero (Majadahonda) · 8,2 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Alcorcón) · 11,6 km / Movilnorte (Majadahonda) · 11,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 31,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- El Prat de Llobregat
CIUDADES["el-prat-de-llobregat"] = {
    "h1": "Especialista BMW para El Prat de Llobregat, a 9 km por la B-10",
    "entradilla": "Entre el aeropuerto, el delta y el mar, El Prat tiene a mano casi todo lo que necesita un BMW: dos servicios oficiales a unos cinco kilómetros, la ITV en Cornellà y nuestro taller especialista en Sant Joan Despí, a 9,2 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 9.2},
    "secciones": [
        {"id": "b10-sant-joan-despi", "h2": "Nueve kilómetros hasta el carrer del Tambor del Bruc",
         "parrafos": [
             "Desde el centro de El Prat, la ruta hasta la nave de Dasercars Barcelona sigue la B-10: 9,2 km por carretera, 5 en línea recta.",
             "Al estar las dos dentro del Área Metropolitana de Barcelona, puedes pedir que recojan y devuelvan el coche, o un vehículo de cortesía si la reparación dura varios días. Ambas cosas dependen de disponibilidad, así que conviene pedirlas con la cita.",
         ]},
        {"id": "aire-del-delta", "h2": "Coches que duermen a menos de cuatro kilómetros del mar",
         "parrafos": [
             "El centro de El Prat está a unos 3,8 km de la costa y a 8 m de altitud. La humedad salina no se ve, pero trabaja: oxida los anclajes del escape y los soportes de los bajos, deja una capa de óxido en los discos de un coche que pasa una semana sin moverse y ataca los conectores que quedan expuestos.",
             "Si tu BMW pasa temporadas aparcado, los primeros frenazos después de la pausa pueden sonar o vibrar. Si el ruido no se va en pocos kilómetros, que lo mire alguien antes de que el óxido marque el disco.",
         ]},
        {"id": "hospitalet-o-sant-boi", "h2": "Servicio oficial: L'Hospitalet y Sant Boi, casi a la misma distancia",
         "parrafos": [
             "El localizador de bmw.es sitúa dos puntos de Barcelona Premium casi igual de cerca: el de la calle Montserrat Roig 31, en L'Hospitalet de Llobregat, a 4,7 km por carretera, y el de la carretera del Prat 15, en Sant Boi, a 5,2 km. Si buscabas el concesionario, es uno de esos dos; nosotros somos un taller independiente que solo trabaja BMW y MINI.",
         ]},
        {"id": "itv-campsa", "h2": "La ITV, en el passeig de la Campsa de Cornellà",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es la de Cornellà (B11), en el passeig de la Campsa 64, a 5,3 km. Queda prácticamente de camino al taller, así que una pre-ITV y la inspección se pueden encadenar en la misma semana. Y con la C-31, la C-32 y la A-2 a menos de tres kilómetros del centro, un diésel tiene a mano la vía rápida que necesita de vez en cuando para regenerar el filtro de partículas.",
             "El Prat tenía 66.338 habitantes en 2025 y 27.428 turismos en 2024 (Idescat, con datos de la DGT): 413 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuánto hay desde El Prat hasta vuestro taller?",
         "a": "9,2 km por la B-10 hasta Sant Joan Despí."},
        {"q": "¿Recogéis el coche en El Prat?",
         "a": "Sí, El Prat está en el área metropolitana de Barcelona. La recogida está sujeta a disponibilidad: pídela al reservar."},
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Cornellà de Llobregat (B11), passeig de la Campsa 64, a 5,3 km según el registro de la Generalitat."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano a El Prat?",
         "a": "Barcelona Premium en L'Hospitalet (4,7 km) y su punto de Sant Boi (5,2 km), según bmw.es."},
        {"q": "¿Qué le hace el aire del mar a un BMW?",
         "a": "Acelera el óxido en bajos, escape y discos de freno de un coche parado, y la sulfatación de conectores."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "66.338 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("081691")},
        {"etiqueta": "Turismos (2024)", "valor": "27.428 · 413 por cada 1.000 hab.", **F.idescat("081691")},
        {"etiqueta": "ITV más cercana", "valor": "Cornellà (B11) · 5,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (L'Hospitalet) · 4,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 9,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081691"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Arganda del Rey
CIUDADES["arganda-del-rey"] = {
    "h1": "Arganda del Rey: horario, ruta por la A-3 y dos ITV para tu BMW",
    "entradilla": "Antes de llevar el coche a ningún sitio, lo primero que se pregunta desde Arganda es cuándo abre el taller y si es el servicio técnico de BMW. Lo aclaramos, junto con las dos estaciones de ITV del municipio y la ruta hasta Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 40.2},
    "secciones": [
        {"id": "horario-y-cita", "h2": "Cuándo abre el taller y cómo se pide cita",
         "parrafos": [
             "Dasercars Madrid trabaja de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00; sábados y domingos, cerrado. Desde Arganda, lo práctico es dejar el coche por la mañana y volver a recogerlo al final de la jornada, o al día siguiente si el trabajo es largo.",
             "Antes de tocar nada recibes un presupuesto por escrito, y el trabajo no empieza hasta que lo apruebas. La diagnosis también se presupuesta: conectar el equipo y buscar una avería es trabajo técnico.",
         ]},
        {"id": "servicio-tecnico-oficial", "h2": "Si buscas el servicio técnico oficial",
         "parrafos": [
             "No lo somos. Según bmw.es, el punto oficial con taller más próximo es AutoPremier, en la carretera de Valencia, km 7,3, ya en Madrid: 19,8 km por carretera. Si lo que necesitas es el fabricante, es esa dirección.",
             "Dasercars es un taller independiente dedicado a BMW y MINI. Hacemos mantenimiento, diagnosis y reparación, con especial experiencia en los diésel N47, N57, B47 y B57.",
         ]},
        {"id": "dos-itv-arganda", "h2": "Dos estaciones ITV dentro del término",
         "parrafos": [
             "El listado de la Comunidad de Madrid incluye dos en Arganda del Rey: la de General de Servicios ITV (2852), en el camino del Puente Viejo, y la de Laboratorio e Inspección de Vehículos (2807), en el camino de San Martín de la Vega 8.",
             "Con dos estaciones a mano, la inspección se resuelve en el propio municipio. Si el coche va antes al taller, pide que repasen holguras de dirección, frenos y luces: son puntos que la inspección mira siempre.",
         ]},
        {"id": "a3-hasta-alcobendas", "h2": "40 kilómetros por la A-3, la M-30 y la A-1",
         "parrafos": [
             "La ruta desde el centro de Arganda entra en Madrid por la A-3, cruza por la M-30 y sale por la A-1 hasta la calle Valgrande: 40,2 km por carretera, 31,8 en línea recta. La R-3 pasa también a menos de tres kilómetros del casco.",
             "Para trabajos de varios días, pregunta por la recogida y el vehículo de cortesía: solo se ofrecen dentro del área metropolitana de Madrid y sujetos a disponibilidad, así que confirma si tu dirección entra. Arganda tenía 60.419 habitantes en 2025 y 30.786 turismos censados: 510 por cada 1.000.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué horario tiene el taller?",
         "a": "De lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00. Fines de semana, cerrado."},
        {"q": "¿Sois el servicio técnico oficial de BMW?",
         "a": "No. Somos taller independiente especialista. El oficial más próximo a Arganda es AutoPremier, carretera de Valencia km 7,3 (Madrid), a 19,8 km."},
        {"q": "¿Qué ITV hay en Arganda del Rey?",
         "a": "Dos: camino del Puente Viejo (2852) y camino de San Martín de la Vega 8 (2807), según la Comunidad de Madrid."},
        {"q": "¿Cuánto hay hasta Alcobendas?",
         "a": "40,2 km por la A-3, la M-30 y la A-1."},
        {"q": "¿La diagnosis se paga aparte?",
         "a": "Se presupuesta antes, como cualquier otro trabajo: sabes el importe antes de que se conecte el equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "60.419 habitantes (+10,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "30.786 · 510 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Estaciones ITV en el municipio", "valor": "2", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, ctra. de Valencia km 7,3 · 19,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 40,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Colmenar Viejo
CIUDADES["colmenar-viejo"] = {
    "h1": "Colmenar Viejo: el especialista BMW queda más cerca que el concesionario",
    "entradilla": "Una curiosidad útil: desde Colmenar Viejo, nuestro taller de Alcobendas está a 22 km y el servicio oficial BMW más próximo, a 24,1. Te contamos la ruta, la ITV del polígono La Mina y qué pide un coche a casi 900 metros.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 22.0},
    "secciones": [
        {"id": "m607-m616", "h2": "Por la M-607 y la M-616, sin entrar en Madrid",
         "parrafos": [
             "La ruta hasta la calle Valgrande baja por la M-607 y cruza por la M-616 hacia Alcobendas: 22 km por carretera, 16,8 en línea recta. No hace falta pisar la M-40 ni la M-30.",
             "El taller ofrece recogida y entrega dentro del área metropolitana de Madrid y vehículo de cortesía para reparaciones largas, sujetos ambos a disponibilidad; pregunta al reservar si cubren tu calle.",
         ]},
        {"id": "las-tablas-o-cuzco", "h2": "El servicio oficial, en el norte de Madrid",
         "parrafos": [
             "Según el localizador de bmw.es, los puntos oficiales más próximos están en la capital y casi empatados: BYmyCAR Madrid, en la avenida de Burgos 133 (Las Tablas), a 24,1 km, y Caetano Cuzco, en Salvatierra, a 24,4 km.",
             "Para el mantenimiento puedes elegir taller. Desde Colmenar, además, el especialista independiente te ahorra unos kilómetros.",
         ]},
        {"id": "itv-la-mina", "h2": "La ITV, en la calle Perfumería",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid sitúa una estación dentro del municipio: la de Applus Iteuve (2890), en la calle Perfumería 1 del polígono industrial La Mina. Para la inspección no hace falta salir de Colmenar.",
         ]},
        {"id": "892-metros", "h2": "Un término de 182 km² a 892 metros de altitud",
         "parrafos": [
             "El centro urbano está a 892 m, y en invierno se nota. El líquido de frenos merece atención aparte: absorbe humedad con el tiempo y pierde capacidad, por eso BMW lo cambia por años y no por kilómetros. En las bajadas de las carreteras de la sierra, un líquido viejo es lo último que quieres.",
             "La batería es el otro clásico de las mañanas frías. Si la cambias, que la registren en la centralita: sin ese paso, el sistema de carga sigue tratándola como la antigua. Y si subes a menudo hacia los puertos, piensa en neumáticos de invierno o cadenas homologadas para tu medida: un BMW de propulsión trasera lo agradece especialmente en una rampa helada.",
             "Colmenar ha pasado de 47.601 habitantes en 2015 a 58.730 en 2025, un 23,4 % más, y tenía 28.162 turismos censados en 2025: 480 por cada 1.000 vecinos. Con un término tan extenso, la densidad es de solo 323 habitantes por km².",
         ]},
    ],
    "faq": [
        {"q": "¿Qué queda más cerca de Colmenar, vuestro taller o el concesionario?",
         "a": "Nuestro taller, a 22 km en Alcobendas. El servicio oficial más próximo, BYmyCAR Madrid en Las Tablas, está a 24,1 km."},
        {"q": "¿Dónde paso la ITV en Colmenar Viejo?",
         "a": "En la calle Perfumería 1, polígono La Mina (estación 2890), dentro del municipio."},
        {"q": "¿Recogéis el coche en Colmenar?",
         "a": "Hay recogida en el área metropolitana de Madrid, sujeta a disponibilidad. Confirma al reservar si tu dirección entra."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, con el mismo equipo de diagnosis y los mismos planes de mantenimiento que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "58.730 habitantes (+23,4 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "28.162 · 480 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Superficie del término", "valor": "182 km²", **F.cartociudad},
        {"etiqueta": "ITV en el municipio", "valor": "Applus Iteuve, c/ Perfumería 1", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid (Las Tablas) · 24,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 22 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.cartociudad_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Cerdanyola del Vallès
CIUDADES["cerdanyola-del-valles"] = {
    "h1": "Cambio de aceite y mantenimiento BMW para Cerdanyola del Vallès",
    "entradilla": "Para un BMW, el cambio de aceite es la operación más frecuente y la que más se presta a ahorrar donde no se debe. Te explicamos qué exige, dónde tienes el servicio oficial y la ITV desde Cerdanyola y cómo llegar a nuestro taller de Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 24.1},
    "secciones": [
        {"id": "aceite-longlife", "h2": "Qué lleva un cambio de aceite bien hecho",
         "parrafos": [
             "Un BMW no admite cualquier aceite: el plan de mantenimiento exige uno con la homologación Longlife que corresponda a su motor, y en los diésel con filtro de partículas, uno bajo en cenizas. El filtro de aceite, la junta del tapón y el reinicio del indicador de servicio forman parte del trabajo; si falta alguna de las tres cosas, el cambio no está completo.",
             "Lo que de verdad ahorra es poner el aceite correcto en su intervalo. El indicador de servicio calcula el cambio según el uso, pero si el coche hace sobre todo trayectos cortos por Cerdanyola, no conviene apurarlo hasta el último kilómetro. Un lubricante sin la especificación o un cambio que se retrasa miles de kilómetros se paga más adelante en la cadena de distribución o en el turbo.",
         ]},
        {"id": "presupuesto", "h2": "El importe, por escrito y antes de empezar",
         "parrafos": [
             "No publicamos tarifas: la cantidad de aceite, el filtro y la especificación cambian de un motor a otro. Con el modelo y el año te damos el número exacto, y te llega por escrito antes de que nadie abra el capó; si no te convence, no se hace.",
         ]},
        {"id": "sant-cugat", "h2": "Servicio oficial e ITV, en Sant Cugat",
         "parrafos": [
             "Según bmw.es, el servicio oficial más próximo es Quadis Munich, en el carrer Vallespir 19 de Sant Cugat del Vallès: 7,4 km por la ruta más corta, unos 10 por la más rápida.",
             "Para la ITV, el registro de la Generalitat da la de Sant Cugat (B22), en el carrer Amposta 2 del polígono Sant Mamet, a 7,9 km por carretera, y casi a la par la de Sabadell (B24), a 8,3 km.",
         ]},
        {"id": "c58-b20", "h2": "Por la C-58 y la B-20 hasta Sant Joan Despí",
         "parrafos": [
             "Desde el centro de Cerdanyola hasta la nave de Dasercars Barcelona hay 24,1 km por la C-58 y la B-20, 15,3 en línea recta. El municipio pertenece al Área Metropolitana de Barcelona, así que puedes pedir recogida y entrega del coche, sujeta a disponibilidad.",
             "Cerdanyola tenía 58.528 habitantes en 2025, apenas un 1,9 % más que en 2015, y 26.213 turismos en 2024 según Idescat: 448 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué aceite lleva mi BMW?",
         "a": "El que indica su plan de mantenimiento, con la homologación Longlife de su motor. Con el modelo y el año te decimos cuál."},
        {"q": "¿Me dais el precio del cambio de aceite?",
         "a": "Sí, por escrito y antes de empezar, en cuanto sepamos modelo, año y motor."},
        {"q": "¿Dónde paso la ITV desde Cerdanyola?",
         "a": "La más próxima por carretera es Sant Cugat (B22), a 7,9 km; la de Sabadell (B24) queda a 8,3."},
        {"q": "¿Recogéis el coche en Cerdanyola?",
         "a": "Sí, dentro del área metropolitana de Barcelona y sujeto a disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "58.528 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082665")},
        {"etiqueta": "Turismos (2024)", "valor": "26.213 · 448 por cada 1.000 hab.", **F.idescat("082665")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Cugat (B22) · 7,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Cugat) · 7,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 24,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082665"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Pinto
CIUDADES["pinto"] = {
    "h1": "Taller BMW cerca de Pinto: Getafe para lo oficial, Alcobendas para el especialista",
    "entradilla": "Desde Pinto, el servicio oficial BMW está a 9,5 km y nuestro taller, a 37,9, al otro lado de Madrid. La ITV no hace falta buscarla fuera: hay dos estaciones en el municipio.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 37.9},
    "secciones": [
        {"id": "getafe-cerca", "h2": "Vehinter, en la carretera de Toledo",
         "parrafos": [
             "El punto oficial más próximo según bmw.es es Vehinter, en la carretera de Madrid a Toledo, en Getafe: 9,5 km por carretera. Para lo que solo puede hacer la red de la marca, es lo más cómodo.",
             "Si lo que necesitas es un taller que conozca bien BMW sin pasar por el concesionario, ahí entramos nosotros, aunque nos separe más distancia.",
         ]},
        {"id": "dos-itv-pinto", "h2": "Dos ITV sin salir de Pinto",
         "parrafos": [
             "El listado de la Comunidad de Madrid recoge dos estaciones en el municipio: la de Applus Iteuve (2867), en la calle Carpinteros 13, y la de ITV Maco (2864), en la avenida de las Avutardas 7, en el polígono El Cascajal.",
             "Si el coche tiene algún testigo encendido en el cuadro, resuélvelo antes de pedir cita: un aviso de motor o de airbag es motivo de rechazo, y borrarlo sin reparar la causa no sirve porque vuelve a aparecer.",
         ]},
        {"id": "a4-m30-a1", "h2": "De sur a norte: A-4, M-30 y A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas sube por la A-4, cruza Madrid por la M-30 y sale por la A-1: 37,9 km por carretera, 33,1 en línea recta. Por eso tiene más sentido traer el coche para un trabajo concreto —una avería que no se ha localizado, distribución, inyección o el mantenimiento por plan de marca— que para algo menor.",
             "Para trabajos de más de un día existen recogida y vehículo de cortesía dentro del área metropolitana de Madrid, sujetos a disponibilidad. Pregunta al reservar si llegan hasta tu calle.",
         ]},
        {"id": "pinto-en-cifras", "h2": "56.651 vecinos y 28.166 turismos",
         "parrafos": [
             "Pinto tenía 48.660 habitantes en 2015 y 56.651 en 2025, un 16,4 % más. El parque de 2025, según la Comunidad de Madrid a partir de la DGT, era de 28.166 turismos: 497 por cada 1.000 vecinos. La A-4 pasa a menos de tres kilómetros del centro, igual que la M-506 y la M-841.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Pinto?",
         "a": "Vehinter, en la carretera de Madrid a Toledo (Getafe), a 9,5 km según bmw.es."},
        {"q": "¿Qué ITV hay en Pinto?",
         "a": "Dos: calle Carpinteros 13 (Applus Iteuve) y avenida de las Avutardas 7, polígono El Cascajal (ITV Maco)."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "37,9 km por la A-4, la M-30 y la A-1, en la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Recogéis el coche en Pinto?",
         "a": "La recogida existe dentro del área metropolitana de Madrid y está sujeta a disponibilidad: confirma al reservar si llega a tu dirección."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, MINI y BMW comparten buena parte de motores y electrónica."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "56.651 habitantes (+16,4 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "28.166 · 497 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Estaciones ITV en el municipio", "valor": "2", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 9,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 37,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Tres Cantos
CIUDADES["tres-cantos"] = {
    "h1": "BMW en Tres Cantos: el taller especialista, a 12 km en Alcobendas",
    "entradilla": "Desde Tres Cantos, el taller de la red está a 12,4 km: los que separan el municipio de la calle Valgrande de Alcobendas. Te contamos también dónde está la ITV del municipio y qué servicio oficial te queda más cerca.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 12.4},
    "secciones": [
        {"id": "doce-kilometros", "h2": "12,4 kilómetros por la M-607 y la M-616",
         "parrafos": [
             "Desde el centro de Tres Cantos, la ruta a Dasercars Madrid toma la M-607 y enlaza con la M-616 hasta Alcobendas: 12,4 km por carretera, 8,6 en línea recta. Con esa distancia, dejar el coche de camino al trabajo y recogerlo a la vuelta es realista.",
             "Si no puedes acercarte, el taller ofrece recogida y entrega dentro del área metropolitana de Madrid, y vehículo de cortesía cuando la reparación se alarga, siempre sujetos a disponibilidad.",
         ]},
        {"id": "no-somos-el-concesionario", "h2": "Lo que somos y lo que no",
         "parrafos": [
             "Dasercars no es concesionario ni servicio oficial de la marca: es un taller independiente dedicado a BMW y MINI, con especial experiencia en los diésel de cuatro y seis cilindros (N47, N57, B47, B57) y homologación REDISTA para escape y gases.",
             "Los puntos oficiales más próximos según bmw.es están en Madrid y casi empatados: BYmyCAR, en la avenida de Burgos 133 (Las Tablas), a 14,5 km, y Caetano Cuzco, en Salvatierra, a 14,7. Ojo a un detalle: nuestro taller te queda incluso un poco más cerca.",
         ]},
        {"id": "itv-san-isidro", "h2": "La ITV de la calle San Isidro Labrador",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid incluye una estación en el municipio: la de TÜV SÜD ATISAE (2811), en la calle San Isidro Labrador 6. Si el coche pasa antes por el taller por otra cosa, aprovecha para una revisión de luces, frenos y emisiones y ve a la inspección con todo en orden.",
         ]},
        {"id": "tres-cantos-crece", "h2": "Un 26,1 % más de vecinos que en 2015",
         "parrafos": [
             "Tres Cantos ha pasado de 43.309 a 54.592 habitantes en diez años. En 2025 tenía 28.323 turismos censados según la Comunidad de Madrid a partir de la DGT: 519 por cada 1.000 vecinos, frente a los 388 de Madrid capital.",
             "Una ciudad de trayectos cortos tiene un enemigo para los diésel: el filtro de partículas necesita kilómetros seguidos para regenerarse. Si tu BMW apenas sale del casco, una salida por la M-607 de vez en cuando le viene bien.",
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Tres Cantos?",
         "a": "No. Somos Dasercars, taller independiente especialista en Alcobendas. Los oficiales más próximos están en Las Tablas y en Salvatierra (Madrid)."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 12,4 km por la M-607 y la M-616."},
        {"q": "¿Puedo dejar el coche por la mañana y recogerlo por la tarde?",
         "a": "Sí, para trabajos de un día es lo habitual. El taller trabaja de lunes a viernes en jornada partida."},
        {"q": "¿Dónde paso la ITV en Tres Cantos?",
         "a": "En la estación de la calle San Isidro Labrador 6, dentro del municipio."},
        {"q": "¿Recogéis el coche en Tres Cantos?",
         "a": "Sí, dentro del área metropolitana de Madrid y sujeto a disponibilidad. Pídelo al reservar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "54.592 habitantes (+26,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "28.323 · 519 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "TÜV SÜD ATISAE, c/ San Isidro Labrador 6", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid (Las Tablas) · 14,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 12,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Vic
CIUDADES["vic"] = {
    "h1": "BMW en Vic: el concesionario está en la ciudad, el especialista a 77 km",
    "entradilla": "En Vic tienes el servicio oficial BMW y la ITV de Osona dentro del municipio. Nuestro taller está en Sant Joan Despí, a 77,1 km. Para que no haya confusión: esta página no es la del taller de la marca en Vic.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 77.1},
    "secciones": [
        {"id": "quadis-vic", "h2": "El taller de la marca está en la calle Perot Rocaguinarda",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial de la ciudad es Quadis Munich, en el carrer Perot Rocaguinarda 1, a 1,1 km del centro. Si buscabas su teléfono o su revisión oficial, el contacto es el suyo, no el de esta página.",
             "Nosotros somos Dasercars, un taller independiente especializado en BMW y MINI. El mantenimiento fuera del concesionario no anula la garantía si se respetan los intervalos y la especificación de piezas y aceites, como reconoce el Reglamento (UE) 461/2010; las llamadas a revisión de la marca, en cambio, se atienden en su red.",
         ]},
        {"id": "itv-osona", "h2": "La ITV de Osona, dentro del municipio",
         "parrafos": [
             "La estación de Osona (B04) del registro de la Generalitat está en el carrer Sant Llorenç Desmunts 22, en el propio término de Vic. Con la inspección y el servicio oficial a mano, para lo rutinario no hay motivo para salir de la comarca.",
         ]},
        {"id": "cuando-bajar", "h2": "Cuándo merece la pena bajar 77 kilómetros",
         "parrafos": [
             "Para un cambio de aceite o unas pastillas, no. Para una avería que ha vuelto después de dos visitas, un testigo de motor intermitente, un problema del sistema de AdBlue o un ruido de cadena en un diésel N47, sí puede compensar un segundo diagnóstico de especialista.",
             "La ruta hasta el carrer del Tambor del Bruc va por la C-17, la C-33 y la B-20: 77,1 km por carretera, 64,7 en línea recta. Vic queda fuera del área metropolitana, de modo que la recogida del taller no llega hasta aquí.",
             "Desde esta distancia, la llamada previa es casi obligada: modelo, año, kilómetros y cómo aparece el fallo. Con eso se decide si el viaje tiene sentido y, si lo tiene, se baja con la pieza encargada.",
         ]},
        {"id": "vic-en-cifras", "h2": "Capital de Osona, con 50.796 vecinos",
         "parrafos": [
             "Vic ha pasado de 42.498 habitantes en 2015 a 50.796 en 2025, un 19,5 % más. Idescat, a partir de la DGT, contaba 22.045 turismos en 2024: 434 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Sois el taller BMW de Vic?",
         "a": "No. El servicio oficial de la marca en Vic es Quadis Munich, carrer Perot Rocaguinarda 1. Dasercars está en Sant Joan Despí, a 77,1 km."},
        {"q": "¿Dónde paso la ITV en Vic?",
         "a": "En la estación de Osona (B04), carrer Sant Llorenç Desmunts 22, dentro del municipio."},
        {"q": "¿Merece la pena llevar el coche desde Vic hasta Sant Joan Despí?",
         "a": "Para el mantenimiento rutinario, normalmente no. Para una avería de BMW que no se ha resuelto en la comarca, puede que sí: llámanos antes y lo valoramos."},
        {"q": "¿Recogéis el coche en Vic?",
         "a": "No: la recogida cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "50.796 habitantes (+19,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082981")},
        {"etiqueta": "Turismos (2024)", "valor": "22.045 · 434 por cada 1.000 hab.", **F.idescat("082981")},
        {"etiqueta": "ITV en el municipio", "valor": "Osona (B04), c. Sant Llorenç Desmunts 22", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, c. Perot Rocaguinarda 1 · 1,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 77,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082981"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Gavà
CIUDADES["gava"] = {
    "h1": "Gavà: ITV a 2,9 km y taller especialista BMW a 14 km por la C-32",
    "entradilla": "Con la ITV de Viladecans a menos de tres kilómetros y el mar a menos de cinco, Gavà tiene sus propias prioridades de mantenimiento. Nuestro taller está en Sant Joan Despí, a 14,1 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 14.1},
    "secciones": [
        {"id": "itv-viladecans", "h2": "La ITV, en la calle Jocelyn Bell de Viladecans",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Viladecans (B07), en el carrer Jocelyn Bell 16: 2,9 km desde el centro de Gavà. Es tan cercana que lo cómodo es pasar allí la inspección y dejar el taller para lo que de verdad requiere un especialista.",
         ]},
        {"id": "playa-y-bajos", "h2": "Salitre: lo que conviene mirar en un coche de Gavà",
         "parrafos": [
             "El centro queda a 4,6 km de la línea de costa, y el término llega hasta la playa. Lo que más sufre con el aire marino son los bajos y el escape, los discos de freno de un coche que pasa días parado y los conectores eléctricos que quedan al aire.",
             "Un manguerazo de agua dulce a los bajos al acabar el verano ayuda más de lo que parece. Y si aparece un aviso eléctrico que va y viene, antes de cambiar una centralita hay que revisar conectores y masas.",
         ]},
        {"id": "c32-b25", "h2": "Por la C-32 y la B-25 hasta Sant Joan Despí",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona usa la C-32 y la B-25: 14,1 km por carretera, 8,5 en línea recta. Gavà es uno de los municipios del Área Metropolitana de Barcelona, así que hay recogida y entrega del coche, sujeta a disponibilidad; pídela al reservar.",
             "El servicio oficial BMW más próximo según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 10,4 km.",
         ]},
        {"id": "gava-en-cifras", "h2": "48.243 habitantes y 20.389 turismos",
         "parrafos": [
             "El padrón de 2025 da a Gavà 48.243 vecinos, un 4 % más que en 2015. Idescat, con datos de la DGT, contaba 20.389 turismos en 2024: 423 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Gavà?",
         "a": "La más próxima por carretera es la de Viladecans (B07), carrer Jocelyn Bell 16, a 2,9 km."},
        {"q": "¿Recogéis el coche en Gavà?",
         "a": "Sí, Gavà está en el área metropolitana. La recogida está sujeta a disponibilidad."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "14,1 km por la C-32 y la B-25 hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "48.243 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080898")},
        {"etiqueta": "Turismos (2024)", "valor": "20.389 · 423 por cada 1.000 hab.", **F.idescat("080898")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecans (B07) · 2,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 10,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 14,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080898"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Ripollet
CIUDADES["ripollet"] = {
    "h1": "Ripollet: el BMW oficial en Sabadell y el especialista a 24 km",
    "entradilla": "Hay quien busca el «BMW oficial» más cercano pensando que solo allí se puede mantener el coche sin perder la garantía. No es así, y te explicamos por qué, además de dónde tienes el servicio oficial, la ITV y nuestro taller.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 24.4},
    "secciones": [
        {"id": "garantia-fuera-de-la-red", "h2": "Mantenimiento fuera del concesionario, garantía intacta",
         "parrafos": [
             "La normativa europea de distribución de vehículos, el Reglamento (UE) 461/2010, permite hacer las revisiones en un taller independiente sin que el fabricante pueda negar la garantía por ello. La condición es seguir el plan: intervalos, piezas de calidad equivalente y aceites con la especificación correcta, con la factura como prueba.",
             "Lo que sí queda en la red oficial son las reparaciones que paga la marca y las campañas de revisión que convoca.",
         ]},
        {"id": "sabadell-oficial", "h2": "Los puntos oficiales, en Sabadell",
         "parrafos": [
             "Según bmw.es, los dos más próximos a Ripollet están en Sabadell y casi a la misma distancia: el taller autorizado Sitjas Motor, en la calle Quintana 64, a 9,5 km por carretera, y Quadis Munich, a 9,6 km.",
             "La ITV también te queda hacia allí: la estación de Sabadell (B24), en el polígono Can Roqueta, es la más próxima por carretera en el registro de la Generalitat, a 6,8 km.",
         ]},
        {"id": "c58-b20-ripollet", "h2": "24 kilómetros hasta Sant Joan Despí",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona va por la C-58 y la B-20: 24,4 km por carretera, 16,5 en línea recta. Ripollet forma parte del Área Metropolitana de Barcelona, de modo que puedes pedir recogida y entrega del coche o un vehículo de cortesía, ambos sujetos a disponibilidad.",
         ]},
        {"id": "ripollet-denso", "h2": "39.897 vecinos en 4,33 km²",
         "parrafos": [
             "Ripollet es un término muy pequeño y muy poblado: 9.214 habitantes por km² en 2025. Tenía 17.224 turismos en 2024 según Idescat, 432 por cada 1.000 vecinos, y una red de vías rápidas alrededor: la C-58, la AP-7, la C-17 y la C-33 pasan a menos de tres kilómetros del centro.",
             "Es una ventaja para un diésel: el filtro de partículas necesita de vez en cuando un rato a velocidad constante para regenerarse, y aquí basta con salir a cualquiera de ellas.",
         ]},
    ],
    "faq": [
        {"q": "¿Pierdo la garantía si no voy al concesionario?",
         "a": "No, si se respeta el plan de mantenimiento del fabricante. Lo ampara el Reglamento (UE) 461/2010."},
        {"q": "¿Cuál es el taller autorizado BMW más cercano a Ripollet?",
         "a": "Sitjas Motor, calle Quintana 64 de Sabadell, a 9,5 km; Quadis Munich, también en Sabadell, queda a 9,6."},
        {"q": "¿Recogéis el coche en Ripollet?",
         "a": "Sí, dentro del área metropolitana de Barcelona y según disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "39.897 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("081803")},
        {"etiqueta": "Turismos (2024)", "valor": "17.224 · 432 por cada 1.000 hab.", **F.idescat("081803")},
        {"etiqueta": "ITV más cercana", "valor": "Sabadell (B24) · 6,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Sitjas Motor (Sabadell) · 9,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 24,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081803"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sant Adrià de Besòs
CIUDADES["sant-adria-de-besos"] = {
    "h1": "Pre-ITV y taller BMW para Sant Adrià de Besòs",
    "entradilla": "En Sant Adrià está uno de los servicios oficiales BMW de Barcelona Premium, y la ITV de Badalona queda a 2,4 km. Nuestro taller, especialista independiente, está en Sant Joan Despí. Lo que necesitas saber para la pre-ITV, el horario y la ruta.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 20.8},
    "secciones": [
        {"id": "pre-itv", "h2": "Qué se mira en una pre-ITV",
         "parrafos": [
             "La ITV más próxima por carretera en el registro de la Generalitat es la de Badalona (B02), en el carrer Indústria 427-449, a 2,4 km del centro de Sant Adrià. Antes de ir, una pre-ITV repasa lo que la estación va a mirar: luces y reglaje, holguras de dirección y suspensión, frenos, neumáticos y emisiones.",
             "En las emisiones el taller tiene algo que aportar: Dasercars cuenta con homologación REDISTA para trabajos de escape y gases, que es justo donde un diésel con el filtro de partículas o el EGR tocados se queda en la inspección.",
         ]},
        {"id": "ronda-litoral", "h2": "El servicio oficial de la Ronda Litoral no somos nosotros",
         "parrafos": [
             "Según bmw.es, en el propio municipio está Barcelona Premium, en la calle Juan de Austria 1, junto a la Ronda Litoral: 1,6 km. Esta página es la de Dasercars, un taller independiente de BMW y MINI que no forma parte de esa red.",
         ]},
        {"id": "horario-sant-joan", "h2": "Horario y ruta hasta Sant Joan Despí",
         "parrafos": [
             "El taller abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00, y cierra los fines de semana. Está a 20,8 km por la B-10 y la B-20, 14,8 en línea recta: se cruza Barcelona por las rondas de punta a punta.",
             "Precisamente por eso, para quien vive en Sant Adrià tiene interés la recogida y entrega dentro del área metropolitana, sujeta a disponibilidad: pídela al reservar.",
         ]},
        {"id": "junto-al-mar", "h2": "A dos kilómetros del mar",
         "parrafos": [
             "El centro está a unos 2,1 km de la costa. El aire húmedo y salino acelera el óxido en bajos y anclajes del escape y deja marcados los discos de un coche que no se mueve en días. En un municipio tan denso —10.294 habitantes por km², en 3,82 km²— muchos coches duermen en la calle, y lo notan antes.",
             "Sant Adrià tenía 39.323 habitantes en 2025 y 12.322 turismos en 2024 (Idescat): 313 por cada 1.000, no muy lejos de los 281 de Barcelona ciudad.",
         ]},
    ],
    "faq": [
        {"q": "¿Hacéis pre-ITV?",
         "a": "Sí. Y la ITV más próxima a Sant Adrià es la de Badalona (B02), a 2,4 km."},
        {"q": "¿Qué horario tenéis?",
         "a": "De lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00."},
        {"q": "¿Sois el BMW de la Ronda Litoral?",
         "a": "No. Ese es Barcelona Premium, servicio oficial en la calle Juan de Austria 1. Nosotros somos Dasercars, en Sant Joan Despí."},
        {"q": "¿Recogéis el coche en Sant Adrià?",
         "a": "Sí, dentro del área metropolitana de Barcelona y sujeto a disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "39.323 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Barcelonès", **F.idescat("081944")},
        {"etiqueta": "Turismos (2024)", "valor": "12.322 · 313 por cada 1.000 hab.", **F.idescat("081944")},
        {"etiqueta": "ITV más cercana", "valor": "Badalona (B02) · 2,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, c. Juan de Austria 1 · 1,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 20,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081944"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Galapagar
CIUDADES["galapagar"] = {
    "h1": "Galapagar: ITV en Villalba, concesionario en Las Rozas y especialista BMW a 43 km",
    "entradilla": "La ITV y el servicio oficial BMW más próximos a Galapagar quedan a menos de quince kilómetros. Nuestro taller está más lejos, en Alcobendas: esto es lo que conviene hacer en cada sitio.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 43.2},
    "secciones": [
        {"id": "itv-a6", "h2": "Tres ITV en Collado-Villalba, casi a la misma distancia",
         "parrafos": [
             "La más próxima por carretera en el listado de la Comunidad de Madrid es la de Itevelesa (2832), en la A-6, km 37,6, a 6,5 km. Las otras dos del polígono P-29 de Collado-Villalba quedan a 7 y 7,1 km: elige la que mejor te venga de horario.",
         ]},
        {"id": "movilnorte", "h2": "Movilnorte, a 14 km en Las Rozas",
         "parrafos": [
             "El localizador de bmw.es da como servicio oficial más próximo a Movilnorte, en el kilómetro 23,100 de la A-6, en Las Rozas: 14 km por carretera. Es la referencia por cercanía para lo que solo hace el concesionario.",
         ]},
        {"id": "m505-hasta-alcobendas", "h2": "43 kilómetros por la M-505 y la A-6",
         "parrafos": [
             "Hasta la calle Valgrande de Alcobendas la ruta sale por la M-505, toma la A-6 y rodea Madrid por la M-40 hasta la A-1: 43,2 km por carretera, 30,2 en línea recta.",
             "Con esa distancia, el viaje compensa cuando el problema es de especialista: la cadena de un N47 que empieza a sonar en frío, un turbo que pierde presión, un aviso de AdBlue o una avería eléctrica sin diagnosticar. La recogida y el vehículo de cortesía funcionan dentro del área metropolitana de Madrid y sujetos a disponibilidad; consulta si llegan a tu dirección.",
         ]},
        {"id": "sierra-885", "h2": "A 885 metros: frenos y refrigerante",
         "parrafos": [
             "El casco urbano está a 885 m. En las carreteras de la zona, con cuestas y curvas, los frenos trabajan más que en llano, y el líquido, que absorbe humedad con los años, pierde punto de ebullición: por eso el plan de BMW lo cambia por tiempo.",
             "Galapagar tenía 36.758 habitantes en 2025, un 13,8 % más que en 2015, y 19.935 turismos censados ese año según la Comunidad de Madrid: 542 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Galapagar?",
         "a": "En Collado-Villalba. La más próxima por carretera es la de la A-6, km 37,6, a 6,5 km; las del polígono P-29 quedan a 7 y 7,1 km."},
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "Movilnorte, en la A-6, km 23,100 (Las Rozas), a 14 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "43,2 km por la M-505, la A-6, la M-40 y la A-1."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "36.758 habitantes (+13,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "19.935 · 542 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "885 m", **F.copernicus},
        {"etiqueta": "ITV más cercana", "valor": "A-6 km 37,6 (Collado-Villalba) · 6,5 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Las Rozas) · 14 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 43,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Azuqueca de Henares
CIUDADES["azuqueca-de-henares"] = {
    "h1": "Azuqueca de Henares: servicio oficial BMW en Alcalá y especialista a 40 km",
    "entradilla": "Azuqueca es provincia de Guadalajara, pero lo que tiene que ver con BMW está hacia Madrid: el servicio oficial, en Alcalá de Henares; nuestro taller, en Alcobendas. Te contamos qué te queda cerca y cuándo compensa el viaje.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 40.5},
    "secciones": [
        {"id": "autopremier-alcala", "h2": "AutoPremier, en la Vía Complutense",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial más próximo es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 11,9 km por carretera. Si lo que necesitas es el concesionario, ese es el más próximo.",
         ]},
        {"id": "a2-r2-m50", "h2": "Por la A-2, la R-2 y la M-50 hasta Alcobendas",
         "parrafos": [
             "La ruta desde el centro de Azuqueca hasta la calle Valgrande va por la A-2, sigue por la R-2 y entra por la M-50: 40,5 km por carretera, 32,6 en línea recta. Con la A-2 y la R-2 a menos de tres kilómetros del casco, la salida es inmediata.",
             "Azuqueca queda fuera del área metropolitana de Madrid, así que la recogida del taller no llega hasta aquí: cuenta con traer el coche tú.",
         ]},
        {"id": "cuando-compensa", "h2": "Cuándo tiene sentido el viaje",
         "parrafos": [
             "Para lo que cualquier buen taller resuelve —neumáticos, escobillas, una revisión sencilla—, no. Para un diagnóstico que no ha dado con la causa, una distribución ruidosa, un fallo de inyección o de AdBlue en un diésel, o para hacer el mantenimiento siguiendo el plan de BMW con el reinicio del indicador de servicio, sí.",
             "Antes de mover el coche, una llamada con modelo, año, kilometraje y el síntoma permite saber si el viaje merece la pena y planificar el trabajo para que salga el mismo día cuando es posible.",
         ]},
        {"id": "azuqueca-en-cifras", "h2": "35.924 vecinos en 19,6 km²",
         "parrafos": [
             "El padrón de 2025 da a Azuqueca de Henares 35.924 habitantes, un 2,9 % más que en 2015. El término mide 19,6 km² y el centro está a 634 m de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Azuqueca?",
         "a": "No. El taller de la red que atiende la zona es Dasercars Madrid, en Alcobendas, a 40,5 km."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "AutoPremier, Vía Complutense 131, Alcalá de Henares, a 11,9 km según bmw.es."},
        {"q": "¿Recogéis el coche en Azuqueca?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Madrid."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "35.924 habitantes (+2,9 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "19,6 km²", **F.cartociudad},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier (Alcalá de Henares) · 11,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 40,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Navalcarnero
CIUDADES["navalcarnero"] = {
    "h1": "Navalcarnero: tu BMW a 55 km del especialista y a 20 del servicio oficial",
    "entradilla": "Desde Navalcarnero hasta el taller de Alcobendas hay casi 55 km. Antes de decidir dónde llevar el coche, mira lo que tienes cerca: ITV en el propio municipio y servicio oficial BMW en Alcorcón.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 54.9},
    "secciones": [
        {"id": "itv-alparrache", "h2": "La ITV, en el polígono El Alparrache",
         "parrafos": [
             "El listado de la Comunidad de Madrid incluye una estación en el término: la de TÜV Rheinland Ibérica (2845), en el paseo de Alparrache 26, dentro del polígono industrial El Alparrache. No hace falta salir del municipio para la inspección.",
         ]},
        {"id": "vehinter-alcorcon", "h2": "El servicio oficial, a 20 km en Alcorcón",
         "parrafos": [
             "Según bmw.es, el punto oficial más próximo es Vehinter, en la avenida de San Martín de Valdeiglesias 14-16 de Alcorcón: 20,1 km por carretera. Queda bastante más cerca que nuestro taller, y conviene tenerlo en cuenta.",
         ]},
        {"id": "a5-hasta-alcobendas", "h2": "55 kilómetros cruzando Madrid",
         "parrafos": [
             "La ruta hasta la calle Valgrande sale por la A-5, toma la M-40 y la M-30 y termina en la A-1: 54,9 km por carretera, 41,2 en línea recta. Es un trayecto largo, y no tiene sentido hacerlo para un cambio de aceite si tienes un taller de confianza cerca.",
             "Sí lo tiene para lo que pide un especialista en la marca: una avería que vuelve, un fallo del sistema SCR, una cadena de distribución ruidosa o un diagnóstico que nadie ha cerrado. En esos casos, cuéntanos primero el síntoma por teléfono y valoramos juntos si el viaje merece la pena. La recogida del taller está limitada al área metropolitana y sujeta a disponibilidad: pregunta si Navalcarnero entra.",
         ]},
        {"id": "navalcarnero-crece", "h2": "Un 25 % más de vecinos en diez años",
         "parrafos": [
             "Navalcarnero ha pasado de 26.672 habitantes en 2015 a 33.331 en 2025. Tenía 15.832 turismos censados en 2025, según la Comunidad de Madrid a partir de la DGT: 475 por cada 1.000 vecinos, en un término de 100,4 km².",
             "Con la A-5 y la R-5 a menos de tres kilómetros del centro, un diésel tiene fácil hacer el rato de carretera que necesita el filtro de partículas para limpiarse.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV en Navalcarnero?",
         "a": "En la estación de TÜV Rheinland, paseo de Alparrache 26, polígono El Alparrache."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Vehinter, en Alcorcón, a 20,1 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "54,9 km por la A-5, la M-40, la M-30 y la A-1 hasta Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "33.331 habitantes (+25 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "15.832 · 475 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "TÜV Rheinland, P.º de Alparrache 26", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Alcorcón) · 20,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 54,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
