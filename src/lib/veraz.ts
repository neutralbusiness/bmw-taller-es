/**
 * Textos de ciudad sin promesas que los talleres de la red no hacen (8-nov-2026).
 *
 * Los JSON de ciudad llegaron generados con «hasta un 50 % menos que el
 * oficial», «diagnosis ISTA», «mantenimiento oficial»… Las ciudades ya no se
 * indexan en Google, pero su llms.txt y su HTML siguen alimentando a la IA y a
 * Bing: el título, la descripción y los chips no pueden prometer eso. Cuando
 * el JSON trae un texto limpio (rama contenido-ciudades), se respeta tal cual.
 */
const PROMESA = /50 ?%|-50\b|\bISTA\b|Rheingold|oficial|concesionario|gratis|gratuit|presupuesto cerrado|precio cerrado|cortes[ií]a|sin sorpresas|urgencias/i;

interface Ciudad { name: string; province: string; metaTitle: string; metaDescription: string; }

export function tituloVeraz(city: Ciudad): string {
  if (!PROMESA.test(city.metaTitle)) return city.metaTitle;
  const zona = city.province && city.province !== city.name ? ` (${city.province})` : "";
  return `Taller BMW para ${city.name}${zona} · BMW Taller`;
}

export function descripcionVeraz(city: Ciudad): string {
  if (!PROMESA.test(city.metaDescription)) return city.metaDescription;
  return `BMW Taller, red de talleres especialistas BMW y MINI, te pone en contacto con el taller de referencia de tu zona para ${city.name}. Diagnosis de nivel de marca y presupuesto por escrito.`;
}

export function chipsVeraces<T extends { text: string }>(chips?: T[]): T[] {
  return (chips ?? []).filter((c) => !PROMESA.test(c.text));
}

/**
 * Ciudades sin contenido local v3 (295 el 15-nov-2026): su texto salió de la
 * plantilla de IA y afirma cosas que no son verdad — «nuestro taller en
 * Salamanca», equipo ISTA oficial, coche de cortesía, presupuesto cerrado,
 * urgencias, horario de lunes a sábado… En esos municipios no hay taller de la
 * red. Se quitan las frases y los elementos que lo dicen; lo demás se respeta.
 */
const INVENTADO = /\bISTA\b|Rheingold|(software|equipos?|diagn[oó]stico|diagnosis|herramientas?)( de diagnosis| de diagn[oó]stico)? oficial|oficial(es)? (de )?BMW|como en (un|el) concesionario|presupuesto cerrado|precio cerrado|precio final|sin sorpresas|sobrecoste|cortes[ií]a|veh[ií]culo de sustituci|coche de sustituci|gratis|gratuit|50 ?%|la mitad|urgencias|nuestro taller|vuestro taller|nuestras instalaciones|vuestras instalaciones|nuestra ubicaci[oó]n|cada semana|recibimos habitualmente|años de experiencia|garant[ií]a de nuestro|meses de garant|recogida|a domicilio|\bi3\b|\biX\d?\b|\bi[457]\b|100 ?% el[eé]ctric|Lunes a S[aá]bado|nuestro equipo|nuestros t[eé]cnicos|certificad/i;

export const esInventado = (t: string): boolean => INVENTADO.test(t);

export function textoVeraz(t: string | undefined): string {
  if (!t) return "";
  return t
    .split(/\n\n/)
    .map((p) => p.split(/(?<=[.!?…])\s+/).filter((s) => s.trim() && !INVENTADO.test(s)).join(" "))
    .filter(Boolean)
    .join("\n\n");
}

interface Pregunta { q: string; a: string }
interface Bloque { title: string; body: string }
interface CiudadVieja {
  name: string;
  heroSubtitle: string;
  introLocal: string | string[];
  servicesIntro: string;
  servicesOverrides?: Record<string, string>;
  processIntro?: string;
  processSteps?: Bloque[];
  commonIssuesIntro?: string;
  commonIssues?: Bloque[];
  whyUs: Bloque[];
  zoneText: string;
  faqLocal: Pregunta[];
  closingHeadline?: string;
  closingCta: string;
}

export function ciudadVeraz<T extends CiudadVieja>(c: T): T {
  const intro = Array.isArray(c.introLocal) ? c.introLocal.join("\n\n") : c.introLocal;
  const bloques = (xs?: Bloque[]) =>
    (xs ?? [])
      .filter((x) => !INVENTADO.test(x.title))
      .map((x) => ({ ...x, body: textoVeraz(x.body) }))
      .filter((x) => x.body);
  const overrides = Object.fromEntries(
    Object.entries(c.servicesOverrides ?? {}).map(([k, v]) => [k, textoVeraz(v)]).filter(([, v]) => v),
  );
  return {
    ...c,
    heroSubtitle: textoVeraz(c.heroSubtitle) || `Red de talleres especialistas BMW y MINI. Cuéntanos qué le pasa a tu BMW desde ${c.name}.`,
    introLocal: textoVeraz(intro),
    servicesIntro: textoVeraz(c.servicesIntro),
    servicesOverrides: overrides,
    processIntro: textoVeraz(c.processIntro),
    processSteps: bloques(c.processSteps),
    commonIssuesIntro: textoVeraz(c.commonIssuesIntro),
    commonIssues: bloques(c.commonIssues),
    whyUs: bloques(c.whyUs),
    zoneText: textoVeraz(c.zoneText),
    faqLocal: (c.faqLocal ?? []).filter((f) => !INVENTADO.test(f.q) && !INVENTADO.test(f.a)),
    closingHeadline: c.closingHeadline && !/lleva tiempo buscando|el taller BMW que/i.test(c.closingHeadline) && !INVENTADO.test(c.closingHeadline) ? c.closingHeadline : "Cuéntanos qué le pasa a tu BMW",
    closingCta: textoVeraz(c.closingCta) || "Pide presupuesto por el formulario",
  };
}
