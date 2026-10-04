# Guía de redacción — contenido local v3 de bmw-taller.es

Para los agentes que escriben las páginas de ciudad. Léela entera antes de la
primera ciudad. El piloto (20 ciudades, `piloto/lote_01.py` a `lote_04.py`) es
la referencia de tono y de método.

## 0. Lo que estamos haciendo y por qué

Google penaliza **lotes** de páginas casi iguales aunque estén «humanizadas»
(ver memoria `feedback_spam_update_paginas_masivas`). Las 575 páginas de ciudad
eran la misma plantilla con el nombre cambiado (similitud media 40 %, máxima
97,7 %). La solución NO es reescribir con sinónimos: es que cada página cuente
cosas **verdaderas, comprobables y distintas** para el dueño de un BMW o MINI
de ese municipio. Si no hay nada verdadero que decir, la página es corta; no se
rellena.

## 1. Materia prima: SOLO `datos/<slug>.json`

- Abre `datos/<slug>.json` (o `python3 resumen.py <slug>` para verlo legible).
- **Lo que no está en ese fichero no existe para el texto.** Ni población «de
  memoria», ni «la autovía que pasa cerca», ni «el polígono de…».
- Excepciones permitidas (conocimiento general verificable, sin cifras locales):
  - Normativa: Reglamento (UE) 461/2010 (mantenimiento fuera de la red oficial
    sin perder la garantía si se respeta el plan); RD 920/2017 (ITV de turismos:
    exento hasta 4 años, bienal de 4 a 10, anual desde 10).
  - Hechos del negocio publicados en la raíz (www.bmw-taller.es): dos talleres
    propios (Alcobendas y Sant Joan Despí), horario L-V 9-14 y 15-18, presupuesto
    por escrito y nada se empieza sin aprobación, la diagnosis se presupuesta,
    trabajan MINI, homologación REDISTA (escape y gases), especialidad diésel
    N47/N57/M47/M57/B47/B57, vehículo de cortesía y recogida/entrega **dentro del
    área metropolitana de Madrid y de Barcelona, sujeto a disponibilidad**.
  - Mecánica general BMW verdadera (registro de batería, líquido de frenos por
    tiempo, regeneración del filtro de partículas, salitre y corrosión…), sin
    cifras de averías ni estadísticas «del taller».
  - Geografía básica indiscutible (capital de provincia, capital de comarca,
    pertenencia al AMB —lista oficial de 36 municipios—).
- Si dudas de un dato: fuera.

### Avisos del fichero que mandan sobre el texto
- `tipo` ≠ `municipio` (6 barrios/distritos): se dice «barrio de X», **no** se
  da población, superficie ni turismos (serían los del municipio entero).
- `taller_que_atiende.id = null` (capitales sin taller de la red): **no se
  escriben** hasta que Martin decida qué se les ofrece (ver PLAN).
- `socio-zaragoza`: no hay dirección publicada. Se dice «taller asociado de la
  red en Zaragoza» y «al llamar te indican dónde llevar el coche». Ni dirección
  ni distancia.
- ITV con `verificar: true` (OpenStreetMap): solo se publica tras confirmarla
  en la web del operador; y entonces sin número de portal si hay dudas, y nunca
  como «la más cercana» (OSM no está completo) → «una estación cercana es…».
- ITV de Cataluña y Madrid: listas oficiales. Aun así **no afirmes que un
  municipio «no tiene ITV»**; di «la más próxima en el registro de la
  Generalitat es…».
- `turismos.por_1000_hab` > 800: hay flotas domiciliadas (Brunete da 4.374).
  No uses la proporción; como mucho la cifra absoluta.
- Distancias: publica km por carretera (`km_carretera`) o en línea recta, nunca
  **tiempos** (OSRM no conoce el tráfico).

## 2. Qué se escribe y dónde

En `piloto/lote_NN.py` (o el fichero de tu tanda, mismo formato) defines un
dict por ciudad y lo aplicas con `piloto/aplicar.py`, que lo vuelca al campo
`local` de `src/content/cities/<slug>.json`, actualiza `population` con el
padrón (o la quita en barrios) y corrige coordenadas si el pipeline lo marcó.

```python
CIUDADES["slug"] = {
  "h1": "...",                      # propio, ≤ 90 caracteres, con BMW y el municipio
  "entradilla": "...",              # 2-3 frases: qué hay y dónde está el taller
  "socio": {"id": "dasercars-alcobendas", "kmCarretera": 37.0},   # del fichero de datos; sin km en Zaragoza
  "secciones": [ {"id": "kebab-case", "h2": "...", "parrafos": ["...", "..."], "lista": ["opcional"]} ],  # 3-6
  "faq": [ {"q": "...", "a": "..."} ],      # 3-5, con datos de la ciudad
  "datos": [ {"etiqueta": "...", "valor": "...", **F.ine} ],       # 4-6 filas, cada una con su fuente
  "fuentes": [F.ine_f, ...],                # las que no estén ya en `datos` se listan al pie
}
```

**No toques**: `slug`, `name`, `metaTitle`, `tenant`, el resto de campos
antiguos (se quedan como respaldo pero no se pintan). `metaDescription` solo se
reescribe en ciudades **sin impresiones** en GSC y si contiene una promesa
(«hasta un 50 %», «oficial»…); en las que tienen impresiones, no se toca.

## 3. Estructura: la deciden los datos, no un molde

Escoge 3-6 secciones de este catálogo **según lo que haya de verdad**. Orden y
títulos libres; los H2 se escriben cada vez (nunca «Por qué elegirnos», «Nuestros
servicios», «Zona de cobertura»…).

| Tipo de sección | Cuándo usarla | Datos que la alimentan |
|---|---|---|
| Lo que se busca desde aquí | consultas de Search Console claras (las muestra `resumen.py`, desde `cache/paso_gsc.json`): concesionario, «talleres en X», MINI, precios | aclarar honestamente qué es esto y qué no |
| Ruta al taller | siempre que haya socio con dirección | `km_carretera`, `km_linea_recta`, `vias_de_la_ruta` |
| Cuándo compensa el viaje / cuándo no | `distancia_taller` media o lejos (40+ km) | km + servicios del taller |
| Recogida y cortesía | solo municipios del AMB o del área metropolitana de Madrid, con «sujeto a disponibilidad» | FAQ de la raíz |
| ITV | estación en el municipio (lista) o la más próxima | `itv.en_el_municipio`, `itv.mas_cercana` |
| Servicio oficial y taller independiente | siempre útil, sin desprestigiar | `bmw_servicio_oficial_mas_cercano` (+ 461/2010 **solo si no se ha usado ya en tu tanda más de 1 de cada 5 veces**) |
| El parque de coches / la población | hay turismos o una evolución llamativa | `poblacion`, `turismos` |
| Costa | `costa.a_menos_de_5km` | salitre: bajos, discos de un coche parado, conectores |
| Altitud | `altitud_m` > 800 | frío: batería y su registro, anticongelante, frenos en bajada |
| Barrio | `tipo` ≠ municipio | «barrio de X», sin cifras municipales |

Longitud (secciones + FAQ + entradilla, lo mide `validar_local.py`):
- pueblo pequeño sin ITV ni consultas: 350-450 palabras;
- municipio medio: 400-550;
- ciudad o capital con varias ITV, consultas y servicio oficial: 550-700.
Nunca más de 750. Si para llegar a 350 tienes que rellenar, quédate en 350 con
datos y no inventes.

## 4. Tono

El de la raíz (Dasercars): tú, directo, técnico sin jerga gratuita, frases
cortas, honesto aunque no venda. Toponimia como en el fichero de datos (en
catalán los municipios catalanes: Sant Boi de Llobregat, Vilafranca del Penedès).
Cifras con punto de miles y coma decimal (3.506.730; 20,5 km).

## 5. Prohibido (lo comprueba `validar_local.py`, pero no te fíes solo de él)

- Opiniones, reseñas, valoraciones, testimonios, «clientes satisfechos».
- Precios o importes; «hasta un 50 % más barato» ni ningún porcentaje de ahorro.
- Tiempos de viaje («a 20 minutos»).
- Presencia física falsa: «nuestro taller de X», «estamos en X», «recibimos
  muchos clientes de X», «Hecho en X».
- «Taller oficial»; somos taller independiente. ISTA/Rheingold (no está
  acreditado en la web de Dasercars).
- Recogida a domicilio fuera del área metropolitana o sin «sujeto a
  disponibilidad»; coche de sustitución garantizado.
- Cifras de negocio: años de experiencia, número de clientes, «desde 2009».
- Superlativos sin dato: «el municipio que más crece», «más coches que en
  ningún sitio». Si quieres comparar, compara con una cifra del fichero de
  datos de otra ciudad («casi el doble que en Madrid capital, 388»).
- Hablar de Search Console o de «las búsquedas que llegan aquí». Usa las
  consultas para elegir el ángulo, no para contarlas.
- Listas de barrios o municipios sin nada detrás (keyword stuffing).
- Muletillas: «en el corazón de», «sin lugar a dudas», «cabe destacar»,
  «amplia experiencia», «equipo de profesionales».

## 6. Anti-plantilla: las frases que ya están gastadas

Estas ideas aparecen en el piloto. Puedes usar la idea, **nunca la misma
redacción**, y cada una como mucho en 1 de cada 5 páginas de tu tanda:
- la explicación del Reglamento 461/2010;
- la periodicidad de la ITV (4/2/10 años) — mejor no explicarla: ya está en
  Madrid y Barcelona;
- «presupuesto por escrito y ningún trabajo empieza sin tu aprobación»;
- «llama antes con modelo, año, kilometraje (y bastidor)»;
- «las campañas del fabricante se hacen en la red oficial»;
- el horario completo del taller (ya sale en la tarjeta de contacto).

Varía también la **apertura** de la entradilla (no empieces todas por el nombre
del municipio + «tiene…») y el **orden** de las secciones.

### Bueno / malo

Malo (plantilla con hueco):
> «Sentmenat es una localidad con carácter propio. Los propietarios de BMW de
> la zona merecen un servicio a la altura, sin pagar las tarifas del
> concesionario.»

Bueno (dato + consecuencia práctica):
> «Según el localizador de bmw.es, el punto de servicio oficial más próximo a
> Sentmenat es Tallcar, un taller autorizado BMW en la calle Suiza 6 de
> Castellar del Vallès, a 6,6 km. Para una campaña de revisión del fabricante es
> la opción lógica por cercanía.»

Malo (invención verosímil):
> «Muchos coches de Getafe hacen a diario la A-42, un uso que acelera el
> desgaste del turbo.»

Bueno (dato verificable, sin estadística inventada):
> «Con la A-2 a menos de tres kilómetros del centro, es fácil que un diésel haga
> de vez en cuando el recorrido a régimen constante que necesita para regenerar
> el filtro de partículas.»

Malo (honestidad al revés):
> «Recibimos clientes de Huelva capital y de Punta Umbría.»

Bueno (honesto aunque no venda):
> «En Lozoyuela-Navas-Sieteiglesias no tenemos taller. El que atiende la zona
> está en Alcobendas, a 52,4 km por la A-1. Para un pinchazo te conviene un
> taller del valle; para una avería concreta de BMW, sí tiene sentido bajar.»

## 7. Comprobación por ciudad (obligatoria antes de dar la tanda por buena)

```bash
cd ~/Sites/bmw-taller-es
python3 scripts/datos_ciudades/piloto/aplicar.py lote_NN
python3 scripts/datos_ciudades/validar_local.py <slugs de la tanda>    # 0 errores; revisa los avisos de cifras uno a uno
npm run build; echo "exit $?"                                         # exit code real, sin | tail
python3 scripts/datos_ciudades/similitud.py --solo <slugs,separados,por,comas>              # <main>: máx < 25 %
python3 scripts/datos_ciudades/similitud.py --zona editorial --solo <slugs>                  # editorial: máx < 15 %
```

Cada aviso «cifras no encontradas» se justifica (cifra de otra ciudad citada
como comparación, redondeo explícito con «casi/unos») o se corrige.
