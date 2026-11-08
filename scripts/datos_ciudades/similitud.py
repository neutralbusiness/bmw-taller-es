"""Comprobador de similitud entre páginas de ciudad (shingles de 5 palabras).

Mide, para cada página de ciudad del build (dist/<slug>/index.html), el
MÁXIMO de similitud Jaccard contra todas las demás, tras:
  1. quedarse solo con <main> (sin cabecera ni pie, que siempre son iguales);
  2. quitar <script>, <style>, <svg> y etiquetas;
  3. normalizar (minúsculas, sin tildes) y ENMASCARAR topónimos —nombres de
     las 575 ciudades de la red, provincias, comunidades, comarcas, municipios
     de los talleres— por «X», y toda cifra por «N»;
  4. trocear en shingles de 5 palabras y comparar conjuntos.

Uso (desde la raíz del repo, después de `npm run build`):
  python3 scripts/datos_ciudades/similitud.py                 # todas, <main> completo
  python3 scripts/datos_ciudades/similitud.py --zona editorial # solo bloques data-editorial
  python3 scripts/datos_ciudades/similitud.py --solo a,b,c     # informa solo de esas (contra todas)
  python3 scripts/datos_ciudades/similitud.py --csv salida.csv
Umbral: máximo < 25 % obligatorio; objetivo < 15 %.
Sale con código 1 si alguna página de las informadas supera el umbral (--umbral).
"""
import argparse
import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from comun import CIUDADES_DIR, REPO, SOCIOS, norm  # noqa: E402

N = 5


def topominos() -> list[str]:
    nombres = set()
    for f in CIUDADES_DIR.glob("*.json"):
        d = json.loads(f.read_text("utf-8"))
        for k in ("name", "province", "ccaa"):
            if d.get(k):
                nombres.add(d[k])
        for b in d.get("zoneNeighborhoods") or []:
            nombres.add(b)
    for s in SOCIOS.values():
        if s.get("municipio"):
            nombres.add(s["municipio"])
    reg = RAIZ / "cache" / "paso_regional.json"
    if reg.exists():
        for v in json.loads(reg.read_text()).values():
            if v.get("comarca"):
                nombres.add(v["comarca"])
    extra = ["madrid", "barcelona", "espana", "catalunya", "cataluna", "comunidad de madrid", "baix llobregat",
             "valles", "maresme", "penedes", "bages", "osona", "anoia", "garraf", "henares", "sierra norte"]
    out = {norm(n) for n in nombres} | set(extra)
    # variantes sin artículo ("Las Rozas de Madrid" -> "rozas de madrid")
    for n in list(out):
        for a in ("el ", "la ", "les ", "els ", "l ", "los ", "las "):
            if n.startswith(a):
                out.add(n[len(a):])
    return sorted((n for n in out if len(n) >= 3), key=len, reverse=True)


def texto_main(h: str, zona: str) -> str:
    m = re.search(r"<main\b.*?</main>", h, re.S)
    h = m.group(0) if m else h
    h = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", h, flags=re.S)
    if zona == "editorial":
        partes = re.findall(r"<(\w+)[^>]*\bdata-editorial\b[^>]*>(.*?)</\1>", h, re.S)
        h = " ".join(p[1] for p in partes)
    h = re.sub(r"<[^>]+>", " ", h)
    return html.unescape(h)


def tokens(txt: str, rx) -> list[str]:
    t = " " + norm(txt) + " "
    t = rx.sub(" x ", t)
    t = re.sub(r"\b\d+\b", " n ", t)
    return t.split()


def shingles(toks: list[str]) -> set:
    return {" ".join(toks[i:i + N]) for i in range(len(toks) - N + 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(REPO / "dist"))
    ap.add_argument("--zona", default="main", choices=["main", "editorial"])
    ap.add_argument("--solo", default="")
    ap.add_argument("--csv", default="")
    ap.add_argument("--umbral", type=float, default=25.0)
    a = ap.parse_args()

    tops = topominos()
    rx = re.compile(r"(?<= )(?:" + "|".join(re.escape(t) for t in tops) + r")(?= )")
    slugs = sorted(p.stem for p in CIUDADES_DIR.glob("*.json"))
    sh, palabras = {}, {}
    for s in slugs:
        f = Path(a.dist) / s / "index.html"
        if not f.exists():
            continue
        toks = tokens(texto_main(f.read_text("utf-8"), a.zona), rx)
        palabras[s] = len(toks)
        sh[s] = shingles(toks)
    idx = defaultdict(list)
    for s, st in sh.items():
        for g in st:
            idx[g].append(s)
    solo = [x for x in a.solo.split(",") if x] or list(sh)
    res = []
    for s in solo:
        if s not in sh or not sh[s]:
            res.append((s, 0.0, "", palabras.get(s, 0)))
            continue
        inter = defaultdict(int)
        for g in sh[s]:
            for o in idx[g]:
                if o != s:
                    inter[o] += 1
        best, bo = 0.0, ""
        for o, k in inter.items():
            j = k / (len(sh[s]) + len(sh[o]) - k)
            if j > best:
                best, bo = j, o
        res.append((s, round(best * 100, 1), bo, palabras[s]))
    res.sort(key=lambda r: -r[1])
    vals = sorted(r[1] for r in res)
    if vals:
        med = vals[len(vals) // 2]
        p90 = vals[int(len(vals) * 0.9) - 1] if len(vals) >= 10 else vals[-1]
        print(f"zona={a.zona} páginas={len(res)} media={sum(vals)/len(vals):.1f}% mediana={med}% p90={p90}% "
              f"máx={vals[-1]}% >25%={sum(v > 25 for v in vals)} >15%={sum(v > 15 for v in vals)}")
    for r in res[: (len(res) if a.solo else 15)]:
        print(f"  {r[0]:<40} {r[1]:>5}%  vs {r[2]:<35} ({r[3]} palabras)")
    if a.csv:
        Path(a.csv).write_text("slug,max_similitud,contra,palabras\n" + "\n".join(f"{r[0]},{r[1]},{r[2]},{r[3]}" for r in res), "utf-8")
    sys.exit(1 if any(r[1] >= a.umbral for r in res) else 0)


if __name__ == "__main__":
    main()
