# Tanda 3: Caldes de Montbui, Cubelles, Montornès del Vallès, Cunit, Vallirana,
# Corbera de Llobregat, Torelló, La Llagosta, Sant Sadurní d'Anoia, Argentona,
# Montgat, Pallejà, La Roca del Vallès, Llinars del Vallès.
# (ejea-de-los-caballeros está en la tanda pero se salta: zona de Zaragoza sin
# dirección de taller, pendiente de decisión de Martin.)
#
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_3
# y las metaDescription nuevas (solo ciudades sin impresiones en GSC cuya
# descripción prometía «hasta un 50 %», «diagnóstico oficial», ISTA…) con
#   python3 scripts/datos_ciudades/tandas/tanda_3.py
import json
import sys
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI.parent / "piloto"))
sys.path.insert(0, str(_AQUI.parent))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

CIUDADES["caldes-de-montbui"] = {
    "h1": "Caldes de Montbui: taller BMW a 40,6 km por la C-59 y la C-33",
    "entradilla": "Desde Caldes, la C-59 pasa a medio kilómetro del centro y es la salida natural hacia cualquier taller. El especialista BMW de la red está en Sant Joan Despí; el servicio autorizado más próximo, en Castellar del Vallès.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 40.6},
    "secciones": [
        {"id": "c59-ap7", "h2": "La C-59 como punto de partida",
         "parrafos": [
             "La ruta que calcula OpenStreetMap desde el centro de Caldes de Montbui hasta Dasercars Barcelona, en el carrer del Tambor del Bruc de Sant Joan Despí, encadena la C-59, la C-33 y la B-20: 40,6 km de carretera para 30,9 km en línea recta.",
             "Caldes no forma parte del Área Metropolitana de Barcelona, y el servicio de recogida del taller no llega hasta aquí: el coche lo traes tú. Lo razonable es reservar el viaje para trabajos que piden conocer la marca —una distribución ruidosa en un diésel N47, una avería eléctrica que nadie ha localizado, poner al día el mantenimiento según el plan de BMW— y resolver cerca lo genérico.",
         ]},
        {"id": "tallcar-castellar", "h2": "Un taller autorizado BMW a 11,5 km, en Castellar",
         "parrafos": [
             "Si lo que necesitas es la red de la marca, la referencia es Tallcar, en la calle Suiza 6 de Castellar del Vallès. El buscador de bmw.es lo identifica como punto solo de taller, sin exposición de venta, a 11,5 km de Caldes por carretera.",
             "Llevar el mantenimiento a un taller independiente no anula la garantía del fabricante: el Reglamento (UE) 461/2010 lo permite mientras se cumplan los intervalos y las especificaciones del plan de BMW. Para lo que dependa directamente de la marca, Tallcar es lo que te pilla más cerca.",
         ]},
        {"id": "itv-les-minetes", "h2": "Pasar la ITV: Santa Perpètua de Mogoda, en Les Minetes",
         "parrafos": [
             "Los datos abiertos de la Generalitat dan como estación más próxima por carretera la ITV CIM Vallès (B20), que gestiona TÜV Rheinland en el polígono Les Minetes, dentro del Centre Integral de Mercaderies de Santa Perpètua de Mogoda. Son 13,6 km desde el centro de Caldes, 10,8 en línea recta.",
         ]},
        {"id": "caldes-en-cifras", "h2": "18.567 vecinos y 9.746 turismos",
         "parrafos": [
             "El padrón de 2025 da a Caldes de Montbui 18.567 habitantes, un 8,6 % más que los 17.098 de 2015, en un término de 37,45 km² a 203 metros de altitud. Idescat, a partir de los datos de la DGT, contaba 9.746 turismos en 2024: 525 por cada 1.000 habitantes.",
             "El diésel que solo hace recados por el pueblo apenas llega a calentar lo suficiente para que el filtro de partículas se regenere. Si el tuyo avisa de filtro saturado, una salida larga a ritmo constante por la C-59 suele bastar; si el aviso vuelve, toca diagnosticar.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el taller BMW que atiende Caldes de Montbui?",
         "a": "En Sant Joan Despí: Dasercars Barcelona, carrer del Tambor del Bruc 3, a 40,6 km por la C-59, la C-33 y la B-20."},
        {"q": "¿Hay algún taller autorizado BMW cerca?",
         "a": "Tallcar, en la calle Suiza 6 de Castellar del Vallès, a 11,5 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima en el registro de la Generalitat es la ITV CIM Vallès (B20), en Santa Perpètua de Mogoda, a 13,6 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "18.567 habitantes (+8,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080333")},
        {"etiqueta": "Turismos (2024)", "valor": "9.746 · 525 por cada 1.000 hab.", **F.idescat("080333")},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20), Santa Perpètua de Mogoda · 13,6 km", **F.itv_cat},
        {"etiqueta": "Taller autorizado BMW", "valor": "Tallcar, Castellar del Vallès · 11,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 40,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080333"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["cubelles"] = {
    "h1": "BMW en Cubelles: a medio kilómetro del mar y a 43,7 km del taller especialista",
    "entradilla": "En Cubelles el mar queda a medio kilómetro del centro urbano, y eso pesa en el cuidado de un coche más que la distancia al taller. Lo que tienes a mano está en Vilanova i la Geltrú; el especialista BMW de la red, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 43.7},
    "secciones": [
        {"id": "humedad-salina", "h2": "Lo que el aire del mar le hace a un BMW aparcado en la calle",
         "parrafos": [
             "Un coche que duerme a pocos cientos de metros de la orilla vive todo el año en un ambiente húmedo y cargado de sal. Los primeros en notarlo suelen ser los discos de freno, que tras unos días sin moverse amanecen con una capa de óxido; después, los soportes y abrazaderas del escape, y las tomas de masa y conectores que quedan bajo el coche o en el vano motor.",
             "No hace falta obsesionarse. Basta con enjuagar los bajos de vez en cuando, mover el coche si pasa semanas parado y, ante un fallo eléctrico que aparece y desaparece, empezar por los conectores antes de cambiar ninguna pieza.",
         ]},
        {"id": "vilanova-al-lado", "h2": "Servicio oficial e ITV, los dos en Vilanova",
         "parrafos": [
             "En el localizador de BMW España, el punto oficial más próximo es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 7,8 km por carretera. La ITV que el registro de la Generalitat sitúa más cerca también está allí: la estación B17 de Applus, en la Ronda Europa, a 8,7 km.",
             "Para la inspección y para cualquier asunto que tenga que pasar por la marca, no hace falta salir del Garraf.",
         ]},
        {"id": "c32-b25", "h2": "43,7 kilómetros por la C-32 hasta el Baix Llobregat",
         "parrafos": [
             "La C-31 atraviesa el propio municipio y la C-32 pasa a un kilómetro del centro. La ruta hasta Dasercars Barcelona encadena la C-31, la C-32 y la B-25 hasta Sant Joan Despí: 43,7 km por carretera, 37,1 en línea recta.",
             "Cubelles no pertenece al Área Metropolitana de Barcelona, así que la recogida del coche que hace el taller queda fuera de su alcance. El viaje compensa para una avería que pide un especialista en la marca o para un fallo que se resiste; para cambiar unas escobillas, no.",
         ]},
        {"id": "cubelles-crece", "h2": "Un 22,6 % más de vecinos que en 2015",
         "parrafos": [
             "Cubelles ha pasado de 14.420 habitantes en 2015 a 17.673 en 2025, según el padrón del INE, en un término de solo 13,49 km². Idescat contaba 8.262 turismos en 2024, 467 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Afecta vivir junto al mar a mi BMW?",
         "a": "Sobre todo a los frenos de un coche que pasa días parado, a los soportes del escape y a los conectores expuestos. Moverlo con regularidad y enjuagar los bajos ayuda."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Cubelles?",
         "a": "Quadis Munich, en Vilanova i la Geltrú, a 7,8 km por carretera según bmw.es."},
        {"q": "¿Y la ITV?",
         "a": "La estación B17 de Vilanova i la Geltrú, en la Ronda Europa, a 8,7 km."},
        {"q": "¿Reparáis también MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.673 habitantes (+22,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Garraf", **F.idescat("080749")},
        {"etiqueta": "Turismos (2024)", "valor": "8.262 · 467 por cada 1.000 hab.", **F.idescat("080749")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 0,5 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Vilanova (B17) · 8,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 7,8 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080749"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["montornes-del-valles"] = {
    "h1": "Montornès del Vallès: ITV y servicio oficial BMW en Granollers, especialista a 35 km",
    "entradilla": "Para un coche de Montornès, casi todo lo oficial está en Granollers, a menos de ocho kilómetros. El taller especialista BMW de la red queda más lejos, en Sant Joan Despí: te contamos por dónde se va y cuándo merece la pena.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 34.7},
    "secciones": [
        {"id": "granollers", "h2": "Granollers: la ITV a 7 km y Pruna Motor a 7,8",
         "parrafos": [
             "La estación de ITV que el registro de la Generalitat sitúa más próxima por carretera es la de Granollers (B18), de Applus, en la avinguda de Sant Julià del polígono El Congost: 7 km. En la misma ciudad está el servicio oficial BMW, Pruna Motor, en la carretera C-17, km 19,060, a 7,8 km según el buscador de bmw.es.",
             "Las llamadas a revisión que convoque BMW se resuelven en un concesionario de la marca como ese. El resto —mantenimiento, desgaste, averías fuera de garantía— puedes llevarlo donde prefieras.",
         ]},
        {"id": "ruta-montornes", "h2": "Hacia Sant Joan Despí por la C-33 y la B-20",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona sale por la BV-5001, toma la C-33 y cruza por la B-20 hasta Sant Joan Despí: 34,7 km por carretera, 25,9 en línea recta.",
             "Montornès no está en el Área Metropolitana de Barcelona, y la recogida que ofrece el taller no llega. Para un trabajo de un día, lo cómodo es dejar el coche a primera hora y volver a por él al cierre.",
         ]},
        {"id": "diesel-autopista", "h2": "Un diésel con la autopista a dos kilómetros",
         "parrafos": [
             "Los diésel de BMW de las familias N47, N57, B47 y B57 necesitan, de vez en cuando, un tramo a régimen sostenido para quemar el hollín del filtro de partículas. Desde Montornès es fácil: la AP-7 pasa a unos dos kilómetros del centro y la C-33 a 2,4. Lo que no le sienta bien es el uso contrario: arrancar, recorrer cuatro calles y apagar, semana tras semana.",
             "Si el aviso del filtro aparece a menudo, conviene mirar también el sensor de presión diferencial y la válvula EGR antes de dar el filtro por perdido.",
         ]},
        {"id": "montornes-en-cifras", "h2": "17.102 habitantes en 10,23 km²",
         "parrafos": [
             "El padrón de 2025 da a Montornès del Vallès 17.102 vecinos, un 5,8 % más que diez años antes (16.172). Idescat, con datos de la DGT, contaba 8.562 turismos en 2024: 501 por cada 1.000 habitantes, prácticamente uno por cada dos personas.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Montornès?",
         "a": "La estación más próxima en el registro de la Generalitat es Granollers (B18), en el polígono El Congost, a 7 km."},
        {"q": "¿Qué servicio oficial BMW tengo más cerca?",
         "a": "Pruna Motor, en la C-17 a su paso por Granollers, a 7,8 km."},
        {"q": "¿Cuántos kilómetros hay hasta vuestro taller?",
         "a": "34,7 por carretera, por la BV-5001, la C-33 y la B-20 hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "17.102 habitantes (+5,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("081363")},
        {"etiqueta": "Turismos (2024)", "valor": "8.562 · 501 por cada 1.000 hab.", **F.idescat("081363")},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 7,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 34,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081363"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["cunit"] = {
    "h1": "Cunit: un BMW en el Baix Penedès, con lo oficial en Vilanova y el taller a 49,6 km",
    "entradilla": "Cunit es provincia de Tarragona, pero lo que un dueño de BMW necesita a mano está en el Garraf: el servicio oficial y la ITV más próximos, en Vilanova i la Geltrú. El taller especialista de la red queda en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 49.6},
    "secciones": [
        {"id": "cunit-crece", "h2": "De 11.883 a 16.385 vecinos en diez años",
         "parrafos": [
             "Entre 2015 y 2025 el padrón de Cunit ha sumado un 37,9 % de habitantes. Idescat contaba 7.152 turismos en 2024: 436 por cada 1.000 vecinos, en un término de 9,74 km².",
             "Si has llegado a Cunit en estos años y el historial de mantenimiento se quedó en tu anterior taller, no lo des por perdido: el propio coche guarda los servicios pendientes en el indicador de mantenimiento, y con un equipo de diagnosis BMW se leen y se ponen al día.",
         ]},
        {"id": "lo-de-vilanova", "h2": "Lo que tienes en Vilanova i la Geltrú",
         "parrafos": [
             "A 11,2 km por carretera está Quadis Munich, el concesionario BMW de la avinguda d'Eduard Toldrà 69, que es el punto oficial más próximo en el buscador de bmw.es. Para la inspección, el listado de la Generalitat da como estación más a mano por carretera la B17 de Applus, en la Ronda Europa de la misma ciudad, a 12,1 km.",
         ]},
        {"id": "costa-cunit", "h2": "A cuatrocientos metros de la costa",
         "parrafos": [
             "El centro de Cunit está a 0,4 km de la línea de costa. Con el mar tan cerca, la humedad salina no castiga solo la carrocería: el condensador del aire acondicionado, que es lo primero que recibe el aire en el frontal, es de las piezas que antes acusan la corrosión en los coches de costa.",
             "Las juntas de goma y las escobillas, resecas por la sal y el sol, son la otra víctima habitual. Revisarlas antes del otoño evita filtraciones y cristales mal barridos.",
         ]},
        {"id": "c32-hasta-sant-joan-despi", "h2": "Por la C-32 y la B-25 hasta el taller",
         "parrafos": [
             "Con la C-31 pasando por el municipio y la C-32 a 1,4 km, la salida es directa. La ruta hasta Dasercars Barcelona, en Sant Joan Despí, suma 49,6 km por carretera (40,3 en línea recta) por la C-32 y la B-25. La recogida del taller no llega a Cunit, que queda fuera del área metropolitana.",
             "Antes de hacer el viaje, una llamada con el modelo, el año y los kilómetros del coche permite saber si el problema es para un especialista o se arregla cerca.",
         ]},
    ],
    "faq": [
        {"q": "¿Por qué el servicio oficial que me toca está en otra provincia?",
         "a": "Porque el punto oficial BMW más próximo a Cunit en el localizador de bmw.es es Quadis Munich, en Vilanova i la Geltrú, a 11,2 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La que el registro de la Generalitat sitúa más cerca por carretera es Vilanova (B17), en la Ronda Europa, a 12,1 km."},
        {"q": "¿Recogéis el coche en Cunit?",
         "a": "No. La recogida cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "16.385 habitantes (+37,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Penedès", **F.idescat("430516")},
        {"etiqueta": "Turismos (2024)", "valor": "7.152 · 436 por cada 1.000 hab.", **F.idescat("430516")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 0,4 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Vilanova (B17) · 12,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 11,2 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("430516"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["vallirana"] = {
    "h1": "Vallirana: el taller BMW de la red a 17,7 km, más cerca que el concesionario",
    "entradilla": "Desde Vallirana, el taller especialista BMW de la red queda más cerca que el servicio oficial de la marca: 17,7 km por la B-24 y la A-2 frente a 18,6 km hasta Sant Boi. Hay un matiz: Vallirana no está en el área metropolitana, y eso cambia algunas cosas.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 17.7},
    "secciones": [
        {"id": "b24-a2", "h2": "La B-24 hasta la A-2",
         "parrafos": [
             "La B-24 pasa a medio kilómetro del centro de Vallirana y es el camino al taller: se sigue hasta la A-2 y de ahí a Sant Joan Despí, donde está Dasercars Barcelona, en el carrer del Tambor del Bruc 3. Son 17,7 km por carretera y 11,2 en línea recta. La N-340 queda a 1,2 km del centro.",
             "Con esa distancia, dejar el coche por la mañana y volver a por él por la tarde es perfectamente viable.",
         ]},
        {"id": "fuera-del-amb", "h2": "Fuera del área metropolitana por muy poco",
         "parrafos": [
             "Vallirana es Baix Llobregat, pero no figura entre los 36 municipios del Área Metropolitana de Barcelona. La recogida y entrega del coche y el vehículo de cortesía que ofrece el taller se limitan a esa área, así que aquí no llegan. Cervelló y Corbera de Llobregat, a 2,5 y 3,5 km en línea recta, sí están dentro.",
             "En la práctica, para un trabajo de un día no supone gran diferencia; para uno de varios días, cuenta con organizar tú la ida y la vuelta.",
         ]},
        {"id": "presupuesto-vallirana", "h2": "Cómo se presupuesta un trabajo",
         "parrafos": [
             "Cada reparación sale con presupuesto escrito, y el taller no toca nada que no hayas aprobado antes. La diagnosis, cuando hay que conectar el equipo, también lleva su presupuesto: es trabajo técnico, no un trámite.",
             "Si el coche es un diésel con avisos repetidos de filtro de partículas o de AdBlue, apunta cuándo salen y en qué tipo de trayecto. Ayuda mucho a acotar la causa.",
         ]},
        {"id": "oficial-e-itv", "h2": "Sant Boi para el servicio oficial; Sant Just o Sant Andreu para la ITV",
         "parrafos": [
             "El punto oficial BMW más próximo en el localizador de bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 18,6 km. Para la ITV, el registro de la Generalitat da dos estaciones casi a la par por carretera: la de Sant Just Desvern (B05), en la avinguda de la Riera, a 15,3 km, y la de Sant Andreu de la Barca (B21), en la N-II, a 15,5.",
             "Vallirana tenía 16.245 habitantes en 2025, un 11 % más que en 2015, y 8.636 turismos en 2024 según Idescat: 532 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Vallirana?",
         "a": "No: Vallirana no está en el Área Metropolitana de Barcelona, y la recogida solo cubre esa área."},
        {"q": "¿Qué está más cerca, vuestro taller o el concesionario?",
         "a": "El taller: 17,7 km hasta Sant Joan Despí, frente a 18,6 km hasta Barcelona Premium, en Sant Boi."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Sant Just Desvern (B05), a 15,3 km por carretera, o en Sant Andreu de la Barca (B21), a 15,5, según el registro de la Generalitat."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "16.245 habitantes (+11 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082956")},
        {"etiqueta": "Turismos (2024)", "valor": "8.636 · 532 por cada 1.000 hab.", **F.idescat("082956")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Just Desvern (B05) · 15,3 km; Sant Andreu (B21) · 15,5", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Boi · 18,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 17,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082956"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["corbera-de-llobregat"] = {
    "h1": "Corbera de Llobregat: taller BMW a 19,9 km y recogida dentro del área metropolitana",
    "entradilla": "Corbera está en alto, a 342 metros, y forma parte del Área Metropolitana de Barcelona. Eso abre una opción que no tienen todos los pueblos de la zona: que el taller recoja el coche, si hay disponibilidad.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 19.9},
    "secciones": [
        {"id": "recogida-corbera", "h2": "Recogida, entrega y coche de cortesía, si hay hueco",
         "parrafos": [
             "Dasercars Barcelona ofrece recogida y entrega del coche y vehículo de cortesía dentro del área metropolitana, y Corbera de Llobregat está dentro. Las dos cosas dependen de la disponibilidad del día, así que lo sensato es pedirlas al cerrar la cita y no la víspera.",
             "Si prefieres llevarlo tú, la ruta baja por la BV-2421 hasta la B-24 y sigue por la A-2 hasta Sant Joan Despí: 19,9 km por carretera, 13,3 en línea recta.",
         ]},
        {"id": "frenos-en-bajada", "h2": "Frenos y una carretera de bajada",
         "parrafos": [
             "El centro urbano está a 342 metros, y llegar a la red principal supone perder altura. En bajadas repetidas el líquido de frenos se calienta más, y como absorbe humedad con los años, uno viejo pierde margen antes de lo que parece. Por eso BMW lo programa por tiempo, y el indicador de servicio lo pide aunque el coche apenas haga kilómetros.",
             "Pastillas y discos también trabajan más con ese perfil. Un chirrido o una vibración al frenar cuesta abajo son motivo suficiente para revisarlos.",
         ]},
        {"id": "itv-sant-andreu", "h2": "ITV en Sant Andreu de la Barca, servicio oficial en Sant Boi",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es Sant Andreu de la Barca (B21), de Applus, en la N-II, punto kilométrico 592,5: 10,4 km desde Corbera.",
             "El servicio oficial BMW que da bmw.es como más próximo queda más lejos que nuestro taller: Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 22 km.",
         ]},
        {"id": "corbera-en-cifras", "h2": "16.010 vecinos, un 12,4 % más que en 2015",
         "parrafos": [
             "Corbera de Llobregat ha pasado de 14.240 habitantes en 2015 a 16.010 en 2025, en un término de 18,41 km². En 2024 tenía 8.002 turismos según Idescat a partir de la DGT: 500 por cada 1.000 vecinos, un coche por cada dos personas.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Corbera de Llobregat?",
         "a": "Sí. Corbera está dentro del área metropolitana de Barcelona; la recogida y entrega está sujeta a disponibilidad, así que pídela al reservar."},
        {"q": "¿Cada cuánto hay que cambiar el líquido de frenos de un BMW?",
         "a": "Por tiempo, según el plan de mantenimiento: el indicador de servicio lo avisa aunque el coche haga pocos kilómetros."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "Sant Andreu de la Barca (B21), a 10,4 km por carretera, según la Generalitat."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "16.010 habitantes (+12,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080728")},
        {"etiqueta": "Altitud", "valor": "342 m", **F.idescat("080728")},
        {"etiqueta": "Turismos (2024)", "valor": "8.002 · 500 por cada 1.000 hab.", **F.idescat("080728")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu de la Barca (B21) · 10,4 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 19,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080728"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["torello"] = {
    "h1": "Torelló, en Osona: cuándo merece la pena llevar el BMW a 93,2 km",
    "entradilla": "Entre Torelló y nuestro taller de Sant Joan Despí hay 93,2 km de carretera. Es una distancia que no se hace por una revisión, y conviene decirlo antes que nada. Lo que sí tienes cerca está en Vic.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 93.2},
    "secciones": [
        {"id": "vic-a-17-km", "h2": "En Vic, a 17 km: el concesionario y la ITV",
         "parrafos": [
             "El servicio oficial BMW más próximo en el buscador de bmw.es es Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 17,6 km por carretera. En la misma ciudad está la estación ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22, a 17 km: es la más próxima a Torelló en el registro de la Generalitat.",
             "Para el mantenimiento rutinario, la inspección o cualquier cosa que pueda hacer un buen taller de la comarca, no hay motivo para salir de Osona.",
         ]},
        {"id": "lo-que-justifica-el-viaje", "h2": "Qué justifica más de noventa kilómetros",
         "parrafos": [
             "El desplazamiento tiene sentido cuando hace falta alguien que trabaje solo con BMW y MINI: un fallo electrónico intermitente que ya ha pasado por otro taller sin solución, la cadena de distribución de un diésel M47, N47 o N57 que empieza a sonar, o un problema de escape y emisiones, para el que el taller cuenta con homologación REDISTA.",
             "Antes de coger el coche, llama y cuenta el síntoma con el modelo, el año y los kilómetros. El presupuesto llega por escrito y no se empieza nada sin tu visto bueno, de modo que decides con el número delante.",
         ]},
        {"id": "c37-c17", "h2": "La ruta: C-37, C-17 y entrada por la B-20",
         "parrafos": [
             "Desde el centro de Torelló, la ruta sale por la BV-5224 hacia la C-37 y baja por la C-17 y la C-33 hasta enlazar con la B-20: 93,2 km por carretera para 77,5 en línea recta. La C-37 pasa a 1,5 km del centro y la C-17 a 2,5.",
             "Torelló queda lejos del área metropolitana y la recogida del taller no llega. Si el coche tiene que pasar la noche en el taller, organiza la vuelta antes de salir.",
         ]},
        {"id": "torello-en-cifras", "h2": "15.334 vecinos a 508 metros",
         "parrafos": [
             "El padrón de 2025 cuenta 15.334 habitantes en Torelló, un 10,5 % más que en 2015 (13.881), en un término de 13 km² a 508 metros de altitud. Idescat contaba 7.913 turismos en 2024: 516 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Osona?",
         "a": "No. El taller de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 93,2 km de Torelló."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 17,6 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En la estación ITV Osona (B04) de Vic, a 17 km, según el registro de la Generalitat."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "15.334 habitantes (+10,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082858")},
        {"etiqueta": "Turismos (2024)", "valor": "7.913 · 516 por cada 1.000 hab.", **F.idescat("082858")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 17 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 17,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 93,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082858"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["la-llagosta"] = {
    "h1": "La Llagosta: ITV a 4,6 km y taller especialista BMW a 29,2 km",
    "entradilla": "En poco más de tres kilómetros cuadrados, La Llagosta reúne 13.280 vecinos y queda rodeada de carreteras. Para quien tiene aquí un BMW, la ITV está casi al lado, en Santa Perpètua de Mogoda, y el taller especialista de la red, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 29.2},
    "secciones": [
        {"id": "itv-santa-perpetua", "h2": "La ITV más próxima: CIM Vallès, en Santa Perpètua",
         "parrafos": [
             "La estación que el registro de la Generalitat sitúa más cerca por carretera es la ITV CIM Vallès (B20), de TÜV Rheinland, en Santa Perpètua de Mogoda: 4,6 km desde el centro de La Llagosta, 2,6 en línea recta.",
             "Con la inspección tan a mano, si el coche no tiene nada más pendiente basta con una pre-ITV cerca de casa; si va a pasar por el taller por otro motivo, aprovecha esa visita para revisar luces, frenos y emisiones.",
         ]},
        {"id": "cinco-carreteras", "h2": "Carreteras a menos de tres kilómetros",
         "parrafos": [
             "Entre las carreteras que OpenStreetMap registra a menos de tres kilómetros del centro están la C-17 a 0,9 km, la C-33 a 1 km, la C-59 a 1,9, la AP-7 a 2,5 y la B-140 a 2,8.",
             "Para un BMW diésel es buena noticia: rodar un rato a régimen constante, que es lo que el filtro de partículas necesita para quemar el hollín acumulado, está a la vuelta de la esquina. Si en cambio el coche solo se mueve entre retenciones, con muchas paradas, el desgaste se concentra en embrague, frenos y caja automática.",
         ]},
        {"id": "ruta-c33", "h2": "29,2 km por la C-33 y la B-20",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona, en el carrer del Tambor del Bruc 3 de Sant Joan Despí, toma la C-33 y cruza por la B-20 hasta Sant Joan Despí: 29,2 km por carretera, 19,7 en línea recta. La Llagosta no forma parte del Área Metropolitana de Barcelona, y la recogida del taller no llega hasta aquí.",
             "El servicio oficial BMW más próximo según bmw.es es Sitjas, un taller autorizado en el carrer Quintana 64 de Sabadell, a 10,1 km por carretera; Quadis Munich, también en Sabadell, queda casi a la par, a 10,5.",
         ]},
        {"id": "la-llagosta-en-cifras", "h2": "4.383 habitantes por kilómetro cuadrado",
         "parrafos": [
             "La Llagosta tenía 13.280 habitantes en 2025, prácticamente los mismos que en 2015 (13.252). Con 3,03 km² de término, salen 4.383 por kilómetro cuadrado. Idescat contaba 5.629 turismos en 2024: 424 por cada 1.000 habitantes.",
             "En calles densas, el coche pasa mucho tiempo aparcado y se mueve en tramos cortos: buena razón para vigilar la batería, que en un BMW, además, hay que dar de alta en el sistema cuando se cambia.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde La Llagosta?",
         "a": "En la ITV CIM Vallès (B20) de Santa Perpètua de Mogoda, a 4,6 km por carretera."},
        {"q": "¿Recogéis el coche en La Llagosta?",
         "a": "No. La recogida del taller solo cubre el área metropolitana de Barcelona, y La Llagosta queda fuera."},
        {"q": "¿Por qué hay que dar de alta la batería nueva de un BMW?",
         "a": "El sistema de gestión de energía adapta la carga al tipo y la edad de la batería que conoce. Si se monta una nueva sin informarle, la sigue tratando como la vieja."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "13.280 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("081056")},
        {"etiqueta": "Turismos (2024)", "valor": "5.629 · 424 por cada 1.000 hab.", **F.idescat("081056")},
        {"etiqueta": "ITV más cercana", "valor": "CIM Vallès (B20), Santa Perpètua de Mogoda · 4,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Sitjas (taller autorizado), Sabadell · 10,1 km (Quadis Munich · 10,5)", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 29,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081056"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["sant-sadurni-d-anoia"] = {
    "h1": "Sant Sadurní d'Anoia: tu BMW a 37 km del taller especialista por la AP-7",
    "entradilla": "Sant Sadurní tiene la AP-7 a poco más de un kilómetro, y eso lo marca casi todo: el taller especialista de la red, en Sant Joan Despí, queda a 37 km de autopista, y el servicio oficial BMW más próximo, en Vilanova i la Geltrú, no está mucho más cerca.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 37.0},
    "secciones": [
        {"id": "ap7-b23", "h2": "De la AP-7 a la B-23",
         "parrafos": [
             "La ruta que traza OpenStreetMap hasta Dasercars Barcelona solo usa dos vías principales: la AP-7, que pasa a 1,1 km del centro, y la B-23 hasta Sant Joan Despí. En total, 37 km por carretera y 24,1 en línea recta.",
             "Sant Sadurní no está en el Área Metropolitana de Barcelona, así que la recogida del taller no llega. Con una ruta tan directa, si el trabajo es de un día, lo práctico es dejar el coche al abrir y llevártelo al cierre.",
         ]},
        {"id": "oficial-a-30-km", "h2": "El concesionario más cercano, a 30,5 km en Vilanova",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 30,5 km por carretera. Con distancias tan parecidas al servicio oficial y al especialista independiente, la elección depende del tipo de trabajo, no de la cercanía.",
             "Si el coche aún está en garantía, hacer las revisiones fuera del concesionario no la pone en riesgo: el Reglamento (UE) 461/2010 lo ampara, con la condición de cumplir el plan de mantenimiento de BMW en intervalos, aceites y recambios.",
         ]},
        {"id": "itv-olerdola", "h2": "La ITV, en Olèrdola",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Olèrdola (B09), de Applus, en la avinguda de l'Hostal Nou: 13,7 km desde el centro de Sant Sadurní.",
         ]},
        {"id": "sant-sadurni-en-cifras", "h2": "12.911 vecinos y 6.631 turismos",
         "parrafos": [
             "El padrón de 2025 da a Sant Sadurní d'Anoia 12.911 habitantes, un 1,7 % más que en 2015. En 2024 había 6.631 turismos censados según Idescat: 514 por cada 1.000 vecinos, en un término de 18,96 km² a 162 metros de altitud.",
             "Si tu coche hace a diario la AP-7, el desgaste se concentra en neumáticos, frenos delanteros y aceite. El indicador de servicio calcula el cambio según el uso real, y estirarlo no sale a cuenta.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué hay más cerca de Sant Sadurní, vuestro taller o el concesionario?",
         "a": "El concesionario BMW de Vilanova i la Geltrú, a 30,5 km; nuestro taller está a 37 km, en Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más próxima en el registro de la Generalitat es Olèrdola (B09), a 13,7 km."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No, la recogida solo cubre el área metropolitana de Barcelona."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI y BMW comparten electrónica y buena parte de los motores."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "12.911 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("082401")},
        {"etiqueta": "Turismos (2024)", "valor": "6.631 · 514 por cada 1.000 hab.", **F.idescat("082401")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 13,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 30,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 37 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082401"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["argentona"] = {
    "h1": "Argentona: ITV en el propio municipio y servicio oficial BMW a 5 km, en Mataró",
    "entradilla": "En Argentona tienes la ITV dentro del término municipal y el concesionario BMW de Mataró a 5 km. El taller especialista de la red queda más lejos, a 42,6 km en Sant Joan Despí; te explicamos para qué compensa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 42.6},
    "secciones": [
        {"id": "itv-el-cros", "h2": "La ITV del polígono El Cros",
         "parrafos": [
             "El registro de estaciones de la Generalitat incluye una ITV en el municipio: la de Argentona (B08), gestionada por Applus, en la zona industrial sector sud del polígono El Cros. Para un coche de Argentona no hay que buscar más.",
             "Si el coche tiene algo pendiente —una luz fundida, un testigo encendido, holguras en la dirección—, resuélvelo antes de la cita: un defecto grave obliga a volver.",
         ]},
        {"id": "pruna-mataro", "h2": "Pruna Motor, en la Via Sergia de Mataró",
         "parrafos": [
             "El servicio oficial BMW más próximo en el localizador de bmw.es es Pruna Motor, en la Via Sergia 2 de Mataró, a 5 km por carretera. Las campañas de revisión que convoca BMW y las reparaciones en garantía que dependen de la marca pasan por allí.",
             "Para el mantenimiento y las averías fuera de garantía, la elección es tuya. Nosotros somos un taller independiente especializado en BMW y MINI, no un concesionario.",
         ]},
        {"id": "ruta-maresme", "h2": "Por la C-32 hacia el Baix Llobregat",
         "parrafos": [
             "Desde el centro de Argentona, la ruta hasta Dasercars Barcelona coge la C-32 y cruza por la B-20 hasta Sant Joan Despí: 42,6 km por carretera y 35 en línea recta. A menos de tres kilómetros pasan, además, la C-60, la B-40 y la N-II.",
             "Argentona no forma parte del Área Metropolitana de Barcelona y la recogida del taller no llega. Para que el viaje no sea en balde, llama antes y explica el síntoma con el modelo y el año del coche.",
         ]},
        {"id": "argentona-en-cifras", "h2": "12.891 vecinos a 4,3 km del mar",
         "parrafos": [
             "El padrón de 2025 da a Argentona 12.891 habitantes, un 7,6 % más que en 2015. Idescat contaba 6.722 turismos en 2024, 521 por cada 1.000 vecinos. El centro está a 88 metros de altitud y a 4,3 km de la costa: lo bastante cerca como para no olvidarse de mirar de vez en cuando bajos y conectores.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Argentona?",
         "a": "Sí: la estación B08, en el polígono El Cros, según el registro de la Generalitat."},
        {"q": "¿Dónde está el concesionario BMW más cercano?",
         "a": "Pruna Motor, en la Via Sergia 2 de Mataró, a 5 km."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 42,6 km por la C-32 y la B-20, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "12.891 habitantes (+7,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("080095")},
        {"etiqueta": "Turismos (2024)", "valor": "6.722 · 521 por cada 1.000 hab.", **F.idescat("080095")},
        {"etiqueta": "ITV en el municipio", "valor": "Argentona (B08), polígono El Cros", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 42,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080095"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["montgat"] = {
    "h1": "Montgat: recogida del BMW dentro del área metropolitana y taller a 25,3 km",
    "entradilla": "Montgat forma parte del Área Metropolitana de Barcelona, y es lo primero que debe saber quien tiene aquí un BMW o un MINI: el taller de Sant Joan Despí puede recoger y devolver el coche, siempre que haya disponibilidad.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 25.3},
    "secciones": [
        {"id": "recoger-en-montgat", "h2": "Que el coche vaya solo al taller",
         "parrafos": [
             "Dasercars Barcelona ofrece recogida y entrega del coche dentro del área metropolitana, y vehículo de cortesía para los trabajos largos; ambos, sujetos a disponibilidad. Desde Montgat el taller queda a 25,3 km por la B-20, así que es la opción que más trayecto te ahorra.",
             "Pídelo al reservar e indica dónde estará el coche. Si prefieres llevarlo tú, la B-20 pasa a 0,3 km del centro.",
         ]},
        {"id": "entre-la-playa-y-la-c32", "h2": "Un municipio entre la playa y la C-32",
         "parrafos": [
             "La C-31 y la C-32 pasan a 0,1 km del centro y la N-II a 0,2; la costa queda a 1,3 km. El salitre trabaja despacio: un coche que pasa años junto al mar acaba mostrando óxido en la tornillería de los bajos, en las grapas del escape y en los anclajes de la matrícula, y sulfato en los bornes de la batería antes que en otros sitios.",
             "Cuando revises el coche, pide que miren los bajos con el coche elevado: es la única forma de ver el estado real de soportes y tubos.",
         ]},
        {"id": "oficial-sant-adria", "h2": "Servicio oficial en Sant Adrià, ITV en Badalona",
         "parrafos": [
             "El punto oficial BMW más próximo en el localizador de bmw.es es Barcelona Premium, en la calle Juan de Austria 1 de Sant Adrià de Besòs, junto a la Ronda Litoral, a 8,7 km. La ITV más próxima en el registro de la Generalitat es la de Badalona (B02), en el carrer de la Indústria 427-449, a 7,7 km.",
             "Mantener el coche fuera del concesionario no hace perder la garantía: el Reglamento (UE) 461/2010 solo exige que se respeten los intervalos y especificaciones del fabricante.",
         ]},
        {"id": "montgat-en-cifras", "h2": "12.879 vecinos en 2,91 km²",
         "parrafos": [
             "Montgat tenía 12.879 habitantes en 2025, un 12 % más que en 2015, en un término de 2,91 km²: 4.426 habitantes por kilómetro cuadrado. Idescat contaba 6.126 turismos en 2024, 476 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Montgat?",
         "a": "Sí, Montgat está dentro del área metropolitana de Barcelona. La recogida y entrega está sujeta a disponibilidad: pídela al reservar."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima en el registro de la Generalitat es Badalona (B02), a 7,7 km."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Barcelona Premium, en la calle Juan de Austria 1 de Sant Adrià de Besòs, a 8,7 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "12.879 habitantes (+12 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("081265")},
        {"etiqueta": "Turismos (2024)", "valor": "6.126 · 476 por cada 1.000 hab.", **F.idescat("081265")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 1,3 km desde el centro", "fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"},
        {"etiqueta": "ITV más cercana", "valor": "Badalona (B02) · 7,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Adrià de Besòs · 8,7 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081265"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

CIUDADES["palleja"] = {
    "h1": "Pallejà: el taller especialista BMW a 10,8 km por la A-2",
    "entradilla": "Desde Pallejà, el taller especialista BMW de la red está a 10,8 km por la A-2, en Sant Joan Despí, más cerca que el concesionario de la marca. Y como Pallejà es área metropolitana, también puedes pedir que lo recojan.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 10.8},
    "secciones": [
        {"id": "a2-diez-km", "h2": "La A-2 a medio kilómetro, el taller a 10,8",
         "parrafos": [
             "La A-2 pasa a 0,5 km del centro de Pallejà y es, prácticamente, el único tramo de la ruta: 10,8 km por carretera, 8,6 en línea recta, hasta la nave de Dasercars Barcelona en el carrer del Tambor del Bruc 3.",
             "El taller abre de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00. Con esta cercanía, puedes dejar el coche antes de ir a trabajar y pasar a por él a la salida.",
         ]},
        {"id": "recogida-palleja", "h2": "Si no puedes acercarlo, el taller lo recoge",
         "parrafos": [
             "Pallejà forma parte del Área Metropolitana de Barcelona, y el taller ofrece recogida y entrega dentro de ella, igual que vehículo de cortesía para los trabajos de varios días. Las dos cosas están sujetas a disponibilidad: lo mejor es pedirlas en el momento de reservar.",
         ]},
        {"id": "oficial-itv-palleja", "h2": "Sant Boi y Sant Andreu de la Barca",
         "parrafos": [
             "El servicio oficial BMW más próximo en el localizador de bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 12,9 km: algo más lejos que el especialista independiente. La ITV que el registro de la Generalitat sitúa más cerca por carretera es Sant Andreu de la Barca (B21), en la N-II, a 5,8 km.",
         ]},
        {"id": "nudo-de-carreteras", "h2": "Diez carreteras a menos de tres kilómetros",
         "parrafos": [
             "OpenStreetMap cuenta a menos de tres kilómetros del centro la N-IIa, la A-2, la B-23, la C-1413a, la B-24, la BV-1468, la N-340, la BV-2002, la BV-2421 y la AP-7. Para un diésel con filtro de partículas es una ventaja: las ocasiones de rodar a ritmo sostenido, que es lo que el filtro necesita para limpiarse, sobran.",
             "Pallejà tenía 12.006 habitantes en 2025, un 6,3 % más que en 2015, y 5.579 turismos en 2024 según Idescat: 465 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuánto hay de Pallejà a vuestro taller?",
         "a": "10,8 km por la A-2 hasta Sant Joan Despí."},
        {"q": "¿Podéis recoger el coche en Pallejà?",
         "a": "Sí, dentro del área metropolitana hay recogida y entrega, sujeta a disponibilidad."},
        {"q": "¿Reparáis MINI?",
         "a": "Sí. Los MINI comparten electrónica y motores con BMW y se diagnostican con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "12.006 habitantes (+6,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("081574")},
        {"etiqueta": "Turismos (2024)", "valor": "5.579 · 465 por cada 1.000 hab.", **F.idescat("081574")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu de la Barca (B21) · 5,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Boi · 12,9 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 10,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081574"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["la-roca-del-valles"] = {
    "h1": "La Roca del Vallès: 563 turismos por cada mil vecinos y el taller BMW a 45,5 km",
    "entradilla": "En La Roca del Vallès hay 563 turismos por cada 1.000 habitantes: más de un coche por cada dos vecinos, en un término amplio y poco denso. Lo que tienes cerca está en Granollers; el taller especialista BMW de la red, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 45.5},
    "secciones": [
        {"id": "termino-disperso", "h2": "36,9 km² y 298 habitantes por kilómetro cuadrado",
         "parrafos": [
             "El término de La Roca del Vallès mide 36,9 km² y la densidad es de 298 habitantes por kilómetro cuadrado, con 11.014 vecinos en el padrón de 2025, un 4,9 % más que en 2015. Idescat contaba 6.206 turismos en 2024.",
             "En un municipio así el coche se usa para casi todo, y en trayectos muy variados: carretera comarcal, rotondas, algún tramo de autopista. Es un uso que reparte el desgaste y que hace aún más importante no saltarse lo que pide el indicador de servicio.",
         ]},
        {"id": "lo-oficial-en-granollers", "h2": "Lo oficial queda en Granollers",
         "parrafos": [
             "Para la inspección, la referencia es la estación B18 de Applus en Granollers, a 8,9 km por carretera según los datos abiertos de la Generalitat. Para el concesionario BMW, Pruna Motor, también en Granollers, a 9,4 km por la C-17.",
             "Ni para la ITV ni para lo que tenga que pasar por la red de la marca hace falta ir más lejos.",
         ]},
        {"id": "ruta-la-roca", "h2": "De la AP-7 a Sant Joan Despí: 45,5 km",
         "parrafos": [
             "La AP-7 pasa a 1,8 km del centro, y por ella empieza la ruta al taller; después, C-33 y B-20 hasta Dasercars Barcelona. Son 45,5 km por carretera, 33 en línea recta.",
             "La recogida del taller no llega hasta aquí, porque La Roca queda fuera del área metropolitana. Con ese trayecto, compensa para trabajos que piden un especialista en la marca: averías electrónicas sin diagnosticar, ruidos de distribución en los diésel N47 y N57, o el sistema de escape y gases, para el que el taller tiene homologación REDISTA.",
         ]},
        {"id": "si-es-un-mini", "h2": "Si tu coche es un MINI",
         "parrafos": [
             "Un MINI moderno es, por dentro, un BMW: comparte arquitectura eléctrica, centralitas y familias de motor. La diagnosis, los procedimientos y los recambios son los mismos, y el taller lo trata exactamente igual.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde La Roca del Vallès?",
         "a": "La estación más próxima por carretera en el registro de la Generalitat es Granollers (B18), a 8,9 km."},
        {"q": "¿Venís a por el coche a La Roca?",
         "a": "No. La recogida cubre solo el área metropolitana de Barcelona, y La Roca del Vallès queda fuera."},
        {"q": "¿Qué distancia hay hasta el taller?",
         "a": "45,5 km por la AP-7, la C-33 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "11.014 habitantes (+4,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("081810")},
        {"etiqueta": "Turismos (2024)", "valor": "6.206 · 563 por cada 1.000 hab.", **F.idescat("081810")},
        {"etiqueta": "ITV más cercana", "valor": "Granollers (B18) · 8,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 9,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 45,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081810"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

CIUDADES["llinars-del-valles"] = {
    "h1": "Llinars del Vallès: ITV en Sant Celoni, concesionario BMW en Granollers y taller a 49,6 km",
    "entradilla": "Llinars del Vallès ha ganado un 14,5 % de población en diez años. Para el dueño de un BMW, sus referencias están repartidas: la ITV más próxima, en Sant Celoni; el concesionario de la marca, en Granollers; y el taller especialista de la red, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 49.6},
    "secciones": [
        {"id": "itv-sant-celoni", "h2": "La ITV de la carretera de Gualba",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sant Celoni (B26), que gestiona TÜV SÜD en la carretera de Gualba 41-43: 12,8 km desde el centro de Llinars.",
             "Si vas a pasar la inspección, revisa antes lo que más suspende: luces, neumáticos, escobillas y cualquier testigo encendido en el cuadro.",
         ]},
        {"id": "concesionario-granollers", "h2": "El concesionario BMW más próximo está en Granollers",
         "parrafos": [
             "El punto oficial BMW que el localizador de bmw.es da como más próximo a Llinars es Pruna Motor, en el km 19 de la C-17, en Granollers, a 17,1 km por carretera. Allí van las campañas de revisión de BMW y lo que cubra la garantía de la marca.",
             "Lo demás —mantenimiento, desgaste, averías fuera de garantía— puede hacerse en un taller independiente.",
         ]},
        {"id": "c35-ap7", "h2": "49,6 kilómetros por la C-35 y la AP-7",
         "parrafos": [
             "La C-35 y la AP-7 pasan a 0,5 km del centro. La ruta hasta Dasercars Barcelona encadena las dos, sigue por la C-33 y termina en la B-20: 49,6 km por carretera, 40,8 en línea recta. La recogida del taller no llega a Llinars, que queda fuera del área metropolitana.",
             "Por distancia, el viaje es para lo específico de la marca. Te damos el presupuesto por escrito antes de empezar y nada se toca sin que lo apruebes; la diagnosis también se presupuesta aparte.",
         ]},
        {"id": "llinars-crece", "h2": "De 9.570 a 10.956 vecinos",
         "parrafos": [
             "El padrón de 2025 da a Llinars del Vallès 10.956 habitantes, frente a los 9.570 de 2015. Idescat contaba 5.667 turismos en 2024: 517 por cada 1.000 vecinos, en un término de 27,63 km² a 198 metros de altitud.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Llinars?",
         "a": "La estación más próxima por carretera en el registro de la Generalitat es Sant Celoni (B26), a 12,8 km."},
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "Porque es el punto oficial que el localizador de bmw.es sitúa más próximo: Pruna Motor, en Granollers, a 17,1 km por carretera."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "49,6 km por carretera, por la C-35, la AP-7, la C-33 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "10.956 habitantes (+14,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("081069")},
        {"etiqueta": "Turismos (2024)", "valor": "5.667 · 517 por cada 1.000 hab.", **F.idescat("081069")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 12,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Granollers · 17,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 49,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081069"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# metaDescription nuevas: solo ciudades SIN impresiones en GSC (todas las de esta
# tanda) cuya descripción anterior prometía ahorro, «diagnóstico oficial» o ISTA.
# Cunit no se toca (su descripción no contiene promesas). Los metaTitle no se tocan.
META = {
    "caldes-de-montbui": "Taller especialista BMW y MINI para Caldes de Montbui: Dasercars Barcelona, a 40,6 km por la C-59 y la C-33. Servicio autorizado e ITV más próximos.",
    "cubelles": "Cubelles, a medio kilómetro del mar: qué vigilar en tu BMW, servicio oficial e ITV en Vilanova i la Geltrú y taller especialista a 43,7 km.",
    "montornes-del-valles": "Montornès del Vallès: ITV y servicio oficial BMW en Granollers y taller especialista independiente a 34,7 km, en Sant Joan Despí.",
    "vallirana": "Vallirana: el taller especialista BMW de la red está a 17,7 km por la B-24 y la A-2, más cerca que el concesionario. ITV y presupuesto por escrito.",
    "corbera-de-llobregat": "Corbera de Llobregat: taller especialista BMW a 19,9 km y recogida en el área metropolitana, sujeta a disponibilidad. ITV en Sant Andreu de la Barca.",
    "torello": "Torelló: concesionario BMW e ITV en Vic, y cuándo compensa llevar el coche al taller especialista de Sant Joan Despí, a 93,2 km.",
    "la-llagosta": "La Llagosta: ITV a 4,6 km en Santa Perpètua de Mogoda y taller especialista BMW y MINI a 29,2 km por la C-33 y la B-20.",
    "sant-sadurni-d-anoia": "Sant Sadurní d'Anoia: taller especialista BMW a 37 km por la AP-7, servicio oficial en Vilanova i la Geltrú e ITV en Olèrdola.",
    "argentona": "Argentona: ITV en el propio municipio, concesionario BMW en Mataró a 5 km y taller especialista independiente a 42,6 km en Sant Joan Despí.",
    "montgat": "Montgat: recogida del coche en el área metropolitana (sujeta a disponibilidad) y taller especialista BMW a 25,3 km. ITV en Badalona.",
    "palleja": "Pallejà: taller especialista BMW y MINI a 10,8 km por la A-2, recogida en el área metropolitana sujeta a disponibilidad e ITV en Sant Andreu de la Barca.",
    "la-roca-del-valles": "La Roca del Vallès: ITV y servicio oficial BMW en Granollers y taller especialista independiente a 45,5 km en Sant Joan Despí.",
    "llinars-del-valles": "Llinars del Vallès: ITV en Sant Celoni, concesionario BMW en Granollers y taller especialista independiente a 49,6 km por la C-35 y la AP-7.",
}


def aplicar_meta():
    from comun import CIUDADES_DIR
    for slug, desc in META.items():
        assert len(desc) <= 160, (slug, len(desc))
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        cj["metaDescription"] = desc
        f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
        print("metaDescription", slug)


if __name__ == "__main__":
    aplicar_meta()
