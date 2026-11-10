/**
 * Textos de ciudad sin promesas que los talleres de la red no hacen (8-nov-2026).
 *
 * Los JSON de ciudad llegaron generados con «hasta un 50 % menos que el
 * oficial», «diagnosis ISTA», «mantenimiento oficial»… Las ciudades ya no se
 * indexan en Google, pero su llms.txt y su HTML siguen alimentando a la IA y a
 * Bing: el título, la descripción y los chips no pueden prometer eso. Cuando
 * el JSON trae un texto limpio (rama contenido-ciudades), se respeta tal cual.
 */
const PROMESA = /50 ?%|-50\b|\bISTA\b|Rheingold|oficial|concesionario|gratis|gratuit/i;

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
