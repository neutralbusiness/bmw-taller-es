"""Paso 2 — población oficial (INE, Cifras oficiales de población de los
municipios españoles: Revisión del Padrón Municipal, tabla 29005).

Guarda la cifra del último año publicado y la de diez años antes para poder
decir, con dato, si el municipio crece o pierde población.
Salida: cache/paso_ine.json  {slug: {poblacion, anio, poblacion_10, anio_10, fuente}}
"""
import csv
import io

from comun import cargar, guardar, http_get

URL = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/29005.csv"
FUENTE = "INE, Revisión del Padrón Municipal (tabla 29005): https://www.ine.es/jaxiT3/Tabla.htm?t=29005"


def main():
    base = cargar("paso_base.json")
    raw = http_get(URL, "ine_29005.csv", timeout=180).decode("utf-8-sig")
    serie: dict[str, dict[int, int]] = {}
    for row in csv.DictReader(io.StringIO(raw), delimiter=";"):
        if row.get("Sexo") != "Total":
            continue
        cod = (row["Municipios"] or "")[:5]
        if not cod.isdigit():
            continue
        try:
            v = int(row["Total"].replace(".", ""))
        except ValueError:
            continue
        serie.setdefault(cod, {})[int(row["Periodo"])] = v
    out, faltan = {}, []
    for s, c in base.items():
        sr = serie.get(str(c["ine"]).zfill(5))
        if not sr:
            faltan.append(s)
            continue
        a = max(sr)
        a10 = a - 10 if (a - 10) in sr else None
        out[s] = {
            "poblacion": sr[a], "anio": a,
            "poblacion_10": sr.get(a10) if a10 else None, "anio_10": a10,
            "fuente": FUENTE,
        }
        if c.get("tipo") != "municipio":
            # la cifra es la del municipio al que pertenece, no la del barrio
            out[s]["poblacion_es_de"] = c.get("pertenece_a")
    guardar("paso_ine.json", out)
    print(f"población: {len(out)}/{len(base)}; sin dato: {faltan}")


if __name__ == "__main__":
    main()
