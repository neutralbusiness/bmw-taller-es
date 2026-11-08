# Tanda 1 (15 ciudades): L'Hospitalet de Llobregat, Santa Coloma de Gramenet, Alcobendas,
# Sant Cugat del Vallès, Rubí, Manresa, Coslada, Granollers, Mollet del Vallès,
# Esplugues de Llobregat, Sant Feliu de Llobregat, Igualada, San Fernando de Henares,
# Montcada i Reixac, Sant Joan Despí.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py tanda_1.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

_DASERCARS_MADRID = {"fuente": "Dasercars Madrid", "url": "https://www.bmw-taller.es/taller-bmw-madrid/"}
_DASERCARS_BCN = {"fuente": "Dasercars Barcelona", "url": "https://www.bmw-taller.es/taller-bmw-barcelona/"}
_NATURAL_EARTH = {"fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["l-hospitalet-de-llobregat"] = {
    "h1": "Taller BMW para L'Hospitalet: Dasercars Barcelona, a 4,1 km en Sant Joan Despí",
    "entradilla": "Con más de 23.000 vecinos por kilómetro cuadrado, en L'Hospitalet el coche se mueve poco y en recorridos cortos. El taller especialista BMW de la red está en el municipio vecino de Sant Joan Despí; aquí tienes la ruta, la ITV, el concesionario de la ciudad y lo que conviene vigilar en un BMW de uso urbano.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 4.1},
    "secciones": [
        {"id": "ciudad-densa", "h2": "289.510 vecinos en 12,4 km²",
         "parrafos": [
             "El padrón de 2025 da a L'Hospitalet de Llobregat 289.510 habitantes, un 14,8 % más que los 252.171 de 2015, en un término de apenas 12,4 km²: 23.348 personas por kilómetro cuadrado. Idescat, con datos de la DGT, contaba 74.343 turismos en 2024, 257 por cada 1.000 habitantes, menos incluso que en Barcelona ciudad (281).",
             "Pocos coches y trayectos cortos tienen una consecuencia mecánica concreta en los diésel: el filtro de partículas necesita temperatura de escape sostenida para regenerarse, y un coche que solo cruza el barrio no la alcanza. Si el aviso del filtro aparece a menudo, borrarlo no sirve; hay que revisar la presión diferencial, el termostato y el historial de regeneraciones que guarda la centralita.",
             "La B-20 y la C-32 pasan a un kilómetro del centro y la C-31 a menos de dos, así que un rato de vía rápida a régimen constante está siempre a mano."
         ]},
        {"id": "ruta-sant-joan-despi", "h2": "Hasta Sant Joan Despí: 3,1 km en línea recta, 4,1 por carretera",
         "parrafos": [
             "La nave de Dasercars Barcelona está en el carrer del Tambor del Bruc 3, en Sant Joan Despí. Desde el centro de L'Hospitalet son 3,1 km en línea recta y 4,1 km por carretera, uno de los recorridos más cortos de toda la red de ciudades.",
             "L'Hospitalet forma parte del Área Metropolitana de Barcelona, de modo que puedes pedir que recojan y devuelvan el coche, o un vehículo de cortesía si el trabajo dura más de un día. Las dos cosas dependen de la disponibilidad de esa semana: plantéalo al reservar, no el mismo día."
         ]},
        {"id": "servicio-oficial-en-la-ciudad", "h2": "Barcelona Premium, el servicio oficial dentro de la ciudad",
         "parrafos": [
             "Según el localizador de bmw.es, L'Hospitalet tiene su propio punto de servicio oficial: Barcelona Premium, en la calle Montserrat Roig 31, a 3,5 km del centro por carretera. Si te ha llegado una carta de BMW por una campaña de revisión, esa cita se pide allí.",
             "Dasercars es otra cosa: un taller independiente que solo trabaja BMW y MINI. El mantenimiento según el plan de la marca, un ruido de cadena en un N47 o un fallo eléctrico que no aparece a la primera son el tipo de trabajo para el que tiene sentido comparar las dos opciones."
         ]},
        {"id": "itv-campsa", "h2": "La ITV, en el passeig de la Campsa de Cornellà",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima al centro de L'Hospitalet es la de Cornellà (B11), que gestiona Applus, en el passeig de la Campsa 64: 0,8 km por carretera. Si el coche pasa antes por el taller para una pre-ITV, la estación queda a un paso tanto de casa como de Sant Joan Despí."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en L'Hospitalet?",
         "a": "No dentro del término. El taller de la red es Dasercars Barcelona, en Sant Joan Despí, a 4,1 km por carretera del centro."},
        {"q": "¿Podéis recoger el coche en L'Hospitalet?",
         "a": "Sí: la ciudad está dentro del área metropolitana. La recogida y entrega está sujeta a disponibilidad."},
        {"q": "¿Por qué se tapona el filtro de partículas en ciudad?",
         "a": "Porque la regeneración necesita temperatura de escape durante un rato y los trayectos cortos no la dan. Si el aviso vuelve aunque el coche salga a vía rápida, hay que buscar la causa."},
        {"q": "¿Dónde está el servicio oficial BMW de L'Hospitalet?",
         "a": "Barcelona Premium, en la calle Montserrat Roig 31, según el localizador de bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "289.510 habitantes (+14,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Barcelonès", **F.idescat("081017")},
        {"etiqueta": "Densidad", "valor": "23.348 hab./km² (12,4 km²)", **F.idescat("081017")},
        {"etiqueta": "Turismos (2024)", "valor": "74.343 · 257 por cada 1.000 hab.", **F.idescat("081017")},
        {"etiqueta": "ITV más cercana", "valor": "Cornellà (B11), pg. de la Campsa 64 · 0,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, c. Montserrat Roig 31 · 3,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 4,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081017"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["santa-coloma-de-gramenet"] = {
    "h1": "BMW en Santa Coloma de Gramenet: especialista a 18,5 km y recogida en el área metropolitana",
    "entradilla": "Nuestro taller de Sant Joan Despí queda en el extremo opuesto del área metropolitana: 18,5 km por la B-20. Por eso, desde Santa Coloma, lo útil es saber qué tienes a dos o tres kilómetros y cuándo merece la pena pedir que vayan a por el coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 18.5},
    "secciones": [
        {"id": "lo-que-queda-cerca", "h2": "Servicio oficial e ITV a menos de tres kilómetros",
         "parrafos": [
             "El punto oficial BMW más cercano en el localizador de bmw.es es Barcelona Premium Ronda Litoral, en la calle Juan de Austria 1 de Sant Adrià de Besòs, a 2,7 km por carretera. La ITV más próxima del registro de la Generalitat ya está en Barcelona: BCN Caracas (B23), de TÜV Rheinland, en el carrer de Caracas 10 B, a 2 km.",
             "Con esas dos referencias tan a mano, para la inspección o para una reparación que paga la garantía de BMW no hace falta cruzar media provincia."
         ]},
        {"id": "rondas-hasta-el-taller", "h2": "Por la B-20 hasta el Baix Llobregat",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona, en el carrer del Tambor del Bruc 3 de Sant Joan Despí, va por la B-20: 18,5 km por carretera, 15,4 en línea recta. Es un recorrido de rondas, con lo que eso supone en hora punta.",
             "Santa Coloma es uno de los municipios del Área Metropolitana de Barcelona, así que el taller puede recoger el coche y devolverlo, y prestar uno de cortesía en trabajos largos, siempre que haya disponibilidad. Para no hacer las rondas dos veces, es la forma razonable de usar un taller que está al otro lado."
         ]},
        {"id": "densidad-santa-coloma", "h2": "17.712 habitantes por kilómetro cuadrado",
         "parrafos": [
             "Santa Coloma tenía 123.981 vecinos en 2025, un 6 % más que en 2015, en solo 7 km² de término. El parque, según Idescat a partir de la DGT, era de 34.470 turismos en 2024: 278 por cada 1.000 habitantes, casi la misma proporción que en Barcelona ciudad (281).",
             "Si tu coche pasa varios días parado entre semana, la batería es lo primero que sufre: un BMW cerrado sigue alimentando alarma, módulos y receptores, y una batería cansada avisa justo la mañana que tienes prisa. Una medición de su estado antes del invierno es barata comparada con una grúa."
         ]},
        {"id": "humedad-salina", "h2": "A 4,2 km de la costa",
         "parrafos": [
             "El centro de Santa Coloma queda a unos 4,2 km de la línea de costa. No es primera línea de mar, pero la humedad salina se nota con los años en anclajes de escape y soportes de los bajos; si el coche se lava poco por debajo, un aclarado con agua dulce al final del verano no sobra."
         ]},
    ],
    "faq": [
        {"q": "¿Podéis recoger el coche en Santa Coloma?",
         "a": "Sí, el municipio está dentro del área metropolitana de Barcelona. Depende de la disponibilidad: pídelo al reservar."},
        {"q": "¿Cuál es la ITV más cercana?",
         "a": "BCN Caracas (B23), en Barcelona, a 2 km por carretera según el registro de la Generalitat."},
        {"q": "¿Sois el concesionario de Sant Adrià?",
         "a": "No. Ese es Barcelona Premium Ronda Litoral. Dasercars es un taller independiente especializado en BMW y MINI, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "123.981 habitantes (+6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Barcelonès", **F.idescat("082457")},
        {"etiqueta": "Turismos (2024)", "valor": "34.470 · 278 por cada 1.000 hab.", **F.idescat("082457")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 4,2 km desde el centro", **_NATURAL_EARTH},
        {"etiqueta": "ITV más cercana", "valor": "BCN Caracas (B23) · 2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium Ronda Litoral (Sant Adrià) · 2,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 18,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082457"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["alcobendas"] = {
    "h1": "Alcobendas: el taller especialista BMW de la red está en el propio municipio",
    "entradilla": "Es de las pocas páginas de la red en la que el taller no queda en otro sitio: Dasercars Madrid tiene su nave en la calle Valgrande 17, dentro del término de Alcobendas. Aquí tienes cómo se trabaja, las cuatro ITV del municipio y dónde está el concesionario más próximo.",
    "socio": {"id": "dasercars-alcobendas"},
    "secciones": [
        {"id": "calle-valgrande", "h2": "Calle Valgrande 17: cómo funciona el taller",
         "parrafos": [
             "Dasercars es un taller independiente especializado en BMW y MINI, con especial dedicación a los diésel N47, N57, M47, M57, B47 y B57 y homologación REDISTA para trabajos de escape y gases. Abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00; el fin de semana está cerrado.",
             "Antes de tocar el coche se entrega un presupuesto por escrito, y no se empieza nada sin que lo apruebes. La diagnosis tampoco se da por supuesta: se presupuesta igual que cualquier otro trabajo.",
             "Al estar en el área metropolitana de Madrid, si no puedes acercarte hay recogida y entrega del coche, y vehículo de cortesía para reparaciones largas, ambos sujetos a disponibilidad."
         ]},
        {"id": "cuatro-itv-alcobendas", "h2": "Cuatro estaciones de ITV en el término",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid recoge cuatro ITV en Alcobendas: Applus Iteuve (estación 2868), en la calle La Maliciosa; TÜV SÜD ATISAE (2814), en la calle Peñalara 29, en el Parque Empresarial Valdelacasa; Itevelesa (2833), en la avenida de Fuencarral 100, y DEKRA (2806), en la avenida de Valdelaparra 1.",
             "Con tantas estaciones en el mismo municipio que el taller, lo lógico es hacer la pre-ITV en la nave y pedir la cita de inspección para esa misma semana."
         ]},
        {"id": "concesionario-las-tablas", "h2": "El concesionario más cercano está en Las Tablas",
         "parrafos": [
             "Según el localizador de bmw.es, el punto de servicio oficial más próximo es BYmyCAR Madrid, en la avenida de Burgos 133 de Madrid, a 7 km por carretera. Las reparaciones que cubre la garantía de BMW se gestionan en la red oficial.",
             "El mantenimiento periódico es otra historia: el Reglamento (UE) 461/2010 permite hacerlo en un taller independiente sin perder la garantía, con dos condiciones, respetar los intervalos y usar recambios y aceites con la especificación del fabricante."
         ]},
        {"id": "turismos-alcobendas", "h2": "332.201 turismos para 123.342 vecinos",
         "parrafos": [
             "El padrón de 2025 da a Alcobendas 123.342 habitantes, un 9,1 % más que en 2015. La cifra de turismos que publica la Comunidad de Madrid a partir de la DGT, 332.201 en 2025, casi triplica la población: no mide los coches de los vecinos, sino que incluye flotas de empresa domiciliadas en el municipio. Por eso no sacamos de ella ninguna proporción.",
             "Lo que sí sirve es la red viaria: la A-1, la M-12, la M-603 y la M-616 pasan a menos de tres kilómetros del centro, y San Sebastián de los Reyes está a 1,5 km, de modo que desde el norte de la región el taller queda prácticamente de camino."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está exactamente el taller?",
         "a": "En la calle Valgrande 17 de Alcobendas (CP 28108)."},
        {"q": "¿Qué ITV hay en Alcobendas?",
         "a": "Cuatro, según la Comunidad de Madrid: Applus Iteuve, TÜV SÜD ATISAE, Itevelesa y DEKRA."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
        {"q": "¿Por qué hay más turismos censados que habitantes?",
         "a": "Porque el censo de la DGT asigna cada vehículo al domicilio de su titular, y en Alcobendas hay flotas de empresa domiciliadas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "123.342 habitantes (+9,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos censados (2025)", "valor": "332.201 (incluye flotas domiciliadas)", **F.cam_parque},
        {"etiqueta": "Estaciones ITV en el municipio", "valor": "4", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid, av. de Burgos 133 · 7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Calle Valgrande 17, en el municipio · 2,5 km del centro", **_DASERCARS_MADRID},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.r461_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["sant-cugat-del-valles"] = {
    "h1": "Sant Cugat: concesionario BMW en la ciudad y especialista independiente a 20,2 km",
    "entradilla": "En línea recta, el taller de Sant Joan Despí está a 11,8 km de Sant Cugat; por carretera, a 20,2. Te explicamos por qué y lo que tienes dentro del municipio: servicio oficial, ITV y recogida del coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 20.2},
    "secciones": [
        {"id": "rodeo-por-carretera", "h2": "11,8 km en línea recta, 20,2 por carretera",
         "parrafos": [
             "Entre Sant Cugat y el Baix Llobregat no hay un camino directo: la ruta que calcula OpenStreetMap baja por la C-16 y enlaza con la B-20 hasta el carrer del Tambor del Bruc. Son 20,2 km, un 71 % más que la distancia en línea recta.",
             "Sant Cugat es uno de los municipios del Área Metropolitana de Barcelona, así que entra en la zona de recogida y entrega del taller y en la de vehículo de cortesía, siempre sujetos a disponibilidad. Con un trayecto así, merece la pena pedirlo."
         ]},
        {"id": "quadis-vallespir", "h2": "Quadis Munich, en el carrer Vallespir",
         "parrafos": [
             "El localizador de bmw.es sitúa en la ciudad un punto de servicio oficial: Quadis Munich, en el carrer Vallespir 19, a 2,3 km del centro. Para una reparación en garantía o una campaña del fabricante, es tu sitio.",
             "Para lo demás —un mantenimiento por plan con el aceite de la especificación correcta, un fallo intermitente que nadie ha localizado, un segundo diagnóstico antes de aceptar una reparación cara— puedes comparar con un taller independiente que solo trabaja BMW y MINI."
         ]},
        {"id": "itv-sant-mamet", "h2": "ITV propia en el polígono Sant Mamet",
         "parrafos": [
             "La estación de Sant Cugat (B22), de TÜV Rheinland, está en el carrer d'Amposta 2, en el polígono industrial Sant Mamet, dentro del término municipal según el registro de la Generalitat. Es también la más próxima para los conductores de Rubí."
         ]},
        {"id": "sant-cugat-crece", "h2": "97.983 vecinos y 40.087 turismos",
         "parrafos": [
             "Sant Cugat ha pasado de 87.830 habitantes en 2015 a 97.983 en 2025, un 11,6 % más, en un término de 48,23 km². Idescat, con datos de la DGT, contaba 40.087 turismos en 2024: 409 por cada 1.000 habitantes.",
             "Con la C-16, la AP-7 y la B-30 a menos de tres kilómetros del centro, un coche de Sant Cugat hace autopista con facilidad. Eso favorece al filtro de partículas, pero no exime de lo que se cambia por tiempo: el líquido de frenos y el aceite tienen fecha además de kilómetros."
         ]},
    ],
    "faq": [
        {"q": "¿Por qué hay tanta diferencia entre línea recta y carretera?",
         "a": "Porque no hay vía directa entre Sant Cugat y Sant Joan Despí: la ruta rodea por la C-16 y la B-20."},
        {"q": "¿Recogéis el coche en Sant Cugat?",
         "a": "Sí, está dentro del área metropolitana. Depende de la disponibilidad de ese día."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación B22 del polígono Sant Mamet, en el carrer d'Amposta 2."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "97.983 habitantes (+11,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082055")},
        {"etiqueta": "Turismos (2024)", "valor": "40.087 · 409 por cada 1.000 hab.", **F.idescat("082055")},
        {"etiqueta": "ITV en el municipio", "valor": "Sant Cugat (B22), polígono Sant Mamet", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, c. Vallespir 19 · 2,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 20,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082055"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["rubi"] = {
    "h1": "Rubí: tu BMW a 20,9 km del taller especialista, fuera del área metropolitana por poco",
    "entradilla": "Castellbisbal, Sant Cugat y el Papiol, a menos de seis kilómetros, están en el Área Metropolitana de Barcelona; Rubí no. Para el dueño de un BMW o un MINI eso cambia una cosa concreta, la recogida del coche. Lo demás queda bastante a mano.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 20.9},
    "secciones": [
        {"id": "sin-recogida", "h2": "Por qué no hay recogida en Rubí",
         "parrafos": [
             "La recogida y entrega de Dasercars Barcelona, igual que el vehículo de cortesía, solo cubre el área metropolitana, y Rubí queda fuera aunque sus vecinos más cercanos estén dentro. No es cuestión de kilómetros: el taller está a 20,9 km por carretera, prácticamente lo mismo que desde Sant Cugat (20,2), que sí entra.",
             "En la práctica, el coche lo traes tú. La ruta va por la B-30, un tramo de la AP-7 y la B-23 hasta el carrer del Tambor del Bruc 3, en Sant Joan Despí; en línea recta son 14,3 km."
         ]},
        {"id": "todo-en-sant-cugat", "h2": "ITV y servicio oficial, los dos en Sant Cugat",
         "parrafos": [
             "Lo oficial que tienes más cerca está en el municipio vecino. La estación de ITV más próxima en el registro de la Generalitat es la de Sant Cugat (B22), en el polígono Sant Mamet, a 3,4 km por carretera. El punto de servicio oficial BMW más cercano según bmw.es, Quadis Munich, en el carrer Vallespir 19 de Sant Cugat, queda a 3,8 km.",
             "Si el coche aún está en garantía, la normativa europea de competencia permite hacer el mantenimiento fuera de la red oficial mientras se respeten intervalos y especificaciones; lo que debe pasar por el concesionario es la reparación que pagaría BMW."
         ]},
        {"id": "organizar-la-visita", "h2": "Cómo organizar la visita",
         "parrafos": [
             "Llama con modelo, año, kilometraje y el síntoma bien descrito: si hay un testigo encendido, cuál y desde cuándo. Con eso se puede saber si el trabajo cabe en una jornada y si conviene pedir la pieza antes de que llegues.",
             "El taller trabaja de lunes a viernes, por la mañana y por la tarde. Para trabajos de un día, lo que mejor funciona desde Rubí es entrar a primera hora."
         ]},
        {"id": "rubi-en-cifras", "h2": "82.823 vecinos, 36.053 turismos",
         "parrafos": [
             "El padrón de 2025 da a Rubí 82.823 habitantes, un 11,1 % más que diez años antes, en un término de 32,3 km². En 2024 tenía 36.053 turismos según Idescat a partir de la DGT, 435 por cada 1.000 vecinos. Tres vías rápidas, la C-16, la AP-7 y la B-30, quedan a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Rubí?",
         "a": "No. La recogida cubre solo el área metropolitana de Barcelona, y Rubí queda fuera."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de Sant Cugat (B22), en el polígono Sant Mamet, a 3,4 km por carretera."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 20,9 km por la B-30, la AP-7 y la B-23, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "82.823 habitantes (+11,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("081846")},
        {"etiqueta": "Turismos (2024)", "valor": "36.053 · 435 por cada 1.000 hab.", **F.idescat("081846")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Cugat (B22) · 3,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Cugat) · 3,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 20,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081846"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["manresa"] = {
    "h1": "Manresa: servicio oficial BMW a 6,9 km y taller especialista a 60 km por la C-16",
    "entradilla": "En la capital del Bages tienes ITV propia y el concesionario BMW en Sant Fruitós, a menos de siete kilómetros. Nuestro taller está a 59,7 km, en Sant Joan Despí. Esta página va de cómo repartir los trabajos entre lo de cerca y lo de lejos.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 59.7},
    "secciones": [
        {"id": "repartir-trabajos", "h2": "Qué conviene hacer en el Bages y qué en Sant Joan Despí",
         "parrafos": [
             "La inspección, los neumáticos, un cambio de pastillas o una revisión que solo necesita el aceite de la especificación correcta se resuelven en Manresa sin perder un día de carretera. El punto oficial BMW más próximo según el localizador de bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 6,9 km; es donde se tramitan las reparaciones en garantía.",
             "La bajada al Baix Llobregat tiene sentido para lo que pide un especialista de la marca: una avería en un diésel de las familias N47, N57, B47 o B57, una modificación de escape que hay que homologar —el taller tiene homologación REDISTA para escape y gases— o un fallo electrónico que ya ha pasado por otros talleres sin solución."
         ]},
        {"id": "c16-hacia-el-taller", "h2": "59,7 km por la C-16 y la B-20",
         "parrafos": [
             "Desde el centro de Manresa hasta el carrer del Tambor del Bruc, la ruta usa la C-16 y la B-20: 59,7 km por carretera, 44,9 en línea recta. Manresa no está en el área metropolitana, así que la recogida del taller no llega hasta aquí.",
             "Para que el viaje no sea en balde, describe el síntoma por teléfono, ten a mano el número de bastidor y, si el coche guarda avisos, di cuáles. Con eso la pieza puede estar pedida el día que llegas."
         ]},
        {"id": "itv-manresa-b06", "h2": "La ITV de Manresa, en Bufalvent",
         "parrafos": [
             "La estación de Manresa (B06), de TÜV Rheinland, está en el carrer d'Esteve Terrades 2-4, en el polígono industrial Bufalvent, dentro del término municipal según el registro de la Generalitat."
         ]},
        {"id": "manresa-en-cifras", "h2": "80.974 vecinos a 238 metros",
         "parrafos": [
             "Manresa tenía 80.974 habitantes en 2025, un 8,5 % más que en 2015, y 36.690 turismos en 2024 según Idescat a partir de la DGT: 453 por cada 1.000 habitantes. El centro está a 238 metros de altitud, y la C-25, la C-55 y la C-16C pasan a menos de tres kilómetros."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Manresa?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 59,7 km."},
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "Quadis Munich, en la carretera de Manresa a Berga, km 34,5 (Sant Fruitós de Bages), a 6,9 km según bmw.es."},
        {"q": "¿Homologáis cambios de escape?",
         "a": "El taller cuenta con homologación REDISTA para trabajos de escape y gases. Consulta tu caso por teléfono antes de bajar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "80.974 habitantes (+8,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("081136")},
        {"etiqueta": "Turismos (2024)", "valor": "36.690 · 453 por cada 1.000 hab.", **F.idescat("081136")},
        {"etiqueta": "ITV en el municipio", "valor": "Manresa (B06), polígono Bufalvent", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 6,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 59,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081136"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["coslada"] = {
    "h1": "Coslada: tres ITV en el municipio y taller BMW en Alcobendas por la M-40",
    "entradilla": "En Coslada vive hoy un 7,4 % menos de gente que en 2015, pero el municipio sigue teniendo tres estaciones de ITV y 42.062 turismos censados. El taller especialista que lo atiende está en Alcobendas, a 19,5 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 19.5},
    "secciones": [
        {"id": "tres-itv-coslada", "h2": "Tres estaciones de ITV dentro de Coslada",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid incluye tres estaciones en el municipio: Itevelesa (estación 2880), en la avenida de la Constitución 4; General de Servicios ITV (2851), en la avenida de San Pablo 29, y TÜV SÜD ATISAE (2815), en la calle Alcarria 2.",
             "Para un término de 12 km² es mucha oferta, y permite pedir cita casi sin mirar el calendario."
         ]},
        {"id": "m40-a1", "h2": "Hacia Alcobendas por la M-40 y la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 de Alcobendas sube por la M-40 y la A-1: 19,5 km por carretera, 14,7 en línea recta. Coslada está dentro del área metropolitana de Madrid, de modo que, si no puedes llevar el coche, el taller ofrece recogida y entrega sujeta a disponibilidad, igual que el vehículo de cortesía en trabajos de varios días."
         ]},
        {"id": "caetano-alcala", "h2": "Dos concesionarios a 8,4 km, en Madrid",
         "parrafos": [
             "Según el localizador de bmw.es, los dos puntos de servicio oficial más cercanos están en Madrid y a la misma distancia, 8,4 km por carretera: Caetano Cuzco, en la calle de Alcalá 474, y AutoPremier, en la carretera de Valencia, km 7,3. Son la dirección para una reparación cubierta por la garantía del fabricante.",
             "Un taller independiente no compite con eso, sino con el mantenimiento y las averías fuera de garantía. En Dasercars cada trabajo arranca con un presupuesto escrito que tienes que aprobar, y la diagnosis se presupuesta aparte."
         ]},
        {"id": "coslada-en-cifras", "h2": "522 turismos por cada 1.000 habitantes",
         "parrafos": [
             "Coslada tenía 86.919 habitantes en 2015 y 80.512 en 2025. Los 42.062 turismos censados en 2025, según la Comunidad de Madrid a partir de la DGT, salen a 522 por cada 1.000 vecinos, frente a 388 en Madrid capital.",
             "La A-2, la R-3, la M-21, la M-22 y la M-45 pasan a menos de tres kilómetros del centro. Un municipio tan rodeado de vías rápidas es buen sitio para un diésel; lo que más castiga aquí a un coche son los atascos de entrada a Madrid, con embrague y frenos trabajando a ratos."
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV hay en Coslada?",
         "a": "Tres, según la Comunidad de Madrid: Itevelesa (avenida de la Constitución 4), General de Servicios ITV (avenida de San Pablo 29) y TÜV SÜD ATISAE (calle Alcarria 2)."},
        {"q": "¿Recogéis el coche en Coslada?",
         "a": "Sí, Coslada está en el área metropolitana de Madrid. La recogida está sujeta a disponibilidad."},
        {"q": "¿Cuánto hay hasta el taller?",
         "a": "19,5 km por la M-40 y la A-1, hasta la calle Valgrande 17 de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "80.512 habitantes (−7,4 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "42.062 · 522 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Estaciones ITV en el municipio", "valor": "3", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Caetano Cuzco o AutoPremier (Madrid) · 8,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 19,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["granollers"] = {
    "h1": "Granollers: concesionario BMW en la C-17 y especialista independiente a 38,9 km",
    "entradilla": "Si vives en Granollers, el concesionario BMW está en la propia ciudad y la ITV, en el polígono El Congost. Nuestro taller, en Sant Joan Despí, queda a 38,9 km. Cuándo encaja cada cosa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 38.9},
    "secciones": [
        {"id": "pruna-motor", "h2": "Pruna Motor, en la carretera C-17",
         "parrafos": [
             "El localizador de bmw.es sitúa en Granollers un servicio oficial BMW: Pruna Motor, en la carretera C-17, km 19,060, a 4,9 km del centro por carretera. Es también el más próximo para Mollet del Vallès.",
             "Un taller independiente encaja en lo que no depende de la marca: el mantenimiento por plan, las averías fuera de garantía, la puesta a punto antes de un viaje largo. La garantía no se pierde por hacer el mantenimiento fuera si se respetan intervalos y especificaciones (Reglamento UE 461/2010)."
         ]},
        {"id": "c17-c33-b20", "h2": "38,9 km por la C-17, la C-33 y la B-20",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona baja por la C-17 y la C-33 y sigue por la B-20: 38,9 km por carretera y 32,8 en línea recta. Granollers no está en el área metropolitana, así que la recogida del taller no llega hasta aquí: el coche lo traes tú.",
             "Con esa distancia, organiza el día: el taller abre de lunes a viernes en jornada partida, y lo razonable es entrar a primera hora con el trabajo ya hablado por teléfono."
         ]},
        {"id": "itv-congost", "h2": "ITV en el polígono El Congost",
         "parrafos": [
             "La estación de Granollers (B18), gestionada por Applus, está en la avinguda de Sant Julià 253-255, en el polígono industrial El Congost, dentro del municipio según el registro de la Generalitat."
         ]},
        {"id": "granollers-en-cifras", "h2": "65.341 vecinos en 14,87 km²",
         "parrafos": [
             "Granollers tenía 65.341 habitantes en 2025, un 8,7 % más que en 2015. Idescat, con datos de la DGT, contaba 29.424 turismos en 2024, 450 por cada 1.000 habitantes. Alrededor del centro se cruzan la AP-7, la C-17, la C-352 y la C-155, todas a menos de tres kilómetros."
         ]},
    ],
    "faq": [
        {"q": "¿Sois Pruna Motor?",
         "a": "No. Pruna Motor es el servicio oficial BMW de Granollers. Nosotros somos Dasercars, taller independiente en Sant Joan Despí."},
        {"q": "¿Recogéis el coche en Granollers?",
         "a": "No: la recogida solo cubre el área metropolitana de Barcelona."},
        {"q": "¿Dónde está la ITV de Granollers?",
         "a": "En la avinguda de Sant Julià 253-255, polígono El Congost (estación B18)."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "65.341 habitantes (+8,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080961")},
        {"etiqueta": "Turismos (2024)", "valor": "29.424 · 450 por cada 1.000 hab.", **F.idescat("080961")},
        {"etiqueta": "ITV en el municipio", "valor": "Granollers (B18), polígono El Congost", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, ctra. C-17 km 19,060 · 4,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 38,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080961"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["mollet-del-valles"] = {
    "h1": "Mollet del Vallès: ITV a 3,4 km, concesionario en Granollers y taller BMW a 29,1 km",
    "entradilla": "Tres referencias para el dueño de un BMW o un MINI en Mollet: la ITV de Santa Perpètua, a 3,4 km; el concesionario de Granollers, a 7,8; y nuestro taller de Sant Joan Despí, a 29,1 km por la C-33.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 29.1},
    "secciones": [
        {"id": "itv-cim-valles", "h2": "La ITV del CIM Vallès, en Santa Perpètua de Mogoda",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima al centro de Mollet es la de CIM Vallès (B20), de TÜV Rheinland, en el carrer del Pont Vell, dentro del Centre Integral de Mercaderies del polígono Les Minetes de Santa Perpètua de Mogoda: 3,4 km por carretera."
         ]},
        {"id": "c33-sant-joan", "h2": "Por la C-33 y la B-20 hasta el Baix Llobregat",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona va por la C-33 y la B-20: 29,1 km por carretera, 23 en línea recta. Mollet no es uno de los municipios del Área Metropolitana de Barcelona, así que la recogida del coche que ofrece el taller no llega.",
             "Lo que más ahorra un viaje en balde es explicar bien el problema: cuándo aparece, si hay un testigo encendido y desde cuándo. Con el bastidor, además, se confirma la referencia exacta de la pieza."
         ]},
        {"id": "pruna-granollers", "h2": "El servicio oficial, a 7,8 km en Granollers",
         "parrafos": [
             "El punto oficial BMW más cercano según bmw.es es Pruna Motor, en la carretera C-17, km 19,060, en Granollers, a 7,8 km. Es la referencia para reparaciones en garantía y para las campañas que convoque la marca."
         ]},
        {"id": "mollet-en-cifras", "h2": "52.990 vecinos y 23.471 turismos",
         "parrafos": [
             "El padrón de 2025 da a Mollet 52.990 habitantes, un 2,6 % más que en 2015; el municipio ocupa 10,77 km². En 2024 tenía 23.471 turismos según Idescat a partir de la DGT, 443 por cada 1.000 habitantes.",
             "La AP-7, la C-17, la C-33 y la C-59 pasan a menos de tres kilómetros del centro. Si el coche hace a diario autopista, el desgaste se concentra en neumáticos y en la pastilla delantera; si solo se mueve por el casco urbano, en la batería."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Mollet?",
         "a": "La más próxima en el registro de la Generalitat es la de CIM Vallès (B20), en Santa Perpètua de Mogoda, a 3,4 km."},
        {"q": "¿Hay recogida en Mollet?",
         "a": "No, la recogida cubre solo el área metropolitana de Barcelona."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "29,1 km por la C-33 y la B-20, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "52.990 habitantes (+2,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("081249")},
        {"etiqueta": "Turismos (2024)", "valor": "23.471 · 443 por cada 1.000 hab.", **F.idescat("081249")},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20), Santa Perpètua · 3,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Granollers) · 7,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 29,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081249"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["esplugues-de-llobregat"] = {
    "h1": "Esplugues de Llobregat: a 3,3 km del taller especialista BMW de Sant Joan Despí",
    "entradilla": "Entre Esplugues y la nave de Dasercars Barcelona hay 2,4 km en línea recta. Con tan poca distancia, lo que más te interesa de esta página es otra cosa: cómo dejar el coche sin perder la mañana y qué tienes alrededor.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 3.3},
    "secciones": [
        {"id": "por-la-c245", "h2": "Por la C-245 hasta el Tambor del Bruc",
         "parrafos": [
             "La ruta por carretera hasta el carrer del Tambor del Bruc 3 de Sant Joan Despí es de 3,3 km y usa la C-245. Esplugues pertenece al Área Metropolitana de Barcelona, y el taller ofrece dentro de ella recogida y entrega del coche y vehículo de cortesía, ambos sujetos a disponibilidad.",
             "Con el taller tan cerca, muchas veces lo práctico es dejarlo de camino al trabajo y recogerlo al volver; si la reparación se alarga, pregunta por el coche de cortesía al reservar."
         ]},
        {"id": "itv-sant-just", "h2": "La ITV, en el polígono de Sant Just Desvern",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima al centro de Esplugues es la de Sant Just Desvern (B05), de Applus, en la avinguda de la Riera 19-21 del polígono industrial núm. 1, a 2,7 km por carretera. La de Cornellà (B11) queda casi igual, a 3,5."
         ]},
        {"id": "termino-pequeno", "h2": "48.221 vecinos en 4,6 km²",
         "parrafos": [
             "Esplugues tenía 48.221 vecinos en 2025, un 5,7 % más que en 2015, en un término de solo 4,6 km²: 10.483 habitantes por kilómetro cuadrado. Idescat, a partir de la DGT, contaba 16.965 turismos en 2024, 352 por cada 1.000 habitantes.",
             "En un término tan pequeño, muchos desplazamientos del día a día no pasan de unos pocos kilómetros. Es el uso que peor llevan las baterías de los BMW con arranque y parada automático: el alternador no llega a reponer lo que gasta cada arranque. Si cambias la batería, hay que registrarla en la centralita para que la carga se ajuste a la nueva."
         ]},
        {"id": "oficial-hospitalet", "h2": "El servicio oficial más cercano, en L'Hospitalet",
         "parrafos": [
             "En el localizador de bmw.es, el punto oficial más próximo a Esplugues es Barcelona Premium, en el carrer Montserrat Roig 31 de L'Hospitalet de Llobregat, a 5,9 km por la ruta más corta (unos 9 por la más rápida). Es la referencia para lo que cubre la garantía de BMW."
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Esplugues?",
         "a": "Sí. Esplugues está en el área metropolitana de Barcelona; la recogida está sujeta a disponibilidad."},
        {"q": "¿Por qué hay que registrar la batería nueva de un BMW?",
         "a": "Porque la centralita adapta la carga a la batería que tiene registrada. Si no se registra, la nueva se carga mal y dura menos."},
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Sant Just Desvern (B05), en la avinguda de la Riera, a 2,7 km según la Generalitat; la de Cornellà (B11), a 3,5."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "48.221 habitantes (+5,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080771")},
        {"etiqueta": "Turismos (2024)", "valor": "16.965 · 352 por cada 1.000 hab.", **F.idescat("080771")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 2,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (L'Hospitalet) · 5,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 3,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080771"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["sant-feliu-de-llobregat"] = {
    "h1": "Sant Feliu de Llobregat: el taller BMW de la red, a 2,8 km por carretera",
    "entradilla": "La capital del Baix Llobregat linda con Sant Joan Despí, y el taller de la red queda a 2,2 km en línea recta y 2,8 por carretera. Con esa cercanía, lo que importa es cómo organizarte y qué más tienes alrededor.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 2.8},
    "secciones": [
        {"id": "kilometros-justos", "h2": "Casi tres kilómetros hasta el carrer del Tambor del Bruc",
         "parrafos": [
             "Desde el centro de Sant Feliu hasta la nave de Dasercars Barcelona hay 2,8 km por carretera. Es una distancia que permite dejar el coche por la mañana, volver andando o en transporte público y recogerlo por la tarde.",
             "Si prefieres no moverte, Sant Feliu está dentro del Área Metropolitana de Barcelona y el taller puede recoger y devolver el coche; también hay vehículo de cortesía para reparaciones largas. Ambas cosas, sujetas a disponibilidad."
         ]},
        {"id": "itv-a-1-3-km", "h2": "La ITV de Sant Just, a 1,3 km",
         "parrafos": [
             "La estación más próxima en el registro de la Generalitat es la de Sant Just Desvern (B05), en la avinguda de la Riera 19-21, a 1,3 km del centro de Sant Feliu. Con taller e ITV tan juntos, la pre-ITV y la inspección caben en el mismo día si pides las dos citas con margen."
         ]},
        {"id": "concesionario-sant-boi", "h2": "El concesionario, en la carretera del Prat de Sant Boi",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más cercano es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 7,6 km. Desde Sant Feliu el concesionario queda casi tres veces más lejos que el taller independiente, al revés de lo que pasa en casi toda la red."
         ]},
        {"id": "sant-feliu-en-cifras", "h2": "46.781 vecinos y 17.738 turismos",
         "parrafos": [
             "Sant Feliu tenía 46.781 habitantes en 2025, un 6,8 % más que en 2015, en 11,82 km². En 2024 había 17.738 turismos censados según Idescat a partir de la DGT, 379 por cada 1.000 habitantes. La N-340, la A-2 y la B-23 pasan a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿A qué distancia está el taller?",
         "a": "A 2,8 km por carretera, en el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
        {"q": "¿Recogéis el coche en Sant Feliu?",
         "a": "Sí, sujeto a disponibilidad: Sant Feliu está en el área metropolitana de Barcelona."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI comparte con BMW motores y electrónica, y se trabaja con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "46.781 habitantes (+6,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082114")},
        {"etiqueta": "Turismos (2024)", "valor": "17.738 · 379 por cada 1.000 hab.", **F.idescat("082114")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 1,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 7,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 2,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082114"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["igualada"] = {
    "h1": "Igualada: tu BMW, la A-2 y un taller especialista a 55 km",
    "entradilla": "Desde la capital de l'Anoia, todo lo relacionado con BMW queda a más de 40 km: el servicio oficial más cercano está en el Bages y nuestro taller, en Sant Joan Despí. Cuando todo queda lejos, el teléfono es la primera herramienta.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 55.2},
    "secciones": [
        {"id": "dos-opciones-lejos", "h2": "Servicio oficial a 40,7 km, taller especialista a 55,2",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo a Igualada es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 40,7 km. El taller de la red, Dasercars Barcelona, está a 55,2 km, en el carrer del Tambor del Bruc 3 de Sant Joan Despí.",
             "Con las dos opciones a esa distancia, lo cotidiano —neumáticos, pastillas, un cambio de aceite con la especificación que pide tu motor— conviene resolverlo en Igualada. El viaje se reserva para lo que de verdad pide un especialista en la marca."
         ]},
        {"id": "una-sola-autovia", "h2": "Una sola autovía: la A-2",
         "parrafos": [
             "La ruta hasta el taller es la A-2 casi de principio a fin: 55,2 km por carretera, 44,2 en línea recta. Igualada queda fuera del área metropolitana, así que la recogida del taller no llega; cuenta con traer el coche.",
             "Antes de salir, pide el presupuesto por escrito: en Dasercars no se empieza ningún trabajo sin que lo hayas aprobado, y así sabes antes de hacer los kilómetros qué te vas a encontrar."
         ]},
        {"id": "itv-les-comes", "h2": "La ITV, en el polígono Les Comes",
         "parrafos": [
             "La estación de Igualada (B12), de Applus, está en el carrer dels Països Baixos 18, en el polígono industrial Les Comes, dentro del término municipal según el registro de la Generalitat. La inspección, por tanto, no necesita ningún desplazamiento."
         ]},
        {"id": "igualada-en-cifras", "h2": "42.085 vecinos en 8,11 km²",
         "parrafos": [
             "Igualada tenía 42.085 habitantes en 2025, un 8,6 % más que en 2015, con 5.189 personas por kilómetro cuadrado. Los 20.375 turismos de 2024 (Idescat, a partir de la DGT) salen a 484 por cada 1.000 habitantes. La A-2 y la C-37 pasan a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Igualada?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 40,7 km según bmw.es."},
        {"q": "¿Recogéis el coche en Igualada?",
         "a": "No, la recogida solo cubre el área metropolitana de Barcelona."},
        {"q": "¿Merece la pena ir hasta Sant Joan Despí?",
         "a": "Para una avería específica de BMW sin resolver, un diésel N47 o N57 o una homologación de escape, sí; para el mantenimiento básico, mejor un taller de la comarca."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "42.085 habitantes (+8,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("081022")},
        {"etiqueta": "Turismos (2024)", "valor": "20.375 · 484 por cada 1.000 hab.", **F.idescat("081022")},
        {"etiqueta": "ITV en el municipio", "valor": "Igualada (B12), polígono Les Comes", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 40,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 55,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081022"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["san-fernando-de-henares"] = {
    "h1": "San Fernando de Henares: ITV en la calle Tapiceros y taller BMW a 21,5 km",
    "entradilla": "Un término de 38,7 km² con seis vías rápidas a menos de tres kilómetros del centro y una estación de ITV propia. El taller especialista que lo atiende está en Alcobendas; aquí van la ruta y lo que tienes más cerca.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 21.5},
    "secciones": [
        {"id": "itv-tapiceros", "h2": "ITV Jarama, en la calle Tapiceros",
         "parrafos": [
             "El listado de la Comunidad de Madrid incluye una estación de ITV en el municipio: ITV Jarama (estación 2881), en la calle Tapiceros 2. Para un coche de San Fernando, es la opción sin desplazamiento."
         ]},
        {"id": "seis-vias", "h2": "A-2, M-45, M-50: carreteras para elegir",
         "parrafos": [
             "A menos de tres kilómetros del centro pasan la A-2, la M-21, la M-22, la M-45, la M-50 y la M-206. La ruta hacia la calle Valgrande 17 de Alcobendas usa la M-21, la M-40 y la A-1: 21,5 km por carretera, 16,1 en línea recta.",
             "San Fernando está en el área metropolitana de Madrid, así que el taller puede recoger el coche y devolverlo, o dejarte uno de cortesía si la reparación se alarga, siempre según disponibilidad."
         ]},
        {"id": "oficial-11-km", "h2": "El servicio oficial, a unos 11 km en Madrid",
         "parrafos": [
             "Según el localizador de bmw.es, los dos puntos oficiales BMW más próximos están en Madrid y casi a la par: AutoPremier, en la carretera de Valencia, km 7,3, a 11 km, y Caetano Cuzco, en la calle de Alcalá 474, a 11,1. Para el mantenimiento por plan o una avería fuera de garantía, la alternativa es un especialista independiente como Dasercars, que solo trabaja BMW y MINI."
         ]},
        {"id": "poblacion-san-fernando", "h2": "Algo menos de población que hace diez años",
         "parrafos": [
             "San Fernando de Henares tenía 40.188 habitantes en 2015 y 39.059 en 2025, un 2,8 % menos. En 2025 tenía 21.285 turismos censados según la Comunidad de Madrid a partir de la DGT: 545 por cada 1.000 habitantes, una proporción parecida a la de su vecina Coslada (522).",
             "Si el coche se mueve poco entre semana, recuerda que hay mantenimiento que caduca aunque no se hagan kilómetros: el líquido de frenos absorbe humedad con el tiempo y el aceite envejece en el cárter. El indicador de servicio del BMW cuenta las dos cosas, fecha y distancia."
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en San Fernando de Henares?",
         "a": "Sí: ITV Jarama, en la calle Tapiceros 2, según la Comunidad de Madrid."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "21,5 km por la M-21, la M-40 y la A-1, hasta Alcobendas."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "Sí, dentro del área metropolitana de Madrid y sujeto a disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "39.059 habitantes (−2,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "21.285 · 545 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "ITV Jarama, c. Tapiceros 2", **F.itv_madrid},
        {"etiqueta": "Superficie del término", "valor": "38,7 km²", **F.cartociudad},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier o Caetano Cuzco (Madrid) · 11 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 21,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["montcada-i-reixac"] = {
    "h1": "Montcada i Reixac: BMW entre la C-17 y la C-58, a 20,7 km del taller",
    "entradilla": "Montcada i Reixac está dentro del Área Metropolitana de Barcelona, pero en el lado contrario al de nuestro taller. Lo que eso supone para el dueño de un BMW o un MINI: la ruta, la recogida y lo que tienes más cerca.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 20.7},
    "secciones": [
        {"id": "otro-lado-del-amb", "h2": "Al otro lado del área metropolitana",
         "parrafos": [
             "Desde el centro de Montcada hasta el carrer del Tambor del Bruc 3 de Sant Joan Despí, la ruta usa la C-17 y la B-20: 20,7 km por carretera, 16,4 en línea recta.",
             "Como el municipio forma parte del Área Metropolitana de Barcelona, puedes pedir que el taller recoja el coche y lo devuelva terminado, y un vehículo de cortesía para trabajos largos. Las dos cosas dependen de la disponibilidad, así que conviene pedirlas al cerrar la cita."
         ]},
        {"id": "oficial-sant-adria", "h2": "El concesionario más cercano, en Sant Adrià de Besòs",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo es Barcelona Premium Ronda Litoral, en la calle Juan de Austria 1 de Sant Adrià de Besòs, a 9,3 km. Las reparaciones que paga la garantía de BMW se hacen allí."
         ]},
        {"id": "itv-cim-caracas", "h2": "Dos ITV casi a la par: Santa Perpètua y Barcelona",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, las dos más cercanas por carretera al centro de Montcada quedan casi a la par: CIM Vallès (B20), en el polígono Les Minetes de Santa Perpètua de Mogoda, a 7,3 km, y BCN Caracas (B23), en el carrer de Caracas 10 B de Barcelona, a 7,9."
         ]},
        {"id": "montcada-en-cifras", "h2": "37.460 vecinos en 23,47 km²",
         "parrafos": [
             "Montcada tenía 37.460 habitantes en 2025, un 9 % más que en 2015. El parque de 2024 era de 17.869 turismos según Idescat a partir de la DGT: 477 por cada 1.000 habitantes, bastantes más que en Santa Coloma de Gramenet (278), a 4,1 km.",
             "Por el término pasan la C-17, la C-33, la C-58 y la B-10, todas a menos de tres kilómetros del centro. Un turbo que trabaja a menudo en autopista agradece un gesto sencillo: no apagar el motor nada más parar después de un tramo exigente, para que el aceite siga refrigerando el eje unos segundos."
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Montcada?",
         "a": "Sí, Montcada está en el área metropolitana de Barcelona. Sujeto a disponibilidad."},
        {"q": "¿Qué ITV tengo más cerca?",
         "a": "CIM Vallès (B20), en Santa Perpètua de Mogoda, a 7,3 km, o BCN Caracas (B23), en Barcelona, a 7,9, según la Generalitat."},
        {"q": "¿A cuánto está el taller?",
         "a": "A 20,7 km por la C-17 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "37.460 habitantes (+9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("081252")},
        {"etiqueta": "Turismos (2024)", "valor": "17.869 · 477 por cada 1.000 hab.", **F.idescat("081252")},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20) · 7,3 km; BCN Caracas (B23) · 7,9", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium Ronda Litoral (Sant Adrià) · 9,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 20,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081252"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["sant-joan-despi"] = {
    "h1": "Sant Joan Despí: el especialista BMW y MINI de la red, en el carrer del Tambor del Bruc",
    "entradilla": "Aquí no hay ruta que explicar: Dasercars Barcelona tiene su nave en el carrer del Tambor del Bruc 3, dentro de Sant Joan Despí. Esta página cuenta cómo trabaja el taller y qué más conviene tener a mano si vives en el municipio.",
    "socio": {"id": "dasercars-sant-joan-despi"},
    "secciones": [
        {"id": "que-se-hace", "h2": "Qué se hace en la nave del Tambor del Bruc",
         "parrafos": [
             "Dasercars Barcelona es un taller independiente dedicado a BMW y MINI: mantenimiento según el plan del fabricante, diagnosis electrónica, mecánica de motor —con especial dedicación a los diésel N47, N57, M47, M57, B47 y B57— y trabajos de escape y gases con homologación REDISTA.",
             "La diagnosis se presupuesta como un trabajo más. El taller abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00, y cierra sábados y domingos."
         ]},
        {"id": "recogida-sant-joan", "h2": "Recogida y coche de cortesía dentro del área metropolitana",
         "parrafos": [
             "Sant Joan Despí forma parte del Área Metropolitana de Barcelona. Si no puedes acercar el coche aunque el taller esté en el mismo municipio, hay recogida y entrega, y vehículo de cortesía para reparaciones de más de un día, ambos sujetos a disponibilidad."
         ]},
        {"id": "itv-y-concesionario", "h2": "ITV en Sant Just, concesionario en Sant Boi",
         "parrafos": [
             "La estación de ITV más próxima en el registro de la Generalitat es la de Sant Just Desvern (B05), en la avinguda de la Riera 19-21, a 3,5 km. El punto de servicio oficial BMW más cercano según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 5,5 km: allí se hacen las reparaciones cubiertas por la garantía de la marca."
         ]},
        {"id": "sant-joan-en-cifras", "h2": "35.926 vecinos en 6,17 km²",
         "parrafos": [
             "Sant Joan Despí tenía 35.926 habitantes en 2025, un 8 % más que en 2015. En 2024 había 13.458 turismos según Idescat a partir de la DGT, 375 por cada 1.000 habitantes.",
             "A menos de tres kilómetros del centro pasan la A-2, la B-20, la B-23, la B-25, la C-32, la C-245 y la N-340. Para quien vive aquí, eso significa que una prueba en carretera después de la reparación —para confirmar que un ruido o un aviso han desaparecido de verdad— se puede hacer contigo en el coche sin alejarse."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el taller exactamente?",
         "a": "En el carrer del Tambor del Bruc 3 (CP 08970), en Sant Joan Despí."},
        {"q": "¿Qué días abre?",
         "a": "De lunes a viernes, mañana y tarde. Sábados y domingos está cerrado."},
        {"q": "¿Hacéis trabajos de escape homologados?",
         "a": "El taller tiene homologación REDISTA para escape y gases; consulta tu caso concreto por teléfono."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "35.926 habitantes (+8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082172")},
        {"etiqueta": "Turismos (2024)", "valor": "13.458 · 375 por cada 1.000 hab.", **F.idescat("082172")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 3,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 5,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Carrer del Tambor del Bruc 3, en el municipio · 0,8 km del centro", **_DASERCARS_BCN},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082172"), F.itv_cat_f, F.bmw_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
# metaDescription: las 15 ciudades tienen 0 impresiones en GSC (cache/paso_gsc.json,
# 90 días) y su descripción prometía «hasta un 50 %», «ISTA oficial» o «garantía
# oficial» (guía §2). aplicar.py no toca este campo: se aplica con
#   python3 -c "import sys; sys.path.insert(0,'scripts/datos_ciudades/tandas'); import tanda_1; tanda_1.aplicar_meta()"
META = {
    "l-hospitalet-de-llobregat": "BMW y MINI en L'Hospitalet: taller especialista independiente a 4,1 km, en Sant Joan Despí. Recogida en el área metropolitana sujeta a disponibilidad e ITV en Cornellà.",
    "santa-coloma-de-gramenet": "Taller especialista BMW y MINI para Santa Coloma de Gramenet, a 18,5 km en Sant Joan Despí. Servicio oficial e ITV cercanos y recogida sujeta a disponibilidad.",
    "alcobendas": "Dasercars Madrid, taller independiente especializado en BMW y MINI, está en la calle Valgrande 17 de Alcobendas. Presupuesto por escrito y cuatro ITV en el municipio.",
    "sant-cugat-del-valles": "Especialista independiente BMW y MINI para Sant Cugat, a 20,2 km por carretera en Sant Joan Despí. ITV en Sant Mamet y recogida sujeta a disponibilidad.",
    "rubi": "Taller especialista BMW y MINI para Rubí, a 20,9 km por la B-30 y la AP-7. ITV y servicio oficial en Sant Cugat; Rubí queda fuera de la zona de recogida.",
    "manresa": "BMW en Manresa: servicio oficial a 6,9 km en Sant Fruitós y taller especialista independiente a 59,7 km. Qué conviene resolver cerca y qué merece el viaje.",
    "coslada": "Taller especialista BMW y MINI para Coslada, en Alcobendas a 19,5 km por la M-40. Tres ITV en el municipio y recogida sujeta a disponibilidad.",
    "granollers": "Granollers: servicio oficial BMW en la C-17 y taller especialista independiente a 38,9 km en Sant Joan Despí. ITV en el polígono El Congost.",
    "mollet-del-valles": "BMW y MINI en Mollet del Vallès: ITV a 3,4 km, servicio oficial en Granollers y taller especialista independiente a 29,1 km por la C-33.",
    "esplugues-de-llobregat": "Taller especialista BMW y MINI a 3,3 km de Esplugues, en Sant Joan Despí. Recogida en el área metropolitana sujeta a disponibilidad e ITV en Sant Just.",
    "sant-feliu-de-llobregat": "Sant Feliu de Llobregat: el taller especialista BMW y MINI de la red, a 2,8 km en Sant Joan Despí. ITV a 1,3 km y recogida sujeta a disponibilidad.",
    "igualada": "BMW en Igualada: servicio oficial a 40,7 km y taller especialista independiente a 55,2 km por la A-2. ITV en el polígono Les Comes.",
    "san-fernando-de-henares": "Taller especialista BMW y MINI para San Fernando de Henares, en Alcobendas a 21,5 km. ITV en la calle Tapiceros y recogida sujeta a disponibilidad.",
    "montcada-i-reixac": "Especialista independiente BMW y MINI para Montcada i Reixac, a 20,7 km en Sant Joan Despí. Recogida en el área metropolitana sujeta a disponibilidad.",
    "sant-joan-despi": "Dasercars Barcelona, taller independiente especializado en BMW y MINI, en el carrer del Tambor del Bruc 3 de Sant Joan Despí. Homologación REDISTA.",
}


def aplicar_meta():
    import json
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from comun import CIUDADES_DIR
    for slug, desc in META.items():
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        cj["metaDescription"] = desc
        f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
        print("meta", slug, len(desc))
