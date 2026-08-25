/**
 * /llms.txt del master (www.bmw-taller.es) — estándar https://llmstxt.org/
 *
 * Vista de red completa para LLMs (ChatGPT, Claude, Gemini, Perplexity…):
 * qué es BMW Taller, cobertura nacional, servicios y contacto real del
 * operador de la red. Cada subdominio de ciudad publica además su propio
 * /llms.txt con el detalle local (src/pages/[city]/llms.txt.ts).
 */
import type { APIRoute } from "astro";
import { NETWORK, SERVICES, FAQ_BASE } from "../lib/network.ts";

interface CityRef { slug: string; name: string; province: string; ccaa: string; }

/* Datos de contacto del operador real de la red (el mismo tenant "BMW Taller"
   que atiende los subdominios contratados). */
const CONTACT = {
  businessName: "BMW Taller",
  phoneDisplay: "641 161 771",
  phone: "+34641161771",
  whatsapp: "34641161771",
  email: "info@bmw-taller.es",
};

export const GET: APIRoute = () => {
  const mods = import.meta.glob<{ default: CityRef }>("../content/cities/*.json", { eager: true });
  const cities = Object.values(mods).map(m => m.default);
  const provinces = new Set(cities.map(c => c.province));
  const ccaas = new Set(cities.map(c => c.ccaa));
  const base = `https://www.${NETWORK.domain}`;

  const lines: string[] = [];

  lines.push(`# ${NETWORK.brand} — red de talleres especialistas BMW en España`);
  lines.push("");
  lines.push(`> ${NETWORK.tagline}. Red nacional con presencia en ${cities.length} ciudades de ${provinces.size} provincias (${ccaas.size} comunidades autónomas).`);
  lines.push("");
  lines.push(
    `${NETWORK.brand} es una red de talleres especializados en la marca BMW. ` +
    `Diagnóstico con software BMW ISTA/Rheingold de nivel concesionario, recambios OE o equivalente premium y presupuesto cerrado por escrito antes de cualquier intervención — con un ahorro de hasta el 50 % frente al servicio oficial. ` +
    `Cada ciudad de la red tiene su propia web en {ciudad}.${NETWORK.domain} con información local detallada y su propio llms.txt.`,
  );
  lines.push("");

  lines.push("## Identidad");
  lines.push("");
  lines.push(`- Nombre comercial: ${CONTACT.businessName}`);
  lines.push(`- Web principal: ${base}/`);
  lines.push(`- Directorio de zonas: ${base}/zonas/`);
  lines.push(`- Sector: talleres de reparación y mantenimiento especializados en BMW`);
  lines.push(`- País: España`);
  lines.push("");

  lines.push("## Contacto");
  lines.push("");
  lines.push(`- Teléfono: ${CONTACT.phoneDisplay} (${CONTACT.phone})`);
  lines.push(`- WhatsApp: +${CONTACT.whatsapp}`);
  lines.push(`- Email: ${CONTACT.email}`);
  lines.push(`- Horario: Lunes a Sábado · 08:00–20:00`);
  lines.push("");

  lines.push("## Cobertura");
  lines.push("");
  lines.push(`- ${cities.length} ciudades con taller en ${provinces.size} provincias.`);
  lines.push(`- Comunidades autónomas: ${[...ccaas].sort((a, b) => a.localeCompare(b, "es")).join(", ")}.`);
  lines.push(`- Listado completo de ciudades con enlace a cada web local: ${base}/zonas/`);
  lines.push("");

  lines.push("## Servicios");
  lines.push("");
  for (const s of SERVICES) {
    lines.push(`- **${s.title}**: ${s.summary}`);
  }
  lines.push("");

  lines.push("## Preguntas frecuentes");
  lines.push("");
  for (const f of FAQ_BASE) {
    lines.push(`### ${f.q}`);
    lines.push("");
    lines.push(f.a);
    lines.push("");
  }

  lines.push("## Política y garantías");
  lines.push("");
  lines.push("- Presupuesto cerrado por escrito antes de iniciar cualquier reparación; sin sobrecostes no autorizados.");
  lines.push("- Recambios OE (calidad original) o equivalente premium; recambio BMW original bajo petición.");
  lines.push("- Diagnóstico con software BMW ISTA/Rheingold de nivel concesionario.");
  lines.push("- Aceite homologado BMW LL-01/LL-04 y respeto de los intervalos CBS: la garantía del fabricante se mantiene.");
  lines.push("- Factura desglosada en la entrega.");
  lines.push("");

  lines.push("---");
  lines.push("");
  lines.push(`Más información legal: ${base}/aviso-legal/ y ${base}/privacidad/`);

  return new Response(lines.join("\n"), {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=300, s-maxage=3600",
    },
  });
};
