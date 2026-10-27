"""Fase 1 del plan: genera docs/datos/00_inventario.md y docs/datos/01_frontend.md.

Solo lectura. Requiere haber ejecutado antes herramientas/extraer_metadatos.ps1
(crea datos/metadatos_be.json y datos/metadatos_fe.json).

Uso:  python -m herramientas.inventario
"""
import datetime
import json
import warnings
from collections import Counter
from pathlib import Path

import pandas as pd

from herramientas.acceso import DB_BE, conectar

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "datos"
DOCS = RAIZ / "docs" / "datos"

TIPOS_DAO = {
    1: "Sí/No", 2: "Byte", 3: "Entero", 4: "Entero largo", 5: "Moneda", 6: "Simple",
    7: "Doble", 8: "Fecha/Hora", 9: "Binario", 10: "Texto", 11: "OLE", 12: "Memo/Texto largo",
    15: "GUID", 16: "BigInt", 17: "Binario var.", 18: "Char", 19: "Numérico",
    20: "Decimal", 21: "Float", 22: "Hora", 23: "Marca de tiempo", 101: "Adjunto",
    102: "Complejo (multivalor)",
}
MAX_TXT = 60
TIPOS_NUMERICOS = (2, 3, 4, 5, 6, 7, 8, 19, 20, 21)


def _categoria(nombre):
    if nombre[:6].isdigit():
        return "revisión puntual"
    if nombre.startswith("Estado") or nombre.startswith("Tipos") or nombre in ("ProvT", "TextosT"):
        return "catálogo"
    if nombre.startswith("Rel"):
        return "relación N:M"
    if "Indicadores" in nombre or nombre in ("MedidasT", "ObjetivosEspecificosT", "AmbitoIntervencionT"):
        return "marco FEDER"
    return "datos"


def _corto(v):
    s = str(v).replace("\r", " ").replace("\n", " ").strip()
    return s if len(s) <= MAX_TXT else s[:MAX_TXT] + "…"


def _esc(s):
    return str(s).replace("|", "\\|")


def perfilar(conn, tabla, campos):
    """Devuelve (nº filas, [(campo, nulos, distintos, frecuentes, rango, total)])."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        df = pd.read_sql(f"SELECT * FROM [{tabla}]", conn)
    filas = []
    for c in campos:
        n = c["nombre"]
        if n not in df.columns:
            continue
        s = df[n]
        nulos = int(s.isna().sum())
        try:
            distintos = int(s.nunique(dropna=True))
        except TypeError:
            distintos = -1
        top = ""
        if 0 < distintos <= 400 or c["tipo"] in (1, 3, 4, 10):
            try:
                cuenta = Counter(s.dropna().map(_corto)).most_common(6)
                top = "; ".join(f"{k} ({v})" for k, v in cuenta)
            except TypeError:
                pass
        rango = ""
        if c["tipo"] in TIPOS_NUMERICOS and nulos < len(s):
            try:
                rango = f"{_corto(s.min())} → {_corto(s.max())}"
            except TypeError:
                pass
        filas.append((c, nulos, distintos, top, rango, len(s)))
    return len(df), filas


def _mermaid(rels):
    er = ["```mermaid", "erDiagram"]
    vistos = set()
    for r in rels:
        k = (r["TablaPrimaria"], r["TablaSecundaria"], r["CampoForaneo"])
        if k in vistos:
            continue
        vistos.add(k)
        a, b = (x.replace("-", "_") for x in (r["TablaPrimaria"], r["TablaSecundaria"]))
        a = "t" + a if a[0].isdigit() else a
        b = "t" + b if b[0].isdigit() else b
        er.append(f'    {a} ||--o{{ {b} : "{r["CampoForaneo"].replace(".", "_")}"')
    er.append("```")
    return er


def _detalle_tabla(nombre, t, n, perfil, rels):
    pk = [i["campos"] for i in t["indices"] if i["primario"]]
    d = [f"### {nombre}\n",
         f"- Categoría: {_categoria(nombre)} · Filas: **{n}** · Columnas: **{len(t['campos'])}**"
         f" · Clave primaria: {', '.join(pk[0]) if pk else '—'}"]
    ent = [r for r in rels if r["TablaSecundaria"] == nombre]
    sal = [r for r in rels if r["TablaPrimaria"] == nombre]
    if ent:
        d.append("- Referencia a: " + "; ".join(
            f"`{r['CampoForaneo']}` → {r['TablaPrimaria']}.{r['CampoPrimario']}" for r in ent))
    if sal:
        d.append("- Referenciada por: " + "; ".join(
            f"{r['TablaSecundaria']}.{r['CampoForaneo']}" for r in sal))
    d += ["", "| Columna | Tipo | % nulos | Distintos | Rango | Valores frecuentes | Descripción (Access) |",
          "|---|---|---|---|---|---|---|"]
    for c, nulos, dist, top, rango, tot in perfil:
        pct = f"{100 * nulos / tot:.0f}%" if tot else "—"
        d.append(f"| {_esc(c['nombre'])} | {TIPOS_DAO.get(c['tipo'], c['tipo'])} | {pct} | "
                 f"{dist if dist >= 0 else '—'} | {_esc(rango)} | {_esc(top)} | {_esc(c['descripcion'] or '')} |")
    d.append("")
    return d


def _frontend(fe, tablas, hoy):
    f = [
        "# Inventario del frontend Access (`Database_fe.accdb`)\n",
        f"- Generado: **{hoy}** · Origen: `{fe['ruta']}`",
        f"- Tablas vinculadas al backend: **{len(fe['tablas'])}**",
        f"- Consultas: **{len(fe['consultas'])}** · Formularios: **{len(fe['formularios'])}** · "
        f"Informes: **{len(fe['informes'])}** · Módulos VBA: **{len(fe['modulos'])}** · Macros: **{len(fe['macros'])}**",
        "- El SQL completo de cada consulta está en `datos/metadatos_fe.json` (local, fuera de git).\n",
        "## Formularios\n", ", ".join(f"`{x}`" for x in fe["formularios"]), "",
        "## Informes\n", ", ".join(f"`{x}`" for x in fe["informes"]), "",
        "## Módulos y macros\n", ", ".join(f"`{x}`" for x in fe["modulos"] + fe["macros"]), "",
        "## Consultas guardadas\n",
        "| Consulta | Tipo | Lee de (tablas/consultas) |", "|---|---|---|",
    ]
    nombres = [x["nombre"] for x in fe["consultas"]] + list(tablas)
    tipos = {0: "select", 16: "crosstab", 32: "delete", 48: "update", 64: "append",
             80: "make-table", 96: "DDL", 112: "passthrough", 128: "union"}
    for q in sorted(fe["consultas"], key=lambda x: x["nombre"]):
        sql = q["sql"] or ""
        usa = [n for n in nombres if n != q["nombre"] and (f"[{n}]" in sql or f"{n}." in sql
                                                           or f" {n} " in sql or f" {n}\r" in sql
                                                           or f" {n}\n" in sql or sql.rstrip(" ;\r\n").endswith(f" {n}"))]
        f.append(f"| {_esc(q['nombre'])} | {tipos.get(q['tipo'], q['tipo'])} | {_esc(', '.join(usa[:8]))} |")
    return f


def main():
    be = json.loads((DATOS / "metadatos_be.json").read_text(encoding="utf-8-sig"))
    fe = json.loads((DATOS / "metadatos_fe.json").read_text(encoding="utf-8-sig"))
    DOCS.mkdir(parents=True, exist_ok=True)

    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM RelacionesAccessT")
    cols = [d[0] for d in cur.description]
    rels = [dict(zip(cols, r)) for r in cur.fetchall() if not r[1].startswith("MSys")]

    tablas = {t["nombre"]: t for t in be["tablas"]}
    resumen, detalle = [], []
    for nombre, t in tablas.items():
        n, perfil = perfilar(conn, nombre, t["campos"])
        resumen.append((nombre, _categoria(nombre), n, len(t["campos"])))
        detalle += _detalle_tabla(nombre, t, n, perfil, rels)
    conn.close()

    hoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    out = [
        "# Inventario del backend Access (`Database_be.accdb`)\n",
        f"- Generado: **{hoy}** (solo lectura, sobre el NAS)",
        f"- Origen: `{DB_BE}`",
        "- Generado por: `herramientas/inventario.py`",
        f"- Tablas: **{len(tablas)}** · Relaciones declaradas en `RelacionesAccessT`: **{len(rels)}**",
        "- Observación: las relaciones están **sin integridad referencial**, así que Access no impide huérfanos.\n",
        "## 1. Resumen de tablas\n",
        "| Tabla | Categoría | Filas | Columnas |",
        "|---|---|---|---|",
    ]
    for nombre, cat, n, nc in sorted(resumen, key=lambda x: (x[1], -x[2])):
        out.append(f"| {nombre} | {cat} | {n} | {nc} |")
    out += ["", "## 2. Diagrama de relaciones\n", *_mermaid(rels), "", "## 3. Detalle por tabla\n", *detalle]
    (DOCS / "00_inventario.md").write_text("\n".join(out), encoding="utf-8")
    (DOCS / "01_frontend.md").write_text("\n".join(_frontend(fe, tablas, hoy)), encoding="utf-8")
    print("OK ->", DOCS)


if __name__ == "__main__":
    main()

