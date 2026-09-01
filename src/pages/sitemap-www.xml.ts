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
    { loc: `${base}/aviso-legal/`, changefreq: "yearly", priority: "0.3" },
    { loc: `${base}/blog/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/aviso-adblue-bmw-cuenta-atras/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/cada-cuanto-cambiar-aceite-bmw-cbs/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/comprar-bmw-segunda-mano-revision-pre-compra/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/garantia-bmw-taller-independiente-reglamento-461-2010/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/preparar-itv-bmw-motivos-rechazo/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/registro-bateria-bmw-por-que-es-obligatorio/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/testigo-motor-perdida-potencia-bmw/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/traqueteo-en-frio-bmw-que-significa/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/blog/volante-bimasa-bmw-sintomas/`, changefreq: "monthly", priority: "0.7" },
    { loc: `${base}/cookies/`, changefreq: "yearly", priority: "0.3" },
    { loc: `${base}/glosario-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/mapa-del-sitio/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/`, changefreq: "monthly", priority: "0.8" },
    { loc: `${base}/modelos/bmw-serie-1/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/bmw-serie-2/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/bmw-serie-3/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/bmw-serie-4/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/bmw-serie-5/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/bmw-x1/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/bmw-x3/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/modelos/bmw-x5/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/motores-bmw/`, changefreq: "monthly", priority: "0.8" },
    { loc: `${base}/motores-bmw/b47/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/motores-bmw/b57/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/motores-bmw/cadena-distribucion-n47-n57/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/motores-bmw/m47/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/motores-bmw/m57/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/motores-bmw/n47/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/motores-bmw/n57/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/preguntas-frecuentes/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/privacidad/`, changefreq: "yearly", priority: "0.3" },
    { loc: `${base}/servicios/`, changefreq: "monthly", priority: "0.8" },
    { loc: `${base}/servicios/adblue-scr-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/bateria-sistema-electrico-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/cadena-distribucion-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/chapa-y-pintura-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/diagnosis-electronica-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/embrague-volante-bimasa-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/frenos-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/mantenimiento-revisiones-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/mecanica-general-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/neumaticos-alineacion-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/pre-itv-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/servicios/turbo-bmw/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/sobre-nosotros/`, changefreq: "monthly", priority: "0.6" },
    { loc: `${base}/taller-bmw-barcelona/`, changefreq: "monthly", priority: "0.9" },
    { loc: `${base}/taller-bmw-madrid/`, changefreq: "monthly", priority: "0.9" },
    { loc: `${base}/talleres/`, changefreq: "monthly", priority: "0.9" },
    { loc: `${base}/zonas/`, changefreq: "weekly", priority: "0.9" },
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
  <url>
    <loc>${base}/llms.txt</loc>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
`;

  return new Response(body, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600, s-maxage=86400",
    },
  });
};
