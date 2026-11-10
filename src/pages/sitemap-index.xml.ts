/**
 * Sitemap Index (www.bmw-taller.es/sitemap-index.xml)
 *
 * Solo referencia el sitemap del propio www. Desde el 8-nov-2026 las
 * ciudades llevan noindex para Google (penalización de la spam update de
 * septiembre): enviarlas aquí hacía que Search Console las marcara como
 * «URL enviada marcada como noindex». Cada ciudad conserva su sitemap y su
 * robots.txt propios (Bing y rastreadores de IA) y su llms.txt.
 *
 * Spec: https://www.sitemaps.org/protocol.html#index
 * "A Sitemap index file can include Sitemaps that are provided on
 *  different hosts, as long as both hosts are verified in Search Console."
 */
import type { APIRoute } from "astro";
import { NETWORK } from "../lib/network.ts";

export const GET: APIRoute = async () => {
  const base = `https://www.${NETWORK.domain}`;

  const entries = [
    `  <sitemap>\n    <loc>${base}/sitemap-www.xml</loc>\n  </sitemap>`,
  ];

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${entries.join("\n")}
</sitemapindex>
`;

  return new Response(body, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600, s-maxage=86400",
    },
  });
};
