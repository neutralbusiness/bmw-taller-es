# Piloto (lote 1): Madrid, Guadalajara, Lozoyuela-Navas-Sieteiglesias, Zaragoza, Sant Boi de Llobregat.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con aplicar.py.
from fuentes import F

REVISADO = "2026-10-04"

CIUDADES = {}

CIUDADES["madrid"] = {
    "h1": "Taller BMW para Madrid capital: Dasercars, a 20 km del centro por la A-1",
    "entradilla": "Madrid no tiene un taller nuestro dentro del término municipal: el taller especialista que atiende la capital está en Alcobendas. Aquí tienes la ruta, las 17 ITV de la ciudad y el servicio oficial más próximo al centro, para que compares con datos.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 20.2},
    "secciones": [
        {"id": "ruta-alcobendas", "h2": "Del centro de Madrid a Alcobendas: 20,2 km por la M-30 y la A-1",
         "parrafos": [
             "Desde la Puerta del Sol, la ruta más corta hasta la nave de Dasercars en la calle Valgrande sale a la M-30 y sigue por la A-1 hasta el polígono industrial de Alcobendas: 20,2 km por carretera, 14,1 km en línea recta. Desde el norte de la ciudad —Fuencarral, Hortaleza, Las Tablas o Sanchinarro— el trayecto se acorta mucho; desde Vallecas o Villaverde hay que cruzar la M-30 o la M-40.",
             "El taller abre de lunes a viernes en jornada partida (9:00–14:00 y 15:00–18:00) y cierra el fin de semana, así que lo práctico es dejar el coche a primera hora y recogerlo por la tarde. Para trabajos de varios días existe vehículo de cortesía y recogida y entrega dentro del área metropolitana de Madrid, siempre sujetos a disponibilidad: pídelo al reservar, no el mismo día."
         ]},
        {"id": "itv-madrid", "h2": "Diecisiete estaciones ITV dentro del término municipal",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid sitúa 17 estaciones de ITV en el municipio de Madrid. Entre ellas están las de Vallecas (Bruno Abúndez y avenida de la Democracia), Villaverde (A-42, km 9,8), Vicálvaro, La Gavia, el polígono Fin de Semana, la carretera de Valencia (A-3, km 7,1) y la de Miguel Yuste, en Simancas. Hacia el norte, la más cómoda si luego vas a Alcobendas es la de María de Portugal, en Sanchinarro.",
             "Un turismo pasa su primera ITV a los cuatro años, después cada dos hasta los diez, y a partir de ahí cada año (Real Decreto 920/2017). Una pre-ITV repasa luces, emisiones, frenos y holguras de dirección y suspensión antes de pedir cita en la estación."
         ]},
        {"id": "oficial-o-independiente", "h2": "Servicio oficial a 4,9 km o taller independiente a 20: cómo decidir",
         "parrafos": [
             "El punto de servicio oficial BMW más próximo al centro, según el localizador de bmw.es, es Caetano Cuzco, en la calle Edgar Neville, a unos 4,9 km de Sol. Las campañas de llamada a revisión del fabricante se hacen en la red oficial.",
             "Para el mantenimiento, el Reglamento (UE) 461/2010 permite revisar el coche en un taller independiente sin perder la garantía del fabricante, siempre que se respeten intervalos y especificaciones del plan de mantenimiento. En Dasercars se entrega presupuesto por escrito y ningún trabajo empieza sin tu aprobación; la diagnosis también se presupuesta antes de conectar el equipo."
         ]},
        {"id": "parque-madrid", "h2": "Una ciudad con menos coche por vecino que su corona",
         "parrafos": [
             "Madrid tenía 3.506.730 habitantes en el padrón de 2025, un 11,6 % más que diez años antes, y 1.360.704 turismos censados en 2025 según el Instituto de Estadística de la Comunidad de Madrid a partir de los datos de la DGT. Son 388 turismos por cada 1.000 habitantes, muy lejos de municipios de la misma red como Humanes de Madrid (590) o Camarma de Esteruelas (630).",
             "Menos coches por vecino no significa menos desgaste por coche. Un diésel que solo hace trayectos cortos por la ciudad rara vez completa la regeneración del filtro de partículas, y es el uso que peor lleva; si es tu caso, una salida de vez en cuando por la M-40 o la A-1 a régimen constante le sienta mejor que cualquier aditivo."
         ]},
    ],
    "faq": [
        {"q": "¿Hay algún taller vuestro dentro de Madrid capital?",
         "a": "No. El taller que atiende Madrid es Dasercars Madrid, en la calle Valgrande 17 de Alcobendas, a 20,2 km del centro por la A-1."},
        {"q": "¿Podéis recoger el coche en mi casa de Madrid?",
         "a": "Hay recogida y entrega dentro del área metropolitana de Madrid, sujeta a disponibilidad. Conviene pedirla al reservar la cita."},
        {"q": "¿En qué ITV de Madrid paso la inspección después de la pre-ITV?",
         "a": "En cualquiera de las 17 estaciones del municipio que publica la Comunidad de Madrid; la del norte más cercana al taller es la de María de Portugal, en Sanchinarro."},
        {"q": "¿Trabajáis también MINI?",
         "a": "Sí. MINI comparte electrónica y motores con BMW y se diagnostica con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "3.506.730 habitantes (+11,6 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos censados (2025)", "valor": "1.360.704 · 388 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Estaciones ITV en el municipio", "valor": "17", **F.itv_madrid},
        {"etiqueta": "Distancia al taller (Alcobendas)", "valor": "20,2 km por carretera", **F.osrm},
        {"etiqueta": "Servicio oficial BMW más cercano", "valor": "Caetano Cuzco, c/ Edgar Neville 1 · 4,9 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.rd920_f, F.r461_f, F.dasercars_madrid_f],
}

CIUDADES["guadalajara"] = {
    "h1": "Guadalajara: concesionario BMW en la ciudad, taller especialista en Alcobendas",
    "entradilla": "Mucha gente que busca «taller BMW Guadalajara» quiere en realidad el concesionario. Te decimos dónde está cada cosa y qué supone traer el coche desde la capital alcarreña hasta Alcobendas por la A-2.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 52.5},
    "secciones": [
        {"id": "concesionario-o-taller", "h2": "Si lo que buscas es el concesionario",
         "parrafos": [
             "El concesionario oficial BMW de la ciudad es AutoPremier, en el Paseo de la Estación 23, a 2,3 km del centro según el localizador de bmw.es. Allí se hacen las campañas de revisión del fabricante y las reparaciones en garantía que dependen de BMW.",
             "Nosotros no somos ese concesionario ni tenemos taller en Guadalajara. Somos un taller independiente especializado en BMW con nave propia en Alcobendas. Te lo aclaramos de entrada porque mucha gente llega a esta página buscando el concesionario, y no queremos que llames pensando que hablas con otro."
         ]},
        {"id": "a2-r2", "h2": "52 kilómetros por la A-2: cuándo compensa el viaje",
         "parrafos": [
             "La ruta desde el centro de Guadalajara hasta la calle Valgrande de Alcobendas va por la A-2, enlaza con la R-2 y entra por la M-50: 52,5 km por carretera. La recogida y entrega del coche que ofrece el taller solo cubre el área metropolitana de Madrid, de modo que desde aquí cuenta con traerlo tú.",
             "Por eso tiene más sentido para trabajos en los que la especialización marca la diferencia —un ruido de cadena en un N47, un fallo del sistema SCR con la cuenta atrás de AdBlue en marcha, una avería eléctrica que nadie ha conseguido localizar— que para un cambio de aceite. Llama antes con modelo, año y kilometraje: muchas veces se puede orientar el problema por teléfono y decidir si merece la pena el desplazamiento."
         ]},
        {"id": "itv-guadalajara", "h2": "La ITV, en la calle Trafalgar",
         "parrafos": [
             "La estación de ITV de la ciudad, de Itevelesa, está en la calle Trafalgar. Si vas a bajar el coche a Alcobendas por otro motivo y la inspección está cerca, pide que te hagan la pre-ITV en la misma visita."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Guadalajara?",
         "a": "No. El concesionario es AutoPremier, en el Paseo de la Estación 23. Somos Dasercars, taller independiente especializado en BMW, en Alcobendas."},
        {"q": "¿Cuánto hay desde Guadalajara hasta vuestro taller?",
         "a": "52,5 km por carretera desde el centro, por la A-2, la R-2 y la M-50."},
        {"q": "¿Pierdo la garantía si hago el mantenimiento con vosotros?",
         "a": "No, si se respetan los intervalos y especificaciones del plan de mantenimiento: lo ampara el Reglamento (UE) 461/2010."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "92.834 habitantes (+11,3 % desde 2015)", **F.ine},
        {"etiqueta": "Altitud del centro urbano", "valor": "718 m", **F.copernicus},
        {"etiqueta": "Concesionario oficial BMW", "valor": "AutoPremier, Paseo de la Estación 23 · 2,3 km", **F.bmw},
        {"etiqueta": "Distancia al taller (Alcobendas)", "valor": "52,5 km por carretera", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.bmw_f, F.osrm_f, F.rd920_f, F.r461_f, F.dasercars_madrid_f],
}

CIUDADES["lozoyuela-navas-sieteiglesias"] = {
    "h1": "Talleres en Lozoyuela: lo que hay cerca y el especialista BMW de la Sierra Norte",
    "entradilla": "En Lozoyuela-Navas-Sieteiglesias no tenemos taller. Si tienes un BMW o un MINI y vives en el municipio, esto es lo que te queda cerca y lo que supone bajar hasta Alcobendas por la A-1.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 52.3},
    "secciones": [
        {"id": "sin-taller-en-el-pueblo", "h2": "Por qué esta página no es la de un taller del pueblo",
         "parrafos": [
             "Quien llega a esta página suele buscar un taller en el propio pueblo, así que lo decimos claro: el taller especialista que atiende esta zona es Dasercars Madrid, en la calle Valgrande 17 de Alcobendas, a 52,3 km por la A-1. Para un pinchazo o una revisión de rutina te conviene un taller del valle; para una avería concreta de BMW, un diagnóstico que otro taller no ha resuelto o el mantenimiento por plan de marca, sí tiene sentido bajar.",
             "El municipio, con 1.468 vecinos en el padrón de 2025, ha crecido un 22 % en diez años. En 2025 tenía 809 turismos censados: 551 por cada 1.000 habitantes, bastantes más que en Madrid capital, como es lógico en un sitio donde casi todo queda a varios kilómetros."
         ]},
        {"id": "itv-a1-km66", "h2": "La ITV la tienes en tu propio término: A-1, kilómetro 66",
         "parrafos": [
             "Es un dato que pocos pueblos de este tamaño pueden dar: la estación de ITV de TÜV SÜD ATISAE en la A-1, km 66 (estación 2812 del listado oficial de la Comunidad de Madrid) queda dentro del término municipal. Es también la estación oficial más próxima para pueblos de alrededor como El Atazar.",
             "Si el coche tiene más de diez años y pasa inspección anual, aprovecha cuando lo bajes al taller para una pre-ITV: luces, emisiones, frenos y holguras. Así no subes y bajas dos veces."
         ]},
        {"id": "mil-metros", "h2": "Un BMW a mil metros de altitud",
         "parrafos": [
             "El núcleo urbano está a unos 1.000 metros. En invierno eso se nota en la batería, que pierde capacidad con el frío y en los BMW con arranque y parada automático trabaja más; en el anticongelante, que conviene comprobar por concentración y no solo por nivel; y en los diésel, que agradecen un precalentamiento en buen estado.",
             "Si el coche duerme en la calle, una batería al límite suele dar la cara la primera mañana de helada. Una comprobación de batería y del registro en la centralita —en los BMW la batería nueva hay que registrarla— cuesta menos que una grúa."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Lozoyuela?",
         "a": "No. El taller que atiende la zona está en Alcobendas, a 52,3 km por la A-1."},
        {"q": "¿Dónde paso la ITV si vivo en Lozoyuela?",
         "a": "En la estación de la A-1, km 66, dentro del propio término municipal."},
        {"q": "¿Hace falta registrar una batería nueva en un BMW?",
         "a": "Sí. La centralita ajusta la carga a la batería registrada; sin registrarla, la nueva se carga mal y dura menos."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.468 habitantes (+22 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos censados (2025)", "valor": "809 · 551 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el término", "valor": "TÜV SÜD ATISAE, A-1 km 66", **F.itv_madrid},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 1.000 m", **F.copernicus},
        {"etiqueta": "Distancia al taller (Alcobendas)", "valor": "52,3 km por la A-1", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.osrm_f, F.dasercars_madrid_f],
}

CIUDADES["zaragoza"] = {
    "h1": "Especialista BMW en Zaragoza: taller asociado de la red",
    "entradilla": "En Zaragoza no trabaja Dasercars sino un taller asociado de la red, que es quien responde al teléfono de esta página. Aquí tienes lo que te sirve de la ciudad para decidir: servicio oficial, ITV y accesos.",
    "socio": {"id": "socio-zaragoza"},
    "secciones": [
        {"id": "quien-atiende", "h2": "Quién te atiende cuando llamas desde Zaragoza",
         "parrafos": [
             "Los dos talleres propios de Dasercars están en Alcobendas y en Sant Joan Despí, a varios cientos de kilómetros. Para Zaragoza, la red funciona con un taller asociado: el teléfono que ves en esta página es el suyo, y al llamar te dicen dónde y cuándo pueden ver el coche. No publicamos su dirección aquí mientras no esté confirmada en la ficha de la red.",
             "Cuando llames, ten a mano modelo, año, kilometraje y, si puede ser, el número de bastidor: con eso se identifica la referencia exacta del recambio y se puede orientar el presupuesto antes de que lleves el coche."
         ]},
        {"id": "servicio-oficial", "h2": "Augusta Aragón, el servicio oficial, a 3,4 km del centro",
         "parrafos": [
             "El servicio oficial BMW de la ciudad que aparece en el localizador de bmw.es es Augusta Aragón, en la avenida Alcalde Caballero 112, a unos 3,4 km del centro por carretera. Las campañas de revisión del fabricante y las reparaciones cubiertas por la garantía de BMW se hacen allí.",
             "El mantenimiento, en cambio, puedes hacerlo en un taller independiente sin perder la garantía siempre que se respeten los intervalos y las especificaciones del plan de mantenimiento: es lo que establece el Reglamento (UE) 461/2010."
         ]},
        {"id": "itv-zaragoza", "h2": "Cuatro estaciones de ITV en el término municipal",
         "parrafos": [
             "El directorio de estaciones del Gobierno de Aragón recoge cuatro estaciones de ITV dentro del municipio de Zaragoza, además de las de Utebo y Quinto de Ebro en la misma provincia. Con un término municipal de casi 969 km², merece la pena elegir la estación por cercanía a tu barrio y no por costumbre.",
         ]},
    ],
    "faq": [
        {"q": "¿Es Dasercars quien repara mi coche en Zaragoza?",
         "a": "No. En Zaragoza te atiende un taller asociado de la red; Dasercars tiene sus talleres en Alcobendas y Sant Joan Despí."},
        {"q": "¿Dónde está el servicio oficial BMW en Zaragoza?",
         "a": "Augusta Aragón, en la avenida Alcalde Caballero 112, según el localizador oficial de bmw.es."},
        {"q": "¿Cuántas ITV hay en Zaragoza?",
         "a": "Cuatro dentro del término municipal, según el directorio del Gobierno de Aragón."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "693.091 habitantes (+4,2 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "968,8 km²", **F.cartociudad},
        {"etiqueta": "Estaciones ITV en el municipio", "valor": "4", **F.itv_aragon},
        {"etiqueta": "Servicio oficial BMW", "valor": "Augusta Aragón, av. Alcalde Caballero 112 · 3,4 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.itv_aragon_f, F.bmw_f, F.osrm_f, F.rd920_f, F.r461_f],
}

CIUDADES["sant-boi-de-llobregat"] = {
    "h1": "Taller BMW cerca de Sant Boi: Dasercars Barcelona, a 6 km en Sant Joan Despí",
    "entradilla": "Si vives en Sant Boi de Llobregat, el taller especialista BMW de la red está en el municipio de al lado. Te contamos cómo llegar, qué ofrece dentro del área metropolitana y en qué se diferencia del concesionario que tienes en la carretera del Prat.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 6.1},
    "secciones": [
        {"id": "el-concesionario-de-sant-boi", "h2": "El concesionario de la carretera del Prat no somos nosotros",
         "parrafos": [
             "En Sant Boi hay servicio oficial BMW: Barcelona Premium, en la carretera del Prat 15, a unos 2,4 km del centro según el localizador de bmw.es. Hay quien llega a esta página buscando el teléfono de ese concesionario. Si es tu caso, el teléfono que buscas es el suyo, no el de esta página.",
             "Nosotros somos Dasercars, taller independiente especializado en BMW. La diferencia práctica: en el concesionario se hacen las campañas del fabricante y las reparaciones en garantía; el mantenimiento puedes hacerlo con nosotros sin perder esa garantía, siempre que se respete el plan de mantenimiento (Reglamento UE 461/2010)."
         ]},
        {"id": "seis-kilometros", "h2": "Seis kilómetros hasta el Tambor del Bruc",
         "parrafos": [
             "La nave de Dasercars Barcelona está en el carrer del Tambor del Bruc 3, en Sant Joan Despí: 6,1 km por carretera desde el centro de Sant Boi, 3,4 km en línea recta. Es, de toda la red, una de las ciudades con el taller más a mano.",
             "Sant Boi forma parte del Área Metropolitana de Barcelona, y el taller ofrece recogida y entrega del coche dentro del área metropolitana y vehículo de cortesía, ambos sujetos a disponibilidad. Pídelo al reservar la cita, no a última hora."
         ]},
        {"id": "itv-cornella", "h2": "La ITV más cercana está en Viladecans",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera al centro de Sant Boi es la de Viladecans (B07), en el carrer Jocelyn Bell 16, a 6,7 km."
         ]},
        {"id": "parque-sant-boi", "h2": "85.610 vecinos y casi 34.000 turismos",
         "parrafos": [
             "El padrón de 2025 da a Sant Boi 85.610 habitantes, y el parque de vehículos de 2024 (Idescat, con datos de la DGT) 33.970 turismos: 397 por cada 1.000 vecinos. Con la C-245, la C-32 y la A-2 a menos de tres kilómetros del centro, es fácil dar al coche el rato de carretera que necesita un diésel para regenerar el filtro de partículas, algo que un uso solo urbano no consigue."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Sant Boi?",
         "a": "No. El servicio oficial de Sant Boi es Barcelona Premium, en la carretera del Prat 15. Nosotros somos Dasercars, taller independiente en Sant Joan Despí."},
        {"q": "¿Recogéis el coche en Sant Boi?",
         "a": "Sí, dentro del área metropolitana de Barcelona hay recogida y entrega, sujeta a disponibilidad. Pídela al reservar."},
        {"q": "¿Qué horario tiene el taller?",
         "a": "De lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00. Sábados y domingos, cerrado."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "85.610 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082009")},
        {"etiqueta": "Turismos censados (2024)", "valor": "33.970 · 397 por cada 1.000 hab.", **F.idescat("082009")},
        {"etiqueta": "Distancia al taller (Sant Joan Despí)", "valor": "6,1 km por carretera", **F.osrm},
        {"etiqueta": "ITV más cercana", "valor": "Viladecans (B07) · 6,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, ctra. del Prat 15 · 2,4 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082009"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}
