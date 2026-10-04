# Tanda 5: Morata de Tajuña, Santa Coloma de Cervelló, Vacarisses, Begues, Nuevo Baztán,
# Fuente el Saz de Jarama, Sallent, Campo Real, Roda de Ter, Sant Vicenç de Montalt,
# Villanueva de la Torre, Dosrius.
# Saltadas por decisión pendiente de Martin (Zaragoza sin dirección): zuera, tauste, muela-la.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"

CIUDADES = {}

# metaDescription nuevas solo para ciudades sin impresiones en GSC cuya
# descripción actual contiene una promesa («hasta un 50 %», «diagnóstico oficial», ISTA).
META = {}

# ---------------------------------------------------------------- Morata de Tajuña
CIUDADES["morata-de-tajuna"] = {
    "h1": "Morata de Tajuña: del sureste de Madrid al taller BMW de Alcobendas por la A-3",
    "entradilla": "Para un BMW o un MINI de Morata, lo útil cabe en tres datos: la ITV queda en Arganda del Rey, el servicio oficial en la carretera de Valencia y el taller especialista de la red, al otro lado de Madrid, a 47,5 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 47.5},
    "secciones": [
        {"id": "por-la-a3", "h2": "47,5 km: M-313, A-3, M-30 y A-1 hacia el norte",
         "parrafos": [
             "La ruta sale de Morata por la M-313, sube por la A-3, cruza Madrid por la M-30 y sale por la A-1 hasta Alcobendas, donde está Dasercars Madrid, en la calle Valgrande 17. En línea recta son 38,6 km; por carretera, 47,5.",
             "Es un viaje que se hace para algo concreto. Un cambio de pastillas lo resuelve cualquier taller de la comarca; una avería electrónica que vuelve, un consumo de aceite raro en un diésel N47 o un aviso del sistema de AdBlue piden a alguien que trabaje solo con BMW.",
         ]},
        {"id": "itv-arganda", "h2": "La inspección, en el Camino Puente Viejo de Arganda",
         "parrafos": [
             "Según el listado oficial de la Comunidad de Madrid, la estación más próxima por carretera es la de General de Servicios ITV (estación 2852), en el Camino Puente Viejo, en Arganda del Rey: 9,9 km desde el centro de Morata. Si el coche va antes a Alcobendas, pide la pre-ITV allí y deja la inspección para la vuelta, ya cerca de casa.",
         ]},
        {"id": "oficial-carretera-valencia", "h2": "El servicio oficial más cercano, a 27 km",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto oficial más próximo en AutoPremier, carretera de Valencia, km 7,3, ya dentro del término de Madrid: 27 km por carretera. Es la referencia si tienes una reparación en garantía de BMW pendiente; para el resto puedes elegir taller.",
         ]},
        {"id": "morata-en-cifras", "h2": "8.397 vecinos y 4.083 turismos",
         "parrafos": [
             "Morata tenía 7.453 habitantes en 2015 y 8.397 en 2025, un 12,7 % más según el padrón. La Comunidad de Madrid, con datos de la DGT, contaba 4.083 turismos en 2025: 486 por cada mil vecinos, más que los 388 de Madrid capital.",
             "Con la M-313 y la M-302 a menos de medio kilómetro del centro, la M-315 a 0,6 km y la M-311 a 2,8 km, buena parte de los trayectos son por carretera autonómica, con curvas y cambios de ritmo. A un diésel moderno le conviene, de vez en cuando, un tramo largo de autovía para que el filtro de partículas complete su regeneración.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Morata de Tajuña?",
         "a": "No. El taller de la red que atiende la zona es Dasercars Madrid, en Alcobendas, a 47,5 km por la A-3, la M-30 y la A-1."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de General de Servicios ITV en el Camino Puente Viejo de Arganda del Rey, a 9,9 km, según la Comunidad de Madrid."},
        {"q": "¿Podéis recoger el coche en Morata?",
         "a": "La recogida y entrega del taller se limita al área metropolitana de Madrid y está sujeta a disponibilidad. Pregunta al reservar si tu dirección entra."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "8.397 habitantes (+12,7 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "4.083 · 486 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "Arganda del Rey, Camino Puente Viejo · 9,9 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, ctra. de Valencia km 7,3 · 27 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 47,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["morata-de-tajuna"] = "Morata de Tajuña: el taller especialista BMW de la red está en Alcobendas, a 47,5 km por la A-3. ITV en Arganda, servicio oficial a 27 km y qué compensa."

# ---------------------------------------------------------------- Santa Coloma de Cervelló
CIUDADES["santa-coloma-de-cervello"] = {
    "h1": "BMW en Santa Coloma de Cervelló: el taller especialista, a 3,5 km en línea recta",
    "entradilla": "Pocas páginas de la red pueden decir esto: desde Santa Coloma de Cervelló, la nave de Dasercars Barcelona queda a 3,5 km en línea recta. Lo que hay que saber para usarla bien.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 9.1},
    "secciones": [
        {"id": "cruzar-el-rio", "h2": "Nueve kilómetros por carretera, tres y medio a vuelo de pájaro",
         "parrafos": [
             "El taller está en el carrer del Tambor del Bruc 3, en Sant Joan Despí. La distancia en línea recta es de 3,5 km, pero por carretera sube a 9,1: la ruta más corta da la vuelta por la A-2.",
             "Con la BV-2002 a medio kilómetro del centro y la A-2 y la B-23 a menos de un kilómetro y medio, no hace falta atravesar ningún casco urbano para llegar.",
         ]},
        {"id": "recogida-amb", "h2": "Dentro del área metropolitana: recogida y coche de cortesía",
         "parrafos": [
             "Santa Coloma de Cervelló es uno de los 36 municipios del Área Metropolitana de Barcelona. Eso le da acceso a la recogida y entrega del coche y al vehículo de cortesía que el taller ofrece dentro del área, ambos sujetos a disponibilidad: mejor pedirlos al reservar que la víspera.",
         ]},
        {"id": "concesionario-sant-boi", "h2": "El concesionario está en Sant Boi",
         "parrafos": [
             "El punto oficial BMW más próximo en el localizador de bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 6,8 km. Para una reparación cubierta por la garantía de BMW, es allí.",
             "Para el mantenimiento periódico, no: el Reglamento (UE) 461/2010 protege tu derecho a revisar el coche fuera de la red oficial sin perder la garantía, mientras se respeten los intervalos y las especificaciones del fabricante.",
         ]},
        {"id": "itv-sant-just", "h2": "La ITV, en el polígono de Sant Just Desvern",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sant Just Desvern (B05), en la avinguda de la Riera 19-21, a 10,4 km. El municipio tenía 8.273 habitantes en 2025, en un término de solo 7,49 km², y 4.022 turismos en 2024 según Idescat a partir de la DGT: 486 por cada mil vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "9,1 km por carretera, por la A-2, hasta el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
        {"q": "¿Recogéis el coche en Santa Coloma de Cervelló?",
         "a": "Sí, el municipio está en el Área Metropolitana de Barcelona. La recogida y entrega está sujeta a disponibilidad."},
        {"q": "¿Sois el concesionario de Sant Boi?",
         "a": "No. Ese es Barcelona Premium, servicio oficial BMW. Nosotros somos Dasercars, taller independiente especializado en BMW y MINI."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Sant Just Desvern (B05), a 10,4 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "8.273 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat (AMB)", **F.idescat("082444")},
        {"etiqueta": "Turismos (2024)", "valor": "4.022 · 486 por cada 1.000 hab.", **F.idescat("082444")},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 9,1 km (3,5 km en línea recta)", **F.osrm},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 10,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 6,8 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082444"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}
META["santa-coloma-de-cervello"] = "Taller independiente especializado en BMW y MINI a 9,1 km de Santa Coloma de Cervelló, en Sant Joan Despí. Recogida en el área metropolitana, sujeta a disponibilidad."

# ---------------------------------------------------------------- Vacarisses
CIUDADES["vacarisses"] = {
    "h1": "Vacarisses ha crecido un 25,8 % en diez años: dónde llevar tu BMW",
    "entradilla": "Más vecinos, más coches y ningún concesionario en el pueblo. Te contamos qué tienes en Terrassa y Viladecavalls y qué supone bajar hasta nuestro taller de Sant Joan Despí, a 40 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 40.4},
    "secciones": [
        {"id": "mas-vecinos", "h2": "De 6.143 a 7.729 habitantes",
         "parrafos": [
             "El padrón daba a Vacarisses 6.143 vecinos en 2015 y 7.729 en 2025. En 2024 había 4.269 turismos censados según Idescat, con datos de la DGT: 552 por cada mil habitantes, casi el doble que los 281 de Barcelona ciudad.",
             "En un término de 40,7 km² y a 382 metros de altitud, el coche se usa para casi todo. La C-16 pasa a 2,1 km del centro y la C-58 a 2,3, así que muchos trayectos acaban en vía rápida, algo que agradecen los diésel con filtro de partículas.",
         ]},
        {"id": "terrassa-oficial", "h2": "Lo oficial, en Terrassa",
         "parrafos": [
             "El punto de servicio oficial BMW más próximo según bmw.es es Quadis Munich, en el carrer Anoia 9 de Terrassa, a 17,5 km. Si recibes una carta de BMW por una campaña de revisión, la cita es con la red oficial; esas campañas no las hace un taller independiente.",
         ]},
        {"id": "itv-can-trias", "h2": "ITV en Can Trias, Viladecavalls",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Viladecavalls (B03), en el polígono industrial Can Trias, a 11,4 km. Queda de camino si sales hacia Terrassa por la C-58.",
         ]},
        {"id": "cuarenta-km", "h2": "40,4 km hasta Sant Joan Despí: cuándo compensa",
         "parrafos": [
             "La ruta encadena la C-58, la C-16 y la B-20 hasta el carrer del Tambor del Bruc. Vacarisses no está en el Área Metropolitana de Barcelona, de modo que la recogida del taller no llega: el coche lo traes tú.",
             "Con esa distancia, el viaje tiene sentido para lo que pide un especialista: una caja automática que da tirones, un ruido de distribución en un diésel B47 o un fallo eléctrico que otro taller no ha localizado. Para la revisión de rutina, decide tú si te compensa.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Vacarisses?",
         "a": "No. La recogida del taller solo cubre el Área Metropolitana de Barcelona y Vacarisses queda fuera."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en el carrer Anoia 9 de Terrassa, a 17,5 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Viladecavalls (B03), en el polígono Can Trias, a 11,4 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "7.729 habitantes (+25,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082917")},
        {"etiqueta": "Turismos (2024)", "valor": "4.269 · 552 por cada 1.000 hab.", **F.idescat("082917")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecavalls (B03) · 11,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Terrassa) · 17,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 40,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082917"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["vacarisses"] = "Vacarisses: servicio oficial BMW en Terrassa, ITV en Viladecavalls y taller especialista independiente en Sant Joan Despí, a 40,4 km. Cuándo compensa el viaje."

# ---------------------------------------------------------------- Begues
CIUDADES["begues"] = {
    "h1": "Begues: sin autovía cerca, pero con recogida del taller BMW a 24 km",
    "entradilla": "Begues pertenece al Área Metropolitana de Barcelona aunque ninguna autovía pase cerca del pueblo. Eso tiene una ventaja práctica: el taller de Sant Joan Despí puede recoger el coche, sujeto a disponibilidad.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 24.1},
    "secciones": [
        {"id": "bv-2041", "h2": "Primero la BV-2041, luego la C-32",
         "parrafos": [
             "En un radio de tres kilómetros desde el centro solo hay carreteras secundarias: la C-535, a unos 200 metros, y la BV-2041, a 1,8 km. Para salir, la ruta hasta Dasercars Barcelona toma la BV-2041, enlaza con la C-32 y termina por la B-25: 24,1 km por carretera, 12,1 en línea recta.",
             "Es un pueblo a 399 metros, y la bajada hacia el llano se hace con el freno trabajando. El líquido de frenos absorbe humedad con el tiempo y pierde capacidad aunque el coche haga pocos kilómetros: el plan de BMW lo cambia por fecha, y conviene no saltárselo.",
         ]},
        {"id": "recogida-begues", "h2": "Recogida dentro del área metropolitana",
         "parrafos": [
             "Al ser uno de los 36 municipios del AMB, Begues entra en la zona donde el taller ofrece recogida y entrega del coche y vehículo de cortesía. Las dos cosas están sujetas a disponibilidad, así que lo razonable es pedirlas al reservar.",
             "El taller abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00; sábados y domingos está cerrado.",
         ]},
        {"id": "itv-y-oficial", "h2": "ITV en Viladecans, concesionario en Sant Boi",
         "parrafos": [
             "La estación más próxima por carretera según la Generalitat es la de Viladecans (B07), en el carrer Jocelyn Bell 16, a 15,8 km. El servicio oficial BMW más cercano, Barcelona Premium, está en la carretera del Prat 15 de Sant Boi de Llobregat, a 20,4 km según bmw.es.",
         ]},
        {"id": "begues-en-cifras", "h2": "Un término de 50 km² para 7.561 vecinos",
         "parrafos": [
             "Begues tenía 7.561 habitantes en 2025, un 13,4 % más que en 2015, repartidos en 50,44 km². Idescat contaba 3.747 turismos en 2024: 496 por cada mil vecinos. Con tanta superficie y sin vía rápida a mano, casi todos los desplazamientos empiezan con unos kilómetros de carretera secundaria.",
         ]},
    ],
    "faq": [
        {"q": "¿Llega la recogida del taller hasta Begues?",
         "a": "Sí, Begues está en el Área Metropolitana de Barcelona. La recogida y entrega está sujeta a disponibilidad."},
        {"q": "¿Cuánto hay hasta Sant Joan Despí?",
         "a": "24,1 km por carretera, por la BV-2041, la C-32 y la B-25."},
        {"q": "¿Por qué el líquido de frenos se cambia por tiempo?",
         "a": "Porque absorbe humedad aunque el coche no se mueva, y con ella baja su punto de ebullición."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "7.561 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat (AMB)", **F.idescat("080207")},
        {"etiqueta": "Turismos (2024)", "valor": "3.747 · 496 por cada 1.000 hab.", **F.idescat("080207")},
        {"etiqueta": "Superficie", "valor": "50,44 km²", **F.idescat("080207")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecans (B07) · 15,8 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 24,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080207"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["begues"] = "Begues está en el área metropolitana: el taller especialista BMW de Sant Joan Despí, a 24,1 km, ofrece recogida sujeta a disponibilidad. ITV en Viladecans."

# ---------------------------------------------------------------- Nuevo Baztán
CIUDADES["nuevo-baztan"] = {
    "h1": "Nuevo Baztán, a 838 metros: invierno, batería y el taller BMW de Alcobendas",
    "entradilla": "A 838 metros de altitud y con 653 turismos por cada mil vecinos, en Nuevo Baztán el coche trabaja en frío buena parte del año. Lo que conviene vigilar y dónde tienes cada servicio.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 49.4},
    "secciones": [
        {"id": "frio-838", "h2": "Lo que el frío pide a un BMW",
         "parrafos": [
             "Las mañanas de helada son las que descubren una batería cansada. En un BMW reciente, además, cambiarla no es solo montar otra: hay que registrarla para que la gestión de carga sepa qué capacidad tiene. Sin ese paso, el alternador la carga mal y se acorta su vida.",
             "En los diésel, las bujías de precalentamiento son la otra pieza que avisa con el frío: un arranque largo o humo blanco al encender suelen ser el primer síntoma. Y el anticongelante se comprueba por concentración, no solo mirando el nivel del depósito.",
         ]},
        {"id": "todo-en-alcala", "h2": "ITV y servicio oficial, en Alcalá de Henares",
         "parrafos": [
             "La estación oficial más próxima por carretera es la de TÜV SÜD ATISAE (estación 2878), en la avenida Juan Carlos I, junto al centro comercial La Garena de Alcalá, a 17,6 km según la Comunidad de Madrid. El servicio oficial BMW más cercano en bmw.es también está en Alcalá: AutoPremier, en la Vía Complutense 131, a 21,4 km.",
         ]},
        {"id": "m100-r2-nuevo-baztan", "h2": "Hacia Alcobendas por la M-100 y la R-2",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 sale por la M-204 y la M-300, sigue por la M-100 y enlaza con la R-2 y la M-50: 49,4 km por carretera, 38,6 en línea recta. No hay ninguna vía principal a menos de tres kilómetros del centro, así que el primer tramo es siempre secundario.",
             "Si el trabajo es de varios días, pregunta por el vehículo de cortesía y confirma si la recogida del área metropolitana llega a tu calle; ambos dependen de disponibilidad.",
         ]},
        {"id": "nuevo-baztan-crece", "h2": "Un 21,8 % más de vecinos que en 2015",
         "parrafos": [
             "El padrón pasó de 6.098 habitantes en 2015 a 7.429 en 2025. La Comunidad de Madrid, con datos de la DGT, contaba 4.853 turismos en 2025: 653 por cada mil vecinos, frente a 388 en Madrid capital.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Nuevo Baztán?",
         "a": "La estación oficial más próxima es la de TÜV SÜD ATISAE en la avenida Juan Carlos I de Alcalá de Henares, a 17,6 km."},
        {"q": "¿Por qué hay que registrar la batería nueva?",
         "a": "Porque la gestión de carga del BMW trabaja con la capacidad registrada; si no se actualiza, la batería nueva se carga mal."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 49,4 km por carretera, en la calle Valgrande 17 de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "7.429 habitantes (+21,8 % desde 2015)", **F.ine},
        {"etiqueta": "Altitud del centro urbano", "valor": "838 m", **F.copernicus},
        {"etiqueta": "Turismos (2025)", "valor": "4.853 · 653 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "TÜV SÜD ATISAE, Alcalá de Henares · 17,6 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Vía Complutense 131 · 21,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 49,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

META["nuevo-baztan"] = "Nuevo Baztán, a 838 m: batería, precalentamiento y anticongelante en un BMW. ITV y servicio oficial en Alcalá; taller especialista en Alcobendas, a 49,4 km."

# ---------------------------------------------------------------- Fuente el Saz de Jarama
CIUDADES["fuente-el-saz-de-jarama"] = {
    "h1": "Fuente el Saz de Jarama: taller especialista BMW a 24 km, servicio oficial en Algete",
    "entradilla": "Entre Algete y la A-1, Fuente el Saz queda a 24,3 km de nuestro taller de Alcobendas. Tienes el concesionario más cerca todavía, y conviene saber qué se hace en cada sitio.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 24.3},
    "secciones": [
        {"id": "m111-m100-a1", "h2": "Por la M-111, la M-100 y la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 de Alcobendas usa la M-111, la M-100 y la A-1: 24,3 km por carretera, 15,7 en línea recta. La M-111 pasa a unos 200 metros del centro, así que la salida es directa.",
             "A esta distancia, la recogida y entrega del coche dentro del área metropolitana de Madrid puede ser una opción; está sujeta a disponibilidad y conviene confirmarla al pedir cita.",
         ]},
        {"id": "bymycar-algete", "h2": "El servicio oficial, a 8,6 km en Algete",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo es BYmyCAR Madrid, en la calle Tejera 2, carretera de Algete km 3, a 8,6 km. Es donde se tramitan las reparaciones en garantía que cubre BMW.",
             "El mantenimiento es otra cosa. Revisarlo en un taller independiente no anula la garantía del fabricante mientras se sigan los intervalos y se usen piezas y aceites con la especificación correcta: lo garantiza el Reglamento (UE) 461/2010.",
         ]},
        {"id": "itv-nicasio-martin", "h2": "La ITV más próxima, en la avenida Nicasio Martín de Algete",
         "parrafos": [
             "En el listado oficial de la Comunidad de Madrid, la estación más próxima por carretera es la 2818, de ITV Barbastro, en la avenida Nicasio Martín 4, en el polígono industrial del sector 8 de Algete, a 9,5 km. Si vas a pasar la inspección poco después de una visita al taller, pide la pre-ITV en esa misma cita.",
         ]},
        {"id": "fuente-el-saz-parque", "h2": "596 turismos por cada mil vecinos",
         "parrafos": [
             "Fuente el Saz tenía 7.413 habitantes en 2025, un 15,1 % más que en 2015. En 2025 había 4.418 turismos censados según la Comunidad de Madrid a partir de la DGT: 596 por cada mil habitantes, por encima de los 388 de Madrid capital, en un término de 33 km².",
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Algete?",
         "a": "No. El servicio oficial de Algete es BYmyCAR Madrid. Nosotros somos Dasercars, taller independiente especializado en BMW y MINI, en Alcobendas."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "24,3 km por carretera, por la M-111, la M-100 y la A-1."},
        {"q": "¿Pierdo la garantía si hago aquí las revisiones?",
         "a": "No, si se respetan los intervalos y especificaciones del plan de mantenimiento de BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "7.413 habitantes (+15,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "4.418 · 596 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "ITV Barbastro, Algete (estación 2818) · 9,5 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid (Algete) · 8,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 24,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}
META["fuente-el-saz-de-jarama"] = "Fuente el Saz de Jarama: taller independiente especializado en BMW y MINI en Alcobendas, a 24,3 km. Servicio oficial e ITV más cercana, en Algete."

# ---------------------------------------------------------------- Sallent
CIUDADES["sallent"] = {
    "h1": "Sallent: tu BMW a 72 km del taller, casi todo por la C-16",
    "entradilla": "Desde Sallent hasta Sant Joan Despí hay 72 km, y la mayor parte se hace por la misma carretera que pasa junto al pueblo. Antes de decidir si bajas, mira lo que tienes en el Bages.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 72.0},
    "secciones": [
        {"id": "la-c16", "h2": "La C-16, a medio kilómetro del centro",
         "parrafos": [
             "La C-16 pasa a medio kilómetro del centro de Sallent y es la columna de la ruta hasta el taller: C-16 y, al final, la B-20 hasta el carrer del Tambor del Bruc. En línea recta son 53 km; por carretera, 72.",
             "Un trayecto así, a velocidad constante, es justo lo que necesita un diésel para quemar el hollín del filtro de partículas. Si tu coche solo hace recorridos cortos por el pueblo, el viaje al taller le sirve de regeneración de paso.",
         ]},
        {"id": "en-el-bages", "h2": "Lo que tienes a menos de 16 km",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 10,8 km. La ITV más cercana por carretera en el registro de la Generalitat también está en ese municipio: Sant Fruitós (B25), en el polígono El Grau, a 15,9 km.",
             "Para un cambio de neumáticos, unas pastillas o la revisión anual, lo sensato es resolverlo en la comarca.",
         ]},
        {"id": "por-que-bajar", "h2": "Por qué alguien de Sallent haría 72 km",
         "parrafos": [
             "Por un problema que pide conocer BMW a fondo: una avería del turbo o del sistema de escape en un diésel N57, una centralita que pierde la codificación, un fallo intermitente de la caja automática. También para un segundo diagnóstico antes de aceptar una reparación grande.",
             "Antes de coger la C-16, llama con modelo, año, kilometraje y lo que notas. Muchas veces se puede orientar el problema por teléfono y tener la pieza pedida el día que llegas.",
         ]},
        {"id": "sallent-en-cifras", "h2": "7.030 vecinos en 65 km²",
         "parrafos": [
             "Sallent tenía 7.030 habitantes en 2025 y 6.669 en 2015, según el padrón. Idescat, con datos de la DGT, contaba 3.780 turismos en 2024: 538 por cada mil vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en el Bages?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 72 km de Sallent."},
        {"q": "¿Dónde paso la ITV desde Sallent?",
         "a": "La estación más próxima por carretera es Sant Fruitós (B25), en el polígono El Grau, a 15,9 km."},
        {"q": "¿Recogéis el coche en Sallent?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "7.030 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("081918")},
        {"etiqueta": "Turismos (2024)", "valor": "3.780 · 538 por cada 1.000 hab.", **F.idescat("081918")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 10,8 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sant Fruitós (B25) · 15,9 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 72 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081918"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["sallent"] = "Sallent: servicio oficial BMW e ITV en Sant Fruitós de Bages; taller especialista independiente en Sant Joan Despí, a 72 km por la C-16. Cuándo compensa bajar."

# ---------------------------------------------------------------- Campo Real
CIUDADES["campo-real"] = {
    "h1": "Campo Real y tu BMW: ITV en Arganda, taller especialista a 47 km",
    "entradilla": "Campo Real ha sumado más de mil vecinos en diez años. Si tienes un BMW o un MINI, la ITV te queda a unos 9 km, en Arganda, y el taller de la red en Alcobendas, cruzando Madrid por la R-3 y la M-30.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 46.7},
    "secciones": [
        {"id": "itv-san-martin", "h2": "Una ITV en el camino de San Martín de la Vega",
         "parrafos": [
             "La estación oficial más próxima por carretera es la de Laboratorio e Inspección de Vehículos (estación 2807), en el Camino de San Martín de la Vega 8, en Arganda del Rey: 9,4 km desde el centro de Campo Real, según la Comunidad de Madrid.",
         ]},
        {"id": "r3-m30", "h2": "46,7 km por la R-3, la M-30 y la A-1",
         "parrafos": [
             "Desde Campo Real, la ruta hasta la calle Valgrande de Alcobendas sale por la M-209, que pasa a 0,4 km del centro, toma la R-3, cruza por la M-30 y termina por la A-1: 46,7 km por carretera, 31,9 en línea recta.",
             "No es un viaje para una escobilla. Sí lo es para un diagnóstico que nadie ha cerrado o para el mantenimiento por plan de marca. Antes de mover el coche recibes un presupuesto por escrito, y el trabajo no empieza hasta que das el visto bueno; la diagnosis también se presupuesta.",
         ]},
        {"id": "oficial-la-garena", "h2": "El servicio oficial, en el polígono La Garena",
         "parrafos": [
             "En el localizador de bmw.es, el punto oficial más cercano es AutoPremier, en la calle Argentina 7 del polígono La Garena, en Alcalá de Henares, a 23,7 km por carretera.",
         ]},
        {"id": "campo-real-crece", "h2": "De 5.854 a 6.974 vecinos",
         "parrafos": [
             "El padrón registraba 5.854 habitantes en 2015 y 6.974 en 2025: un 19,1 % más. En 2025 había 3.820 turismos censados según la Comunidad de Madrid a partir de la DGT, 548 por cada mil vecinos, en un término de 61,5 km² situado a unos 776 metros de altitud.",
             "A esa altura las heladas de invierno no son raras. Si el coche duerme en la calle, revisa la batería antes de diciembre: es la pieza que antes falla con el frío.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Campo Real?",
         "a": "En la estación 2807 del Camino de San Martín de la Vega, en Arganda del Rey, a 9,4 km."},
        {"q": "¿Cómo llego a vuestro taller?",
         "a": "Por la M-209, la R-3, la M-30 y la A-1 hasta Alcobendas: 46,7 km."},
        {"q": "¿Llega hasta aquí la recogida del coche?",
         "a": "La recogida y entrega se ofrece dentro del área metropolitana de Madrid y está sujeta a disponibilidad. Confírmalo al llamar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "6.974 habitantes (+19,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "3.820 · 548 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Superficie del término", "valor": "61,5 km²", **F.cartociudad},
        {"etiqueta": "ITV más cercana", "valor": "Arganda del Rey (estación 2807) · 9,4 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 23,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 46,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.cartociudad_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

META["campo-real"] = "Campo Real: ITV en Arganda del Rey a 9,4 km, servicio oficial BMW en Alcalá y taller independiente especializado en BMW y MINI en Alcobendas, a 46,7 km."

# ---------------------------------------------------------------- Roda de Ter
CIUDADES["roda-de-ter"] = {
    "h1": "Roda de Ter: servicio oficial BMW a 9 km en Vic, especialista a 89 km",
    "entradilla": "Con el servicio oficial y la ITV en Vic, a menos de diez kilómetros, el día a día de un BMW de Roda de Ter se resuelve en Osona. Nuestro taller está a 88,7 km: te explicamos para qué tiene sentido.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 88.7},
    "secciones": [
        {"id": "vic-al-lado", "h2": "Vic lo tiene casi todo a mano",
         "parrafos": [
             "La estación de ITV más próxima por carretera en el registro de la Generalitat es la de Osona (B04), en el carrer Sant Llorenç Desmunts 22 de Vic, a 5,6 km. El servicio oficial BMW más cercano según bmw.es, Quadis Munich, está en el carrer Perot Rocaguinarda 1, también en Vic, a 9,3 km.",
             "Con esas dos referencias tan cerca, nadie debería hacer 89 km para una revisión o una inspección.",
         ]},
        {"id": "ochenta-y-nueve-km", "h2": "Cuándo sí: 88,7 km por la C-17",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc encadena la C-153, la C-25, la C-17, la C-33 y la B-20. Es largo, y solo compensa para trabajos de especialista: una distribución que hace ruido en un diésel N47, un fallo del SCR con la cuenta atrás de AdBlue en el cuadro o una avería eléctrica que ya ha pasado por otros talleres.",
             "Antes de que salgas, se presupuesta. Recibes el presupuesto por escrito y no se toca el coche sin tu conformidad, de modo que el viaje no es a ciegas.",
         ]},
        {"id": "termino-pequeno", "h2": "Un término de 2,23 km²",
         "parrafos": [
             "Roda de Ter es un municipio de término muy pequeño: 2,23 km² para 6.937 habitantes en 2025, lo que da una densidad de 3.111 habitantes por km². Aun así, Idescat contaba 3.908 turismos en 2024, 563 por cada mil vecinos: el doble que en Barcelona ciudad.",
             "En un término tan pequeño, cualquier recorrido dentro del pueblo es corto. Un diésel que solo hace eso acumula hollín en el filtro de partículas; una salida por carretera de vez en cuando le ayuda a regenerar.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 9,3 km según bmw.es."},
        {"q": "¿Qué ITV me corresponde?",
         "a": "La más próxima por carretera es la de Osona (B04), en Vic, a 5,6 km."},
        {"q": "¿Tenéis taller en Osona?",
         "a": "No. El taller de la red está en Sant Joan Despí, a 88,7 km de Roda de Ter."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "6.937 habitantes (+13,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081831")},
        {"etiqueta": "Superficie", "valor": "2,23 km²", **F.idescat("081831")},
        {"etiqueta": "Turismos (2024)", "valor": "3.908 · 563 por cada 1.000 hab.", **F.idescat("081831")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 5,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 9,3 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081831"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["roda-de-ter"] = "Roda de Ter: servicio oficial BMW e ITV en Vic; taller independiente especializado en BMW y MINI en Sant Joan Despí, a 88,7 km. Para qué compensa el viaje."

# ---------------------------------------------------------------- Sant Vicenç de Montalt
CIUDADES["sant-vicenc-de-montalt"] = {
    "h1": "Sant Vicenç de Montalt: un BMW a 2 km del mar y el taller a 51 km por la C-32",
    "entradilla": "En el Maresme, a unos dos kilómetros de la costa, el coche convive con la humedad salina. Te contamos qué vigilar, dónde está el servicio oficial más próximo y qué supone ir hasta Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 50.8},
    "secciones": [
        {"id": "humedad-salina", "h2": "La sal no se ve, pero trabaja",
         "parrafos": [
             "El centro del municipio está a unos 2,1 km de la línea de costa. La brisa marina deposita sal en todo lo que está al aire, y donde más se nota es abajo: anclajes del escape, tornillería de la suspensión y protecciones de los bajos. Un BMW que pasa la noche fuera lo acusa antes que uno de garaje.",
             "Dos hábitos ayudan: aclarar los bajos con agua a presión cada cierto tiempo y no dejar el coche semanas sin moverlo, porque los discos se cubren de óxido y luego vibran al frenar. Si un testigo eléctrico se enciende y se apaga, revisar conectores es el primer paso.",
         ]},
        {"id": "mataro-y-argentona", "h2": "Servicio oficial en Mataró, ITV en Argentona",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo es Pruna Motor, en la Via Sergia 2 de Mataró, a 13,6 km. La estación de ITV más cercana por carretera en el registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 13,2 km.",
         ]},
        {"id": "c32-sur", "h2": "50,8 km de C-32 hacia el sur",
         "parrafos": [
             "La C-32 pasa a medio kilómetro del centro y la N-II a 1,4 km. La ruta hasta Dasercars Barcelona baja por la C-32 y llega por la B-20: 50,8 km por carretera.",
             "El municipio no forma parte del Área Metropolitana de Barcelona y la recogida del taller no llega hasta aquí. Con esa distancia, el viaje se reserva para averías que necesitan un especialista en BMW o MINI.",
         ]},
    ],
    "faq": [
        {"q": "¿Afecta vivir cerca del mar a mi BMW?",
         "a": "Acelera la corrosión de bajos, escape y tornillería, y el óxido de los discos si el coche está parado. Aclarar los bajos ayuda."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima por carretera es la de Argentona (B08), en el polígono El Cros, a 13,2 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sergia 2 de Mataró, a 13,6 km."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "6.802 habitantes (+12,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082649")},
        {"etiqueta": "Turismos (2024)", "valor": "3.613 · 531 por cada 1.000 hab.", **F.idescat("082649")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 2,1 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 13,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 13,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 50,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082649"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
META["sant-vicenc-de-montalt"] = "Sant Vicenç de Montalt, a 2 km del mar: qué hace el salitre a un BMW, servicio oficial en Mataró, ITV en Argentona y taller especialista a 50,8 km."

# ---------------------------------------------------------------- Villanueva de la Torre
CIUDADES["villanueva-de-la-torre"] = {
    "h1": "Villanueva de la Torre: provincia de Guadalajara, taller BMW en Alcobendas",
    "entradilla": "Villanueva de la Torre está en Guadalajara, pero el taller especialista de la red que la atiende está en la Comunidad de Madrid, a 47,6 km. El concesionario, en cambio, lo tienes en la capital de tu provincia.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 47.6},
    "secciones": [
        {"id": "concesionario-guadalajara", "h2": "El concesionario, en el Paseo de la Estación",
         "parrafos": [
             "El punto oficial BMW más próximo según el localizador de bmw.es es AutoPremier, en el Paseo de la Estación 23 de Guadalajara, a 18,3 km por carretera. Si lo que necesitas es una reparación cubierta por la garantía de BMW, ese es el sitio.",
             "Nosotros no somos ese concesionario. Somos Dasercars, taller independiente especializado en BMW y MINI, con nave propia en Alcobendas.",
         ]},
        {"id": "a2-r2-villanueva", "h2": "47,6 km por la A-2 y la R-2",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 sale por la CM-1008, toma la A-2, sigue por la R-2 y entra por la M-50: 47,6 km por carretera, 30,1 en línea recta. Villanueva queda fuera del área metropolitana de Madrid, así que la recogida del taller no llega aquí.",
             "Por eso, antes de coger el coche, llama con modelo, año, kilometraje y el síntoma: a veces el problema se orienta por teléfono y sabes antes de salir si merece la pena el viaje.",
         ]},
        {"id": "r2-y-filtro", "h2": "La R-2 a 2,4 km: autovía para regenerar",
         "parrafos": [
             "La R-2 pasa a 2,4 km del centro. Para un BMW diésel que hace casi todo en trayectos cortos, eso es una ventaja: unos kilómetros a régimen constante permiten que el filtro de partículas complete la regeneración sin forzar nada.",
             "Si el cuadro avisa de filtro saturado, no lo ignores: una regeneración que no termina acaba en limpieza o sustitución.",
         ]},
        {"id": "villanueva-en-cifras", "h2": "6.666 vecinos en 11,2 km²",
         "parrafos": [
             "El padrón de 2025 da a Villanueva de la Torre 6.666 habitantes, frente a 6.443 en 2015 (un 3,5 % más), en un término de 11,2 km² situado a unos 715 metros de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Guadalajara?",
         "a": "No. El concesionario es AutoPremier, en el Paseo de la Estación 23. Somos un taller independiente en Alcobendas."},
        {"q": "¿Recogéis el coche en Villanueva de la Torre?",
         "a": "No: la recogida del taller solo cubre el área metropolitana de Madrid."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "47,6 km por la CM-1008, la A-2, la R-2 y la M-50."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "6.666 habitantes (+3,5 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "11,2 km²", **F.cartociudad},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 715 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier (Guadalajara) · 18,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 47,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
META["villanueva-de-la-torre"] = "Villanueva de la Torre: concesionario BMW en Guadalajara, a 18,3 km, y taller independiente especializado en BMW y MINI en Alcobendas, a 47,6 km por la A-2."

# ---------------------------------------------------------------- Dosrius
CIUDADES["dosrius"] = {
    "h1": "Dosrius, Maresme de interior: dónde llevar el BMW",
    "entradilla": "Con la C-60 a 2,7 km del centro y un 20,6 % más de vecinos que hace diez años, en Dosrius casi todo se hace en coche. Esto es lo que tienes en Mataró y Argentona y lo que supone ir a Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 49.5},
    "secciones": [
        {"id": "pruna-mataro", "h2": "Pruna Motor, en Mataró, a 12 km",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la Via Sergia 2 de Mataró, a 12 km por carretera. Las campañas de llamada a revisión que convoque BMW se hacen en la red oficial; todo lo demás puedes hacerlo donde prefieras.",
         ]},
        {"id": "itv-el-cros", "h2": "La ITV de Argentona, en el polígono El Cros",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es la de Argentona (B08), a 11,6 km del centro de Dosrius, aunque en línea recta son solo 6,6. La diferencia la marcan las carreteras del interior del Maresme.",
         ]},
        {"id": "cincuenta-km", "h2": "Casi cincuenta kilómetros por la C-60 y la C-32",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc arranca por la B-510, enlaza con la C-60 y la C-32 y cruza por la B-20: 49,5 km por carretera. Dosrius no está en el Área Metropolitana de Barcelona y la recogida del taller no llega hasta aquí.",
             "El viaje compensa para lo que un taller generalista no resuelve: una codificación tras cambiar una centralita, un fallo del cambio automático, una distribución ruidosa en un N47. Para el aceite y los filtros, un taller cercano te ahorra kilómetros.",
         ]},
        {"id": "dosrius-crece", "h2": "De 5.215 a 6.287 habitantes",
         "parrafos": [
             "Dosrius ha pasado de 5.215 vecinos en 2015 a 6.287 en 2025, según el padrón. Idescat contaba 3.316 turismos en 2024, 527 por cada mil vecinos, en un término de 40,73 km². Con tanto recorrido por carretera secundaria, frenos y suspensión trabajan más que en ciudad.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Dosrius?",
         "a": "Pruna Motor, en la Via Sergia 2 de Mataró, a 12 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima por carretera es la de Argentona (B08), a 11,6 km."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 49,5 km por carretera, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "6.287 habitantes (+20,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("080752")},
        {"etiqueta": "Turismos (2024)", "valor": "3.316 · 527 por cada 1.000 hab.", **F.idescat("080752")},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 11,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 12 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 49,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080752"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
