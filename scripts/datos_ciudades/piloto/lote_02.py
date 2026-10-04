# Piloto (lote 2): Terrassa, Camarma de Esteruelas, Sentmenat, Santpedor, Humanes de Madrid.
from fuentes import F

REVISADO = "2026-10-04"
CIUDADES = {}

CIUDADES["terrassa"] = {
    "h1": "BMW y MINI en Terrassa: especialista independiente a 32 km por la C-16",
    "entradilla": "Terrassa supera los 230.000 habitantes y tiene concesionario oficial propio. Nuestro taller está en Sant Joan Despí; esta página explica cuándo encaja cada opción y dónde pasa la ITV un coche de Terrassa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 32.3},
    "secciones": [
        {"id": "bmw-y-mini", "h2": "También MINI, con el mismo equipo de diagnosis",
         "parrafos": [
             "Si tienes un MINI, también es tu página. MINI comparte electrónica y buena parte de los motores con BMW —los gasolina de tres y cuatro cilindros y los diésel B37 y B47 de las últimas generaciones—, así que en el taller se diagnostica y se mantiene con el mismo equipo y el mismo plan de marca que un BMW.",
             "Si lo que buscas es el concesionario, el punto oficial BMW de la ciudad que figura en el localizador de bmw.es es Quadis Munich, en el carrer Anoia 9, a unos 5,2 km del centro. Allí se tramitan campañas del fabricante y reparaciones en garantía; el mantenimiento puede hacerse fuera sin perder la garantía si se respeta el plan (Reglamento UE 461/2010)."
         ]},
        {"id": "c16-b30", "h2": "Por la C-16 y la B-30 hasta Sant Joan Despí",
         "parrafos": [
             "Desde el centro de Terrassa hasta la nave de Dasercars Barcelona hay 32,3 km por carretera: C-16, B-30, un tramo de AP-7 y la B-23 hasta Sant Joan Despí. Terrassa no forma parte del Área Metropolitana de Barcelona, así que la recogida del coche que ofrece el taller dentro del área metropolitana no llega hasta aquí: cuenta con traerlo tú.",
             "El taller trabaja de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00. Para trabajos de un día, lo cómodo es entrar a primera hora y volver por la tarde."
         ]},
        {"id": "itv-viladecavalls", "h2": "La ITV de referencia está en Viladecavalls",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera al centro de Terrassa es la de Viladecavalls (B03), en el polígono industrial Can Trias, a 6,3 km. Es también la más próxima por carretera para Ullastrell y Matadepera."
         ]},
        {"id": "parque-terrassa", "h2": "Un parque de más de 100.000 turismos",
         "parrafos": [
             "Idescat, con datos de la DGT, contaba 102.461 turismos en Terrassa en 2024: 439 por cada 1.000 habitantes, frente a los 281 de Barcelona ciudad. La población ha pasado de 215.214 vecinos en 2015 a 233.270 en 2025, un 8,4 % más."
         ]},
    ],
    "faq": [
        {"q": "¿Reparáis MINI además de BMW?",
         "a": "Sí. MINI comparte electrónica y motores con BMW y se trabaja con el mismo equipo de diagnosis."},
        {"q": "¿Recogéis el coche en Terrassa?",
         "a": "No: la recogida que ofrece el taller cubre solo el área metropolitana de Barcelona, y Terrassa queda fuera."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 32,3 km por carretera desde el centro, por la C-16, la B-30, la AP-7 y la B-23."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "233.270 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082798")},
        {"etiqueta": "Turismos (2024)", "valor": "102.461 · 439 por cada 1.000 hab.", **F.idescat("082798")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecavalls (B03) · 6,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, c. Anoia 9 · 5,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 32,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082798"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["camarma-de-esteruelas"] = {
    "h1": "Camarma de Esteruelas: tu BMW, entre Alcalá y Alcobendas",
    "entradilla": "En Camarma hay muchos más coches por habitante que en Madrid capital. Lo que tienes cerca está en Alcalá de Henares; el taller especialista de la red, en Alcobendas, a 37 km.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 37.0},
    "secciones": [
        {"id": "un-coche-por-vecino", "h2": "630 turismos por cada mil vecinos",
         "parrafos": [
             "Camarma de Esteruelas tenía 8.331 habitantes en el padrón de 2025, un 16,8 % más que en 2015, y 5.249 turismos censados en 2025 según la Comunidad de Madrid a partir de la DGT. Son 630 turismos por cada 1.000 habitantes; en Madrid capital la cifra es de 388.",
             "Es lo esperable en un municipio pequeño sin autovía a menos de tres kilómetros del centro: casi cualquier desplazamiento se hace en coche y por carretera secundaria, con rotondas y arranques frecuentes, que es donde más trabajan embrague, frenos y suspensión."
         ]},
        {"id": "alcala-al-lado", "h2": "Lo oficial, en Alcalá de Henares",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es AutoPremier, en la calle Argentina 7 del polígono La Garena, en Alcalá de Henares, a 9,7 km por carretera. La estación de ITV oficial más cercana, también en Alcalá: ITVERSIA, en la Vía Complutense 105, a 10,8 km.",
             "Que el servicio oficial esté tan cerca no obliga a hacer allí las revisiones: la normativa europea de competencia protege el derecho a elegir taller sin perder la garantía, siempre que se siga el plan de mantenimiento del coche."
         ]},
        {"id": "m100-r2", "h2": "Hasta Alcobendas por la M-100 y la R-2",
         "parrafos": [
             "La ruta desde Camarma hasta la calle Valgrande de Alcobendas sale por la M-119 y la M-100, enlaza con la R-2 y entra por la M-50: 37 km por carretera, 22,6 en línea recta. Si el trabajo es de más de un día, pregunta por el vehículo de cortesía al reservar; está sujeto a disponibilidad."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el taller que atiende Camarma?",
         "a": "En la calle Valgrande 17 de Alcobendas (Dasercars Madrid), a 37 km por carretera."},
        {"q": "¿Dónde paso la ITV desde Camarma?",
         "a": "La estación oficial más cercana es ITVERSIA, en la Vía Complutense 105 de Alcalá de Henares, a 10,8 km."},
        {"q": "¿Cómo pido presupuesto?",
         "a": "Llamando con modelo, año, kilometraje y, si puede ser, el bastidor. El presupuesto se entrega por escrito antes de empezar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "8.331 habitantes (+16,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "5.249 · 630 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITVERSIA, Alcalá de Henares · 10,8 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 9,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 37 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

CIUDADES["sentmenat"] = {
    "h1": "Sentmenat: taller autorizado BMW a 6,6 km o especialista independiente",
    "entradilla": "Desde Sentmenat tienes un taller autorizado BMW en Castellar del Vallès y nuestro taller especialista en Sant Joan Despí, a 42 km. Qué te ofrece cada uno y cómo se presupuesta.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 42.1},
    "secciones": [
        {"id": "tallcar-castellar", "h2": "El servicio autorizado más cercano está en Castellar",
         "parrafos": [
             "Según el localizador de bmw.es, el punto de servicio oficial más próximo a Sentmenat es Tallcar, un taller autorizado BMW en la calle Suiza 6 de Castellar del Vallès, a 6,6 km por carretera. Para una campaña de revisión del fabricante o una reparación en garantía, es la opción lógica por cercanía.",
             "Nuestro taller, Dasercars Barcelona, queda bastante más lejos: 42,1 km por la B-142, la AP-7 y la B-23 hasta Sant Joan Despí. Tiene sentido cuando buscas un especialista independiente para una avería concreta o para el mantenimiento fuera de la red oficial, que no hace perder la garantía si se respeta el plan del fabricante."
         ]},
        {"id": "presupuesto-por-escrito", "h2": "Presupuesto cerrado y por escrito",
         "parrafos": [
             "Hay quien llega aquí buscando «precios cerrados». Lo que sí podemos asegurar es el método: el presupuesto se entrega por escrito y ningún trabajo empieza sin tu aprobación. La diagnosis es un trabajo técnico y también se presupuesta antes de conectar el equipo.",
             "El precio depende del modelo, del motor y de la pieza, y ninguna cifra genérica te dice nada sobre tu coche. Llama con modelo, año y kilometraje y te damos un número concreto."
         ]},
        {"id": "itv-sabadell", "h2": "La ITV, en el polígono Can Roqueta de Sabadell",
         "parrafos": [
             "La estación más próxima en el registro de la Generalitat es la de Sabadell (B24), en el polígono Can Roqueta, a 11,4 km del centro de Sentmenat. El municipio, con 9.548 vecinos en 2025 y 5.242 turismos en 2024 (Idescat, a partir de la DGT), tiene 549 turismos por cada 1.000 habitantes: más de un coche por cada dos personas."
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el taller BMW autorizado más cercano a Sentmenat?",
         "a": "Tallcar, en la calle Suiza 6 de Castellar del Vallès, a 6,6 km según el localizador de bmw.es."},
        {"q": "¿Me dais el precio por teléfono?",
         "a": "Te orientamos con modelo, año y kilometraje, y el presupuesto definitivo se entrega por escrito antes de empezar."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "42,1 km por carretera hasta Sant Joan Despí, por la B-142, la AP-7 y la B-23."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "9.548 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082671")},
        {"etiqueta": "Turismos (2024)", "valor": "5.242 · 549 por cada 1.000 hab.", **F.idescat("082671")},
        {"etiqueta": "Taller autorizado BMW", "valor": "Tallcar, Castellar del Vallès · 6,6 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sabadell (B24) · 11,4 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 42,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082671"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["santpedor"] = {
    "h1": "Santpedor y el Bages: cuándo compensa llevar el BMW a 70 km",
    "entradilla": "De Santpedor a nuestro taller de Sant Joan Despí hay 70 km. No siempre merece la pena el viaje, y preferimos decirte cuándo sí y cuándo no antes de que cojas la C-16.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 70.4},
    "secciones": [
        {"id": "cuando-si", "h2": "Cuándo sí compensa bajar",
         "parrafos": [
             "Compensa cuando el problema es específico de BMW y no se ha resuelto cerca de casa: una avería eléctrica intermitente, un fallo del sistema SCR con el aviso de AdBlue en cuenta atrás, ruido de cadena de distribución en un diésel N47 o N57, o un testigo que vuelve una y otra vez después de borrarlo. También si quieres que el mantenimiento se haga por el plan de marca, con el reinicio del indicador de servicio y el registro de lo hecho.",
             "Para esos casos, llama antes con modelo, año y kilometraje: muchas veces se puede orientar por teléfono y llegar con el diagnóstico encaminado y la pieza pedida."
         ]},
        {"id": "cuando-no", "h2": "Cuándo no",
         "parrafos": [
             "Para un pinchazo, unas escobillas o una revisión sencilla, 70,4 km por la C-16, la B-30, la AP-7 y la B-23 no tienen sentido: cualquier taller de confianza del Bages te lo resuelve. Y si el coche está en garantía y lo que toca es una campaña del fabricante, el servicio oficial más cercano según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 8,4 km."
         ]},
        {"id": "itv-bufalvent", "h2": "La ITV, en el polígono El Grau de Sant Fruitós",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Sant Fruitós (B25), en el polígono industrial El Grau de Sant Fruitós de Bages, a 8,9 km; la de Manresa (B06), en Bufalvent, es la otra opción cercana. Santpedor tenía 7.744 habitantes en 2025 y 4.295 turismos en 2024 (Idescat a partir de la DGT): 555 por cada 1.000 habitantes, casi el doble que en Barcelona ciudad."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en el Bages?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 70,4 km de Santpedor."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en la carretera de Manresa a Berga, km 34,5 (Sant Fruitós de Bages), según bmw.es."},
        {"q": "¿Puedo consultar por teléfono antes de ir?",
         "a": "Sí, y es lo recomendable desde esta distancia: con modelo, año, kilometraje y el síntoma se puede orientar el problema."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "7.744 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("081923")},
        {"etiqueta": "Turismos (2024)", "valor": "4.295 · 555 por cada 1.000 hab.", **F.idescat("081923")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 8,4 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Sant Fruitós (B25) · 8,9 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 70,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081923"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["humanes-de-madrid"] = {
    "h1": "Humanes de Madrid: ITV en el pueblo, especialista BMW al otro lado de Madrid",
    "entradilla": "Humanes tiene estación de ITV propia y el servicio oficial BMW a 10 km, en Leganés. Nuestro taller está en Alcobendas, en el extremo opuesto de la región: 46 km. Te contamos cómo encaja.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 46.1},
    "secciones": [
        {"id": "itv-avenida-fuenlabrada", "h2": "La ITV la tienes en la avenida de Fuenlabrada",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid incluye una estación de ITV dentro del municipio: Alcaravan ITV (estación 2829), en la avenida de Fuenlabrada 15. Para un coche de Humanes, es la opción evidente.",
             "Si el BMW tiene más de diez años y pasa inspección cada año, una pre-ITV antes de pedir cita evita sustos con luces, emisiones o holguras."
         ]},
        {"id": "cruzar-madrid", "h2": "46 kilómetros de sur a norte",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas cruza la región: M-405 y M-506, A-42, M-40, M-30 y A-1. Son 46,1 km por carretera y 36,5 en línea recta.",
             "Por eso, para el día a día, el servicio oficial que te queda cerca —Vehinter, Momentum Leganés, a 10,1 km según bmw.es— es más práctico. El viaje a Alcobendas compensa para trabajos de especialista o cuando buscas una alternativa independiente al concesionario; si es tu caso, pregunta por la recogida y entrega dentro del área metropolitana, sujeta a disponibilidad."
         ]},
        {"id": "carreteras-humanes", "h2": "Un municipio rodeado de carreteras autonómicas",
         "parrafos": [
             "En un radio de tres kilómetros desde el centro pasan la M-405, la M-407, la M-410, la M-413 y la M-419. Con 20.500 vecinos en 2025 y 12.096 turismos censados (590 por cada 1.000 habitantes), Humanes tiene bastantes más coches por vecino que Madrid capital, donde la proporción es de 388 por cada 1.000."
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Humanes de Madrid?",
         "a": "Sí: Alcaravan ITV, en la avenida de Fuenlabrada 15, según el listado oficial de la Comunidad de Madrid."},
        {"q": "¿Dónde está vuestro taller?",
         "a": "En la calle Valgrande 17 de Alcobendas, a 46,1 km de Humanes por carretera."},
        {"q": "¿Recogéis el coche en Humanes?",
         "a": "Hay recogida y entrega dentro del área metropolitana de Madrid, sujeta a disponibilidad: confírmalo al pedir cita."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "20.500 habitantes", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "12.096 · 590 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "Alcaravan ITV, av. de Fuenlabrada 15", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Leganés) · 10,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 46,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
