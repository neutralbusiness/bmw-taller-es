/**
 * /llms.txt del master (www.bmw-taller.es) — estándar https://llmstxt.org/
 *
 * Vista de red completa para LLMs (ChatGPT, Claude, Gemini, Perplexity…):
 * qué es BMW Taller, cobertura nacional, servicios y contacto real del
 * operador de la red. Cada subdominio de ciudad publica además su propio
 * /llms.txt con el detalle local (src/pages/[city]/llms.txt.ts).
 */
import type { APIRoute } from "astro";
import { NETWORK, SERVICES, FAQ_BASE, DELEGACIONES } from "../lib/network.ts";

interface CityRef { slug: string; name: string; province: string; ccaa: string; }

/* Contacto general de la red: viene de network.ts, que es lo que el panel
   reescribe al cambiar el teléfono. Antes estaba copiado aquí a mano y se
   quedaba desactualizado. */
const CONTACT = {
  businessName: "BMW Taller",
  phoneDisplay: NETWORK.phoneDisplay,
  phone: NETWORK.phone,
  whatsapp: NETWORK.whatsapp,
  email: NETWORK.email,
};

export const GET: APIRoute = () => {
  const mods = import.meta.glob<{ default: CityRef }>("../content/cities/*.json", { eager: true });
  const cities = Object.values(mods).map(m => m.default);
  const provinces = new Set(cities.map(c => c.province));
  const ccaas = new Set(cities.map(c => c.ccaa));
  const base = `https://www.${NETWORK.domain}`;

  const lines: string[] = [];

  lines.push(`# ${NETWORK.brand} (Dasercars) — taller especialista BMW y MINI en Madrid y Barcelona`);
  lines.push("");
  lines.push(`> Dasercars es un taller especialista en BMW y MINI con dos naves propias: Alcobendas (Madrid) y Sant Joan Despí (Barcelona). Taller homologado REDISTA para sistemas de escape y tratamiento de gases; especialidad en los motores diésel N47, N57, M47, M57, B47 y B57.`);
  lines.push("");
  lines.push(
    `Mecánica, diagnosis electrónica con software y equipo de nivel de marca (no un lector OBD genérico), mantenimiento según el plan CBS y chapa y pintura con cabina propia. ` +
    `Mecánicos en plantilla; la reparación no se subcontrata. Presupuesto cerrado por escrito antes de empezar. ` +
    `Además de esta web, ${cities.length} municipios de ${provinces.size} provincias tienen una página informativa en {ciudad}.${NETWORK.domain} con su propio llms.txt; ` +
    `no hay un taller en cada municipio: los clientes de esas zonas se atienden en los dos talleres.`,
  );
  lines.push("");

  lines.push("## Identidad");
  lines.push("");
  lines.push(`- Nombre comercial: ${CONTACT.businessName}`);
  lines.push(`- Web principal: ${base}/`);
  lines.push(`- Directorio de zonas: ${base}/zonas/`);
  lines.push(`- Contacto y cita previa (Madrid y Barcelona, llamada o WhatsApp): ${base}/contacto/`);
  lines.push(`- Sector: talleres de reparación y mantenimiento especializados en BMW`);
  lines.push(`- País: España`);
  lines.push("");

  lines.push("## Contacto");
  lines.push("");
  // Dos delegaciones: son los únicos teléfonos (llamada y WhatsApp).
  for (const d of [DELEGACIONES.madrid, DELEGACIONES.barcelona]) {
    lines.push(`- Teléfono y WhatsApp ${d.nombre}: ${d.phoneDisplay} (${d.phone})`);
  }
  lines.push(`- Email: ${CONTACT.email}`);
  lines.push(`- Horario (talleres Dasercars de Alcobendas y Sant Joan Despí): De lunes a viernes de 09:00h a 14:00h y de 15:00h a 18:00h (sábado cerrado)`);
  lines.push("");

  lines.push("## Cobertura");
  lines.push("");
  lines.push(`- Talleres físicos: 2, propios. Calle Valgrande, 17, 28108 Alcobendas (Madrid) y Carrer del Tambor del Bruc, 3, 08970 Sant Joan Despí (Barcelona).`);
  lines.push(`- Páginas locales: ${cities.length} municipios en ${provinces.size} provincias (no son talleres; indican cómo llegar al taller y a quién llamar).`);
  lines.push(`- Comunidades autónomas: ${[...ccaas].sort((a, b) => a.localeCompare(b, "es")).join(", ")}.`);
  lines.push(`- Listado de municipios con enlace a cada página local: ${base}/zonas/`);
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
  lines.push("- Presupuesto cerrado por escrito antes de iniciar cualquier reparación.");
  lines.push("- Recambios OE (calidad original) o equivalente premium; recambio BMW original bajo petición.");
  lines.push("- Diagnosis con software y equipo de nivel de marca, no un lector OBD genérico.");
  lines.push("- Aceite homologado BMW LL-01/LL-04 y respeto de los intervalos CBS: la garantía del fabricante se mantiene.");
  lines.push("- Vehículo de cortesía sujeto a disponibilidad; conviene reservarlo al pedir cita.");
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
