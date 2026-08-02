/**
 * Sitemap del master (www.bmw-taller.es).
 *
 * Solo URLs del propio host: home, /zonas/ y páginas legales. El protocolo
 * de sitemaps.org exige que todas las URL de un sitemap (y los sitemaps
 * referenciados por un sitemapindex) vivan en el MISMO host, así que aquí no
 * se listan los ~561 subdominios ni sus sitemaps: cada subdominio declara el
 * suyo en su propio robots.txt ({slug}.bmw-taller.es/robots.txt) y Google los
 * descubre por los enlaces de /zonas/ y del enlazado interno entre vecinas.
 *
 * Sin lastmod: no hay fecha real de modificación de contenido en el master y
 * poner la fecha del build sería engañoso.
 */
import type { APIRoute } from "astro";
import { NETWORK } from "../lib/network.ts";

export const GET: APIRoute = () => {
  const base = `https://www.${NETWORK.domain}`;

  const urls = [
    { loc: `${base}/`, changefreq: "weekly", priority: "1.0" },
    { loc: `${base}/zonas/`, changefreq: "weekly", priority: "0.9" },
    { loc: `${base}/aviso-legal/`, changefreq: "yearly", priority: "0.3" },
    { loc: `${base}/privacidad/`, changefreq: "yearly", priority: "0.3" },
  ];

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(
    u => `  <url>
    <loc>${u.loc}</loc>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`,
  )
  .join("\n")}
</urlset>
`;

  return new Response(body, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600, s-maxage=86400",
    },
  });
};
