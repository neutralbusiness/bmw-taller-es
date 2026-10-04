# Tanda 9: Cabrera d'Anoia, Gualba, Castellví de la Marca, Villanueva de Perales, Fogars de la Selva,
# Casserres, Torrelavit, Orusco de Tajuña, Santa Eulàlia de Riuprimer, Font-rubí, Tórtola de Henares,
# Vallbona d'Anoia, Anchuelo, el Pla del Penedès y Titulcia.
# Texto escrito a mano a partir de datos/<slug>.json. Se carga con piloto/aplicar.py.
# META: metaDescription nueva para ciudades sin impresiones cuya descripción actual contenía
# promesas no acreditadas («diagnosis oficial/original», ISTA, garantía por escrito, recogida
# fuera del área metropolitana, especialidades inventadas). Se aplica con un script aparte.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "piloto"))
from fuentes import F  # noqa: E402

REVISADO = "2026-10-04"
CIUDADES = {}
OSM = {"texto": "OpenStreetMap (estación ITV de Guadalajara)", "url": "https://www.openstreetmap.org/way/381990031"}

META = {
    "cabrera-d-anoia": "BMW en Cabrera d'Anoia: ITV en Olèrdola, servicio oficial en Vilanova i la Geltrú y taller especialista independiente en Sant Joan Despí, a 48,1 km.",
    "gualba": "BMW y MINI en Gualba: ITV a 6,9 km en Sant Celoni, servicio oficial en Mataró y taller especialista de la red en Sant Joan Despí, a 65,5 km.",
    "villanueva-de-perales": "BMW en Villanueva de Perales: ITV en Navalcarnero, servicio oficial en Alcorcón y taller especialista independiente en Alcobendas, a 60,5 km.",
    "torrelavit": "BMW en Torrelavit: ITV en Olèrdola, servicio oficial en Vilanova i la Geltrú y taller especialista de la red en Sant Joan Despí, a 43,7 km por la AP-7.",
    "orusco-de-tajuna": "BMW en Orusco de Tajuña: ITV en Villarejo de Salvanés, servicio oficial en Alcalá de Henares y taller especialista en Alcobendas, a 64,6 km.",
    "santa-eulalia-de-riuprimer": "BMW en Santa Eulàlia de Riuprimer: servicio oficial e ITV en Vic y taller especialista independiente en Sant Joan Despí, a 82,5 km. Cuándo compensa.",
    "font-rubi": "BMW en Font-rubí: ITV en Olèrdola, servicio oficial en Vilanova i la Geltrú y taller especialista independiente en Sant Joan Despí, a 55,6 km.",
    "tortola-de-henares": "BMW en Tórtola de Henares: concesionario en Guadalajara, a 13,8 km, y taller especialista independiente en Alcobendas, a 65,3 km por la R-2.",
    "vallbona-d-anoia": "BMW en Vallbona d'Anoia: ITV en Igualada, servicio oficial en Terrassa y taller especialista de la red en Sant Joan Despí, a 47,5 km por la A-2.",
    "anchuelo": "BMW en Anchuelo: servicio oficial e ITV en Alcalá de Henares y taller especialista independiente en Alcobendas, a 42,2 km por la R-2.",
    "el-pla-del-penedes": "BMW en el Pla del Penedès: ITV en Olèrdola, servicio oficial en Vilanova i la Geltrú y taller especialista en Sant Joan Despí, a 45,9 km.",
    "titulcia": "BMW en Titulcia: ITV en Valdemoro, servicio oficial en Getafe y taller especialista independiente en Alcobendas, a 56,1 km por la A-4.",
}

# ---------------------------------------------------------------- Cabrera d'Anoia
CIUDADES["cabrera-d-anoia"] = {
    "h1": "Cabrera d'Anoia: un pueblo que crece y su BMW, a 48 km del taller especialista",
    "entradilla": "Un 31,5 % más de vecinos en diez años: pocos municipios de la red han crecido tanto. Para quien tiene aquí un BMW o un MINI, lo útil es saber que la ITV y el concesionario quedan hacia el Penedès y el Garraf, y el taller de la red, en el Baix Llobregat.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 48.1},
    "secciones": [
        {"id": "de-1348-a-1772", "h2": "De 1.348 a 1.772 habitantes",
         "parrafos": [
             "El padrón del INE contaba 1.348 vecinos en Cabrera d'Anoia en 2015 y 1.772 en 2025. En un término de 17 km², a 299 metros de altitud, eso son 104 habitantes por kilómetro cuadrado. Idescat, a partir de la DGT, registraba 983 turismos en 2024: 555 por cada 1.000 vecinos.",
             "Más de un coche por cada dos personas es la norma en los pueblos del Anoia y del Penedès, donde casi cualquier gestión obliga a coger el coche. Lo que eso supone para un BMW es uso mixto: tramos cortos por carreteras locales y, de vez en cuando, autopista.",
         ]},
        {"id": "hacia-el-baix-llobregat", "h2": "Por la BV-2242 y la AP-7 hasta Sant Joan Despí",
         "parrafos": [
             "La nave de Dasercars Barcelona está en el carrer del Tambor del Bruc 3. Desde Cabrera, la ruta enlaza la BV-2242 y la BV-2244, toma la AP-7 y termina por la B-23: 48,1 km por carretera, 31,8 en línea recta.",
             "Cabrera no está entre los 36 municipios del Área Metropolitana de Barcelona, así que la recogida de coches del taller, que se limita a esa área, no llega hasta aquí.",
         ]},
        {"id": "itv-y-oficial-al-sur", "h2": "La ITV y el servicio oficial, hacia el sur",
         "parrafos": [
             "Aunque el municipio es del Anoia, la estación más próxima por carretera en el registro de la Generalitat no es la de Igualada sino la de Olèrdola (B09), en la avinguda de l'Hostal Nou, a 24,1 km. El servicio oficial BMW más cercano según el localizador de bmw.es está todavía más al sur: Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 38,7 km.",
             "Si el coche está en garantía y te llega una carta de la marca, esa cita es en Vilanova. Para una avería que no se ha resuelto o un diésel con problemas de filtro de partículas, el viaje al especialista tiene más sentido.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué ITV me toca desde Cabrera d'Anoia?",
         "a": "La más próxima por carretera en el registro de la Generalitat es la de Olèrdola (B09), a 24,1 km."},
        {"q": "¿Dónde está el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en Vilanova i la Geltrú, a 38,7 km según bmw.es."},
        {"q": "¿Recogéis el coche en Cabrera?",
         "a": "No. La recogida del taller cubre solo el área metropolitana de Barcelona, y Cabrera queda fuera."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.772 habitantes (+31,5 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("080288")},
        {"etiqueta": "Turismos (2024)", "valor": "983 · 555 por cada 1.000 hab.", **F.idescat("080288")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 24,1 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 38,7 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 48,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080288"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Gualba
CIUDADES["gualba"] = {
    "h1": "BMW en Gualba: la ITV en la carretera de Gualba y el taller especialista a 65,5 km",
    "entradilla": "La estación de ITV que le toca a Gualba está en Sant Celoni, en una calle que lleva el nombre del pueblo. El servicio oficial BMW queda en Mataró y el taller de la red, en Sant Joan Despí. Esto es lo que te conviene resolver cerca y lo que no.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 65.5},
    "secciones": [
        {"id": "itv-sant-celoni", "h2": "Sant Celoni (B26), a 6,9 km",
         "parrafos": [
             "En el registro de estaciones de la Generalitat, la más próxima por carretera es ITV Sant Celoni (B26), en la carretera de Gualba 41-43, a 6,9 km del centro del pueblo. Es tan accesible que no tiene sentido mezclarla con el viaje al taller: la pre-ITV la puede hacer cualquier taller de la zona, y la inspección, en la misma mañana.",
         ]},
        {"id": "mataro-o-sant-joan", "h2": "Mataró para lo de la marca, Sant Joan Despí para lo difícil",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más cercano es Pruna Motor, en la Via Sergia 2 de Mataró, a 38,4 km por carretera. Allí se tramitan las reparaciones cubiertas por la garantía de BMW.",
             "Dasercars Barcelona, el taller independiente de la red, está a 65,5 km: BV-5115, C-35, AP-7, C-33 y B-20 hasta el carrer del Tambor del Bruc. Es mucha carretera para un cambio de pastillas y poca para una avería que lleva meses sin diagnóstico, un diésel N47 o B47 con ruido de distribución o un escape que no pasa las emisiones (el taller tiene homologación REDISTA).",
         ]},
        {"id": "gualba-en-cifras", "h2": "1.766 vecinos repartidos en 23 km²",
         "parrafos": [
             "Gualba, en el Vallès Oriental, tenía 1.766 habitantes en 2025, un 24,9 % más que en 2015, en un término de 23,29 km² a 177 metros. En 2024 había 933 turismos (Idescat, con datos de la DGT): 528 por cada 1.000 habitantes.",
             "La C-35 pasa a menos de tres kilómetros del centro. Para un diésel que hace sobre todo trayectos cortos por el pueblo, salir de vez en cuando por ella o por la AP-7 a régimen constante ayuda a que el filtro de partículas complete su regeneración.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es la ITV más cercana a Gualba?",
         "a": "Según el registro de la Generalitat, la de Sant Celoni (B26), en la carretera de Gualba 41-43, a 6,9 km."},
        {"q": "¿Tenéis taller en el Vallès Oriental?",
         "a": "No. El taller de la red es Dasercars Barcelona, en Sant Joan Despí, a 65,5 km por carretera."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí. MINI comparte motores y electrónica con BMW y se diagnostica con el mismo equipo."},
        {"q": "¿Llega la recogida del taller hasta Gualba?",
         "a": "No: solo cubre el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.766 habitantes (+24,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Vallès Oriental", **F.idescat("080977")},
        {"etiqueta": "Turismos (2024)", "valor": "933 · 528 por cada 1.000 hab.", **F.idescat("080977")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 6,9 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Pruna Motor, Mataró · 38,4 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 65,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080977"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Castellví de la Marca
CIUDADES["castellvi-de-la-marca"] = {
    "h1": "Castellví de la Marca: 661 turismos por cada mil vecinos y un taller BMW a 55,5 km",
    "entradilla": "Más del doble de turismos por habitante que en Barcelona ciudad. En Castellví de la Marca el coche es imprescindible, y la AP-7 pasa al lado: eso marca cómo conviene mantener un BMW aquí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 55.5},
    "secciones": [
        {"id": "dos-coches-cada-tres", "h2": "Casi dos coches por cada tres habitantes",
         "parrafos": [
             "El padrón de 2025 da a Castellví de la Marca 1.721 vecinos, un 11,8 % más que en 2015, repartidos en 28,4 km². Idescat, con datos de la DGT, registraba 1.138 turismos en 2024: 661 por cada 1.000 habitantes, más del doble que en Barcelona ciudad (281).",
             "Con 61 habitantes por kilómetro cuadrado y el término salpicado de núcleos, cada desplazamiento es en coche. Muchos hogares tienen dos, y suele ser el segundo, el que menos se mueve, el que da sustos con la batería.",
         ]},
        {"id": "ap7-al-lado", "h2": "La AP-7, la N-340 y la B-212 a menos de 3 km",
         "parrafos": [
             "Tener la AP-7 tan cerca es una ventaja para un diésel moderno: unos kilómetros a régimen constante permiten que el filtro de partículas se regenere, cosa que no ocurre en trayectos cortos entre masías. Si el cuadro avisa de regeneración, lo correcto es seguir circulando, no apagar el motor.",
             "Esa misma AP-7, tras la B-212 y la N-340, lleva al taller: 55,5 km hasta el carrer del Tambor del Bruc de Sant Joan Despí, terminando por la B-23. Castellví queda fuera del área metropolitana, así que la recogida del taller no llega hasta aquí.",
         ]},
        {"id": "itv-y-oficial", "h2": "Olèrdola y Vilanova, lo más próximo",
         "parrafos": [
             "La estación más cercana por carretera en el registro de la Generalitat es la de Olèrdola (B09), a 13,4 km. El servicio oficial BMW que figura en bmw.es más próximo es Quadis Munich, en Vilanova i la Geltrú, a 24,3 km; ahí van las reparaciones en garantía de la marca.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "55,5 km por la B-212, la N-340, la AP-7 y la B-23 hasta Sant Joan Despí."},
        {"q": "¿Qué hago si mi diésel avisa de regeneración del filtro?",
         "a": "Seguir circulando a régimen constante hasta que termine. Si el aviso se repite a menudo, conviene revisarlo."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La más próxima por carretera es Olèrdola (B09), a 13,4 km, según la Generalitat."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.721 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("080654")},
        {"etiqueta": "Turismos (2024)", "valor": "1.138 · 661 por cada 1.000 hab.", **F.idescat("080654")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 13,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 24,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 55,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080654"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Villanueva de Perales
CIUDADES["villanueva-de-perales"] = {
    "h1": "Villanueva de Perales: ITV en Navalcarnero y especialista BMW a 60 km, en Alcobendas",
    "entradilla": "Desde el suroeste de la región, el taller especialista de la red queda al otro lado de Madrid. Antes de hacer 60 km conviene saber qué tienes más a mano: la ITV en Navalcarnero y el servicio oficial BMW en Alcorcón.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 60.5},
    "secciones": [
        {"id": "navalcarnero", "h2": "La ITV de El Alparrache, en Navalcarnero",
         "parrafos": [
             "La estación oficial más cercana por carretera, según el listado de la Comunidad de Madrid, es la de TÜV Rheinland Ibérica (estación 2845), en el paseo de Alparrache 26, en el polígono industrial El Alparrache de Navalcarnero: 16 km desde el centro de Villanueva de Perales.",
         ]},
        {"id": "alcorcon-o-alcobendas", "h2": "Alcorcón a 31 km, Alcobendas a 60",
         "parrafos": [
             "El servicio oficial BMW más próximo según bmw.es es Vehinter, en la avenida de San Martín de Valdeiglesias 14-16 de Alcorcón, a 31,1 km por carretera. Las reparaciones cubiertas por la garantía de BMW se gestionan en la red oficial.",
             "Para el mantenimiento puedes elegir taller: el Reglamento (UE) 461/2010 impide que el fabricante condicione la garantía a revisar en su red, siempre que se sigan intervalos y especificaciones. Dasercars Madrid, en la calle Valgrande 17 de Alcobendas, queda a 60,5 km por la M-524, la M-501, la M-40 y la A-1 (43,6 en línea recta).",
             "A esa distancia, el viaje compensa para lo que pide un especialista —una avería eléctrica que vuelve, un fallo del sistema de AdBlue, una distribución ruidosa en un N47— más que para una revisión rutinaria. La recogida y el vehículo de cortesía, sujetos a disponibilidad, se limitan al área metropolitana de Madrid: confirma antes si tu dirección entra.",
         ]},
        {"id": "un-dato-que-engana", "h2": "7.422 turismos para 1.715 vecinos: un dato que engaña",
         "parrafos": [
             "El Instituto de Estadística de la Comunidad de Madrid, a partir de la DGT, registra 7.422 turismos en el municipio en 2025, cuando el padrón da 1.715 habitantes (un 19 % más que en 2015). Una diferencia así suele deberse a vehículos de empresa domiciliados en el municipio, así que la cifra no describe el uso real de los vecinos.",
             "Lo que sí es real: la M-523, la M-524 y la M-530 pasan a menos de tres kilómetros del centro, y casi todo se hace por carretera secundaria.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Villanueva de Perales?",
         "a": "La estación oficial más cercana por carretera es la de El Alparrache, en Navalcarnero, a 16 km."},
        {"q": "¿Cuál es el servicio oficial BMW más próximo?",
         "a": "Vehinter, en Alcorcón, a 31,1 km según el localizador de bmw.es."},
        {"q": "¿Pierdo la garantía si no reviso en el concesionario?",
         "a": "No, si se respetan los intervalos y especificaciones del plan de mantenimiento."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.715 habitantes (+19 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "31,3 km²", **F.cartociudad},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV Rheinland, Navalcarnero · 16 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Alcorcón) · 31,1 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 60,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.cartociudad_f, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Fogars de la Selva
CIUDADES["fogars-de-la-selva"] = {
    "h1": "Fogars de la Selva: BMW entre la AP-7 y la C-35, servicio oficial en Salt",
    "entradilla": "Provincia de Barcelona, comarca de la Selva: Fogars mira a la vez hacia Girona y hacia el Vallès. El servicio oficial BMW más cercano está en Salt, la ITV en Sant Celoni y el taller especialista de la red, a 74,9 km.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 74.9},
    "secciones": [
        {"id": "seis-carreteras", "h2": "Seis carreteras a menos de 3 km",
         "parrafos": [
             "Por el entorno del núcleo urbano pasan la AP-7, la C-35, la GI-512, la GI-555, la BV-5122 y la BV-5123. Es un término de 32,12 km² con 53 habitantes por kilómetro cuadrado, de modo que el coche se usa a diario, y no siempre en trayectos largos.",
             "Idescat, con datos de la DGT, contaba 1.060 turismos en 2024 para 1.704 vecinos en 2025: 622 por cada 1.000. Con la AP-7 tan cerca, un diésel tiene fácil hacer el tramo a velocidad constante que le permite regenerar el filtro de partículas; el problema aparece en los coches que solo van del pueblo al tren y vuelta.",
         ]},
        {"id": "salt-y-sant-celoni", "h2": "Salt para la marca, Sant Celoni para la ITV",
         "parrafos": [
             "Según el localizador de bmw.es, el punto oficial BMW más próximo es Oliva Motor Girona, en el carrer de Lingen 9-11 de Salt, a 37 km por carretera. La estación más cercana por carretera en el registro de la Generalitat es ITV Sant Celoni (B26), en la carretera de Gualba 41-43, a 16,8 km.",
         ]},
        {"id": "hasta-sant-joan", "h2": "75 km hasta Sant Joan Despí: para qué",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona sale por la BV-5122 a la AP-7 y sigue por la C-33 y la B-20: 74,9 km por carretera. Con esa distancia, el viaje se justifica por una avería concreta de BMW o MINI que no se ha resuelto cerca, o por un escape y unas emisiones que necesitan un taller con homologación REDISTA.",
             "Antes de moverte, llama con modelo, año, kilometraje y el síntoma: se puede orientar por teléfono si merece la pena. Fogars no está en el área metropolitana de Barcelona, y la recogida del taller no llega.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el servicio oficial BMW más cercano a Fogars de la Selva?",
         "a": "Oliva Motor Girona, en Salt, a 37 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "La estación más cercana por carretera es Sant Celoni (B26), a 16,8 km, según la Generalitat."},
        {"q": "¿A qué distancia está vuestro taller?",
         "a": "A 74,9 km por la AP-7, la C-33 y la B-20, en Sant Joan Despí."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.704 habitantes (+15,9 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Selva", **F.idescat("080826")},
        {"etiqueta": "Turismos (2024)", "valor": "1.060 · 622 por cada 1.000 hab.", **F.idescat("080826")},
        {"etiqueta": "ITV más cercana", "valor": "Sant Celoni (B26) · 16,8 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Oliva Motor Girona (Salt) · 37 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 74,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080826"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Casserres
CIUDADES["casserres"] = {
    "h1": "Casserres, en el Berguedà: casi 100 km hasta el taller BMW y lo que te queda cerca",
    "entradilla": "Hasta nuestro taller hay 98,7 km por la C-16. No vamos a decirte que es un paseo: para casi todo, Berga y Sant Fruitós te quedan mucho más cerca. Esta página separa lo que merece el viaje de lo que no.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 98.7},
    "secciones": [
        {"id": "berga-y-sant-fruitos", "h2": "La ITV en Berga, el concesionario en Sant Fruitós",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Berga (B13), en el camí de Sant Bartomeu, polígono industrial La Valldan, a 15,3 km. El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la carretera de Manresa a Berga, km 34,5, en Sant Fruitós de Bages: 37,5 km.",
             "Las dos quedan sobre el eje de la C-16, que pasa a menos de tres kilómetros del centro de Casserres junto con la BV-4131 y la BV-4132.",
         ]},
        {"id": "lo-que-no-merece", "h2": "Lo que no merece 99 kilómetros",
         "parrafos": [
             "Neumáticos, escobillas, un cambio de aceite sin complicaciones o la pre-ITV: todo eso lo resuelve un taller de confianza del Berguedà. Bajar a Sant Joan Despí por esto sería gastar un día.",
         ]},
        {"id": "lo-que-si", "h2": "Lo que sí puede merecerlo",
         "parrafos": [
             "Un problema específico de BMW que ha pasado por varios talleres sin solución, un diésel M57 o N57 con fallos que nadie localiza, o un mantenimiento hecho según el plan de la marca. La ruta es directa: BV-4132, C-16 y B-20 hasta el carrer del Tambor del Bruc.",
             "Desde aquí lo sensato es organizarlo antes. El presupuesto llega por escrito y no se toca nada sin tu visto bueno, y la diagnosis también se presupuesta: así sabes a qué vas antes de coger el coche. Casserres queda lejos del área metropolitana, de modo que la recogida del taller no cubre la zona.",
         ]},
        {"id": "casserres-en-cifras", "h2": "1.660 vecinos a 611 metros",
         "parrafos": [
             "Casserres tenía 1.660 habitantes en 2025, un 7,7 % más que en 2015, y 1.102 turismos en 2024 según Idescat a partir de la DGT: 664 por cada 1.000, frente a los 281 de Barcelona ciudad.",
         ]},
    ],
    "faq": [
        {"q": "¿Tenéis taller en el Berguedà?",
         "a": "No. El taller de la red más cercano está en Sant Joan Despí, a 98,7 km de Casserres."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En ITV Berga (B13), polígono La Valldan, a 15,3 km: la más próxima por carretera según la Generalitat."},
        {"q": "¿Puedo saber el presupuesto antes de bajar?",
         "a": "Sí. La diagnosis se presupuesta antes de hacerla, y la reparación, por escrito, antes de empezar."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.660 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Berguedà", **F.idescat("080497")},
        {"etiqueta": "Altitud", "valor": "611 m", **F.idescat("080497")},
        {"etiqueta": "Turismos (2024)", "valor": "1.102 · 664 por cada 1.000 hab.", **F.idescat("080497")},
        {"etiqueta": "ITV más cercana", "valor": "Berga (B13) · 15,3 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Sant Fruitós de Bages · 37,5 km", **F.bmw},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080497"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Torrelavit
CIUDADES["torrelavit"] = {
    "h1": "Torrelavit: tres direcciones para tu BMW, con el taller especialista a 43,7 km",
    "entradilla": "Desde Torrelavit, cada cosa está en un sitio distinto: la ITV en Olèrdola, el concesionario en Vilanova i la Geltrú y el taller especialista de la red en Sant Joan Despí. Así se reparte el trabajo con cabeza.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 43.7},
    "secciones": [
        {"id": "al-este-el-taller", "h2": "Al este, por la AP-7: el taller",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona sale por la BP-2151, sigue por la BV-2244, coge la AP-7 y entra por la B-23: 43,7 km por carretera, 29,1 en línea recta. Es algo menos que desde el Pla del Penedès (45,9 km) y bastante menos que desde Font-rubí (55,6).",
             "Aun así, Torrelavit no pertenece al Área Metropolitana de Barcelona, y la recogida del taller no llega aquí. Lo práctico es reservar día y dejar el coche por la mañana.",
         ]},
        {"id": "al-sur-itv-y-marca", "h2": "Al sur: la ITV y la red oficial",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima por carretera es la de Olèrdola (B09), a 20 km. Según el localizador de bmw.es, el servicio oficial BMW más cercano es Quadis Munich, en Vilanova i la Geltrú, a 34,6 km.",
             "Curiosamente, en línea recta el concesionario (24,6 km) y el taller (29,1 km) están a una distancia parecida: lo que decide no es tanto el kilometraje como el tipo de trabajo. Garantía de fábrica, en la red oficial; diagnosis de averías, mantenimiento y diésel —la especialidad del taller son los N47, N57, B47 y B57—, con el especialista.",
         ]},
        {"id": "torrelavit-en-cifras", "h2": "1.572 vecinos y 930 turismos",
         "parrafos": [
             "El padrón de 2025 da a Torrelavit 1.572 habitantes, un 12,2 % más que en 2015, en 23,65 km² a 202 metros de altitud. Idescat, con datos de la DGT, registraba 930 turismos en 2024: 592 por cada 1.000 vecinos.",
             "Un parque así, con mucho trayecto corto por carreteras locales como la BP-2151, desgasta más frenos y embrague que kilómetros de autopista. Si notas vibración al frenar después de unos días sin usar el coche, suele ser óxido superficial en los discos y se va con el uso; si persiste, hay que mirarlo.",
         ]},
    ],
    "faq": [
        {"q": "¿Qué distancia hay hasta el taller?",
         "a": "43,7 km por carretera, por la AP-7 y la B-23, hasta Sant Joan Despí."},
        {"q": "¿Dónde está la ITV más próxima?",
         "a": "En Olèrdola (B09), a 20 km por carretera, según el registro de la Generalitat."},
        {"q": "¿Trabajáis diésel?",
         "a": "Sí: los motores diésel N47, N57, B47 y B57 son la especialidad del taller."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.572 habitantes (+12,2 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("082877")},
        {"etiqueta": "Turismos (2024)", "valor": "930 · 592 por cada 1.000 hab.", **F.idescat("082877")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 20 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 34,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 43,7 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082877"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Orusco de Tajuña
CIUDADES["orusco-de-tajuna"] = {
    "h1": "Orusco de Tajuña: del valle a Alcobendas, 64,6 km hasta el taller especialista BMW",
    "entradilla": "En la vega del Tajuña lo que tienes más cerca para tu BMW está en Villarejo de Salvanés y en Alcalá de Henares. El taller especialista de la red queda en Alcobendas, y conviene saber cuándo merece la pena el viaje.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 64.6},
    "secciones": [
        {"id": "ruta-r3", "h2": "Por la R-3 y la M-30 hasta la calle Valgrande",
         "parrafos": [
             "La ruta desde el centro de Orusco va por la M-229, la M-221 y la M-209 hasta la R-3, cruza por la M-30 y sale por la A-1: 64,6 km por carretera y 46 en línea recta hasta Dasercars Madrid, en la calle Valgrande 17 de Alcobendas.",
             "La recogida y el vehículo de cortesía del taller existen, sujetos a disponibilidad, pero solo dentro del área metropolitana de Madrid; desde el valle, cuenta con llevar tú el coche.",
         ]},
        {"id": "villarejo-y-alcala", "h2": "ITV en Villarejo, servicio oficial en Alcalá",
         "parrafos": [
             "La estación oficial más próxima por carretera, según el listado de la Comunidad de Madrid, es la de General de Servicios ITV (estación 2853), en la avenida Juan Carlos I Rey de España 13 de Villarejo de Salvanés, a 19,8 km.",
             "El servicio oficial BMW más cercano en el localizador de bmw.es es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 36,2 km. Allí se tramitan las reparaciones en garantía de la marca.",
         ]},
        {"id": "cuando-compensa", "h2": "Cuándo compensa bajar",
         "parrafos": [
             "Para una avería de BMW o MINI que no se ha localizado cerca, un problema del sistema de AdBlue o una cadena de distribución ruidosa en un diésel. En esos casos, el presupuesto se entrega por escrito y nada se empieza sin tu aprobación, de modo que el viaje no te ata a una reparación que no quieras.",
         ]},
        {"id": "orusco-en-cifras", "h2": "1.531 vecinos a 714 metros",
         "parrafos": [
             "Orusco de Tajuña tenía 1.531 habitantes en el padrón de 2025, un 21,5 % más que en 2015, en un término de 21,3 km². La Comunidad de Madrid, con datos de la DGT, contaba 754 turismos en 2025: 492 por cada 1.000 habitantes, menos que en Anchuelo (602), aunque por encima de Madrid capital (388).",
             "La M-229, la M-204 y la M-215 pasan a menos de tres kilómetros del centro.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde paso la ITV desde Orusco?",
         "a": "La estación oficial más cercana por carretera es la de Villarejo de Salvanés (estación 2853), a 19,8 km."},
        {"q": "¿Cuál es el concesionario BMW más próximo?",
         "a": "AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 36,2 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "64,6 km por la R-3, la M-30 y la A-1 hasta Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.531 habitantes (+21,5 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "754 · 492 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "Villarejo de Salvanés · 19,8 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 36,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 64,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Santa Eulàlia de Riuprimer
CIUDADES["santa-eulalia-de-riuprimer"] = {
    "h1": "Santa Eulàlia de Riuprimer: servicio oficial BMW a 7,3 km y especialista a 82,5",
    "entradilla": "Lo decimos de entrada: para un vecino de Santa Eulàlia de Riuprimer, el concesionario BMW de Vic está a 7,3 km y nuestro taller, a 82,5. Hay trabajos para cada uno, y aquí te explicamos cuáles.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 82.5},
    "secciones": [
        {"id": "vic-al-lado", "h2": "Vic lo tiene casi todo a mano",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial más próximo es Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 7,3 km por carretera. La ITV, también en Vic: ITV Osona (B04), en el carrer Sant Llorenç Desmunts 22, a 11,6 km, la más próxima por carretera en el registro de la Generalitat.",
             "Con eso tan cerca, revisiones de rutina, inspección y reparaciones en garantía no justifican salir de Osona.",
         ]},
        {"id": "taller-independiente", "h2": "Por qué hay quien elige un independiente",
         "parrafos": [
             "La normativa europea —Reglamento (UE) 461/2010— permite hacer el mantenimiento fuera del concesionario sin que el fabricante pueda negar la garantía, con una condición: respetar intervalos, especificaciones y recambios de calidad equivalente. Es lo que hace un taller especialista como Dasercars.",
             "El viaje hasta el carrer del Tambor del Bruc de Sant Joan Despí, por la BV-4316, la C-17, la C-33 y la B-20, son 82,5 km. Tiene sentido para una segundo diagnóstico antes de aceptar una reparación grande, para un diésel B47 o N57 con un fallo recurrente o para emisiones y escape, donde el taller trabaja con homologación REDISTA.",
         ]},
        {"id": "riuprimer-en-cifras", "h2": "1.516 vecinos y 783 turismos en 13,82 km²",
         "parrafos": [
             "El padrón de 2025 cuenta 1.516 habitantes, un 18,1 % más que en 2015. Idescat, con datos de la DGT, registraba 783 turismos en 2024, 516 por cada 1.000 vecinos. El núcleo está a 568 metros, y la C-25 pasa a menos de tres kilómetros.",
             "En invierno, la batería es lo que más sufre en un coche que duerme fuera. En un BMW, además, una batería nueva hay que registrarla en la centralita para que la carga se ajuste a ella.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es el concesionario BMW más cercano?",
         "a": "Quadis Munich, en la calle Perot Rocaguinarda 1 de Vic, a 7,3 km según bmw.es."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En ITV Osona (B04), en Vic, a 11,6 km: la más próxima por carretera en el registro de la Generalitat."},
        {"q": "¿Recogéis el coche en Osona?",
         "a": "No. La recogida del taller cubre solo el área metropolitana de Barcelona."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.516 habitantes (+18,1 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Osona", **F.idescat("082476")},
        {"etiqueta": "Turismos (2024)", "valor": "783 · 516 por cada 1.000 hab.", **F.idescat("082476")},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vic · 7,3 km", **F.bmw},
        {"etiqueta": "ITV más cercana", "valor": "Osona (B04), Vic · 11,6 km", **F.itv_cat},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 82,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082476"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.r461_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Font-rubí
CIUDADES["font-rubi"] = {
    "h1": "Font-rubí: un término de 37 km² donde el BMW no descansa",
    "entradilla": "Con 39 habitantes por kilómetro cuadrado, en Font-rubí casi nada queda a pie. El taller especialista de la red está a 55,6 km, en Sant Joan Despí; la ITV y el concesionario, hacia la costa.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 55.6},
    "secciones": [
        {"id": "termino-disperso", "h2": "1.441 vecinos en 37,42 km²",
         "parrafos": [
             "El término de Font-rubí mide 37,42 km², casi cuatro veces el del Pla del Penedès (9,56), para 1.441 habitantes en 2025 (un 6,9 % más que en 2015). Idescat, con datos de la DGT, registraba 957 turismos en 2024: 664 por cada 1.000 vecinos.",
             "Ese reparto tiene una consecuencia mecánica. Muchos trayectos son cortos y por carreteras de curvas, con el motor sin llegar a temperatura: el aceite se contamina antes y el diésel no completa las regeneraciones del filtro de partículas. Respetar el indicador de servicio, y no estirarlo, compensa.",
         ]},
        {"id": "bv2127-ap7", "h2": "BV-2127 y AP-7 hasta el taller",
         "parrafos": [
             "Desde Font-rubí, la ruta hasta Dasercars Barcelona baja por la BV-2127, sigue por la AP-7 y termina por la B-23: 55,6 km por carretera, 35 en línea recta. La recogida del taller no llega: se limita al área metropolitana de Barcelona.",
             "Para que el viaje sirva, el taller entrega el presupuesto por escrito y no empieza nada sin tu conformidad; la diagnosis también se presupuesta antes.",
         ]},
        {"id": "itv-oficial-font-rubi", "h2": "Olèrdola para la ITV, Vilanova para la marca",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es Olèrdola (B09), en la avinguda de l'Hostal Nou, a 16,4 km. El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en Vilanova i la Geltrú, a 28,6 km.",
             "La C-15 pasa a menos de tres kilómetros del centro y es la salida natural hacia los dos.",
         ]},
    ],
    "faq": [
        {"q": "¿A qué distancia está el taller?",
         "a": "A 55,6 km por la BV-2127, la AP-7 y la B-23, en Sant Joan Despí."},
        {"q": "¿Por qué mi diésel avisa a menudo del filtro de partículas?",
         "a": "Suele pasar con trayectos cortos en los que el motor no llega a la temperatura de regeneración. Si el aviso es frecuente, hay que revisarlo."},
        {"q": "¿Dónde paso la ITV desde Font-rubí?",
         "a": "La más próxima por carretera es Olèrdola (B09), a 16,4 km, según la Generalitat."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.441 habitantes", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "37,42 km²", **F.cartociudad},
        {"etiqueta": "Turismos (2024)", "valor": "957 · 664 por cada 1.000 hab.", **F.idescat("080850")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 16,4 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 28,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 55,6 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("080850"), F.cartociudad_f, F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Tórtola de Henares
CIUDADES["tortola-de-henares"] = {
    "h1": "Tórtola de Henares: concesionario BMW en Guadalajara y especialista a 65 km",
    "entradilla": "Tórtola de Henares ha pasado de 990 a 1.439 vecinos en diez años. Para el dueño de un BMW o un MINI, Guadalajara capital resuelve lo cercano; el taller especialista de la red está en Alcobendas, por la R-2.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 65.3},
    "secciones": [
        {"id": "un-45-por-ciento", "h2": "Un 45,4 % más de población desde 2015",
         "parrafos": [
             "Según el padrón del INE, Tórtola de Henares tenía 990 habitantes en 2015 y 1.439 en 2025. El término mide 26,6 km² y el núcleo está a unos 743 metros. La CM-1003 pasa a medio kilómetro del centro y es por donde sale casi todo el tráfico.",
         ]},
        {"id": "guadalajara-cerca", "h2": "Lo de la marca y la ITV, en Guadalajara",
         "parrafos": [
             "El punto oficial BMW más próximo según el localizador de bmw.es es AutoPremier, en el Paseo de la Estación 23 de Guadalajara, a 13,8 km por carretera. Si el coche está en garantía, las reparaciones a cargo de BMW se hacen en la red oficial.",
             "El mantenimiento, en cambio, no te ata al concesionario: el Reglamento (UE) 461/2010 protege la garantía si el coche se revisa en un taller independiente cumpliendo el plan del fabricante.",
             "Para la inspección, una estación cercana es la de Guadalajara capital, en la calle Trafalgar.",
         ]},
        {"id": "r2-hasta-alcobendas", "h2": "Por la CM-1003, la R-2 y la M-50",
         "parrafos": [
             "La ruta hasta Dasercars Madrid, en la calle Valgrande 17 de Alcobendas, va por la CM-1003, la R-2 y la M-50: 65,3 km por carretera, 48,2 en línea recta. Tórtola es provincia de Guadalajara y queda fuera del área metropolitana de Madrid, así que la recogida del taller no la cubre.",
             "Compensa bajar para lo que pide conocer la marca: una avería electrónica sin diagnóstico, un diésel N47 o B47 con problemas de distribución o un fallo del sistema SCR. Para el resto, Guadalajara te queda a un paso.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el concesionario BMW más cercano a Tórtola?",
         "a": "AutoPremier, en el Paseo de la Estación 23 de Guadalajara, a 13,8 km según bmw.es."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "65,3 km por la CM-1003, la R-2 y la M-50 hasta Alcobendas."},
        {"q": "¿Recogéis el coche en Tórtola de Henares?",
         "a": "No: la recogida del taller cubre solo el área metropolitana de Madrid."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.439 habitantes (+45,4 % desde 2015)", **F.ine},
        {"etiqueta": "Superficie del término", "valor": "26,6 km²", **F.cartociudad},
        {"etiqueta": "Altitud del centro urbano", "valor": "unos 743 m", **F.copernicus},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Guadalajara · 13,8 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 65,3 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cartociudad_f, F.bmw_f, F.osrm_f, OSM, F.r461_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- Vallbona d'Anoia
CIUDADES["vallbona-d-anoia"] = {
    "h1": "Vallbona d'Anoia: tu BMW por la A-2 hasta el taller especialista, a 47,5 km",
    "entradilla": "A diferencia de los pueblos del Penedès vecinos, desde Vallbona d'Anoia al taller se va por la A-2. La ITV está en Igualada y el servicio oficial BMW más próximo, en Terrassa, en una calle que se llama precisamente Anoia.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 47.5},
    "secciones": [
        {"id": "por-la-a2", "h2": "B-224, B-231 y A-2",
         "parrafos": [
             "Desde el centro del núcleo urbano, la ruta hasta Dasercars Barcelona toma la B-224, enlaza con la B-231 y sigue por la A-2 hasta Sant Joan Despí: 47,5 km por carretera, 34,2 en línea recta. El taller está en el carrer del Tambor del Bruc 3, cerca de la salida.",
             "Vallbona no forma parte del Área Metropolitana de Barcelona, de modo que la recogida del taller no llega hasta aquí.",
         ]},
        {"id": "igualada-y-terrassa", "h2": "La ITV en Igualada, el concesionario en Terrassa",
         "parrafos": [
             "La estación más próxima por carretera en el registro de la Generalitat es ITV Igualada (B12), en el carrer Països Baixos 18, polígono industrial Les Comes, a 15,5 km. El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en el carrer Anoia 9 de Terrassa, a 38 km.",
             "Si te llega una llamada a revisión de BMW, la cita es en la red oficial. Para lo demás, el mantenimiento y las averías, la elección de taller es tuya.",
         ]},
        {"id": "pueblo-compacto", "h2": "Un pueblo compacto que no ha cambiado de tamaño",
         "parrafos": [
             "Vallbona d'Anoia tenía 1.417 habitantes en 2015 y 1.424 en 2025: un 0,5 % de variación, prácticamente estable. Su término es pequeño, 6,45 km², con 221 habitantes por kilómetro cuadrado, el doble que la vecina Cabrera d'Anoia (104). Idescat, con datos de la DGT, contaba 806 turismos en 2024: 566 por cada 1.000.",
             "La B-224 y la C-15 pasan a menos de tres kilómetros. Un coche que hace a diario el trayecto corto hacia Capellades o Piera y solo de vez en cuando sale a la A-2 agradece revisiones a tiempo de batería, frenos y aceite.",
         ]},
    ],
    "faq": [
        {"q": "¿Por dónde se va a vuestro taller desde Vallbona?",
         "a": "Por la B-224, la B-231 y la A-2: 47,5 km hasta Sant Joan Despí."},
        {"q": "¿Dónde paso la ITV?",
         "a": "En ITV Igualada (B12), polígono Les Comes, a 15,5 km: la más próxima por carretera según la Generalitat."},
        {"q": "¿Cuál es el servicio oficial BMW más cercano?",
         "a": "Quadis Munich, en el carrer Anoia 9 de Terrassa, a 38 km según bmw.es."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.424 habitantes", **F.ine},
        {"etiqueta": "Comarca", "valor": "Anoia", **F.idescat("082922")},
        {"etiqueta": "Turismos (2024)", "valor": "806 · 566 por cada 1.000 hab.", **F.idescat("082922")},
        {"etiqueta": "ITV más cercana", "valor": "Igualada (B12) · 15,5 km", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Terrassa · 38 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 47,5 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("082922"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Anchuelo
CIUDADES["anchuelo"] = {
    "h1": "Anchuelo: Alcalá para la ITV y el concesionario, Alcobendas para el especialista BMW",
    "entradilla": "Para un vecino de Anchuelo, Alcalá de Henares concentra casi todo lo que necesita un BMW: estación de ITV y servicio oficial. El taller especialista de la red está a 42,2 km, en Alcobendas.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 42.2},
    "secciones": [
        {"id": "todo-en-alcala", "h2": "Dos citas en Alcalá de Henares",
         "parrafos": [
             "Según el localizador de bmw.es, el servicio oficial BMW más cercano es AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 14,3 km por carretera. La ITV oficial más próxima del listado de la Comunidad de Madrid también está en Alcalá: TÜV SÜD ATISAE (estación 2878), en la avenida Juan Carlos I, junto al centro comercial La Garena, a unos 10 km.",
             "Tener las dos cosas en la misma ciudad permite encadenar la inspección y una visita al concesionario el mismo día, si hace falta.",
         ]},
        {"id": "m100-hacia-alcobendas", "h2": "M-213, M-100 y R-2 hasta Alcobendas",
         "parrafos": [
             "La ruta desde Anchuelo hasta la calle Valgrande 17 enlaza la M-213, la M-300 y la M-100, sigue por la R-2 y entra por la M-50: 42,2 km por carretera, 32,6 en línea recta.",
             "La recogida y el vehículo de cortesía, ambos sujetos a disponibilidad, funcionan dentro del área metropolitana de Madrid. Pregunta al pedir cita si tu dirección entra; si no, lo cómodo es dejar el coche a primera hora.",
         ]},
        {"id": "anchuelo-en-cifras", "h2": "602 turismos por cada mil vecinos",
         "parrafos": [
             "Anchuelo tenía 1.414 habitantes en 2025, un 17,8 % más que en 2015, en un término de 21,5 km² a 736 metros. La Comunidad de Madrid, con datos de la DGT, registraba 851 turismos en 2025: 602 por cada 1.000 habitantes, frente a 388 en Madrid capital.",
             "La M-213 pasa por el propio casco urbano. Para un BMW que hace casi siempre el mismo trayecto corto hasta Alcalá, lo más delicado suele ser la batería y, en diésel, el filtro de partículas: un aviso de regeneración que se repite merece una revisión.",
         ]},
    ],
    "faq": [
        {"q": "¿Dónde está el servicio oficial BMW más cercano a Anchuelo?",
         "a": "AutoPremier, en la Vía Complutense 131 de Alcalá de Henares, a 14,3 km según bmw.es."},
        {"q": "¿Qué ITV me queda más cerca?",
         "a": "La de TÜV SÜD ATISAE (estación 2878), en la avenida Juan Carlos I de Alcalá de Henares, a unos 10 km."},
        {"q": "¿Cuánto hay hasta vuestro taller?",
         "a": "42,2 km por la M-100, la R-2 y la M-50 hasta Alcobendas."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.414 habitantes (+17,8 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "851 · 602 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "TÜV SÜD ATISAE, Alcalá de Henares · unos 10 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "AutoPremier, Alcalá de Henares · 14,3 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 42,2 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}

# ---------------------------------------------------------------- el Pla del Penedès
CIUDADES["el-pla-del-penedes"] = {
    "h1": "El Pla del Penedès: la ITV a 6,6 km en línea recta, el doble por carretera",
    "entradilla": "Hay datos que engañan sobre el mapa. La estación de ITV de Olèrdola parece estar al lado del Pla del Penedès, pero por carretera son 12,6 km. El taller especialista BMW de la red queda a 45,9 km, en Sant Joan Despí.",
    "socio": {"id": "dasercars-sant-joan-despi", "kmCarretera": 45.9},
    "secciones": [
        {"id": "itv-olerdola", "h2": "Olèrdola (B09): 6,6 km en el mapa, 12,6 al volante",
         "parrafos": [
             "En el registro de la Generalitat, la estación más próxima es la de Olèrdola (B09), en la avinguda de l'Hostal Nou. En línea recta queda a 6,6 km del centro; por carretera, a 12,6 km, porque hay que rodear Vilafranca.",
             "Si el coche tiene una holgura, una luz fundida o un testigo encendido, mejor saberlo antes de pedir cita: una pre-ITV ahorra repetir el viaje.",
         ]},
        {"id": "seis-vias-al-taller", "h2": "Cinco carreteras hasta el Tambor del Bruc",
         "parrafos": [
             "La ruta hasta Dasercars Barcelona encadena la BV-2154, la C-243a, la BV-2244, la AP-7 y la B-23: 45,9 km por carretera, 29,2 en línea recta. El Pla no está en el área metropolitana de Barcelona, por lo que la recogida del taller no llega hasta aquí.",
             "Antes de ir, explica por teléfono el modelo, el año y lo que le pasa al coche; con el bastidor se puede tener la pieza correcta pedida.",
         ]},
        {"id": "vilanova-red-oficial", "h2": "La red oficial, en Vilanova i la Geltrú",
         "parrafos": [
             "El servicio oficial BMW más cercano según bmw.es es Quadis Munich, en la avinguda d'Eduard Toldrà 69 de Vilanova i la Geltrú, a 27,2 km. Para una reparación cubierta por la garantía de fábrica, el sitio es ese.",
         ]},
        {"id": "el-pla-en-cifras", "h2": "1.393 vecinos en 9,56 km²",
         "parrafos": [
             "El padrón de 2025 da al Pla del Penedès 1.393 habitantes, un 13,3 % más que en 2015, en un término pequeño, de 9,56 km², a 216 metros. Idescat, con datos de la DGT, registraba 784 turismos en 2024: 563 por cada 1.000 vecinos. La C-15 y la BP-2151 pasan a menos de tres kilómetros del centro.",
         ]},
    ],
    "faq": [
        {"q": "¿Cuál es la ITV más cercana al Pla del Penedès?",
         "a": "Olèrdola (B09), a 12,6 km por carretera según el registro de la Generalitat."},
        {"q": "¿Dónde está vuestro taller?",
         "a": "En el carrer del Tambor del Bruc 3 de Sant Joan Despí, a 45,9 km por la AP-7 y la B-23."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí: MINI comparte electrónica y motores con BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.393 habitantes (+13,3 % desde 2015)", **F.ine},
        {"etiqueta": "Comarca", "valor": "Alt Penedès", **F.idescat("081640")},
        {"etiqueta": "Turismos (2024)", "valor": "784 · 563 por cada 1.000 hab.", **F.idescat("081640")},
        {"etiqueta": "ITV más cercana", "valor": "Olèrdola (B09) · 12,6 km por carretera", **F.itv_cat},
        {"etiqueta": "Servicio oficial BMW", "valor": "Quadis Munich, Vilanova i la Geltrú · 27,2 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Sant Joan Despí · 45,9 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.idescat_f("081640"), F.itv_cat_f, F.bmw_f, F.osrm_f, F.dasercars_bcn_f],
}

# ---------------------------------------------------------------- Titulcia
CIUDADES["titulcia"] = {
    "h1": "Titulcia: de las Vegas al norte de Madrid, 56 km hasta el taller especialista BMW",
    "entradilla": "Desde Titulcia, el taller especialista BMW de la red queda en la otra punta de la región. Antes de cruzar Madrid por la A-4 y la M-30, conviene saber que la ITV la tienes en Valdemoro y el servicio oficial en Getafe.",
    "socio": {"id": "dasercars-alcobendas", "kmCarretera": 56.1},
    "secciones": [
        {"id": "cruzar-madrid", "h2": "M-404, A-4, M-30 y A-1",
         "parrafos": [
             "La ruta desde el centro del núcleo urbano hasta Dasercars Madrid sale por la M-404, sube por la A-4, cruza por la M-30 y termina en la A-1: 56,1 km por carretera, 44,8 en línea recta, hasta la calle Valgrande 17 de Alcobendas.",
             "Con esa distancia, la recogida del taller —limitada al área metropolitana de Madrid y sujeta a disponibilidad— no es algo con lo que contar. Llama con el modelo, el año y el síntoma y decide después si el viaje compensa.",
         ]},
        {"id": "valdemoro-y-getafe", "h2": "Valdemoro y Getafe, a mitad de camino",
         "parrafos": [
             "Para la inspección, el listado de la Comunidad de Madrid sitúa a 12 km por carretera la estación 2863, ITV Valdemoro, en la calle Vereda de la Solana 43-45 del polígono Las Canteras.",
             "El servicio oficial BMW más próximo en el localizador de bmw.es es Vehinter, en la carretera de Madrid a Toledo, en Getafe, a 28,6 km. Para las campañas que convoque BMW, esa es la dirección.",
         ]},
        {"id": "que-justifica", "h2": "Qué justifica los 56 kilómetros",
         "parrafos": [
             "Una avería que otro taller no ha resuelto, un diésel N57 o B57 con pérdida de potencia, un problema de emisiones (el taller tiene homologación REDISTA) o el mantenimiento de un MINI con el mismo equipo de diagnosis que un BMW. Para frenos o neumáticos, mejor algo más cerca.",
         ]},
        {"id": "titulcia-en-cifras", "h2": "Un pueblo pequeño con un coche para casi cada dos vecinos",
         "parrafos": [
             "Son 1.389 personas empadronadas en 2025 —en 2015 eran 1.234— y 812 turismos censados ese mismo año según el Instituto de Estadística de la Comunidad de Madrid, que toma el dato de la DGT. Sale a 585 coches por cada millar de habitantes en apenas 10,1 km² de término.",
             "Las dos carreteras que dan servicio al pueblo, la M-404 y la M-320, son también las que más kilómetros cortos acumulan en un coche de aquí: arranques en frío y poco tramo a régimen constante, justo lo contrario de lo que pide un diésel moderno.",
         ]},
    ],
    "faq": [
        {"q": "Vivo en Titulcia, ¿qué estación de ITV me conviene?",
         "a": "La oficial que queda más a mano por carretera es la de Valdemoro, en el polígono Las Canteras, a 12 km."},
        {"q": "¿Hay concesionario BMW cerca de las Vegas?",
         "a": "El punto oficial más próximo que da bmw.es es Vehinter, en Getafe, a 28,6 km de Titulcia."},
        {"q": "¿Trabajáis MINI?",
         "a": "Sí, con el mismo equipo de diagnosis que usamos para BMW."},
    ],
    "datos": [
        {"etiqueta": "Población (padrón 2025)", "valor": "1.389 habitantes (+12,6 % desde 2015)", **F.ine},
        {"etiqueta": "Turismos (2025)", "valor": "812 · 585 por cada 1.000 hab.", **F.cam_parque},
        {"etiqueta": "ITV oficial más cercana", "valor": "Valdemoro, polígono Las Canteras · 12 km", **F.itv_madrid},
        {"etiqueta": "Servicio oficial BMW", "valor": "Vehinter (Getafe) · 28,6 km", **F.bmw},
        {"etiqueta": "Taller de la red", "valor": "Alcobendas · 56,1 km", **F.osrm},
    ],
    "fuentes": [F.ine_f, F.cam_parque_f, F.itv_madrid_f, F.bmw_f, F.osrm_f, F.dasercars_madrid_f],
}
