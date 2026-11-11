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
    a: "Depende del modelo y del tipo de aceite (LL-01 o LL-04). Te damos presupuesto cerrado por escrito antes de tocar nada, para que puedas compararlo con el del concesionario.",
  },
  {
    q: "¿Trabajáis con todos los modelos BMW?",
    a: "Sí: Serie 1, 2, 3, 4, 5, 6, 7, 8, X1 a X7, Z4, Serie M, y los eléctricos i3, i4, i5, i7, iX1, iX3, iX. Tanto diésel (B47, N47, N57) como gasolina (B48, N20, N55, B58, S55, S58) y eléctricos/híbridos.",
  },
  {
    q: "¿Tenéis software BMW de diagnóstico original?",
    a: "Trabajamos con software y equipo de diagnosis de nivel de marca, no con un lector OBD genérico: leemos las unidades de control, codificamos y programamos módulos.",
  },
  {
    q: "¿Cuánto tarda la reparación?",
    a: "Para una revisión CBS estándar, en el día. Las averías mecánicas (distribución, turbo, Vanos) suelen ser 1-3 días según disponibilidad de pieza. Te confirmamos plazo antes de empezar.",
  },
  {
    q: "¿Coche de cortesía?",
    a: "Si la reparación se alarga más de un día, te ofrecemos coche de cortesía sujeto a disponibilidad.",
  },
] as const;


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

export function contactFor(city?: ContactSource | null): Contact {
  const t = city?.tenant && city.tenant.active ? city.tenant : null;
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
