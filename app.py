from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

# -----------------------------
# 1. Conexión a la base en NAS
# -----------------------------
def conectar():
    DB_PATH = r"\\nas.cifs.cti-sevilla.sas.junta-andalucia.es\SSCC-CONSTITUCION-1\SSCC\Sb-ServiciosGestionCentros\FondosEuropeos\Database_be.accdb"
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        fr"DBQ={DB_PATH};"
    )
    return pyodbc.connect(conn_str)


# -----------------------------
# 2. Lógica de macroestado
# -----------------------------
def macroestado(est):
    if est >= 8:
        return "finalizada"
    if est == 7:
        return "ejecucion"
    if est == 6:
        return "licitacion-obra"
    if est == 5:
        return "proyecto"
    if est == 4:
        return "redaccion"
    if est == 3:
        return "licitacion"
    return "pendiente"


# -----------------------------
# 3. Responsable actual
# -----------------------------
def responsable(macro):
    if macro == "pendiente":
        return "Órgano gestor"
    if macro in ("licitacion", "redaccion"):
        return "Proyecto"
    if macro == "proyecto":
        return "DO"
    if macro == "licitacion-obra":
        return "Contratación"
    if macro == "ejecucion":
        return "Empresa"
    if macro == "finalizada":
        return "—"
    return "—"


# -----------------------------
# 4. Alertas
# -----------------------------
def alerta(macro, cubierta):
    # cubierta=False → DO no adjudicada en tu dataset
    if macro == "licitacion-obra" and not cubierta:
        return "⚠️ DO pendiente (crítica)"
    if macro == "proyecto" and not cubierta:
        return "⚠️ Proyecto recibido sin DO adjudicada"
    return ""


# -----------------------------
# 5. Endpoint resumen
# -----------------------------
@app.get("/actuaciones_resumen")
def actuaciones_resumen():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ActuacionesT")
    columnas = [c[0] for c in cursor.description]
    filas = cursor.fetchall()

    resumen = []

    for fila in filas:
        a = dict(zip(columnas, fila))

        est_macro = macroestado(a.get("EstadoActuacion", 0))
        resp = responsable(est_macro)
        al = alerta(est_macro, a.get("Cubierta", True))

        resumen.append({
            "CodActuacion": a.get("CodActuacion"),
            "CentroSanitario": a.get("CENTRO SANITARIO"),
            "Provincia": a.get("PROVINCIA"),
            "OrganoGestor": a.get("ORGANO GESTOR"),
            "Medida": a.get("MedidaUnificada") or a.get("Medida"),
            "EstadoActuacion": a.get("EstadoActuacion"),
            "Macroestado": est_macro,
            "ResponsableActual": resp,
            "Alerta": al,
            "ProgresoEstimado": round((a.get("N", 0) or 0) * 10),
            "ImporteTotal": a.get("IMPORTE TOTAL "),
            "FE04": a.get("FE04"),
            "Operacion": a.get("Operacion"),
            "IDActuacion": a.get("IDActuacion")
        })

    conn.close()
    return jsonify(resumen)
# NUEVO: 7. Listar todas las tablas
@app.get("/db_tables")
def db_tables():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM MSysObjects WHERE Type=1 AND Flags=0")
    tablas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify({"tables": tablas})

# NUEVO: 8. Esquema de tabla específica (columnas + tipos)
@app.get("/db_schema/<table_name>")
def db_schema(table_name):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM [{table_name}] WHERE 1=0")  # Solo metadata
    columnas = [{"name": c[0], "type": str(c[1]), "nullable": c[6]} for c in cursor.description]
    conn.close()
    return jsonify({"table": table_name, "columns": columnas})

# NUEVO: 9. Datos paginados de tabla (máx 1000 filas por llamada)
@app.get("/db_data/<table_name>")
def db_data(table_name):
    page = request.args.get("page", 1, type=int)
    limit = min(request.args.get("limit", 100, type=int), 1000)  # Límite seguridad
    offset = (page - 1) * limit
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT TOP {limit + 1} * FROM [{table_name}]")  # +1 para next_page
    filas = cursor.fetchall()
    columnas = [c[0] for c in cursor.description]
    
    data = [dict(zip(columnas, fila)) for fila in filas[:limit]]
    has_more = len(filas) > limit
    
    conn.close()
    return jsonify({
        "table": table_name,
        "page": page,
        "data": data,
        "next_page": page + 1 if has_more else None,
        "total_rows_estimate": "Usa COUNT(*) para exacto"  # Evitar COUNT en tablas grandes
    })

# NUEVO: 10. Consulta SQL personalizada (solo SELECT, sanitizada)
@app.get("/db_query")
def db_query():
    sql = request.args.get("sql", "").strip()
    if not sql.upper().startswith("SELECT"):  
        return jsonify({"error": "Solo SELECT permitidas"}), 400
    
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        columnas = [c[0] for c in cursor.description]
        filas = cursor.fetchall()
        data = [dict(zip(columnas, fila)) for fila in filas]
        conn.close()
        return jsonify({"results": data, "columns": columnas})
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 400


# -----------------------------
# 6. Arranque
# -----------------------------
app.run(host="0.0.0.0", port=5000)


