import type { APIRoute, GetStaticPaths } from "astro";
import { getCollection } from "astro:content";
import { NETWORK } from "../../lib/network.ts";

interface CityRef { slug: string; }

export const getStaticPaths: GetStaticPaths = async () => {
  const mods = import.meta.glob<{ default: CityRef }>("../../content/cities/*.json", { eager: true });
  return Object.values(mods).map(m => ({ params: { city: m.default.slug } }));
};

export const GET: APIRoute = async ({ params }) => {
  const base = `https://${params.city}.${NETWORK.domain}`;

  // Blog posts visibles para esta ciudad = específicos de la ciudad + globales
  const all = await getCollection("blog");
  const cityPosts = all.filter(p => {
    const parts = p.id.split("/");
    if (parts.length === 1) return true;     // global
    return parts[0] === params.city;          // city-specific
  });

  /*
   * Reglas SEO del sitemap:
   *  - Solo páginas HTML indexables (nada de /llms.txt: no es una página).
   *  - /blog/ y sus posts solo si esta ciudad tiene posts visibles; un blog
   *    vacío en el sitemap son URLs fantasma.
   *  - lastmod solo cuando hay fecha real de contenido (posts). Para la
   *    portada no la tenemos, y poner la fecha del build sería engañoso →
   *    se omite.
   */
  const urls: string[] = [];

  urls.push(`  <url>
    <loc>${base}/</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>`);

  if (cityPosts.length > 0) {
    const newest = cityPosts
      .map(p => (p.data.updatedDate || p.data.publishDate))
      .sort((a, b) => b.getTime() - a.getTime())[0]
      .toISOString()
      .slice(0, 10);

    urls.push(`  <url>
    <loc>${base}/blog/</loc>
    <lastmod>${newest}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>`);

    for (const p of cityPosts) {
      const slug = p.id.split("/").pop();
      const last = (p.data.updatedDate || p.data.publishDate).toISOString().slice(0, 10);
      urls.push(`  <url>
    <loc>${base}/blog/${slug}/</loc>
    <lastmod>${last}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>`);
    }
  }

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
