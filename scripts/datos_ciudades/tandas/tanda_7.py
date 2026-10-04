# Tanda 7: Sant Climent de Llobregat, Santa Susanna, Quijorna, Sant Cebrià de Vallalta, Òdena,
# Santa Oliva, Calaf, Caldes d'Estrac, Sant Julià de Vilatorta, Valdilecha, Monistrol de Montserrat,
# Sant Esteve de Palautordera, Tielmes, Los Santos de la Humosa, Galápagos.
# Ninguna de la lista de exclusiones del coordinador cae en esta tanda: se escriben las 15.
# Galápagos: la ITV del fichero es de OpenStreetMap (verificar: true), así que no se publica.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py.
# META: metaDescription nueva para ciudades sin impresiones cuya descripción actual
# contenía promesas («hasta un 50 %», ISTA, «oficial», garantía por escrito, recogida,
# presupuesto cerrado o gratis, presencia en la zona).
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
NATURAL_EARTH = {"fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"}

META = {
    "sant-climent-de-llobregat": "Taller especialista BMW y MINI a 12,6 km de Sant Climent de Llobregat, en Sant Joan Despí. Recogida en el área metropolitana sujeta a disponibilidad.",
    "quijorna": "BMW en Quijorna: servicio oficial en Majadahonda, ITV en la M-506 y el taller especialista de la red en Alcobendas, a 51,3 km por la M-40 y la A-1.",
    "odena": "BMW en Òdena: ITV de Igualada a 2,4 km, servicio oficial en Sant Fruitós de Bages y taller especialista de la red a 53,1 km, todo por la A-2.",
    "santa-oliva": "BMW en Santa Oliva: ITV del Baix Penedès en Bellvei, servicio oficial en Vilanova i la Geltrú y taller especialista de la red a 62,6 km.",
    "calaf": "BMW en Calaf: servicio oficial en Tàrrega, ITV en Igualada y el taller especialista de la red en Sant Joan Despí, a 78,1 km por la A-2.",
    "caldes-d-estrac": "BMW en Caldes d'Estrac: el coche a menos de un kilómetro del mar, servicio oficial en Mataró y taller especialista de la red a 51,8 km por la C-32.",
    "valdilecha": "BMW en Valdilecha: ITV en Arganda del Rey, servicio oficial en Alcalá de Henares y taller especialista de la red en Alcobendas, a 55,1 km.",
    "monistrol-de-montserrat": "BMW en Monistrol de Montserrat: ITV en Manresa, servicio oficial en Sant Fruitós de Bages y taller especialista de la red a 39,2 km por la A-2.",
    "sant-esteve-de-palautordera": "BMW en Sant Esteve de Palautordera: ITV en Sant Celoni a 11,2 km, servicio oficial en Granollers o Mataró y taller especialista de la red a 63,8 km.",
    "tielmes": "BMW en Tielmes: ITV en Villarejo de Salvanés, servicio oficial en la A-3 y taller especialista de la red en Alcobendas, a 58,9 km.",
    "santos-de-la-humosa-los": "BMW en Los Santos de la Humosa: ITV y servicio oficial en la Vía Complutense de Alcalá y taller especialista de la red a 41,3 km.",
    "galapagos": "BMW en Galápagos (Guadalajara): concesionario en Guadalajara, a 23,8 km, y el taller especialista de la red en Alcobendas, a 44,9 km.",
}

# ---------------------------------------------------------------------------
CIUDADES["sant-climent-de-llobregat"] = {
    "h1": "Sant Climent de Llobregat: taller BMW a 12,6 km y recogida dentro del AMB",
    "entradilla": "Pocos municipios de la red tienen el taller tan a mano y además entran en la recogida del coche. Sant Climent es uno: forma parte del Área Metropolitana de Barcelona y la nave de Dasercars está a 12,6 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 12.6},
    "secciones": [
        {"id": "dentro-del-amb", "h2": "Uno de los 36 municipios del área metropolitana",
         "parrafos": [
             "Sant Climent de Llobregat está en la lista oficial del AMB, y eso cuenta: el taller ofrece recogida y entrega del coche y vehículo de cortesía dentro del área metropolitana. Ninguna de las dos cosas está garantizada, dependen de la agenda de cada semana, así que lo sensato es pedirlas al reservar la cita.",
             "Si prefieres llevarlo tú, el trayecto hasta el carrer del Tambor del Bruc 3 de Sant Joan Despí es de 12,6 km por carretera y termina por la B-25; en línea recta son 6,3 km.",
         ]},
        {"id": "trayectos-cortos", "h2": "Un pueblo pequeño y un diésel que casi no sale",
         "parrafos": [
             "La única carretera con referencia a menos de tres kilómetros del centro es la BV-2005, a 2,2 km. Con un término de 10,81 km², muchos desplazamientos del día a día son cortos, y para un diésel con filtro de partículas ese es el peor uso: el motor no llega a la temperatura que necesita la regeneración y el filtro se va cargando.",
             "Si el cuadro avisa del filtro o notas que el ventilador sigue girando al aparcar, no lo dejes para más adelante. Una diagnosis a tiempo suele quedarse en una regeneración forzada; esperar acaba a veces en sustitución.",
         ]},
        {"id": "itv-y-oficial", "h2": "Viladecans para la ITV, Sant Boi para el concesionario",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es ITV Viladecans (B07), de Applus, en el carrer Jocelyn Bell 16: 5,4 km. El servicio oficial BMW más cercano según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 6,9 km.",
             "Nosotros no somos ese concesionario: somos un taller independiente que trabaja BMW y MINI.",
         ]},
        {"id": "sant-climent-en-cifras", "h2": "4.187 vecinos y 1.987 turismos",
         "parrafos": [
             "El padrón de 2025 da a Sant Climent 4.187 habitantes, un 4,3 % más que los 4.013 de 2015. Idescat, con datos de la DGT, contaba 1.987 turismos en 2024: 475 por cada 1.000 vecinos. El núcleo está a 87 metros de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Entra Sant Climent en la recogida del coche?",
         "a": "Sí, el municipio forma parte del área metropolitana. La recogida y el vehículo de cortesía están sujetos a disponibilidad: pídelos al reservar."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de Viladecans (B07), en el carrer Jocelyn Bell 16, a 5,4 km por carretera según el registro de la Generalitat."},
        {"q": "¿Por qué se tapona el filtro de partículas en trayectos cortos?",
         "a": "Porque el motor no alcanza la temperatura necesaria para quemar el hollín acumulado y la regeneración no llega a completarse."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.187 habitantes (+4,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082042")},
        {"etiqueta": "Turismos (2024)", "valor": "1.987 · 475 por cada 1.000 hab.", **F.idescat("082042")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecans (B07) · 5,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium (Sant Boi) · 6,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 12,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082042"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["santa-susanna"] = {
    "h1": "Santa Susanna: un BMW a 1,8 km del mar y el taller especialista a 70 km",
    "entradilla": "Con el centro a menos de dos kilómetros de la playa y la ITV en Blanes, lo que más condiciona a un BMW de Santa Susanna es el aire del mar. El taller de la red queda lejos, a 69,9 km, y te explicamos cuándo merece la pena el viaje.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 69.9},
    "secciones": [
        {"id": "aire-salino", "h2": "1,8 km de costa: dónde ataca primero la sal",
         "parrafos": [
             "El núcleo urbano está a 1,8 km de la línea de costa. La humedad salina no se ve, pero trabaja todo el año sobre las piezas metálicas sin pintar: soportes del escape, abrazaderas, tornillería de los bajos y latiguillos de freno. Si el coche duerme en la calle, revísalas cada vez que esté en el elevador.",
             "Los discos son el otro punto sensible. Un coche que pasa una semana sin moverse cerca del mar amanece con una capa de óxido que suele desaparecer en las primeras frenadas; si en lugar de eso aparece vibración en el pedal, el disco se ha marcado y conviene medirlo.",
         ]},
        {"id": "blanes-y-mataro", "h2": "ITV en Blanes, servicio oficial en Mataró",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Blanes (G07), en la avinguda de l'Estació 47, a 9,7 km. El punto oficial BMW más cercano según bmw.es es Pruna Motor, en la Via Sèrgia 2 de Mataró, a 32,7 km: ahí van las campañas del fabricante y las reparaciones cubiertas por la garantía de BMW.",
         ]},
        {"id": "n2-c32-b20", "h2": "69,9 km por la N-II, la C-32 y la B-20",
         "parrafos": [
             "Hasta la nave de Dasercars Barcelona, en Sant Joan Despí, se baja por la N-II, que pasa a 0,6 km del centro, se sigue por la C-32 y se termina por la B-20: 69,9 km por carretera, 62 en línea recta. Santa Susanna no está en el área metropolitana, así que la recogida del taller no llega aquí.",
             "Con esa distancia, el viaje encaja para una avería que se resiste, un testigo eléctrico intermitente —los conectores corroídos son sospechosos habituales en la costa— o el mantenimiento de un diésel N47 o B47 por el plan de marca. Para unas pastillas, mejor un taller del Maresme.",
         ]},
        {"id": "un-cuarto-mas", "h2": "Un 25,2 % más de vecinos que en 2015",
         "parrafos": [
             "Santa Susanna ha pasado de 3.275 habitantes en 2015 a 4.099 en 2025, según el padrón. En 2024 tenía 1.984 turismos censados (Idescat a partir de la DGT), 484 por cada 1.000 vecinos, en un término de 12,63 km².",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Santa Susanna?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Blanes (G07), en la avinguda de l'Estació 47, a 9,7 km."},
        {"q": "¿Recogéis el coche en Santa Susanna?",
         "a": "No. La recogida del taller se limita al área metropolitana de Barcelona."},
        {"q": "¿Cada cuánto conviene lavar los bajos si vivo junto al mar?",
         "a": "Después del verano y siempre que el coche haya estado mucho tiempo parado cerca de la playa, con agua dulce y sin presión excesiva sobre conectores."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.099 habitantes (+25,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082613")},
        {"etiqueta": "Turismos (2024)", "valor": "1.984 · 484 por cada 1.000 hab.", **F.idescat("082613")},
        {"etiqueta": "Distancia a la costa", "valor": "1,8 km desde el centro", **NATURAL_EARTH},
        {"etiqueta": "ITV más cercana", "valor": "Blanes (G07) · 9,7 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 69,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082613"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["quijorna"] = {
    "h1": "Quijorna: del oeste de Madrid al taller BMW de Alcobendas, 51,3 km",
    "entradilla": "En diez años Quijorna ha pasado de 3.196 a 4.044 vecinos, y el coche es casi obligatorio. Lo que te queda cerca está en Majadahonda y Alcorcón; el taller especialista de la red, al otro lado de la M-40.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 51.3},
    "secciones": [
        {"id": "majadahonda-alcorcon", "h2": "Concesionario en Majadahonda, ITV en la M-506",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más próximo es Movilnorte, en la carretera de El Plantío 62 de Majadahonda, a 24,3 km por carretera. En el listado de la Comunidad de Madrid, las dos estaciones ITV más cercanas por carretera quedan casi a la par: la de ITV Villaviciosa (estación 2871), en la M-506, punto kilométrico 4,200, término de Alcorcón, a 21,8 km, y la de TÜV SÜD ATISAE (2816), en Las Rozas, a 22.",
             "Están a una distancia parecida pero en direcciones distintas, así que no esperes resolver las dos cosas en el mismo viaje.",
         ]},
        {"id": "m40-hacia-el-norte", "h2": "M-521, M-503 y M-40 hasta la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 de Alcobendas sale por la M-521, que pasa a cien metros del centro, enlaza con la M-600 y la M-503 y rodea Madrid por la M-40 hasta la A-1: 51,3 km por carretera, 36,4 en línea recta.",
             "El taller tiene recogida y entrega del coche dentro del área metropolitana de Madrid, siempre sujeta a disponibilidad. Desde aquí, confírmalo al pedir cita antes de contar con ello.",
         ]},
        {"id": "cuando-merece", "h2": "Qué tipo de trabajo justifica el viaje",
         "parrafos": [
             "Un cambio de neumáticos no. Lo que suele justificarlo es un problema que pide conocer la marca: un diésel de la familia N47 o B47 con ruido de distribución, una caja automática que da tirones, o una avería eléctrica que vuelve después de borrar los errores. El taller tiene además homologación REDISTA para escape y gases.",
         ]},
        {"id": "quijorna-en-cifras", "h2": "2.225 turismos para 4.044 vecinos",
         "parrafos": [
             "El padrón pasó de 3.196 habitantes en 2015 a 4.044 en 2025, un 26,5 % más. La Comunidad de Madrid, a partir de la DGT, contaba 2.225 turismos en 2025: 550 por cada 1.000 habitantes. El término ocupa 25,5 km² a 591 metros de altitud, con la M-521 y la M-522 pegadas al casco.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el concesionario BMW más cercano a Quijorna?",
         "a": "Movilnorte, en la carretera de El Plantío 62 de Majadahonda, a 24,3 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más cercana por carretera en el listado oficial es la de ITV Villaviciosa, en la M-506, km 4,200 (Alcorcón), a 21,8 km; la de TÜV SÜD ATISAE en Las Rozas queda a 22."},
        {"q": "¿A cuánto queda vuestro taller?",
         "a": "A 51,3 km, en la calle Valgrande 17 de Alcobendas, por la M-40 y la A-1."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "4.044 habitantes (+26,5 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "2.225 · 550 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "ITV Villaviciosa, M-506 km 4,2 (Alcorcón) · 21,8 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte (Majadahonda) · 24,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 51,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------------------
CIUDADES["sant-cebria-de-vallalta"] = {
    "h1": "Sant Cebrià de Vallalta: un BMW a 3,2 km del mar y a 61,2 del taller",
    "entradilla": "A 3,2 km del mar pero ya en el interior del Maresme, Sant Cebrià tiene una particularidad: la ITV más próxima por carretera ya está en la provincia de Girona, en Blanes, a 20,5 km. El taller de la red, a 61,2 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 61.2},
    "secciones": [
        {"id": "itv-blanes", "h2": "La ITV, en Blanes: más cerca al volante que Sant Celoni",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es ITV Blanes (G07), en la avinguda de l'Estació 47, a 20,5 km (15,9 en línea recta). La de Sant Celoni (B26) parece más cerca en el mapa, a 11,6 km en línea recta, pero por carretera son 22,4.",
             "Por eso conviene llegar a la inspección con el coche revisado: repetir el viaje por un defecto leve de luces o de neumáticos sale caro en tiempo.",
         ]},
        {"id": "humedad-a-3-km", "h2": "Tres kilómetros del mar, más humedad que sal",
         "parrafos": [
             "El centro queda a 3,2 km de la costa. Es menos que primera línea, pero suficiente para que la humedad marina acelere la corrosión de lo que no está protegido: escape, anclajes y algunos conectores de los bajos. Una revisión visual de esas zonas cuando el coche pasa por un cambio de aceite cuesta poco.",
         ]},
        {"id": "c32-hasta-sant-joan", "h2": "Por la C-32 hasta Sant Joan Despí",
         "parrafos": [
             "La C-32 pasa a 1,6 km del centro y es casi toda la ruta: C-32 y B-20 hasta el carrer del Tambor del Bruc 3, 61,2 km por carretera y 52,9 en línea recta. El municipio no forma parte del área metropolitana, así que la recogida del taller no llega.",
             "El servicio oficial BMW más cercano según bmw.es está a 24 km: Pruna Motor, en la Via Sèrgia 2 de Mataró. Nosotros somos la opción independiente, especializada en BMW y MINI.",
         ]},
        {"id": "sant-cebria-en-cifras", "h2": "3.872 vecinos y 1.907 turismos",
         "parrafos": [
             "El padrón de 2025 da 3.872 habitantes, un 16,4 % más que los 3.326 de 2015, en 15,8 km² a 71 metros de altitud. Idescat contaba 1.907 turismos en 2024 a partir de la DGT: 493 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV me corresponde desde Sant Cebrià?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Blanes (G07), en la avinguda de l'Estació 47, a 20,5 km. Sant Celoni (B26) queda a 22,4."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 24 km según bmw.es."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW: comparten electrónica y buena parte de los motores."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.872 habitantes (+16,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("082037")},
        {"etiqueta": "Turismos (2024)", "valor": "1.907 · 493 por cada 1.000 hab.", **F.idescat("082037")},
        {"etiqueta": "ITV más cercana", "valor": "Blanes (G07) · 20,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 24 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 61,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082037"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["odena"] = {
    "h1": "Òdena: ITV a 2,4 km y taller especialista BMW a 53 km sin salir de la A-2",
    "entradilla": "Desde Òdena, la estación ITV de Igualada está prácticamente al lado y el taller de la red se alcanza por una sola autovía. Lo que no tienes cerca es el concesionario, a 35 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 53.1},
    "secciones": [
        {"id": "toda-la-a2", "h2": "53,1 km, toda la ruta por la A-2",
         "parrafos": [
             "La A-2 pasa a 0,8 km del centro y es el único eje que hace falta: por ella se llega hasta Sant Joan Despí, donde está la nave de Dasercars Barcelona, en el carrer del Tambor del Bruc 3. Son 53,1 km por carretera y 44 en línea recta.",
             "Òdena no pertenece al área metropolitana y la recogida del taller no llega. Antes de bajar, apunta cuándo aparece la avería —en frío, en caliente, a qué marcha— y con qué testigo: ese dato ahorra más diagnosis que cualquier otra cosa.",
         ]},
        {"id": "itv-les-comes", "h2": "La ITV de Igualada, en el polígono Les Comes",
         "parrafos": [
             "La estación más próxima por carretera del registro de la Generalitat es ITV Igualada (B12), de Applus, en el carrer Països Baixos 18 del polígono Les Comes: 2,4 km desde el centro de Òdena. Con la inspección tan cerca, una pre-ITV en un taller de la comarca tiene más lógica que bajar a Barcelona solo para eso.",
         ]},
        {"id": "concesionario-bages", "h2": "El servicio oficial más próximo, en el Bages",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más cercano es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 35 km por carretera. Es el sitio para las campañas de revisión que convoque la marca.",
             "Para el resto, el Reglamento (UE) 461/2010 deja elegir taller sin perder la garantía siempre que el mantenimiento siga el plan y las especificaciones de BMW.",
         ]},
        {"id": "odena-en-cifras", "h2": "615 turismos por cada mil vecinos",
         "parrafos": [
             "Òdena tenía 3.760 habitantes en 2025 (3.623 en 2015) repartidos en un término amplio, de 52,66 km², a 421 metros. Idescat, con datos de la DGT, contaba 2.312 turismos en 2024: 615 por cada 1.000 habitantes, más del doble que los 281 de Barcelona ciudad.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Òdena?",
         "a": "En ITV Igualada (B12), polígono Les Comes, a 2,4 km por carretera."},
        {"q": "¿Cómo llego al taller?",
         "a": "Por la A-2 de principio a fin: 53,1 km hasta Sant Joan Despí."},
        {"q": "¿Pierdo la garantía si no voy al concesionario?",
         "a": "No, mientras el mantenimiento respete los intervalos y especificaciones del plan de BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.760 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("081430")},
        {"etiqueta": "Turismos (2024)", "valor": "2.312 · 615 por cada 1.000 hab.", **F.idescat("081430")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 2,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 35 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 53,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081430"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["santa-oliva"] = {
    "h1": "Santa Oliva: seis carreteras alrededor y el taller BMW a 62,6 km",
    "entradilla": "La AP-7, la AP-2 y la N-340 pasan a menos de tres kilómetros del centro de Santa Oliva. Es provincia de Tarragona, pero el taller especialista que te atiende está en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 62.6},
    "secciones": [
        {"id": "nudo-de-carreteras", "h2": "AP-7, AP-2 y N-340 a la puerta",
         "parrafos": [
             "En un radio de tres kilómetros desde el centro pasan la TP-2125 (0,6 km), la AP-7 (1,2), la AP-2 (1,9), la N-340 (2,2), la C-51 (2,5) y la TV-2126 (2,6). Para un diésel, tener autopista tan cerca es una ventaja: un tramo a velocidad constante de vez en cuando permite que el filtro de partículas complete su regeneración.",
         ]},
        {"id": "itv-els-massets", "h2": "ITV en Bellvei, a 5,3 km",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la del Baix Penedès (T07), de Itevelesa, en el polígono Els Massets de Bellvei: 5,3 km por carretera, 2,4 en línea recta.",
         ]},
        {"id": "ruta-y-oficial", "h2": "Hasta Sant Joan Despí por la C-32, o a Vilanova por lo oficial",
         "parrafos": [
             "La ruta al taller sale por la TP-2125, toma la C-31 y la C-32 y termina por la B-25: 62,6 km por carretera y 44,6 en línea recta. Santa Oliva no está en el área metropolitana de Barcelona, así que el coche lo traes tú.",
             "El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 27,2 km. Para una reparación cubierta por la garantía de BMW, es la referencia.",
         ]},
        {"id": "antes-de-bajar", "h2": "Antes de hacer 62,6 kilómetros",
         "parrafos": [
             "Llama con el modelo, el año y lo que notas. Con el bastidor se identifica la referencia exacta de cada recambio y, si el trabajo lo requiere, se pide antes de que llegue el coche. El presupuesto lo tienes por escrito y nada empieza sin que lo apruebes.",
             "El municipio tenía 3.711 habitantes en 2025, un 13 % más que en 2015, y 2.254 turismos en 2024 según Idescat a partir de la DGT: 607 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está la ITV más cercana a Santa Oliva?",
         "a": "En el polígono Els Massets de Bellvei: estación Baix Penedès (T07), a 5,3 km por carretera."},
        {"q": "¿Por qué me atiende un taller de Barcelona si estoy en Tarragona?",
         "a": "Porque el taller de la red más próximo es Dasercars Barcelona, en Sant Joan Despí, a 62,6 km."},
        {"q": "¿Recogéis el coche?",
         "a": "No en Santa Oliva: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.711 habitantes (+13 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Penedès", **F.idescat("431401")},
        {"etiqueta": "Turismos (2024)", "valor": "2.254 · 607 por cada 1.000 hab.", **F.idescat("431401")},
        {"etiqueta": "ITV más cercana", "valor": "Baix Penedès (T07), Bellvei · 5,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vilanova i la Geltrú) · 27,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 62,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("431401"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["calaf"] = {
    "h1": "Calaf: el concesionario BMW más cercano está en Tàrrega, el taller a 78 km",
    "entradilla": "Desde Calaf, nada de lo relacionado con BMW queda a menos de 27,4 km. El servicio oficial más próximo ni siquiera está en la provincia de Barcelona. Así se organiza el mantenimiento desde aquí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 78.1},
    "secciones": [
        {"id": "tarrega-igualada", "h2": "Tàrrega para el concesionario, Igualada para la ITV",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo a Calaf es Unicars Ponent, en el carrer de la Conca de Barberà (nave 6) de Tàrrega, a 34,4 km por carretera. La estación ITV más próxima por carretera en el registro de la Generalitat es la de Igualada (B12), en el polígono Les Comes, a 27,4 km.",
             "Las dos están en direcciones opuestas, así que cada visita es un viaje propio.",
         ]},
        {"id": "a2-hasta-el-taller", "h2": "78,1 km por la C-1412a y la A-2",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona, en Sant Joan Despí, baja por la C-1412a hasta la A-2 y ya no la deja: 78,1 km por carretera, 61,4 en línea recta. La recogida del taller cubre solo el área metropolitana, así que desde aquí no llega.",
         ]},
        {"id": "que-si-que-no", "h2": "Qué vale el viaje y qué no",
         "parrafos": [
             "No lo vale una revisión de rutina, que puede hacerse en cualquier taller cercano con el aceite de la homologación correcta. Sí lo vale un problema que se repite sin solución: un fallo del sistema de AdBlue, un ruido de cadena en un diésel N47 o N57, una caja que cambia mal o una avería eléctrica que nadie localiza.",
             "Desde 78 km, la llamada previa no es opcional. Con el síntoma bien descrito se puede orientar el problema y decidir si el viaje compensa.",
         ]},
        {"id": "calaf-en-cifras", "h2": "A 680 metros, con 1.880 turismos",
         "parrafos": [
             "Calaf tenía 3.644 vecinos en 2025, un 6,4 % más que en 2015, en un término compacto de 9,22 km² a 680 metros de altitud. Idescat contaba 1.880 turismos en 2024 a partir de la DGT, 516 por cada 1.000 habitantes. La C-1412a, la BV-1001 y la C-25 pasan a menos de un kilómetro del centro.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Calaf?",
         "a": "Unicars Ponent, en Tàrrega, a 34,4 km por carretera según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Igualada (B12), a 27,4 km, según el registro de la Generalitat."},
        {"q": "¿Tenéis taller cerca de Calaf?",
         "a": "No. El taller de la red más próximo está en Sant Joan Despí, a 78,1 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.644 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("080312")},
        {"etiqueta": "Altitud", "valor": "680 m", **F.idescat("080312")},
        {"etiqueta": "Turismos (2024)", "valor": "1.880 · 516 por cada 1.000 hab.", **F.idescat("080312")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 27,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent (Tàrrega) · 34,4 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080312"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["caldes-d-estrac"] = {
    "h1": "Caldes d'Estrac: un BMW en menos de un kilómetro cuadrado junto al mar",
    "entradilla": "El término de Caldes d'Estrac mide 0,88 km² y el centro está a 0,9 km de la costa. Para un coche, eso significa sal todo el año. El concesionario está en Mataró y el taller especialista de la red, a 51,8 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 51.8},
    "secciones": [
        {"id": "primera-linea", "h2": "Coche de primera línea: lo que hay que vigilar",
         "parrafos": [
             "Con el mar a 0,9 km y la mayoría de coches aparcados en la calle, la corrosión no es una posibilidad sino un proceso. Lo primero que lo acusa es lo que va por debajo: escape, sus anclajes, abrazaderas y protecciones de los bajos. Lo segundo, la electricidad: un conector sulfatado puede dar un testigo que aparece y desaparece sin patrón aparente.",
             "Dos hábitos ayudan mucho: aclarar los bajos con agua dulce después del verano y mover el coche si va a estar días parado, para que los discos no se queden marcados por el óxido.",
         ]},
        {"id": "mataro-al-lado", "h2": "Mataró a 10,7 km; la ITV, en Argentona",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Pruna Motor, en la Via Sèrgia 2 de Mataró, a 10,7 km por carretera. La estación ITV más próxima por carretera del registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 14,2 km.",
         ]},
        {"id": "c32-al-taller", "h2": "Por la C-32 hasta Sant Joan Despí",
         "parrafos": [
             "La N-II cruza el pueblo a 0,2 km del centro y la C-32 queda a 0,8. Por la C-32 y la B-20 se llega a la nave de Dasercars Barcelona: 51,8 km por carretera, 44,8 en línea recta. Caldes no está dentro del área metropolitana, así que la recogida del coche no llega.",
             "Si vas a hacer el viaje por una avería concreta, describe por teléfono qué pasa y cuándo; con un BMW o un MINI de costa, revisar los conectores suele ser parte del diagnóstico.",
         ]},
        {"id": "densidad", "h2": "3.814 habitantes por kilómetro cuadrado",
         "parrafos": [
             "En 2025 vivían en Caldes 3.356 personas, un 23,5 % más que las 2.717 de 2015. En un término tan pequeño eso da 3.814 habitantes por km². Idescat contaba 1.679 turismos en 2024 a partir de la DGT: 500 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 10,7 km según bmw.es."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de Argentona (B08), en el polígono El Cros, a 14,2 km por carretera."},
        {"q": "¿Por qué falla la electricidad de los coches cerca del mar?",
         "a": "La humedad salina sulfata los conectores expuestos, y un mal contacto produce avisos intermitentes que no siempre dejan un error claro."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.356 habitantes (+23,5 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "0,88 km²", **F.cartociudad},
        {"etiqueta": "Turismos (2024)", "valor": "1.679 · 500 por cada 1.000 hab.", **F.idescat("080327")},
        {"etiqueta": "Distancia a la costa", "valor": "0,9 km desde el centro", **NATURAL_EARTH},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 10,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 51,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.idescat_f("080327"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["sant-julia-de-vilatorta"] = {
    "h1": "Sant Julià de Vilatorta: concesionario e ITV en Vic, especialista BMW a 90 km",
    "entradilla": "Para casi todo lo que necesita un BMW o un MINI, desde Sant Julià de Vilatorta basta con ir a Vic. El taller de la red está a 90,3 km y no lo vamos a presentar como si estuviera cerca.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 90.3},
    "secciones": [
        {"id": "todo-en-vic", "h2": "Vic, a ocho kilómetros, resuelve lo habitual",
         "parrafos": [
             "La estación ITV más próxima por carretera en el registro de la Generalitat es ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22 de Vic, a 7,6 km. El servicio oficial BMW según bmw.es está en la misma ciudad: Quadis Munich, en la calle Perot Rocaguinarda 1, a 8,1 km.",
             "Lo rutinario, por tanto, se queda en Osona.",
         ]},
        {"id": "cuando-bajar", "h2": "Cuándo sí tiene sentido bajar 90 km",
         "parrafos": [
             "Cuando lo que buscas es una alternativa independiente para algo que no se ha resuelto: un diésel con fallos repetidos del filtro de partículas o del AdBlue, una avería eléctrica intermitente o un segundo diagnóstico antes de una reparación cara. También para un trabajo de escape o emisiones, porque el taller tiene homologación REDISTA.",
             "La ruta sale por la BV-5201 a la C-25, baja por la C-17 y la C-33 y termina por la B-20: 90,3 km por carretera, 65,3 en línea recta. La recogida del taller no llega hasta aquí: cubre solo el área metropolitana.",
         ]},
        {"id": "seiscientos-metros", "h2": "Un coche a 600 metros en la plana de Vic",
         "parrafos": [
             "El núcleo está a 600 metros de altitud y la C-25 pasa a 1,3 km. Las mañanas frías de la plana ponen a prueba la batería, sobre todo en un BMW con arranque y parada automático. Si hay que cambiarla, la nueva se registra en la centralita para que la carga se ajuste a ella.",
         ]},
        {"id": "en-cifras", "h2": "3.323 vecinos y 1.860 turismos",
         "parrafos": [
             "El padrón de 2025 da 3.323 habitantes (3.104 en 2015, un 7,1 % más) en 15,94 km². Idescat contaba 1.860 turismos en 2024 a partir de la DGT: 560 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV?",
         "a": "En ITV Osona (B04), en Vic, a 7,6 km por carretera según el registro de la Generalitat."},
        {"q": "¿Tenéis taller en Osona?",
         "a": "No. El taller de la red más próximo es Dasercars Barcelona, en Sant Joan Despí, a 90,3 km."},
        {"q": "¿Por qué hay que registrar la batería de un BMW?",
         "a": "La centralita adapta la carga a la batería que tiene registrada; si no se registra la nueva, se carga de forma incorrecta."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.323 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082205")},
        {"etiqueta": "Turismos (2024)", "valor": "1.860 · 560 por cada 1.000 hab.", **F.idescat("082205")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 7,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 8,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 90,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082205"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["valdilecha"] = {
    "h1": "Valdilecha y su BMW: Arganda para la ITV, Alcobendas para el especialista",
    "entradilla": "Desde la comarca del Tajuña, todo lo que tiene que ver con un BMW obliga a coger la carretera. La ITV más próxima está en Arganda del Rey, el servicio oficial en Alcalá de Henares y el taller de la red en Alcobendas, a 55,1 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 55.1},
    "secciones": [
        {"id": "itv-arganda", "h2": "La ITV, en el camino de San Martín de la Vega",
         "parrafos": [
             "La estación más próxima por carretera en el listado de la Comunidad de Madrid es la de Laboratorio e Inspección de Vehículos (estación 2807), en el camino de San Martín de la Vega 8 de Arganda del Rey: 16,2 km por carretera, 13,3 en línea recta. La 2852, de General de Servicios ITV y también en Arganda, queda casi igual, a 16,9.",
         ]},
        {"id": "a3-m30-a1", "h2": "Por la A-3 y la M-30 hasta la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 de Alcobendas sale por la M-229, que pasa a medio kilómetro del centro, toma la N-IIIa y la A-3 hacia Madrid, cruza por la M-30 y sale por la A-1: 55,1 km por carretera, 40,3 en línea recta.",
             "Para un viaje así, conviene que el trabajo esté definido antes de salir: con el modelo, el año y el síntoma se puede orientar el problema, y si hace falta una pieza concreta, tenerla el día de la cita.",
         ]},
        {"id": "alcala-garantia", "h2": "Servicio oficial en Alcalá y la garantía",
         "parrafos": [
             "El punto oficial BMW más próximo según bmw.es es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 28,3 km por la ruta más corta (unos 33,8 por la más rápida). Allí se tramitan las reparaciones que paga la garantía de BMW.",
             "Las revisiones periódicas, en cambio, no tienen por qué hacerse allí: la normativa europea permite hacerlas en un taller independiente sin perder la garantía, con los intervalos y los recambios que marca el fabricante.",
         ]},
        {"id": "valdilecha-en-cifras", "h2": "Un 15,9 % más de vecinos en diez años",
         "parrafos": [
             "Valdilecha pasó de 2.838 habitantes en 2015 a 3.289 en 2025. La Comunidad de Madrid, a partir de la DGT, contaba 1.733 turismos en 2025: 527 por cada 1.000 vecinos. El término es amplio, 42,3 km², y el casco está a 674 metros.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Valdilecha?",
         "a": "La más próxima por carretera es la estación 2807, en el camino de San Martín de la Vega 8 de Arganda del Rey, a 16,2 km; la 2852, también en Arganda, a 16,9."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "AutoPremier, en la Vía Complutense de Alcalá de Henares, a 28,3 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "55,1 km por la A-3, la M-30 y la A-1, hasta la calle Valgrande 17 de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.289 habitantes (+15,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "1.733 · 527 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "Estación 2807, Arganda del Rey · 16,2 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier (Alcalá de Henares) · 28,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 55,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------------------
CIUDADES["monistrol-de-montserrat"] = {
    "h1": "Monistrol de Montserrat: el taller BMW de la red a 39,2 km por la A-2",
    "entradilla": "De los municipios del Bages en la red, Monistrol es de los que tienen el taller más a mano: menos de 40 km. La C-55 pasa por el mismo centro y lleva directa a la A-2.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 39.2},
    "secciones": [
        {"id": "c55-a2", "h2": "C-55 y A-2: 39,2 km hasta Sant Joan Despí",
         "parrafos": [
             "La C-55 pasa a cien metros del centro. Por ella se baja hasta la A-2, y la A-2 lleva hasta la nave de Dasercars Barcelona, en el carrer del Tambor del Bruc 3: 39,2 km por carretera, 32,8 en línea recta.",
             "El taller abre de lunes a viernes, en jornada partida de 9:00 a 14:00 y de 15:00 a 18:00. A esta distancia es posible dejar el coche por la mañana y volver por él a última hora. Monistrol queda fuera del área metropolitana y la recogida no llega.",
         ]},
        {"id": "itv-y-concesionario", "h2": "Manresa para la ITV, Sant Fruitós para el concesionario",
         "parrafos": [
             "La estación ITV más próxima por carretera en el registro de la Generalitat es ITV Manresa (B06), de TÜV Rheinland, en el carrer Esteve Terrades 2-4 del polígono Bufalvent: 14,5 km. El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 20,9 km.",
         ]},
        {"id": "subidas-y-bajadas", "h2": "Carreteras con desnivel",
         "parrafos": [
             "Además de la C-55, en tres kilómetros a la redonda pasan la C-58 (1,4 km), la BP-1103 (1,5) y la C-16 (2,5). Quien sube y baja a menudo por carreteras con pendiente gasta más frenos que en llano, y el líquido de frenos, que absorbe humedad con el tiempo, merece cambiarse cuando toca por plan aunque el coche haga pocos kilómetros.",
         ]},
        {"id": "monistrol-en-cifras", "h2": "3.250 vecinos y 1.662 turismos",
         "parrafos": [
             "El padrón de 2025 da a Monistrol 3.250 habitantes, un 12 % más que los 2.901 de 2015, en 11,77 km² a 161 metros de altitud. Idescat, con datos de la DGT, contaba 1.662 turismos en 2024: 511 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿A cuánto está vuestro taller desde Monistrol?",
         "a": "A 39,2 km por la C-55 y la A-2, en Sant Joan Despí."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "ITV Manresa (B06), en el polígono Bufalvent, a 14,5 km por carretera."},
        {"q": "¿El líquido de frenos se cambia por kilómetros?",
         "a": "No, por tiempo, según el plan de mantenimiento: pierde propiedades al absorber humedad aunque el coche se use poco."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.250 habitantes (+12 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("081271")},
        {"etiqueta": "Turismos (2024)", "valor": "1.662 · 511 por cada 1.000 hab.", **F.idescat("081271")},
        {"etiqueta": "ITV más cercana", "valor": "Manresa (B06) · 14,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 20,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 39,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081271"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["sant-esteve-de-palautordera"] = {
    "h1": "Sant Esteve de Palautordera: ITV en Sant Celoni y especialista BMW por la AP-7",
    "entradilla": "El servicio oficial BMW más próximo está en Mataró, a 30,1 km. La ITV sí está a mano, en Sant Celoni, y el taller de la red a 63,8 km por la AP-7.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 63.8},
    "secciones": [
        {"id": "itv-gualba", "h2": "La ITV de Sant Celoni, en la carretera de Gualba",
         "parrafos": [
             "La estación más próxima por carretera del registro de la Generalitat es ITV Sant Celoni (B26), de TÜV SÜD, en la carretera de Gualba 41-43, a 11,2 km. Si la inspección se acerca y el coche tiene algún testigo encendido, resuélvelo antes: un fallo de emisiones o de airbag es motivo de desfavorable.",
         ]},
        {"id": "pruna-mataro", "h2": "El servicio oficial, en Mataró",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo a Sant Esteve es Pruna Motor, en la Via Sèrgia 2 de Mataró, a 30,1 km por carretera. Para lo que dependa de la garantía de BMW, ese es el sitio.",
             "Para el mantenimiento habitual y las averías fuera de garantía, la alternativa es un taller independiente especializado. Trabajamos BMW y MINI con presupuesto por escrito, y la diagnosis también se presupuesta antes de empezar.",
         ]},
        {"id": "bv5301-ap7", "h2": "63,8 km: BV-5301, AP-7, C-33 y B-20",
         "parrafos": [
             "La BV-5301 pasa a 1,3 km del centro y lleva a la AP-7; desde ahí, C-33 y B-20 hasta la nave de Dasercars Barcelona en Sant Joan Despí. Son 63,8 km por carretera, 49 en línea recta. No hay recogida: el municipio queda fuera del área metropolitana.",
         ]},
        {"id": "crecimiento", "h2": "Un 20,7 % más de vecinos que en 2015",
         "parrafos": [
             "El padrón pasó de 2.568 habitantes en 2015 a 3.099 en 2025, en un término de 10,64 km² a 231 metros. Idescat contaba 1.428 turismos en 2024 a partir de la DGT: 461 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV?",
         "a": "En ITV Sant Celoni (B26), carretera de Gualba 41-43, a 11,2 km por carretera."},
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 30,1 km por carretera según bmw.es."},
        {"q": "¿Puedo pasar la ITV con un testigo encendido?",
         "a": "Depende del testigo, pero los de emisiones, airbag o frenos suelen acabar en desfavorable: mejor diagnosticarlos antes."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.099 habitantes (+20,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("082074")},
        {"etiqueta": "Turismos (2024)", "valor": "1.428 · 461 por cada 1.000 hab.", **F.idescat("082074")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 11,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor (Mataró) · 30,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 63,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082074"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------------------
CIUDADES["tielmes"] = {
    "h1": "Tielmes: ITV en Villarejo de Salvanés y taller BMW a 58,9 km por la A-3",
    "entradilla": "La M-204 atraviesa Tielmes y la A-3 queda a menos de tres kilómetros. Por esa autovía se llega, después de cruzar Madrid, al taller especialista de Alcobendas; el servicio oficial BMW más próximo está en Alcalá de Henares.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 58.9},
    "secciones": [
        {"id": "itv-villarejo", "h2": "La ITV que te queda más cerca, en Villarejo",
         "parrafos": [
             "En el listado de la Comunidad de Madrid, la estación más próxima por carretera es la de General de Servicios ITV (estación 2853), en la avenida Juan Carlos I Rey de España 13 de Villarejo de Salvanés: 12 km.",
         ]},
        {"id": "oficial-alcala", "h2": "Servicio oficial en Alcalá de Henares",
         "parrafos": [
             "Según bmw.es, el punto oficial BMW más cercano es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares: 34,2 km por la ruta más corta; por la más rápida, unos 52. Para una avería en garantía, ese es el sitio.",
             "Fuera de eso, el mantenimiento lo puedes hacer donde prefieras sin perder la garantía, siempre que se cumpla el plan de BMW: intervalos, aceite con la homologación del motor y recambios de calidad equivalente. Lo ampara el Reglamento (UE) 461/2010.",
         ]},
        {"id": "hasta-alcobendas", "h2": "58,9 km: M-204, A-3, M-30 y A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande 17 de Alcobendas sale por la M-204, sigue la A-3 hasta Madrid, cruza por la M-30 y termina por la A-1: 58,9 km por carretera, 43,2 en línea recta.",
             "Es un trayecto largo para un cambio de aceite, pero razonable para un diésel con problemas de filtro de partículas o de AdBlue, una caja automática que da tirones o un aviso que vuelve tras cada borrado.",
         ]},
        {"id": "tielmes-en-cifras", "h2": "563 turismos por cada mil vecinos",
         "parrafos": [
             "Tielmes tenía 2.964 habitantes en 2025, un 14,7 % más que los 2.585 de 2015, y 1.668 turismos censados en 2025 según la Comunidad de Madrid a partir de la DGT: 563 por cada 1.000. Además de la M-204, pasan cerca la M-228, la M-302 y la N-IIIa. El casco está a 715 metros.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Tielmes?",
         "a": "En la estación 2853, avenida Juan Carlos I Rey de España 13, Villarejo de Salvanés, a 12 km por carretera."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 34,2 km según bmw.es."},
        {"q": "¿Puedo hacer las revisiones fuera del concesionario estando en garantía?",
         "a": "Sí, siempre que se respeten intervalos y especificaciones del plan de mantenimiento de BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.964 habitantes (+14,7 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "1.668 · 563 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "Estación 2853, Villarejo de Salvanés · 12 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 34,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 58,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------------------
CIUDADES["santos-de-la-humosa-los"] = {
    "h1": "Los Santos de la Humosa: ITV y concesionario BMW en la misma avenida de Alcalá",
    "entradilla": "Una coincidencia práctica: la ITV y el servicio oficial BMW más próximos a Los Santos de la Humosa están los dos en la Vía Complutense de Alcalá de Henares. El taller especialista de la red, en Alcobendas, a 41,3 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 41.3},
    "secciones": [
        {"id": "via-complutense", "h2": "Vía Complutense 105 y 131",
         "parrafos": [
             "La estación ITV más cercana por carretera en el listado de la Comunidad de Madrid es la de ITVERSIA (estación 2891), en la Vía Complutense 105, a 13,9 km. Unos números más allá, en la Vía Complutense 131, está AutoPremier, el servicio oficial BMW más próximo según bmw.es, a 13 km.",
             "Con las dos cosas en la misma calle, una mañana en Alcalá puede cubrir la inspección y, si toca, una campaña de la marca.",
         ]},
        {"id": "r2-m50", "h2": "Por la M-226 y la R-2 hasta Alcobendas",
         "parrafos": [
             "Hasta la calle Valgrande 17 de Alcobendas, la ruta sale por la M-226, toma la R-2 y entra por la M-50: 41,3 km por carretera, 33,9 en línea recta.",
             "Lo que justifica ese trayecto es lo específico: un BMW con un fallo que vuelve, un sistema de AdBlue que avisa, un diésel de las familias N47, N57, B47 o B57 que pide manos que lo conozcan. Para el resto, decide tú con el presupuesto en la mano: se da por escrito y no se toca nada sin tu visto bueno.",
         ]},
        {"id": "dependencia-del-coche", "h2": "576 turismos por cada mil vecinos",
         "parrafos": [
             "La Comunidad de Madrid, a partir de la DGT, contaba 1.652 turismos en 2025 para 2.867 habitantes: 576 por cada 1.000, frente a los 388 de Madrid capital. Es lo normal en un término de 34,6 km² donde las carreteras más próximas son la M-235, a 0,6 km del centro, y la M-213, a 2,8.",
             "El padrón ha crecido un 20 % desde 2015, cuando había 2.389 vecinos. El casco está a 648 metros de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Los Santos de la Humosa?",
         "a": "En ITVERSIA, Vía Complutense 105 de Alcalá de Henares, a 13,9 km por carretera."},
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 13 km según bmw.es."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "41,3 km por la M-226, la R-2 y la M-50, hasta Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.867 habitantes (+20 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "1.652 · 576 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV más cercana", "valor": "ITVERSIA, Vía Complutense 105 (Alcalá) · 13,9 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Vía Complutense 131 · 13 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 41,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------------------
CIUDADES["galapagos"] = {
    "h1": "Galápagos: tu BMW entre la N-320 y la A-1, con el especialista a 44,9 km",
    "entradilla": "Para un BMW o un MINI de Galápagos hay dos destinos posibles según lo que le pase: AutoPremier, en la capital alcarreña, a 23,8 km, o la nave de Dasercars en Alcobendas, a 44,9. Te explicamos qué va a cada sitio.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 44.9},
    "secciones": [
        {"id": "que-va-a-cada-sitio", "h2": "Garantía en Guadalajara, especialidad en Alcobendas",
         "parrafos": [
             "AutoPremier, en el Paseo de la Estación 23 de Guadalajara, es el punto oficial BMW más próximo que da el localizador de bmw.es. Lo que paga la garantía del fabricante se tramita allí, y está a la mitad de distancia que nuestro taller.",
             "Lo que tiene sentido llevar a un independiente es otra cosa: el mantenimiento cuando el coche ya no está en garantía, un segundo diagnóstico antes de aceptar una reparación cara o una avería concreta de la marca. No somos el concesionario ni trabajamos para él.",
         ]},
        {"id": "seis-carreteras", "h2": "GU-1056, N-320, GU-193 y tres carreteras madrileñas",
         "parrafos": [
             "El camino hasta la calle Valgrande 17 empieza por la GU-1056, enlaza con la N-320 —a 2,7 km del centro— y con la GU-193, y ya en la Comunidad de Madrid encadena la M-117, la M-111 y la M-100 antes de la A-1. En total, 44,9 km por carretera y 31,4 en línea recta.",
             "Al no estar en el área metropolitana de Madrid, Galápagos queda fuera de la recogida del taller.",
         ]},
        {"id": "trabajos-que-compensan", "h2": "Trabajos que compensan los 44,9 km",
         "parrafos": [
             "Un diésel N47 o N57 con ruido de cadena, un aviso de AdBlue con la cuenta atrás en marcha, un fallo de emisiones (el taller tiene homologación REDISTA para escape y gases) o un mantenimiento por plan de marca con el indicador de servicio reiniciado. Un pinchazo o unas escobillas los resuelve cualquier taller cercano.",
             "Desde aquí ayuda mucho describir el síntoma por teléfono: cuándo aparece, en frío o en caliente, y qué testigo se enciende.",
         ]},
        {"id": "galapagos-en-cifras", "h2": "De 2.368 a 2.802 vecinos",
         "parrafos": [
             "El padrón de 2025 da a Galápagos 2.802 habitantes, un 18,3 % más que en 2015. El término mide 33,7 km² y el casco está a 764 metros: en invierno, batería y anticongelante son lo primero que conviene mirar.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué hago con una reparación en garantía?",
         "a": "Llevarla al servicio oficial: el más cercano según bmw.es es AutoPremier, en el Paseo de la Estación 23 de Guadalajara, a 23,8 km."},
        {"q": "¿Por qué carreteras se llega a vuestro taller?",
         "a": "GU-1056, N-320, GU-193, M-117, M-111, M-100 y A-1: 44,9 km hasta Alcobendas."},
        {"q": "¿Trabajáis también MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "2.802 habitantes · 2.368 en 2015", **F.ine},
        {"etiqueta": "Término municipal", "valor": "33,7 km²", **F.cartociudad},
        {"etiqueta": "Altitud", "valor": "764 m", **F.copernicus},
        {"etiqueta": "Concesionario BMW más cercano", "valor": "AutoPremier, Paseo de la Estación 23 · 23,8 km", **F.bmw},
        {"etiqueta": "Dasercars Madrid (Alcobendas)", "valor": "44,9 km por carretera", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
