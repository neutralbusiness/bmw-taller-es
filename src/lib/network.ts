/**
 * Configuración estática de la red BMW Taller.
 * Se importa desde layouts y pages.
 * El contenido IA por ciudad vive en src/content/cities/<slug>.json y se
 * carga vía import.meta.glob en [city].astro.
 */
import servicesData from "../data/services.json";

export const NETWORK = {
  slug: "bmw-taller",
  domain: "bmw-taller.es",
  brand: "BMW Taller",
  sector: "taller-bmw",
  tagline: "Red de talleres especialistas BMW y MINI, con un taller de referencia en cada zona",
  // Contacto solo por formulario (11-nov-2026, decisión de Martín): los cuatro
  // campos van vacíos. El panel los vuelve a rellenar aquí y las plantillas
  // pintan teléfono, WhatsApp o email solo cuando el valor resuelto no está vacío.
  phone: "",
  phoneDisplay: "",
  whatsapp: "",
  email: "",
  heroImage: "/img/hero.webp",
  gtmId: "GTM-MXDJ2V5T",
} as const;

// Servicios del taller BMW (cards en #servicios). Texto base — el copy de cada
// ciudad puede sobreescribir vía content/cities/<slug>.json.
// Los servicios se gestionan en el panel (Redes › Servicios), que escribe
// src/data/services.json: ahí se añaden, se editan, se ordenan y se ocultan,
// para toda la red o ciudad por ciudad. Un servicio oculto no llega al HTML.
type ServiceItem = { id: string; title: string; icon: string; summary: string; hidden?: boolean };
const SERVICES_DATA = servicesData as { services: ServiceItem[]; cities?: Record<string, string[]> };

/** Servicios visibles en toda la red. */
export const SERVICES: ServiceItem[] = SERVICES_DATA.services.filter((s) => !s.hidden);

/** Servicios visibles en una ciudad: los de la red menos los ocultos en esa ciudad. */
export function servicesFor(citySlug?: string): ServiceItem[] {
  const off = new Set((citySlug && SERVICES_DATA.cities?.[citySlug]) || []);
  return SERVICES.filter((s) => !off.has(s.id));
}

export const FAQ_BASE = [
  {
    q: "¿Pierdo la garantía BMW si llevo el coche a vuestro taller?",
    a: "No. La normativa europea de libre competencia protege tu derecho a elegir taller. Usamos recambios de calidad original y respetamos los intervalos CBS, así que tu garantía sigue intacta.",
  },
  {
    q: "¿Cuánto cuesta una revisión BMW frente al concesionario?",
    a: "Depende del modelo y del tipo de aceite (LL-01 o LL-04). Te damos presupuesto por escrito antes de tocar nada, para que puedas compararlo con el del concesionario. No es un precio cerrado: si al desmontar aparece otra avería, se para y se presupuesta aparte.",
  },
  {
    q: "¿Trabajáis con todos los modelos BMW?",
    a: "Con la gama de combustión e híbrida: Serie 1 a 8, X1 a X7, Z4, Serie M y MINI, en diésel (M47, M57, N47, N57, B47, B57), gasolina (B48, N20, N55, B58, S55, S58) e híbridos enchufables. Los 100 % eléctricos (i3, i4, iX…) no los atienden las delegaciones de Alcobendas y Sant Joan Despí.",
  },
  {
    q: "¿Tenéis software BMW de diagnóstico original?",
    a: "Trabajamos con software y equipo de diagnosis de nivel de marca, no con un lector OBD genérico: leemos las unidades de control, codificamos y programamos módulos.",
  },
  {
    q: "¿Cuánto tarda la reparación?",
    a: "Una revisión CBS estándar suele hacerse en el día. Las averías mecánicas (distribución, turbo, Vanos) llevan de uno a tres días según la pieza, y la diagnosis puede pedir dejar el coche para verlo también en frío. El taller confirma el plazo antes de empezar.",
  },
  {
    q: "¿Hay vehículo de sustitución?",
    a: "En Alcobendas y Sant Joan Despí hay vehículo de sustitución con sus propias condiciones (de pago, por días y según disponibilidad); conviene pedirlo al solicitar cita. En las demás delegaciones, pregúntalo al taller.",
  },
] as const;


/**
 * Las siete delegaciones de la red (24-nov-2026, Martín): nombre de zona, nunca el
 * nombre comercial del taller. Son los ÚNICOS teléfonos de la web.
 */
export interface Delegacion {
  id: string; nombre: string; ciudad: string; pagina: string;
  direccion: string; cp: string; municipio: string; provincia: string;
  phone: string; phoneDisplay: string; whatsapp: string; whatsappDisplay: string; email: string;
  horario: string; lat: number; lng: number;
}
export const DELEGACIONES: Delegacion[] = [
  { id: "alcobendas", nombre: "Alcobendas", ciudad: "Madrid", pagina: "/taller-bmw-madrid/", direccion: "Calle Valgrande, 17, Local", cp: "28108", municipio: "Alcobendas", provincia: "Madrid",
    phone: "+34679176858", phoneDisplay: "679 176 858", whatsapp: "34679176858", whatsappDisplay: "679 176 858", email: "info@taller-madrid.es",
    horario: "Lunes a viernes, 9:00–14:00 y 15:00–18:00", lat: 40.53717, lng: -3.65107 },
  { id: "sant-joan-despi", nombre: "Sant Joan Despí", ciudad: "Barcelona", pagina: "/taller-bmw-barcelona/", direccion: "Carrer del Tambor del Bruc, 3, Local", cp: "08970", municipio: "Sant Joan Despí", provincia: "Barcelona",
    phone: "+34631687779", phoneDisplay: "631 687 779", whatsapp: "34631687779", whatsappDisplay: "631 687 779", email: "info@tallerbarcelona.com",
    horario: "Lunes a viernes, 9:00–14:00 y 15:00–18:00", lat: 41.36594, lng: 2.06355 },
  { id: "nou-barris", nombre: "Nou Barris", ciudad: "Barcelona", pagina: "/taller-bmw-barcelona/#nou-barris", direccion: "Carrer de l'Escultor Llimona, 13", cp: "08031", municipio: "Barcelona", provincia: "Barcelona",
    phone: "+34934293902", phoneDisplay: "934 293 902", whatsapp: "34686619891", whatsappDisplay: "686 619 891", email: "info@tallergarrido.es",
    horario: "Lunes a viernes, 8:30–13:30 y 15:30–18:30", lat: 41.4425, lng: 2.1745 },
  { id: "poligono-francoli", nombre: "Polígono Francolí", ciudad: "Tarragona", pagina: "/taller-bmw-tarragona/", direccion: "Pol. Ind. Francolí, Parcela 9, Nau 9", cp: "43006", municipio: "Tarragona", provincia: "Tarragona",
    phone: "+34977896577", phoneDisplay: "977 89 65 77", whatsapp: "34659731615", whatsappDisplay: "659 731 615", email: "ad@carservice-francoli.com",
    horario: "Lunes a jueves, 9:00–13:00 y 15:00–19:00; viernes, 7:00–13:00", lat: 41.1235, lng: 1.2318 },
  { id: "cuarte-de-huerva", nombre: "Cuarte de Huerva", ciudad: "Zaragoza", pagina: "/taller-bmw-zaragoza/", direccion: "Carretera de Valencia, km 6,2, Nave 8", cp: "50410", municipio: "Cuarte de Huerva", provincia: "Zaragoza",
    phone: "+34614607718", phoneDisplay: "614 607 718", whatsapp: "34614607718", whatsappDisplay: "614 607 718", email: "info@asfmotors.es",
    horario: "Lunes a viernes, 9:00–13:30 y 15:00–19:00; sábados, 9:00–13:00", lat: 41.60672, lng: -0.93076 },
  { id: "zaragoza-norte", nombre: "Zaragoza Norte", ciudad: "Zaragoza", pagina: "/taller-bmw-zaragoza/#zaragoza-norte", direccion: "Calle Alcalde Francisco Caballero, 19", cp: "50015", municipio: "Zaragoza", provincia: "Zaragoza",
    phone: "+34647503521", phoneDisplay: "647 503 521", whatsapp: "34647503521", whatsappDisplay: "647 503 521", email: "avicarautomovilescenter@gmail.com",
    horario: "Lunes a viernes, 7:00–15:00", lat: 41.6705, lng: -0.8905 },
  { id: "barakaldo", nombre: "Barakaldo", ciudad: "Bizkaia", pagina: "/taller-bmw-bizkaia/", direccion: "Serralta Aldapa, 6", cp: "48903", municipio: "Barakaldo", provincia: "Bizkaia",
    phone: "+34944850645", phoneDisplay: "944 85 06 45", whatsapp: "34688620836", whatsappDisplay: "688 620 836", email: "info@autosvinor.com",
    horario: "Lunes a jueves, 8:00–13:00 y 14:00–17:00; viernes, 8:00–14:30", lat: 43.2895, lng: -2.9785 },
];
const DEL = Object.fromEntries(DELEGACIONES.map((d) => [d.id, d])) as Record<string, Delegacion>;
/** Socio del bloque `local` (JSON v3) → delegación. */
const SOCIO_A_DELEGACION: Record<string, string> = { "dasercars-sant-joan-despi": "sant-joan-despi", "dasercars-alcobendas": "alcobendas", "socio-zaragoza": "cuarte-de-huerva" };

function distKm(aLat: number, aLng: number, bLat: number, bLng: number): number {
  const r = Math.PI / 180;
  const dLat = (bLat - aLat) * r, dLng = (bLng - aLng) * r;
  const h = Math.sin(dLat / 2) ** 2 + Math.cos(aLat * r) * Math.cos(bLat * r) * Math.sin(dLng / 2) ** 2;
  return 12742 * Math.asin(Math.sqrt(h));
}
function masCercana(ids: string[], lat?: number, lng?: number): Delegacion {
  const c = ids.map((i) => DEL[i]);
  if (typeof lat !== "number" || typeof lng !== "number") return c[0];
  return c.reduce((a, b) => (distKm(lat, lng, a.lat, a.lng) <= distKm(lat, lng, b.lat, b.lng) ? a : b));
}
export interface CiudadZona { ccaa?: string; province?: string; lat?: number; lng?: number; local?: { socio?: { id?: string } } | null }
/**
 * Delegación que atiende una ciudad:
 *   · Comunidad de Madrid → Alcobendas
 *   · provincia de Barcelona → Sant Joan Despí o Nou Barris, la más cercana
 *   · provincia de Tarragona → Polígono Francolí
 *   · Aragón → Cuarte de Huerva o Zaragoza Norte, la más cercana
 *   · País Vasco → Barakaldo
 *   · resto de España → ninguna (solo formulario): los teléfonos de una zona no
 *     salen en webs de otra (norma del 21-oct-2026).
 */
export function delegacionPara(c?: CiudadZona | null): Delegacion | null {
  if (!c) return null;
  const pv = (c.province || "").toLowerCase(), cc = (c.ccaa || "").toLowerCase();
  // Dentro de su zona, las ciudades con texto local (v3) conservan el taller que ya nombran.
  const s = c.local?.socio?.id ? SOCIO_A_DELEGACION[c.local.socio.id] : undefined;
  if (cc.includes("madrid") || pv === "madrid") return DEL["alcobendas"];
  if (pv === "barcelona") return s === "sant-joan-despi" ? DEL[s] : masCercana(["sant-joan-despi", "nou-barris"], c.lat, c.lng);
  if (pv === "tarragona") return DEL["poligono-francoli"];
  if (cc.includes("arag")) return s === "cuarte-de-huerva" ? DEL[s] : masCercana(["cuarte-de-huerva", "zaragoza-norte"], c.lat, c.lng);
  if (cc.includes("vasco") || cc.includes("euskadi") || ["bizkaia", "vizcaya", "gipuzkoa", "guipúzcoa", "álava", "araba"].includes(pv)) return DEL["barakaldo"];
  return null;
}

/**
 * Contacto de una página: el valor de la ciudad (bloque `tenant` activo del
 * JSON, que escribe el panel, o los campos `custom*`) y, si está vacío, el de
 * la red (NETWORK). Con todo vacío la web solo ofrece el formulario; en cuanto
 * el panel vuelve a publicar un teléfono, un WhatsApp o un email, reaparece
 * sin tocar código.
 */
export interface ContactSource {
  tenant?: { active?: boolean; phone?: string; phoneDisplay?: string; whatsapp?: string; email?: string } | null;
  customPhone?: string;
  customPhoneDisplay?: string;
  customWhatsapp?: string;
  customEmail?: string;
}

export interface Contact {
  /** Teléfono en formato tel: (+34…). "" si no hay. */
  phone: string;
  phoneDisplay: string;
  /** Número de WhatsApp sin signos (34…). "" si no hay. */
  whatsapp: string;
  email: string;
}

const clean = (v: unknown): string => (typeof v === "string" ? v.trim() : "");

export function contactFor(city?: (ContactSource & CiudadZona) | null): Contact {
  const t = city?.tenant && city.tenant.active ? city.tenant : null;
  const d = delegacionPara(city);
  if (d && !clean(t?.phone) && !clean(city?.customPhone)) {
    return { phone: d.phone, phoneDisplay: d.phoneDisplay, whatsapp: d.whatsapp, email: d.email };
  }
  const phone = clean(t?.phone) || clean(city?.customPhone) || clean(NETWORK.phone);
  const phoneDisplay =
    (clean(t?.phone) && clean(t?.phoneDisplay)) ||
    (clean(city?.customPhone) && clean(city?.customPhoneDisplay)) ||
    clean(NETWORK.phoneDisplay) ||
    phone;
  return {
    phone,
    phoneDisplay: phone ? phoneDisplay || phone : "",
    whatsapp: (clean(t?.whatsapp) || clean(city?.customWhatsapp) || clean(NETWORK.whatsapp)).replace(/[^0-9]/g, ""),
    email: clean(t?.email) || clean(city?.customEmail) || clean(NETWORK.email),
  };
}

/** Página del formulario de la raíz (las ciudades llevan el suyo en #formulario). */
export const FORM_URL = `https://www.${NETWORK.domain}/contacto/#formulario`;
