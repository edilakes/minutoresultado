import sqlite3, sys, os
import subprocess, sys
try:
    import pyodbc
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyodbc"])
    import pyodbc
except:
    print("pyodbc no disponible; instala: python -m pip install pyodbc")
    sys.exit(1)
DB_BE = os.environ.get("MR_DB_BE", r"\\nas.cifs.cti-sevilla.sas.junta-andalucia.es\SSCC-CONSTITUCION-1\SSCC\Sb-ServiciosGestionCentros\FondosEuropeos\Database_be.accdb")
SQLITE_PATH = os.path.join(os.path.dirname(__file__), "database_be.sqlite")
conn_acc = pyodbc.connect(f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_BE};ReadOnly=1;", readonly=True, autocommit=True)
cur_acc = conn_acc.cursor()
tablas = [r.table_name for r in cur_acc.tables(tableType='TABLE') if not r.table_name.startswith('MSys') and not r.table_name.startswith('~')]
conn_sql = sqlite3.connect(SQLITE_PATH)
for t in tablas:
    try:
        cur_acc.execute(f"SELECT * FROM [{t}]")
        cols = [c[0] for c in cur_acc.description]
        filas = cur_acc.fetchall()
        # Crear tabla SQLite con tipos aproximados
        tipos = {c: "REAL" if isinstance(cur_acc.description[i][1], (int, float)) else "TEXT" for i, c in enumerate(cols)}
        cols_def = ", ".join([f'"{c}" {tipos[c]}' for c in cols])
        conn_sql.execute(f"DROP TABLE IF EXISTS \"{t}\"")
        conn_sql.execute(f"CREATE TABLE \"{t}\" ({cols_def})")
        for fila in filas:
            from decimal import Decimal
            vals = [float(v) if isinstance(v, Decimal) else (v if v is not None else (0 if isinstance(v, (int, float)) else "")) for v in fila]
            placeholders = ", ".join(["?" for _ in fila])
            conn_sql.execute(f'INSERT INTO "{t}" VALUES ({placeholders})', vals)
        print(f"Exportada: {t} ({len(filas)} filas)")
    except Exception as e:
        print(f"Error en {t}: {e}")
conn_sql.commit()
conn_sql.close()
print(f"SQLite creado: {SQLITE_PATH}")
