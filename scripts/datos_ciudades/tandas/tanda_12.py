# Tanda 12: Tavèrnoles, Sant Martí Sesgueioles, Copons, Lluçà, l'Espunyola, Vallcebre,
# Argençola, Berzosa del Lozoya, Mura, Sant Julià de Cerdanyola, Sora,
# Santa Cecília de Voltregà, Calonge de Segarra, Viver i Serrateix y Orpí.
# Ninguna ciudad de la tanda está en la lista de exclusiones del coordinador.
#
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con
#   python3 scripts/datos_ciudades/piloto/aplicar.py tanda_12
# y las metaDescription nuevas (todas las ciudades de la tanda tienen 0 impresiones
# en GSC; solo se reescriben las que prometían recogida a domicilio, ISTA,
# «diagnosis oficial», «presupuesto gratis», garantía por escrito o superlativos) con
#   python3 scripts/datos_ciudades/tandas/tanda_12.py
# Los metaTitle no se tocan.
#
# Sant Julià de Cerdanyola: el fichero de datos da como servicio oficial más cercano
# Quadis Munich (Vic) a 71,1 km, cuando Vallcebre, a 6,4 km, tiene Sant Fruitós de
# Bages a 66,7 km. Parece que no es el más cercano por carretera: no se publica.
import json
import sys
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(_AQUI.parent / "piloto"))
sys.path.insert(0, str(_AQUI.parent))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}

# ---------------------------------------------------------------- Tavèrnoles
CIUDADES["tavernoles"] = {
    "h1": "Tavèrnoles: ITV y servicio oficial BMW en Vic, taller especialista a 89 km",
    "entradilla": "Para un BMW o un MINI de Tavèrnoles, casi todo lo cotidiano se resuelve en Vic. El taller especialista de la red queda mucho más abajo, en Sant Joan Despí; aquí explicamos cuándo merece la pena ese viaje.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 89.2},
    "secciones": [
        {"id": "vic-al-lado", "h2": "Vic, la referencia para la inspección y para la marca",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22 de Vic: 6 km desde el núcleo urbano de Tavèrnoles. En la misma ciudad está el punto de servicio oficial que da el localizador de bmw.es, Quadis Munich, en la calle Perot Rocaguinarda 1, a 9,8 km.",
             "Para la inspección o una campaña de revisión que convoque BMW, no tiene sentido bajar a Barcelona.",
         ]},
        {"id": "c25-c17-b20", "h2": "De la C-25 a la B-20: 89,2 km hasta Sant Joan Despí",
         "parrafos": [
             "La ruta que calcula OpenStreetMap sale por la BV-5213, toma la C-25 —cuyo trazado pasa a unos 3 km del pueblo—, baja por la C-17 y la C-33 y termina en la B-20, junto a la nave del carrer del Tambor del Bruc. En total, 89,2 km por carretera para 69,3 en línea recta.",
             "Es un viaje para algo concreto: una avería electrónica que nadie en la comarca ha cerrado, un diésel con problemas en la recirculación de gases o un segundo diagnóstico antes de aceptar un cambio de motor.",
             "Tavèrnoles no forma parte del área metropolitana de Barcelona, de modo que la recogida del coche que ofrece el taller no llega hasta aquí.",
         ]},
        {"id": "pueblo-y-coches", "h2": "354 vecinos y 242 turismos",
         "parrafos": [
             "El padrón de 2025 da a Tavèrnoles 354 habitantes, frente a 319 en 2015 (un 11 % más). Idescat, con datos de la DGT, contaba 242 turismos en 2024: 684 por cada 1.000 vecinos. En un término de 18,78 km² con el casco a 537 metros, sin coche se hace poco.",
             "Un coche que hace a diario los kilómetros justos hasta Vic sufre arranques en frío y una batería que casi nunca termina de cargarse; en los BMW con arranque y parada automático, es lo primero que conviene revisar.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Tavèrnoles?",
         "a": "En ITV Osona (B04), en Vic, a 6 km: es la estación más próxima por carretera según la Generalitat."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 9,8 km según bmw.es."},
        {"q": "¿Hay recogida del coche en Tavèrnoles?",
         "a": "No. Ese servicio se limita al área metropolitana de Barcelona y, además, está sujeto a disponibilidad."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "354 habitantes (+11 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082750")},
        {"etiqueta": "Turismos (2024)", "valor": "242 · 684 por cada 1.000 hab.", **F.idescat("082750")},
        {"etiqueta": "ITV más cercana", "valor": "ITV Osona (B04), Vic · 6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 9,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 89,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082750"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sant Martí Sesgueioles
CIUDADES["sant-marti-sesgueioles"] = {
    "h1": "BMW en Sant Martí Sesgueioles: ITV en Igualada y taller especialista a 80,7 km",
    "entradilla": "Sant Martí Sesgueioles cabe en 3,87 km² y tiene 353 vecinos. Para mantener un BMW o un MINI desde aquí hay que salir del término para todo: la ITV y el taller especialista quedan hacia Barcelona, y el servicio oficial, en sentido contrario, hacia Tàrrega.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 80.7},
    "secciones": [
        {"id": "tres-direcciones", "h2": "Tres destinos, ninguno en el pueblo",
         "parrafos": [
             "Según el registro de la Generalitat, la estación de ITV más próxima por carretera es la de Igualada (B12), en el polígono Les Comes, carrer dels Països Baixos 18: 29,9 km. El punto de servicio oficial que da el localizador de bmw.es está en Tàrrega: Unicars Ponent, en el carrer de la Conca de Barberà, nave 6, a 38 km.",
             "El taller de la red, Dasercars Barcelona, queda a 80,7 km por la BV-1001, la C-1412a y la A-2, en Sant Joan Despí; en línea recta son 60,3. Ninguno de los tres está cerca, así que lo sensato es agrupar: si el coche baja al taller por una avería, que vuelva con la pre-ITV hecha.",
         ]},
        {"id": "menos-vecinos", "h2": "De 378 a 353 vecinos en diez años",
         "parrafos": [
             "El padrón registraba 378 habitantes en 2015 y 353 en 2025, un 6,6 % menos. Idescat, a partir de la DGT, contaba 252 turismos en 2024: 714 por cada 1.000 vecinos. Con un término tan pequeño, casi cualquier desplazamiento sale de él, y se hace en coche.",
             "Copons, a 6,2 km en línea recta, tiene un término casi cinco veces mayor. Aquí casi todos los kilómetros del coche son de carretera.",
         ]},
        {"id": "c1412a", "h2": "La C-1412a y la BV-1001, a la puerta",
         "parrafos": [
             "Las dos carreteras con las que empieza la ruta al taller, la BV-1001 y la C-1412a, pasan a menos de tres kilómetros del centro. Son vías secundarias, con cruces y rotondas; el tramo largo de verdad empieza al enlazar con la A-2.",
             "Para un diésel BMW, ese tramo de autovía es el que permite completar la regeneración del filtro de partículas. Si el coche solo hace trayectos cortos por la comarca y el aviso del filtro aparece a menudo, conviene revisarlo antes de que la centralita limite la potencia.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en el Anoia?",
         "a": "No. El más cercano de la red es Dasercars Barcelona, en Sant Joan Despí, a 80,7 km por la A-2."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Igualada (B12), en el polígono Les Comes, a 29,9 km: es la estación más próxima por carretera según la Generalitat."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "En Tàrrega: Unicars Ponent, a 38 km según el localizador de bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "353 habitantes (−6,6 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("082286")},
        {"etiqueta": "Superficie del término", "valor": "3,87 km²", **F.idescat("082286")},
        {"etiqueta": "Turismos (2024)", "valor": "252 · 714 por cada 1.000 hab.", **F.idescat("082286")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 29,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent (Tàrrega) · 38 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 80,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082286"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Copons
CIUDADES["copons"] = {
    "h1": "Copons y la A-2: tu BMW a 65,6 km del taller especialista de Sant Joan Despí",
    "entradilla": "La A-2 pasa a menos de tres kilómetros de Copons, y eso simplifica mucho llevar un BMW o un MINI al taller: casi todo el trayecto hasta Sant Joan Despí es autovía. Lo que no está tan cerca es el servicio oficial.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 65.6},
    "secciones": [
        {"id": "casi-todo-autovia", "h2": "65,6 kilómetros, casi todos de autovía",
         "parrafos": [
             "Desde el núcleo urbano de Copons, la ruta sale por la C-1412a y enlaza enseguida con la A-2, que lleva hasta el Baix Llobregat: 65,6 km por carretera y 54,4 en línea recta hasta la nave de Dasercars Barcelona, en el carrer del Tambor del Bruc 3.",
             "Es una distancia media. Compensa para lo que exige conocer bien la marca —un fallo eléctrico que va y viene, una fuga de aceite en un diésel de la familia N47 o B47, un coche que alguien ha intentado arreglar sin éxito— y no tanto para cambiar unas pastillas. Copons no está en el área metropolitana de Barcelona: la recogida del taller no llega aquí.",
         ]},
        {"id": "itv-igualada", "h2": "La inspección, a 14,8 km en Igualada",
         "parrafos": [
             "La estación más próxima por carretera según la Generalitat es la de Igualada (B12), en el polígono Les Comes. Con menos de quince kilómetros hasta allí, no hace falta combinarla con nada: se pasa cuando toque.",
         ]},
        {"id": "oficial-lejos", "h2": "El servicio oficial, a 41,5 km en Tàrrega",
         "parrafos": [
             "El localizador de bmw.es sitúa el punto oficial más cercano en Tàrrega: Unicars Ponent, a 41,5 km por carretera. Es algo menos de lo que hay hasta nuestro taller, pero no mucho menos.",
             "Para el mantenimiento, el Reglamento (UE) 461/2010 deja elegir taller sin perder la garantía del fabricante, con una condición: que se sigan los intervalos y las especificaciones del plan de mantenimiento. Las campañas que convoque BMW, eso sí, van por la red oficial.",
         ]},
        {"id": "copons-crece", "h2": "Un 14,7 % más de vecinos que en 2015",
         "parrafos": [
             "Copons tenía 307 habitantes en 2015 y 352 en 2025. En 2024 había 187 turismos según Idescat, a partir de la DGT: 531 por cada 1.000 vecinos, en un término de 18,66 km² con el pueblo a 432 metros.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué distancia hay de Copons a vuestro taller?",
         "a": "65,6 km por la C-1412a y la A-2 hasta Sant Joan Despí."},
        {"q": "¿Puedo hacer las revisiones fuera del concesionario sin perder la garantía?",
         "a": "Sí, si se cumplen los intervalos y las especificaciones del plan de mantenimiento del fabricante."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. Comparte motores y electrónica con BMW y se diagnostica con el mismo equipo."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "352 habitantes (+14,7 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("080713")},
        {"etiqueta": "Turismos (2024)", "valor": "187 · 531 por cada 1.000 hab.", **F.idescat("080713")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 14,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent (Tàrrega) · 41,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 65,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080713"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Lluçà
CIUDADES["lluca"] = {
    "h1": "Lluçà, en el Lluçanès: tu BMW a 116,6 km del taller y la ITV en Berga",
    "entradilla": "En Lluçà viven cinco personas por kilómetro cuadrado y no hay ninguna carretera principal a menos de tres kilómetros del núcleo. Para un BMW, eso quiere decir carreteras locales a diario y un taller especialista muy lejos. Vamos a lo práctico.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 116.6},
    "secciones": [
        {"id": "berga-y-vic", "h2": "ITV hacia Berga, servicio oficial hacia Vic",
         "parrafos": [
             "Dos gestiones, dos direcciones. La estación de ITV más próxima por carretera a Lluçà, según el registro de la Generalitat, es la de Berga (B13), en el polígono La Valldan, a 29,4 km. El servicio oficial BMW está en Vic: Quadis Munich, calle Perot Rocaguinarda 1, a 32,8 km según bmw.es.",
         ]},
        {"id": "cuando-no-merece", "h2": "116,6 kilómetros: cuándo no merece la pena",
         "parrafos": [
             "La ruta hasta Sant Joan Despí va por la BV-4341 hasta la C-62, baja por la C-16 y entra por la B-20: 116,6 km por carretera, 76,3 en línea recta. Para un cambio de aceite, unos neumáticos o unos frenos, ese viaje no se justifica: un taller del Lluçanès o de Osona lo hace igual de bien.",
             "Sí se justifica cuando el problema es de los que exigen conocer la marca a fondo: una centralita que pierde la codificación, una caja automática con cambios bruscos, un ruido de distribución en un diésel. Antes de mover el coche, cuéntalo por teléfono con todo el detalle que puedas; a veces el viaje se descarta en la misma llamada.",
         ]},
        {"id": "lluca-en-cifras", "h2": "281 vecinos en casi 53 km²",
         "parrafos": [
             "El padrón contaba 280 habitantes en 2015 y 281 en 2025: la población no se ha movido. El término mide 52,98 km² y el núcleo está a 745 metros. Idescat, con datos de la DGT, registraba 167 turismos en 2024, 594 por cada 1.000 vecinos.",
             "Sin vías principales cerca, casi todos los kilómetros del día a día se hacen por carreteras locales, con curvas y cambios de rasante. Ahí trabajan más la suspensión y los frenos que en autovía: un golpe seco al pasar un bache o una vibración al frenar en bajada son avisos que no conviene dejar para más adelante.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Lluçà?",
         "a": "En la estación de Berga (B13), a 29,4 km: es la más próxima por carretera según la Generalitat."},
        {"q": "¿Tenéis taller en el Lluçanès?",
         "a": "No. El de la red más cercano es Dasercars Barcelona, en Sant Joan Despí, a 116,6 km."},
        {"q": "¿Recogéis el coche en Lluçà?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "281 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Lluçanès", **F.idescat("081094")},
        {"etiqueta": "Superficie del término", "valor": "52,98 km²", **F.idescat("081094")},
        {"etiqueta": "Turismos (2024)", "valor": "167 · 594 por cada 1.000 hab.", **F.idescat("081094")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 29,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 32,8 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081094"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- l'Espunyola
CIUDADES["l-espunyola"] = {
    "h1": "L'Espunyola: un BMW a 803 metros, con la ITV a 8,9 km y el taller a 112,4",
    "entradilla": "En l'Espunyola hay casi ocho turismos por cada diez vecinos, una proporción que casi triplica la de Barcelona ciudad (281 por cada 1.000). La ITV de Berga queda cerca; nuestro taller, en Sant Joan Despí, bastante lejos.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 112.4},
    "secciones": [
        {"id": "coche-imprescindible", "h2": "203 turismos para 260 vecinos",
         "parrafos": [
             "Idescat, a partir de la DGT, contaba 203 turismos en l'Espunyola en 2024; el padrón de 2025 da 260 habitantes, ocho más que en 2015, cuando eran 252. Son 781 turismos por cada 1.000 vecinos en un término de 35,46 km²: sin coche no se llega a casi nada.",
         ]},
        {"id": "803-metros", "h2": "Por encima de los 800 metros",
         "parrafos": [
             "El núcleo está a 803 metros según Idescat. En invierno, lo primero que acusa el frío en un BMW moderno es la batería: entre el arranque y parada, la calefacción de asientos y lunas y la electrónica, la demanda es alta, y una batería al final de su vida avisa poco. Cuando se cambia, hay que registrarla en la centralita para que el alternador la cargue como corresponde.",
             "El anticongelante se comprueba por concentración, no solo por nivel. Y si el diésel tarda en arrancar las mañanas frías, los calentadores son los primeros sospechosos.",
         ]},
        {"id": "c26-berga", "h2": "La C-26 lleva a Berga y a la C-16",
         "parrafos": [
             "La C-26 pasa a menos de tres kilómetros del pueblo y es el inicio de la ruta al taller: C-26 hasta la C-16 y después la B-20, 112,4 km por carretera (80,1 en línea recta) hasta Sant Joan Despí. Por el camino queda Berga, con la estación de ITV (B13) del polígono La Valldan a 8,9 km, la más próxima por carretera en el registro de la Generalitat.",
             "El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 51,2 km. Nuestro taller compensa cuando se trata de una avería que no se ha resuelto en el Berguedà; para la rutina, no. Y la recogida del taller no llega a l'Espunyola: se limita al área metropolitana.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Berga (B13), en el polígono La Valldan, a 8,9 km por carretera."},
        {"q": "¿Qué conviene revisar antes del invierno?",
         "a": "La batería, la concentración del anticongelante y, en los diésel, los calentadores. Si cambias la batería, hay que registrarla en el coche."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 112,4 km, en Sant Joan Despí, por la C-26, la C-16 y la B-20."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "260 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080787")},
        {"etiqueta": "Altitud", "valor": "803 m", **F.idescat("080787")},
        {"etiqueta": "Turismos (2024)", "valor": "203 · 781 por cada 1.000 hab.", **F.idescat("080787")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 8,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 51,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 112,4 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080787"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Vallcebre
CIUDADES["vallcebre"] = {
    "h1": "Vallcebre, a 1.123 metros: lo que pide un BMW en la montaña del Berguedà",
    "entradilla": "El núcleo de Vallcebre está a 1.123 metros y el taller especialista de la red, a 127,9 km. Con esas dos cifras, esta página va de lo que puedes prevenir aquí arriba y de cuándo tiene sentido bajar hasta Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 127.9},
    "secciones": [
        {"id": "frio-y-bajadas", "h2": "Frío y bajadas largas",
         "parrafos": [
             "A más de mil metros, las heladas forman parte del invierno. Las comprobaciones que más rinden antes de que lleguen: batería (en un BMW, la nueva se registra en la centralita), anticongelante con la mezcla adecuada y neumáticos con dibujo suficiente.",
             "Para salir del pueblo hacia la C-16 se baja por la B-400 y la B-401, carreteras de montaña con desnivel. En un descenso largo los frenos se calientan, y un líquido viejo, cargado de humedad, hierve antes: el pedal se vuelve esponjoso justo cuando más falta hace. Bajar con una marcha corta alivia discos y pastillas.",
         ]},
        {"id": "berga-28-km", "h2": "ITV en Berga, a 28,7 km",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Berga (B13), en el polígono La Valldan, a 28,7 km. El servicio oficial BMW más cercano según bmw.es está más abajo, en Sant Fruitós de Bages: Quadis Munich, en la carretera de Manresa a Berga, km 34,5, a 66,7 km.",
         ]},
        {"id": "bajar-a-barcelona", "h2": "127,9 km hasta el taller: solo para lo que lo merece",
         "parrafos": [
             "La ruta completa va por la B-401, la B-400, la C-16 y la B-20: 127,9 km por carretera y 95,4 en línea recta hasta el carrer del Tambor del Bruc. Es demasiado para una revisión; tiene sentido cuando el BMW arrastra una avería que no se ha resuelto en la comarca y necesita diagnosis específica de la marca.",
             "En esos casos, lo que más ahorra es una llamada previa con el modelo, el año y el síntoma: cuándo aparece y qué testigos se encienden. La recogida del taller no llega hasta aquí.",
         ]},
        {"id": "vallcebre-en-cifras", "h2": "260 vecinos y 187 turismos",
         "parrafos": [
             "El padrón da 260 habitantes en 2025 (255 en 2015). Idescat, con datos de la DGT, contaba 187 turismos en 2024: 719 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Vallcebre?",
         "a": "En Berga (B13), a 28,7 km por carretera."},
        {"q": "¿Por qué se cambia el líquido de frenos aunque el coche haga pocos kilómetros?",
         "a": "Porque absorbe humedad con el tiempo y pierde eficacia cuando se calienta en bajadas largas; el plan de mantenimiento lo cambia por fecha."},
        {"q": "¿Tenéis taller en el Berguedà?",
         "a": "No. El de la red más cercano está en Sant Joan Despí, a 127,9 km."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "260 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("082938")},
        {"etiqueta": "Altitud", "valor": "1.123 m", **F.idescat("082938")},
        {"etiqueta": "Turismos (2024)", "valor": "187 · 719 por cada 1.000 hab.", **F.idescat("082938")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 28,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 66,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 127,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082938"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Argençola
CIUDADES["argencola"] = {
    "h1": "Argençola: un BMW entre Tàrrega e Igualada, con el taller especialista a 74,3 km",
    "entradilla": "Desde Argençola, la A-2 queda a menos de tres kilómetros. Hacia el oeste está el servicio oficial BMW más próximo; hacia el este, la ITV y, al final de la autovía, el taller de la red en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 74.3},
    "secciones": [
        {"id": "bv2231-a2", "h2": "Por la BV-2231 y la A-2",
         "parrafos": [
             "La ruta que calcula OpenStreetMap sale del pueblo por la BV-2231 y sigue por la A-2 hasta el final: 74,3 km por carretera, 57,7 en línea recta hasta Dasercars Barcelona. Al no estar en el área metropolitana, la recogida que ofrece el taller no llega a Argençola.",
             "Es media distancia: para un mantenimiento de rutina hay talleres más cerca; para un diagnóstico que no ha salido en otro sitio o un trabajo de motor en un diésel N47 o N57, sí compensa el viaje.",
         ]},
        {"id": "tarrega-oficial", "h2": "El servicio oficial, a 32,4 km en Tàrrega",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial más próximo es Unicars Ponent, en el carrer de la Conca de Barberà de Tàrrega, a 32,4 km. Si te llega una carta de llamada a revisión, esa cita es con ellos.",
             "Todo lo demás —aceite, filtros, frenos, averías fuera de garantía— puedes hacerlo donde prefieras. Con nosotros, el trabajo se presupuesta por escrito y no se empieza nada que no hayas aprobado.",
         ]},
        {"id": "itv-hacia-igualada", "h2": "ITV: Igualada, a 23,5 km",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Igualada (B12), en el polígono Les Comes, a 23,5 km y en el mismo sentido que el taller. Si el coche baja a Sant Joan Despí por otra cosa, la pre-ITV puede hacerse allí y la inspección, a la vuelta.",
         ]},
        {"id": "argencola-en-cifras", "h2": "245 vecinos en 47 km²",
         "parrafos": [
             "Argençola ha pasado de 223 habitantes en 2015 a 245 en 2025, un 9,9 % más, en un término de 47,09 km² con 5 habitantes por km². El núcleo está a 716 metros. Idescat contaba 129 turismos en 2024 a partir de la DGT: 527 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Argençola?",
         "a": "En Tàrrega: Unicars Ponent, a 32,4 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Igualada (B12), a 23,5 km: es la estación más próxima por carretera según la Generalitat."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "74,3 km por la BV-2231 y la A-2, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "245 habitantes (+9,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("080082")},
        {"etiqueta": "Turismos (2024)", "valor": "129 · 527 por cada 1.000 hab.", **F.idescat("080082")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 23,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent (Tàrrega) · 32,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 74,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080082"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Berzosa del Lozoya
CIUDADES["berzosa-del-lozoya"] = {
    "h1": "Berzosa del Lozoya: servicio oficial BMW y taller especialista, casi a la misma distancia",
    "entradilla": "Desde Berzosa del Lozoya, el servicio oficial BMW más cercano está a 70,3 km y nuestro taller, a 72,3. Con dos kilómetros de diferencia, la distancia no decide: decide lo que necesita el coche.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 72.3},
    "secciones": [
        {"id": "algete-o-alcobendas", "h2": "Algete o Alcobendas",
         "parrafos": [
             "El localizador de bmw.es da como punto oficial más próximo BYmyCAR Madrid, en la calle Tejera 2, carretera de Algete, km 3: 70,3 km por carretera. Dasercars Madrid está en la calle Valgrande 17 de Alcobendas, a 72,3 km por la M-127, la M-135 y la A-1 (49,5 km en línea recta).",
             "La garantía del fabricante no obliga a revisar en el concesionario: el Reglamento (UE) 461/2010 permite hacerlo en un taller independiente si se respetan los intervalos y las especificaciones del plan de mantenimiento. En Dasercars, además, la diagnosis se presupuesta antes de empezar.",
         ]},
        {"id": "itv-a1-km-66", "h2": "La ITV, en la A-1 a la altura de Lozoyuela",
         "parrafos": [
             "La estación oficial más próxima por carretera es la de TÜV SÜD ATISAE (estación 2812), en la A-1, km 66, en el término de Lozoyuela-Navas-Sieteiglesias: 20,5 km según el listado de la Comunidad de Madrid. Si el coche baja al taller por otro motivo, la pre-ITV puede hacerse allí y la inspección, después.",
         ]},
        {"id": "a-1077-metros", "h2": "A unos 1.077 metros",
         "parrafos": [
             "El casco urbano está a unos 1.077 metros según el modelo de elevación Copernicus. En la sierra, el invierno castiga sobre todo la batería, el refrigerante y los neumáticos. En un BMW con muchos consumidores eléctricos, una batería que flojea suele avisar la primera mañana de helada, y la nueva hay que registrarla para que el coche la cargue bien.",
         ]},
        {"id": "berzosa-en-cifras", "h2": "242 vecinos, un 19,8 % más que en 2015",
         "parrafos": [
             "El padrón pasó de 202 habitantes en 2015 a 242 en 2025, en un término de 14,5 km². La Comunidad de Madrid, a partir de la DGT, contaba 116 turismos en 2025: 479 por cada 1.000 vecinos, bastantes menos que en El Atazar, a 7 km, donde son 764.",
             "Berzosa queda fuera del área metropolitana de Madrid, y la recogida y entrega que ofrece el taller no llega hasta aquí: el coche lo bajas tú.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué me queda más cerca, el concesionario o vuestro taller?",
         "a": "Prácticamente igual: BYmyCAR, en Algete, a 70,3 km, y Dasercars, en Alcobendas, a 72,3 km."},
        {"q": "¿Dónde paso la ITV desde Berzosa?",
         "a": "En la estación de TÜV SÜD ATISAE de la A-1, km 66, a 20,5 km."},
        {"q": "¿Reparáis MINI?",
         "a": "Sí. MINI comparte electrónica y buena parte de los motores con BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "242 habitantes (+19,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "116 · 479 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 1.077 m", **F.copernicus},
        {"etiqueta": "ITV más cercana", "valor": "A-1 km 66 (Lozoyuela) · 20,5 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "BYmyCAR Madrid (Algete) · 70,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 72,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.cartociudad_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Mura
CIUDADES["mura"] = {
    "h1": "Mura: un BMW a 59 km del taller especialista, por la B-40 y la C-16",
    "entradilla": "Ninguna carretera principal pasa a menos de tres kilómetros de Mura, y aun así el taller de la red queda a 59 km: la B-40 acerca bastante Sant Joan Despí. La ITV y el servicio oficial BMW, hacia Manresa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 59.0},
    "secciones": [
        {"id": "b40", "h2": "La B-40 acorta el camino",
         "parrafos": [
             "La ruta sale por la BV-1223 y la BV-1221, toma la B-40 y enlaza con la C-16 y la B-20 hasta el carrer del Tambor del Bruc de Sant Joan Despí: 59 km por carretera, 37,9 en línea recta.",
             "A esa distancia, llevar el coche a un especialista ya es razonable también para el mantenimiento por plan de marca, no solo para averías raras. Mura no forma parte del área metropolitana, de modo que la recogida del taller no llega; el coche lo traes tú.",
         ]},
        {"id": "manresa-bufalvent", "h2": "ITV en el polígono Bufalvent de Manresa",
         "parrafos": [
             "La estación más próxima por carretera según la Generalitat es la de Manresa (B06), en el carrer Esteve Terrades 2-4 del polígono Bufalvent, a 16,8 km. El punto oficial BMW que da el localizador de bmw.es está a 21,6 km: Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages.",
         ]},
        {"id": "carreteras-locales", "h2": "Carreteras locales hasta la autovía",
         "parrafos": [
             "Hasta llegar a la B-40, todo es carretera local, con curvas y desnivel. Es un uso que pide atención a frenos, neumáticos y amortiguadores, y en el que un diésel pocas veces mantiene la temperatura y el régimen que necesita el filtro de partículas para limpiarse.",
             "Si el aviso del filtro se enciende a menudo, aprovecha el tramo de B-40 y C-16 para que termine la regeneración; si no se apaga, que lo revise un taller antes de que el coche entre en modo de emergencia.",
         ]},
        {"id": "mura-en-cifras", "h2": "235 vecinos, un 15,8 % más que en 2015",
         "parrafos": [
             "Mura tenía 203 habitantes en 2015 y 235 en 2025, en un término de 47,79 km² con el núcleo a 454 metros. Idescat, a partir de la DGT, contaba 120 turismos en 2024: 511 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Recogéis el coche en Mura?",
         "a": "No. La recogida del taller cubre solo el área metropolitana de Barcelona, y Mura queda fuera."},
        {"q": "¿Dónde está la ITV más cercana?",
         "a": "En Manresa (B06), en el polígono Bufalvent, a 16,8 km por carretera."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "59 km, por la B-40, la C-16 y la B-20 hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "235 habitantes (+15,8 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Bages", **F.idescat("081398")},
        {"etiqueta": "Turismos (2024)", "valor": "120 · 511 por cada 1.000 hab.", **F.idescat("081398")},
        {"etiqueta": "ITV más cercana", "valor": "Manresa (B06) · 16,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 21,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 59 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081398"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sant Julià de Cerdanyola
CIUDADES["sant-julia-de-cerdanyola"] = {
    "h1": "Sant Julià de Cerdanyola: tu BMW junto a la C-16, a 123,9 km del taller",
    "entradilla": "La C-16 pasa a menos de tres kilómetros de Sant Julià de Cerdanyola y es la carretera que lleva, casi sin desvíos, hasta nuestro taller de Sant Joan Despí. Son 123,9 km: aquí tienes qué conviene hacer cerca y qué justifica el viaje.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 123.9},
    "secciones": [
        {"id": "c16-directa", "h2": "Por la BV-4021 y la C-16",
         "parrafos": [
             "La ruta sale por la BV-4021, enlaza con la C-16 y la sigue hasta la B-20: 123,9 km por carretera para 96,6 en línea recta. Además de la C-16, a menos de tres kilómetros del pueblo pasan la B-400 y la B-402.",
             "Con esa distancia, el viaje se reserva para lo específico de BMW: una avería electrónica sin diagnosticar, un problema de inyección o de turbo en un diésel, o una reparación grande que quieres que vea un especialista antes de decidir. Para la rutina, mejor un taller del Berguedà. Tampoco hay recogida: el taller solo la ofrece dentro del área metropolitana de Barcelona, que queda fuera de alcance desde aquí.",
         ]},
        {"id": "itv-berga-c16", "h2": "La ITV, a 24,6 km en Berga",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Berga (B13), en el polígono La Valldan, a 24,6 km bajando por la C-16.",
             "Si el coche tiene más de diez años y pasa inspección cada año, repasar antes luces, frenos y emisiones evita tener que repetir el viaje.",
         ]},
        {"id": "954-metros", "h2": "A 954 metros de altitud",
         "parrafos": [
             "El núcleo está a 954 metros según Idescat, y a esa altura el invierno es largo. Un BMW que duerme en la calle agradece una batería en buen estado y bien registrada, un refrigerante con la proporción correcta y, si es diésel, unos calentadores que funcionen. En las bajadas de la C-16 hacia Berga, mejor con el líquido de frenos al día.",
         ]},
        {"id": "sant-julia-en-cifras", "h2": "234 vecinos y 142 turismos",
         "parrafos": [
             "El padrón contaba 242 habitantes en 2015 y 234 en 2025, un 3,3 % menos, en un término de 11,79 km². Idescat registraba 142 turismos en 2024 a partir de la DGT: 607 por cada 1.000 vecinos.",
         ]},
    ],
    "faq": [
        {"q": "¿Hay algún taller vuestro cerca de Sant Julià?",
         "a": "No. El más cercano de la red está en Sant Joan Despí, a 123,9 km por la C-16."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En Berga (B13), a 24,6 km: es la estación más próxima por carretera según la Generalitat."},
        {"q": "¿Trabajáis también MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que los BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "234 habitantes (−3,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("089030")},
        {"etiqueta": "Altitud", "valor": "954 m", **F.idescat("089030")},
        {"etiqueta": "Turismos (2024)", "valor": "142 · 607 por cada 1.000 hab.", **F.idescat("089030")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 24,6 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 123,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("089030"), F.itv_cat_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Sora
CIUDADES["sora"] = {
    "h1": "Sora, en el norte de Osona: ITV en Ripoll y taller BMW especialista a 107 km",
    "entradilla": "Un 22,3 % más de vecinos que en 2015 y ninguna carretera principal a menos de tres kilómetros: así es Sora. Para el dueño de un BMW o un MINI, la ITV más práctica está en Ripoll, el servicio oficial en Vic y el taller especialista de la red, a 107 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 107.0},
    "secciones": [
        {"id": "ripoll-y-vic", "h2": "Ripoll para la ITV, Vic para la marca",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Ripoll (G08), en el passeig d'Ordina, a 15,6 km. El punto de servicio oficial BMW según bmw.es está en Vic: Quadis Munich, calle Perot Rocaguinarda 1, a 31,5 km.",
             "Son dos direcciones distintas desde el pueblo, y conviene saberlo antes de pedir cita: la inspección no tiene por qué hacerse en la capital de la comarca.",
         ]},
        {"id": "bv4655-c17", "h2": "107 km por la BV-4655 y la C-17",
         "parrafos": [
             "La ruta hasta la nave de Dasercars Barcelona baja por la BV-4655 hasta la C-17, sigue por la C-33 y entra por la B-20: 107 km por carretera, 83,2 en línea recta. Sora no está en el área metropolitana de Barcelona y la recogida del taller no llega.",
             "Compensa para trabajos en los que pesa la especialización en BMW —electrónica, cajas automáticas, distribución de los diésel N47 y N57— y no para el mantenimiento corriente. Si dudas, pregunta antes de hacer el viaje: con el síntoma bien descrito se puede orientar bastante.",
         ]},
        {"id": "sora-crece", "h2": "De 184 a 225 vecinos",
         "parrafos": [
             "Según el padrón, Sora tenía 184 habitantes en 2015 y 225 en 2025. El término mide 31,71 km² y el núcleo está a 716 metros. Idescat, a partir de la DGT, contaba 150 turismos en 2024: 667 por cada 1.000 vecinos, unos dos coches por cada tres personas.",
             "Sin autovía cerca, la mayoría de los trayectos son cortos y por carretera local. Ese uso castiga más el aceite y la batería que muchos kilómetros de autopista: respeta el indicador de servicio aunque el cuentakilómetros avance despacio.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV si vivo en Sora?",
         "a": "En Ripoll (G08), en el passeig d'Ordina, a 15,6 km: es la estación más próxima por carretera según la Generalitat."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "En Vic: Quadis Munich, calle Perot Rocaguinarda 1, a 31,5 km según bmw.es."},
        {"q": "¿Qué distancia hay hasta vuestro taller?",
         "a": "107 km por la BV-4655, la C-17, la C-33 y la B-20, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "225 habitantes (+22,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082726")},
        {"etiqueta": "Turismos (2024)", "valor": "150 · 667 por cada 1.000 hab.", **F.idescat("082726")},
        {"etiqueta": "ITV más cercana", "valor": "Ripoll (G08) · 15,6 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 31,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 107 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082726"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Santa Cecília de Voltregà
CIUDADES["santa-cecilia-de-voltrega"] = {
    "h1": "Santa Cecília de Voltregà: BMW a 10 km de Vic y a 85,8 km del taller especialista",
    "entradilla": "Con la C-17 a menos de tres kilómetros, desde Santa Cecília de Voltregà se llega sin complicaciones a Vic, donde están la ITV y el servicio oficial BMW, y la misma carretera baja hacia Barcelona. Nuestro taller está al final de ese recorrido, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 85.8},
    "secciones": [
        {"id": "c17-de-punta-a-punta", "h2": "La C-17, de punta a punta",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona es casi entera por la C-17, después la C-33 y al final la B-20: 85,8 km por carretera, 70,9 en línea recta. A menos de tres kilómetros del pueblo pasan la C-17 y la C-37.",
             "Es un recorrido de vía rápida, cómodo para bajar el coche cuando hace falta un especialista. Lo que no hay desde aquí es recogida: el taller la ofrece solo dentro del área metropolitana de Barcelona.",
         ]},
        {"id": "dos-citas-en-vic", "h2": "Las dos citas del calendario, en Vic",
         "parrafos": [
             "Vic reúne las dos visitas obligadas de un coche: la inspección, en la estación ITV Osona (B04) del carrer Sant Llorenç Desmunts 22, a 9,7 km según la Generalitat, y el concesionario de la marca, Quadis Munich, en la calle Perot Rocaguinarda 1, a 10,3 km según bmw.es.",
             "Con el servicio oficial tan cerca, la pregunta razonable es para qué bajar 85,8 km. Para una segunda diagnosis independiente, para una reparación fuera de garantía en la que quieres otro presupuesto, o para el mantenimiento de un coche ya mayor que pide a alguien centrado en la marca.",
         ]},
        {"id": "voltrega-en-cifras", "h2": "197 vecinos en 8,63 km²",
         "parrafos": [
             "El padrón da a Santa Cecília 197 habitantes en 2025, frente a 179 en 2015 (un 10,1 % más). Idescat contaba 133 turismos en 2024 a partir de la DGT: 675 por cada 1.000 vecinos. El núcleo está a 519 metros.",
             "Si el coche pasa la mayor parte del tiempo en recorridos cortos hasta Vic, el aceite trabaja en frío buena parte del trayecto. El intervalo que marca el indicador de servicio es un máximo, no un objetivo.",
         ]},
    ],
    "faq": [
        {"q": "¿Para qué ir a vuestro taller si tengo el oficial en Vic?",
         "a": "Para el mantenimiento y las reparaciones fuera de garantía puedes elegir taller. Nosotros somos un taller independiente especializado en BMW y MINI, en Sant Joan Despí, a 85,8 km."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En ITV Osona (B04), en Vic, a 9,7 km por carretera."},
        {"q": "¿Recogéis el coche en Santa Cecília?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "197 habitantes (+10,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082439")},
        {"etiqueta": "Turismos (2024)", "valor": "133 · 675 por cada 1.000 hab.", **F.idescat("082439")},
        {"etiqueta": "ITV más cercana", "valor": "ITV Osona (B04), Vic · 9,7 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Vic) · 10,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 85,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082439"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Calonge de Segarra
CIUDADES["calonge-de-segarra"] = {
    "h1": "Calonge de Segarra: un BMW a 33 km de la ITV y a 83,8 del taller especialista",
    "entradilla": "En Calonge de Segarra hay 179 vecinos y 131 turismos. Todo lo que tiene que ver con el coche queda a más de treinta kilómetros: la ITV en Igualada, el servicio oficial en Tàrrega y nuestro taller, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 83.8},
    "secciones": [
        {"id": "lejos-de-todo", "h2": "Ninguna gestión a menos de treinta kilómetros",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Igualada (B12), en el polígono Les Comes, a 33,1 km. El servicio oficial BMW más cercano según bmw.es es Unicars Ponent, en Tàrrega, a 37,8 km. Y el taller de la red, Dasercars Barcelona, a 83,8 km por la C-1412a y la A-2 (65 km en línea recta).",
             "Con esas distancias, cada viaje cuenta. Si el coche tiene que bajar al taller por una avería, aprovecha para hacer allí la pre-ITV y pasa la inspección en Igualada a la vuelta: queda en la misma ruta.",
         ]},
        {"id": "c25-c1412a", "h2": "La C-25 y la C-1412a, a menos de tres kilómetros",
         "parrafos": [
             "Dos carreteras pasan cerca del pueblo: la C-1412a, que es la de la ruta hacia la A-2, y la C-25. Cuando un coche hace más carretera abierta que ciudad, lo que más se desgasta son neumáticos y amortiguadores, y el frontal recibe gravilla. En los motores con muchos kilómetros, además, conviene mirar el nivel de aceite entre revisiones y no fiarlo todo al aviso del cuadro.",
         ]},
        {"id": "calonge-pierde", "h2": "Un 9,1 % menos de vecinos",
         "parrafos": [
             "El padrón pasó de 197 habitantes en 2015 a 179 en 2025. El término, de 37,15 km², tiene 5 habitantes por km², y el núcleo está a 688 metros. Idescat, con datos de la DGT, registraba 131 turismos en 2024: 732 por cada 1.000 vecinos, más del doble que en Barcelona ciudad (281).",
         ]},
        {"id": "antes-de-bajar", "h2": "Antes de bajar, el presupuesto",
         "parrafos": [
             "Desde aquí no tiene sentido llevar el coche a ciegas. En Dasercars la diagnosis se presupuesta antes de empezar, el trabajo se presupuesta por escrito y no se toca nada sin tu visto bueno. La recogida del taller no llega a Calonge: solo cubre el área metropolitana de Barcelona.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Calonge de Segarra?",
         "a": "En Igualada (B12), a 33,1 km: es la estación más próxima por carretera según la Generalitat."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Unicars Ponent, en Tàrrega, a 37,8 km según bmw.es."},
        {"q": "¿A cuánto queda vuestro taller?",
         "a": "A 83,8 km por la C-1412a y la A-2, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "179 habitantes (−9,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("080364")},
        {"etiqueta": "Turismos (2024)", "valor": "131 · 732 por cada 1.000 hab.", **F.idescat("080364")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 33,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Unicars Ponent (Tàrrega) · 37,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 83,8 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080364"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Viver i Serrateix
CIUDADES["viver-i-serrateix"] = {
    "h1": "Viver i Serrateix: 66,8 km² para 178 vecinos y un BMW a 91,9 km del taller",
    "entradilla": "Tres habitantes por kilómetro cuadrado: en Viver i Serrateix todo queda lejos. La ITV de Berga y el servicio oficial de Sant Fruitós de Bages están a 32,1 y 30,7 km; el taller especialista de la red, a 91,9 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 91.9},
    "secciones": [
        {"id": "tres-por-km2", "h2": "Tres habitantes por km²",
         "parrafos": [
             "El término mide 66,8 km² y el padrón de 2025 da 178 habitantes (168 en 2015). Idescat, a partir de la DGT, contaba 127 turismos en 2024: 713 por cada 1.000 vecinos. Ninguna carretera principal pasa a menos de tres kilómetros del núcleo, que está a 729 metros.",
             "En un sitio así, buena parte de los kilómetros diarios son de carretera local hasta llegar a la C-16. Es un uso que gasta suspensión, neumáticos y frenos más deprisa que la autovía, y que conviene tener en cuenta al decidir cuándo cambiarlos.",
         ]},
        {"id": "norte-o-sur", "h2": "Berga o Sant Fruitós: a una distancia parecida",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Berga (B13), en el polígono La Valldan, a 32,1 km. El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages, a 30,7 km. Uno hacia el norte y otro hacia el sur por la misma C-16.",
         ]},
        {"id": "bv4235-c16", "h2": "91,9 km por la BV-4235 y la C-16",
         "parrafos": [
             "Hasta Dasercars Barcelona, la ruta sale por la BV-4235, baja por la C-16 y entra por la B-20: 91,9 km por carretera, 68,6 en línea recta. La recogida que ofrece el taller se limita al área metropolitana de Barcelona y no llega aquí.",
             "Si el coche aún está en garantía, hacer el mantenimiento en un taller independiente no la anula siempre que se cumpla el plan del fabricante: lo establece el Reglamento (UE) 461/2010. Desde esta distancia, lo que sí conviene es bajar con cita y con el trabajo hablado.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Viver i Serrateix?",
         "a": "En Berga (B13), a 32,1 km por carretera, según el registro de la Generalitat."},
        {"q": "¿Pierdo la garantía si no voy al concesionario?",
         "a": "No, si se respetan los intervalos y especificaciones del plan de mantenimiento de BMW."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "91,9 km, por la BV-4235, la C-16 y la B-20, hasta Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "178 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("083089")},
        {"etiqueta": "Superficie del término", "valor": "66,8 km²", **F.idescat("083089")},
        {"etiqueta": "Turismos (2024)", "valor": "127 · 713 por cada 1.000 hab.", **F.idescat("083089")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 32,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 30,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 91,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("083089"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Orpí
CIUDADES["orpi"] = {
    "h1": "Orpí: un 25,9 % más de vecinos y un BMW a 64,3 km del taller especialista",
    "entradilla": "De 139 a 175 vecinos en diez años. Orpí está a 6,7 km de Igualada en línea recta, tiene la C-37 a menos de tres kilómetros y nuestro taller de Sant Joan Despí queda a 64,3 km, no mucho más lejos que el servicio oficial BMW.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 64.3},
    "secciones": [
        {"id": "oficial-o-especialista", "h2": "Servicio oficial a 50,5 km, especialista a 64,3",
         "parrafos": [
             "El punto oficial BMW más próximo según bmw.es está en Sant Fruitós de Bages: Quadis Munich, en la carretera de Manresa a Berga, km 34,5, a 50,5 km. Dasercars Barcelona, en Sant Joan Despí, está a 64,3 km por la BV-2132, la BV-2131, la C-244 y la A-2 (44,1 km en línea recta).",
             "Con distancias tan parecidas, la elección no es de kilómetros. Para el mantenimiento y las averías fuera de garantía, un taller independiente especializado hace el trabajo siguiendo el plan de BMW; el presupuesto se entrega por escrito y nada empieza sin tu aprobación.",
         ]},
        {"id": "itv-igualada-orpi", "h2": "La ITV, en Igualada: 18,3 km",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es la de Igualada (B12), en el polígono Les Comes, carrer dels Països Baixos 18, a 18,3 km. Orpí está fuera del área metropolitana de Barcelona, y la recogida del taller no llega hasta aquí.",
         ]},
        {"id": "orpi-en-cifras", "h2": "175 vecinos y 100 turismos",
         "parrafos": [
             "El padrón de 2025 da a Orpí 175 habitantes, un 25,9 % más que en 2015. Idescat, a partir de la DGT, contaba 100 turismos en 2024: 571 por cada 1.000 vecinos. El término mide 15,23 km² y el núcleo está a 375 metros.",
             "Hasta la A-2 se va por carreteras comarcales con curvas y bajadas. Si el volante vibra al frenar en ellas, lo habitual es que los discos se hayan deformado por calor; y un chirrido metálico suele ser el testigo de desgaste de las pastillas, que en los BMW además avisa en el cuadro.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué me queda más cerca, el servicio oficial o vuestro taller?",
         "a": "El oficial, en Sant Fruitós de Bages, a 50,5 km; nuestro taller, en Sant Joan Despí, a 64,3 km."},
        {"q": "¿Dónde paso la ITV si vivo en Orpí?",
         "a": "En Igualada (B12), a 18,3 km: es la estación más próxima por carretera según la Generalitat."},
        {"q": "¿Recogéis el coche en Orpí?",
         "a": "No. La recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "175 habitantes (+25,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("081521")},
        {"etiqueta": "Turismos (2024)", "valor": "100 · 571 por cada 1.000 hab.", **F.idescat("081521")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 18,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich (Sant Fruitós de Bages) · 50,5 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 64,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081521"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# metaDescription nuevas: todas las ciudades de la tanda tienen 0 impresiones en GSC.
# Solo se reescriben las que prometían algo prohibido por la guía (recogida a domicilio,
# ISTA, «diagnosis oficial», «presupuesto gratis», garantía por escrito, piezas
# originales, superlativos). Sant Martí Sesgueioles, Argençola, Sant Julià de Cerdanyola
# y Calonge de Segarra no se tocan.
META = {
    "tavernoles": "BMW en Tavèrnoles: ITV y servicio oficial en Vic, a menos de 10 km, y el taller especialista de la red en Sant Joan Despí, a 89,2 km. Cuándo compensa.",
    "copons": "Copons, con la A-2 al lado: taller especialista BMW a 65,6 km en Sant Joan Despí, ITV en Igualada a 14,8 km y servicio oficial en Tàrrega.",
    "lluca": "BMW en Lluçà: ITV más próxima en Berga, servicio oficial en Vic y taller especialista de la red a 116,6 km. Qué merece el viaje y qué no.",
    "l-espunyola": "L'Espunyola: ITV en Berga a 8,9 km, servicio oficial en Sant Fruitós de Bages y taller especialista BMW a 112,4 km. Un BMW a 803 metros.",
    "vallcebre": "Vallcebre, a 1.123 metros: qué revisar en tu BMW, ITV en Berga a 28,7 km y taller especialista de la red a 127,9 km en Sant Joan Despí.",
    "berzosa-del-lozoya": "Berzosa del Lozoya: servicio oficial BMW en Algete a 70,3 km y taller especialista en Alcobendas a 72,3 km. ITV en la A-1, km 66.",
    "mura": "BMW en Mura: ITV en Manresa a 16,8 km, servicio oficial en Sant Fruitós de Bages y taller especialista a 59 km por la B-40 y la C-16.",
    "sora": "BMW en Sora: ITV en Ripoll a 15,6 km, servicio oficial en Vic y taller especialista de la red a 107 km en Sant Joan Despí.",
    "santa-cecilia-de-voltrega": "Santa Cecília de Voltregà: ITV y servicio oficial BMW en Vic, a unos 10 km, y taller especialista independiente a 85,8 km por la C-17.",
    "viver-i-serrateix": "Viver i Serrateix: ITV en Berga, servicio oficial en Sant Fruitós de Bages y taller especialista BMW a 91,9 km por la C-16.",
    "orpi": "Orpí: ITV en Igualada a 18,3 km, servicio oficial BMW en Sant Fruitós de Bages a 50,5 km y taller especialista a 64,3 km por la A-2.",
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
