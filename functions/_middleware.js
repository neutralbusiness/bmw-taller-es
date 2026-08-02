/**
 * Cloudflare Pages middleware.
 *
 * El repo construye:
 *   - /        → master directorio (todas las ciudades agrupadas por CCAA)
 *   - /<slug>/ → one-page de la ciudad <slug>
 *
 * El dominio sirve:
 *   - bmw-taller.es / www.bmw-taller.es  → master directorio
 *   - <slug>.bmw-taller.es                → reescribe a /<slug>/ vía env.ASSETS
 *
 * Importante: usamos `env.ASSETS.fetch()` (binding inyectado por CF Pages) en
 * lugar de `fetch()` global. El fetch global mantiene el hostname público y
 * CF detecta loop → 403. ASSETS sirve directamente los archivos estáticos
 * construidos por el build.
 */
export async function onRequest(context) {
  const { request, next, env } = context;
  const url = new URL(request.url);
  const forwardedHost = request.headers.get("x-forwarded-host");
  const hostname = (forwardedHost || url.hostname).toLowerCase();

  // Dominio principal sin subdominio relevante → master directorio
  const isApex = hostname === "bmw-taller.es";
  const isWww = hostname === "www.bmw-taller.es";

  if (isApex) {
    // Redirige apex a www para consolidar señales SEO
    const target = new URL(url);
    target.hostname = "www.bmw-taller.es";
    return Response.redirect(target.toString(), 301);
  }

  if (isWww) {
    return next();
  }

  // Subdominio de ciudad: <slug>.bmw-taller.es
  if (hostname.endsWith(".bmw-taller.es")) {
    const subdomain = hostname.replace(/\.bmw-taller\.es$/, "");
    if (subdomain && !subdomain.includes(".") && subdomain !== "www") {
      // Assets puros (.css/.webp/.js/.svg/etc) → servir tal cual.
      // NO incluimos .txt/.xml aquí porque /llms.txt, /robots.txt, /sitemap.xml
      // deben reescribirse a /<slug>/* para servir contenido específico de ciudad.
      if (/\.(css|js|mjs|map|webp|avif|jpe?g|png|svg|gif|ico|woff2?|ttf|otf|eot|webmanifest|json)$/i.test(url.pathname)) {
        return env.ASSETS.fetch(request);
      }

      // Rutas legales compartidas: NO se reescriben a /<slug>/... — se sirven
      // desde el master (existen una sola vez en el build, con canonical a www).
      if (/^\/(aviso-legal|privacidad)\/?$/.test(url.pathname)) {
        const legal = new URL(url);
        legal.pathname = url.pathname.endsWith("/") ? url.pathname : `${url.pathname}/`;
        return env.ASSETS.fetch(new Request(legal.toString(), request));
      }

      // Rewrite interno: /<algo> o / → /<slug>/<resto>
      let rewrittenPath = url.pathname === "/" || url.pathname === ""
        ? `/${subdomain}/`
        : `/${subdomain}${url.pathname}`;

      // Asegurar trailing slash en rutas que no son archivos. Sin esto, ASSETS
      // devuelve un 308 redirect a /<slug>/path/ cuyo Location expone el prefijo
      // interno al navegador → el usuario ve /<slug>/<slug>/path/ en la barra.
      if (!rewrittenPath.endsWith("/") && !/\.\w+$/.test(rewrittenPath)) {
        rewrittenPath += "/";
      }

      const rewritten = new URL(url);
      rewritten.pathname = rewrittenPath;
      // Si la ruta no existe, ASSETS responde con dist/404.html y status 404
      // (al existir 404.html en el build, Pages desactiva el fallback SPA que
      // antes devolvía la portada con 200). Se propaga tal cual.
      return env.ASSETS.fetch(new Request(rewritten.toString(), request));
    }
  }

  // Dominio técnico *.pages.dev accedido en directo (sin X-Forwarded-Host del
  // Worker): duplica todo el contenido del build → marcar noindex. El tráfico
  // real llega siempre vía Worker con X-Forwarded-Host y no pasa por aquí.
  if (!forwardedHost && url.hostname.toLowerCase().endsWith(".pages.dev")) {
    const res = await next();
    const marked = new Response(res.body, res);
    marked.headers.set("X-Robots-Tag", "noindex");
    return marked;
  }

  // Otros casos → continuar
  return next();
}