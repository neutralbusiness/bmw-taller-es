# Datos verificados por ciudad — bmw-taller.es

Pipeline reproducible (Python 3, solo biblioteca estándar + `curl`) que genera,
para cada una de las 575 páginas de ciudad del repo (529 activas en el panel),
un fichero `datos/<slug>.json` con datos públicos y **la fuente de cada uno**.
Es la única materia prima que pueden usar los redactores de contenido local
(ver `GUIA-REDACCION.md`). Cobertura de cada campo: `COBERTURA.md`.

## Ejecutar

```bash
cd ~/Sites/neutralb-panel && set -a && . ./.env.local && set +a   # Supabase + AGENT_RUN_SECRET
cd ~/Sites/bmw-taller-es/scripts/datos_ciudades
python3 p01_base.py                 # ciudades del repo + estado/INE del panel
python3 p02_ine.py                  # población (INE, padrón)
python3 p03_geo.py                  # término municipal (CartoCiudad), superficie, altitud
python3 p03b_nucleo.py              # núcleo urbano (CartoCiudad): origen de rutas si el punto del repo cae fuera del casco
python3 p04_bmw_oficial.py          # red oficial BMW (localizador de bmw.es)
python3 p05_itv.py                  # estaciones ITV (redes oficiales + OSM marcado)
python3 p06_estadistica_regional.py # Idescat (Cataluña) y parque de turismos de Madrid
python3 p07_rutas.py                # distancias por carretera (OSRM) — ~10 min
python3 p08_vias_costa.py           # carreteras cercanas y costa (OSM/Overpass)
python3 p09_gsc.py                  # consultas reales de Search Console por subdominio
python3 p10_ensamblar.py            # datos/<slug>.json, datos/_indice.csv, COBERTURA.md
```

Todo lo descargado queda en `cache/` (no versionado): volver a ejecutar un paso
no repite peticiones. Para refrescar un dato, borra su fichero de `cache/`.
`datos/` sí se versiona: es lo que leen los agentes.

## Fuentes

| Dato | Fuente | Notas |
|---|---|---|
| Población y evolución a 10 años | INE, Revisión del Padrón Municipal, tabla 29005 | último año publicado (2025) |
| Código INE | panel (`network_cities.ine_code`), comprobado contra el nombre oficial del INE | 1 corregido (La Llagosta) |
| Término municipal, superficie, comprobación de coordenadas | CartoCiudad (IGN/CNIG) | 5 coordenadas del repo caían fuera de su municipio: corregidas |
| Altitud | Idescat (Cataluña); fuera, MDT Copernicus vía Open-Meteo | |
| Comarca | Idescat (solo Cataluña tiene comarcas oficiales en la red) | |
| Parque de turismos | Idescat a partir de DGT (Cataluña, 2024); Instituto de Estadística de la Comunidad de Madrid a partir de DGT (2025) | resto: sin fuente municipal abierta cargada |
| Taller que atiende la zona | JSON-LD de `/taller-bmw-madrid/` y `/taller-bmw-barcelona/` + teléfono por zona del panel | Zaragoza: sin dirección publicada |
| Distancia por carretera y vías de la ruta | OSRM (router.project-osrm.org) sobre OpenStreetMap | no se publica el tiempo (estimación sin tráfico). Origen: el punto de la página, o el centro del núcleo urbano (CartoCiudad, `p03b`) si el punto cae fuera del casco a más de 1 km (`distancias_desde` en el fichero) |
| Servicio oficial BMW más cercano | localizador de concesionarios de bmw.es (puntos con taller, rama «T») | solo como referencia, nunca para desprestigiar. Fuera: Andorra (Pyrénées Motors sale con país «ES») y centros de ocasión sin taller comprobado (AutoPremier La Garena, Movilnorte El Carralero…; lista en `p04`). Más cercano: ruta más corta (alternativas de OSRM) entre los 6 más próximos en línea recta; `casi_igual_de_cerca` si otro queda a < 1 km |
| ITV | Generalitat (dades obertes 7dyp-y4dd), Comunidad de Madrid (listado oficial), aragon.es (municipios); resto OSM con `verificar: true` | Cataluña: coordenadas del campo `localitzador_a_google_maps` (los campos lat/long pierden el punto decimal). Madrid: geocodificadas por dirección o punto kilométrico (CartoCiudad); 10 estaciones solo con precisión de municipio (`precision`). «En el municipio» = municipio de la lista oficial (código INE), no el polígono. Más cercana: ruta más corta (alternativas de OSRM, no solo la más rápida) entre las 8 más próximas en línea recta; `casi_igual_de_cerca` si otra queda a < 1 km. Direcciones de la Generalitat limpiadas (comillas escapadas, «l¿estació») y municipios con el artículo delante («les Borges Blanques») |
| Carreteras a < 3 km, costa a < 5 km | OpenStreetMap (Overpass); costa: Natural Earth 10m | autopista, autovía, primaria y secundaria con referencia, medidas sobre el trazado (no el centro del tramo) |
| Búsquedas reales | Google Search Console vía panel | solo en `cache/paso_gsc.json` (no se versiona: el repo es público); orientan el texto, no se listan |

## Avisos que salen de los datos (revisar con Martin)

- **Seis subdominios no son municipios** (`chamartin`, `ciudad-lineal`, `el-goloso`,
  `las-matas`, `llefia`, `vilaseca`): sus JSON publicaban la población del
  municipio entero (Las Matas = 99.037, que es Las Rozas). En `vilaseca` la cifra
  era la de Vila-seca (Tarragona). Su texto debe decir «barrio de…».
  Desde el 04-oct-2026 su `population` heredada (17.305 en Vilaseca, 14.213 en Las Matas…) se ha quitado
  también de `src/content/cities/` aunque aún no estén escritas, y en `cercanas_red` se marcan con
  `tipo`/`pertenece_a` y no aparecen como «cercanos» de su propio municipio (Vilaseca en Orís).
- **Borredà y Perafita** tienen la misma población (433, padrón 2025) y los mismos turismos (259,
  Idescat 2024): comprobado en las dos fuentes, es una coincidencia real (la evolución a 10 años es distinta).
- **`arganda` y `arganda-del-rey` son el mismo municipio** con dos subdominios.
  Propuesta: 301 de `arganda` a `arganda-del-rey` (mecanismo `RETIRED_CITIES`).
- **Ciudades sin taller de la red en su zona** (capitales con teléfono general,
  p. ej. Cádiz, Jaén, Huelva…): el texto actual dice que «recibimos clientes de
  Huelva capital». No se pueden reescribir con datos reales sin decidir antes
  qué se les ofrece (ver `PLAN-PRODUCCION.md`).
- La población del JSON de muchas ciudades está desfasada respecto al padrón
  2025: al reescribir una ciudad se actualiza `population` con `datos/<slug>.json`.

## Similitud: línea base y piloto (04-oct-2026)

Medido con `similitud.py` (Jaccard de shingles de 5 palabras sobre `<main>`,
topónimos y cifras enmascarados; máximo de cada página contra las 575):

| | media | mediana | p90 | máx | páginas > 25 % |
|---|---|---|---|---|---|
| Línea base (antes de tocar nada) | 40,3 % | 41,0 % | 75,5 % | 97,7 % (cardona/moia) | 354 de 575 |
| Las 20 del piloto, antes | 36,4 % | — | — | 81,4 % (sentmenat) | — |
| Las 20 del piloto, después (`<main>`) | 14,9 % | 14,7 % | 18,6 % | 19,0 % | 0 |
| Las 20 del piloto, después (solo bloque editorial) | 5,3 % | 5,2 % | 6,8 % | 8,0 % | 0 |

El residuo en `<main>` es la carcasa común de las páginas v3 (ficha de datos,
tarjeta de contacto, municipios cercanos); el texto editorial comparte < 10 %.
