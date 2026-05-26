/**
 * Configuración estática de la red BMW Taller.
 * Se importa desde layouts y pages.
 * El contenido IA por ciudad vive en src/content/cities/<slug>.json y se
 * carga vía import.meta.glob en [city].astro.
 */
export const NETWORK = {
  slug: "bmw-taller",
  domain: "bmw-taller.es",
  brand: "BMW Taller",
  sector: "taller-bmw",
  tagline: "Especialistas BMW en toda España — hasta un 50 % menos que el oficial",
  phone: "+34641161771‬",
  phoneDisplay: "641161771‬",
  whatsapp: "34641161771‬",
  email: "info@bmw-taller.es",
  heroImage: "/img/hero.webp",
} as const;

// Servicios del taller BMW (cards en #servicios). Texto base — el copy de cada
// ciudad puede sobreescribir vía content/cities/<slug>.json.
export const SERVICES = [
  {
    id: "revision",
    title: "Revisiones CBS BMW",
    icon: "🛠️",
    summary: "Aceite LL-04 homologado, filtros y los 30+ puntos del plan CBS de tu BMW. Respetamos el libro de mantenimiento sin perder la garantía.",
  },
  {
    id: "mecanica",
    title: "Mecánica especializada BMW",
    icon: "⚙️",
    summary: "Cadena de distribución N47/N57, embrague, suspensión adaptativa, transmisión ZF 8HP y Vanos/Valvetronic — con recambios OE o equivalente premium.",
  },
  {
    id: "averias",
    title: "Diagnóstico BMW (ISTA)",
    icon: "🔧",
    summary: "Lectura con software de nivel concesionario (ISTA/Rheingold). Diagnóstico real antes de presupuestar: sin cambiar piezas a ciegas.",
  },
  {
    id: "neumaticos",
    title: "Neumáticos y geometría",
    icon: "🛞",
    summary: "Run-flat y convencionales, montaje + equilibrado + alineación de dirección con valores originales BMW.",
  },
  {
    id: "electronica",
    title: "Electrónica y codificación",
    icon: "💻",
    summary: "Centralita DME/DDE, módulos de confort, iDrive, sensores de aparcamiento, ABS/DSC, airbag y retrofit de extras (Apple CarPlay, luces LED, etc.).",
  },
  {
    id: "itv",
    title: "Pre-ITV BMW",
    icon: "✅",
    summary: "Revisión exhaustiva de emisiones, luces xenón/LED adaptativas, suspensión y dirección para pasar la ITV a la primera.",
  },
] as const;

export const FAQ_BASE = [
  {
    q: "¿Pierdo la garantía BMW si llevo el coche a vuestro taller?",
    a: "No. La normativa europea de libre competencia protege tu derecho a elegir taller. Usamos recambios de calidad original y respetamos los intervalos CBS, así que tu garantía sigue intacta.",
  },
  {
    q: "¿Cuánto cuesta una revisión BMW frente al concesionario?",
    a: "Depende del modelo y del tipo de aceite (LL-01 o LL-04), pero de media ahorras entre un 30 % y un 50 % frente al precio del servicio oficial. Te damos presupuesto cerrado antes de tocar nada.",
  },
  {
    q: "¿Trabajáis con todos los modelos BMW?",
    a: "Sí: Serie 1, 2, 3, 4, 5, 6, 7, 8, X1 a X7, Z4, Serie M, y los eléctricos i3, i4, i5, i7, iX1, iX3, iX. Tanto diésel (B47, N47, N57) como gasolina (B48, N20, N55, B58, S55, S58) y eléctricos/híbridos.",
  },
  {
    q: "¿Tenéis software BMW de diagnóstico original?",
    a: "Trabajamos con ISTA (BMW Integrated Standard Toolset) y Rheingold, el mismo software de diagnóstico que usan los concesionarios oficiales. Podemos leer, codificar y programar módulos.",
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
