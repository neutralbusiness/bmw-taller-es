# metaTitle de ciudades revisados el 04-oct-2026 (decisión de Martin sobre la
# propuesta de titles con promesas prohibidas o errores).
#
# - 57 ciudades sin impresiones en GSC: title nuevo de la propuesta, recortado a
#   ≤ 65 caracteres donde se pasaba (normalmente quitando «y MINI»).
# - 4 ciudades con impresiones (madrid, zaragoza, sant-boi-de-llobregat, sentmenat):
#   cambio mínimo, solo se quita lo prohibido y se conserva el resto del title.
#   Sant Boi: el taller está en Sant Joan Despí, de ahí «junto a».
# - Barcelona: «para Barcelona» en vez de «en Barcelona» (el taller está en Sant
#   Joan Despí; la guía prohíbe la presencia física falsa).
#
# Ni aplicar.py ni p10_ensamblar.py escriben metaTitle: viven solo en
# src/content/cities/<slug>.json. Para reaplicarlos (idempotente):
#   python3 scripts/datos_ciudades/tandas/titles_2026-10-04.py
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun import CIUDADES_DIR  # noqa: E402

TITLES = {
    # --- con impresiones: cambio mínimo
    "madrid": "BMW Taller en Madrid para Profesionales",
    "zaragoza": "Taller BMW en Zaragoza | Especialistas en diagnosis",
    "sant-boi-de-llobregat": "Taller BMW junto a Sant Boi de Llobregat — Especialista en CBS",
    "sentmenat": "BMW Sentmenat — Tu taller especialista",
    # --- sin impresiones: propuesta
    "barbera-del-valles": "Taller especialista BMW y MINI cerca de Barberà del Vallès",
    "begues": "Taller BMW cerca de Begues | Especialista BMW, Baix Llobregat",
    "cardona": "Taller BMW cerca de Cardona | Especialista independiente, Bages",
    "castellar-del-valles": "Taller BMW cerca de Castellar del Vallès | Especialista BMW",
    "corbera-de-llobregat": "Taller BMW cerca de Corbera de Llobregat | Especialista BMW",
    "fuente-el-saz-de-jarama": "Taller BMW cerca de Fuente el Saz de Jarama | Especialista BMW",
    "girona": "Taller BMW para Girona | Especialista independiente BMW y MINI",
    "l-hospitalet-de-llobregat": "Taller BMW cerca de L'Hospitalet | Especialista BMW y MINI",
    "mollet-del-valles": "Taller BMW cerca de Mollet del Vallès | Especialista BMW y MINI",
    "montcada-i-reixac": "Taller BMW cerca de Montcada i Reixac | Especialista BMW y MINI",
    "roda-de-ter": "Taller BMW para Roda de Ter (Osona) | Especialista independiente",
    "rubi": "Taller BMW cerca de Rubí | Revisiones y diagnosis BMW y MINI",
    "sabadell": "Taller BMW cerca de Sabadell | Especialista en diésel N47 y B47",
    "sant-climent-de-llobregat": "Taller BMW cerca de Sant Climent de Llobregat | Especialista BMW",
    "sant-cugat-del-valles": "Taller BMW cerca de Sant Cugat del Vallès | Especialista BMW",
    "sant-fost-de-campsentelles": "Taller BMW cerca de Sant Fost de Campsentelles | Especialista BMW",
    "sant-joan-despi": "Taller BMW en Sant Joan Despí | Especialista independiente BMW",
    "sant-sadurni-d-anoia": "Taller BMW cerca de Sant Sadurní d'Anoia | Especialista BMW",
    "sant-vicenc-de-montalt": "Taller BMW cerca de Sant Vicenç de Montalt | Especialista BMW",
    "santa-coloma-de-cervello": "Taller BMW cerca de Santa Coloma de Cervelló | Especialista BMW",
    "villalbilla": "Taller BMW cerca de Villalbilla | Especialista BMW y MINI",
    "villanueva-de-perales": "Taller BMW cerca de Villanueva de Perales | Especialista BMW",
    "villaviciosa-de-odon": "Taller BMW cerca de Villaviciosa de Odón | Especialista BMW",
    "barcelona": "Taller BMW para Barcelona | Especialista independiente BMW y MINI",
    "gironella": "Taller BMW para Gironella (Berguedà) | Especialista independiente",
    "la-roca-del-valles": "Taller BMW cerca de La Roca del Vallès | Especialista BMW y MINI",
    "montgat": "Taller BMW cerca de Montgat | Especialista BMW y MINI, Maresme",
    "odena": "Taller BMW para Òdena (Anoia) | Especialista independiente BMW",
    "sant-pere-de-ribes": "Taller BMW cerca de Sant Pere de Ribes | Especialista BMW y MINI",
    "sant-pol-de-mar": "Taller BMW para Sant Pol de Mar | Especialista BMW, Maresme",
    "vacarisses": "Taller BMW cerca de Vacarisses | Especialista BMW y MINI",
    "vilafranca-del-penedes": "Taller BMW cerca de Vilafranca del Penedès | Especialista BMW",
    "vilassar-de-dalt": "Taller BMW cerca de Vilassar de Dalt | Especialista BMW y MINI",
    "el-vendrell": "Taller BMW para El Vendrell | Especialista BMW, Baix Penedès",
    "valdeavero": "Taller BMW cerca de Valdeavero | Especialista BMW y MINI",
    "calaf": "Taller BMW para Calaf (Anoia) | Especialista independiente BMW",
    "cubelles": "Taller BMW cerca de Cubelles | Especialista BMW y MINI, Garraf",
    "suria": "Taller BMW para Súria (Bages) | Especialista independiente BMW",
    "vilassar-de-mar": "Taller BMW cerca de Vilassar de Mar | Especialista BMW y MINI",
    "pozuelo-del-rey": "Taller BMW para Pozuelo del Rey | Especialista BMW en Alcobendas",
    "ribatejada": "Taller BMW para Ribatejada | Especialista BMW en Alcobendas",
    "l-espunyola": "Taller BMW para l'Espunyola (Berguedà) | Especialista BMW",
    "campins": "Taller BMW para Campins | Montseny y BV-5301, especialista BMW",
    "lluca": "Taller BMW para Lluçà (Lluçanès) | Especialista independiente BMW",
    "calldetenes": "Taller BMW para Calldetenes (Osona) | Especialista BMW y MINI",
    "santa-eulalia-de-riuprimer": "Taller BMW para Santa Eulàlia de Riuprimer (Osona)",
    "calders": "Taller BMW para Calders (Moianès) | Diagnosis y reparación BMW",
    "monistrol-de-calders": "Taller BMW para Monistrol de Calders | Moianès, especialista BMW",
    "ambite": "Taller BMW para Ambite | Especialista BMW, sureste de Madrid",
    "anchuelo": "Taller BMW para Anchuelo | Especialista BMW cerca de Alcalá",
    "argencola": "Taller BMW para Argençola (Anoia) | Especialista independiente",
    "jorba": "Taller BMW para Jorba (Anoia) | Especialista BMW junto a la A-2",
    "olost": "Taller BMW para Olost (Lluçanès) | Especialista independiente BMW",
    "santa-maria-d-olo": "Taller BMW para Santa Maria d'Oló (Moianès) | Especialista BMW",
    "fogars-de-montclus": "Taller BMW para Fogars de Montclús | Montseny, especialista BMW",
    "galapagos": "Taller BMW para Galápagos (Guadalajara) | Especialista BMW y MINI",
    "palleja": "Taller BMW cerca de Pallejà | Especialista BMW, Baix Llobregat",
}

PROHIBIDO = re.compile(
    r"(?-i:\bISTA\b)|Rheingold|oficial|%|presupuesto cerrado|recogida|domicilio|minutos?\b|\bmin\b|"
    r"coraz[oó]n|alta monta|garant[ií]a|rendimiento|profesionales de",
    re.I,
)


def comprobar():
    assert len(TITLES) == 61, len(TITLES)
    vistos = {}
    for slug, t in TITLES.items():
        assert len(t) <= 65, (slug, len(t), t)
        assert not PROHIBIDO.search(t), (slug, t)
        assert t not in vistos, (slug, vistos.get(t))
        vistos[t] = slug


def aplicar():
    comprobar()
    cambiados = 0
    for slug, t in TITLES.items():
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        if cj.get("metaTitle") != t:
            cj["metaTitle"] = t
            f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
            cambiados += 1
            print("metaTitle", slug)
    print(f"{cambiados} cambiados de {len(TITLES)}")


if __name__ == "__main__":
    aplicar()
