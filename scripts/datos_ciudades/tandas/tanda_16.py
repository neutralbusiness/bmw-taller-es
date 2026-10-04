# Tanda 16: Calafell, Sitges, Pineda de Mar, Paracuellos de Jarama, Sant Andreu de la
# Barca, Ciempozuelos, Santa Perpètua de Mogoda, Torrelodones, Olesa de Montserrat,
# Villanueva de la Cañada, Esparreguera, Manlleu, Algete, Sant Just Desvern y Calella.
# Ninguna está en la lista de exclusiones del coordinador (todas son municipios con
# taller de la red con dirección).
#
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_16
# Las 15 ciudades tienen impresiones en GSC (cache/paso_gsc.json): no se tocan ni
# metaTitle ni metaDescription, así que esta tanda no lleva dicts META ni TITLES.
#
# Frases gastadas (guía §6), máximo 3 de 15 cada una:
#   Reglamento 461/2010: santa-perpetua-de-mogoda, algete, sant-just-desvern
#   presupuesto por escrito / sin aprobación: ciempozuelos, olesa-de-montserrat, calella
#   llamar antes con modelo/año/km: pineda-de-mar, villanueva-de-la-canada, manlleu
#   campañas en la red oficial: sitges, torrelodones, esparreguera
#   horario completo: sant-andreu-de-la-barca, paracuellos-de-jarama
#   periodicidad de la ITV: ninguna
import sys
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI.parent / "piloto"))
sys.path.insert(0, str(_AQUI.parent))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

COSTA = {"fuente": "Natural Earth", "url": "https://www.naturalearthdata.com/"}

# ---------------------------------------------------------------- Calafell
CIUDADES["calafell"] = {
    "h1": "Calafell: un BMW a 1,2 km del mar y a 55 km del taller especialista",
    "entradilla": "A poco más de un kilómetro de la playa, el coche convive con el salitre todo el año. La ITV queda en Bellvei, el servicio oficial en Vilanova i la Geltrú y nuestro taller, en Sant Joan Despí: así se reparte lo que necesita un BMW de Calafell.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 55.2},
    "secciones": [
        {"id": "aire-salino", "h2": "Lo que el aire del mar pide revisar",
         "parrafos": [
             "El centro del municipio está a unos 1,2 km de la costa. La sal en suspensión trabaja despacio, pero trabaja: los bajos, los soportes del escape y los anclajes de la suspensión son lo primero que se oxida, y los conectores eléctricos que quedan al aire acaban con verdín si nadie los mira.",
             "Un BMW que pasa semanas aparcado cerca del paseo marítimo suele estrenar la vuelta a la carretera con un roce metálico al frenar: es óxido superficial en los discos y casi siempre se va en pocos kilómetros. Si no se va, o si vibra el volante, toca revisar discos y pastillas antes de que el desgaste sea irregular."
         ]},
        {"id": "bellvei-y-vilanova", "h2": "ITV a 5,3 km y servicio oficial a 19,7",
         "parrafos": [
             "La estación de ITV del Baix Penedès (T07) está en el polígono Els Massets de Bellvei: 5,3 km por carretera según el registro de la Generalitat. Es la referencia también para El Vendrell, el municipio de al lado.",
             "Para lo que depende de la marca —una carta de BMW por una campaña o una reparación en garantía— el localizador de bmw.es da como punto oficial más próximo Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 19,7 km."
         ]},
        {"id": "c32-b25", "h2": "La C-32 a menos de un kilómetro",
         "parrafos": [
             "La autopista C-32 pasa a 0,8 km del centro y es la misma que lleva a nuestro taller: C-32 y B-25 hasta el carrer del Tambor del Bruc, 55,2 km por carretera. Calafell no forma parte del Área Metropolitana de Barcelona, de modo que la recogida del coche que ofrece el taller no llega aquí.",
             "Con esa distancia, el viaje se justifica para una avería que pide especialista: un diésel N47 con ruido de cadena, un fallo de AdBlue o una electrónica que nadie ha sabido leer. Una revisión de rutina la resuelve cualquier taller del Penedès."
         ]},
        {"id": "calafell-crece", "h2": "Un tercio más de vecinos que en 2015",
         "parrafos": [
             "El padrón pasó de 24.256 habitantes en 2015 a 32.624 en 2025, un 34,5 % más. Idescat, con datos de la DGT, contaba 14.326 turismos en 2024: 439 por cada 1.000 vecinos, bastante por encima de los 281 de Barcelona ciudad."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Calafell?",
         "a": "La estación más próxima en el registro de la Generalitat es la del Baix Penedès (T07), en Bellvei, a 5,3 km por carretera."},
        {"q": "¿Afecta la cercanía del mar a mi BMW?",
         "a": "Sí: acelera el óxido de bajos y anclajes, el de los discos de un coche parado y la sulfatación de conectores. Un lavado de bajos con agua dulce ayuda."},
        {"q": "¿Recogéis el coche en Calafell?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "32.624 habitantes (+34,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Penedès", **F.idescat("430379")},
        {"etiqueta": "Turismos (2024)", "valor": "14.326 · 439 por cada 1.000 hab.", **F.idescat("430379")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 1,2 km desde el centro", **COSTA},
        {"etiqueta": "ITV más cercana", "valor": "Baix Penedès (T07), Bellvei · 5,3 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 55,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("430379"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sitges
CIUDADES["sitges"] = {
    "h1": "Sitges y tu BMW: Vilanova para la ITV y la marca, Sant Joan Despí para el especialista",
    "entradilla": "Ni la ITV ni el servicio oficial BMW están dentro del término de Sitges: los dos quedan en Vilanova i la Geltrú, a unos 10 km. Nuestro taller está a 32,2 km por la C-32. Te explicamos qué conviene hacer en cada sitio.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 32.2},
    "secciones": [
        {"id": "todo-en-vilanova", "h2": "Dos citas en Vilanova i la Geltrú",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova, a 9,6 km por carretera. Si BMW te escribe por una llamada a revisión, esa cita es allí: las campañas del fabricante solo las hace la red de la marca.",
             "La inspección técnica también cae en Vilanova: la estación B17, en la Ronda Europa, a 10,6 km según el registro de la Generalitat."
         ]},
        {"id": "pegado-al-mar", "h2": "A 0,2 km del agua",
         "parrafos": [
             "El centro de Sitges está a unos 0,2 km de la línea de costa, y eso el coche lo nota. La humedad salina se queda en los pasos de rueda y en los bajos, y los primeros en sufrirla son las grapas, los tornillos del protector inferior y los soportes del escape.",
             "Si el BMW duerme en la calle, merece la pena revisar con más frecuencia los conectores de los sensores de aparcamiento y de los faros: un aviso intermitente en el cuadro suele empezar por ahí."
         ]},
        {"id": "c32-hasta-el-taller", "h2": "32 kilómetros de C-32",
         "parrafos": [
             "Hasta la nave de Dasercars Barcelona son 32,2 km por carretera, 25,6 en línea recta: la C-32 y después la B-25. Sitges pertenece al Garraf y no al Área Metropolitana de Barcelona, así que la recogida que ofrece el taller no llega hasta aquí.",
             "Donde sí aporta un especialista independiente es en el mantenimiento de un coche fuera de garantía y en las averías que el concesionario resuelve cambiando piezas una tras otra."
         ]},
        {"id": "pocos-coches", "h2": "Menos coches por vecino que en Madrid capital",
         "parrafos": [
             "Sitges tenía 32.609 habitantes en 2025, un 15,4 % más que en 2015, y 12.341 turismos en 2024 según Idescat a partir de la DGT: 378 por cada 1.000 vecinos. Es una proporción menor que la de Madrid capital (388) y muy lejos de los municipios de interior."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Sitges?",
         "a": "Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 9,6 km según bmw.es."},
        {"q": "¿Qué ITV me toca?",
         "a": "La más próxima en el registro de la Generalitat es la de Vilanova (B17), en la Ronda Europa, a 10,6 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "32,2 km por la C-32 y la B-25, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "32.609 habitantes (+15,4 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Garraf", **F.idescat("082704")},
        {"etiqueta": "Turismos (2024)", "valor": "12.341 · 378 por cada 1.000 hab.", **F.idescat("082704")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 9,6 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Vilanova (B17), Ronda Europa · 10,6 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 32,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082704"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Pineda de Mar
CIUDADES["pineda-de-mar"] = {
    "h1": "Pineda de Mar: ITV en Blanes, servicio oficial en Mataró y taller BMW a 67,5 km",
    "entradilla": "Para pasar la ITV desde Pineda de Mar se sale de la provincia: la estación más próxima está en Blanes. El servicio oficial BMW queda en Mataró y el taller de la red, en el Baix Llobregat. Distancias y criterio para decidir.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 67.5},
    "secciones": [
        {"id": "itv-blanes", "h2": "La ITV, al otro lado de la Tordera",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es la de Blanes (G07), en la avinguda de l'Estació 47, a 10,7 km. Es ya provincia de Girona, pero según ese registro queda más a mano que cualquier estación del Maresme.",
             "Si el coche tiene una avería pendiente, arréglala antes de pedir hora: volver a la estación por un defecto grave es un segundo viaje."
         ]},
        {"id": "pruna-mataro", "h2": "El concesionario, en Mataró",
         "parrafos": [
             "El localizador de bmw.es sitúa el servicio oficial más próximo en Pruna Motor, en la Via Sèrgia 2 de Mataró, a 30,3 km por carretera. Allí se tramitan las reparaciones que cubre la garantía de BMW."
         ]},
        {"id": "maresme-abajo", "h2": "67,5 km por la C-32: cuándo merece la pena",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona baja por la C-32 y cruza por la B-20 hasta Sant Joan Despí: 67,5 km por carretera, 59,7 en línea recta. Pineda está fuera del área metropolitana, así que la recogida que ofrece el taller no cubre el municipio.",
             "Antes de hacer el viaje, una llamada con el modelo, el año, los kilómetros y lo que notas en el coche ahorra muchas vueltas: a veces basta con eso para saber si el problema es de especialista o lo arregla un taller del pueblo."
         ]},
        {"id": "salitre-pineda", "h2": "La costa a 1,1 km",
         "parrafos": [
             "Con el centro a 1,1 km del mar y la N-II a menos de tres kilómetros, los coches de Pineda acumulan salitre en los bajos y en los discos de freno. Si el BMW está parado entre temporada y temporada, revisa frenos y batería antes de volver a usarlo a diario.",
             "El municipio tenía 30.108 vecinos en 2025 (25.968 en 2015) y 13.967 turismos en 2024 según Idescat a partir de la DGT, 464 por cada 1.000 habitantes."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Pineda de Mar?",
         "a": "La estación más próxima en el registro de la Generalitat es la de Blanes (G07), a 10,7 km por carretera."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Pruna Motor, en la Via Sèrgia 2 de Mataró, a 30,3 km según bmw.es."},
        {"q": "¿Tenéis taller en el Maresme?",
         "a": "No. El taller de la red es Dasercars Barcelona, en Sant Joan Despí, a 67,5 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "30.108 habitantes (+15,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("081635")},
        {"etiqueta": "Turismos (2024)", "valor": "13.967 · 464 por cada 1.000 hab.", **F.idescat("081635")},
        {"etiqueta": "ITV más cercana", "valor": "Blanes (G07) · 10,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 30,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 67,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081635"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Paracuellos de Jarama
CIUDADES["paracuellos-de-jarama"] = {
    "h1": "Paracuellos de Jarama: revisión de tu BMW fuera del concesionario, a 18 km",
    "entradilla": "Quien busca «revisión oficial» en Paracuellos suele querer dos cosas distintas: el concesionario o una revisión hecha según el plan de BMW. Aquí tienes dónde está cada una, la ITV del propio municipio y la ruta a Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 18.4},
    "secciones": [
        {"id": "revision-oficial", "h2": "«Revisión oficial» no siempre significa concesionario",
         "parrafos": [
             "Si lo que quieres es el concesionario, el punto oficial BMW más próximo según bmw.es es Caetano Cuzco, en la calle Alcalá 474 de Madrid, a 14,1 km. Nosotros no somos servicio oficial; somos Dasercars, taller independiente especializado en BMW.",
             "Si lo que quieres es que la revisión se haga según el plan del fabricante —aceite con la homologación de tu motor, filtros, reinicio del indicador de servicio y registro de lo hecho—, eso no exige pasar por la red de la marca, y es justo lo que hacemos."
         ]},
        {"id": "itv-camino-de-cobena", "h2": "La ITV, en el Camino Viejo de Cobeña",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid incluye una estación dentro del municipio: la de DEKRA (estación 2808), en el Camino Viejo de Cobeña 36. No hace falta salir de Paracuellos para la inspección."
         ]},
        {"id": "m113-m12", "h2": "A Alcobendas por la M-113 y la M-12",
         "parrafos": [
             "La ruta hasta la calle Valgrande sale por la M-113 y la M-111 y enlaza con la M-12: 18,4 km por carretera, 11,1 en línea recta. El taller abre de lunes a viernes de 9:00 a 14:00 y de 15:00 a 18:00; dejar el coche por la mañana y recogerlo al cerrar es lo habitual en trabajos de un día.",
             "Para reparaciones más largas hay vehículo de cortesía, y recogida y entrega del coche dentro del área metropolitana de Madrid, ambas cosas sujetas a disponibilidad: pregúntalo al reservar."
         ]},
        {"id": "paracuellos-crece", "h2": "Un 24 % más de vecinos en diez años",
         "parrafos": [
             "Paracuellos pasó de 22.293 habitantes en 2015 a 27.650 en 2025. Tenía 14.158 turismos censados en 2025, según la Comunidad de Madrid a partir de la DGT: 512 por cada 1.000 vecinos, frente a 388 en Madrid capital. Con la M-50 y la R-2 a menos de tres kilómetros, un diésel tiene a mano tramos largos para regenerar el filtro de partículas."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el servicio oficial BMW de la zona?",
         "a": "No. El punto oficial más próximo según bmw.es es Caetano Cuzco, en la calle Alcalá 474 de Madrid. Nosotros somos un taller independiente en Alcobendas."},
        {"q": "¿Hay ITV en Paracuellos de Jarama?",
         "a": "Sí: la estación 2808 de DEKRA, en el Camino Viejo de Cobeña 36, según la Comunidad de Madrid."},
        {"q": "¿Podéis recoger el coche en Paracuellos?",
         "a": "Hay recogida y entrega dentro del área metropolitana de Madrid, sujeta a disponibilidad. Confírmalo al pedir cita."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "27.650 habitantes (+24 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "14.158 · 512 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "DEKRA (2808), Camino Viejo de Cobeña 36", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Caetano Cuzco, c/ Alcalá 474 (Madrid) · 14,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 18,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Sant Andreu de la Barca
CIUDADES["sant-andreu-de-la-barca"] = {
    "h1": "Sant Andreu de la Barca: taller BMW a 14,4 km, dentro del área metropolitana",
    "entradilla": "Desde Sant Andreu de la Barca, el taller especialista y el servicio oficial BMW más próximo quedan prácticamente a la misma distancia, uno a cada lado. Y la ITV la tienes en tu propio término, junto a la N-II.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 14.4},
    "secciones": [
        {"id": "empate-a-catorce", "h2": "14,4 km a un lado, 14,5 al otro",
         "parrafos": [
             "Nuestro taller, Dasercars Barcelona, está a 14,4 km por la N-IIa y la A-2, en el carrer del Tambor del Bruc de Sant Joan Despí. El punto oficial BMW más próximo según bmw.es, Quadis Munich, en el carrer Vallespir 19 de Sant Cugat del Vallès, queda a 14,5 km. Por distancia es un empate.",
             "Lo que cambia es para qué vas. Una reparación cubierta por la garantía de BMW se hace en la red de la marca. El mantenimiento, una avería fuera de garantía o un segundo diagnóstico, donde tú decidas."
         ]},
        {"id": "recogida-amb", "h2": "Un municipio del área metropolitana",
         "parrafos": [
             "Sant Andreu de la Barca forma parte del Área Metropolitana de Barcelona, igual que Sant Joan Despí. Eso te da acceso a la recogida y entrega del coche y al vehículo de cortesía que ofrece el taller, siempre sujetos a disponibilidad: pídelo al reservar.",
             "El horario es de lunes a viernes, de 9:00 a 14:00 y de 15:00 a 18:00; sábado y domingo cerrado."
         ]},
        {"id": "itv-n2", "h2": "La ITV, en la N-II, punto kilométrico 592,5",
         "parrafos": [
             "La estación B21 del registro de la Generalitat está dentro del municipio, en la carretera N-II, pk 592,5. Según ese mismo registro, es también la más próxima por carretera a Esparreguera."
         ]},
        {"id": "cinco-km2", "h2": "Mucha ciudad en 5,5 km²",
         "parrafos": [
             "Sant Andreu tenía 27.094 habitantes en 2025, casi los mismos que en 2015 (27.340), en un término de solo 5,5 km²: 4.926 vecinos por kilómetro cuadrado. Idescat, con datos de la DGT, contaba 12.403 turismos en 2024, 458 por cada 1.000 habitantes.",
             "Con la A-2, la AP-7 y la B-23 a menos de tres kilómetros, los trayectos largos están a mano; lo que castiga al coche aquí es el uso urbano corto, con muchos arranques en frío."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Sant Andreu de la Barca?",
         "a": "No. El taller de la red es Dasercars Barcelona, en Sant Joan Despí, a 14,4 km."},
        {"q": "¿Recogéis el coche en Sant Andreu?",
         "a": "Sí, el municipio está en el área metropolitana. La recogida está sujeta a disponibilidad."},
        {"q": "¿Hay ITV en el municipio?",
         "a": "Sí: la estación B21, en la N-II, pk 592,5, según la Generalitat."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "27.094 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("081960")},
        {"etiqueta": "Turismos (2024)", "valor": "12.403 · 458 por cada 1.000 hab.", **F.idescat("081960")},
        {"etiqueta": "ITV en el municipio", "valor": "Sant Andreu (B21), N-II pk 592,5", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Cugat del Vallès · 14,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 14,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081960"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Ciempozuelos
CIUDADES["ciempozuelos"] = {
    "h1": "Pre-ITV y mantenimiento BMW para Ciempozuelos: lo cercano y lo especialista",
    "entradilla": "La pre-ITV es lo que más se busca desde Ciempozuelos, y la estación oficial más cercana está en Valdemoro, a 5,7 km. Nuestro taller queda a 49,7 km, en Alcobendas: te contamos qué tiene sentido hacer allí y qué no.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 49.7},
    "secciones": [
        {"id": "pre-itv", "h2": "Pre-ITV: dónde tiene sentido hacerla",
         "parrafos": [
             "La ITV que te queda cerca es la de ITV Valdemoro (estación 2863), en la calle Vereda de la Solana 43-45 del polígono Las Canteras, a 5,7 km según el listado de la Comunidad de Madrid. Bajar a Alcobendas solo para una pre-ITV no compensa.",
             "Sí la aprovechas si el coche ya va al taller por otra cosa: luces, holguras, frenos y emisiones se miran en la misma visita, y a la vuelta pides hora en Valdemoro."
         ]},
        {"id": "caja-automatica", "h2": "El aceite de la caja automática",
         "parrafos": [
             "Muchos BMW montan cambios automáticos de ZF, y BMW los entrega con un aceite «de por vida». El propio fabricante del cambio recomienda sustituirlo con los años; si la caja empieza a dar tirones al bajar marchas o tarda en engranar en frío, el aceite y el filtro son lo primero que hay que revisar.",
             "Es un trabajo con procedimiento propio: nivel a temperatura controlada y adaptaciones borradas al terminar. Antes de tocar nada recibes el presupuesto por escrito, y el trabajo no arranca sin tu visto bueno."
         ]},
        {"id": "a4-m30-a1", "h2": "Cruzar Madrid: M-404, A-4, M-30 y A-1",
         "parrafos": [
             "Hasta la calle Valgrande de Alcobendas hay 49,7 km por carretera, 42,1 en línea recta, cruzando de sur a norte por la A-4, la M-30 y la A-1. Si no puedes traer el coche, pregunta al reservar si tu dirección entra en la recogida del taller, que se limita al área metropolitana de Madrid y está sujeta a disponibilidad.",
             "Para las campañas de la marca, el punto oficial más próximo según bmw.es es Vehinter, en la carretera de Madrid a Toledo, en Getafe, a 22,3 km."
         ]},
        {"id": "ciempozuelos-cifras", "h2": "26.350 vecinos y 12.104 turismos",
         "parrafos": [
             "Ciempozuelos tenía 26.350 habitantes en 2025, un 11,2 % más que en 2015, y 12.104 turismos censados ese año según la Comunidad de Madrid a partir de la DGT: 459 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Ciempozuelos?",
         "a": "La estación oficial más cercana es ITV Valdemoro, en el polígono Las Canteras, a 5,7 km."},
        {"q": "¿Cambiáis el aceite de la caja automática?",
         "a": "Sí, con su filtro, control de nivel a temperatura y borrado de adaptaciones. Se presupuesta antes."},
        {"q": "¿A qué distancia está el taller?",
         "a": "A 49,7 km, en la calle Valgrande 17 de Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "26.350 habitantes (+11,2 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "12.104 · 459 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "ITV Valdemoro, pol. Las Canteras · 5,7 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 22,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 49,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Santa Perpètua de Mogoda
CIUDADES["santa-perpetua-de-mogoda"] = {
    "h1": "Santa Perpètua de Mogoda: la ITV del CIM Vallès y un especialista BMW a 29 km",
    "entradilla": "Entre el centro de mercancías, la AP-7 y la C-33, Santa Perpètua está rodeada de carreteras. Lo útil para un BMW: ITV en el término, dos puntos oficiales en Sabadell y nuestro taller a 29,4 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 29.4},
    "secciones": [
        {"id": "itv-les-minetes", "h2": "ITV en el polígono Les Minetes",
         "parrafos": [
             "La estación ITV CIM Vallès (B20) está dentro del municipio, en el carrer Pont Vell, en el Centre Integral de Mercaderies del polígono Les Minetes, según el registro de la Generalitat. Inspección sin salir de casa."
         ]},
        {"id": "dos-en-sabadell", "h2": "Dos puntos oficiales en Sabadell, casi a la par",
         "parrafos": [
             "El localizador de bmw.es da dos opciones a menos de un kilómetro de diferencia: Sitjas Motor, taller autorizado BMW en la calle Quintana 64, a 8,6 km, y Quadis Munich Sabadell, a 9 km. Cualquiera de los dos sirve para una campaña o una reparación en garantía.",
             "Para el resto, el Reglamento (UE) 461/2010 deja claro que revisar el coche en un taller independiente no anula la garantía mientras se siga el plan del fabricante con recambios de calidad equivalente."
         ]},
        {"id": "c33-b20", "h2": "Por la C-33 y la B-20",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona va por la C-33 y la B-20: 29,4 km por carretera, 21,1 en línea recta. Santa Perpètua no está en el Área Metropolitana de Barcelona, así que la recogida del coche que ofrece el taller no la cubre.",
             "A menos de tres kilómetros del centro pasan la AP-7, la C-33, la C-17, la C-59 y varias carreteras del Vallès con matrícula B. Con autopista tan a mano, un diésel tiene fácil hacer de vez en cuando el tramo a ritmo constante que necesita el filtro de partículas para regenerarse."
         ]},
        {"id": "parque-mogoda", "h2": "Más de un turismo por cada dos vecinos",
         "parrafos": [
             "El padrón de 2025 da 26.130 habitantes, un 2,6 % más que en 2015. Idescat contaba 13.675 turismos en 2024 a partir de la DGT: 523 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Hay ITV en Santa Perpètua de Mogoda?",
         "a": "Sí: la estación CIM Vallès (B20), en el polígono Les Minetes, según la Generalitat."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Hay dos en Sabadell casi a la misma distancia: Sitjas Motor (8,6 km) y Quadis Munich (9 km)."},
        {"q": "¿Recogéis el coche aquí?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona, y Santa Perpètua queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "26.130 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Occidental", **F.idescat("082606")},
        {"etiqueta": "Turismos (2024)", "valor": "13.675 · 523 por cada 1.000 hab.", **F.idescat("082606")},
        {"etiqueta": "ITV en el municipio", "valor": "CIM Vallès (B20), pol. Les Minetes", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Sitjas Motor (8,6 km) y Quadis Munich (9 km), Sabadell", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 29,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082606"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Torrelodones
CIUDADES["torrelodones"] = {
    "h1": "Torrelodones, a 852 metros: tu BMW, la A-6 y el especialista de Alcobendas",
    "entradilla": "El centro de Torrelodones está a 852 metros, y eso se nota en invierno. El servicio oficial lo tienes a 6,7 km por la A-6; nuestro taller, a 37,9 km rodeando Madrid por la M-40.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 37.9},
    "secciones": [
        {"id": "invierno-852", "h2": "Lo que pide un coche a 852 metros",
         "parrafos": [
             "Con heladas frecuentes, la batería es el punto débil: en un BMW con arranque y parada automático trabaja mucho, y cuando se cambia hay que registrarla en la centralita para que el sistema de carga la trate como nueva. Si no se registra, dura bastante menos.",
             "El anticongelante conviene medirlo por concentración, no solo por nivel, y en los diésel el precalentamiento tiene que estar en buen estado: una bujía de precalentamiento cansada da la cara la primera mañana fría."
         ]},
        {"id": "movilnorte-a6", "h2": "El concesionario, en la A-6 a 6,7 km",
         "parrafos": [
             "El punto oficial BMW más próximo según bmw.es es Movilnorte, en la A-6, km 23,1, en Las Rozas: 6,7 km por carretera. Las llamadas a revisión del fabricante se atienden en la red de la marca; si te llega una carta de BMW, la cita es con ellos."
         ]},
        {"id": "a6-m40-a1", "h2": "A Alcobendas por la A-6, la M-40 y la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande rodea Madrid por el norte: A-6, M-40 y A-1, 37,9 km por carretera y 23,7 en línea recta. Pregunta por el vehículo de cortesía o por la recogida dentro del área metropolitana de Madrid al pedir cita; los dos están sujetos a disponibilidad.",
             "La ITV oficial más próxima es la de Itevelesa (estación 2832) en la A-6, km 37,6, en Collado Villalba, a 8,6 km según el listado de la Comunidad de Madrid."
         ]},
        {"id": "torrelodones-cifras", "h2": "557 turismos por cada mil vecinos",
         "parrafos": [
             "Torrelodones tenía 25.433 habitantes en 2025, un 10 % más que en 2015, y 14.161 turismos censados ese año (Comunidad de Madrid, a partir de la DGT): 557 por cada 1.000 habitantes, muy por encima de los 388 de Madrid capital."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Torrelodones?",
         "a": "Movilnorte, en la A-6, km 23,1 (Las Rozas), a 6,7 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación oficial más próxima es la de la A-6, km 37,6, en Collado Villalba, a 8,6 km."},
        {"q": "¿Hay que registrar la batería nueva en un BMW?",
         "a": "Sí. Sin registrarla, la centralita la carga como si fuera la vieja y su vida se acorta."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "25.433 habitantes (+10 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "14.161 · 557 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "852 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte, A-6 km 23,1 (Las Rozas) · 6,7 km", **F.bmw},
        {"etiqueta": "ITV oficial más cercana", "valor": "A-6 km 37,6 (Collado Villalba) · 8,6 km", **F.itv_madrid},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 37,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Olesa de Montserrat
CIUDADES["olesa-de-montserrat"] = {
    "h1": "Olesa de Montserrat: no somos el concesionario BMW, somos el especialista a 29 km",
    "entradilla": "Si buscabas el concesionario BMW más cercano a Olesa, está en Terrassa. Nosotros somos un taller independiente en Sant Joan Despí. Te dejamos los datos de los dos para que elijas sabiendo qué hace cada uno.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 29.0},
    "secciones": [
        {"id": "concesionario-terrassa", "h2": "El concesionario más cercano, en Terrassa",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo a Olesa es Quadis Munich, en el carrer Anoia 9 de Terrassa, a 16,8 km por carretera. Es donde se venden coches nuevos y donde se tramitan las reparaciones en garantía de BMW.",
             "Dasercars no es concesionario: es un taller especializado en BMW y MINI, sin vínculo con la red de la marca. Lo decimos claro para que no llames a un número pensando que es otro."
         ]},
        {"id": "c55-a2", "h2": "29 km por la C-55 y la A-2",
         "parrafos": [
             "Desde el centro de Olesa hasta el carrer del Tambor del Bruc hay 29 km por carretera y 24,3 en línea recta: la C-55 baja por el valle del Llobregat y la A-2 lleva hasta Sant Joan Despí. Olesa no está en el Área Metropolitana de Barcelona, y la recogida del coche que ofrece el taller no llega aquí.",
             "Funcionamos con presupuesto escrito: sabes qué se va a hacer antes de que nadie toque el coche, y nada empieza hasta que lo aceptas. También la diagnosis se presupuesta, porque es trabajo técnico con equipo y horas, no una lectura rápida de códigos."
         ]},
        {"id": "itv-viladecavalls", "h2": "La ITV, en Can Trias",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Viladecavalls (B03), en el polígono Can Trias, a 12,5 km. Para Esparreguera, a 2,1 km, la más próxima es otra: la de Sant Andreu de la Barca."
         ]},
        {"id": "olesa-cifras", "h2": "24.966 vecinos en el Baix Llobregat",
         "parrafos": [
             "Olesa tenía 24.966 habitantes en 2025, un 6,1 % más que en 2015, y 11.215 turismos en 2024 según Idescat a partir de la DGT: 449 por cada 1.000 vecinos."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de la zona?",
         "a": "No. El punto oficial más próximo es Quadis Munich, en el carrer Anoia 9 de Terrassa. Nosotros somos Dasercars, taller independiente."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 29 km por la C-55 y la A-2, en Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV desde Olesa?",
         "a": "La más próxima en el registro de la Generalitat es la de Viladecavalls (B03), a 12,5 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "24.966 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("081477")},
        {"etiqueta": "Turismos (2024)", "valor": "11.215 · 449 por cada 1.000 hab.", **F.idescat("081477")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Terrassa · 16,8 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Viladecavalls (B03) · 12,5 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 29 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081477"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Villanueva de la Cañada
CIUDADES["villanueva-de-la-canada"] = {
    "h1": "Villanueva de la Cañada: especialista BMW en Alcobendas, a 45 km por la M-40",
    "entradilla": "No somos un taller del pueblo ni tenemos relación con ningún taller de Villanueva. Somos Dasercars, especialista en BMW y MINI con taller en Alcobendas. Esto es lo que tiene sentido traernos desde aquí y lo que te queda más cerca.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 45.3},
    "secciones": [
        {"id": "no-somos-local", "h2": "Un taller de fuera, para lo que pide especialista",
         "parrafos": [
             "Para una rueda o unas escobillas, un taller de Villanueva o de Brunete te sirve igual. Donde tiene sentido un especialista BMW es en una avería que se repite, en un fallo electrónico sin diagnosticar o en el mantenimiento por plan de marca de un coche que quieres conservar.",
             "Antes de mover el coche, llámanos y cuéntanos qué modelo es, de qué año, cuántos kilómetros lleva y qué hace raro. Muchas veces se puede orientar por teléfono si el viaje compensa."
         ]},
        {"id": "m503-m40", "h2": "45,3 km por la M-503, la M-40 y la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande de Alcobendas sale por la M-503, rodea Madrid por la M-40 y sube por la A-1: 45,3 km por carretera, 31,5 en línea recta. La recogida del coche se limita al área metropolitana de Madrid y está sujeta a disponibilidad; confirma al reservar si tu dirección entra."
         ]},
        {"id": "lo-cercano", "h2": "Lo que tienes más cerca: Majadahonda y Las Rozas",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Movilnorte, en la carretera de El Plantío 62 de Majadahonda, a 20,2 km. Para la inspección, la estación oficial más cercana por carretera es la de TÜV SÜD ATISAE (estación 2816), en el polígono Európolis de Las Rozas, a 16 km según la Comunidad de Madrid."
         ]},
        {"id": "villanueva-crece", "h2": "Casi un 25 % más de vecinos que en 2015",
         "parrafos": [
             "Villanueva de la Cañada pasó de 19.250 habitantes en 2015 a 24.028 en 2025, un 24,8 % más. En 2025 tenía 12.602 turismos según la Comunidad de Madrid a partir de la DGT: 524 por cada 1.000 vecinos.",
             "Con la M-600, la M-521 y la M-503 a menos de tres kilómetros, casi todo se hace en coche por carretera autonómica, con rotondas y cambios de ritmo que cargan embrague y frenos más que un tramo de autovía."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Villanueva de la Cañada?",
         "a": "No. El taller de la red es Dasercars Madrid, en la calle Valgrande 17 de Alcobendas, a 45,3 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación oficial más cercana por carretera es la de TÜV SÜD ATISAE en el polígono Európolis de Las Rozas, a 16 km."},
        {"q": "¿Cuál es el servicio oficial BMW más próximo?",
         "a": "Movilnorte, en la carretera de El Plantío 62 de Majadahonda, a 20,2 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "24.028 habitantes (+24,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "12.602 · 524 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE, Las Rozas · 16 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Movilnorte, Majadahonda · 20,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 45,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Esparreguera
CIUDADES["esparreguera"] = {
    "h1": "Esparreguera: un especialista BMW a 26,9 km, no el taller de la esquina",
    "entradilla": "Esta no es la página de ningún taller de Esparreguera. Es la de Dasercars, taller independiente especializado en BMW y MINI, con nave en Sant Joan Despí. Si tienes uno de estos coches, aquí tienes distancias reales y alternativas.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 26.9},
    "secciones": [
        {"id": "taller-de-fuera", "h2": "Por qué un taller de fuera del pueblo",
         "parrafos": [
             "Un taller generalista resuelve bien lo común. Un especialista de marca tiene sentido cuando el problema es de BMW: una cadena de distribución ruidosa en un N47, una caja automática que da tirones, un aviso de AdBlue con cuenta atrás o un testigo que vuelve después de borrarlo.",
             "Para lo que depende del fabricante —campañas de revisión y reparaciones en garantía—, la cita es con la red oficial. El punto más cercano según bmw.es es Quadis Munich, en el carrer Anoia 9 de Terrassa, a 18,6 km."
         ]},
        {"id": "c55-a2-esparreguera", "h2": "Del núcleo urbano a Sant Joan Despí",
         "parrafos": [
             "Medido desde el centro del núcleo urbano, hasta nuestro taller hay 26,9 km por carretera y 22,7 en línea recta, por la C-55 y la A-2. Esparreguera no pertenece al Área Metropolitana de Barcelona, así que la recogida del coche que ofrece el taller no llega aquí."
         ]},
        {"id": "itv-sant-andreu", "h2": "La ITV, en Sant Andreu de la Barca",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Sant Andreu de la Barca (B21), en la N-II, a 12,1 km. Sant Andreu queda entre Esparreguera y Sant Joan Despí, así que la pre-ITV en el taller y la inspección pueden encajarse en el mismo viaje."
         ]},
        {"id": "esparreguera-cifras", "h2": "513 turismos por cada mil vecinos",
         "parrafos": [
             "El padrón de 2025 da a Esparreguera 22.665 habitantes, un 4,4 % más que en 2015, en un término de 27,4 km². Idescat contaba 11.629 turismos en 2024 a partir de la DGT: 513 por cada 1.000 vecinos, más que en la vecina Olesa (449).",
             "Con la A-2, la B-40 y la C-55 a menos de tres kilómetros, los tramos largos están a mano; un diésel que solo hace recorridos por el pueblo, en cambio, no termina de regenerar el filtro de partículas."
         ]},
    ],
    "faq": [
        {"q": "¿Sois un taller de Esparreguera?",
         "a": "No. Somos Dasercars Barcelona, taller especializado en BMW en Sant Joan Despí, a 26,9 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Sant Andreu de la Barca (B21), a 12,1 km."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI comparte electrónica y motores con BMW y se trabaja con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "22.665 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("080765")},
        {"etiqueta": "Turismos (2024)", "valor": "11.629 · 513 por cada 1.000 hab.", **F.idescat("080765")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Andreu de la Barca (B21) · 12,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Terrassa · 18,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 26,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080765"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Manlleu
CIUDADES["manlleu"] = {
    "h1": "Manlleu: Vic lo tiene casi todo; el especialista BMW está a 88 km",
    "entradilla": "Desde Manlleu, la ITV y el servicio oficial BMW están en Vic, a 8,9 y 12,5 km. Nuestro taller queda a 88,1 km, en Sant Joan Despí. Es mucha distancia y conviene saber cuándo compensa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 88.1},
    "secciones": [
        {"id": "vic-al-lado", "h2": "Todo lo rutinario, en Vic",
         "parrafos": [
             "La estación ITV de Osona (B04) está en el carrer Sant Llorenç Desmunts 22 de Vic, a 8,9 km por carretera según el registro de la Generalitat. El servicio oficial BMW más próximo según bmw.es, Quadis Munich, en el carrer Perot Rocaguinarda 1, también en Vic, a 12,5 km.",
             "Para una inspección, una revisión sencilla o una reparación en garantía no tiene sentido hacer 88 km. Ahí no te vamos a decir otra cosa."
         ]},
        {"id": "cuando-bajar", "h2": "Cuándo sí vale la pena bajar",
         "parrafos": [
             "Cuando el coche está fuera de garantía y lleva una avería que no se ha resuelto: un fallo eléctrico intermitente, una caja automática que no cambia bien, un turbo que pierde presión o un ruido de distribución en un diésel B47 o N47. También para un segundo diagnóstico antes de aceptar una reparación cara.",
             "Desde aquí, la primera conversación debería ser por teléfono: el modelo, el año, los kilómetros y el síntoma bastan para saber si el viaje tiene sentido y, si lo tiene, para que el día que llegues la pieza esté pedida."
         ]},
        {"id": "ruta-c17", "h2": "88 km por la C-17",
         "parrafos": [
             "La ruta sale por la B-522, baja por la C-17, enlaza con la C-33 y termina por la B-20: 88,1 km por carretera, 73,1 en línea recta. La recogida que ofrece el taller se limita al área metropolitana de Barcelona; desde Osona, el coche lo traes tú."
         ]},
        {"id": "manlleu-cifras", "h2": "21.425 vecinos a orillas del Ter",
         "parrafos": [
             "Manlleu tenía 21.425 habitantes en 2025, un 5,9 % más que en 2015, y 10.536 turismos en 2024 según Idescat a partir de la DGT: 492 por cada 1.000 vecinos. El centro está a 461 metros de altitud, y la C-17 y la C-37 pasan a menos de tres kilómetros: buenas carreteras para que un diésel complete la regeneración del filtro de partículas."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Manlleu?",
         "a": "En la estación de Osona (B04), en Vic, a 8,9 km por carretera."},
        {"q": "¿Hay servicio oficial BMW cerca?",
         "a": "Sí: Quadis Munich, en el carrer Perot Rocaguinarda 1 de Vic, a 12,5 km según bmw.es."},
        {"q": "¿Recogéis el coche en Manlleu?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "21.425 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("081120")},
        {"etiqueta": "Turismos (2024)", "valor": "10.536 · 492 por cada 1.000 hab.", **F.idescat("081120")},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 8,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 12,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 88,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081120"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Algete
CIUDADES["algete"] = {
    "h1": "Taller BMW y Algete: el oficial está en el pueblo, el especialista a 18 km",
    "entradilla": "En Algete hay servicio oficial BMW, a 4,2 km del centro, y estación de ITV en el polígono. Nosotros somos otra cosa: un taller independiente especializado en BMW, en Alcobendas. Lo que ofrece cada uno.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 18.0},
    "secciones": [
        {"id": "bymycar-algete", "h2": "El servicio oficial de Algete no somos nosotros",
         "parrafos": [
             "El punto oficial BMW del municipio, según el localizador de bmw.es, es BYmyCAR Madrid, en la calle Tejera 2, carretera de Algete km 3: 4,2 km por carretera desde el centro. Si buscabas su teléfono, no es el de esta página.",
             "Nosotros somos Dasercars, taller independiente. El Reglamento (UE) 461/2010 permite hacer el mantenimiento fuera de la red oficial sin perder la garantía, siempre que se cumplan los intervalos del plan con aceites y recambios de la especificación correcta."
         ]},
        {"id": "itv-sector-8", "h2": "ITV en el polígono Sector 8",
         "parrafos": [
             "El listado oficial de la Comunidad de Madrid incluye una estación dentro del término: la de ITV Barbastro (estación 2818), en la avenida Nicasio Martín 4, polígono Sector 8. No necesitas salir de Algete para la inspección."
         ]},
        {"id": "m106-m100", "h2": "18 km por la M-106, la M-100 y la A-1",
         "parrafos": [
             "La ruta hasta la calle Valgrande va por la M-106 y la M-100 hasta la A-1: 18 km por carretera, 14,6 en línea recta.",
             "Si el trabajo dura más de un día, pregunta por el vehículo de cortesía, o por la recogida y entrega dentro del área metropolitana de Madrid; las dos cosas dependen de disponibilidad."
         ]},
        {"id": "algete-cifras", "h2": "604 turismos por cada mil vecinos",
         "parrafos": [
             "Algete tenía 21.144 habitantes en 2025, un 4,9 % más que en 2015. La Comunidad de Madrid, a partir de la DGT, contaba 12.767 turismos ese año: 604 por cada 1.000 vecinos, frente a 388 en Madrid capital.",
             "El centro está a 718 metros de altitud y la M-103 y la M-106 pasan a menos de tres kilómetros. Con tanto trayecto corto entre urbanizaciones y polígono, en un diésel conviene vigilar el filtro de partículas: si el aviso de regeneración aparece a menudo, no es normal y hay que mirar por qué no completa el ciclo."
         ]},
    ],
    "faq": [
        {"q": "¿Sois el concesionario BMW de Algete?",
         "a": "No. El servicio oficial es BYmyCAR Madrid, en la calle Tejera 2. Nosotros somos un taller independiente en Alcobendas."},
        {"q": "¿Hay ITV en Algete?",
         "a": "Sí: la estación 2818, en la avenida Nicasio Martín 4, polígono Sector 8."},
        {"q": "¿Pierdo la garantía si reviso el coche con vosotros?",
         "a": "No, si se respeta el plan de mantenimiento del fabricante."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "21.144 habitantes (+4,9 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "12.767 · 604 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV en el municipio", "valor": "ITV Barbastro (2818), av. Nicasio Martín 4", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid, c/ Tejera 2 · 4,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 18 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Sant Just Desvern
CIUDADES["sant-just-desvern"] = {
    "h1": "Sant Just Desvern: el taller especialista BMW está a 3,9 km, en el municipio vecino",
    "entradilla": "Entre el centro de Sant Just y nuestra nave de Sant Joan Despí hay 2 km en línea recta. Pocas páginas de la red pueden decir algo así. Además, la ITV está dentro del término y el servicio oficial, en Sant Boi.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 3.9},
    "secciones": [
        {"id": "al-lado", "h2": "3,9 km por carretera",
         "parrafos": [
             "Dasercars Barcelona está en el carrer del Tambor del Bruc 3, en Sant Joan Despí: 3,9 km por carretera desde el centro de Sant Just. Es una distancia que permite dejar el coche por la mañana sin organizar el día alrededor del taller.",
             "Sant Just y Sant Joan Despí forman parte del Área Metropolitana de Barcelona, así que también tienes la recogida y entrega del coche y el vehículo de cortesía para trabajos largos, sujetos a disponibilidad."
         ]},
        {"id": "itv-la-riera", "h2": "La ITV, en la avinguda de la Riera",
         "parrafos": [
             "El registro de la Generalitat sitúa la estación B05 dentro del municipio, en la avinguda de la Riera 19-21, polígono industrial número 1. Con el taller a 3,9 km y la inspección en el pueblo, una pre-ITV en el taller y la cita en la estación caben en la misma semana."
         ]},
        {"id": "oficial-sant-boi", "h2": "Servicio oficial en Sant Boi, a 8,7 km",
         "parrafos": [
             "El punto oficial BMW más próximo según bmw.es es Barcelona Premium, en la carretera del Prat 15 de Sant Boi de Llobregat, a 8,7 km. Para un coche en garantía, el mantenimiento puede hacerse en un taller independiente sin perderla, siempre que se respete el plan de BMW: lo establece el Reglamento (UE) 461/2010."
         ]},
        {"id": "sant-just-crece", "h2": "Un 26,5 % más de vecinos y pocos coches por cabeza",
         "parrafos": [
             "Sant Just pasó de 16.631 habitantes en 2015 a 21.037 en 2025. Idescat contaba 8.324 turismos en 2024 a partir de la DGT: 396 por cada 1.000 vecinos, una proporción baja para el Baix Llobregat.",
             "Muchos de esos coches hacen trayectos cortos hacia Barcelona por la B-23 o la N-340, a menos de tres kilómetros. En un BMW diésel ese uso dificulta la regeneración del filtro de partículas; si se enciende el testigo, un trayecto largo a régimen constante suele ser el primer remedio."
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está vuestro taller respecto a Sant Just?",
         "a": "En el carrer del Tambor del Bruc 3 de Sant Joan Despí, a 3,9 km por carretera."},
        {"q": "¿Recogéis el coche en Sant Just Desvern?",
         "a": "Sí, el municipio está en el área metropolitana de Barcelona. Sujeto a disponibilidad."},
        {"q": "¿Hay ITV en Sant Just?",
         "a": "Sí: la estación B05, en la avinguda de la Riera 19-21, según la Generalitat."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "21.037 habitantes (+26,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Baix Llobregat", **F.idescat("082212")},
        {"etiqueta": "Turismos (2024)", "valor": "8.324 · 396 por cada 1.000 hab.", **F.idescat("082212")},
        {"etiqueta": "ITV en el municipio", "valor": "Sant Just Desvern (B05), av. de la Riera", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Barcelona Premium, Sant Boi · 8,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 3,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082212"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Calella
CIUDADES["calella"] = {
    "h1": "Calella: especialista BMW a 66,8 km, ITV en Blanes y concesionario en Mataró",
    "entradilla": "Esta página no es la de un taller de Calella. Es la de Dasercars, especialista independiente en BMW y MINI, en Sant Joan Despí. Te damos lo que tienes cerca y por qué, a veces, compensa bajar.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 66.8},
    "secciones": [
        {"id": "no-es-local", "h2": "No somos el taller de Calella",
         "parrafos": [
             "Si buscabas un taller dentro del municipio, no somos nosotros: nuestro único taller en Cataluña está en el Baix Llobregat, a 66,8 km por la C-32 y la B-20. Para un cambio de neumáticos o una revisión sencilla, un taller del Maresme es lo razonable.",
             "Para una avería propia de BMW sí puede compensar el viaje. Y si vienes, sabes a qué atenerte: el presupuesto te llega por escrito y no se toca nada sin que lo apruebes."
         ]},
        {"id": "cerca-de-calella", "h2": "Lo cercano: Blanes para la ITV, Mataró para la marca",
         "parrafos": [
             "La estación de ITV más próxima por carretera en el registro de la Generalitat es la de Blanes (G07), en la avinguda de l'Estació 47, a 13,3 km. El servicio oficial BMW más cercano según bmw.es es Pruna Motor, en la Via Sèrgia 2 de Mataró, a 29,6 km."
         ]},
        {"id": "primera-linea", "h2": "Un municipio en primera línea de mar",
         "parrafos": [
             "El centro de Calella está a 0,9 km de la costa, a 5 metros sobre el nivel del mar. La humedad salina se acumula en los bajos, los pasos de rueda y las grapas de las protecciones. Un manguerazo con agua dulce bajo el coche al final del verano evita buena parte de la corrosión.",
             "Si el BMW pasa temporadas parado, la batería se descarga más rápido de lo que parece: los sistemas electrónicos siguen consumiendo. Un mantenedor de carga o arrancarlo y moverlo cada pocos días ayuda."
         ]},
        {"id": "calella-cifras", "h2": "356 turismos por cada mil habitantes",
         "parrafos": [
             "Calella tenía 20.864 vecinos en 2025, un 14,5 % más que en 2015, en apenas 8 km². Idescat contaba 7.438 turismos en 2024 a partir de la DGT: 356 por cada 1.000 habitantes, menos que en Sitges (378) o en Pineda de Mar (464)."
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en Calella?",
         "a": "No. El taller de la red es Dasercars Barcelona, en Sant Joan Despí, a 66,8 km."},
        {"q": "¿Dónde paso la ITV desde Calella?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Blanes (G07), a 13,3 km."},
        {"q": "¿Recogéis el coche en Calella?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "20.864 habitantes (+14,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Maresme", **F.idescat("080351")},
        {"etiqueta": "Turismos (2024)", "valor": "7.438 · 356 por cada 1.000 hab.", **F.idescat("080351")},
        {"etiqueta": "Distancia a la costa", "valor": "unos 0,9 km desde el centro", **COSTA},
        {"etiqueta": "ITV más cercana", "valor": "Blanes (G07) · 13,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 29,6 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080351"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}
