# Piloto (lote 4): El Vendrell, Calatayud, Seseña, Alpens, El Atazar.
from fuentes import F

REVISADO = "2026-10-04"
CIUDADES = {}

CIUDADES["el-vendrell"] = {
    "h1": "El Vendrell: BMW junto al mar, ITV a 3 km y taller especialista a 61 km",
    "entradilla": "El Vendrell está a unos tres kilómetros de la costa y tiene la ITV del Baix Penedès casi al lado. Nuestro taller queda a 61,5 km, en Sant Joan Despí. Lo que conviene saber si tienes un BMW o un MINI aquí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 61.5},
    "secciones": [
        {"id": "salitre", "h2": "Tres kilómetros de mar: qué hace el salitre a un coche",
         "parrafos": [
             "El centro de El Vendrell queda a unos 3,3 km de la línea de costa, y en los núcleos de playa del municipio la distancia es mínima. El aire salino no estropea un coche de un día para otro, pero acelera tres cosas: la corrosión de bajos, anclajes de escape y soportes; el óxido superficial en los discos de freno si el coche pasa días parado, que luego se nota como vibración o ruido al frenar; y la sulfatación de conectores expuestos.",
             "Un lavado de bajos con agua dulce después del verano y una revisión de frenos si el coche ha estado semanas sin moverse evitan la mayoría de sustos. Si el BMW lleva tiempo con un testigo eléctrico intermitente, los conectores son lo primero que hay que mirar."
         ]},
        {"id": "itv-bellvei", "h2": "La ITV del Baix Penedès, a 3 km en Bellvei",
         "parrafos": [
             "La estación de ITV del Baix Penedès (T07) está en el polígono industrial Els Massets de Bellvei, a 3 km del centro de El Vendrell por carretera, según el registro de la Generalitat. Está tan cerca que lo razonable es hacer la pre-ITV en un taller del Penedès y no bajar a Sant Joan Despí solo para eso."
         ]},
        {"id": "c32-hasta-el-taller", "h2": "Por la C-32 hasta Sant Joan Despí",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona va por la C-32 y la B-25: 61,5 km por carretera. El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 25,9 km; allí se hacen las campañas del fabricante y las reparaciones en garantía.",
             "Desde aquí no hay recogida: el servicio del taller solo cubre el área metropolitana. Lo práctico es una llamada previa con el modelo y el síntoma, para bajar con hora y, si hace falta, con la pieza ya pedida."
         ]},
        {"id": "vendrell-crece", "h2": "Un municipio que ha crecido un 12,5 % en diez años",
         "parrafos": [
             "El padrón pasó de 36.558 vecinos en 2015 a 41.133 en 2025. En 2024 había 19.239 turismos censados según Idescat a partir de la DGT, 468 por cada 1.000 habitantes, con la N-340, la AP-7 y la C-32 a menos de tres kilómetros del centro."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en El Vendrell?",
         "a": "En la estación del Baix Penedès (T07), en el polígono Els Massets de Bellvei, a 3 km."},
        {"q": "¿Afecta la proximidad del mar a mi BMW?",
         "a": "Acelera la corrosión de bajos y anclajes, el óxido en discos de un coche parado y la sulfatación de conectores. Un lavado de bajos con agua dulce ayuda."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 61,5 km por la C-32 y la B-25, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "41.133 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Penedès", **F.idescat("431634")},
        {"etiqueta": "Turismos (2024)", "valor": "19.239 · 468 por cada 1.000 hab.", **F.idescat("431634")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 3,3 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Baix Penedès (T07), Bellvei · 3 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 61,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("431634"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["calatayud"] = {
    "h1": "Calatayud: ITV en la ciudad, servicio oficial BMW a 87 km",
    "entradilla": "Calatayud queda lejos de casi todo lo que tiene que ver con BMW: el servicio oficial más cercano y el taller asociado de la red están en Zaragoza. Te explicamos qué puedes resolver aquí y qué conviene hablar por teléfono antes de coger la A-2.",
    "socio": {"id": "socio-zaragoza"},
    "secciones": [
        {"id": "lejos-de-zaragoza", "h2": "A 87 kilómetros del servicio oficial",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo a Calatayud es Augusta Aragón, en la avenida Alcalde Caballero 112 de Zaragoza, a 86,9 km por carretera. El taller de la red que atiende esta zona es un taller asociado de Zaragoza: el teléfono de esta página es el suyo, y al llamar te indican dónde llevar el coche.",
             "Con esa distancia, lo sensato es que el mantenimiento rutinario y lo que no es específico de la marca se resuelva en Calatayud, y reservar el viaje para lo que de verdad necesita un especialista BMW: una avería electrónica sin diagnosticar, un problema del sistema de AdBlue o de la cadena de distribución, o una segunda revisión antes de aceptar una reparación cara."
         ]},
        {"id": "itv-calatayud", "h2": "La ITV, sin salir de la ciudad",
         "parrafos": [
             "El directorio oficial del Gobierno de Aragón incluye una estación de ITV en el municipio de Calatayud, en la comarca Comunidad de Calatayud. Tenerla en la ciudad permite separar las cosas: la inspección aquí y el viaje a Zaragoza solo cuando haya una avería que lo justifique."
         ]},
        {"id": "a2-n234", "h2": "Un cruce de carreteras: A-2, N-234 y A-202",
         "parrafos": [
             "A menos de tres kilómetros del centro pasan la A-2, la N-234 y la A-202. Es un municipio de 154 km² y 20.158 habitantes en 2025, con un crecimiento del 2,2 % en diez años.",
             "Para un BMW que hace mucha autovía, lo que más agradece es respetar los intervalos del indicador de servicio con el aceite de homologación correcta para su motor, y no dejar pasar un aviso de temperatura o de presión de aceite «hasta llegar»."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Calatayud?",
         "a": "No. La zona la atiende un taller asociado de la red en Zaragoza; al llamar te indican dónde llevar el coche."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "En Zaragoza: Augusta Aragón, avenida Alcalde Caballero 112, a 86,9 km."},
        {"q": "¿Hay ITV en Calatayud?",
         "a": "Sí. El directorio del Gobierno de Aragón recoge una estación en el municipio."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "20.158 habitantes", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "154,2 km²", **F.cartociudad},
        {"etiqueta": "ITV en el municipio", "valor": "Sí (directorio de Aragón)", **F.itv_aragon},
        {"etiqueta": "Servicio oficial BMW", "valor": "Augusta Aragón (Zaragoza) · 86,9 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.itv_aragon_f, F.bmw_f, F.osrm_f, F.rd920_f],
}

CIUDADES["sesena"] = {
    "h1": "Seseña, un 43 % más grande que hace diez años: tu BMW y el taller de Alcobendas",
    "entradilla": "Seseña ha pasado de 21.558 a 30.907 vecinos en diez años. Es provincia de Toledo, pero el taller que la atiende está en Alcobendas, a 58 km por la A-4. Esto es lo que tienes cerca y lo que supone el viaje.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 58.1},
    "secciones": [
        {"id": "un-43-por-ciento", "h2": "Un 43,4 % más de población desde 2015",
         "parrafos": [
             "Según el padrón del INE, Seseña tenía 21.558 habitantes en 2015 y 30.907 en 2025: un 43,4 % más. ",
             "Si tu coche está todavía en garantía, hacer las revisiones fuera del concesionario no la anula mientras se cumplan los intervalos del plan de BMW y se usen recambios y aceites con la especificación correcta (Reglamento UE 461/2010). Lo único que no sale de la red oficial son las campañas que convoque la marca."
         ]},
        {"id": "lo-oficial-cerca", "h2": "Lo oficial que tienes más cerca",
         "parrafos": [
             "El servicio oficial BMW más próximo según el localizador de bmw.es es Vehinter, en la carretera de Madrid a Toledo, en Getafe, a 29,4 km por carretera. Para la ITV, una estación oficial cercana es la de General de Servicios ITV en el polígono Gonzalo Chacón de Aranjuez, a 14,7 km, que figura en el listado de la Comunidad de Madrid."
         ]},
        {"id": "a4-hasta-alcobendas", "h2": "58 kilómetros por la A-4, la M-30 y la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas sube por la R-4 y la A-4, cruza por la M-30 y sale por la A-1: 58,1 km por carretera. Seseña queda fuera del área metropolitana de Madrid, así que la recogida y entrega que ofrece el taller no te sirve; el viaje lo haces tú.",
             "Para que compense, llama antes con modelo, año, kilometraje y bastidor. El presupuesto se entrega por escrito y ningún trabajo empieza sin tu aprobación, de modo que puedes decidir antes de mover el coche."
         ]},
    ],
    "faq": [
        {"q": "¿Por qué os atiende un taller de Madrid si Seseña es de Toledo?",
         "a": "Porque el taller de la red más cercano es Dasercars Madrid, en Alcobendas, a 58,1 km; no hay otro taller de la red más próximo."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Vehinter, en la carretera de Madrid a Toledo, en Getafe, a 29,4 km según bmw.es."},
        {"q": "¿Recogéis el coche en Seseña?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Madrid."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "30.907 habitantes (+43,4 % desde 2015)", **F.ine},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 29,4 km", **F.bmw},
        {"etiqueta": "ITV oficial cercana", "valor": "Aranjuez, polígono Gonzalo Chacón · 14,7 km", **F.itv_madrid},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 58,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.bmw_f, F.itv_madrid_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

CIUDADES["alpens"] = {
    "h1": "Alpens, en el Lluçanès: un BMW a 855 metros y a 125 km del taller",
    "entradilla": "Alpens tiene 267 vecinos y está a 855 metros de altitud. Nuestro taller queda a 125 km, en Sant Joan Despí, y no tiene sentido fingir que está cerca. Esto es lo que te sirve de verdad.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 125.0},
    "secciones": [
        {"id": "montana-y-frio", "h2": "Lo que pide un coche a 855 metros",
         "parrafos": [
             "En invierno, a esta altitud, el frío se nota primero en la batería: un BMW con arranque y parada automático y mucho consumo eléctrico la exige más que un coche sencillo, y una batería cansada suele fallar la primera mañana de helada. La batería nueva, además, hay que registrarla en la centralita.",
             "En las bajadas largas de carretera de montaña, los frenos trabajan más que en llano: el líquido de frenos absorbe humedad con los años y pierde punto de ebullición, por eso se cambia por tiempo y no por kilómetros."
         ]},
        {"id": "lo-mas-cercano", "h2": "Lo más cercano: Vic y Ripoll",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 41 km por carretera. La estación de ITV más cercana por carretera en el registro de la Generalitat es la de Ripoll (G08), en el passeig d'Ordina, a 36,3 km.",
             "Para el mantenimiento de rutina, lo razonable es un taller de la comarca o de Osona. El viaje a Sant Joan Despí —125 km por la BV-4341, la C-62, la C-25, la C-16 y la AP-7— solo compensa para una avería concreta de BMW que no se haya resuelto cerca, y siempre después de una llamada con modelo, año y síntomas."
         ]},
        {"id": "alpens-en-cifras", "h2": "267 vecinos y 153 turismos",
         "parrafos": [
             "Alpens tenía 290 habitantes en 2015 y 267 en 2025, según el padrón. Idescat, con datos de la DGT, contaba 153 turismos en 2024: 573 por cada 1.000 vecinos, el doble que en Barcelona ciudad."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller cerca de Alpens?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 125 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más cercana por carretera en el registro de la Generalitat es la de Ripoll (G08), a 36,3 km."},
        {"q": "¿Cada cuánto se cambia el líquido de frenos?",
         "a": "Por tiempo, según el plan de mantenimiento del coche, porque absorbe humedad aunque no se hagan kilómetros."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "267 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Lluçanès", **F.idescat("080044")},
        {"etiqueta": "Altitud", "valor": "855 m", **F.idescat("080044")},
        {"etiqueta": "Turismos (2024)", "valor": "153", **F.idescat("080044")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 36,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 41 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080044"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["atazar-el"] = {
    "h1": "El Atazar: 110 vecinos, 84 turismos y el taller BMW más cercano a 69 km",
    "entradilla": "El Atazar es uno de los municipios más pequeños de la Comunidad de Madrid. Aquí el coche no es opcional, y el taller especialista más cercano está en Alcobendas. Te contamos la ruta, la ITV que te toca y qué revisar antes del invierno.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 68.7},
    "secciones": [
        {"id": "un-coche-por-vecino", "h2": "764 turismos por cada mil vecinos",
         "parrafos": [
             "El Atazar tenía 110 habitantes en el padrón de 2025, 14 más que en 2015, y 84 turismos censados según la Comunidad de Madrid a partir de la DGT. Son 764 turismos por cada 1.000 vecinos, casi el doble que en Madrid capital. En un término de 28,3 km², con la ITV a 27 km y el servicio oficial a más de 50, se entiende."
         ]},
        {"id": "m133-a1", "h2": "De las carreteras de la sierra a la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas baja por la M-133, la M-131 y la M-127 hasta la A-1: 68,7 km por carretera, 45 en línea recta. Son carreteras autonómicas de montaña en buena parte del recorrido, con curvas y desnivel, donde frenos y neumáticos trabajan más que en autovía.",
             "Con esa distancia, el viaje tiene sentido para el mantenimiento por plan de marca o para una avería que no se ha resuelto cerca, y siempre con cita previa: el taller abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00."
         ]},
        {"id": "itv-lozoyuela", "h2": "La ITV, en la A-1 a la altura de Lozoyuela",
         "parrafos": [
             "La estación oficial más cercana por carretera es la de TÜV SÜD ATISAE en la A-1, km 66 (término de Lozoyuela-Navas-Sieteiglesias), a 27,4 km según el listado de la Comunidad de Madrid. El servicio oficial BMW más próximo, BYmyCAR Madrid en Algete, queda a 52,1 km.",
             "A unos 900 metros de altitud, antes del invierno conviene revisar batería, anticongelante y neumáticos; si el coche duerme fuera, la batería es lo primero que falla con la primera helada."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde El Atazar?",
         "a": "En la estación de la A-1, km 66, en Lozoyuela-Navas-Sieteiglesias, a 27,4 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "68,7 km por la M-133, la M-131, la M-127 y la A-1 hasta Alcobendas."},
        {"q": "¿Puedo consultar antes por teléfono?",
         "a": "Sí, y desde aquí es lo recomendable: con modelo, año, kilometraje y el síntoma se puede orientar el problema antes de bajar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "110 habitantes", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "84 · 764 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Superficie del término", "valor": "28,3 km²", **F.cartociudad},
        {"etiqueta": "ITV más cercana", "valor": "A-1 km 66 (Lozoyuela) · 27,4 km", **F.itv_madrid},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 68,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.cartociudad_f, F.dasercars_madrid_f],
}
