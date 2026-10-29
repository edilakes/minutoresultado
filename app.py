import os, json
from http.server import HTTPServer, BaseHTTPRequestHandler
# Auto-instalar pyodbc en runtime si falta
import sys, subprocess, importlib.util
try:
    import pyodbc
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyodbc"])
    import pyodbc



DB_BE = os.environ.get(
    "MR_DB_BE",
    r"\\nas.cifs.cti-sevilla.sas.junta-andalucia.es\SSCC-CONSTITUCION-1\SSCC"
    r"\Sb-ServiciosGestionCentros\FondosEuropeos\Database_be.accdb"
)
def macroestado(est):
    if est >= 8: return "finalizada"
    if est == 7: return "ejecucion"
    if est == 6: return "licitacion-obra"
    if est == 5: return "proyecto"
    if est == 4: return "redaccion"
    if est == 3: return "licitacion"
    return "pendiente"
def responsable(macro):
    if macro == "pendiente": return "Órgano gestor"
    if macro in ("licitacion", "redaccion"): return "Proyecto"
    if macro == "proyecto": return "DO"
    if macro == "licitacion-obra": return "Contratación"
    if macro == "ejecucion": return "Empresa"
    if macro == "finalizada": return "—"
    return "—"
def alerta(macro, cubierta):
    if macro == "licitacion-obra" and not cubierta: return "⚠️ DO pendiente (crítica)"
    if macro == "proyecto" and not cubierta: return "⚠️ Proyecto recibido sin DO adjudicada"
    return ""
class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args): pass
    def send_json(self, data, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False, default=str).encode("utf-8"))
    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/actuaciones_resumen":
            conn = pyodbc.connect(f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_BE};ReadOnly=1;", readonly=True, autocommit=True)
            cur = conn.cursor()
            cur.execute("SELECT * FROM ActuacionesT")
            cols = [c[0] for c in cur.description]
            resumen = []
            for fila in cur.fetchall():
                a = dict(zip(cols, fila))
                est_macro = macroestado(a.get("EstadoActuacion", 0) or 0)
                resumen.append({
                    "CodActuacion": a.get("CodActuacion"),
                    "CentroSanitario": a.get("CENTRO SANITARIO"),
                    "Provincia": a.get("PROVINCIA"),
                    "OrganoGestor": a.get("ORGANO GESTOR"),
                    "Medida": a.get("MedidaUnificada") or a.get("Medida"),
                    "EstadoActuacion": a.get("EstadoActuacion"),
                    "Macroestado": est_macro,
                    "ResponsableActual": responsable(est_macro),
                    "Alerta": alerta(est_macro, a.get("Cubierta", True)),
                    "ProgresoEstimado": round((a.get("N", 0) or 0) * 10),
                    "ImporteTotal": a.get("IMPORTE TOTAL "),
                    "FE04": a.get("FE04"),
                    "Operacion": a.get("Operacion"),
                    "CodSegFact": a.get("CodSegFact"),
                })
            conn.close()
            return self.send_json(resumen)
        elif path == "/db_tables":
            conn = pyodbc.connect(f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_BE};ReadOnly=1;", readonly=True, autocommit=True)
            cur = conn.cursor()
            cur.execute("SELECT Name FROM MSysObjects WHERE Type=1 AND Flags=0")
            tablas = [r[0] for r in cur.fetchall()]
            conn.close()
            return self.send_json({"tables": tablas})
        elif path.startswith("/db_schema/"):
            table_name = path.split("/")[-1]
            conn = pyodbc.connect(f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={DB_BE};ReadOnly=1;", readonly=True, autocommit=True)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM [{table_name}] WHERE 1=0")
            columnas = [{"name": c[0], "type": str(c[1]), "nullable": c[6]} for c in cur.description]
            conn.close()
            return self.send_json({"table": table_name, "columns": columnas})
        elif path.startswith("/db_data/"):
            table_name = path.split("/")[-1]
            return self.send_json({"table": table_name, "note":"paginación pendiente"})
        else:
            return self.send_json({"error":"Not found"}, 404)
if __name__ == "__main__":
    print("Servidor http://localhost:5000 (http.server, sin Flask)")
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
