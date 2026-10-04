"""Aplica los bloques `local` escritos en lote_*.py a src/content/cities/<slug>.json.

Uso: python3 scripts/datos_ciudades/piloto/aplicar.py lote_01 [tanda_05 ...]  (busca en piloto/ y tandas/)
- añade/reemplaza `local` (version 3 + fecha de revisión);
- actualiza `population` con el padrón del fichero de datos (o la quita si el
  subdominio no es un municipio);
- corrige lat/lng si el pipeline detectó que caían fuera del municipio.
No toca slug, name, metaTitle, tenant ni nada más.
"""
import importlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent))
sys.path.insert(0, str(AQUI.parent / "tandas"))  # tandas de producción: tandas/tanda_NN.py
from comun import CIUDADES_DIR, DATOS  # noqa: E402


def main():
    for lote in sys.argv[1:]:
        m = importlib.import_module(lote)
        for slug, contenido in m.CIUDADES.items():
            f = CIUDADES_DIR / f"{slug}.json"
            cj = json.loads(f.read_text("utf-8"))
            d = json.loads((DATOS / f"{slug}.json").read_text("utf-8"))
            for sec in contenido["secciones"]:
                sec["parrafos"] = [x.strip() for x in sec["parrafos"] if x.strip()]
            cj["local"] = {"version": 3, "revisado": m.REVISADO, **contenido}
            pob = (d.get("poblacion") or {}).get("valor")
            if d.get("tipo") != "municipio":
                cj.pop("population", None)
            elif pob:
                cj["population"] = pob
            if d["coordenadas"].get("comprobadas") is False:
                cj["lat"], cj["lng"] = d["coordenadas"]["lat"], d["coordenadas"]["lng"]
            f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
            print("aplicado", slug)


if __name__ == "__main__":
    main()
