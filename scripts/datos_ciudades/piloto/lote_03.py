# Piloto (lote 3): Barcelona, Sabadell, Torrejón de Ardoz, Girona, Vilafranca del Penedès.
from fuentes import F

REVISADO = "2026-10-04"
CIUDADES = {}

CIUDADES["barcelona"] = {
    "h1": "Taller especialista BMW para Barcelona ciudad, a 12,7 km por la Diagonal y la B-23",
    "entradilla": "El taller BMW de la red para Barcelona está fuera del término municipal, en Sant Joan Despí. Para quien vive en la ciudad hay dos datos que importan: se llega por la B-23 y hay recogida del coche dentro del área metropolitana.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 12.7},
    "secciones": [
        {"id": "salir-por-la-b23", "h2": "Salir de Barcelona por la B-23",
         "parrafos": [
             "Desde el centro de la ciudad hasta la nave de Dasercars Barcelona, en el carrer del Tambor del Bruc 3 de Sant Joan Despí, hay 12,7 km por carretera y 8,8 en línea recta. El recorrido natural es Diagonal abajo hasta la B-23, y de ahí al Baix Llobregat; desde la parte alta de la ciudad, la Ronda de Dalt es la alternativa.",
             "El taller abre de lunes a viernes en jornada partida, de 9:00 a 14:00 y de 15:00 a 18:00. Los fines de semana está cerrado."
         ]},
        {"id": "recogida-amb", "h2": "Recogida y entrega dentro del área metropolitana",
         "parrafos": [
             "Barcelona y Sant Joan Despí forman parte del Área Metropolitana de Barcelona, y el taller ofrece recogida y entrega del coche y vehículo de cortesía dentro del área metropolitana, ambos sujetos a disponibilidad. Para quien no quiere cruzar media ciudad para dejar el coche, suele ser la forma más cómoda de hacerlo. Pídelo al reservar la cita."
         ]},
        {"id": "cuatro-itv", "h2": "Seis estaciones de ITV dentro de la ciudad",
         "parrafos": [
             "El registro de estaciones de la Generalitat sitúa seis ITV dentro de la ciudad: Còrsega (B16), en el carrer de Còrsega 384-392; Diputació (B14), en el carrer de la Diputació 158-160; Àvila (B19), en el carrer d'Àvila 130-134; Puigmadrona (B10), en el passatge de Puigmadrona 9-15; BCN Caracas (B23), en el carrer de Caracas 10 B, y Motors (B15), en el carrer dels Motors 136.",
             "Con seis estaciones repartidas por la ciudad, la pre-ITV tiene sentido hacerla en el taller cuando el coche ya va por otro motivo, y la inspección, después, en la estación que te quede más cerca de casa."
         ]},
        {"id": "oficial-en-la-ciudad", "h2": "El servicio oficial, en la Ronda de Dalt",
         "parrafos": [
             "El punto de servicio oficial BMW más próximo al centro según el localizador de bmw.es es el taller de Barcelona Premium en el carrer d'Esteve Terrades 77-79, junto a la Ronda de Dalt, a unos 4,2 km. Las campañas del fabricante y las reparaciones en garantía de BMW se hacen en la red oficial; el mantenimiento se puede hacer en un taller independiente sin perder la garantía si se respeta el plan del fabricante (Reglamento UE 461/2010)."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller dentro de Barcelona?",
         "a": "No. El taller de la red para Barcelona es Dasercars Barcelona, en Sant Joan Despí, a 12,7 km del centro."},
        {"q": "¿Recogéis el coche en Barcelona?",
         "a": "Sí, dentro del área metropolitana hay recogida y entrega, sujeta a disponibilidad. Conviene pedirla al reservar."},
        {"q": "¿Qué ITV hay en Barcelona ciudad?",
         "a": "Según la Generalitat, seis: Còrsega (B16), Diputació (B14), Àvila (B19), Puigmadrona (B10), BCN Caracas (B23) y Motors (B15)."},
        {"q": "¿Puedo hacer el mantenimiento con vosotros sin perder la garantía?",
         "a": "Sí, si se respetan los intervalos y especificaciones del plan de mantenimiento de BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.731.649 habitantes", **F.ine},
        {"etiqueta": "Turismos (2024)", "valor": "487.185 · 281 por cada 1.000 hab.", **F.idescat("080193")},
        {"etiqueta": "Estaciones ITV en la ciudad", "valor": "6", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, c. Esteve Terrades 77-79 · 4,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 12,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080193"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.rd920_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["sabadell"] = {
    "h1": "Sabadell: servicio autorizado BMW en la ciudad y especialista independiente por la AP-7",
    "entradilla": "Sabadell tiene taller autorizado BMW propio y estación de ITV en el polígono Can Roqueta. Nuestro taller está a 32 km, en Sant Joan Despí. Qué ofrece cada opción, sin rodeos.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 32.0},
    "secciones": [
        {"id": "sitjas", "h2": "Sitjas, el taller autorizado de la calle Quintana",
         "parrafos": [
             "En el localizador de bmw.es, el punto de servicio oficial de la ciudad es Sitjas Motor, un taller autorizado BMW en la calle Quintana 64, a 1,7 km del centro. Para una campaña de revisión del fabricante o una reparación cubierta por la garantía de BMW, es el sitio.",
             "El mantenimiento periódico y las reparaciones fuera de garantía puedes hacerlos en un taller independiente sin perder la garantía del fabricante, siempre que se respeten los intervalos y especificaciones (Reglamento UE 461/2010). Ahí es donde encajamos nosotros."
         ]},
        {"id": "ap7-b23", "h2": "32 kilómetros por la AP-7 y la B-23",
         "parrafos": [
             "La ruta desde el centro de Sabadell hasta la nave de Dasercars Barcelona va por la AP-7 y la B-23: 32 km por carretera, 20,1 en línea recta. Sabadell no forma parte del Área Metropolitana de Barcelona, y la recogida del taller, que cubre solo el área metropolitana, no llega aquí: cuenta con traer el coche.",
             "Para que el viaje compense, llama antes con modelo, año, kilometraje y el síntoma. Con el bastidor se comprueba la referencia exacta del recambio y se puede tener la pieza el día que entra el coche."
         ]},
        {"id": "itv-can-roqueta", "h2": "La ITV de Sabadell, en Can Roqueta",
         "parrafos": [
             "La estación de Sabadell (B24) del registro de la Generalitat está en el polígono Can Roqueta, dentro del término municipal. Si el coche tiene más de diez años, la inspección es anual; entre los cuatro y los diez, cada dos años."
         ]},
        {"id": "sabadell-en-cifras", "h2": "225.368 vecinos y 95.235 turismos",
         "parrafos": [
             "El padrón de 2025 da a Sabadell 225.368 habitantes, 17.554 más que en 2015 (un 8,4 %). El parque de 2024, según Idescat a partir de la DGT, era de 95.235 turismos: 423 por cada 1.000 habitantes. La C-58 y la N-150 pasan a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el taller BMW de Sabadell?",
         "a": "No. El taller autorizado BMW de Sabadell es Sitjas Motor, en la calle Quintana 64. Nosotros somos Dasercars, taller independiente en Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV en Sabadell?",
         "a": "En la estación B24 del polígono Can Roqueta, según el registro de la Generalitat."},
        {"q": "¿Recogéis el coche en Sabadell?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona, y Sabadell queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "225.368 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("081878")},
        {"etiqueta": "Turismos (2024)", "valor": "95.235 · 423 por cada 1.000 hab.", **F.idescat("081878")},
        {"etiqueta": "ITV en el municipio", "valor": "Sabadell (B24), polígono Can Roqueta", **F.itv_cat},
        {"etiqueta": "Taller autorizado BMW", "valor": "Sitjas Motor, c. Quintana 64 · 1,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 32 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081878"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["torrejon-de-ardoz"] = {
    "h1": "Torrejón de Ardoz: dos ITV en el municipio y taller BMW en Alcobendas, a 27 km",
    "entradilla": "Torrejón ha ganado más de 16.000 vecinos en diez años. Para el dueño de un BMW o un MINI, lo útil es saber dónde pasar la ITV dentro del municipio y qué ruta lleva al taller de Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 27.0},
    "secciones": [
        {"id": "dos-itv", "h2": "Dos estaciones de ITV sin salir de Torrejón",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid recoge dos estaciones de ITV en el municipio: la de Itversia Gestión (estación 2861), en la calle Jacinto Benavente 6, en el polígono Casablanca Este, y la de ITV Maco (estación 2865), en la avenida de la Constitución 3.",
             "Tener dos estaciones en el municipio da margen para elegir día y hora sin salir de Torrejón. Y si el coche va antes al taller, la pre-ITV y la inspección pueden quedar en la misma semana."
         ]},
        {"id": "ruta-r2", "h2": "Hacia Alcobendas por la M-50 y la R-2",
         "parrafos": [
             "La ruta desde el centro de Torrejón hasta la calle Valgrande de Alcobendas usa la M-108, la M-50 y la R-2: 27 km por carretera, 17,6 en línea recta. El taller trabaja de lunes a viernes de 9:00 a 14:00 y de 15:00 a 18:00.",
             "Para trabajos de más de un día existe vehículo de cortesía y recogida y entrega dentro del área metropolitana de Madrid, siempre sujetos a disponibilidad. Pregunta al reservar si tu dirección entra."
         ]},
        {"id": "oficial-alcala", "h2": "El servicio oficial más cercano está en Alcalá",
         "parrafos": [
             "El punto oficial BMW más próximo por carretera, según bmw.es, es AutoPremier, en la calle Argentina 7 del polígono La Garena de Alcalá de Henares, a 12,7 km. Si te llega una carta de BMW para una campaña de revisión, esa cita es con ellos; para todo lo demás, la elección de taller es tuya."
         ]},
        {"id": "torrejon-crece", "h2": "143.526 vecinos, un 13,1 % más que en 2015",
         "parrafos": [
             "Torrejón pasó de 126.934 habitantes en 2015 a 143.526 en 2025. En 2025 tenía 69.412 turismos censados según la Comunidad de Madrid a partir de la DGT, 484 por cada 1.000 habitantes. Con la A-2 a menos de tres kilómetros del centro, es fácil que un diésel haga de vez en cuando el recorrido a régimen constante que necesita para regenerar el filtro de partículas."
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV hay en Torrejón de Ardoz?",
         "a": "Dos, según la Comunidad de Madrid: Itversia (calle Jacinto Benavente 6, polígono Casablanca Este) e ITV Maco (avenida de la Constitución 3)."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 27 km por carretera, en la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, MINI comparte electrónica y motores con BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "143.526 habitantes (+13,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "69.412 · 484 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "2 estaciones", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 12,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 27 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

CIUDADES["girona"] = {
    "h1": "BMW en Girona: servicio oficial en Salt y especialista independiente a 111 km",
    "entradilla": "Nuestro taller más cercano a Girona está en Sant Joan Despí, a 111 km por la AP-7. Es mucha distancia y no lo vamos a disimular: te explicamos para qué tiene sentido y qué tienes a mano en la ciudad.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 111.0},
    "secciones": [
        {"id": "lo-que-hay-en-girona", "h2": "Lo que tienes en Girona",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es Oliva Motor Girona, en el carrer de Lingen 9-11 de Salt, a 4,8 km del centro de Girona. La ITV, dentro del propio municipio: la estación de Girona (G09) del registro de la Generalitat, en el carrer Sarrià de Ter.",
             "Con esas dos cosas a menos de cinco kilómetros, para revisiones, campañas del fabricante e inspecciones no tiene sentido bajar a Barcelona."
         ]},
        {"id": "cuando-bajar", "h2": "Para qué sí compensa hacer 111 kilómetros",
         "parrafos": [
             "Para lo que no se ha resuelto cerca: una avería que vuelve después de varias visitas, un fallo del sistema SCR o del AdBlue con la cuenta atrás en marcha, un ruido de cadena en un diésel N47 o N57, o un segundo diagnóstico antes de aceptar una reparación cara. El trayecto es AP-7, C-33, B-20 y B-23 hasta el carrer del Tambor del Bruc.",
             "Desde esta distancia, lo primero es una llamada con modelo, año, kilometraje y bastidor. Muchas veces se puede orientar el problema por teléfono, decidir si merece la pena el viaje y, si es así, tener la pieza pedida el día que llegas."
         ]},
        {"id": "girona-en-cifras", "h2": "108.666 habitantes y 46.124 turismos",
         "parrafos": [
             "Girona tenía 108.666 vecinos en 2025, un 11,4 % más que en 2015, y 46.124 turismos en 2024 según Idescat a partir de la DGT: 424 por cada 1.000 habitantes. Es la capital del Gironès, y los municipios de la red más próximos quedan a más de 30 km."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Girona?",
         "a": "No. El taller de la red más cercano está en Sant Joan Despí, a 111 km por la AP-7."},
        {"q": "¿Dónde está el servicio oficial BMW de Girona?",
         "a": "Oliva Motor Girona, en el carrer de Lingen 9-11 de Salt, según bmw.es."},
        {"q": "¿Dónde paso la ITV en Girona?",
         "a": "En la estación G09, en el carrer Sarrià de Ter, dentro del municipio."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "108.666 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Gironès", **F.idescat("170792")},
        {"etiqueta": "Turismos (2024)", "valor": "46.124 · 424 por cada 1.000 hab.", **F.idescat("170792")},
        {"etiqueta": "ITV en el municipio", "valor": "Girona (G09), c. Sarrià de Ter", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Oliva Motor Girona (Salt) · 4,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 111 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("170792"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["vilafranca-del-penedes"] = {
    "h1": "Vilafranca del Penedès: tu BMW a 46 km del taller y a 17 del servicio oficial",
    "entradilla": "Desde la capital del Alt Penedès, el taller de la red queda a 46 km por la AP-7, el servicio oficial BMW más cercano está en Vilanova i la Geltrú y la ITV, en el municipio vecino de Olèrdola.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 46.4},
    "secciones": [
        {"id": "itv-bellvei", "h2": "La ITV, a 4,4 km en Olèrdola",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera al centro de Vilafranca es la de Olèrdola (B09), en la avinguda de l'Hostal Nou, a 4,4 km. Si el coche pasa antes por el taller para una pre-ITV, la inspección se hace a la vuelta, ya cerca de casa.",
         ]},
        {"id": "ap7-hasta-el-taller", "h2": "Por la AP-7 hasta Sant Joan Despí",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona va por la AP-7 y la B-23: 46,4 km por carretera, 30,2 en línea recta. Vilafranca no está en el Área Metropolitana de Barcelona, así que la recogida que ofrece el taller no llega hasta aquí.",
             "Con la N-340, la AP-7 y la C-15 a menos de tres kilómetros del centro, el viaje es sencillo; lo que conviene es llamar antes con modelo, año y kilometraje para que el día que bajes el trabajo esté planificado."
         ]},
        {"id": "oficial-vilanova", "h2": "El servicio oficial, en Vilanova i la Geltrú",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 16,8 km por carretera. Las campañas del fabricante se hacen allí; el mantenimiento puede hacerse en un taller independiente sin perder la garantía si se respeta el plan (Reglamento UE 461/2010).",
             "Vilafranca tenía 42.607 habitantes en 2025 y 19.219 turismos en 2024 según Idescat a partir de la DGT: 451 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Vilafranca?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Olèrdola (B09), en la avinguda de l'Hostal Nou, a 4,4 km."},
        {"q": "¿Recogéis el coche en Vilafranca?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Vilanova i la Geltrú, a 16,8 km por carretera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "42.607 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("083054")},
        {"etiqueta": "Turismos (2024)", "valor": "19.219 · 451 por cada 1.000 hab.", **F.idescat("083054")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 4,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 16,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 46,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("083054"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.rd920_f, F.r461_f, F.dasercars_bcn_f],
}
