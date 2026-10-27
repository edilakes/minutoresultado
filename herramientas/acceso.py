"""Acceso de SOLO LECTURA a las bases Access del proyecto Minuto y Resultado.

Uso rápido:
    from herramientas.acceso import conectar, consultar
    filas = consultar("SELECT TOP 5 * FROM ActuacionesT")

Las rutas se pueden sobrescribir con variables de entorno:
    MR_DB_BE  -> backend (datos)      Database_be.accdb en el NAS
    MR_DB_FE  -> frontend (formularios, informes, consultas) Database_fe.accdb
"""
import os

import pyodbc

DB_BE = os.environ.get(
    "MR_DB_BE",
    r"\\nas.cifs.cti-sevilla.sas.junta-andalucia.es\SSCC-CONSTITUCION-1\SSCC"
    r"\Sb-ServiciosGestionCentros\FondosEuropeos\Database_be.accdb",
)
DB_FE = os.environ.get(
    "MR_DB_FE",
    r"C:\Users\lagosedgar20p\Desktop\Database_fe.accdb",
)
NORMATIVA_DIR = os.environ.get("MR_NORMATIVA", r"F:\EDG\Normativa")

_DRIVER = "{Microsoft Access Driver (*.mdb, *.accdb)}"


def conectar(ruta=None, readonly=True):
    """Abre una conexión ODBC a Access. Por defecto, solo lectura sobre el backend."""
    ruta = ruta or DB_BE
    conn_str = f"Driver={_DRIVER};DBQ={ruta};"
    if readonly:
        conn_str += "ReadOnly=1;"
    return pyodbc.connect(conn_str, readonly=readonly, autocommit=True)


def consultar(sql, params=(), ruta=None):
    """Ejecuta un SELECT y devuelve (columnas, filas). Rechaza cualquier otra sentencia."""
    if not sql.lstrip().upper().startswith("SELECT"):
        raise ValueError("Solo se permiten consultas SELECT")
    conn = conectar(ruta)
    try:
        cur = conn.cursor()
        cur.execute(sql, params)
        columnas = [c[0] for c in cur.description]
        filas = cur.fetchall()
        return columnas, filas
    finally:
        conn.close()
