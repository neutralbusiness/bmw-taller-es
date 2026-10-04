"""Valida el bloque `local` (contenido v3) de una o varias ciudades.

Comprueba, por ciudad:
  - estructura: h1, entradilla, 3-6 secciones con id/h2/parrafos, 3-5 FAQ,
    4-10 datos con fuente, fuentes, revisado (AAAA-MM-DD), socio coherente;
  - longitud: 350-750 palabras útiles (secciones + FAQ + entradilla);
  - expresiones prohibidas (opiniones, precios, «hasta un 50 %», tiempos de
    viaje, afirmaciones de presencia física en la ciudad, muletillas de IA);
  - cifras: toda cifra del texto debe estar en datos/<slug>.json o en la lista
    de cifras normativas permitidas; las que no, se listan para revisión;
  - que `population` del JSON coincida con el padrón del fichero de datos.
Uso: python3 scripts/datos_ciudades/validar_local.py slug1 slug2 ...   (o --todas)
Sale con 1 si hay errores (los avisos no cuentan como error).
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from comun import CIUDADES_DIR, DATOS  # noqa: E402

PROHIBIDAS = [
    (r"\b\d+[.,]?\d*\s?(€|euros?)\b", "precio (no hay catálogo de precios en esta red)"),
    (r"50\s?%|cincuenta por ciento|mitad de precio", "promesa de ahorro sin respaldo"),
    (r"\bopini|reseñ|valoraci|estrellas|testimoni|clientes satisfechos|nos recomiendan", "opiniones/valoraciones"),
    (r"\bminutos?\b|\bmin\.?\b|\bmedia hora\b|\buna hora\b", "tiempo de viaje (no se publica)"),
    (r"años de experiencia|(en activo|trabajamos|abiertos|fundad[oa]s?|nacimos) desde (19|20)\d\d|miles de clientes|cientos de clientes", "cifra de negocio sin fuente"),
    (r"taller oficial|concesionario oficial de la red|servicio oficial bmw de la red", "no somos servicio oficial"),
    (r"nuestro taller (de|en) {ciudad}|en nuestro taller de {ciudad}|estamos en {ciudad}|nuestras instalaciones en {ciudad}", "presencia física falsa en la ciudad"),
    (r"a domicilio|vamos a buscar|te lo recogemos|coche de sustitución|vehículo de sustitución", "servicio no acreditado (solo existe recogida en el área metropolitana, sujeta a disponibilidad)"),
    (r"en el corazón de|sin lugar a dudas|no es ningún secreto|en definitiva|cabe destacar|a la vanguardia|amplia experiencia|equipo de profesionales altamente", "muletilla"),
    (r"\bISTA\b|Rheingold", "herramienta no acreditada en la web de Dasercars: no citar"),
]

# Cifras normativas o técnicas que pueden aparecer sin estar en datos/<slug>.json
CIFRAS_LIBRES = {"461", "2010", "920", "2017", "1", "2", "3", "4", "5", "6", "8", "10", "12", "24", "100", "1000"}


def palabras(t: str) -> int:
    return len(re.findall(r"\w+", t))


def cifras_datos(d) -> set:
    out = set()

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, (int, float)) and not isinstance(o, bool):
            out.add(str(o))
            out.add(str(round(o)))
            if isinstance(o, float):
                out.add(f"{o:.1f}".replace(".", ","))
                out.add(str(o).replace(".", ","))
        elif isinstance(o, str):
            for m in re.findall(r"\d+(?:[.,]\d+)?", o):
                out.add(m)
                out.add(m.replace(".", ""))
    walk(d)
    return out


def validar(slug: str):
    errs, avisos = [], []
    cj = json.loads((CIUDADES_DIR / f"{slug}.json").read_text("utf-8"))
    df = DATOS / f"{slug}.json"
    datos = json.loads(df.read_text("utf-8")) if df.exists() else {}
    L = cj.get("local")
    if not L:
        return [f"{slug}: sin bloque local"], []
    for k in ("h1", "entradilla", "secciones", "faq", "datos", "fuentes", "revisado"):
        if not L.get(k):
            errs.append(f"falta {k}")
    if L.get("version") != 3:
        errs.append("version debe ser 3")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", L.get("revisado", "")):
        errs.append("revisado no es AAAA-MM-DD")
    sec = L.get("secciones") or []
    if not 3 <= len(sec) <= 6:
        errs.append(f"{len(sec)} secciones (3-6)")
    ids = [s.get("id") for s in sec]
    if len(set(ids)) != len(ids) or any(not re.match(r"^[a-z0-9-]+$", i or "") for i in ids):
        errs.append("ids de sección repetidos o inválidos")
    if not 3 <= len(L.get("faq") or []) <= 5:
        errs.append("FAQ: 3-5 preguntas")
    for d in L.get("datos") or []:
        if not d.get("fuente"):
            errs.append(f"dato sin fuente: {d.get('etiqueta')}")
    soc_d = (datos.get("taller_que_atiende") or {}).get("id")
    soc_l = (L.get("socio") or {}).get("id")
    if soc_d and soc_l != soc_d:
        errs.append(f"socio {soc_l} ≠ datos {soc_d}")
    if not soc_d and soc_l:
        errs.append("socio declarado pero la ciudad no tiene taller de la red en su zona")
    texto = " ".join([L.get("h1", ""), L.get("entradilla", "")]
                     + [s.get("h2", "") + " " + " ".join(s.get("parrafos", [])) + " " + " ".join(s.get("lista") or []) for s in sec]
                     + [f["q"] + " " + f["a"] for f in L.get("faq") or []])
    n = palabras(texto)
    if n < 350 or n > 750:
        errs.append(f"{n} palabras (350-750)")
    ciudad = re.escape(cj["name"].lower())
    for pat, motivo in PROHIBIDAS:
        m = re.search(pat.replace("{ciudad}", ciudad), texto, re.I)
        if m:
            errs.append(f"prohibido ({motivo}): «{m.group(0)}»")
    # La recogida/entrega y el vehículo de cortesía existen (FAQ de la raíz) pero
    # solo en el área metropolitana de Madrid y de Barcelona y sujetos a disponibilidad.
    if re.search(r"recogida|cortesía", texto, re.I) and not re.search(r"disponibilidad|solo cubre|cubre solo|no cubre|no llega|queda fuera", texto, re.I):
        errs.append("recogida/cortesía sin la condición «sujeto a disponibilidad» o sin acotar al área metropolitana")
    # cifras trazables
    dat = cifras_datos(datos) | cifras_datos(L.get("datos"))
    sueltas = []
    for m in re.findall(r"(?<![\w-])\d[\d.]*(?:,\d+)?(?![\w-])", texto):
        v = m.rstrip(".")
        if v in CIFRAS_LIBRES or v.replace(".", "") in dat or v in dat:
            continue
        sueltas.append(v)
    if sueltas:
        avisos.append("cifras no encontradas en los datos (revisar a mano): " + ", ".join(sorted(set(sueltas))))
    pob = (datos.get("poblacion") or {}).get("valor")
    if pob and cj.get("population") != pob:
        errs.append(f"population {cj.get('population')} ≠ padrón {pob}")
    if datos.get("tipo") and datos["tipo"] != "municipio" and cj.get("population"):
        errs.append("no es municipio: quitar population")
    return [f"{slug}: {e}" for e in errs], [f"{slug}: {a}" for a in avisos] + [f"{slug}: {n} palabras"]


def main():
    args = sys.argv[1:]
    if args == ["--todas"]:
        args = [p.stem for p in CIUDADES_DIR.glob("*.json") if json.loads(p.read_text("utf-8")).get("local")]
    todos = []
    for s in args:
        e, a = validar(s)
        todos += e
        for x in a:
            print("  aviso", x)
        for x in e:
            print("  ERROR", x)
    print(f"{len(args)} ciudades, {len(todos)} errores")
    sys.exit(1 if todos else 0)


if __name__ == "__main__":
    main()
