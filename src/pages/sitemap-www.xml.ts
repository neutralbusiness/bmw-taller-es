/**
 * Sitemap del master (www.bmw-taller.es).
 *
 * Solo URLs del propio host. El protocolo de sitemaps.org exige que todas las
 * URL de un sitemap vivan en el MISMO host, así que aquí no se listan los
 * subdominios de ciudad: cada uno declara el suyo en su robots.txt.
 *
 * Las URL salen de las páginas estáticas de public/ (cada carpeta con
 * index.html), así una página o un artículo nuevo entra sin tocar este fichero.
 * lastmod es el dateModified que la propia página declara en su JSON-LD; si no
 * lo declara, no se inventa.
 */
import type { APIRoute } from "astro";
import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join } from "node:path";
import { NETWORK } from "../lib/network.ts";

const PUBLIC = join(process.cwd(), "public");

function paginas(dir = PUBLIC, ruta = "/"): string[] {
  const out: string[] = [];
  if (existsSync(join(dir, "index.html"))) out.push(ruta);
  for (const nombre of readdirSync(dir).sort()) {
    const hijo = join(dir, nombre);
    if (statSync(hijo).isDirectory() && !nombre.startsWith(".") && nombre !== "img") {
      out.push(...paginas(hijo, `${ruta}${nombre}/`));
    }
  }
  return out;
}

function lastmod(ruta: string): string | null {
  const html = readFileSync(join(PUBLIC, ruta, "index.html"), "utf8");
  const fechas = [...html.matchAll(/"dateModified":\s*"(\d{4}-\d{2}-\d{2})/g)].map((m) => m[1]);
  return fechas.length ? fechas.sort().at(-1)! : null;
}

function prioridad(ruta: string): [string, string] {
  if (ruta === "/") return ["weekly", "1.0"];
  if (/^\/(aviso-legal|privacidad|cookies)\/$/.test(ruta)) return ["yearly", "0.3"];
  if (/^\/(talleres|taller-bmw-[a-z]+|zonas)\/$/.test(ruta)) return ["monthly", "0.9"];
  if (/^\/(servicios|modelos|motores-bmw|contacto)\/$/.test(ruta)) return ["monthly", "0.8"];
  if (ruta.startsWith("/blog/")) return ["monthly", "0.7"];
  return ["monthly", "0.6"];
}

export const GET: APIRoute = () => {
  const base = `https://www.${NETWORK.domain}`;
  const urls = paginas().map((ruta) => {
    const [changefreq, priority] = prioridad(ruta);
    const lm = lastmod(ruta);
    return `  <url>
    <loc>${base}${ruta}</loc>${lm ? `\n    <lastmod>${lm}</lastmod>` : ""}
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`;
  });

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.join("\n")}
</urlset>
`;

  return new Response(body, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600, s-maxage=86400",
    },
  });
};
