# Tanda 18: Lliçà d'Amunt, Meco, Alpedrete, Palau-solità i Plegamans, Canet de Mar, Moralzarzal,
# Alovera, Velilla de San Antonio, Valdemorillo, El Casar, San Agustín del Guadalix, Abrera,
# Castellbisbal y Badia del Vallès.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_18
#
# Saltada (nota del coordinador): cuarte-de-huerva (zona de Zaragoza, socio sin dirección publicada).
#
# Las 14 ciudades tienen impresiones en GSC (paso_gsc.json, 90 días): no se tocan ni metaTitle ni
# metaDescription, de modo que META y TITLES quedan vacíos.
#
# Notas de datos:
#  - Moralzarzal: 69.259 turismos para 14.772 vecinos (4.689 por 1.000): flotas domiciliadas,
#    no se publica el parque.
#  - Alovera y El Casar: la ITV del fichero procede de OpenStreetMap (`verificar: true`) y no hay
#    turismos: no se publica ninguna estación de ITV.
#  - El Casar: distancias desde el centro del núcleo urbano (`distancias_desde`).
#  - BYmyCAR Algete y AutoPremier Guadalajara llevan `centro_ocasion_con_taller`: se describen
#    como servicio oficial, sin más.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
META = {}
TITLES = {}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["llica-d-amunt"] = {
    "h1": "Lliçà d'Amunt: concesionario BMW a 6,3 km en Granollers y especialista a 43,8",
    "entradilla": "Para un BMW de Lliçà d'Amunt, lo oficial queda a un paso, en la C-17 a la altura de Granollers. Nuestro taller está bastante más lejos, en Sant Joan Despí, y conviene tener claro para qué trabajos merece la pena ir hasta allí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 43.8},
    "secciones": [
        {"id": "pruna-c17", "h2": "Pruna Motor, en la C-17: el punto oficial más próximo",
         "parrafos": [
             "El localizador de bmw.es da como servicio oficial más cercano a Pruna Motor, en la carretera C-17, km 19,060, ya en Granollers: 6,3 km por carretera desde el centro de Lliçà d'Amunt. Si el coche tiene una avería cubierta por la garantía del fabricante, esa es la puerta.",
             "Fuera de esos casos, el taller lo eliges tú. Nosotros somos Dasercars, un taller independiente dedicado a BMW y MINI, y no tenemos instalaciones en el Vallès Oriental.",
         ]},
        {"id": "c17-c33-b20", "h2": "43,8 kilómetros por la C-17, la C-33 y la B-20",
         "parrafos": [
             "La ruta desde el centro del municipio sale por la C-1415b, toma la C-17 hacia el sur, sigue por la C-33 y termina por la B-20 en el carrer del Tambor del Bruc de Sant Joan Despí: 43,8 km por carretera, 31,3 en línea recta. Lliçà d'Amunt no pertenece al Área Metropolitana de Barcelona, y la recogida del taller no llega hasta aquí.",
             "Con esa distancia, el viaje encaja con lo que de verdad pide un especialista de marca: un testigo que vuelve a encenderse después de borrarlo, una fuga de aceite que nadie localiza, un fallo de la válvula EGR en un diésel B47 o la codificación de un módulo electrónico nuevo. Antes de salir, una llamada contando el síntoma y el modelo ahorra viajes en balde.",
         ]},
        {"id": "itv-el-congost", "h2": "La ITV, en el polígono El Congost",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es la de Granollers (B18), en la avinguda Sant Julià del polígono industrial El Congost, a 11,8 km.",
         ]},
        {"id": "llica-en-cifras", "h2": "612 turismos por cada mil vecinos",
         "parrafos": [
             "El padrón de 2025 da a Lliçà d'Amunt 16.540 habitantes, frente a 14.742 en 2015: un 12,2 % más. En 2024, según Idescat a partir de la DGT, había 10.123 turismos, 612 por cada 1.000 habitantes, muy por encima de los 281 de Barcelona ciudad.",
             "En un término de 22,33 km², con la C-1415 a 1,1 km y la C-17 a 2,7, muchos trayectos diarios son cortos. Es el uso que peor lleva un diésel con filtro de partículas: rara vez llega a completar la regeneración.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Lliçà d'Amunt?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 43,8 km por carretera."},
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "Pruna Motor, en la C-17, km 19,060, en Granollers, a 6,3 km según el localizador de bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Granollers (B18), en el polígono El Congost, a 11,8 km."},
        {"q": "¿Recogéis el coche en Lliçà d'Amunt?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "16.540 habitantes (+12,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("081075")},
        {"etiqueta": "Turismos (2024)", "valor": "10.123 · 612 por cada 1.000 hab.", **F.idescat("081075")},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 11,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 6,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 43,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081075"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["meco"] = {
    "h1": "Meco: ITV y concesionario BMW en Alcalá, taller especialista a 35,8 km por la R-2",
    "entradilla": "A 8,3 km de Alcalá de Henares en línea recta, Meco ha ganado un 20 % de población en diez años. Si tienes aquí un BMW o un MINI, lo oficial te queda en la Vía Complutense y el especialista independiente, en Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 35.8},
    "secciones": [
        {"id": "via-complutense", "h2": "Dos direcciones en la misma avenida de Alcalá",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 11 km por carretera. En la misma vía, en el número 105, está la estación de ITV de ITVERSIA (la 2891 del listado de la Comunidad de Madrid), a 11,9 km. Quedan tan cerca una de otra que una misma mañana puede dar para las dos visitas.",
             "Al concesionario le corresponde lo que cubra la garantía de BMW. Para lo demás —aceite, frenos, distribución, diagnosis— puedes acudir al taller que prefieras.",
         ]},
        {"id": "r2-m50", "h2": "Por la R-2 y la M-50 hasta la calle Valgrande",
         "parrafos": [
             "La R-2 pasa a 2,1 km del centro de Meco y es la carretera que lleva al taller: R-2 y M-50 hasta Alcobendas, 35,8 km por carretera, 27,3 en línea recta. Es un recorrido de autopista casi entero, de los que un diésel agradece para quemar el hollín acumulado en el filtro de partículas.",
             "Si el trabajo va a durar más de un día, pregunta por el vehículo de cortesía al pedir la cita. Igual que la recogida y entrega dentro del área metropolitana de Madrid, está sujeto a disponibilidad, y conviene confirmar si tu dirección entra.",
         ]},
        {"id": "parque-meco", "h2": "629 turismos por cada mil habitantes",
         "parrafos": [
             "En 2025 había en Meco 10.009 turismos censados, según el Instituto de Estadística de la Comunidad de Madrid a partir de la DGT, para 15.922 vecinos: 629 por cada 1.000. Es prácticamente la proporción de Camarma de Esteruelas (630), el municipio de al lado, y mucho más que la de Madrid capital (388).",
             "El padrón ha pasado de 13.269 habitantes en 2015 a 15.922 en 2025. Si tu coche todavía está en garantía, revisarlo fuera del concesionario no la anula mientras se sigan los intervalos del plan de mantenimiento y se usen recambios y aceites con la especificación que pide BMW.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Meco?",
         "a": "La estación oficial más cercana es la de ITVERSIA, en la Vía Complutense 105 de Alcalá de Henares, a 11,9 km."},
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 11 km según el localizador de bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "35,8 km por la R-2 y la M-50, hasta la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI comparte electrónica y buena parte de los motores con BMW y se diagnostica con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "15.922 habitantes (+20 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "10.009 · 629 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITVERSIA, Alcalá de Henares · 11,9 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 11 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 35,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["alpedrete"] = {
    "h1": "Alpedrete, a 914 metros: tu BMW, la ITV de Collado Villalba y el taller de Alcobendas",
    "entradilla": "Alpedrete está en plena sierra y casi pegado a Collado Villalba, donde tienes la ITV. El taller especialista de la red queda a 51,5 km, en Alcobendas: aquí tienes los datos para decidir qué resuelves cerca y qué no.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 51.5},
    "secciones": [
        {"id": "dos-itv-p29", "h2": "Dos estaciones de ITV en el polígono P-29",
         "parrafos": [
             "Según el listado oficial de la Comunidad de Madrid, las dos estaciones más próximas por carretera están en el polígono P-29 de Collado Villalba y casi a la misma distancia: la de TÜV SÜD ATISAE (estación 2813), en la calle Escofina 3, a 4,8 km, y la de ITV P-29 Collado Villalba (estación 2883), a 5,5 km. Elige la que tenga antes cita.",
         ]},
        {"id": "frio-de-sierra", "h2": "Lo que pide un coche a 914 metros",
         "parrafos": [
             "En las mañanas de helada, lo primero que falla en un BMW es una batería cansada: con el frío pierde capacidad justo cuando el motor de arranque más le exige, y los modelos con arranque y parada automático la someten a muchos más ciclos. Si toca cambiarla, la nueva se registra en la centralita para que el alternador la cargue como corresponde.",
             "El anticongelante se comprueba por concentración y no solo por nivel, y el líquido de frenos se cambia por tiempo: absorbe humedad aunque el coche haga pocos kilómetros, y en las bajadas de puerto es cuando más se nota.",
         ]},
        {"id": "a6-m40-a1", "h2": "Hasta Alcobendas por la A-6, la M-40 y la A-1",
         "parrafos": [
             "Desde el centro de Alpedrete, la ruta al taller baja por la A-6, rodea Madrid por la M-40 y sube por la A-1 hasta la calle Valgrande: 51,5 km por carretera para 34,4 en línea recta. En un radio de tres kilómetros del pueblo pasan, entre otras, la M-619, la M-601, la AP-6 y la A-6, así que el acceso a la autovía es inmediato.",
             "El servicio oficial más cercano según bmw.es es Movilnorte, en la A-6, km 23,100, en Las Rozas, a 20,2 km. Para una reparación en garantía es lo práctico; el viaje a Alcobendas tiene sentido para una avería de especialista o para el mantenimiento fuera de la red.",
         ]},
        {"id": "alpedrete-en-cifras", "h2": "15.686 vecinos y 8.620 turismos",
         "parrafos": [
             "El padrón de 2025 cuenta 15.686 habitantes, un 10,1 % más que en 2015. El parque de turismos de 2025, según la Comunidad de Madrid a partir de la DGT, era de 8.620: 550 por cada 1.000 vecinos, en un término de solo 12,6 km².",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Alpedrete?",
         "a": "En el polígono P-29 de Collado Villalba: TÜV SÜD ATISAE (calle Escofina 3), a 4,8 km, o ITV P-29 Collado Villalba, a 5,5 km."},
        {"q": "¿Tenéis taller en la sierra?",
         "a": "No. El taller de la red es Dasercars Madrid, en Alcobendas, a 51,5 km de Alpedrete."},
        {"q": "¿Hay que registrar una batería nueva en un BMW?",
         "a": "Sí. Si no se registra, la centralita sigue cargándola como si fuera la vieja y la batería nueva dura menos."},
        {"q": "¿Podéis recoger el coche en Alpedrete?",
         "a": "La recogida y entrega se ofrece en el área metropolitana de Madrid y está sujeta a disponibilidad: pregunta al reservar si tu dirección entra."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "15.686 habitantes (+10,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "8.620 · 550 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "914 m", **F.copernicus},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE, Collado Villalba · 4,8 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte, Las Rozas · 20,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 51,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["palau-solita-i-plegamans"] = {
    "h1": "Palau-solità i Plegamans: ITV a 6,8 km y especialista BMW a 33,8 por la C-33",
    "entradilla": "En Palau-solità i Plegamans tienes la ITV y el servicio oficial BMW a menos de diez kilómetros. Lo que no tienes es nuestro taller, que está en Sant Joan Despí. Te contamos cuándo te compensa ir y cuándo no.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 33.8},
    "secciones": [
        {"id": "itv-cim-valles", "h2": "La ITV del CIM Vallès, en Santa Perpètua",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de CIM Vallès (B20), en el carrer del Pont Vell del polígono Les Minetes, dentro del Centre Integral de Mercaderies de Santa Perpètua de Mogoda: 6,8 km desde el centro de Palau-solità.",
         ]},
        {"id": "pruna-granollers", "h2": "El servicio oficial, en Granollers",
         "parrafos": [
             "El punto oficial BMW más cercano según bmw.es es Pruna Motor, en la carretera C-17, km 19,060, en Granollers, a 9,8 km por carretera. Es el sitio para una reparación que pague la garantía del fabricante.",
             "No somos ese concesionario ni formamos parte de la red oficial: Dasercars es un taller independiente especializado en BMW y MINI, y el mantenimiento o una reparación fuera de garantía los puedes llevar a donde prefieras.",
         ]},
        {"id": "ruta-c59", "h2": "33,8 km por la C-59, la C-33 y la B-20",
         "parrafos": [
             "La C-59 pasa a 0,7 km del centro y es el arranque de la ruta: B-143, C-59, C-33 y B-20 hasta el carrer del Tambor del Bruc, en Sant Joan Despí. Son 33,8 km por carretera y 25,7 en línea recta. El municipio no forma parte del Área Metropolitana de Barcelona, así que la recogida que ofrece el taller no llega aquí.",
             "Lo que sí puedes hacer es aprovechar el viaje: si el coche tiene que pasar la ITV pronto, una pre-ITV en el taller —luces, frenos, emisiones, holguras de dirección— y la inspección después, ya cerca de casa.",
         ]},
        {"id": "parque-palau", "h2": "562 turismos por cada mil habitantes",
         "parrafos": [
             "Palau-solità i Plegamans tenía 15.614 habitantes en 2025, frente a 14.457 en 2015: un 8 % más. Idescat, con datos de la DGT, contaba 8.773 turismos en 2024, 562 por cada 1.000 habitantes, en un término de 14,93 km² con la C-155 y la B-142 también a menos de tres kilómetros.",
             "Si tu coche se mueve sobre todo en trayectos cortos, trabaja mucho embrague, frenos y suspensión en arranques cortos. Si el tuyo es diésel, sácalo de vez en cuando a la C-59 o a la C-33 a ritmo sostenido para que el filtro de partículas termine sus regeneraciones.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Palau-solità?",
         "a": "Pruna Motor, en la C-17, km 19,060 de Granollers, a 9,8 km según el localizador de bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera en el registro de la Generalitat es CIM Vallès (B20), en Santa Perpètua de Mogoda, a 6,8 km."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona, y Palau-solità i Plegamans queda fuera."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 33,8 km por carretera, en el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "15.614 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("081568")},
        {"etiqueta": "Turismos (2024)", "valor": "8.773 · 562 por cada 1.000 hab.", **F.idescat("081568")},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20), Santa Perpètua · 6,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 9,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 33,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081568"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["canet-de-mar"] = {
    "h1": "Revisión de un BMW en Canet de Mar: el salitre, la ITV de Argentona y el taller a 57 km",
    "entradilla": "A poco más de un kilómetro del mar, un coche de Canet de Mar envejece de forma distinta que uno de interior. Qué conviene revisar por eso, dónde queda lo oficial en el Maresme y qué supone llevarlo a Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 57.0},
    "secciones": [
        {"id": "revision-junto-al-mar", "h2": "Qué mirar en una revisión cuando el coche vive junto al mar",
         "parrafos": [
             "El centro de Canet queda a 1,1 km de la costa. El aire con sal no estropea nada de un día para otro, pero trabaja sin descanso sobre lo que está al descubierto: los bajos, los soportes y abrazaderas del escape, los anclajes de la suspensión y los conectores eléctricos expuestos.",
             "En la revisión de un coche del litoral conviene añadir tres puntos a la lista: mirar los bajos con el coche elevado, comprobar los discos si ha pasado temporadas parado —se oxidan en superficie y luego vibran al frenar— y repasar conectores ante cualquier fallo eléctrico intermitente. Un aclarado de bajos con agua dulce al acabar el verano ayuda.",
         ]},
        {"id": "lo-oficial-en-el-maresme", "h2": "Lo oficial, en Mataró y Argentona",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial más próximo es Pruna Motor, en la Via Sergia 2 de Mataró: 16 km por la ruta más corta; por la más rápida son 19,8. La estación de ITV más próxima por carretera en el registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 19,4 km.",
             "Para el mantenimiento periódico no hace falta pasar por el concesionario: el Reglamento (UE) 461/2010 permite revisar el coche fuera de la red oficial sin perder la garantía, siempre que se cumplan los intervalos y especificaciones del fabricante.",
         ]},
        {"id": "c32-b20", "h2": "57 kilómetros por la C-32",
         "parrafos": [
             "Desde Canet, la N-II pasa a 0,4 km y la C-32 a 1 km. La ruta al taller va por la C-32 y la B-20 hasta el carrer del Tambor del Bruc: 57 km por carretera, 49,8 en línea recta. La recogida del taller solo cubre el área metropolitana de Barcelona, y Canet queda fuera.",
             "A esa distancia, lo razonable es dejar las revisiones de rutina para un taller del Maresme y reservar el viaje para una avería propia de BMW. Antes, llama con el modelo, el año, los kilómetros y lo que notas: así llegas con hora y, si hace falta, con el recambio pedido.",
         ]},
        {"id": "canet-en-cifras", "h2": "15.198 vecinos en 5,56 km²",
         "parrafos": [
             "Canet de Mar tenía 15.198 habitantes en 2025, un 7,2 % más que en 2015, en un término de 5,56 km². Idescat, a partir de la DGT, contaba 6.523 turismos en 2024: 429 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Hacéis revisiones a coches de Canet de Mar?",
         "a": "Sí, en el taller de Sant Joan Despí, a 57 km. Desde aquí no hay recogida: el coche lo traes tú."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Argentona (B08), en el polígono El Cros, a 19,4 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sergia 2 de Mataró, a 16 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "15.198 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("080403")},
        {"etiqueta": "Turismos (2024)", "valor": "6.523 · 429 por cada 1.000 hab.", **F.idescat("080403")},
        {"etiqueta": "Distancia a la costa", "valor": "1,1 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Argentona (B08) · 19,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 16 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 57 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080403"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["moralzarzal"] = {
    "h1": "Moralzarzal: taller especialista BMW a 42,4 km y la ITV de Cerceda a 5,8",
    "entradilla": "Quien busca taller en Moralzarzal suele querer uno en el pueblo, y conviene decirlo pronto: el nuestro está en Alcobendas. Te contamos cuándo compensa el viaje, qué tienes cerca en la sierra y dónde está el servicio oficial de Las Rozas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 42.4},
    "secciones": [
        {"id": "no-es-un-taller-del-pueblo", "h2": "No es un taller del pueblo, y por qué puede interesarte igual",
         "parrafos": [
             "Dasercars Madrid está en la calle Valgrande 17 de Alcobendas, a 42,4 km de Moralzarzal por carretera. No tenemos nave en la sierra. Para cambiar una rueda o unas escobillas, un taller de la zona te lo resuelve antes; para un BMW o un MINI con una avería que nadie ha encontrado, un ruido de distribución en un diésel N47 o un fallo del sistema de AdBlue, la especialización sí pesa.",
             "El presupuesto se da por escrito y el coche no se toca hasta que lo apruebas; la diagnosis también se presupuesta. Así puedes decidir si el viaje merece la pena antes de hacerlo.",
         ]},
        {"id": "m608-m607-m616", "h2": "Por la M-608, la M-607 y la M-616",
         "parrafos": [
             "La ruta más corta desde el centro sale por la M-608, que pasa a 0,3 km, sigue por la M-607 y enlaza con la M-616 hasta Alcobendas: 42,4 km por carretera y 31,2 en línea recta.",
             "La recogida y entrega del taller funciona en el área metropolitana de Madrid y está sujeta a disponibilidad; desde la sierra, confírmala al reservar antes de contar con ella.",
         ]},
        {"id": "itv-cerceda", "h2": "La ITV, en la M-607 a la altura de Cerceda",
         "parrafos": [
             "La estación oficial más próxima por carretera es la de I.T.V. Cerceda (la 2866 del listado de la Comunidad de Madrid), en la M-607, km 48,2: 5,8 km desde el centro de Moralzarzal.",
         ]},
        {"id": "movilnorte-las-rozas", "h2": "El servicio oficial, en Las Rozas",
         "parrafos": [
             "Si lo que buscas es el concesionario de Las Rozas, el punto oficial BMW más cercano según bmw.es es Movilnorte, en la A-6, km 23,100, a 22,7 km. Las campañas de revisión que convoque la marca y las reparaciones en garantía de BMW se hacen allí.",
         ]},
        {"id": "a-974-metros", "h2": "974 metros y un pueblo que ha crecido un 21 %",
         "parrafos": [
             "Moralzarzal tenía 12.213 habitantes en 2015 y 14.772 en 2025. A 974 metros, el invierno pide revisar la batería antes de las primeras heladas y, en un diésel, también los calentadores: un arranque largo en frío suele ser el primer aviso de que alguno ha dejado de funcionar.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Moralzarzal?",
         "a": "No. El taller de la red es Dasercars Madrid, en la calle Valgrande 17 de Alcobendas, a 42,4 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de I.T.V. Cerceda, en la M-607, km 48,2, a 5,8 km del centro."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Movilnorte, en la A-6, km 23,100 de Las Rozas, a 22,7 km según el localizador de bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "14.772 habitantes (+21 % desde 2015)", **F.ine},
        {"etiqueta": "Altitud del centro urbano", "valor": "974 m", **F.copernicus},
        {"etiqueta": "ITV oficial más cercana", "valor": "I.T.V. Cerceda, M-607 km 48,2 · 5,8 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte, Las Rozas · 22,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 42,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["alovera"] = {
    "h1": "Alovera y el concesionario BMW de Guadalajara: quién es quién y dónde está el taller",
    "entradilla": "Si has llegado buscando un taller BMW en Guadalajara, te aclaramos antes de nada quién es quién: el concesionario está en la capital, a 10,1 km de Alovera, y nosotros somos un taller independiente con nave en Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 46.2},
    "secciones": [
        {"id": "el-concesionario-de-guadalajara", "h2": "El concesionario de Guadalajara no somos nosotros",
         "parrafos": [
             "El servicio oficial BMW más próximo a Alovera según bmw.es es AutoPremier, en el Paseo de la Estación 23 de Guadalajara, a 10,1 km por carretera. Es concesionario con taller propio: si te llega una carta de BMW para una campaña de revisión, la cita es allí.",
             "Dasercars es otra cosa: un taller especializado en BMW y MINI que no pertenece a la red oficial, con nave en la calle Valgrande 17 de Alcobendas. Lo decimos claro para que no llames creyendo que hablas con el concesionario.",
         ]},
        {"id": "a2-r2-m50", "h2": "46,2 km por la A-2, la R-2 y la M-50",
         "parrafos": [
             "La A-2 pasa a 1,5 km del centro de Alovera y la R-2 a 1,6. Por ellas, y luego por la M-50, se llega al taller: 46,2 km por carretera, 34,8 en línea recta. Alovera es provincia de Guadalajara y queda fuera del área metropolitana de Madrid, donde el taller ofrece recogida, así que el coche lo traes tú.",
             "Compensa para trabajos en los que se nota la especialización: un filtro de partículas que se satura una y otra vez, un fallo de inyectores en un N57, un problema eléctrico intermitente o un ruido que ya han mirado sin éxito en otro sitio.",
         ]},
        {"id": "de-12247-a-14526", "h2": "De 12.247 a 14.526 vecinos en diez años",
         "parrafos": [
             "El padrón del INE da a Alovera 14.526 habitantes en 2025, un 18,6 % más que en 2015. El término mide 13,7 km² y tiene siete carreteras con número a menos de tres kilómetros del centro —la A-2, la R-2, la N-320 o la CM-1008, entre otras—: la autovía queda a un paso.",
             "Para un diésel, alternar los trayectos cortos con un tramo de autovía a ritmo constante es lo que le permite regenerar el filtro de partículas sin ayuda. Si el testigo del filtro aparece a menudo, suele ser señal de que el coche hace casi solo recorridos cortos.",
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Guadalajara?",
         "a": "No. El concesionario es AutoPremier, en el Paseo de la Estación 23. Nosotros somos Dasercars, taller independiente especializado en BMW, en Alcobendas."},
        {"q": "¿Tenéis taller en Alovera?",
         "a": "No. El taller de la red más cercano está en Alcobendas, a 46,2 km de Alovera por carretera."},
        {"q": "¿Recogéis el coche en Alovera?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Madrid, y Alovera queda fuera."},
        {"q": "¿Trabajáis también MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "14.526 habitantes (+18,6 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "13,7 km²", **F.cartociudad},
        {"etiqueta": "Altitud del centro urbano", "valor": "641 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Guadalajara · 10,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 46,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["velilla-de-san-antonio"] = {
    "h1": "Velilla de San Antonio: ITV a 4,9 km en Mejorada y especialista BMW a 34,2 km",
    "entradilla": "En el sureste de la Comunidad de Madrid, Velilla de San Antonio tiene la ITV en el polígono del municipio vecino. El taller especialista BMW de la red está en Alcobendas, a 34,2 km; aquí van la ruta y las alternativas que tienes más cerca.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 34.2},
    "secciones": [
        {"id": "itv-mejorada", "h2": "La ITV, en la calle Levante de Mejorada del Campo",
         "parrafos": [
             "La estación oficial más cercana por carretera es la de ITV Barbastro (la 2819 del listado de la Comunidad de Madrid), en la calle Levante 10 del polígono industrial de Mejorada del Campo: 4,9 km desde el centro de Velilla, 2,6 en línea recta.",
         ]},
        {"id": "m208-r3-m30", "h2": "M-208, R-3, M-30 y A-1",
         "parrafos": [
             "La M-208 pasa a 0,2 km del centro y la R-3 a 1,8. La ruta hasta la calle Valgrande de Alcobendas encadena las dos, cruza por la M-30 y sale por la A-1: 34,2 km por carretera, 23,7 en línea recta.",
             "Para trabajos de varios días, el taller tiene vehículo de cortesía y recogida y entrega dentro del área metropolitana de Madrid, ambos sujetos a disponibilidad. Pregunta al reservar si tu calle entra.",
         ]},
        {"id": "carretera-de-valencia", "h2": "El concesionario más cercano, en la carretera de Valencia",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo es AutoPremier, en la carretera de Valencia, km 7,3, ya en el término de Madrid, a 18,7 km. Ahí van las reparaciones que paga la garantía de BMW.",
             "Para el resto —mantenimiento, diagnosis, reparaciones fuera de garantía— el taller lo eliges tú, también si tienes un MINI, que comparte electrónica y motores con BMW.",
         ]},
        {"id": "velilla-en-cifras", "h2": "14.468 vecinos y 8.298 turismos",
         "parrafos": [
             "Velilla de San Antonio tenía 12.382 habitantes en 2015 y 14.468 en 2025, un 16,8 % más. La Comunidad de Madrid, a partir de la DGT, contaba 8.298 turismos en 2025: 574 por cada 1.000 vecinos, frente a 388 en Madrid capital. El término mide 14,3 km² y el centro está a 551 metros de altitud.",
             "Con la R-3 tan cerca, un diésel de Velilla tiene fácil hacer de vez en cuando el tramo a velocidad constante que necesita el filtro de partículas para limpiarse; los problemas llegan cuando el coche solo se usa para recados dentro del pueblo.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Velilla?",
         "a": "En ITV Barbastro, calle Levante 10, polígono industrial de Mejorada del Campo, a 4,9 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "34,2 km por la M-208, la R-3, la M-30 y la A-1, hasta la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Podéis recoger el coche en Velilla?",
         "a": "La recogida y entrega se ofrece dentro del área metropolitana de Madrid, sujeta a disponibilidad: confírmala al pedir cita."},
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "AutoPremier, en la carretera de Valencia, km 7,3 (Madrid), a 18,7 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "14.468 habitantes (+16,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "8.298 · 574 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITV Barbastro, Mejorada del Campo · 4,9 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, ctra. de Valencia km 7,3 · 18,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 34,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["valdemorillo"] = {
    "h1": "Mantenimiento de un BMW en Valdemorillo: lo que tienes cerca y el taller a 49,6 km",
    "entradilla": "Valdemorillo tiene un término enorme, 93,4 km², y la ITV y el servicio oficial BMW más próximos quedan a casi 20 km o más. Te ordenamos las opciones para el mantenimiento del coche, con el taller especialista de la red en Alcobendas como referencia.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 49.6},
    "secciones": [
        {"id": "plan-de-mantenimiento", "h2": "Revisiones por plan de BMW, sin pasar por el concesionario",
         "parrafos": [
             "Un BMW avisa de su mantenimiento con el indicador de servicio: aceite, filtros, líquido de frenos o bujías tienen cada uno su plazo, en kilómetros o en tiempo. Lo que importa es cumplirlo con el aceite de la homologación que pide el motor y recambios de la especificación correcta, y que quede registrado y el indicador reiniciado.",
             "Si el coche está en garantía, el Reglamento (UE) 461/2010 deja claro que esas revisiones pueden hacerse en un taller independiente sin perderla, siempre que se respeten intervalos y especificaciones.",
         ]},
        {"id": "cuatro-itv", "h2": "Cuatro ITV casi a la misma distancia",
         "parrafos": [
             "Desde el centro de Valdemorillo, cuatro estaciones del listado oficial de la Comunidad de Madrid quedan casi empatadas por carretera: la de ITEVELESA en la A-6, km 37,6, a 19,8 km; la de ITV P-29 (estación 2883) y la de TÜV SÜD ATISAE (2813), las dos en Collado Villalba, a 20 y 20,1 km; y la de TÜV SÜD ATISAE en Las Rozas (2816), a 20,3. Escoge por la cita disponible, no por la distancia.",
         ]},
        {"id": "m600-hasta-alcobendas", "h2": "49,6 km por la M-600, la M-503 y la M-40",
         "parrafos": [
             "La M-600 pasa a 0,8 km del centro y es la salida natural hacia el taller: M-600, M-503, M-40 y A-1 hasta la calle Valgrande de Alcobendas, 49,6 km por carretera y 35,4 en línea recta. El servicio oficial más próximo según bmw.es es Movilnorte, en la carretera de El Plantío 62 de Majadahonda, a 24,5 km.",
             "A 810 metros de altitud, antes del invierno vale la pena medir la batería y comprobar el anticongelante. Si la batería se cambia, se registra en la centralita.",
         ]},
        {"id": "valdemorillo-en-cifras", "h2": "619 turismos por cada mil vecinos",
         "parrafos": [
             "Valdemorillo tenía 14.420 habitantes en 2025, un 18,5 % más que en 2015, repartidos en 93,4 km²: 154 por kilómetro cuadrado. La Comunidad de Madrid, a partir de la DGT, contaba 8.928 turismos en 2025, 619 por cada 1.000 habitantes.",
         ]},
    ],
    "faq": [
        {"q": "¿Pierdo la garantía si hago la revisión fuera del concesionario?",
         "a": "No, siempre que se respeten los intervalos y las especificaciones del plan de mantenimiento de BMW."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de ITEVELESA en la A-6, km 37,6, a 19,8 km, aunque otras tres en Collado Villalba y Las Rozas están a menos de un kilómetro más."},
        {"q": "¿Recogéis el coche en Valdemorillo?",
         "a": "La recogida y entrega se ofrece en el área metropolitana de Madrid, sujeta a disponibilidad; confirma al reservar si tu dirección entra."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "14.420 habitantes (+18,5 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "8.928 · 619 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Superficie del término", "valor": "93,4 km²", **F.cartociudad},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITEVELESA, A-6 km 37,6 · 19,8 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte, Majadahonda · 24,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 49,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.cartociudad_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["casar-el"] = {
    "h1": "El Casar: especialista BMW a 33,6 km por la A-1 y servicio oficial en Algete",
    "entradilla": "El Casar es provincia de Guadalajara, pero lo que tiene más cerca en BMW está en la Comunidad de Madrid: el servicio oficial en Algete y el taller especialista de la red en Alcobendas. Las distancias de esta página se miden desde el centro del casco urbano.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 33.6},
    "secciones": [
        {"id": "guadalajara-o-algete", "h2": "Provincia de Guadalajara, servicio oficial en Algete",
         "parrafos": [
             "Aunque el municipio es de Guadalajara, el punto oficial BMW más cercano por carretera según bmw.es no está en la capital de la provincia sino en Algete: BYmyCAR Madrid, en la calle Tejera 2, carretera de Algete km 3, a 18,6 km. Para una reparación en garantía, esa es la referencia.",
             "Nosotros no somos un concesionario: Dasercars es un taller independiente especializado en BMW y MINI, con nave en la calle Valgrande 17 de Alcobendas.",
         ]},
        {"id": "gu193-a1", "h2": "De la GU-193 a la A-1",
         "parrafos": [
             "El término mide 52 km², así que importa desde dónde se mide. Desde el centro del casco urbano, la ruta más corta sale por la GU-193, pasa por la M-117, la M-111 y la M-100 y entra en la A-1: 33,6 km hasta la calle Valgrande, 26,2 en línea recta.",
             "El Casar no está en el área metropolitana de Madrid, y la recogida y entrega del taller no llega hasta aquí: el coche lo traes tú. Para que el viaje no sea en balde, describe el síntoma por teléfono antes de venir.",
         ]},
        {"id": "a-849-metros", "h2": "A 849 metros: invierno, batería y carretera abierta",
         "parrafos": [
             "El centro urbano está a 849 metros de altitud. Una batería con años encima suele fallar la primera mañana fría, y en los BMW con mucho consumo eléctrico se nota antes. Merece la pena medirla en otoño; si se cambia, hay que registrarla en la centralita para que la carga se ajuste a la nueva.",
             "Con la N-320 a 0,4 km y la CM-1009 a 0,8, el coche sale enseguida a carretera abierta, que es donde un diésel completa la regeneración del filtro de partículas.",
         ]},
        {"id": "el-casar-crece", "h2": "13.962 vecinos, un 20,3 % más que en 2015",
         "parrafos": [
             "El padrón del INE pasó de 11.606 habitantes en 2015 a 13.962 en 2025. Son 2.356 vecinos más en diez años.",
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Guadalajara?",
         "a": "No. Somos Dasercars, taller independiente especializado en BMW, en Alcobendas. El servicio oficial más cercano a El Casar es BYmyCAR Madrid, en Algete."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "33,6 km desde el centro del casco urbano, por la GU-193, la M-117, la M-111, la M-100 y la A-1."},
        {"q": "¿Recogéis el coche en El Casar?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Madrid, y El Casar queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "13.962 habitantes (+20,3 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "52 km²", **F.cartociudad},
        {"etiqueta": "Altitud del centro urbano", "valor": "849 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid, Algete · 18,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 33,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["san-agustin-del-guadalix"] = {
    "h1": "San Agustín del Guadalix: el taller BMW de la red, a 21,2 km bajando por la A-1",
    "entradilla": "Con la A-1 a 0,4 km del centro, desde San Agustín del Guadalix el taller especialista queda a una sola autovía de distancia, en Alcobendas. La ITV, en cambio, la tienes en El Molar, y el servicio oficial, en Algete.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 21.2},
    "secciones": [
        {"id": "solo-la-a1", "h2": "21,2 kilómetros sin salir de la A-1",
         "parrafos": [
             "La ruta al taller es la más sencilla posible: A-1 hacia Madrid hasta Alcobendas y desvío a la calle Valgrande. Son 21,2 km por carretera y 16 en línea recta. La M-104 también pasa junto al casco, a 0,3 km.",
             "El taller trabaja de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00. A esta distancia, dejar el coche a primera hora y recogerlo por la tarde es perfectamente viable para un trabajo de un día.",
             "Recogida y entrega, y vehículo de cortesía para trabajos de varios días: existen dentro del área metropolitana de Madrid y están sujetos a disponibilidad. Si los necesitas, pídelos al reservar y confirma que tu dirección entra.",
         ]},
        {"id": "itv-el-molar", "h2": "La ITV, en la A-1 a la altura de El Molar",
         "parrafos": [
             "La estación oficial más cercana por carretera es la de ITEVELESA en la A-1, km 40,200, en el término de El Molar: 6,7 km desde el centro de San Agustín, según el listado de la Comunidad de Madrid. Está en la misma A-1 que lleva al taller.",
         ]},
        {"id": "bymycar-algete", "h2": "El servicio oficial, en Algete",
         "parrafos": [
             "El punto oficial BMW más próximo según bmw.es es BYmyCAR Madrid, en la calle Tejera 2 de Algete, a 19,1 km por carretera: casi la misma distancia que nuestro taller.",
             "La diferencia no está en los kilómetros sino en lo que hace cada uno: en el concesionario, la garantía de BMW; en un taller independiente especializado, el mantenimiento y las reparaciones de un BMW o un MINI, con la diagnosis presupuestada antes de empezar.",
         ]},
        {"id": "san-agustin-en-cifras", "h2": "556 turismos por cada mil habitantes",
         "parrafos": [
             "El padrón de 2025 da a San Agustín del Guadalix 13.825 habitantes, un 6,5 % más que diez años antes (12.982). En 2025 había 7.689 turismos censados, según la Comunidad de Madrid a partir de la DGT. El casco está a 675 metros de altitud y el término ocupa 38,1 km².",
         ]},
    ],
    "faq": [
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 21,2 km por la A-1, en la calle Valgrande 17 de Alcobendas."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de ITEVELESA en la A-1, km 40,200 (El Molar), a 6,7 km."},
        {"q": "¿Hay un servicio oficial BMW cerca?",
         "a": "BYmyCAR Madrid, en la calle Tejera 2 de Algete, a 19,1 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "13.825 habitantes (+6,5 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "7.689 · 556 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITEVELESA, A-1 km 40,200 (El Molar) · 6,7 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid, Algete · 19,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 21,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["abrera"] = {
    "h1": "Abrera: especialista BMW independiente a 25,5 km, todo por la A-2",
    "entradilla": "Desde Abrera, la A-2 pasa a 0,2 km del centro y lleva sin desvíos hasta Sant Joan Despí, donde está el taller de la red. Antes de llamar, conviene aclarar qué somos y qué no.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 25.5},
    "secciones": [
        {"id": "no-somos-red-oficial", "h2": "Ni concesionario ni red oficial: un taller independiente",
         "parrafos": [
             "Hay quien llega aquí buscando un concesionario de la red oficial con nombre de Barcelona. Dasercars no lo es: somos un taller independiente especializado en BMW y MINI, sin relación con los concesionarios de la marca.",
             "El punto oficial BMW más próximo a Abrera según el localizador de bmw.es es Quadis Munich, en el carrer Anoia 9 de Terrassa, a 17,5 km por carretera. Para una reparación cubierta por la garantía de BMW o una campaña de la marca, ese es el sitio.",
         ]},
        {"id": "todo-por-la-a2", "h2": "25,5 kilómetros, todos por la A-2",
         "parrafos": [
             "La ruta más corta desde el centro de Abrera al carrer del Tambor del Bruc no cambia de carretera: A-2 hasta Sant Joan Despí, 25,5 km por carretera y 21,6 en línea recta. Además de la A-2, a menos de tres kilómetros pasan la C-55, la B-40, la C-1414 y la N-IIa.",
             "Abrera es del Baix Llobregat, pero no pertenece al Área Metropolitana de Barcelona, y la recogida del taller no llega hasta aquí. Con esta distancia, lo práctico es traer el coche por la mañana y volver a por él por la tarde si el trabajo es de un día.",
         ]},
        {"id": "itv-sant-andreu", "h2": "La ITV, en la N-II a su paso por Sant Andreu de la Barca",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Sant Andreu de la Barca (B21), en la carretera N-II, punto kilométrico 592,5, a 10,6 km del centro de Abrera.",
         ]},
        {"id": "abrera-en-cifras", "h2": "13.227 vecinos y 7.410 turismos",
         "parrafos": [
             "Abrera tenía 13.227 habitantes en 2025, un 9,6 % más que en 2015. Idescat, con datos de la DGT, contaba 7.410 turismos en 2024: 560 por cada 1.000 habitantes, el doble que en Barcelona ciudad (281).",
             "Con autovía a la puerta, un diésel tiene fácil completar la regeneración del filtro de partículas; el problema aparece cuando el coche solo hace recorridos cortos por el pueblo y la autovía se queda para el fin de semana.",
         ]},
    ],
    "faq": [
        {"q": "¿Sois un concesionario BMW?",
         "a": "No. Dasercars es un taller independiente especializado en BMW y MINI. El servicio oficial más cercano a Abrera es Quadis Munich, en Terrassa."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 25,5 km por la A-2, en el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
        {"q": "¿Recogéis el coche en Abrera?",
         "a": "No: la recogida cubre solo el área metropolitana de Barcelona, y Abrera queda fuera."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Sant Andreu de la Barca (B21), en la N-II, a 10,6 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "13.227 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080018")},
        {"etiqueta": "Turismos (2024)", "valor": "7.410 · 560 por cada 1.000 hab.", **F.idescat("080018")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu de la Barca (B21) · 10,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Terrassa · 17,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 25,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080018"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["castellbisbal"] = {
    "h1": "Castellbisbal: taller BMW a 17,1 km y recogida dentro del área metropolitana",
    "entradilla": "Castellbisbal forma parte del Área Metropolitana de Barcelona, y eso cambia las cosas: el taller de Sant Joan Despí queda a 17,1 km y puede ir a buscar el coche, según disponibilidad. Aquí van la ruta, la ITV y el servicio oficial más cercano.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 17.1},
    "secciones": [
        {"id": "si-no-puedes-acercarlo", "h2": "Si no puedes acercar el coche",
         "parrafos": [
             "Al estar dentro del área metropolitana, el taller ofrece recogida y entrega del coche, y vehículo de cortesía para los trabajos que se alargan, siempre sujetos a disponibilidad. Pídelo al reservar la cita, no el mismo día.",
             "Si prefieres traerlo tú, no vas a ciegas: recibes el presupuesto por escrito y nada se empieza sin tu visto bueno.",
         ]},
        {"id": "b150-c1413a-b23", "h2": "Por la B-150, la C-1413a y la B-23",
         "parrafos": [
             "La ruta más corta desde el centro sale por la B-150, sigue por la C-1413a y entra en la B-23 hasta el carrer del Tambor del Bruc: 17,1 km por carretera, 13,9 en línea recta. A menos de tres kilómetros del casco pasan también la AP-7, a 0,9 km, y la A-2, a 1,5.",
             "Castellbisbal tenía 13.061 habitantes en 2025, un 5,6 % más que en 2015, y 7.514 turismos en 2024 según Idescat a partir de la DGT: 575 por cada 1.000 habitantes, en un término de 31,03 km².",
         ]},
        {"id": "itv-b21", "h2": "La ITV, a 5 km en Sant Andreu de la Barca",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sant Andreu de la Barca (B21), en la N-II, punto kilométrico 592,5: 5 km desde el centro de Castellbisbal, 2,5 en línea recta.",
         ]},
        {"id": "quadis-sant-cugat", "h2": "El servicio oficial, en Sant Cugat",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más cercano es Quadis Munich, en el carrer Vallespir 19 de Sant Cugat del Vallès: 12,1 km por la ruta más corta y 13,3 por la más rápida. Allí corresponden las reparaciones en garantía de BMW; el mantenimiento puedes hacerlo donde quieras.",
             "Con la AP-7 y la A-2 tan cerca, es fácil darle a un diésel el tramo de autopista que necesita para limpiar el filtro de partículas. Si aun así el aviso del filtro vuelve, el origen suele estar en un sensor de presión diferencial o en la válvula EGR, y conviene diagnosticarlo antes de forzar una regeneración.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Castellbisbal?",
         "a": "Sí: está dentro del área metropolitana de Barcelona. La recogida y entrega está sujeta a disponibilidad; pídela al reservar."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 17,1 km por carretera, en el carrer del Tambor del Bruc 3 de Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Sant Andreu de la Barca (B21), en la N-II, a 5 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "13.061 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("080543")},
        {"etiqueta": "Turismos (2024)", "valor": "7.514 · 575 por cada 1.000 hab.", **F.idescat("080543")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu de la Barca (B21) · 5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Cugat del Vallès · 12,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 17,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080543"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
CIUDADES["badia-del-valles"] = {
    "h1": "Badia del Vallès: dos servicios oficiales BMW a 4 km y el especialista a 29,1",
    "entradilla": "Badia del Vallès cabe en 0,93 km², y la ITV y el servicio oficial BMW los tiene en Sabadell, a pocos kilómetros. Nuestro taller está más lejos, en Sant Joan Despí, pero Badia es área metropolitana y eso permite pedir la recogida del coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 29.1},
    "secciones": [
        {"id": "sitjas-y-quadis", "h2": "Sitjas y Quadis, los dos en Sabadell y casi a la par",
         "parrafos": [
             "El localizador de bmw.es da dos puntos oficiales casi a la misma distancia del centro de Badia: Sitjas Motor, taller autorizado BMW en la calle Quintana 64 de Sabadell, a 3,7 km por carretera, y Quadis Munich, también en Sabadell, a 4 km. Para lo que cubra la garantía del fabricante, cualquiera de los dos.",
             "Dasercars no es ninguno de ellos: somos un taller independiente especializado en BMW y MINI. Lo nuestro es el mantenimiento y las reparaciones fuera de garantía, que puedes llevar al taller que elijas.",
         ]},
        {"id": "itv-can-roqueta", "h2": "La ITV de Sabadell, a 6,7 km",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Sabadell (B24), en el carrer Can Camps del polígono Can Roqueta, a 6,7 km del centro de Badia (3 en línea recta).",
         ]},
        {"id": "ruta-ap7", "h2": "29,1 km por carretera para 16,6 en línea recta",
         "parrafos": [
             "La diferencia entre las dos cifras la marca la ruta: desde Badia hay que salir por la B-30, tomar la AP-7 y bajar por la B-23 hasta Sant Joan Despí. No hay un camino directo.",
             "Badia es uno de los municipios del Área Metropolitana de Barcelona, así que el taller puede recoger el coche y devolverlo, y prestarte uno de cortesía si la reparación dura días; las dos cosas, sujetas a disponibilidad.",
         ]},
        {"id": "badia-en-cifras", "h2": "14.043 habitantes por kilómetro cuadrado",
         "parrafos": [
             "Con 13.060 vecinos en 2025 y 0,93 km² de término, Badia tiene una densidad de 14.043 habitantes por km². Y ha perdido población: tenía 13.502 vecinos en 2015, de modo que hoy son un 3,3 % menos.",
             "El parque de 2024, según Idescat a partir de la DGT, era de 5.748 turismos: 440 por cada 1.000 habitantes. Con la C-58, la AP-7, la B-30 y la N-150 a un kilómetro o menos del centro, la autovía queda literalmente a la salida de casa. Aun así, si el coche pasa días aparcado sin moverse, la batería es lo primero que lo nota.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Badia?",
         "a": "Sitjas Motor, en la calle Quintana 64 de Sabadell, a 3,7 km, y Quadis Munich, también en Sabadell, a 4 km, según bmw.es."},
        {"q": "¿Recogéis el coche en Badia del Vallès?",
         "a": "Sí, dentro del área metropolitana de Barcelona hay recogida y entrega, sujeta a disponibilidad."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación de Sabadell (B24), polígono Can Roqueta, a 6,7 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "13.060 habitantes (−3,3 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "0,93 km² · 14.043 hab./km²", **F.idescat("089045")},
        {"etiqueta": "Turismos (2024)", "valor": "5.748 · 440 por cada 1.000 hab.", **F.idescat("089045")},
        {"etiqueta": "ITV más cercana", "valor": "Sabadell (B24) · 6,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Sitjas Motor, Sabadell · 3,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 29,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("089045"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
