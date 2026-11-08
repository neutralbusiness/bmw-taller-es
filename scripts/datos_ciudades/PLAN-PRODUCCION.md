# Plan de producción — contenido local v3 (fase 2)

Estado al cerrar la fase 1 (04-oct-2026, rama `contenido-ciudades`):
20 ciudades piloto escritas e integradas; plantilla `[city].astro` con el
bloque `local` (v3) que convive con el formato antiguo; datos verificados de
las 575 ciudades en `datos/`; validador y comprobador de similitud.

## Qué queda

| Grupo | Ciudades | Qué se hace |
|---|---|---|
| Activas con taller que las atiende (cola) | **503** | Fase 2: tandas 1-34 de `tandas.csv` (15 por tanda; la 34 tiene 8) |
| Publicadas pero desactivadas en el panel, con taller que las atiende | 9 (Getafe, Móstoles, Alcalá de Henares, Leganés, Fuenlabrada, Alcorcón, Tarragona, Lleida, Chamartín) | Tanda 35 |
| Activas sin taller de la red en su zona | 5 (`jaen`, `cadiz`, `ourense`, `barakaldo`, `orihuela`) | Esperar decisión de Martin |
| Capitales publicadas, desactivadas en el panel y sin taller de la red | 37 (lista en `COBERTURA.md`) | Igual que las anteriores: decisión de Martin |
| Duplicado | `arganda` (= `arganda-del-rey`) | Propuesta: 301 a `arganda-del-rey` vía `RETIRED_CITIES`; no se reescribe |

Orden de `tandas.csv` (lo pidió Martin): primero las **196 sin impresiones**,
de más a menos población; después las **307 con impresiones**, también por
población. Las 6 que no son municipio (barrios) están en la cola marcadas
con su `tipo`.

## Organización

- **15 ciudades por agente** (una tanda). Es lo que cabe con calidad: unas
  7.000-9.000 palabras escritas a mano por respuesta.
- **6 agentes en paralelo por ronda** → 6 rondas (35 tandas).
- Cada agente trabaja en su **propio worktree y rama**
  `contenido-ciudades-tNN`, creada desde `contenido-ciudades`, y solo crea o
  modifica:
  - `scripts/datos_ciudades/tandas/tanda_NN.py` (sus 15 bloques),
  - `src/content/cities/<slug>.json` de **sus** 15 slugs.
  Nada más: ni la plantilla, ni `comun.py`, ni los datos. Así no hay
  conflictos de fusión (un JSON por ciudad, ficheros disjuntos).
- Si un agente encuentra un dato malo en `datos/<slug>.json`, **no lo arregla**:
  lo anota en su informe y deja esa ciudad fuera de la tanda.

## Verificación de cada tanda (antes de fusionar)

El agente entrega, y el coordinador repite:

1. `python3 scripts/datos_ciudades/validar_local.py <15 slugs>` → 0 errores y
   cada aviso de cifras justificado.
2. `npm run build; echo "exit $?"` → `exit 0` (nunca `| tail`, que da falso OK).
3. `python3 scripts/datos_ciudades/similitud.py --solo <slugs>` → máximo en
   `<main>` < 25 % contra **todas** las páginas; y `--zona editorial` < 15 %.
4. Revisión humana de 3 de las 15 al azar contra su `datos/<slug>.json`
   (cada cifra, cada nombre de ITV, cada dirección).
5. `git diff --stat` solo muestra los 15 JSON + `tanda_NN.py`.

## Al cerrar cada ronda (6 tandas)

1. Fusionar las 6 ramas en `contenido-ciudades` (sin conflictos esperables).
2. Build + `similitud.py --zona editorial` sobre **todas** las páginas con
   contenido v3 (`--solo $(ls de slugs con local)`): detecta frases que se
   repiten entre agentes distintos. Si una frase aparece en más de 10 páginas,
   se añade a la lista de «gastadas» de `GUIA-REDACCION.md` §6 antes de la
   ronda siguiente y se corrige en las afectadas.
3. Volver a ejecutar `p09_gsc.py` y `p10_ensamblar.py` solo si ha pasado más de
   un mes (las consultas cambian; los datos oficiales no).

## Publicación

- Nada va a `main` hasta que Martin vea el piloto en la vista previa de
  Cloudflare Pages de la rama `contenido-ciudades` y dé el visto bueno.
- Cuando lo dé: fusionar a `main` **por rondas completas**, no ciudad a ciudad
  (la memoria de la spam update dice: todos los cambios de una vez y luego
  dejar el sitio en paz 2-3 meses).
- Tras publicar, cada `<slug>/llms.txt` refleja ya el contenido v3 (lo genera
  `src/pages/[city]/llms.txt.ts`).

## Decisiones pendientes de Martin (bloquean partes del plan)

1. **Ciudades sin taller de la red** (5 activas + 37 capitales desactivadas en el
   panel pero publicadas, p. ej. Huelva, Cádiz, Algeciras, Jerez, Valladolid,
   Granada, Málaga): hoy dicen «recibimos clientes de Huelva capital». O se les
   da una página honesta («no hay taller de la red cerca; el más próximo es
   Dasercars Madrid a N km; consulta telefónica»), o se buscan socios, o se
   retiran. Varias están entre las que más visitas reciben de Google.
2. **Socio de Zaragoza**: si tiene dirección pública, añadirla en
   `src/lib/socios.ts` y en `comun.py → SOCIOS` y regenerar `p07`/`p10`; las
   15 páginas de Zaragoza ganarían ruta y LocalBusiness.
3. **Titles con promesas sin respaldo** («hasta -50%» en Sentmenat, «Mantenimiento
   oficial» en Barcelona y Vilafranca, «diagnosis ISTA» en varias): no se han
   tocado porque la norma era no cambiar titles de ciudades con impresiones.
4. **Barrios** (`chamartin`, `ciudad-lineal`, `el-goloso`, `las-matas`,
   `llefia`, `vilaseca`): reescribirlos como barrio o redirigirlos al municipio.
5. **Las 555 páginas antiguas** siguen publicando un horario inventado
   («Lunes a Sábado · 08:00–20:00»; JSON-LD 9-18 L-V y sábados) y un
   `AutoRepair` con la localidad de la ciudad. Las v3 ya usan el horario y la
   dirección reales del taller. Se corrigen solas al pasar cada ciudad a v3.

---

## Instrucciones para copiar a cada agente de tanda

> Sustituye `NN` por el número de tanda.

```
Responde en español. Eres el redactor de la TANDA NN del contenido local de
bmw-taller.es (taller especialista BMW/MINI; Dasercars). Martin ha pedido
contenido real y único por ciudad.

1. Prepara tu espacio (worktree propio, nunca `git add -A`):
   cd ~/Sites/bmw-taller-es && git fetch && git worktree add ../bmw-tNN -b contenido-ciudades-tNN origin/contenido-ciudades
   cd ../bmw-tNN && npm ci
2. Lee ENTERAS: scripts/datos_ciudades/GUIA-REDACCION.md, README.md y los
   cuatro ficheros del piloto scripts/datos_ciudades/piloto/lote_0*.py.
3. Copia las consultas de Search Console (no se versionan, el repo es público):
   mkdir -p scripts/datos_ciudades/cache && cp ~/Sites/bmw-taller-es/scripts/datos_ciudades/cache/paso_gsc.json scripts/datos_ciudades/cache/
   Tus 15 ciudades: awk -F, '$1==NN {print $2}' scripts/datos_ciudades/tandas.csv
   Para cada una: python3 scripts/datos_ciudades/resumen.py <slug> y lee
   scripts/datos_ciudades/datos/<slug>.json. SOLO esos datos (y las excepciones
   de la guía §1). Si un dato no está, no se escribe.
4. Escribe TÚ el texto (sin APIs de IA) en scripts/datos_ciudades/tandas/tanda_NN.py
   con el mismo formato que los lotes del piloto (from fuentes import F; añade
   sys.path al directorio piloto si hace falta). Estructura según los datos
   (guía §3), longitud según el tamaño, nada de frases de la lista §6.
5. Aplica: python3 scripts/datos_ciudades/piloto/aplicar.py tanda_NN
6. Verifica (guía §7): validar_local.py → 0 errores; npm run build; echo "exit $?"
   → 0; similitud.py --solo <tus slugs> → <main> < 25 % y --zona editorial < 15 %.
7. git add scripts/datos_ciudades/tandas/tanda_NN.py src/content/cities/<cada slug>.json
   git commit -m "Contenido local v3: tanda NN (15 ciudades)"
   git push -u origin contenido-ciudades-tNN     (NUNCA a main)
8. Informe final: slugs hechos, palabras por ciudad, máximo de similitud
   (main y editorial), avisos de cifras justificados, y cualquier dato de
   datos/<slug>.json que te pareciera erróneo (sin corregirlo).
```
