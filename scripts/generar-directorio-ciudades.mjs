/**
 * Genera /zonas/ (directorio de las ciudades de la red) y añade el mismo
 * listado al /mapa-del-sitio/, con el diseño real de la web.
 *
 * Por qué existe: la raíz de bmw-taller.es es el sitio estático de Dasercars
 * y no sabe nada de los 561 subdominios de ciudad. Había una página
 * `src/pages/zonas.astro` que sí los listaba, pero se construía con el layout
 * antiguo, así que era una isla con otro diseño, sin enlace en el menú y
 * ausente del mapa del sitio.
 *
 * Se ejecuta en cada build (`prebuild`), así que las ciudades que se añadan
 * en el futuro entran solas: la fuente es src/content/cities/*.json.
 */
import { readFile, writeFile, readdir, mkdir } from "node:fs/promises";
import path from "node:path";

const RAIZ = path.resolve(import.meta.dirname, "..");
const PUBLIC = path.join(RAIZ, "public");
/** Página que se usa como molde: aporta cabecera, pie, CSS y scripts. */
const MOLDE = path.join(PUBLIC, "preguntas-frecuentes", "index.html");
const DOMINIO = "bmw-taller.es";
const BASE = `https://www.${DOMINIO}`;

const esc = (s) =>
  String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

async function leerCiudades() {
  const dir = path.join(RAIZ, "src", "content", "cities");
  const files = (await readdir(dir)).filter((f) => f.endsWith(".json"));
  const ciudades = [];
  for (const f of files) {
    ciudades.push(JSON.parse(await readFile(path.join(dir, f), "utf8")));
  }
  return ciudades;
}

/** Agrupa por provincia y ordena todo alfabéticamente en español. */
function agrupar(ciudades) {
  const porProvincia = new Map();
  for (const c of ciudades) {
    const p = c.province || "Otras";
    if (!porProvincia.has(p)) porProvincia.set(p, { ccaa: c.ccaa, ciudades: [] });
    porProvincia.get(p).ciudades.push(c);
  }
  for (const v of porProvincia.values()) {
    v.ciudades.sort((a, b) => a.name.localeCompare(b.name, "es"));
  }
  return [...porProvincia.entries()].sort((a, b) => a[0].localeCompare(b[0], "es"));
}

function bloqueProvincias(grupos) {
  return grupos
    .map(([prov, { ccaa, ciudades }]) => {
      const enlaces = ciudades
        .map((c) => `<li><a href="https://${c.slug}.${DOMINIO}/">${esc(c.name)}</a></li>`)
        .join("");
      return (
        `<section class="zn__prov">` +
        `<h3 class="zn__prov-h">${esc(prov)}<span class="zn__ccaa">${esc(ccaa || "")}</span>` +
        `<span class="zn__n">${ciudades.length}</span></h3>` +
        `<ul class="zn__list">${enlaces}</ul></section>`
      );
    })
    .join("");
}

const ESTILOS = `<style>
.zn__intro{max-width:70ch}
.zn__grid{display:grid;gap:1.75rem 2.5rem;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));margin-top:2.25rem}
.zn__prov{break-inside:avoid}
.zn__prov-h{display:flex;align-items:baseline;gap:.5rem;font-size:1rem;margin:0 0 .5rem;padding-bottom:.4rem;border-bottom:1px solid rgba(255,255,255,.12)}
.zn__ccaa{font-size:.72rem;font-weight:400;opacity:.55}
.zn__n{margin-left:auto;font-size:.72rem;opacity:.55;font-variant-numeric:tabular-nums}
.zn__list{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:.15rem .7rem}
.zn__list li{font-size:.92rem}
.zn__list a{opacity:.82;text-decoration:none}
.zn__list a:hover{opacity:1;text-decoration:underline}
</style>`;

async function main() {
  const ciudades = await leerCiudades();
  const grupos = agrupar(ciudades);
  const total = ciudades.length;
  const molde = await readFile(MOLDE, "utf8");

  const titulo = `Talleres BMW por provincia · ${total} ciudades | Dasercars`;
  const descripcion =
    `Directorio completo: ${total} ciudades con página propia de taller especialista BMW, ` +
    `agrupadas por provincia. Entra en la de tu ciudad y pide cita.`;
  const canonica = `${BASE}/zonas/`;

  // ── <head> ──
  let html = molde;
  html = html.replace(/<title>[\s\S]*?<\/title>/, `<title>${esc(titulo)}</title>`);
  html = html.replace(
    /<meta name="description" content="[^"]*">/,
    `<meta name="description" content="${esc(descripcion)}">`,
  );
  html = html.replace(/https:\/\/www\.bmw-taller\.es\/preguntas-frecuentes\//g, canonica);
  html = html.replace(
    /<meta property="og:title" content="[^"]*">/,
    `<meta property="og:title" content="${esc(titulo)}">`,
  );
  html = html.replace(
    /<meta property="og:description" content="[^"]*">/,
    `<meta property="og:description" content="${esc(descripcion)}">`,
  );
  html = html.replace(
    /<meta name="twitter:title" content="[^"]*">/,
    `<meta name="twitter:title" content="${esc(titulo)}">`,
  );
  html = html.replace(
    /<meta name="twitter:description" content="[^"]*">/,
    `<meta name="twitter:description" content="${esc(descripcion)}">`,
  );

  // El JSON-LD del molde describe la FAQ; aquí sobra y se sustituye por el
  // de una página de colección con sus migas de pan.
  const schema = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "CollectionPage",
        "@id": `${canonica}#webpage`,
        url: canonica,
        name: titulo,
        description: descripcion,
        inLanguage: "es-ES",
        isPartOf: { "@id": `${BASE}/#website` },
      },
      {
        "@type": "BreadcrumbList",
        "@id": `${canonica}#breadcrumb`,
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Inicio", item: `${BASE}/` },
          { "@type": "ListItem", position: 2, name: "Talleres BMW por provincia", item: canonica },
        ],
      },
    ],
  };
  html = html.replace(
    /<script type="application\/ld\+json">[\s\S]*?<\/script>/,
    `<script type="application/ld+json">${JSON.stringify(schema)}</script>`,
  );

  // ── <main> ──
  const main =
    `<main id="main">
<nav class="crumbs wrap" aria-label="Migas de pan"><ol><li><a href="/">Inicio</a></li><li><span aria-current="page">Talleres BMW por provincia</span></li></ol></nav>
<section class="hero"><div class="wrap hero__in"><div class="hero__copy">
<p class="eyebrow">Cobertura</p>
<h1 class="hero__title">Talleres BMW<br><em>por provincia</em></h1>
<p class="hero__sub">Tenemos página propia en ${total} ciudades, con los precios, los tiempos y las averías más frecuentes de cada zona. Entra en la tuya y pide cita.</p>
</div></div></section>
<section class="wrap sec">
<p class="zn__intro">Los dos talleres físicos están en Madrid y Barcelona; desde ahí atendemos al resto de España. Cada ciudad tiene su propia página con la información de la zona.</p>
<div class="zn__grid">${bloqueProvincias(grupos)}</div>
</section>
</main>`;
  html = html.replace(/<main id="main">[\s\S]*?<\/main>/, main);
  html = html.replace("</head>", `${ESTILOS}</head>`);

  await mkdir(path.join(PUBLIC, "zonas"), { recursive: true });
  await writeFile(path.join(PUBLIC, "zonas", "index.html"), html, "utf8");

  // ── Mapa del sitio: mismo listado, para que no se quede fuera ──
  const mapaRuta = path.join(PUBLIC, "mapa-del-sitio", "index.html");
  let mapa = await readFile(mapaRuta, "utf8");
  const MARCA_INI = "<!-- ciudades:inicio -->";
  const MARCA_FIN = "<!-- ciudades:fin -->";
  const seccion =
    `${MARCA_INI}<section class="sec"><h2>Talleres por ciudad <span class="zn__n">${total}</span></h2>` +
    `<p class="zn__intro">Cada ciudad tiene su propia página. Listado completo en ` +
    `<a href="/zonas/">talleres BMW por provincia</a>.</p>` +
    `<div class="zn__grid">${bloqueProvincias(grupos)}</div></section>${MARCA_FIN}`;

  if (mapa.includes(MARCA_INI)) {
    mapa = mapa.replace(new RegExp(`${MARCA_INI}[\\s\\S]*?${MARCA_FIN}`), seccion);
  } else {
    // Se cuelga al final del <main>, antes de cerrarlo.
    const cierre = mapa.lastIndexOf("</main>");
    if (cierre < 0) throw new Error("mapa-del-sitio: no encuentro </main>");
    mapa = mapa.slice(0, cierre) + seccion + mapa.slice(cierre);
  }
  if (!mapa.includes(ESTILOS)) mapa = mapa.replace("</head>", `${ESTILOS}</head>`);
  await writeFile(mapaRuta, mapa, "utf8");

  console.log(`Directorio generado: ${total} ciudades en ${grupos.length} provincias → /zonas/ y /mapa-del-sitio/`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
