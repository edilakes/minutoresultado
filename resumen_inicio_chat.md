---
referencia: contexto base para nuevos chats (agente)
app: minutoresultado
version_documento: 202610290956
---

## 1. Proyecto / Contexto (referencia)
Servidor local (app.py) que expone datos de Access (Database_be.accdb) y sirve portada.html. El agente usa este archivo como punto de referencia inicial.

## 2. Aplicación (minutoresultado)
- app.py: http.server en puerto 5000 (Flask eliminado).
- portada.html: UI que consume /actuaciones_resumen.
- Endpoints: /actuaciones_resumen, /db_tables, /db_schema/<table>, /db_data/<table>.
- Dependencia clave: pyodbc (auto-instala en runtime si falta).
- Base de datos: \nas...\SSCC...\Database_be.accdb (solo lectura).

## 3. Análisis de datos (enfoque)
Objetivo: diseñar análisis sobre ActuacionesT.
Variables clave: EstadoActuacion, Cubierta, N, IMPORTE TOTAL, PROVINCIA, CentroSanitario.
Conceptos: macroestado, responsable, alerta, progreso.
Queries de referencia: /db_query?sql=SELECT...

## 4. Glosario / Conceptos generales (mejoran con versiones)
- DB_BE: ruta NAS a la base Access (.accdb).
- pyodbc: módulo Python para conectar a Access; se instala automáticamente si falta.
- http.server: reemplazo de Flask para evitar dependencias externas.

Nota: este documento es referencia viva. Actualizar glosario y variables según nuevas versiones.
