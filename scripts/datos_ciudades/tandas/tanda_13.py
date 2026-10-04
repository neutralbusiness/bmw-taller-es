# Tanda 13: Veciana, Castellar de n'Hug, Santa Maria de Besora, la Nou de Berguedà,
# Castellfollit de Riubregós, Castellar del Riu, Santa Maria de Miralles,
# Sant Agustí de Lluçanès, Capolat, Sobremunt, Granera, la Quar, Fígols, Gisclareny
# y Sant Jaume de Frontanyà.
# Ninguna ciudad de la tanda está en la lista de exclusiones del coordinador: todas
# son municipios con taller con dirección (Dasercars Barcelona, Sant Joan Despí).
#
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_13
# y las metaDescription y metaTitle nuevos (las 15 ciudades tienen 0 impresiones en
# paso_gsc.json) con
#   python3 scripts/datos_ciudades/tandas/tanda_13.py
#
# Criterio META: todas las descripciones antiguas prometían algo que la guía prohíbe
# (recogida a domicilio o «subimos a recoger tu BMW», «diagnóstico oficial»,
# «recambios garantizados», «mantenimiento con garantía», superlativos de tamaño sin
# dato, «especialistas en condiciones extremas», protecciones inventadas): se
# reescriben las 15.
# Criterio TITLES: se cambian los 13 que decían «Taller BMW en X» (presencia física
# falsa) con coletillas prohibidas o sin dato: «Expertos en Alta Montaña», «Donde el
# servicio sube a buscarte» y «El taller que llega a las masías» (recogida), «El más
# cercano», «El más pequeño de Osona merece el mejor taller» (superlativo y comarca
# equivocada: Sobremunt es del Lluçanès según Idescat), «Servicio en tu valle» y
# «Servicio al pie del Cadí» (presencia), «Meseta ventosa», «Frontera con Ripollès»,
# «Remoto y fiable», «Servicio para Zonas Remotas», «Donde la minería…».
# Se conservan santa-maria-de-miralles y granera, que ya decían «cerca de» y la
# comarca correcta.
#
# Datos con proporción de turismos > 800 por 1.000 hab. (Castellfollit de Riubregós,
# Santa Maria de Miralles, Granera, la Quar, Fígols): solo cifra absoluta.
import json
import re
import sys
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI.parent / "piloto"))
sys.path.insert(0, str(_AQUI.parent))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

# ---------------------------------------------------------------- Veciana
CIUDADES["veciana"] = {
    "h1": "Veciana (Anoia): ITV en Igualada, servicio oficial BMW en Tàrrega y taller a 70,7 km",
    "entradilla": "Con 168 vecinos repartidos en casi 39 km², en Veciana el coche hace falta para todo. Hacia el este queda la ITV de Igualada; hacia el oeste, el servicio oficial BMW de Tàrrega; y el taller especialista de la red, en Sant Joan Despí, a 70,7 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 70.7},
    "secciones": [
        {"id": "dos-direcciones", "h2": "Igualada para la inspección, Tàrrega para la marca",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Igualada (B12), de Applus, en el carrer Països Baixos del polígono Les Comes, a 19,9 km. Igualada, capital de l'Anoia, es la dirección natural desde Veciana.",
             "El servicio oficial BMW que da el localizador de bmw.es está en sentido contrario: Unicars Ponent, en el carrer de la Conca de Barberà de Tàrrega, a 37,9 km. Es la referencia si BMW convoca una campaña de revisión para tu modelo o si la avería entra en la garantía del fabricante.",
         ]},
        {"id": "a2-hasta-el-taller", "h2": "Por la BV-1005 y la C-1412a hasta la A-2",
         "parrafos": [
             "Hasta la nave de Dasercars Barcelona, en el carrer del Tambor del Bruc de Sant Joan Despí, la ruta enlaza la BV-1005 y la C-1412a con la A-2: 70,7 km por carretera, 57,9 en línea recta.",
             "Compensa para una avería de BMW que no se ha cerrado en la comarca, para un segundo diagnóstico antes de aceptar una reparación grande o para llevar el mantenimiento con el plan de la marca. No compensa para un neumático o unas escobillas: eso lo resuelve cualquier taller de Igualada.",
         ]},
        {"id": "cuatro-por-km2", "h2": "Cuatro habitantes por kilómetro cuadrado",
         "parrafos": [
             "El padrón de 2025 da a Veciana 168 habitantes, frente a 175 en 2015. Idescat, con datos de la DGT, contaba 110 turismos en 2024: 655 por cada 1.000 vecinos. Con una densidad de 4 habitantes por km², no hay trayectos cortos; la BV-1001 y la C-1412a pasan a menos de tres kilómetros del núcleo.",
             "Ese uso, carretera secundaria con tramos rápidos, le va bien a un diésel: el filtro de partículas se regenera sin problemas. Lo que más acusa los años es la suspensión delantera, con brazos y silentblocks que se resienten de baches y cunetas.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV me queda más cerca desde Veciana?",
         "a": "ITV Igualada (B12), en el polígono Les Comes, a 19,9 km por carretera según el registro de la Generalitat."},
        {"q": "¿Dónde está el servicio oficial BMW más próximo?",
         "a": "En Tàrrega: Unicars Ponent, a 37,9 km, según el localizador de bmw.es."},
        {"q": "¿Llega hasta Veciana la recogida del coche?",
         "a": "No: solo cubre el área metropolitana de Barcelona, y sujeta a disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "168 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("082975")},
        {"etiqueta": "Turismos (2024)", "valor": "110 · 655 por cada 1.000 hab.", **F.idescat("082975")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 19,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent (Tàrrega) · 37,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 70,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082975"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Castellar de n'Hug
CIUDADES["castellar-de-n-hug"] = {
    "h1": "Castellar de n'Hug, a 1.395 metros: tu BMW, la ITV de Ripoll y el taller a 140,5 km",
    "entradilla": "El núcleo de Castellar de n'Hug está a 1.395 metros, y eso condiciona el coche más que cualquier otra cosa. Para la inspección y para la marca, lo más cercano mira al Ripollès y a la Garrotxa; el taller especialista de la red queda a 140,5 km, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 140.5},
    "secciones": [
        {"id": "invierno-de-montana", "h2": "Lo que exige el invierno a esta altura",
         "parrafos": [
             "Aquí las heladas no son la excepción. Con mucho frío, el gasóleo puede enturbiarse y tapar el filtro de combustible, sobre todo si el depósito lleva semanas con gasóleo repostado en verano. Los BMW diésel con sistema SCR llevan además un depósito de AdBlue, que se congela a temperaturas bajo cero; el coche lo calienta, pero un aviso de ese sistema no se debe dejar pasar.",
             "La otra pieza crítica es la batería. Si el coche duerme en la calle, una batería envejecida suele fallar la primera mañana de helada fuerte. Cuando se cambia, un BMW necesita registrar la nueva en la centralita para que la cargue como corresponde.",
         ]},
        {"id": "ripoll-y-olot", "h2": "ITV en Ripoll y taller autorizado BMW en Olot",
         "parrafos": [
             "La estación más próxima por carretera según la Generalitat es ITV Ripoll (G08), en el passeig d'Ordina, a 25,8 km del núcleo urbano. Para la marca, el punto más cercano del localizador de bmw.es es Oliva Motor Girona en Olot, taller autorizado BMW en la Ronda Les Mates 32, a 59,2 km.",
         ]},
        {"id": "b402-c16", "h2": "140,5 km hasta Sant Joan Despí por la B-402 y la C-16",
         "parrafos": [
             "La ruta más corta sale por la BV-4031, baja por la B-402 hasta la C-16 y termina en la B-20: 140,5 km por carretera para 101,9 en línea recta. Es demasiado viaje para una revisión corriente.",
             "Puede compensar para una avería concreta de BMW que nadie ha resuelto cerca: un fallo eléctrico intermitente, un problema del sistema de AdBlue o una cadena de distribución ruidosa en un diésel N47. El municipio, con 166 vecinos en 2025, queda lejos del área metropolitana y la recogida del taller no llega.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué conviene revisar antes del invierno?",
         "a": "Batería, concentración del anticongelante, neumáticos y, en los diésel con AdBlue, que el sistema no tenga ningún aviso pendiente."},
        {"q": "¿Dónde paso la ITV desde Castellar de n'Hug?",
         "a": "En Ripoll (G08), a 25,8 km por carretera, según el registro de la Generalitat."},
        {"q": "¿Cuál es el punto oficial BMW más cercano?",
         "a": "Oliva Motor Girona, taller autorizado en Olot, a 59,2 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "166 habitantes (+4,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080522")},
        {"etiqueta": "Altitud", "valor": "1.395 m", **F.idescat("080522")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 25,8 km", **F.itv_cat},
        {"etiqueta": "Taller autorizado BMW", "valor": "Oliva Motor Girona (Olot) · 59,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 140,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080522"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Santa Maria de Besora
CIUDADES["santa-maria-de-besora"] = {
    "h1": "Santa Maria de Besora: un BMW entre Ripoll y Vic, a 106 km del taller especialista",
    "entradilla": "Desde Santa Maria de Besora, la ITV más próxima está en Ripoll, a 20,9 km, y el servicio oficial BMW en Vic, a 30,5. El taller especialista de la red queda bastante más lejos, a 106 km por la C-17. Así se reparte cada cosa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 106.0},
    "secciones": [
        {"id": "norte-y-sur", "h2": "La inspección hacia el norte, la marca hacia el sur",
         "parrafos": [
             "En línea recta, ITV Ripoll (G08), en el passeig d'Ordina, está a 10,2 km; por carretera son 20,9, y es la estación más próxima en el registro de la Generalitat. Vic, la capital de Osona, queda al otro lado: allí está Quadis Munich, en la calle Perot Rocaguinarda 1, el punto de servicio oficial que da el localizador de bmw.es, a 30,5 km.",
             "Conviene organizar las salidas: la inspección hacia el Ripollès; el concesionario, en un viaje a Vic.",
         ]},
        {"id": "eje-c17", "h2": "106 kilómetros por la C-17 y la C-33",
         "parrafos": [
             "Hasta el carrer del Tambor del Bruc, en Sant Joan Despí, la ruta sale por la BV-5227, baja por la C-17, sigue por la C-33 y entra por la B-20: 106 km por carretera, 86,2 en línea recta.",
             "Con esa distancia, bajar el coche tiene sentido para un problema que pida conocimiento específico de BMW: un testigo que vuelve tras borrarlo, una avería eléctrica que nadie localiza, un diésel B47 o N47 con ruido en la distribución. Santa Maria de Besora no está en el área metropolitana de Barcelona, así que la recogida del taller no llega.",
         ]},
        {"id": "866-metros", "h2": "A 866 metros: neumáticos antes que nada",
         "parrafos": [
             "El núcleo está a 866 metros de altitud. En invierno, lo que más se olvida son los neumáticos: con el dibujo al límite y la goma endurecida por los años, en una mañana de escarcha agarran mucho menos. Si no quieres cambiar a neumáticos de invierno, los de todo tiempo con el símbolo de la montaña y el copo son una opción razonable.",
             "El padrón de 2025 da 164 habitantes (158 en 2015) e Idescat, a partir de la DGT, 121 turismos en 2024: 738 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV queda más cerca de Santa Maria de Besora?",
         "a": "La de Ripoll (G08), en el passeig d'Ordina, a 20,9 km por carretera."},
        {"q": "¿Dónde está el concesionario BMW más próximo?",
         "a": "En Vic: Quadis Munich, calle Perot Rocaguinarda 1, a 30,5 km según bmw.es."},
        {"q": "¿Valen los neumáticos de todo tiempo para el invierno aquí?",
         "a": "Los que llevan el símbolo de la montaña con el copo de nieve están homologados para condiciones invernales; con heladas puntuales son una opción sensata."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "164 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082536")},
        {"etiqueta": "Turismos (2024)", "valor": "121 · 738 por cada 1.000 hab.", **F.idescat("082536")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 20,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 30,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 106 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082536"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- la Nou de Berguedà
CIUDADES["la-nou-de-bergueda"] = {
    "h1": "La Nou de Berguedà: tu BMW junto a la C-16, con la ITV de Berga a 19,2 km",
    "entradilla": "La Nou de Berguedà tiene una ventaja que muchos pueblos de montaña no tienen: la C-16 pasa a unos dos kilómetros. Por ella se llega a la ITV de Berga, al servicio oficial de Sant Fruitós de Bages y, más abajo, al taller especialista de Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 118.5},
    "secciones": [
        {"id": "c16-cerca", "h2": "La C-16, a 2,1 km del núcleo",
         "parrafos": [
             "Según OpenStreetMap, el trazado de la C-16 pasa a 2,1 km del núcleo urbano. Si el testigo del filtro de partículas de tu diésel se enciende a menudo, suele ser porque el coche nunca llega a la temperatura y al régimen que necesita para quemar el hollín: subidas cortas, motor frío, contacto apagado a mitad de proceso.",
             "Con una vía rápida tan cerca, la solución está a mano: incluir de vez en cuando un tramo largo de C-16 en tus salidas, sin parar el motor a mitad de una regeneración.",
         ]},
        {"id": "berga-y-sant-fruitos", "h2": "ITV en Berga, servicio oficial en Sant Fruitós de Bages",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Berga (B13), en el polígono La Valldan, a 19,2 km. Siguiendo la misma carretera hacia el sur está el punto de servicio oficial que da el localizador de bmw.es: Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 57,3 km.",
         ]},
        {"id": "una-sola-carretera", "h2": "118,5 km hasta el taller por una sola carretera principal",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona: la BV-4022 hasta la C-16, la C-16 hacia el sur y la B-20. En total, 118,5 km por carretera y 90,2 en línea recta.",
             "Esa distancia no compensa para un cambio de aceite. Sí para un diagnóstico que no se ha cerrado en la comarca o para un trabajo en el que importa conocer la marca: la electrónica de un BMW reciente, el sistema de AdBlue de un diésel o una distribución que hace ruido.",
         ]},
        {"id": "nou-en-cifras", "h2": "163 vecinos a 876 metros",
         "parrafos": [
             "El padrón de 2025 da 163 habitantes, frente a 153 en 2015, e Idescat contaba 109 turismos en 2024: 669 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es la ITV más próxima a la Nou de Berguedà?",
         "a": "Berga (B13), en el polígono La Valldan, a 19,2 km por carretera."},
        {"q": "¿Por qué se enciende tanto el testigo del filtro de partículas?",
         "a": "Casi siempre por trayectos cortos que no completan la regeneración. Si tras un tramo largo de carretera sigue, hay que revisarlo."},
        {"q": "¿A cuántos kilómetros está vuestro taller?",
         "a": "A 118,5 km por carretera, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "163 habitantes (+6,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("081424")},
        {"etiqueta": "Altitud", "valor": "876 m", **F.idescat("081424")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 19,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 57,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 118,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081424"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Castellfollit de Riubregós
CIUDADES["castellfollit-de-riubregos"] = {
    "h1": "Castellfollit de Riubregós: ITV a 38 km, servicio oficial a 43 y especialista BMW a 89",
    "entradilla": "Desde Castellfollit de Riubregós, cualquier cosa que tenga que ver con el coche está lejos. Por eso esta página no va de cercanía, sino de cómo agrupar viajes: la ITV en Igualada, el servicio oficial BMW en Tàrrega y el taller especialista de la red en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 88.9},
    "secciones": [
        {"id": "igualada-y-tarrega", "h2": "Igualada y Tàrrega, a una distancia parecida",
         "parrafos": [
             "La estación más próxima por carretera del registro de la Generalitat es ITV Igualada (B12), en el polígono Les Comes, a 38,2 km. El punto de servicio oficial BMW más cercano según bmw.es es Unicars Ponent, en Tàrrega, a 42,9 km. Igualada queda hacia Barcelona; Tàrrega, hacia Lleida.",
             "Con esas distancias, lo práctico es hacer coincidir la ITV con otra gestión en Igualada y reservar Tàrrega para lo que solo puede hacer la red oficial, como las campañas de revisión que convoque BMW.",
         ]},
        {"id": "c1412a", "h2": "La C-1412a, a menos de un kilómetro del centro",
         "parrafos": [
             "El trazado de la C-1412a pasa a 0,8 km del centro, según OpenStreetMap, y es también la primera parte de la ruta hasta el taller: C-1412a y A-2, 88,9 km por carretera y 68,6 en línea recta hasta el carrer del Tambor del Bruc.",
             "Si vas a hacer ese viaje, que sea por algo que lo justifique: un diagnóstico que no se ha resuelto en la zona, una avería de la caja automática o del sistema eléctrico, o el mantenimiento de un BMW que quieres llevar con su plan de marca. La diagnosis se presupuesta antes de conectar el equipo, así que sabes de antemano a qué te comprometes.",
         ]},
        {"id": "catorce-menos", "h2": "153 vecinos, catorce menos que en 2015",
         "parrafos": [
             "El padrón de 2025 da a Castellfollit de Riubregós 153 habitantes, frente a 167 en 2015: un 8,4 % menos. Idescat registraba 127 turismos en 2024, en un término de 26,21 km² con el núcleo a 467 metros.",
             "Si tu coche pasa días parado, lo que más sufre es la batería, que se descarga sin llegar a recuperarse, y los discos de freno, que con la humedad se cubren de óxido. Un trayecto largo de vez en cuando les sienta bien a los dos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Castellfollit de Riubregós?",
         "a": "En Igualada (B12), a 38,2 km por carretera, según la Generalitat."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Unicars Ponent, en Tàrrega, a 42,9 km según el localizador de bmw.es."},
        {"q": "¿Se cobra la diagnosis?",
         "a": "Sí: es un trabajo técnico y se presupuesta antes de empezar, como el resto de la reparación."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "153 habitantes (−8,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("080608")},
        {"etiqueta": "Turismos (2024)", "valor": "127", **F.idescat("080608")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 38,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent (Tàrrega) · 42,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 88,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080608"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Castellar del Riu
CIUDADES["castellar-del-riu"] = {
    "h1": "Castellar del Riu: Berga a 5,9 km en línea recta y a 13,1 por carretera; el taller BMW, a 114,4",
    "entradilla": "Berga queda muy cerca en el mapa, pero por carretera la ITV está a 13,1 km. Esa diferencia dice mucho de cómo se conduce aquí y de lo que pide a un BMW o un MINI. El taller especialista de la red está en Sant Joan Despí, a 114,4 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 114.4},
    "secciones": [
        {"id": "curvas-y-desgaste", "h2": "Más del doble de kilómetros que en línea recta",
         "parrafos": [
             "ITV Berga (B13), en el polígono La Valldan, está a 5,9 km en línea recta y a 13,1 por carretera: es la estación más próxima en el registro de la Generalitat. Cuando el recorrido dobla la línea recta, lo que hay en medio son curvas, pendiente y frenadas.",
             "En ese tipo de carretera, pastillas y discos delanteros se gastan antes que en llano, y los neumáticos se comen por los hombros en las curvas cerradas. Mirar el desgaste en cada cambio de aceite ahorra sorpresas.",
         ]},
        {"id": "hacia-el-sur", "h2": "El servicio oficial y el taller especialista, por la C-16",
         "parrafos": [
             "Siguiendo hacia el sur, el punto oficial BMW más próximo según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5 (Sant Fruitós de Bages), a 53,2 km. Dasercars Barcelona queda bastante más lejos: 114,4 km por la BV-4243, la C-16 y la B-20, y 87,6 en línea recta.",
             "Con esa diferencia, el viaje a Sant Joan Despí se reserva para lo que pide un especialista independiente en BMW: averías que no se han resuelto en la comarca o un diésel con problemas en el sistema de gases, para el que el taller cuenta con homologación REDISTA. El mantenimiento rutinario se hace mejor cerca.",
         ]},
        {"id": "riu-en-cifras", "h2": "151 vecinos a 920 metros",
         "parrafos": [
             "El núcleo está a 920 metros de altitud, en un término de 32,74 km². El padrón de 2025 da 151 habitantes, frente a 175 en 2015, e Idescat, con datos de la DGT, 114 turismos en 2024: 755 por cada 1.000 vecinos.",
             "A esa altura, una batería débil da la cara con el primer frío serio. En los BMW, la batería de recambio se registra en el coche para que el sistema de carga sepa qué capacidad y qué tecnología tiene.",
         ]},
    ],
    "faq": [
        {"q": "¿Por qué se gastan antes las pastillas de freno aquí?",
         "a": "Por las bajadas y las curvas: los frenos trabajan mucho más que en llano. Conviene revisarlas en cada mantenimiento."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Berga (B13), a 13,1 km por carretera desde Castellar del Riu."},
        {"q": "¿Tenéis taller en el Berguedà?",
         "a": "No. El de la red está en Sant Joan Despí, a 114,4 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "151 habitantes (−13,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080500")},
        {"etiqueta": "Altitud", "valor": "920 m", **F.idescat("080500")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 13,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 53,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 114,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080500"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Santa Maria de Miralles
CIUDADES["santa-maria-de-miralles"] = {
    "h1": "Santa Maria de Miralles: servicio oficial BMW a 52,5 km y especialista independiente a 66,3",
    "entradilla": "Para un BMW de Santa Maria de Miralles, el servicio oficial más próximo y el taller especialista de la red quedan a una distancia parecida: 52,5 y 66,3 km. La elección, por tanto, no va de kilómetros, sino de qué necesita el coche.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 66.3},
    "secciones": [
        {"id": "elegir-por-el-trabajo", "h2": "Dos opciones a distancia parecida: elige por el trabajo",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más cercano es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages. Allí van las campañas que convoque BMW y las reparaciones cubiertas por la garantía del fabricante.",
             "Para el mantenimiento y las reparaciones fuera de garantía, el Reglamento (UE) 461/2010 permite usar un taller independiente sin perder la garantía, con la condición de respetar intervalos y especificaciones. Dasercars Barcelona trabaja BMW y MINI, tiene especialidad en los diésel N47, N57, B47 y B57 y homologación REDISTA para escape y gases.",
         ]},
        {"id": "c37-a2", "h2": "Por la C-37 hasta la A-2",
         "parrafos": [
             "La C-37 pasa a medio kilómetro del núcleo urbano, y por ella empieza la ruta: C-37 y A-2 hasta el carrer del Tambor del Bruc, 66,3 km por carretera y 47,4 en línea recta. El municipio no forma parte del área metropolitana de Barcelona, de modo que la recogida del taller no llega y el coche lo traes tú.",
         ]},
        {"id": "itv-igualada-miralles", "h2": "La ITV, en Igualada",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Igualada (B12), de Applus, en el polígono Les Comes, a 15,7 km. En línea recta son 12, así que el rodeo es corto.",
             "Santa Maria de Miralles tenía 144 habitantes en 2025, catorce más que en 2015, y 118 turismos en 2024 según Idescat. El núcleo está a 543 metros, en un término de 25,04 km². Un coche que hace a diario la C-37, con curvas y repechos, agradece que se revisen a tiempo los amortiguadores: cuando pierden eficacia, el coche cabecea en las frenadas y la frenada se alarga.",
         ]},
    ],
    "faq": [
        {"q": "¿Pierdo la garantía si no voy al servicio oficial?",
         "a": "No, siempre que el mantenimiento siga los intervalos y las especificaciones del plan de BMW."},
        {"q": "¿Qué ITV me toca desde Santa Maria de Miralles?",
         "a": "La más próxima por carretera es la de Igualada (B12), a 15,7 km."},
        {"q": "¿Por dónde se va al taller?",
         "a": "Por la C-37 y la A-2: 66,3 km hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "144 habitantes (+10,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("082573")},
        {"etiqueta": "Turismos (2024)", "valor": "118", **F.idescat("082573")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 15,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 52,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 66,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082573"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sant Agustí de Lluçanès
CIUDADES["sant-agusti-de-llucanes"] = {
    "h1": "Sant Agustí de Lluçanès: 106 vecinos, ITV en Ripoll y taller BMW especialista a 107,7 km",
    "entradilla": "En diez años, Sant Agustí de Lluçanès ha pasado de 90 a 106 habitantes. Si tienes aquí un BMW o un MINI, lo útil es saber dónde queda la inspección, dónde la red oficial y qué supone bajar al taller especialista de Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 107.7},
    "secciones": [
        {"id": "crecer-desde-poco", "h2": "Un 17,8 % más de vecinos desde 2015",
         "parrafos": [
             "Según el padrón, el municipio tenía 90 habitantes en 2015 y 106 en 2025. Idescat, a partir de la DGT, contaba 68 turismos en 2024: 642 por cada 1.000 vecinos, en un término de 13,26 km² con el núcleo a 816 metros.",
             "A esa altitud, antes del invierno merecen atención dos detalles que se suelen olvidar: las escobillas y el líquido lavaparabrisas con anticongelante, que en una mañana de escarcha marcan la diferencia, y la carga de la batería si el coche hace pocos kilómetros.",
         ]},
        {"id": "ripoll-21", "h2": "La ITV de Ripoll, a 21,5 km",
         "parrafos": [
             "La estación más cercana por carretera en el registro de la Generalitat es ITV Ripoll (G08), en el passeig d'Ordina: 21,5 km, aunque en línea recta son 13,7. El servicio oficial BMW más próximo según bmw.es está en Vic: Quadis Munich, en la calle Perot Rocaguinarda 1, a 32,2 km.",
         ]},
        {"id": "bp4654-c17", "h2": "Hasta Sant Joan Despí por la BP-4654 y la C-17",
         "parrafos": [
             "La ruta al taller de la red sale por la BP-4654, toma la C-17, sigue por la C-33 y termina por la B-20: 107,7 km por carretera, 80 en línea recta.",
             "Para ese trayecto, mejor ir con el trabajo claro. Llama con el modelo, el año, los kilómetros y lo que notas, y pide que te digan si conviene bajar o resolverlo cerca. En Dasercars el presupuesto se da por escrito y nada se toca sin tu visto bueno.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "En Vic: Quadis Munich, a 32,2 km según bmw.es."},
        {"q": "¿Qué ITV queda más cerca de Sant Agustí de Lluçanès?",
         "a": "La de Ripoll (G08), a 21,5 km por carretera."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No. La recogida del taller solo cubre el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "106 habitantes (+17,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081957")},
        {"etiqueta": "Turismos (2024)", "valor": "68 · 642 por cada 1.000 hab.", **F.idescat("081957")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 21,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 32,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 107,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081957"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Capolat
CIUDADES["capolat"] = {
    "h1": "Capolat, a 1.279 metros: BMW en la montaña del Berguedà, a 117,9 km del especialista",
    "entradilla": "Capolat tiene 93 vecinos y su núcleo está a 1.279 metros. Hacia el sur, la ruta empieza bajando por la BV-4241 hasta la C-26; desde ahí, Berga para la ITV y, mucho más lejos, el taller especialista de la red.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 117.9},
    "secciones": [
        {"id": "subir-y-bajar", "h2": "Subir y bajar a diario: refrigeración y frenos",
         "parrafos": [
             "La ruta hacia el taller empieza por la BV-4241, que enlaza con la C-26; el trazado de esta pasa a 2,5 km del núcleo, según OpenStreetMap. Un desnivel así, repetido a diario, se nota en el coche.",
             "Subiendo, sobre todo en verano, trabaja la refrigeración: vigila el nivel del refrigerante y no ignores un aviso de temperatura. Bajando, trabajan los frenos; con una marcha corta y el freno motor, discos y pastillas sufren menos. En un BMW con caja automática, el modo manual sirve para lo mismo.",
         ]},
        {"id": "berga-capital", "h2": "Berga, la capital comarcal, para la ITV",
         "parrafos": [
             "La estación más próxima por carretera según la Generalitat es ITV Berga (B13), en el polígono La Valldan: 13,6 km por carretera, 6,4 en línea recta. El servicio oficial BMW más cercano en el localizador de bmw.es está en Sant Fruitós de Bages: Quadis Munich, a 56,8 km.",
         ]},
        {"id": "hasta-sant-joan-despi", "h2": "117,9 km hasta Sant Joan Despí",
         "parrafos": [
             "Por la BV-4241, la C-26, la C-16 y la B-20 hay 117,9 km hasta la nave de Dasercars Barcelona, 83,3 en línea recta. Solo compensa para algo que necesite un especialista en BMW: un fallo electrónico sin diagnosticar, un aviso del sistema de emisiones o un diésel que ha perdido potencia sin causa clara. Para lo demás, un taller de Berga.",
             "El padrón da 93 habitantes en 2025 (92 en 2015), e Idescat 61 turismos en 2024: 656 por cada 1.000 vecinos, en un término de 34,13 km².",
         ]},
    ],
    "faq": [
        {"q": "¿Cómo freno mejor en las bajadas largas?",
         "a": "Con una marcha corta para aprovechar el freno motor y con frenadas cortas y firmes, en lugar de llevar el pedal pisado todo el descenso."},
        {"q": "¿Dónde paso la ITV desde Capolat?",
         "a": "En Berga (B13), a 13,6 km por carretera."},
        {"q": "¿Cuál es el servicio oficial BMW más próximo?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 56,8 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "93 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080459")},
        {"etiqueta": "Altitud", "valor": "1.279 m", **F.idescat("080459")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 13,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 56,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 117,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080459"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sobremunt
CIUDADES["sobremunt"] = {
    "h1": "Sobremunt (Lluçanès): ITV y servicio oficial BMW en Vic, el especialista a 100,4 km",
    "entradilla": "Desde Sobremunt, Vic lo resuelve casi todo: allí están la estación de ITV más próxima y el servicio oficial BMW, a 24,2 y 24,8 km. El taller especialista de la red queda a 100,4 km, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 100.4},
    "secciones": [
        {"id": "todo-en-vic", "h2": "Inspección y concesionario en la misma ciudad",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22 de Vic. El localizador de bmw.es da como punto oficial más cercano Quadis Munich, en la calle Perot Rocaguinarda 1, también en Vic. Con poco más de medio kilómetro de diferencia entre una ruta y otra, se pueden juntar en la misma salida.",
             "Si el coche ya pasa la ITV cada año, una revisión previa de luces, frenos y neumáticos evita volver a Vic una segunda vez.",
         ]},
        {"id": "bv4608", "h2": "Por la BV-4608 y la C-17: 100,4 km",
         "parrafos": [
             "La ruta hasta el carrer del Tambor del Bruc sale por la BV-4608, baja por la C-17 y la C-33 y entra por la B-20: 100,4 km por carretera y 74,9 en línea recta. Sobremunt no está en el área metropolitana, así que la recogida del taller queda fuera de alcance.",
             "Compensa cuando el problema es de BMW y no de cualquier coche: una caja automática que da tirones, un aviso de AdBlue que no se va, una electrónica que falla sin patrón. Para eso, el taller trabaja con presupuesto previo, también de la diagnosis.",
         ]},
        {"id": "sobremunt-cifras", "h2": "90 vecinos a 881 metros",
         "parrafos": [
             "El padrón da a Sobremunt 90 habitantes en 2025, frente a 82 en 2015. Idescat contaba 57 turismos en 2024, 633 por cada 1.000 vecinos, en un término de 13,8 km².",
             "A 881 metros hay heladas. El líquido refrigerante protege del frío solo si la mezcla es correcta, y eso se mide con un densímetro o un refractómetro, no mirando el nivel del vaso de expansión.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está la ITV más próxima a Sobremunt?",
         "a": "En Vic: ITV Osona (B04), a 24,2 km por carretera."},
        {"q": "¿Y el servicio oficial BMW?",
         "a": "También en Vic: Quadis Munich, a 24,8 km según bmw.es."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI comparte motores y electrónica con BMW y se diagnostica con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "90 habitantes (+9,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Lluçanès", **F.idescat("082711")},
        {"etiqueta": "Turismos (2024)", "valor": "57 · 633 por cada 1.000 hab.", **F.idescat("082711")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 24,2 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 24,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 100,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082711"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Granera
CIUDADES["granera"] = {
    "h1": "Granera (Moianès): taller autorizado BMW en Castellar del Vallès y especialista a 68,6 km",
    "entradilla": "Granera está a 40,2 km en línea recta de nuestro taller de Sant Joan Despí, pero por carretera son 68,6. Esa diferencia resume el sitio: relieve, curvas y pocos atajos. Lo que tienes más cerca de la marca es un taller autorizado en Castellar del Vallès.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 68.6},
    "secciones": [
        {"id": "tallcar-castellar", "h2": "Tallcar, el punto oficial más próximo",
         "parrafos": [
             "Según el localizador de bmw.es, el punto de servicio oficial más cercano a Granera es Tallcar, en Castellar del Vallès (calle Suiza 6): un taller autorizado de la marca a 25,2 km por carretera. Para una reparación cubierta por la garantía del fabricante, es la referencia.",
             "Un taller independiente puede encargarse del mantenimiento sin que pierdas la garantía de BMW mientras se cumpla el plan del fabricante, con sus intervalos y especificaciones.",
         ]},
        {"id": "seis-carreteras", "h2": "Seis carreteras hasta Sant Joan Despí",
         "parrafos": [
             "La ruta más corta que calcula OpenStreetMap enlaza la BV-1245, la C-59, la BV-1341, la C-1413b, la C-33 y la B-20. Son 68,6 km por carretera para 40,2 en línea recta: un rodeo de casi treinta kilómetros que imponen el relieve y el trazado.",
             "Granera queda fuera del área metropolitana de Barcelona y la recogida del taller no llega. Si bajas, que sea por algo que merezca el viaje; una llamada previa con modelo, año y síntoma lo aclara.",
         ]},
        {"id": "itv-viladecavalls", "h2": "La ITV, en el polígono Can Trias de Viladecavalls",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Viladecavalls (B03), en el polígono Can Trias, a 40,1 km; en línea recta, 19,9.",
             "Granera tiene 84 vecinos según el padrón de 2025 (80 en 2015) y 78 turismos censados en 2024 según Idescat, en un término de 23,73 km². El núcleo está a 782 metros: con heladas, las juntas de las puertas y el freno de estacionamiento pueden quedarse pegados si el coche duerme mojado al raso; dejarlo con una marcha engranada, o en P en un automático, evita forzar el freno.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el taller autorizado BMW más cercano a Granera?",
         "a": "Tallcar, en la calle Suiza 6 de Castellar del Vallès, a 25,2 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es la de Viladecavalls (B03), a 40,1 km."},
        {"q": "¿Por qué hay tanta diferencia entre carretera y línea recta?",
         "a": "Porque las carreteras de la zona rodean el relieve: 68,6 km hasta el taller frente a 40,2 en línea recta."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "84 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Moianès", **F.idescat("080958")},
        {"etiqueta": "Altitud", "valor": "782 m", **F.idescat("080958")},
        {"etiqueta": "ITV más cercana", "valor": "Viladecavalls (B03) · 40,1 km", **F.itv_cat},
        {"etiqueta": "Taller autorizado BMW", "valor": "Tallcar (Castellar del Vallès) · 25,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 68,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080958"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- la Quar
CIUDADES["la-quar"] = {
    "h1": "La Quar: 41 vecinos en 38 km² y el taller especialista BMW a 109,1 km",
    "entradilla": "En la Quar viven 41 personas repartidas en 38,25 km², a un habitante por kilómetro cuadrado. Para el coche eso significa distancias, carreteras de montaña y pocas alternativas cerca. Esto es lo que tienes a mano y lo que queda lejos.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 109.1},
    "secciones": [
        {"id": "un-habitante-por-km2", "h2": "Un habitante por kilómetro cuadrado",
         "parrafos": [
             "El padrón de 2025 da a la Quar 41 habitantes, frente a 52 en 2015. Idescat registraba 47 turismos en 2024; en un municipio tan pequeño, la proporción por vecino dice poco.",
             "Si el coche circula a menudo por caminos sin asfaltar, lo que más se resiente en un BMW es lo que va por debajo: protectores de cárter, silentblocks y rótulas de suspensión, y los neumáticos de perfil bajo, que se dañan con piedras y baches. Con el núcleo a 885 metros, el invierno añade el frío a la lista.",
         ]},
        {"id": "berga-o-vic", "h2": "ITV en Berga, servicio oficial en Vic",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Berga (B13), en el polígono La Valldan, a 21,9 km del núcleo urbano. El punto oficial BMW más cercano según bmw.es, en cambio, está en Vic: Quadis Munich, en la calle Perot Rocaguinarda 1, a 40,1 km.",
         ]},
        {"id": "c62-c16", "h2": "Hasta Sant Joan Despí por la C-62 y la C-16",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona sale por la BV-4346, enlaza con la C-62 y baja por la C-16 hasta la B-20: 109,1 km por carretera, 79,8 en línea recta. La Quar queda muy lejos del área metropolitana y la recogida del taller no llega.",
             "Si te planteas el viaje, que sea por algo que lo pida: un aviso del sistema de emisiones que vuelve, una avería eléctrica que no se ha localizado o un mantenimiento por plan de marca que quede registrado en el historial del coche. Para todo lo demás, Berga está más cerca.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué reviso si circulo por caminos de tierra?",
         "a": "Protectores de los bajos, suspensión (rótulas y silentblocks) y neumáticos. Un golpe en el cárter que no se ve a simple vista puede acabar en una fuga de aceite."},
        {"q": "¿Dónde paso la ITV desde la Quar?",
         "a": "En Berga (B13), a 21,9 km por carretera."},
        {"q": "¿Cuántos kilómetros hay hasta vuestro taller?",
         "a": "109,1 km por carretera, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "41 habitantes (52 en 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("081770")},
        {"etiqueta": "Superficie del término", "valor": "38,25 km²", **F.idescat("081770")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 21,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 40,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 109,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081770"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Fígols
CIUDADES["figols"] = {
    "h1": "Fígols, a 1.154 metros: ITV en Berga y taller especialista BMW a 119 km por la C-16",
    "entradilla": "Fígols tiene 40 vecinos y su núcleo está a 1.154 metros, a dos kilómetros de la C-16. Si tienes aquí un BMW o un MINI, lo que importa es cómo le afecta la altitud, dónde está lo más cercano y cuándo merece la pena bajar al taller especialista de Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 119.0},
    "secciones": [
        {"id": "bv4025", "h2": "De 1.154 metros a la C-16 por la BV-4025",
         "parrafos": [
             "La ruta hacia el sur empieza por la BV-4025, que baja desde el núcleo hasta la C-16; el trazado de esta pasa a 2 km del pueblo, según OpenStreetMap.",
             "En un descenso así, el que trabaja es el líquido de frenos. Con los años se carga de agua, su punto de ebullición baja y, si se sobrecalienta, el pedal se hunde más de lo normal. BMW marca su cambio por fecha y no por kilómetros: en un coche que anda poco, es fácil que se pase sin que nadie lo note.",
         ]},
        {"id": "diesel-en-altura", "h2": "Diésel y frío por encima de mil metros",
         "parrafos": [
             "A esta altitud el invierno es largo. En un diésel, conviene que los calentadores estén bien: si uno falla, el motor arranca peor en frío y humea más los primeros metros.",
             "Si el coche lleva AdBlue, el sistema tiene su propio calentador. Un aviso relacionado con él no es para dejarlo pasar, porque la cuenta atrás termina impidiendo arrancar el motor.",
         ]},
        {"id": "berga-y-sant-fruitos-figols", "h2": "Lo más cercano: Berga y Sant Fruitós de Bages",
         "parrafos": [
             "Según el registro de la Generalitat, la estación de ITV más próxima por carretera es ITV Berga (B13), en el polígono La Valldan, a 19,7 km. El servicio oficial BMW más próximo en el localizador de bmw.es es Quadis Munich, en Sant Fruitós de Bages, a 57,8 km.",
             "El taller de la red, Dasercars Barcelona, queda a 119 km por la BV-4025, la C-16 y la B-20 (92,7 en línea recta). El municipio tiene 40 habitantes según el padrón de 2025, tres menos que en 2015, en un término de 29,31 km².",
         ]},
    ],
    "faq": [
        {"q": "¿Cada cuánto se cambia el líquido de frenos?",
         "a": "Cuando lo marque el plan de mantenimiento; en BMW va por tiempo y el indicador de servicio lo avisa."},
        {"q": "¿Dónde está la ITV más cercana a Fígols?",
         "a": "En Berga (B13), a 19,7 km por carretera."},
        {"q": "¿Sirve el taller para un MINI?",
         "a": "Sí. MINI comparte motores y electrónica con BMW, y se trabaja con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "40 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080804")},
        {"etiqueta": "Altitud", "valor": "1.154 m", **F.idescat("080804")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 19,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 57,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 119 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080804"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Gisclareny
CIUDADES["gisclareny"] = {
    "h1": "Gisclareny: 28 vecinos a 1.340 metros y el taller especialista BMW a 134,6 km",
    "entradilla": "Gisclareny tenía 28 habitantes en 2025 y 19 turismos censados en 2024. Desde aquí, la ITV queda a 35,4 km y el taller especialista de la red, a 134,6. Te contamos qué hacer con esas distancias.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 134.6},
    "secciones": [
        {"id": "b400", "h2": "A 1.340 metros, con la B-400 como carretera más próxima",
         "parrafos": [
             "La carretera con referencia más cercana es la B-400, a 2 km del núcleo urbano según OpenStreetMap. El núcleo está a 1.340 metros, en un término de 36,47 km², así que el coche hace casi siempre kilómetros de montaña.",
             "Neumáticos con buen dibujo y unas cadenas o fundas textiles en el maletero durante el invierno son lo primero que conviene tener a punto. Y si el coche pasa días parado con heladas, al arrancar deja que el motor gire suave antes de exigirle: el aceite frío tarda en llegar a todas partes, y el turbo lo nota.",
         ]},
        {"id": "berga-35", "h2": "ITV a 35,4 km, servicio oficial a 73,5",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Berga (B13), en el polígono La Valldan: 35,4 km por carretera, aunque en línea recta son 18,2. El punto oficial BMW más cercano según bmw.es es Quadis Munich, en Sant Fruitós de Bages, a 73,5 km.",
             "Con esas distancias, conviene que el viaje a la ITV no se convierta en dos. Una revisión previa de luces, frenos, neumáticos y holguras de la dirección, hecha con tiempo, evita tener que volver.",
         ]},
        {"id": "solo-con-motivo", "h2": "134,6 km hasta el taller: solo con motivo",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona, en Sant Joan Despí, suma 134,6 km por carretera, buena parte por la C-16, y 100,9 en línea recta.",
             "Es mucho para una revisión. Tiene sentido si el BMW arrastra una avería que no se ha resuelto en la comarca. En Dasercars nada se empieza sin un presupuesto por escrito que hayas aprobado, de modo que sabes qué se va a hacer antes de dejar el coche.",
         ]},
    ],
    "faq": [
        {"q": "¿Necesito cadenas en invierno?",
         "a": "Si el coche no lleva neumáticos de invierno o de todo tiempo con el símbolo de la montaña y el copo, conviene llevarlas cuando hay previsión de nieve."},
        {"q": "¿Dónde paso la ITV desde Gisclareny?",
         "a": "En Berga (B13), a 35,4 km por carretera."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Sant Fruitós de Bages, a 73,5 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "28 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080930")},
        {"etiqueta": "Altitud", "valor": "1.340 m", **F.idescat("080930")},
        {"etiqueta": "Turismos (2024)", "valor": "19", **F.idescat("080930")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 35,4 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 134,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080930"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sant Jaume de Frontanyà
CIUDADES["sant-jaume-de-frontanya"] = {
    "h1": "Sant Jaume de Frontanyà: 25 vecinos, ITV en Berga a 32 km y el especialista BMW a 131,2",
    "entradilla": "Sant Jaume de Frontanyà tenía 25 habitantes en 2025 y 15 turismos en 2024. Para quien tiene aquí un BMW o un MINI, la cuestión no es qué taller está cerca, porque ninguno lo está, sino qué se resuelve en Berga y qué justifica un viaje largo.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 131.2},
    "secciones": [
        {"id": "bv4656-c26", "h2": "Por la BV-4656 hasta la C-26",
         "parrafos": [
             "La ruta hacia el sur toma la BV-4656 hasta la C-26, y de ahí la C-16 y la B-20: 131,2 km por carretera hasta Sant Joan Despí, 91,9 en línea recta.",
             "La primera parte es carretera de montaña. A 1.072 metros, con heladas en invierno, la batería es lo primero que falla en un coche que pasa días parado. Un mantenedor de carga, si el coche duerme en un garaje con enchufe, alarga mucho su vida.",
         ]},
        {"id": "berga-y-vic", "h2": "Berga para la ITV, Vic para la marca",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Berga (B13), en el polígono La Valldan, a 32 km. El servicio oficial BMW más cercano según el localizador de bmw.es está hacia el otro lado, en Vic: Quadis Munich, en la calle Perot Rocaguinarda 1, a 66 km por carretera.",
         ]},
        {"id": "cuando-merece", "h2": "Cuándo merecen la pena 131 kilómetros",
         "parrafos": [
             "Para un cambio de aceite o de pastillas, no. Para un diagnóstico que nadie ha cerrado, una avería de un diésel N57 o B57, o un trabajo de escape y gases que pida la homologación REDISTA, sí puede merecerla. Una llamada previa con modelo, año y kilometraje te dice si conviene el viaje.",
             "Sant Jaume de Frontanyà pasó de 26 vecinos en 2015 a 25 en 2025, en un término de 21,26 km². No forma parte del área metropolitana de Barcelona, así que la recogida del taller no llega.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es la ITV más próxima a Sant Jaume de Frontanyà?",
         "a": "Berga (B13), a 32 km por carretera, según la Generalitat."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "En Vic: Quadis Munich, a 66 km según bmw.es."},
        {"q": "¿Cómo cuido la batería si el coche pasa días parado?",
         "a": "Con un mantenedor de carga si tienes enchufe, o con un trayecto de carretera de vez en cuando. Si hay que cambiarla, en un BMW la nueva se registra en la centralita."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "25 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("082166")},
        {"etiqueta": "Altitud", "valor": "1.072 m", **F.idescat("082166")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 32 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 66 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 131,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082166"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}


# ================================================================ metaDescription
# Las 15 tienen 0 impresiones en paso_gsc.json y su descripción prometía algo prohibido.
META = {
    "veciana": "BMW en Veciana (Anoia): ITV en Igualada a 19,9 km, servicio oficial en Tàrrega y el taller especialista de la red en Sant Joan Despí, a 70,7 km por la A-2.",
    "castellar-de-n-hug": "Castellar de n'Hug, a 1.395 m: qué revisar en tu BMW antes del invierno, ITV en Ripoll a 25,8 km y taller especialista de la red a 140,5 km.",
    "santa-maria-de-besora": "BMW en Santa Maria de Besora (Osona): ITV en Ripoll a 20,9 km, servicio oficial en Vic a 30,5 km y taller especialista independiente a 106 km.",
    "la-nou-de-bergueda": "BMW en la Nou de Berguedà: ITV en Berga a 19,2 km, servicio oficial en Sant Fruitós de Bages y taller especialista de la red a 118,5 km por la C-16.",
    "castellfollit-de-riubregos": "BMW en Castellfollit de Riubregós (Anoia): ITV en Igualada, servicio oficial en Tàrrega y taller especialista de la red a 88,9 km por la A-2.",
    "castellar-del-riu": "BMW en Castellar del Riu (Berguedà): ITV en Berga a 13,1 km, servicio oficial en Sant Fruitós de Bages y taller especialista independiente a 114,4 km.",
    "santa-maria-de-miralles": "BMW en Santa Maria de Miralles (Anoia): ITV en Igualada a 15,7 km, servicio oficial a 52,5 km y taller especialista independiente a 66,3 km por la A-2.",
    "sant-agusti-de-llucanes": "BMW en Sant Agustí de Lluçanès (Osona): ITV en Ripoll a 21,5 km, servicio oficial en Vic y taller especialista de la red a 107,7 km en Sant Joan Despí.",
    "capolat": "Capolat, a 1.279 m: frenos y refrigeración de tu BMW en la montaña, ITV en Berga a 13,6 km y taller especialista de la red a 117,9 km.",
    "sobremunt": "BMW en Sobremunt (Lluçanès): ITV y servicio oficial en Vic, a unos 24 km, y taller especialista independiente en Sant Joan Despí, a 100,4 km.",
    "granera": "BMW en Granera (Moianès): taller autorizado en Castellar del Vallès a 25,2 km, ITV en Viladecavalls y taller especialista de la red a 68,6 km.",
    "la-quar": "BMW en la Quar (Berguedà): ITV en Berga a 21,9 km, servicio oficial en Vic a 40,1 km y taller especialista independiente a 109,1 km por la C-16.",
    "figols": "Fígols, a 1.154 m: frenos y diésel de tu BMW en invierno, ITV en Berga a 19,7 km y taller especialista de la red a 119 km por la C-16.",
    "gisclareny": "BMW en Gisclareny (Berguedà), a 1.340 m: ITV en Berga a 35,4 km, servicio oficial a 73,5 km y taller especialista independiente a 134,6 km.",
    "sant-jaume-de-frontanya": "BMW en Sant Jaume de Frontanyà (Berguedà): ITV en Berga a 32 km, servicio oficial en Vic y taller especialista de la red a 131,2 km. Cuándo compensa.",
}

# ================================================================ metaTitle
# Solo ciudades sin impresiones (las 15). Se conservan santa-maria-de-miralles y granera.
TITLES = {
    "veciana": "Taller BMW para Veciana (Anoia) | Especialista independiente",
    "castellar-de-n-hug": "Taller BMW para Castellar de n'Hug (Berguedà) | Especialista",
    "santa-maria-de-besora": "Taller BMW para Santa Maria de Besora (Osona) | Especialista",
    "la-nou-de-bergueda": "Taller BMW para la Nou de Berguedà | Especialista independiente",
    "castellfollit-de-riubregos": "Taller BMW para Castellfollit de Riubregós (Anoia)",
    "castellar-del-riu": "Taller BMW para Castellar del Riu (Berguedà) | Especialista BMW",
    "sant-agusti-de-llucanes": "Taller BMW para Sant Agustí de Lluçanès (Osona) | Especialista",
    "capolat": "Taller BMW para Capolat (Berguedà) | Especialista independiente",
    "sobremunt": "Taller BMW para Sobremunt (Lluçanès) | Especialista independiente",
    "la-quar": "Taller BMW para la Quar (Berguedà) | Especialista independiente",
    "figols": "Taller BMW para Fígols (Berguedà) | Especialista BMW y MINI",
    "gisclareny": "Taller BMW para Gisclareny (Berguedà) | Especialista BMW y MINI",
    "sant-jaume-de-frontanya": "Taller BMW para Sant Jaume de Frontanyà (Berguedà)",
}

PROHIBIDO_TITLE = re.compile(
    r"(?-i:\bISTA\b)|Rheingold|oficial|%|presupuesto cerrado|recogida|domicilio|minutos?\b|\bmin\b|"
    r"coraz[oó]n|alta monta|garant[ií]a|rendimiento|profesionales de",
    re.I,
)


def aplicar_meta():
    from comun import CIUDADES_DIR
    gsc = {}
    cache = _AQUI.parent / "cache" / "paso_gsc.json"
    if cache.exists():
        gsc = json.loads(cache.read_text("utf-8"))
    for slug in set(META) | set(TITLES):
        assert slug in CIUDADES, slug
        g = gsc.get(slug) or {}
        assert not (g.get("imp_90d") or g.get("imp_mes")), (slug, "tiene impresiones: no se toca")
    for slug, desc in META.items():
        assert len(desc) <= 160, (slug, len(desc))
    for slug, t in TITLES.items():
        assert len(t) <= 65, (slug, len(t), t)
        assert not PROHIBIDO_TITLE.search(t), (slug, t)
    for slug in set(META) | set(TITLES):
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        if slug in META and cj.get("metaDescription") != META[slug]:
            cj["metaDescription"] = META[slug]
            print("metaDescription", slug)
        if slug in TITLES and cj.get("metaTitle") != TITLES[slug]:
            cj["metaTitle"] = TITLES[slug]
            print("metaTitle", slug)
        f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")


if __name__ == "__main__":
    aplicar_meta()
