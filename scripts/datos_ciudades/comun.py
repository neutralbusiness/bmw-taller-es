"""Utilidades compartidas del pipeline de datos de ciudades (solo stdlib).

Todo lo que se descarga se guarda en cache/ (ignorado por git) para que volver
a ejecutar un paso no repita peticiones. Los resultados por paso van a
cache/paso_*.json y el ensamblado final a datos/<slug>.json (sí versionado).
"""
from __future__ import annotations

import json
import math
import os
import time
import urllib.parse
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
REPO = RAIZ.parent.parent
CIUDADES_DIR = REPO / "src" / "content" / "cities"
CACHE = RAIZ / "cache"
DATOS = RAIZ / "datos"
CACHE.mkdir(exist_ok=True)
DATOS.mkdir(exist_ok=True)

UA = "bmw-taller.es datos-ciudades/1.0 (info@bmw-taller.es)"

# ──────────────────────────────────────────────────────────────────────────
# Talleres reales que atienden cada zona. Fuente: páginas /talleres/,
# /taller-bmw-madrid/ y /taller-bmw-barcelona/ de www.bmw-taller.es (JSON-LD
# con dirección, CP y coordenadas) y la asignación de teléfonos por zona del
# panel (network_sites.custom_phone). Coordenadas: portal geocodificado con
# CartoCiudad (IGN) el 04-oct-2026 (las del JSON-LD estaban redondeadas a 3-4
# decimales: Alcobendas caía 1,2 km al NE, en el centro). Si una zona no tiene dirección real,
# `direccion` es None y NO se calcula distancia ni se declara LocalBusiness.
# ──────────────────────────────────────────────────────────────────────────
SOCIOS = {
    "dasercars-sant-joan-despi": {
        "nombre": "Dasercars Barcelona",
        "direccion": "Carrer del Tambor del Bruc, 3, Local",
        "cp": "08970",
        "municipio": "Sant Joan Despí",
        "provincia": "Barcelona",
        "lat": 41.36594,
        "lng": 2.06355,
        "telefono": "+34622552992",
        "horario": "Lunes a viernes: 9:00–14:00 y 15:00–18:00. Sábados y domingos: cerrado.",
        "horario_schema": [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "09:00", "14:00", "15:00", "18:00"],
        "fuente": "https://www.bmw-taller.es/taller-bmw-barcelona/",
    },
    "dasercars-alcobendas": {
        "nombre": "Dasercars Madrid",
        "direccion": "Calle Valgrande, 17, Local",
        "cp": "28108",
        "municipio": "Alcobendas",
        "provincia": "Madrid",
        "lat": 40.53717,
        "lng": -3.65107,
        "telefono": "+34665245143",
        "horario": "Lunes a viernes: 9:00–14:00 y 15:00–18:00. Sábados y domingos: cerrado.",
        "horario_schema": [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "09:00", "14:00", "15:00", "18:00"],
        "fuente": "https://www.bmw-taller.es/taller-bmw-madrid/",
    },
    "socio-zaragoza": {
        "nombre": "Taller asociado en Zaragoza",
        "direccion": None,  # sin dirección publicada: no se inventa
        "telefono": "+34647503521",
        "fuente": "panel: network_sites.custom_phone",
    },
}

# Códigos INE mal asignados en network_cities (comprobado contra el nombre
# oficial de la tabla 29005 del INE el 04-oct-2026; Arroyomolinos, al comprobar
# que el prefijo provincial del código coincide con la provincia).
INE_CORRECCIONES = {
    "la-llagosta": "08105",
    "arroyomolinos": "28015",  # el panel tenía 10023 = Arroyomolinos (Cáceres): población 816 y coordenadas en Extremadura
}

# Subdominios que NO son municipios: su población, superficie, etc. NO son las
# del municipio al que pertenecen. El texto debe decir «barrio de X».
NO_MUNICIPIO = {
    "chamartin": ("distrito", "Madrid"),
    "ciudad-lineal": ("distrito", "Madrid"),
    "el-goloso": ("barrio", "Madrid"),  # barrio del distrito de Fuencarral-El Pardo
    "las-matas": ("barrio", "Las Rozas de Madrid"),
    "llefia": ("barrio", "Badalona"),
    "vilaseca": ("núcleo de población", "Orís (Osona)"),  # revisar: el JSON tenía la población de Vila-seca (Tarragona)
}

PROV_CATALUNYA = {"Barcelona", "Tarragona", "Girona", "Lleida"}
PROV_CENTRO = {"Madrid", "Guadalajara", "Toledo", "Segovia"}


def socio_para(ciudad: dict) -> str | None:
    """Qué taller real atiende la ciudad, según su teléfono y provincia."""
    tel = ((ciudad.get("tenant") or {}).get("phone")) or ""
    prov = ciudad.get("province")
    if tel.endswith("647503521"):
        return "socio-zaragoza"
    if tel.endswith("665245143") or prov in PROV_CENTRO:
        return "dasercars-alcobendas"
    if prov in PROV_CATALUNYA:
        return "dasercars-sant-joan-despi"
    return None  # capitales fuera de zona: sin taller propio cerca


def haversine_km(lat1, lng1, lat2, lng2) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lng2 - lng1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def _curl(args: list[str], timeout: int) -> bytes:
    # Se usa curl y no urllib: el Python de python.org en macOS no trae los
    # certificados raíz instalados y urllib falla con CERTIFICATE_VERIFY_FAILED.
    import subprocess
    r = subprocess.run(["curl", "-sSL", "--fail", "-m", str(timeout), "-A", UA, *args],
                       capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode(errors="ignore")[:300])
    return r.stdout


def http_get(url: str, cache_name: str | None = None, timeout=60, retries=3, pause=0.0, headers=None) -> bytes:
    if cache_name:
        f = CACHE / cache_name
        if f.exists() and f.stat().st_size > 0:
            return f.read_bytes()
    last = None
    for i in range(retries):
        try:
            args = []
            for k, v in (headers or {}).items():
                args += ["-H", f"{k}: {v}"]
            data = _curl(args + [url], timeout)
            if cache_name:
                (CACHE / cache_name).write_bytes(data)
            if pause:
                time.sleep(pause)
            return data
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"GET {url} falló: {last}")


def http_post(url: str, body: bytes, headers: dict, timeout=120) -> bytes:
    args = ["-X", "POST", "--data-binary", "@-"]
    for k, v in headers.items():
        args += ["-H", f"{k}: {v}"]
    import subprocess
    r = subprocess.run(["curl", "-sSL", "--fail", "-m", str(timeout), "-A", UA, *args, url],
                       input=body, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode(errors="ignore")[:300])
    return r.stdout


def cargar(nombre: str, defecto=None):
    f = CACHE / nombre
    if not f.exists():
        return defecto
    return json.loads(f.read_text("utf-8"))


def guardar(nombre: str, obj) -> None:
    (CACHE / nombre).write_text(json.dumps(obj, ensure_ascii=False, indent=1), "utf-8")


def ciudades_repo() -> list[dict]:
    out = []
    for f in sorted(CIUDADES_DIR.glob("*.json")):
        out.append(json.loads(f.read_text("utf-8")))
    return out


def norm(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFD", s or "").encode("ascii", "ignore").decode().lower()
    return " ".join("".join(c if c.isalnum() else " " for c in s).split())


def q(s: str) -> str:
    return urllib.parse.quote(s)
