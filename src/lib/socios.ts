/**
 * Talleres reales que atienden las ciudades de la red.
 *
 * Fuente: páginas /taller-bmw-madrid/ y /taller-bmw-barcelona/ de la raíz
 * (dirección, CP, coordenadas y horario publicados por Dasercars) y la
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
    nombre: "Dasercars Barcelona",
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
    nombre: "Dasercars Madrid",
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
    nombre: "Taller asociado de la red en Zaragoza",
  },
};

/** Horario en formato schema.org de los talleres con horario publicado. */
export const HORARIO_SCHEMA_DASERCARS = [
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], opens: "09:00", closes: "14:00" },
  { "@type": "OpeningHoursSpecification", dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], opens: "15:00", closes: "18:00" },
];
