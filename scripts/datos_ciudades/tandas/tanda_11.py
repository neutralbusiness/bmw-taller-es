# Tanda 11: Monistrol de Calders, les Masies de Roda, Ambite, Muntanyola, Puigdàlber, Rajadell,
# Campins, Valverde de Alcalá, Oristà, Fogars de Montclús, Borredà, Perafita, Olmeda de las Fuentes,
# Gargantilla del Lozoya y Pinilla de Buitrago y Orís.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py.
# Notas de datos:
#  - Rajadell: 7.508 turismos para 597 vecinos (flotas domiciliadas): no se publica el parque.
#  - Borredà y Perafita tienen exactamente los mismos turismos (259) y la misma proporción (598):
#    sospechoso, no se publica el parque en ninguna de las dos.
#  - Valverde de Alcalá y Olmeda de las Fuentes: la ITV de Alcalá tiene precisión de municipio;
#    la distancia se da como aproximada («unos … km, hasta el centro de Alcalá»).
# META: metaDescription nueva para las ciudades sin impresiones (todas menos Gargantilla, que tiene
# 1 impresión en 90 días) cuya descripción prometía recogida a domicilio, diagnosis «oficial»/ISTA,
# «presupuesto gratis», garantía por escrito o presencia física. Se aplica con
#   python3 -c "import sys; sys.path.insert(0,'scripts/datos_ciudades/tandas'); import tanda_11; tanda_11.aplicar_meta()"
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
META = {}

# ─────────────────────────────────────────────────────────────────────────────
META["monistrol-de-calders"] = "BMW en Monistrol de Calders (Moianès): servicio oficial e ITV en Sant Fruitós de Bages y taller especialista independiente a 78 km, en Sant Joan Despí."
CIUDADES["monistrol-de-calders"] = {
    "h1": "Monistrol de Calders: ITV y servicio oficial BMW en Sant Fruitós, especialista a 78 km",
    "entradilla": "Para un BMW o un MINI matriculado en Monistrol de Calders, casi todo lo oficial queda en el mismo polígono de Sant Fruitós de Bages. El taller especialista de la red está bastante más lejos, en Sant Joan Despí, y aquí te explicamos cuándo merece la pena.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 78.0},
    "secciones": [
        {"id": "todo-en-sant-fruitos", "h2": "Una sola salida para la ITV y el concesionario",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto de servicio oficial más próximo en Quadis Munich, carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 19,7 km por carretera. La estación de ITV que el registro de la Generalitat da como más próxima por carretera también está allí, la B25 del polígono El Grau, a 23 km.",
             "Juntar las dos visitas en la misma mañana es razonable. Para el mantenimiento, no estás obligado a pasar por el concesionario: el Reglamento (UE) 461/2010 protege la garantía del fabricante cuando las revisiones se hacen fuera de la red con los intervalos y recambios que marca BMW."
         ]},
        {"id": "cuarenta-y-tres-en-recta", "h2": "43,6 km en línea recta, 78 por carretera",
         "parrafos": [
             "La diferencia entre las dos cifras dice mucho del trayecto. Desde Monistrol, la ruta hasta el carrer del Tambor del Bruc sale por la B-124, enlaza con la N-141c y baja por la C-16 y la B-20: 78 km para salvar 43,6 en línea recta. Recogida no hay: el servicio del taller cubre solo el área metropolitana de Barcelona.",
             "Por eso el viaje encaja con averías que requieren un especialista en la marca —electrónica que nadie ha localizado, un diésel N47 con ruido de distribución, un fallo de AdBlue— y no con un cambio de pastillas."
         ]},
        {"id": "sin-via-rapida", "h2": "Sin autovía a tres kilómetros: el filtro de partículas lo nota",
         "parrafos": [
             "Ninguna carretera principal pasa a menos de tres kilómetros del centro del pueblo. Un diésel que solo hace trayectos cortos por la zona difícilmente completa la regeneración del filtro de partículas, que necesita un rato de marcha constante.",
             "El municipio, de 21,97 km², tenía 764 vecinos en 2025, 67 más que en 2015, y 454 turismos en 2024 según Idescat: 594 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Monistrol de Calders?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la B25, en el polígono El Grau de Sant Fruitós de Bages, a 23 km."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "78 km por la B-124, la N-141c, la C-16 y la B-20 hasta Sant Joan Despí."},
        {"q": "¿Pierdo la garantía si no reviso el coche en el concesionario?",
         "a": "No, mientras se cumplan los intervalos y especificaciones del plan de mantenimiento de BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "764 habitantes (+9,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Moianès", **F.idescat("081287")},
        {"etiqueta": "Turismos (2024)", "valor": "454 · 594 por cada 1.000 hab.", **F.idescat("081287")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Fruitós (B25) · 23 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 19,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 78 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081287"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["les-masies-de-roda"] = "BMW en les Masies de Roda: ITV de Osona a 6,1 km y servicio oficial en Vic, a 9,9 km. El taller especialista independiente está en Sant Joan Despí, a 89,3 km."
CIUDADES["les-masies-de-roda"] = {
    "h1": "Les Masies de Roda: Vic a diez kilómetros y el especialista BMW a 89",
    "entradilla": "Desde el núcleo de les Masies de Roda, la ITV y el concesionario BMW quedan en Vic, a menos de diez kilómetros. Nuestro taller está a 89,3 km. Te contamos qué tiene sentido resolver en Osona y para qué conviene hacer el viaje.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 89.3},
    "secciones": [
        {"id": "vic-cerca", "h2": "Osona te lo pone fácil: ITV a 6,1 km",
         "parrafos": [
             "La estación ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22 de Vic, es la más próxima por carretera según el registro de la Generalitat: 6,1 km desde el centro del núcleo urbano. El servicio oficial BMW también está en Vic, Quadis Munich en la calle Perot Rocaguinarda 1, a 9,9 km según el localizador de bmw.es.",
             "Con las dos cosas tan a mano, el mantenimiento corriente y las campañas de la marca no justifican un viaje a Barcelona. Si el coche está en garantía, puedes revisarlo en un taller independiente sin perderla siempre que se respete el plan del fabricante; es lo que dice el Reglamento (UE) 461/2010."
         ]},
        {"id": "eje-c17", "h2": "Bajar por la C-17: cinco carreteras y 89,3 km",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona encadena la C-153, la C-25, la C-17, la C-33 y la B-20 hasta Sant Joan Despí. En línea recta son 72,3 km. La recogida del taller no llega a Osona: solo cubre el área metropolitana.",
             "Compensa cuando el problema es de BMW y no se ha resuelto en la comarca: un testigo que vuelve una y otra vez, una avería eléctrica intermitente o una cadena que suena en frío."
         ]},
        {"id": "pueblo-junto-a-roda", "h2": "758 vecinos y más de un coche por cada dos",
         "parrafos": [
             "Les Masies de Roda tenía 758 habitantes en el padrón de 2025, frente a 715 en 2015. Idescat, con datos de la DGT, contaba 480 turismos en 2024: 633 por cada 1.000 habitantes, más del doble que en Barcelona ciudad (281). Roda de Ter, el municipio vecino, queda a menos de un kilómetro en línea recta.",
             "Para un BMW que hace sobre todo recorridos cortos entre pueblos, la batería sufre más que en un coche de autovía. En los modelos de la marca, una batería nueva se registra en la centralita; si no, la carga no se ajusta a ella."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está la ITV más cercana a les Masies de Roda?",
         "a": "La ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22 de Vic, a 6,1 km por carretera."},
        {"q": "¿Y el servicio oficial BMW?",
         "a": "Quadis Munich, calle Perot Rocaguinarda 1 de Vic, a 9,9 km según bmw.es."},
        {"q": "¿Tenéis taller en Osona?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 89,3 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "758 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081167")},
        {"etiqueta": "Turismos (2024)", "valor": "480 · 633 por cada 1.000 hab.", **F.idescat("081167")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 6,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 9,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 89,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081167"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["ambite"] = "BMW en Ambite: ITV en Villarejo de Salvanés, servicio oficial en Alcalá de Henares y taller especialista independiente en Alcobendas, a 66,3 km por la R-3."
CIUDADES["ambite"] = {
    "h1": "Ambite: la ITV al sur, el concesionario BMW al norte y el especialista a 66 km",
    "entradilla": "Quien tiene un BMW o un MINI en Ambite tira hacia lados distintos según lo que necesite: la ITV queda en Villarejo de Salvanés, el servicio oficial en Alcalá de Henares y nuestro taller en Alcobendas. Te damos las distancias reales para que organices cada visita.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 66.3},
    "secciones": [
        {"id": "itv-villarejo", "h2": "La ITV de referencia está en Villarejo de Salvanés",
         "parrafos": [
             "Según el listado oficial de la Comunidad de Madrid, para pasar la inspección desde Ambite hay que bajar 24,7 km hasta Villarejo de Salvanés. Allí, en el número 13 de la avenida que lleva el nombre del rey Juan Carlos I, está la estación 2853, que gestiona General de Servicios ITV.",
             "Si además necesita un repaso, pide la pre-ITV cuando vaya al taller por otra cosa."
         ]},
        {"id": "r3-hasta-alcobendas", "h2": "Por la M-204 y la R-3 hasta la A-1",
         "parrafos": [
             "Hasta Alcobendas son 66,3 km (46 a vuelo de pájaro): primero la M-204 y la M-209, luego la radial R-3 hacia Madrid, un tramo de M-30 y, al final, la A-1 hasta la nave de Valgrande. La recogida que ofrece el taller es para el área metropolitana de Madrid; desde aquí no llega, así que el viaje lo haces tú.",
             "Hacia el norte, a 32,6 km, queda Alcalá de Henares: allí tiene AutoPremier el punto oficial que bmw.es da como más cercano. Para una campaña del fabricante es el sitio; para lo demás, compara."
         ]},
        {"id": "ambite-crece", "h2": "De 618 a 732 vecinos en diez años",
         "parrafos": [
             "El padrón del INE da a Ambite 732 habitantes en 2025, un 18,4 % más que en 2015. Hay 373 turismos censados (Comunidad de Madrid con datos de la DGT, 2025), algo más de uno por cada dos habitantes. A menos de tres kilómetros del centro pasan la M-215, la M-204 y la CM-2031, esta última ya de la red de Castilla-La Mancha.",
             "El pueblo está a unos 774 metros de altitud. Las heladas de invierno castigan las baterías cansadas, y en un BMW con arranque y parada automático la batería trabaja más que en un coche sencillo; revisarla antes del frío ahorra una mañana perdida."
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es la ITV más cercana a Ambite?",
         "a": "La 2853 de Villarejo de Salvanés: 24,7 km de carretera hacia el sur."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "66,3 km. La nave está en Alcobendas y se llega por la R-3."},
        {"q": "¿Dónde está el concesionario BMW más próximo?",
         "a": "El de AutoPremier en Alcalá de Henares, a 32,6 km por carretera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "732 habitantes (+18,4 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "373 · 510 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 774 m", **F.copernicus},
        {"etiqueta": "ITV más cercana", "valor": "Villarejo de Salvanés (estación 2853) · 24,7 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 32,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 66,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["muntanyola"] = "BMW en Muntanyola, a 807 m: qué revisar antes del invierno, ITV y servicio oficial en Vic y taller especialista independiente a 86 km, en Sant Joan Despí."
CIUDADES["muntanyola"] = {
    "h1": "Un BMW en Muntanyola, a 807 metros: frío, batería y el taller a 86 km",
    "entradilla": "A 807 metros de altitud, el invierno de Muntanyola se nota en el coche antes que en ningún otro sitio de la comarca baja. Aquí tienes lo que conviene vigilar, dónde están la ITV y el servicio oficial en Vic, y qué supone bajar a nuestro taller.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 86.0},
    "secciones": [
        {"id": "ochocientos-siete", "h2": "Lo que el frío le hace a un BMW a esta altitud",
         "parrafos": [
             "La batería es lo primero. Con temperaturas bajo cero pierde capacidad, y en un BMW con muchos consumidores eléctricos y arranque y parada automático va más justa que en un coche básico. Si ya tiene años, la primera helada lo destapa. Al cambiarla, recuerda que hay que registrarla en la centralita para que la carga se ajuste a la batería nueva.",
             "El anticongelante se comprueba por concentración, no solo por nivel: un circuito rellenado con agua durante el verano puede quedarse corto en enero. Y en bajadas largas, unos frenos con el líquido envejecido pierden eficacia antes; ese líquido se cambia por tiempo, aunque el coche ande poco."
         ]},
        {"id": "vic-a-diez", "h2": "Servicio oficial a 10,7 km, ITV a 15,1",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 10,7 km por carretera. La ITV de referencia, la estación Osona (B04) del registro de la Generalitat, también en Vic, queda a 15,1 km.",
             "Las campañas de llamada a revisión las gestiona la red oficial. Lo demás —mantenimiento, diagnosis, reparaciones fuera de garantía— puedes hacerlo donde prefieras."
         ]},
        {"id": "bv4316-c17", "h2": "De la BV-4316 a la C-17 y la B-20",
         "parrafos": [
             "Para llegar a Dasercars Barcelona se baja por la BV-4316 hasta la C-17, y luego la C-33 y la B-20 hasta Sant Joan Despí: 86 km por carretera, 59,8 en línea recta. El servicio de recogida del taller no llega a Osona.",
             "Con esa distancia, el viaje se justifica para lo que es propio de la marca y no ha encontrado solución cerca. Muntanyola, con 40,3 km² de término, tenía 697 vecinos en 2025 —un 15 % más que en 2015— y 409 turismos en 2024 según Idescat: 587 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Qué revisar en el coche antes del invierno en Muntanyola?",
         "a": "Batería, concentración del anticongelante, neumáticos y estado del líquido de frenos."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima en el registro de la Generalitat es la de Osona (B04), en Vic, a 15,1 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "86 km por la BV-4316, la C-17, la C-33 y la B-20 hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "697 habitantes (+15 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081290")},
        {"etiqueta": "Altitud", "valor": "807 m", **F.idescat("081290")},
        {"etiqueta": "Turismos (2024)", "valor": "409 · 587 por cada 1.000 hab.", **F.idescat("081290")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 15,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 10,7 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081290"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["puigdalber"] = "BMW en Puigdàlber (Alt Penedès): ITV en Olèrdola a 8,9 km, servicio oficial en Vilanova i la Geltrú y taller especialista independiente a 51,9 km por la AP-7."
CIUDADES["puigdalber"] = {
    "h1": "Puigdàlber, 0,4 km² de término: tu BMW, la C-15 y el taller a 51,9 km",
    "entradilla": "Puigdàlber cabe en menos de medio kilómetro cuadrado. Para el coche, lo que importa es lo que hay alrededor: la ITV en Olèrdola, el servicio oficial BMW en Vilanova i la Geltrú y nuestro taller en Sant Joan Despí, a 51,9 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 51.9},
    "secciones": [
        {"id": "medio-kilometro", "h2": "Un término de 0,4 km² con 1.552 vecinos por km²",
         "parrafos": [
             "Según Idescat, el término municipal de Puigdàlber mide 0,4 km². Con 621 habitantes en el padrón de 2025 —539 en 2015, un 15,2 % más—, la densidad es de 1.552 por km². En 2024 había 337 turismos censados, 543 por cada 1.000 vecinos.",
             "Todo lo que el coche necesita está fuera del término, empezando por la carretera: la C-15 pasa a menos de tres kilómetros y es la puerta de salida hacia la AP-7."
         ]},
        {"id": "itv-olerdola", "h2": "La ITV, a 8,9 km en la avinguda de l'Hostal Nou",
         "parrafos": [
             "El registro de la Generalitat da como estación más próxima por carretera la de Olèrdola (B09), de Applus, en la avinguda de l'Hostal Nou: 8,9 km. El servicio oficial BMW que marca el localizador de bmw.es queda más lejos, en Vilanova i la Geltrú: Quadis Munich, avinguda d'Eduard Toldrà 69, a 23,5 km."
         ]},
        {"id": "c15-ap7-b23", "h2": "C-15, AP-7 y B-23: vía rápida casi todo el camino",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc sale por la C-15, sigue por la AP-7 y entra al Baix Llobregat por la B-23: 51,9 km por carretera, 30,7 en línea recta. Son vías rápidas casi todo el camino, lo que hace razonable bajar el coche y recogerlo en el día. Puigdàlber queda fuera del área metropolitana, de modo que la recogida del taller no cubre el pueblo.",
             "Para que el día cunda, conviene llamar antes con el modelo y el síntoma. La diagnosis y la reparación se presupuestan antes de autorizar nada.",
             "Un detalle para diésel: el recorrido por la AP-7 a velocidad constante es justo el que necesita el filtro de partículas para regenerarse, algo que los trayectos cortos entre pueblos del Penedès no consiguen."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Puigdàlber?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Olèrdola (B09), a 8,9 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 23,5 km según bmw.es."},
        {"q": "¿Recogéis el coche en Puigdàlber?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "621 habitantes (+15,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("081748")},
        {"etiqueta": "Superficie del término", "valor": "0,4 km²", **F.idescat("081748")},
        {"etiqueta": "Turismos (2024)", "valor": "337 · 543 por cada 1.000 hab.", **F.idescat("081748")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 8,9 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 51,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081748"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["rajadell"] = "BMW en Rajadell (Bages): ITV y servicio oficial en Sant Fruitós de Bages y taller especialista independiente en Sant Joan Despí, a 75,7 km por la C-55 y la C-16."
CIUDADES["rajadell"] = {
    "h1": "Rajadell, junto a la C-25: tu BMW entre Manresa y Sant Joan Despí",
    "entradilla": "Con la C-25 a menos de tres kilómetros, Rajadell tiene buena salida hacia todas partes. El servicio oficial BMW está en Sant Fruitós de Bages; la ITV, en Manresa o en Sant Fruitós, y el taller especialista de la red, a 75,7 km. Lo que te sirve para decidir dónde llevar el coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 75.7},
    "secciones": [
        {"id": "el-eje-al-lado", "h2": "El Eix Transversal a la puerta",
         "parrafos": [
             "La C-25, el Eix Transversal, pasa a menos de tres kilómetros del centro. Para un BMW diésel es una ventaja real: el filtro de partículas necesita de vez en cuando un tramo a régimen estable para quemar el hollín acumulado, y aquí no hace falta buscarlo.",
             "Si aun así el aviso del filtro aparece con frecuencia, el problema suele estar en otra parte —un sensor de presión diferencial, una válvula EGR sucia, un termostato que no deja calentar el motor— y merece diagnóstico antes de pensar en cambiar el filtro."
         ]},
        {"id": "sant-fruitos", "h2": "ITV a unos 18 km y servicio oficial a 22,4",
         "parrafos": [
             "En el registro de la Generalitat, dos estaciones de ITV quedan casi a la par por carretera: la de Manresa (B06), en el polígono Bufalvent, a 17,8 km, y la de Sant Fruitós (B25), en el polígono El Grau, a 18,1. En Sant Fruitós, en la carretera de Manresa a Berga km 34,5, está también Quadis Munich, el punto oficial BMW más cercano según bmw.es, a 22,4 km.",
             "Las llamadas a revisión que convoque la marca se atienden allí. Para mantenimiento y averías, la elección del taller es tuya."
         ]},
        {"id": "bajar-a-barcelona", "h2": "75,7 km por la C-55 y la C-16",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona toma la C-25, baja por la C-55 y la C-16 y termina en la B-20: 75,7 km por carretera, 50,2 en línea recta. No hay recogida desde el Bages; el servicio del taller no llega fuera del área metropolitana.",
             "Merece el viaje cuando el problema pide un especialista en BMW y no se ha resuelto en la comarca. En Dasercars nada se toca sin tu aprobación previa sobre un presupuesto escrito.",
             "Rajadell tenía 597 habitantes en 2025, frente a 524 en 2015, repartidos en un término de 45,53 km²."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Rajadell?",
         "a": "En Manresa (B06), polígono Bufalvent, a 17,8 km por carretera, o en Sant Fruitós (B25), polígono El Grau, a 18,1."},
        {"q": "¿Por qué se enciende tan a menudo el testigo del filtro de partículas?",
         "a": "Puede ser por trayectos demasiado cortos, pero también por un sensor, la EGR o el termostato. Conviene diagnosticarlo."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "75,7 km por la C-25, la C-55, la C-16 y la B-20 hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "597 habitantes (+13,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("081786")},
        {"etiqueta": "Superficie del término", "valor": "45,53 km²", **F.idescat("081786")},
        {"etiqueta": "ITV más cercana", "valor": "Manresa (B06) · 17,8 km; Sant Fruitós (B25) · 18,1", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 22,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 75,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081786"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["campins"] = "BMW en Campins (Vallès Oriental): ITV en Sant Celoni a 8,8 km, servicio oficial en Mataró y taller especialista independiente a 64,6 km por la AP-7."
CIUDADES["campins"] = {
    "h1": "Campins: ITV en Sant Celoni, concesionario BMW en Granollers o Mataró y taller a 64,6 km",
    "entradilla": "Con 586 vecinos y casi un 20 % más que hace diez años, Campins depende de Sant Celoni para la ITV y de Granollers o Mataró para el servicio oficial BMW. Nuestro taller queda en Sant Joan Despí. Estas son las distancias y lo que te conviene hacer en cada sitio.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 64.6},
    "secciones": [
        {"id": "itv-sant-celoni", "h2": "Sant Celoni: 4,1 km en recta, 8,8 por carretera",
         "parrafos": [
             "La estación de ITV más próxima según el registro de la Generalitat es la de Sant Celoni (B26), de TÜV SÜD, en la carretera de Gualba 41-43. En línea recta está a 4,1 km; por carretera, a 8,8. Para la inspección no tiene sentido ir a ningún otro sitio.",
             "Si el BMW ya pasa la ITV cada año, merece la pena revisar antes luces, testigos del cuadro y holguras: son comprobaciones rápidas que se pueden hacer antes de pedir cita."
         ]},
        {"id": "mataro-y-sant-joan", "h2": "Dos direcciones distintas: Mataró o el Baix Llobregat",
         "parrafos": [
             "En el localizador de bmw.es, Pruna Motor tiene dos puntos oficiales casi a la misma distancia: el del km 19 de la C-17 en Granollers, a 33,5 km, y el de la Via Sèrgia 2 de Mataró, a 34. Son la referencia para las llamadas a revisión de la marca y lo que cubre su garantía.",
             "Nuestro taller, Dasercars Barcelona, está a 64,6 km: BV-5114, AP-7, C-33 y B-20 hasta el carrer del Tambor del Bruc, 52,5 km en línea recta. Campins no forma parte del área metropolitana y la recogida del taller no llega. Para una revisión rutinaria es mucho camino; para una avería de BMW que nadie ha resuelto cerca, es otra cuenta."
         ]},
        {"id": "campins-crece", "h2": "Un pueblo pequeño que gana vecinos",
         "parrafos": [
             "El padrón pasó de 491 habitantes en 2015 a 586 en 2025, un 19,3 % más, en un término de 7,29 km². Idescat, con datos de la DGT, contaba 344 turismos en 2024: 587 por cada 1.000 habitantes.",
             "Ninguna carretera principal pasa a menos de tres kilómetros del centro, así que el coche hace sobre todo recorridos cortos hasta enlazar con la AP-7. En un diésel, eso pide atención al filtro de partículas; en cualquier BMW, a la batería, que con trayectos breves no llega a recargarse del todo."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Campins?",
         "a": "En la estación de Sant Celoni (B26), carretera de Gualba 41-43, a 8,8 km por carretera."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en Granollers (C-17), a 33,5 km, o en Mataró (Via Sèrgia 2), a 34, según bmw.es."},
        {"q": "¿Recogéis el coche en Campins?",
         "a": "No. La recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "586 habitantes (+19,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080399")},
        {"etiqueta": "Turismos (2024)", "valor": "344 · 587 por cada 1.000 hab.", **F.idescat("080399")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 8,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 33,5 km (Mataró · 34)", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 64,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080399"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["valverde-de-alcala"] = "BMW en Valverde de Alcalá: ITV y servicio oficial en Alcalá de Henares y taller especialista independiente en Alcobendas, a 43,9 km por la R-2 y la M-50."
CIUDADES["valverde-de-alcala"] = {
    "h1": "Valverde de Alcalá: 722 turismos por cada mil vecinos y el taller BMW a 43,9 km",
    "entradilla": "En Valverde de Alcalá hay más de dos turismos por cada tres habitantes, y todo lo relacionado con el coche está fuera del pueblo. Te contamos qué tienes en Alcalá de Henares y cómo se llega a nuestro taller de Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 43.9},
    "secciones": [
        {"id": "parque-valverde", "h2": "Un 28,1 % más de vecinos y casi el doble de coches por persona que Madrid",
         "parrafos": [
             "El padrón del INE da a Valverde de Alcalá 565 habitantes en 2025, frente a 441 en 2015. La Comunidad de Madrid, con datos de la DGT, contaba 408 turismos en 2025: 722 por cada 1.000 vecinos, casi el doble que en Madrid capital, donde la proporción es de 388.",
             "El término mide 13,7 km² y la M-204 es la única carretera principal a menos de tres kilómetros."
         ]},
        {"id": "alcala-concesionario-itv", "h2": "En Alcalá de Henares, el concesionario y la ITV",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 15,9 km por carretera. La estación de ITV oficial de referencia, también en Alcalá, es la de TÜV SÜD ATISAE (estación 2878), en la avenida Juan Carlos I, junto al centro comercial La Garena: unos 12 km contando hasta el centro de Alcalá, porque la ubicación disponible de esa estación es la del municipio.",
             "Tener el concesionario tan cerca no te ata a él para las revisiones. La normativa europea (Reglamento UE 461/2010) permite mantener el coche en un taller independiente sin perder la garantía, siempre que se siga el plan de BMW."
         ]},
        {"id": "r2-alcobendas", "h2": "M-300, M-100 y R-2 hasta la calle Valgrande",
         "parrafos": [
             "La ruta hasta Dasercars Madrid sale por la M-204, enlaza con la M-300 y la M-100, sigue por la R-2 y entra por la M-50: 43,9 km por carretera, 32,9 en línea recta. La recogida y entrega del taller se ciñe al área metropolitana de Madrid y está sujeta a disponibilidad; pregunta al reservar si tu dirección entra.",
             "A 802 metros de altitud, en invierno conviene vigilar la batería y el anticongelante."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Valverde de Alcalá?",
         "a": "La estación oficial de referencia es la de TÜV SÜD ATISAE (2878), en la avenida Juan Carlos I de Alcalá de Henares, a unos 12 km."},
        {"q": "¿Puedo revisar el coche fuera del concesionario sin perder la garantía?",
         "a": "Sí, si se respetan los intervalos y especificaciones del plan de mantenimiento de BMW."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "43,9 km por la M-300, la M-100, la R-2 y la M-50 hasta Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "565 habitantes (+28,1 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "408 · 722 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 802 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 15,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 43,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["orista"] = "BMW en Oristà (Lluçanès): ITV y servicio oficial en Vic y taller especialista independiente en Sant Joan Despí, a 94,5 km. Cuándo compensa el viaje."
CIUDADES["orista"] = {
    "h1": "Oristà: 68 km² de término, la C-670 al lado y el especialista BMW a 94,5 km",
    "entradilla": "El término de Oristà es amplio y está poco poblado: 8 habitantes por km². Aquí el coche hace muchos kilómetros por carretera secundaria. Esto es lo que tienes en Vic y lo que supone llevarlo a nuestro taller.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 94.5},
    "secciones": [
        {"id": "termino-extenso", "h2": "555 vecinos en 68,49 km²",
         "parrafos": [
             "Según Idescat, el término mide 68,49 km², y el padrón de 2025 da 555 habitantes, prácticamente los mismos que en 2015 (559). En 2024 había 359 turismos: 647 por cada 1.000 vecinos, más del doble que en Barcelona ciudad.",
             "Mucho kilómetro por carreteras de curvas desgasta antes frenos, neumáticos y silentblocks de suspensión que la autovía. Si notas que el coche se va hacia un lado al frenar o que la dirección ha perdido precisión, no lo dejes para la siguiente revisión."
         ]},
        {"id": "vic-para-todo", "h2": "Concesionario a 22,1 km y la ITV de Osona a 28,4",
         "parrafos": [
             "El punto oficial BMW más próximo en el localizador de bmw.es es Quadis Munich, calle Perot Rocaguinarda 1 de Vic, a 22,1 km del núcleo urbano. La ITV más cercana por carretera en el registro de la Generalitat también está en Vic: Osona (B04), en el carrer Sant Llorenç Desmunts 22, a 28,4 km.",
             "Si vas a Vic por una cosa, aprovecha para la otra. La ITV se hace allí; el viaje a Barcelona queda para lo que no tenga solución en la comarca."
         ]},
        {"id": "c670-c16", "h2": "94,5 km por la C-670, la C-25 y la C-16",
         "parrafos": [
             "La ruta desde el núcleo de Oristà hasta Sant Joan Despí sale por la C-670, que pasa a menos de tres kilómetros, sigue por la C-25 y baja por la C-16 y la B-20: 94,5 km por carretera, 63,1 en línea recta. La recogida del taller es solo para el área metropolitana y no llega aquí.",
             "Para que el viaje compense, conviene haberlo hablado antes: el modelo, el año y qué hace exactamente el coche bastan para orientar si es algo que merece bajar o se puede resolver cerca."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en el Lluçanès?",
         "a": "No. El taller de la red más próximo es Dasercars Barcelona, en Sant Joan Despí, a 94,5 km de Oristà."},
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Vic: la estación Osona (B04), a 28,4 km por carretera según la Generalitat."},
        {"q": "¿Qué se desgasta más por carreteras de curvas?",
         "a": "Frenos, neumáticos y los silentblocks de la suspensión y la dirección."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "555 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Lluçanès", **F.idescat("081516")},
        {"etiqueta": "Superficie del término", "valor": "68,49 km²", **F.idescat("081516")},
        {"etiqueta": "Turismos (2024)", "valor": "359 · 647 por cada 1.000 hab.", **F.idescat("081516")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 28,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 22,1 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081516"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["fogars-de-montclus"] = "BMW en Fogars de Montclús: ITV en Sant Celoni a 14,5 km, servicio oficial en Mataró y taller especialista independiente a 70,4 km, en Sant Joan Despí."
CIUDADES["fogars-de-montclus"] = {
    "h1": "Fogars de Montclús: la BV-5114, la ITV de Sant Celoni y el taller BMW a 70 km",
    "entradilla": "De Fogars de Montclús a cualquier servicio hay que salir por la BV-5114, y eso se nota en los kilómetros: la ITV de Sant Celoni está a 6,3 km en línea recta pero a 14,5 por carretera. Te contamos qué tienes cerca y qué supone llegar a nuestro taller.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 70.4},
    "secciones": [
        {"id": "carretera-de-curvas", "h2": "Más del doble por carretera que en línea recta",
         "parrafos": [
             "La relación entre las dos distancias lo resume: desde el núcleo urbano hasta la estación de ITV de Sant Celoni (B26), en la carretera de Gualba 41-43, hay 6,3 km en línea recta y 14,5 por carretera. La carretera da muchas vueltas, con curvas y desnivel.",
             "En ese tipo de carretera los frenos trabajan más, sobre todo bajando. El líquido de frenos absorbe humedad con el tiempo y pierde eficacia cuando se calienta, por eso el plan de BMW lo cambia por años y no por kilómetros. Los discos y las pastillas también se gastan antes que en llano."
         ]},
        {"id": "oficial-granollers-mataro", "h2": "El servicio oficial, en Granollers o Mataró",
         "parrafos": [
             "Según bmw.es, Pruna Motor tiene dos puntos oficiales casi a la misma distancia: el de la C-17 en Granollers, a 40,3 km, y el de la Via Sèrgia 2 de Mataró, a 41,1. Para una campaña del fabricante, es en uno de ellos; para mantenimiento y averías, el taller lo eliges tú."
         ]},
        {"id": "hasta-sant-joan-despi", "h2": "70,4 km por la AP-7 y la C-33",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona baja por la BV-5114, toma la AP-7 y después la C-33 y la B-20: 70,4 km por carretera, 52,5 en línea recta. Fogars queda fuera del área metropolitana, y la recogida del taller no llega.",
             "Con esa distancia, tiene sentido para un diagnóstico de especialista o una avería que no se ha resuelto cerca. En el taller se presupuesta todo por escrito antes de empezar, incluida la diagnosis."
         ]},
        {"id": "fogars-en-cifras", "h2": "494 vecinos en casi 40 km²",
         "parrafos": [
             "El padrón de 2025 da a Fogars de Montclús 494 habitantes, 17 más que en 2015, repartidos en 39,72 km². Idescat contaba 279 turismos en 2024, 565 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Fogars de Montclús?",
         "a": "En la estación de Sant Celoni (B26), carretera de Gualba 41-43, a 14,5 km por carretera."},
        {"q": "¿Cada cuánto se cambia el líquido de frenos de un BMW?",
         "a": "Por tiempo, según el plan de mantenimiento del coche, porque absorbe humedad aunque se hagan pocos kilómetros."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 70,4 km por la BV-5114, la AP-7, la C-33 y la B-20, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "494 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080811")},
        {"etiqueta": "Turismos (2024)", "valor": "279 · 565 por cada 1.000 hab.", **F.idescat("080811")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 14,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 40,3 km (Mataró · 41,1)", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 70,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080811"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["borreda"] = "BMW en Borredà (Berguedà), a 854 m: ITV en Berga a 22,9 km, servicio oficial en Vic y taller especialista independiente a 122,1 km. Cuándo no compensa el viaje."
CIUDADES["borreda"] = {
    "h1": "Borredà, a 122 km del taller: lo que conviene resolver en el Berguedà",
    "entradilla": "Seamos claros desde el principio: de Borredà a nuestro taller de Sant Joan Despí hay 122,1 km. Para casi todo lo que necesita un BMW o un MINI hay opciones más cerca, y te decimos cuáles. El viaje solo tiene sentido en casos concretos.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 122.1},
    "secciones": [
        {"id": "lo-que-hay-cerca", "h2": "La ITV en Berga y el concesionario en Vic",
         "parrafos": [
             "La estación de ITV más próxima por carretera en el registro de la Generalitat es la de Berga (B13), en el polígono industrial La Valldan, a 22,9 km. El servicio oficial BMW más cercano según bmw.es está más lejos, en la otra dirección: Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 56,8 km.",
             "Para el mantenimiento rutinario, un taller de confianza de la comarca es lo sensato. Lo importante es que use el aceite con la homologación BMW que pide tu motor."
         ]},
        {"id": "cuando-si-bajar", "h2": "Cuándo sí merece la pena hacer 122 km",
         "parrafos": [
             "Cuando hay una avería específica de la marca que no se ha resuelto cerca: un fallo electrónico que vuelve tras borrarlo, un problema del sistema de AdBlue, un diésel N47 o N57 con ruido de cadena, o un segundo diagnóstico antes de aceptar una reparación cara. La ruta va por la C-26, que pasa a menos de tres kilómetros del pueblo, y después por la C-16 y la B-20: 122,1 km por carretera, 85 en línea recta.",
             "Desde aquí no hay recogida, que solo cubre el área metropolitana. Antes de bajar, una llamada con modelo, año, kilometraje y bastidor permite tener la pieza pedida y no hacer el viaje dos veces."
         ]},
        {"id": "ochocientos-cincuenta-y-cuatro", "h2": "854 metros de altitud y un pueblo que pierde vecinos",
         "parrafos": [
             "Borredà está a 854 metros, según Idescat. En invierno, la batería es la pieza que antes falla en un coche que duerme fuera, y más en un BMW con arranque y parada automático; al sustituirla, se registra en la centralita. El anticongelante debe tener la concentración correcta, no solo el nivel.",
             "El municipio tenía 503 habitantes en 2015 y 433 en 2025, un 13,9 % menos, en un término de 43,45 km²."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en el Berguedà?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 122,1 km de Borredà."},
        {"q": "¿Dónde paso la ITV desde Borredà?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Berga (B13), a 22,9 km."},
        {"q": "¿Qué hay que hacer al cambiar la batería de un BMW?",
         "a": "Registrarla en la centralita, para que el sistema de carga se ajuste a la batería nueva."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "433 habitantes (−13,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080240")},
        {"etiqueta": "Altitud", "valor": "854 m", **F.idescat("080240")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 22,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 56,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 122,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080240"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["perafita"] = "BMW en Perafita (Lluçanès): servicio oficial en Vic e ITV en Ripoll, ambos a 28 km, y taller especialista independiente en Sant Joan Despí, a 111,2 km."
CIUDADES["perafita"] = {
    "h1": "Perafita: Vic y Ripoll a 28 km cada uno, el especialista BMW a 111",
    "entradilla": "Desde Perafita, el concesionario BMW y la ITV quedan a la misma distancia, 28 km, pero en direcciones opuestas: uno en Vic y la otra en Ripoll. Nuestro taller está mucho más lejos. Te explicamos cómo organizarte.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 111.2},
    "secciones": [
        {"id": "vic-o-ripoll", "h2": "Al sur, el concesionario; al norte, la ITV",
         "parrafos": [
             "El localizador de bmw.es da como punto oficial más próximo Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic: 28 km por carretera. La ITV más cercana por carretera en el registro de la Generalitat no está en Vic sino en Ripoll: la estación G08, en el passeig d'Ordina, también a 28 km.",
             "No se pueden juntar en un mismo viaje como en otros pueblos, así que conviene planificar. Una pre-ITV en tu taller habitual antes de subir a Ripoll evita volver por una bombilla o un aviso del cuadro."
         ]},
        {"id": "ciento-once-km", "h2": "111,2 km hasta Sant Joan Despí",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona sale por la BP-4653, enlaza con la C-62 y la C-25 y baja por la C-16 y la B-20: 111,2 km por carretera, 76,2 en línea recta. No hay ninguna carretera principal a menos de tres kilómetros del centro, y la recogida del taller, limitada al área metropolitana, no llega al Lluçanès.",
             "Con esa distancia, lo honesto es decirlo: para revisiones y reparaciones corrientes, mejor cerca. El viaje encaja con averías de BMW que no han tenido solución en la comarca, y siempre con una llamada previa en la que expliques qué le pasa al coche."
         ]},
        {"id": "perafita-754", "h2": "433 vecinos a 754 metros",
         "parrafos": [
             "Perafita tenía 433 habitantes en el padrón de 2025, 14 más que en 2015, en un término de 19,59 km². Está a 754 metros de altitud según Idescat, suficiente para que las mañanas de invierno pongan a prueba una batería que ya no está al cien por cien.",
             "Si el coche tarda en arrancar en frío o el sistema de arranque y parada deja de actuar, suele ser la batería avisando. En un BMW, la nueva se registra en la centralita al montarla."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Perafita?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Ripoll (G08), en el passeig d'Ordina, a 28 km."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 28 km según bmw.es."},
        {"q": "¿Por qué el arranque y parada deja de funcionar en invierno?",
         "a": "Normalmente porque la batería no tiene carga suficiente; el sistema se desactiva para proteger el arranque."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "433 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Lluçanès", **F.idescat("081607")},
        {"etiqueta": "Altitud", "valor": "754 m", **F.idescat("081607")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 28 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 28 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 111,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081607"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["olmeda-de-las-fuentes"] = "BMW en Olmeda de las Fuentes: ITV y servicio oficial en Alcalá de Henares y taller especialista independiente en Alcobendas, a 54,5 km. Ruta y datos."
CIUDADES["olmeda-de-las-fuentes"] = {
    "h1": "Olmeda de las Fuentes: seis carreteras hasta el taller BMW de Alcobendas",
    "entradilla": "Entre Olmeda de las Fuentes y nuestro taller hay 54,5 km y seis carreteras distintas. Lo oficial, concesionario e ITV, está en Alcalá de Henares. Te damos los datos para decidir qué hacer cerca y qué no.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 54.5},
    "secciones": [
        {"id": "seis-carreteras", "h2": "M-219, M-204, M-300, M-100, R-2 y M-50",
         "parrafos": [
             "Desde el centro del núcleo urbano, la ruta hasta la calle Valgrande de Alcobendas encadena la M-219, la M-204, la M-300 y la M-100, sigue por la R-2 y entra por la M-50: 54,5 km por carretera, 40,9 en línea recta. La M-204 pasa a menos de tres kilómetros del pueblo.",
             "El servicio de recogida no llega tan lejos: queda fuera de su zona, que es el área metropolitana. Lo útil es contar por teléfono qué síntoma tiene el coche antes de hacer el viaje, para que no se quede en una visita de ida y vuelta."
         ]},
        {"id": "alcala", "h2": "Inspección y campañas de la marca: las dos cosas, hacia Alcalá",
         "parrafos": [
             "Si te llega una carta de BMW por una llamada a revisión, la cita es con la red oficial; la más próxima según bmw.es es AutoPremier (Vía Complutense 131), a 26,5 km. Para el resto de trabajos, el taller lo eliges tú.",
             "Para la inspección técnica, el listado de la Comunidad de Madrid da como referencia la estación 2878 de TÜV SÜD ATISAE, en el entorno de La Garena. Cuenta con algo más de 20 km: la cifra que manejamos, 22,7, llega al centro de Alcalá y no a la puerta de la estación."
         ]},
        {"id": "olmeda-837", "h2": "Un pueblo a 837 metros que ha ganado un 26,9 % de vecinos",
         "parrafos": [
             "Olmeda de las Fuentes tenía 338 habitantes en 2015 y 429 en 2025, según el INE. En 2025 había 305 turismos censados (Comunidad de Madrid a partir de la DGT): 711 por cada 1.000 vecinos.",
             "A 837 metros de altitud, el invierno exige más de lo que parece. Revisa antes del frío la batería, la concentración del anticongelante y el estado de los neumáticos; en un diésel, también los calentadores, que en las mañanas de helada marcan la diferencia en el arranque."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Olmeda de las Fuentes?",
         "a": "La estación de referencia en el listado de la Comunidad de Madrid es la 2878, en Alcalá de Henares, a algo más de 20 km."},
        {"q": "¿Qué revisar en el coche antes del invierno?",
         "a": "Batería, anticongelante, neumáticos y, en los diésel, los calentadores."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "54,5 km por carretera hasta la calle Valgrande 17 de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "429 habitantes (+26,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "305 · 711 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 837 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 26,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 54,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
# Gargantilla tiene 1 impresión en 90 días: no se toca la metaDescription.
CIUDADES["gargantilla-del-lozoya-y-pinilla-de-buitrago"] = {
    "h1": "Gargantilla del Lozoya y Pinilla de Buitrago: un BMW a 1.054 metros",
    "entradilla": "El centro urbano está a unos 1.054 metros de altitud. Para un BMW o un MINI eso pesa más que la distancia al taller, que son 68 km hasta Alcobendas. Te contamos ambas cosas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 68.0},
    "secciones": [
        {"id": "mil-cincuenta-y-cuatro", "h2": "Por encima de los mil metros: el invierno manda",
         "parrafos": [
             "A esta altitud hay heladas buena parte del invierno. El primer aviso suele darlo la batería: un BMW con muchos consumidores y arranque y parada automático la exige más que un coche sencillo, y al sustituirla hay que registrarla en la centralita. Le siguen el anticongelante, que se comprueba con densímetro y no a ojo, y los neumáticos, que con frío y calzada húmeda pierden agarre antes de lo que parece.",
             "En las bajadas hacia el valle, los frenos se calientan más que en llano. Un líquido de frenos con años pierde punto de ebullición; por eso el plan de mantenimiento lo cambia por tiempo."
         ]},
        {"id": "itv-a1", "h2": "La ITV, a 16,1 km en la A-1",
         "parrafos": [
             "La estación oficial más próxima por carretera es la de TÜV SÜD ATISAE (estación 2812), en la A-1, km 66, en el término de Lozoyuela, a 16,1 km según el listado de la Comunidad de Madrid. Desde el pueblo se llega por la M-604, que pasa a menos de tres kilómetros del centro."
         ]},
        {"id": "taller-u-oficial", "h2": "Concesionario a 65,9 km, taller especialista a 68",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es BYmyCAR Madrid, en la calle Tejera 2, en la carretera de Algete, a 65,9 km. Nuestro taller, Dasercars Madrid, queda prácticamente a la misma distancia: 68 km por la M-634, la M-604 y la A-1 hasta la calle Valgrande de Alcobendas, 47,7 en línea recta.",
             "Con las dos opciones igual de lejos, la decisión no va de kilómetros. Las campañas de la marca, en el concesionario; el mantenimiento y las averías, donde prefieras. La recogida del taller está pensada para el área metropolitana de Madrid y no llega a la Sierra Norte."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Gargantilla del Lozoya?",
         "a": "En la estación de la A-1, km 66 (Lozoyuela), a 16,1 km por carretera."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "68 km por la M-634, la M-604 y la A-1 hasta Alcobendas."},
        {"q": "¿Qué conviene revisar antes del invierno?",
         "a": "Batería, anticongelante, neumáticos y líquido de frenos: a más de mil metros, son lo que antes falla."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "396 habitantes (+12,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "239 · 604 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 1.054 m", **F.copernicus},
        {"etiqueta": "ITV más cercana", "valor": "A-1 km 66 (Lozoyuela) · 16,1 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid (Algete) · 65,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 68 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ─────────────────────────────────────────────────────────────────────────────
META["oris"] = "BMW en Orís (Osona): ITV en Ripoll a 17,4 km, servicio oficial en Vic a 21,6 km y taller especialista independiente a 97,2 km por la C-17."
CIUDADES["oris"] = {
    "h1": "Orís: la C-17 de punta a punta hasta el taller BMW, a 97,2 km",
    "entradilla": "La ruta desde Orís hasta nuestro taller es sencilla: la C-17 baja casi en línea hasta el área de Barcelona. Aun así son 97,2 km. Esto es lo que tienes más cerca y cuándo compensa el trayecto.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 97.2},
    "secciones": [
        {"id": "una-sola-carretera", "h2": "C-17, C-33 y B-20: tres tramos y ningún desvío",
         "parrafos": [
             "La C-17 pasa a menos de tres kilómetros del centro de Orís. Desde ahí, la ruta hasta el carrer del Tambor del Bruc solo cambia a la C-33 y a la B-20: 97,2 km por carretera, 79,8 en línea recta. La poca diferencia entre las dos cifras dice que el camino es directo.",
             "Ese recorrido largo a ritmo constante es, además, el que mejor le va a un diésel con filtro de partículas, que en trayectos cortos no llega a regenerar. La recogida del taller no cubre Osona: solo funciona dentro del área metropolitana."
         ]},
        {"id": "ripoll-y-vic", "h2": "ITV hacia el norte, concesionario hacia el sur",
         "parrafos": [
             "La ITV más próxima por carretera en el registro de la Generalitat es la de Ripoll (G08), en el passeig d'Ordina, a 17,4 km. El servicio oficial BMW queda en la dirección contraria: Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 21,6 km según bmw.es.",
             "Las campañas que convoque BMW se hacen en ese concesionario. Para el mantenimiento y las averías fuera de garantía, la elección es tuya."
         ]},
        {"id": "cuando-compensa", "h2": "Cuándo merece la pena bajar casi cien kilómetros",
         "parrafos": [
             "Para una revisión sencilla, no: lo razonable es un taller de la comarca. Compensa con averías propias de la marca que no se han resuelto cerca —un fallo eléctrico intermitente, un aviso de AdBlue, una cadena de distribución ruidosa— o para un segundo diagnóstico antes de una reparación importante. Antes, una llamada con modelo, año y kilometraje.",
             "Orís tenía 355 habitantes en 2025, un 15,3 % más que en 2015, en un término de 27,17 km². Idescat contaba 222 turismos en 2024: 625 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Orís?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Ripoll (G08), a 17,4 km."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 21,6 km según bmw.es."},
        {"q": "¿Tenéis taller en Osona?",
         "a": "No. El taller de la red más cercano está en Sant Joan Despí, a 97,2 km de Orís por la C-17."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "355 habitantes (+15,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081509")},
        {"etiqueta": "Turismos (2024)", "valor": "222 · 625 por cada 1.000 hab.", **F.idescat("081509")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 17,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 21,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 97,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081509"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
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
