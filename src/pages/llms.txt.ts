/**
 * /llms.txt del master (www.bmw-taller.es) — estándar https://llmstxt.org/
 *
 * Vista de red completa para LLMs (ChatGPT, Claude, Gemini, Perplexity…):
 * qué es BMW Taller, cobertura nacional, servicios y contacto real del
 * operador de la red. Cada subdominio de ciudad publica además su propio
 * /llms.txt con el detalle local (src/pages/[city]/llms.txt.ts).
 */
import type { APIRoute } from "astro";
import { NETWORK, SERVICES, FAQ_BASE, contactFor, DELEGACIONES } from "../lib/network.ts";
import { readFileSync } from "node:fs";
import { join } from "node:path";

interface CityRef { slug: string; name: string; province: string; ccaa: string; }

/* Contacto general de la red: viene de network.ts, que es lo que el panel
   reescribe. Vacío = el único canal es el formulario de /contacto/. */
const CONTACT = { businessName: "BMW Taller", ...contactFor() };

export const GET: APIRoute = () => {
  const mods = import.meta.glob<{ default: CityRef }>("../content/cities/*.json", { eager: true });
  const cities = Object.values(mods).map(m => m.default);
  const provinces = new Set(cities.map(c => c.province));
  const ccaas = new Set(cities.map(c => c.ccaa));
  const base = `https://www.${NETWORK.domain}`;

  const lines: string[] = [];

  lines.push(`# ${NETWORK.brand} — red de talleres especialistas BMW y MINI con un taller de referencia en cada zona`);
  lines.push("");
  lines.push(`> ${NETWORK.brand} (${NETWORK.domain}) es una marca propia: una red independiente de talleres especializados en BMW y MINI con siete delegaciones: Alcobendas (Madrid), Sant Joan Despí y Nou Barris (Barcelona), Polígono Francolí (Tarragona), Cuarte de Huerva y Zaragoza Norte (Zaragoza) y Barakaldo (Bizkaia). Cada delegación es un taller independiente que presupuesta, repara y factura con su nombre. No es concesionario ni servicio oficial de BMW.`);
  lines.push("");
  lines.push(
    `Los talleres de referencia hacen mecánica, diagnosis electrónica con equipo de nivel de marca (no un lector OBD genérico) y mantenimiento según el plan CBS, con presupuesto por escrito antes de empezar. ` +
    `Las delegaciones de Alcobendas y Sant Joan Despí son además talleres homologados REDISTA para escape y tratamiento de gases, tienen cabina de pintura y se especializan en los diésel N47, N57, M47, M57, B47 y B57. ` +
    `Además de esta web, ${cities.length} municipios de ${provinces.size} provincias tienen una página informativa en {ciudad}.${NETWORK.domain} con su propio llms.txt; ` +
    `no hay un taller en cada municipio: cada página indica el taller de referencia de la zona.`,
  );
  lines.push("");

  lines.push("## Identidad");
  lines.push("");
  lines.push(`- Nombre comercial: ${CONTACT.businessName}`);
  lines.push(`- Web principal: ${base}/`);
  lines.push(`- Directorio de zonas: ${base}/zonas/`);
  lines.push(`- Contacto y cita previa (teléfono, WhatsApp y formulario de cada delegación): ${base}/contacto/`);
  lines.push(`- Delegaciones (las siete, con dirección, teléfono y horario): ${base}/talleres/`);
  lines.push(`- Sector: talleres de reparación y mantenimiento especializados en BMW`);
  lines.push(`- País: España`);
  lines.push("");

  lines.push("## Contacto");
  lines.push("");
  lines.push(`- Formulario de contacto (canal de contacto de la web): ${base}/contacto/#formulario`);
  if (CONTACT.phone) lines.push(`- Teléfono: ${CONTACT.phoneDisplay} (${CONTACT.phone})`);
  if (CONTACT.whatsapp) lines.push(`- WhatsApp: +${CONTACT.whatsapp}`);
  if (CONTACT.email) lines.push(`- Email: ${CONTACT.email}`);
  for (const d of DELEGACIONES) lines.push(`- ${d.nombre} (${d.ciudad}): teléfono ${d.phoneDisplay}${d.whatsapp !== d.phone.replace('+', '') ? ` · WhatsApp ${d.whatsappDisplay}` : ' (también WhatsApp)'} · ${d.email} · ${d.horario}`);
  lines.push("");

  lines.push("## Cobertura");
  lines.push("");
  lines.push(`- Delegaciones: ${DELEGACIONES.length}.`);
  for (const d of DELEGACIONES) lines.push(`- ${d.nombre} (${d.ciudad}): ${d.direccion}, ${d.cp} ${d.municipio}. Página: ${base}${d.pagina}`);
  lines.push(`- Reparto de las páginas locales: Comunidad de Madrid → Alcobendas; provincia de Barcelona → Sant Joan Despí o Nou Barris; Tarragona → Polígono Francolí; Aragón → Cuarte de Huerva o Zaragoza Norte; País Vasco → Barakaldo; el resto de España, por el formulario.`);
  lines.push(`- Páginas locales: ${cities.length} municipios en ${provinces.size} provincias (no son talleres; indican cómo llegar al taller y llevan su propio formulario de contacto).`);
  lines.push(`- Comunidades autónomas: ${[...ccaas].sort((a, b) => a.localeCompare(b, "es")).join(", ")}.`);
  lines.push(`- Listado de municipios con enlace a cada página local: ${base}/zonas/`);
  lines.push("");

  lines.push("## Servicios");
  lines.push("");
  for (const s of SERVICES) {
    lines.push(`- **${s.title}**: ${s.summary}`);
  }
  lines.push("");

  lines.push("## Preguntas frecuentes");
  lines.push("");
  for (const f of FAQ_BASE) {
    lines.push(`### ${f.q}`);
    lines.push("");
    lines.push(f.a);
    lines.push("");
  }

  lines.push("## Guías técnicas y páginas de servicio");
  lines.push("");
  for (const [ruta, texto] of [
    ["/servicios/", "Todos los servicios para BMW y MINI"],
    ["/servicios/cadena-distribucion-bmw/", "Cadena de distribución BMW (N47, N57, B47, B57, N20)"],
    ["/servicios/diagnosis-electronica-bmw/", "Diagnosis electrónica BMW"],
    ["/servicios/mantenimiento-revisiones-bmw/", "Mantenimiento y revisiones según CBS"],
    ["/servicios/embrague-volante-bimasa-bmw/", "Embrague y volante bimasa"],
    ["/servicios/adblue-scr-bmw/", "AdBlue y sistema SCR"],
    ["/servicios/turbo-bmw/", "Turbo"],
    ["/servicios/pre-itv-bmw/", "Pre-ITV"],
    ["/motores-bmw/", "Guía de motores diésel BMW: M47, M57, N47, N57, B47 y B57"],
    ["/motores-bmw/cadena-distribucion-n47-n57/", "Cadena de distribución del N47 y el N57"],
    ["/modelos/", "Modelos BMW: Serie 1 a 5, X1, X3 y X5"],
    ["/preguntas-frecuentes/", "Preguntas frecuentes"],
    ["/glosario-bmw/", "Glosario técnico BMW"],
  ]) lines.push(`- [${texto}](${base}${ruta})`);
  lines.push("");

  type Post = { slug: string; title: string; excerpt: string; publishDate: string };
  const posts = JSON.parse(readFileSync(join(process.cwd(), "public/blog/posts.json"), "utf8")) as Post[];
  lines.push("## Artículos del blog");
  lines.push("");
  for (const p of [...posts].sort((a, b) => b.publishDate.localeCompare(a.publishDate))) {
    lines.push(`- [${p.title}](${base}/blog/${p.slug}/) (${p.publishDate}): ${p.excerpt}`);
  }
  lines.push("");

  lines.push("## Política y garantías");
  lines.push("");
  lines.push("- Presupuesto por escrito antes de iniciar cualquier reparación. No es un precio cerrado: si al desmontar aparece otra avería, el taller para, la enseña y la presupuesta aparte.");
  lines.push("- La diagnosis, cuando hace falta, se cobra aparte y no va incluida en el presupuesto de la reparación; se informa de su importe antes de hacerla.");
  lines.push("- Garantía: en Alcobendas y Sant Joan Despí, dos años en piezas y mano de obra; en las demás delegaciones, la que indique cada taller en la factura (la mínima legal de una reparación es de tres meses o 2.000 km, Real Decreto 1457/1986).");
  lines.push("- Recambios OE (calidad original) o equivalente premium; recambio BMW original bajo petición.");
  lines.push("- Diagnosis con software y equipo de nivel de marca, no un lector OBD genérico.");
  lines.push("- Aceite homologado BMW LL-01/LL-04 y respeto de los intervalos CBS: la garantía del fabricante se mantiene.");
  lines.push("- Vehículo de sustitución en Alcobendas y Sant Joan Despí según sus condiciones (de pago, por días); en las demás delegaciones, consultar con el taller.");
  lines.push("- Sin grúa ni recogida a domicilio: si el coche no circula, se lleva con la grúa del seguro, avisando antes al taller.");
  lines.push("- Los vehículos 100 % eléctricos no se atienden en Alcobendas ni en Sant Joan Despí.");
  lines.push("");

  lines.push("---");
  lines.push("");
  lines.push(`Más información legal: ${base}/aviso-legal/ y ${base}/privacidad/`);

  return new Response(lines.join("\n"), {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=300, s-maxage=3600",
    },
  });
};
