/**
 * robots.txt del master (www.bmw-taller.es).
 * Los subdominios de ciudad tienen el suyo propio en
 * src/pages/[city]/robots.txt.ts (el middleware reescribe
 * {slug}.bmw-taller.es/robots.txt → /{slug}/robots.txt).
 */
import type { APIRoute } from "astro";
import { NETWORK } from "../lib/network.ts";

export const GET: APIRoute = () => {
  const base = `https://www.${NETWORK.domain}`;
  const body = `User-agent: *
Allow: /

# AI crawlers — info estructurada en llms.txt
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: ${base}/sitemap-index.xml
`;
  return new Response(body, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=3600, s-maxage=86400",
    },
  });
};
