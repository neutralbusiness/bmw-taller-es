# metaTitle y metaDescription de ciudades ESCRITAS CON IMPRESIONES en GSC
# (cache/paso_gsc.json, 90 días, solo la página de ciudad «/» del subdominio).
#
# Criterio aprobado por Martin (04-oct-2026): quitar SOLO lo prohibido por la
# guía y conservar el resto de palabras tal cual. Se ha quitado:
#   - ISTA / Rheingold, y «original»/«software oficial» pegado a diagnosis
#     (es la misma promesa de herramienta no acreditada);
#   - «oficial» en cualquier sitio («Diagnosis oficial», «mecánica oficial»,
#     «Mantenimiento oficial», «garantía oficial»);
#   - promesas de ahorro: «hasta un 50 %», «hasta -50%», «ahorro garantizado»,
#     «y ahorra», «sin coste de concesionario»;
#   - recogida («con recogida en urbanizaciones», «recogida coordinada»…: sin
#     «sujeto a disponibilidad» y a menudo fuera del área metropolitana);
#   - «BMW M», «Especialistas M», S55/S58 (motores M) y «alto rendimiento»:
#     especialidad no acreditada (la de la raíz es diésel N47/N57/B47/B57…);
#   - un superlativo sin dato («El taller de referencia», Collado Villalba).
# Solo se reescribió la frase que quedaba vacía o rota («Diagnóstico.» →
# «Diagnóstico de averías.»; Sant Andreu de la Barca entera).
# Se han dejado como estaban (no están en la lista de Martin; revisar con él):
# «presupuesto cerrado», «Presupuesto gratis» (El Escorial), «garantía por
# escrito / real / en cada reparación», «Profesionales» (Madrid, ya decidido).
#
# Cada entrada es (antes, después). Para reaplicar (idempotente; avisa si el
# valor actual no es ni el «antes» ni el «después»):
#   python3 scripts/datos_ciudades/tandas/titles_2026-10-05.py
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun import CIUDADES_DIR  # noqa: E402

CAMBIOS = {
    'abrera': {
        'metaDescription': (
            "Taller BMW en Abrera: mantenimiento, revisiones CBS y reparación con diagnóstico ISTA oficial. Recambios OE. Sin perder la garantía del fabricante.",
            "Taller BMW en Abrera: mantenimiento, revisiones CBS y reparación con diagnóstico. Recambios OE. Sin perder la garantía del fabricante.",
        ),
    },
    'algete': {
        'metaTitle': (
            "Taller BMW en Algete — Especialistas con diagnóstico ISTA Oficial",
            "Taller BMW en Algete — Especialistas con diagnóstico",
        ),
        'metaDescription': (
            "Taller especialista en BMW en Algete. Realiza tu revisión CBS o reparación sin perder la garantía oficial. Diagnóstico ISTA y hasta un 50 % de ahorro.",
            "Taller especialista en BMW en Algete. Realiza tu revisión CBS o reparación sin perder la garantía. Diagnóstico de averías.",
        ),
    },
    'alovera': {
        'metaDescription': (
            "Taller BMW especializado en Alovera, junto a Guadalajara. Diagnóstico ISTA, presupuesto cerrado y técnicos formados en la marca. Pide cita.",
            "Taller BMW especializado en Alovera, junto a Guadalajara. Diagnóstico, presupuesto cerrado y técnicos formados en la marca. Pide cita.",
        ),
    },
    'alpedrete': {
        'metaDescription': (
            "Taller BMW especializado cerca de Alpedrete, en la Sierra de Guadarrama. Diagnóstico ISTA, presupuesto cerrado y técnicos formados en la marca.",
            "Taller BMW especializado cerca de Alpedrete, en la Sierra de Guadarrama. Diagnóstico, presupuesto cerrado y técnicos formados en la marca.",
        ),
    },
    'arenys-de-mar': {
        'metaDescription': (
            "Especialistas BMW en Arenys de Mar. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Arenys de Mar. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'arganda-del-rey': {
        'metaDescription': (
            "Taller BMW especializado en Arganda del Rey. Diagnóstico ISTA, presupuesto cerrado y técnicos formados en la marca. Servimos toda la comarca.",
            "Taller BMW especializado en Arganda del Rey. Diagnóstico, presupuesto cerrado y técnicos formados en la marca. Servimos toda la comarca.",
        ),
    },
    'azuqueca-de-henares': {
        'metaDescription': (
            "Taller especializado BMW en Azuqueca de Henares. Diagnosis oficial, mantenimiento y reparación con recogida en polígonos y barrios. Presupuesto cerrado.",
            "Taller especializado BMW en Azuqueca de Henares. Diagnosis, mantenimiento y reparación. Presupuesto cerrado.",
        ),
    },
    'badalona': {
        'metaDescription': (
            "Especialistas BMW en Badalona. Mantén la garantía oficial de tu coche con nuestras revisiones CBS y reparaciones. Diagnóstico ISTA y hasta 50% de ahorro. Pide tu presupuesto.",
            "Especialistas BMW en Badalona. Mantén la garantía de tu coche con nuestras revisiones CBS y reparaciones. Diagnóstico de averías. Pide tu presupuesto.",
        ),
    },
    'badia-del-valles': {
        'metaDescription': (
            "Taller BMW en Badia del Vallès: mantenimiento, revisiones CBS y reparación con diagnóstico ISTA oficial. Recambios OE. Sin perder la garantía del fabricante.",
            "Taller BMW en Badia del Vallès: mantenimiento, revisiones CBS y reparación con diagnóstico. Recambios OE. Sin perder la garantía del fabricante.",
        ),
    },
    'berga': {
        'metaTitle': (
            "BMW Berga — Tu taller especialista con precios de hasta -50%",
            "BMW Berga — Tu taller especialista",
        ),
        'metaDescription': (
            "Tu taller BMW de confianza en Berga. Revisiones CBS, reparación especializada y diagnóstico ISTA. Garantía intacta y presupuestos cerrados.",
            "Tu taller BMW de confianza en Berga. Revisiones CBS, reparación especializada y diagnóstico. Garantía intacta y presupuestos cerrados.",
        ),
    },
    'boadilla-del-monte': {
        'metaDescription': (
            "Taller especializado BMW en Boadilla del Monte. Diagnosis oficial, mantenimiento y reparación con recogida en urbanizaciones. Presupuesto cerrado.",
            "Taller especializado BMW en Boadilla del Monte. Diagnosis, mantenimiento y reparación. Presupuesto cerrado.",
        ),
    },
    'calafell': {
        'metaDescription': (
            "Taller especializado BMW en Calafell. Diagnosis oficial, mantenimiento y reparación de motor y caja. Recogida en Calafell platja, poble y Segur.",
            "Taller especializado BMW en Calafell. Diagnosis, mantenimiento y reparación de motor y caja.",
        ),
    },
    'calella': {
        'metaTitle': (
            "Taller especializado BMW en Calella — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Calella — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Calella? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Calella? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'canet-de-mar': {
        'metaDescription': (
            "Especialistas BMW en Canet de Mar. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Canet de Mar. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'canovelles': {
        'metaTitle': (
            "BMW Canovelles — Tu taller especialista con precios de hasta -50%",
            "BMW Canovelles — Tu taller especialista",
        ),
        'metaDescription': (
            "Tu taller BMW de confianza en Canovelles. Revisiones CBS, reparación especializada y diagnóstico ISTA. Garantía intacta y presupuestos cerrados.",
            "Tu taller BMW de confianza en Canovelles. Revisiones CBS, reparación especializada y diagnóstico. Garantía intacta y presupuestos cerrados.",
        ),
    },
    'cardedeu': {
        'metaDescription': (
            "Especialistas BMW en Cardedeu. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Cardedeu. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'castellbisbal': {
        'metaTitle': (
            "Taller Especialista BMW en Castellbisbal | Revisión Compra ISTA",
            "Taller Especialista BMW en Castellbisbal | Revisión Compra",
        ),
        'metaDescription': (
            "Acabas de comprar un BMW de segunda mano en Castellbisbal y quieres saber su estado real? Taller especialista con diagnóstico ISTA. Pide presupuesto y ahorra.",
            "Acabas de comprar un BMW de segunda mano en Castellbisbal y quieres saber su estado real? Taller especialista con diagnóstico. Pide presupuesto.",
        ),
    },
    'castelldefels': {
        'metaTitle': (
            "Taller Especialista BMW en Castelldefels | Diagnóstico ISTA",
            "Taller Especialista BMW en Castelldefels | Diagnóstico",
        ),
        'metaDescription': (
            "Especialistas en BMW en Castelldefels. Realizamos revisiones de compra, diagnóstico con ISTA y mecánica avanzada. Presupuesto cerrado y ahorro garantizado.",
            "Especialistas en BMW en Castelldefels. Realizamos revisiones de compra, diagnóstico y mecánica avanzada. Presupuesto cerrado.",
        ),
    },
    'cerdanyola-del-valles': {
        'metaTitle': (
            "Taller especializado BMW en Cerdanyola del Vallès — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Cerdanyola del Vallès — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Cerdanyola del Vallès? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Cerdanyola del Vallès? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'collado-villalba': {
        'metaDescription': (
            "Taller BMW en Collado Villalba: diagnóstico oficial, mantenimiento y reparación completa. El taller de referencia para toda la sierra noroeste de Madrid.",
            "Taller BMW en Collado Villalba: diagnóstico, mantenimiento y reparación completa para toda la sierra noroeste de Madrid.",
        ),
    },
    'colmenar-viejo': {
        'metaTitle': (
            "Taller BMW M en Colmenar Viejo — Especialistas en Rendimiento",
            "Taller BMW en Colmenar Viejo — Especialistas",
        ),
        'metaDescription': (
            "Taller especialista en BMW y BMW M en Colmenar Viejo. Diagnóstico ISTA, mantenimiento ZF 8HP y mecánica de alto rendimiento. Ahorra hasta un 50 %.",
            "Taller especialista en BMW en Colmenar Viejo. Diagnóstico, mantenimiento ZF 8HP y mecánica.",
        ),
    },
    'cornella-de-llobregat': {
        'metaTitle': (
            "Taller BMW M en Cornellà — Especialistas en S55, S58 y ZF 8HP",
            "Taller BMW en Cornellà — Especialistas en ZF 8HP",
        ),
        'metaDescription': (
            "Taller especialista BMW en Cornellà de Llobregat. Mantenimiento para motores B58, S55, S58 y eléctricos i/iX. Diagnóstico ISTA y hasta 50% de ahorro. Pide tu presupuesto.",
            "Taller especialista BMW en Cornellà de Llobregat. Mantenimiento para motores B58 y eléctricos i/iX. Diagnóstico de averías. Pide tu presupuesto.",
        ),
    },
    'el-escorial': {
        'metaTitle': (
            "Taller BMW en El Escorial | Diagnosis oficial y garantía",
            "Taller BMW en El Escorial | Diagnosis y garantía",
        ),
        'metaDescription': (
            "Taller BMW en El Escorial, junto a San Lorenzo de El Escorial. Mantenimiento, turbo, Valvetronic, caja ZF y diagnosis con software original. Presupuesto gratis.",
            "Taller BMW en El Escorial, junto a San Lorenzo de El Escorial. Mantenimiento, turbo, Valvetronic, caja ZF y diagnosis. Presupuesto gratis.",
        ),
    },
    'el-prat-de-llobregat': {
        'metaDescription': (
            "Taller especialista en BMW en El Prat de Llobregat. Mantenimiento preventivo para motores con alto kilometraje (cadena, Vanos, juntas). Diagnóstico ISTA. Ahorra hasta un 50 %.",
            "Taller especialista en BMW en El Prat de Llobregat. Mantenimiento preventivo para motores con alto kilometraje (cadena, Vanos, juntas). Diagnóstico de averías.",
        ),
    },
    'esparreguera': {
        'metaDescription': (
            "Especialistas BMW en Esparreguera. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Esparreguera. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'galapagar': {
        'metaTitle': (
            "Taller BMW en Galapagar | Diagnosis oficial y garantía",
            "Taller BMW en Galapagar | Diagnosis y garantía",
        ),
        'metaDescription': (
            "Taller BMW especializado en Galapagar, Sierra de Guadarrama. Mantenimiento, turbo, Valvetronic, caja ZF y diagnosis original. Presupuesto sin compromiso.",
            "Taller BMW especializado en Galapagar, Sierra de Guadarrama. Mantenimiento, turbo, Valvetronic, caja ZF y diagnosis. Presupuesto sin compromiso.",
        ),
    },
    'gargantilla-del-lozoya-y-pinilla-de-buitrago': {
        'metaDescription': (
            "Servicio BMW para Gargantilla del Lozoya y Pinilla de Buitrago, Sierra Norte de Madrid. Diagnosis oficial y caja automática, con recogida coordinada.",
            "Servicio BMW para Gargantilla del Lozoya y Pinilla de Buitrago, Sierra Norte de Madrid. Diagnosis y caja automática.",
        ),
    },
    'gava': {
        'metaDescription': (
            "Tu BMW con más de 150.000km necesita un taller especialista en Gavà. Mantenimiento de cadena, Vanos y turbo con diagnóstico ISTA. Ahorra hasta un 50 %.",
            "Tu BMW con más de 150.000km necesita un taller especialista en Gavà. Mantenimiento de cadena, Vanos y turbo con diagnóstico.",
        ),
    },
    'guadalajara': {
        'metaDescription': (
            "Taller BMW en Guadalajara especializado en diagnosis original, motor, turbo, Valvetronic y caja ZF 8HP. Presupuesto cerrado y garantía por escrito en cada reparación.",
            "Taller BMW en Guadalajara especializado en diagnosis, motor, turbo, Valvetronic y caja ZF 8HP. Presupuesto cerrado y garantía por escrito en cada reparación.",
        ),
    },
    'guadarrama': {
        'metaDescription': (
            "Taller BMW especializado en Guadarrama. Diagnosis original, mantenimiento, turbo, Valvetronic y caja ZF 8HP. Presupuesto cerrado antes de reparar.",
            "Taller BMW especializado en Guadarrama. Diagnosis, mantenimiento, turbo, Valvetronic y caja ZF 8HP. Presupuesto cerrado antes de reparar.",
        ),
    },
    'humanes-de-madrid': {
        'metaDescription': (
            "Taller BMW especializado cerca de Humanes de Madrid. Diagnosis original, mantenimiento, turbo, Valvetronic y caja ZF 8HP. Presupuesto cerrado antes de reparar.",
            "Taller BMW especializado cerca de Humanes de Madrid. Diagnosis, mantenimiento, turbo, Valvetronic y caja ZF 8HP. Presupuesto cerrado antes de reparar.",
        ),
    },
    'la-garriga': {
        'metaTitle': (
            "BMW la Garriga — Tu taller especialista con precios de hasta -50%",
            "BMW la Garriga — Tu taller especialista",
        ),
        'metaDescription': (
            "Tu taller BMW de confianza en la Garriga. Revisiones CBS, reparación especializada y diagnóstico ISTA. Garantía intacta y presupuestos cerrados.",
            "Tu taller BMW de confianza en la Garriga. Revisiones CBS, reparación especializada y diagnóstico. Garantía intacta y presupuestos cerrados.",
        ),
    },
    'llica-d-amunt': {
        'metaTitle': (
            "Taller especializado BMW en Lliçà d'Amunt — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Lliçà d'Amunt — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Lliçà d'Amunt? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Lliçà d'Amunt? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'lozoyuela-navas-sieteiglesias': {
        'metaDescription': (
            "Servicio especializado en BMW para Lozoyuela-Navas-Sieteiglesias, Sierra Norte de Madrid. Diagnóstico oficial y presupuesto claro.",
            "Servicio especializado en BMW para Lozoyuela-Navas-Sieteiglesias, Sierra Norte de Madrid. Diagnóstico y presupuesto claro.",
        ),
    },
    'majadahonda': {
        'metaDescription': (
            "Taller BMW en Majadahonda. Diagnóstico oficial ISTA, mantenimiento, turbo, caja ZF y Vanos. Presupuesto cerrado antes de reparar tu BMW.",
            "Taller BMW en Majadahonda. Diagnóstico, mantenimiento, turbo, caja ZF y Vanos. Presupuesto cerrado antes de reparar tu BMW.",
        ),
    },
    'malgrat-de-mar': {
        'metaDescription': (
            "Especialistas BMW en Malgrat de Mar. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Malgrat de Mar. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'manlleu': {
        'metaTitle': (
            "Taller especializado BMW en Manlleu — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Manlleu — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Manlleu? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Manlleu? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'mataro': {
        'metaTitle': (
            "Taller especializado BMW en Mataró — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Mataró — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Mataró? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Mataró? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'meco': {
        'metaDescription': (
            "Taller especializado en BMW en Meco, Comunidad de Madrid. Diagnosis oficial, mecánica y electrónica con presupuesto claro y garantía en cada reparación.",
            "Taller especializado en BMW en Meco, Comunidad de Madrid. Diagnosis, mecánica y electrónica con presupuesto claro y garantía en cada reparación.",
        ),
    },
    'moralzarzal': {
        'metaDescription': (
            "Taller BMW en Moralzarzal, sierra de Madrid. Diagnosis oficial, mecánica y mantenimiento adaptado a la conducción de montaña, con garantía real.",
            "Taller BMW en Moralzarzal, sierra de Madrid. Diagnosis, mecánica y mantenimiento adaptado a la conducción de montaña, con garantía real.",
        ),
    },
    'navalcarnero': {
        'metaDescription': (
            "Taller especializado en BMW en Navalcarnero. Diagnóstico ISTA, motor, turbo, caja ZF y electrónica. Presupuesto cerrado y garantía por escrito.",
            "Taller especializado en BMW en Navalcarnero. Diagnóstico, motor, turbo, caja ZF y electrónica. Presupuesto cerrado y garantía por escrito.",
        ),
    },
    'olesa-de-montserrat': {
        'metaTitle': (
            "Taller BMW Olesa de Montserrat — Mantenimiento oficial sin coste de concesionario",
            "Taller BMW Olesa de Montserrat — Mantenimiento",
        ),
        'metaDescription': (
            "Taller especialista BMW en Olesa de Montserrat. Revisión CBS en garantía según normativa europea. Diagnóstico ISTA y recambio OE. Ahorra hasta un 50%.",
            "Taller especialista BMW en Olesa de Montserrat. Revisión CBS en garantía según normativa europea. Diagnóstico y recambio OE.",
        ),
    },
    'palau-solita-i-plegamans': {
        'metaTitle': (
            "BMW Palau-solità i Plegamans — Tu taller especialista con precios de hasta -50%",
            "BMW Palau-solità i Plegamans — Tu taller especialista",
        ),
        'metaDescription': (
            "Tu taller BMW de confianza en Palau-solità i Plegamans. Revisiones CBS, reparación especializada y diagnóstico ISTA. Garantía intacta y presupuestos cerrados.",
            "Tu taller BMW de confianza en Palau-solità i Plegamans. Revisiones CBS, reparación especializada y diagnóstico. Garantía intacta y presupuestos cerrados.",
        ),
    },
    'paracuellos-de-jarama': {
        'metaTitle': (
            "Taller BMW en Paracuellos de Jarama — Especialistas M con ISTA",
            "Taller BMW en Paracuellos de Jarama — Especialistas",
        ),
        'metaDescription': (
            "Taller especialista en BMW y BMW M en Paracuellos de Jarama. Diagnóstico ISTA, revisiones CBS y mecánica de alto rendimiento. Presupuesto cerrado.",
            "Taller especialista en BMW en Paracuellos de Jarama. Diagnóstico, revisiones CBS y mecánica. Presupuesto cerrado.",
        ),
    },
    'parets-del-valles': {
        'metaTitle': (
            "BMW Parets del Vallès — Tu taller especialista con precios de hasta -50%",
            "BMW Parets del Vallès — Tu taller especialista",
        ),
        'metaDescription': (
            "Tu taller BMW de confianza en Parets del Vallès. Revisiones CBS, reparación especializada y diagnóstico ISTA. Garantía intacta y presupuestos cerrados.",
            "Tu taller BMW de confianza en Parets del Vallès. Revisiones CBS, reparación especializada y diagnóstico. Garantía intacta y presupuestos cerrados.",
        ),
    },
    'parla': {
        'metaDescription': (
            "Taller especializado en BMW en Parla. Diagnóstico ISTA, motor, turbo, cajas ZF y electrónica. Presupuesto cerrado y garantía por escrito.",
            "Taller especializado en BMW en Parla. Diagnóstico, motor, turbo, cajas ZF y electrónica. Presupuesto cerrado y garantía por escrito.",
        ),
    },
    'piera': {
        'metaTitle': (
            "Taller BMW Piera — Mantenimiento oficial sin coste de concesionario",
            "Taller BMW Piera — Mantenimiento",
        ),
        'metaDescription': (
            "Taller especialista BMW en Piera. Revisión CBS en garantía según normativa europea. Diagnóstico ISTA y recambio OE. Ahorra hasta un 50%.",
            "Taller especialista BMW en Piera. Revisión CBS en garantía según normativa europea. Diagnóstico y recambio OE.",
        ),
    },
    'pineda-de-mar': {
        'metaDescription': (
            "Taller BMW en Pineda de Mar: mantenimiento, revisiones CBS y reparación con diagnóstico ISTA oficial. Recambios OE. Sin perder la garantía del fabricante.",
            "Taller BMW en Pineda de Mar: mantenimiento, revisiones CBS y reparación con diagnóstico. Recambios OE. Sin perder la garantía del fabricante.",
        ),
    },
    'pinto': {
        'metaDescription': (
            "Taller especializado BMW en Pinto: mantenimiento, frenos, distribución, cajas ZF y diagnosis original. Presupuesto cerrado y garantía en cada reparación.",
            "Taller especializado BMW en Pinto: mantenimiento, frenos, distribución, cajas ZF y diagnosis. Presupuesto cerrado y garantía en cada reparación.",
        ),
    },
    'pozuelo-de-alarcon': {
        'metaDescription': (
            "Taller especialista BMW en Pozuelo de Alarcón. Diagnóstico ISTA, revisiones CBS y mecánica para tu BMW. Ahorra hasta un 50 % frente al concesionario.",
            "Taller especialista BMW en Pozuelo de Alarcón. Diagnóstico, revisiones CBS y mecánica para tu BMW.",
        ),
    },
    'reus': {
        'metaTitle': (
            "Taller BMW en Reus | Especialistas en diagnóstico ISTA",
            "Taller BMW en Reus | Especialistas en diagnóstico",
        ),
        'metaDescription': (
            "Taller especialista BMW en Reus. Diagnóstico ISTA, mecánica adaptada al clima mediterráneo del Camp de Tarragona. Ahorra hasta un 50% frente al oficial.",
            "Taller especialista BMW en Reus. Diagnóstico y mecánica adaptada al clima mediterráneo del Camp de Tarragona.",
        ),
    },
    'ripollet': {
        'metaDescription': (
            "Revisión CBS, diagnóstico ISTA y mecánica para tu BMW en Ripollet. Mantén tu garantía oficial y ahorra hasta un 50 % frente al concesionario. Pide presupuesto.",
            "Revisión CBS, diagnóstico y mecánica para tu BMW en Ripollet. Mantén tu garantía. Pide presupuesto.",
        ),
    },
    'rivas-vaciamadrid': {
        'metaDescription': (
            "Taller BMW especializado en Rivas-Vaciamadrid: mantenimiento, frenos, distribución, cajas ZF y diagnosis original. Presupuesto cerrado y garantía real.",
            "Taller BMW especializado en Rivas-Vaciamadrid: mantenimiento, frenos, distribución, cajas ZF y diagnosis. Presupuesto cerrado y garantía real.",
        ),
    },
    'san-agustin-del-guadalix': {
        'metaDescription': (
            "Tu taller especialista BMW en San Agustín del Guadalix. Revisiones CBS con aceite LL-04, diagnóstico ISTA y ahorro del 50 % vs. concesionario. Pide presupuesto.",
            "Tu taller especialista BMW en San Agustín del Guadalix. Revisiones CBS con aceite LL-04 y diagnóstico. Pide presupuesto.",
        ),
    },
    'san-lorenzo-de-el-escorial': {
        'metaDescription': (
            "Taller especializado BMW en San Lorenzo de El Escorial. Diagnosis oficial, mantenimiento y reparación adaptados a la conducción de sierra y frío invernal.",
            "Taller especializado BMW en San Lorenzo de El Escorial. Diagnosis, mantenimiento y reparación adaptados a la conducción de sierra y frío invernal.",
        ),
    },
    'san-sebastian-de-los-reyes': {
        'metaTitle': (
            "Taller BMW en San Sebastián de los Reyes — Especialistas ISTA",
            "Taller BMW en San Sebastián de los Reyes — Especialistas",
        ),
        'metaDescription': (
            "Taller especialista en BMW en San Sebastián de los Reyes. Diagnóstico ISTA, revisiones CBS y averías DPF/AdBlue. Ahorra hasta un 50 % frente al concesionario.",
            "Taller especialista en BMW en San Sebastián de los Reyes. Diagnóstico, revisiones CBS y averías DPF/AdBlue.",
        ),
    },
    'sant-adria-de-besos': {
        'metaDescription': (
            "Conserva la garantía oficial de tu BMW en Sant Adrià de Besòs. Somos el taller especialista con diagnóstico ISTA y un ahorro de hasta el 50 %. Pide presupuesto.",
            "Conserva la garantía de tu BMW en Sant Adrià de Besòs. Somos el taller especialista con diagnóstico. Pide presupuesto.",
        ),
    },
    'sant-andreu-de-la-barca': {
        'metaTitle': (
            "Taller BMW M en Sant Andreu de la Barca – Especialistas S55/S58",
            "Taller BMW en Sant Andreu de la Barca – Especialistas",
        ),
        'metaDescription': (
            "Tu especialista BMW en Sant Andreu de la Barca. Expertos en M (S55/S58), diagnóstico ISTA y mantenimiento de alto rendimiento. Ahorra hasta un 50 %.",
            "Tu especialista BMW en Sant Andreu de la Barca. Diagnóstico, mantenimiento y reparación de tu BMW o MINI.",
        ),
    },
    'sant-boi-de-llobregat': {
        'metaDescription': (
            "Taller especialista en BMW en Sant Boi de Llobregat. Mantenimiento preventivo, cadena N47/B47, Vanos y diagnóstico ISTA. Ahorra hasta un 50 %.",
            "Taller especialista en BMW en Sant Boi de Llobregat. Mantenimiento preventivo, cadena N47/B47, Vanos y diagnóstico.",
        ),
    },
    'sant-celoni': {
        'metaDescription': (
            "Especialistas BMW en Sant Celoni. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Sant Celoni. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'sant-just-desvern': {
        'metaDescription': (
            "Tu taller especialista BMW en Sant Just Desvern. Ahorra hasta un 50% en revisión CBS, distribución N47 y averías complejas. Pide tu presupuesto cerrado.",
            "Tu taller especialista BMW en Sant Just Desvern. Revisión CBS, distribución N47 y averías complejas. Pide tu presupuesto cerrado.",
        ),
    },
    'sant-quirze-del-valles': {
        'metaTitle': (
            "Taller especializado BMW en Sant Quirze del Vallès — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Sant Quirze del Vallès — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Sant Quirze del Vallès? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Sant Quirze del Vallès? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'santa-perpetua-de-mogoda': {
        'metaTitle': (
            "Taller especializado BMW en Santa Perpètua de Mogoda — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Santa Perpètua de Mogoda — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Santa Perpètua de Mogoda? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Santa Perpètua de Mogoda? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'santpedor': {
        'metaDescription': (
            "Taller BMW en Santpedor: mantenimiento, revisiones CBS y reparación con diagnóstico ISTA oficial. Recambios OE. Sin perder la garantía del fabricante.",
            "Taller BMW en Santpedor: mantenimiento, revisiones CBS y reparación con diagnóstico. Recambios OE. Sin perder la garantía del fabricante.",
        ),
    },
    'sentmenat': {
        'metaDescription': (
            "Tu taller BMW de confianza en Sentmenat. Revisiones CBS, reparación especializada y diagnóstico ISTA. Garantía intacta y presupuestos cerrados.",
            "Tu taller BMW de confianza en Sentmenat. Revisiones CBS, reparación especializada y diagnóstico. Garantía intacta y presupuestos cerrados.",
        ),
    },
    'sitges': {
        'metaDescription': (
            "Especialistas BMW en Sitges. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Sitges. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'terrassa': {
        'metaDescription': (
            "Especialistas BMW en Terrassa. Diagnóstico ISTA/Rheingold, aceite LL-04 y recambios OE. Tu garantía BMW intacta y hasta un 50% de ahorro.",
            "Especialistas BMW en Terrassa. Diagnóstico, aceite LL-04 y recambios OE. Tu garantía BMW intacta.",
        ),
    },
    'tordera': {
        'metaTitle': (
            "Taller especializado BMW en Tordera — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Tordera — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Tordera? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Tordera? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'torrelodones': {
        'metaDescription': (
            "Taller especializado BMW en Torrelodones. Diagnosis con equipo original ISTA, reparación de motor, Vanos, turbo y caja ZF 8HP. Presupuesto cerrado y garantía escrita.",
            "Taller especializado BMW en Torrelodones. Diagnosis, reparación de motor, Vanos, turbo y caja ZF 8HP. Presupuesto cerrado y garantía escrita.",
        ),
    },
    'tres-cantos': {
        'metaTitle': (
            "Taller BMW en Tres Cantos — Especialistas N47 y Diagnóstico ISTA",
            "Taller BMW en Tres Cantos — Especialistas N47 y Diagnóstico",
        ),
        'metaDescription': (
            "Tu taller especialista BMW en Tres Cantos. Ahorra hasta un 50 % en averías de cadena (N47/B47), turbo y revisiones CBS. Presupuesto cerrado.",
            "Tu taller especialista BMW en Tres Cantos. Averías de cadena (N47/B47), turbo y revisiones CBS. Presupuesto cerrado.",
        ),
    },
    'valdemorillo': {
        'metaTitle': (
            "Taller BMW en Valdemorillo | Diagnosis y mecánica oficial",
            "Taller BMW en Valdemorillo | Diagnosis y mecánica",
        ),
        'metaDescription': (
            "Taller BMW para Valdemorillo y la sierra oeste de Madrid: diagnosis original, Vanos, turbo, caja ZF 8HP y refrigeración. Presupuesto cerrado. Pide cita.",
            "Taller BMW para Valdemorillo y la sierra oeste de Madrid: diagnosis, Vanos, turbo, caja ZF 8HP y refrigeración. Presupuesto cerrado. Pide cita.",
        ),
    },
    'valdemoro': {
        'metaTitle': (
            "Taller BMW en Valdemoro | Diagnosis original y mecánica",
            "Taller BMW en Valdemoro | Diagnosis y mecánica",
        ),
        'metaDescription': (
            "Taller BMW en Valdemoro: diagnosis con software oficial, revisión de Vanos, turbo, caja ZF 8HP y refrigeración. Presupuesto cerrado. Pide cita hoy.",
            "Taller BMW en Valdemoro: diagnosis, revisión de Vanos, turbo, caja ZF 8HP y refrigeración. Presupuesto cerrado. Pide cita hoy.",
        ),
    },
    'velilla-de-san-antonio': {
        'metaDescription': (
            "Servicio BMW para Velilla de San Antonio: diagnosis original, revisión de Vanos, turbo y caja ZF 8HP. Presupuesto por escrito y recogida disponible.",
            "Servicio BMW para Velilla de San Antonio: diagnosis, revisión de Vanos, turbo y caja ZF 8HP. Presupuesto por escrito.",
        ),
    },
    'vic': {
        'metaTitle': (
            "Taller especializado BMW en Vic — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Vic — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Vic? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Vic? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'viladecans': {
        'metaDescription': (
            "Taller especialista BMW en Viladecans. Diagnóstico ISTA, revisión CBS con aceite LL-04 y mecánica para tu Serie 3/5. Pide presupuesto cerrado.",
            "Taller especialista BMW en Viladecans. Diagnóstico, revisión CBS con aceite LL-04 y mecánica para tu Serie 3/5. Pide presupuesto cerrado.",
        ),
    },
    'vilanova-i-la-geltru': {
        'metaTitle': (
            "Taller especializado BMW en Vilanova i la Geltrú — Diagnóstico ISTA y recambio OE",
            "Taller especializado BMW en Vilanova i la Geltrú — Diagnóstico y recambio OE",
        ),
        'metaDescription': (
            "¿Buscas un taller BMW en Vilanova i la Geltrú? Servicio especialista con diagnóstico oficial ISTA, recambios de primer equipo y precios hasta un 50% por debajo del concesionario.",
            "¿Buscas un taller BMW en Vilanova i la Geltrú? Servicio especialista con diagnóstico y recambios de primer equipo.",
        ),
    },
    'villanueva-de-la-canada': {
        'metaTitle': (
            "Taller BMW en Villanueva de la Cañada | Diagnosis ISTA",
            "Taller BMW en Villanueva de la Cañada | Diagnosis",
        ),
        'metaDescription': (
            "Taller BMW especializado en Villanueva de la Cañada, oeste de Madrid. Diagnosis ISTA, mantenimiento y reparación de averías. Presupuesto claro.",
            "Taller BMW especializado en Villanueva de la Cañada, oeste de Madrid. Diagnosis, mantenimiento y reparación de averías. Presupuesto claro.",
        ),
    },
    'villanueva-del-pardillo': {
        'metaTitle': (
            "Taller BMW en Villanueva del Pardillo | Diagnosis ISTA",
            "Taller BMW en Villanueva del Pardillo | Diagnosis",
        ),
        'metaDescription': (
            "Taller BMW especializado en Villanueva del Pardillo, oeste de Madrid. Diagnosis ISTA, mantenimiento y reparación de averías comunes. Presupuesto claro.",
            "Taller BMW especializado en Villanueva del Pardillo, oeste de Madrid. Diagnosis, mantenimiento y reparación de averías comunes. Presupuesto claro.",
        ),
    },
    'zaragoza': {
        'metaDescription': (
            "Taller especializado en BMW en Zaragoza. Diagnosis ISTA original, mantenimiento, reparación de motor, turbo y caja ZF 8HP. Presupuesto sin compromiso.",
            "Taller especializado en BMW en Zaragoza. Diagnosis, mantenimiento, reparación de motor, turbo y caja ZF 8HP. Presupuesto sin compromiso.",
        ),
    },
}

PROHIBIDO = re.compile(
    r"(?-i:\bISTA\b)|Rheingold|oficial|%|recogida|domicilio|minutos?\b|\bmin\b|ahorr|"
    r"(?-i:\bBMW M\b)|(?-i:\bM\b)|S55|S58|alto rendimiento|coste de concesionario|"
    r"diagnos\w* (con )?(software |equipo )?original|de referencia",
    re.I,
)


def comprobar():
    vistos = {}
    for slug, campos in CAMBIOS.items():
        for campo, (antes, despues) in campos.items():
            assert antes != despues, (slug, campo)
            assert not PROHIBIDO.search(despues), (slug, campo, despues)
            assert not re.search(r"\s[,.]|\.\.|,\s*\.|\by\s*\.", despues), (slug, campo, despues)
            if campo == "metaTitle":
                assert despues not in vistos, (slug, vistos.get(despues))
                vistos[despues] = slug
            else:
                assert len(despues) >= 90, (slug, len(despues), despues)


def aplicar():
    comprobar()
    cambiados = 0
    for slug, campos in CAMBIOS.items():
        f = CIUDADES_DIR / f"{slug}.json"
        cj = json.loads(f.read_text("utf-8"))
        tocado = False
        for campo, (antes, despues) in campos.items():
            actual = cj.get(campo)
            if actual == despues:
                continue
            if actual != antes:
                print(f"AVISO {slug}.{campo}: el valor actual no es el esperado; no se toca\n  {actual}")
                continue
            cj[campo] = despues
            tocado = True
            print(campo, slug)
        if tocado:
            f.write_text(json.dumps(cj, ensure_ascii=False, indent=2) + "\n", "utf-8")
            cambiados += 1
    print(f"{cambiados} ficheros cambiados de {len(CAMBIOS)}")


if __name__ == "__main__":
    aplicar()
