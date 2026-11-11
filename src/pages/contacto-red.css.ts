import type { APIRoute } from "astro";
import { contactFor } from "../lib/network.ts";

/**
 * Hoja mínima que enlazan las páginas estáticas de la raíz (public/). Mientras
 * la red no tenga WhatsApp en network.ts, oculta el botón flotante que track.js
 * inyecta por su cuenta; en cuanto el panel vuelve a publicar un número, la
 * hoja sale vacía y el flotante reaparece sin tocar las páginas.
 */
export const GET: APIRoute = () =>
  new Response(contactFor().whatsapp ? "" : "#nb-wa-float,#nb-wa-panel{display:none!important}\n", {
    headers: { "Content-Type": "text/css; charset=utf-8" },
  });
