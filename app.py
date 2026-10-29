import os, json, sqlite3
DB_BE = os.path.join(os.path.dirname(__file__), "database_be.sqlite")

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

from http.server import HTTPServer, BaseHTTPRequestHandler
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
            conn = sqlite3.connect(DB_BE); conn.row_factory = sqlite3.Row; cur = conn.cursor()
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
                    "IDOperacion": a.get("oper"),
                    "CodSegFact": a.get("CodSegFact"),
                })
            conn.close(); return self.send_json(resumen)
        elif path == "/db_tables":
            conn = sqlite3.connect(DB_BE); cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
            tablas = [r[0] for r in cur.fetchall()]; conn.close()
            return self.send_json({"tables": tablas})
        elif path.startswith("/db_schema/"):
            t = path.split("/")[-1]; conn = sqlite3.connect(DB_BE); cur = conn.cursor()
            cur.execute(f'SELECT * FROM "{t}" WHERE 1=0')
            cols = [{"name": c[0], "type": str(c[1]), "nullable": c[6]} for c in cur.description]
            conn.close(); return self.send_json({"table": t, "columns": cols})
        else:
            return self.send_json({"error":"Not found"}, 404)

if __name__ == "__main__":
    print("Servidor SQLite http://localhost:5000")
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
