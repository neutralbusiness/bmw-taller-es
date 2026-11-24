/**
 * Talleres reales que atienden las ciudades de la red.
 *
 * Fuente: páginas /taller-bmw-madrid/ y /taller-bmw-barcelona/ de la raíz
 * (dirección, CP, coordenadas y horario de cada delegación) y la
 * asignación de teléfonos por zona del panel. Debe coincidir con
 * scripts/datos_ciudades/comun.py → SOCIOS.
 *
 * Regla: si un socio no tiene dirección publicada, NO se muestra dirección,
 * NO se calcula distancia y NO se declara AutoRepair en el JSON-LD.
 */
export interface Socio {
  id: string;
  nombre: string;
  direccion?: string;
  cp?: string;
  municipio?: string;
  provincia?: string;
  lat?: number;
  lng?: number;
  horario?: string;
  urlFicha?: string;
}

export const SOCIOS: Record<string, Socio> = {
  "dasercars-sant-joan-despi": {
    id: "dasercars-sant-joan-despi",
    nombre: "BMW Taller Sant Joan Despí",
    direccion: "Carrer del Tambor del Bruc, 3, Local",
    cp: "08970",
    municipio: "Sant Joan Despí",
    provincia: "Barcelona",
    lat: 41.36594,
    lng: 2.06355,
    horario: "Lunes a viernes, 9:00–14:00 y 15:00–18:00. Sábados y domingos, cerrado.",
    urlFicha: "https://www.bmw-taller.es/taller-bmw-barcelona/",
  },
  "dasercars-alcobendas": {
    id: "dasercars-alcobendas",
    nombre: "BMW Taller Alcobendas",
    direccion: "Calle Valgrande, 17, Local",
    cp: "28108",
    municipio: "Alcobendas",
    provincia: "Madrid",
    lat: 40.53717,
    lng: -3.65107,
    horario: "Lunes a viernes, 9:00–14:00 y 15:00–18:00. Sábados y domingos, cerrado.",
    urlFicha: "https://www.bmw-taller.es/taller-bmw-madrid/",
  },
  "socio-zaragoza": {
    id: "socio-zaragoza",
    nombre: "BMW Taller Cuarte de Huerva",
    direccion: "Carretera de Valencia, km 6,2, Nave 8",
    cp: "50410",
    municipio: "Cuarte de Huerva",
    provincia: "Zaragoza",
    lat: 41.60672,
    lng: -0.93076,
    horario: "Lunes a viernes, 9:00–13:30 y 15:00–19:00. Sábados, 9:00–13:00. Domingos, cerrado.",
    urlFicha: "https://www.bmw-taller.es/taller-bmw-zaragoza/",
  },
  // Delegaciones añadidas el 24-nov-2026 (nombre de zona, nunca el comercial).
  "poligono-francoli": {
    id: "poligono-francoli",
    nombre: "BMW Taller Polígono Francolí",
    direccion: "Pol. Ind. Francolí, Parcela 9, Nau 9",
    cp: "43006",
    municipio: "Tarragona",
    provincia: "Tarragona",
    lat: 41.1235,
    lng: 1.2318,
    horario: "Lunes a jueves, 9:00–13:00 y 15:00–19:00. Viernes, 7:00–13:00. Sábados y domingos, cerrado.",
    urlFicha: "https://www.bmw-taller.es/taller-bmw-tarragona/",
  },
};

export const HORARIO_SCHEMA_FRANCOLI = [
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday"], opens: "09:00", closes: "13:00" },
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday"], opens: "15:00", closes: "19:00" },
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Friday"], opens: "07:00", closes: "13:00" },
];

export const HORARIO_SCHEMA_ASF = [
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], opens: "09:00", closes: "13:30" },
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], opens: "15:00", closes: "19:00" },
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Saturday"], opens: "09:00", closes: "13:00" },
];

/** Horario en formato schema.org de los talleres con horario publicado. */
export const HORARIO_SCHEMA_DASERCARS = [
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], opens: "09:00", closes: "14:00" },
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], opens: "15:00", closes: "18:00" },
];
