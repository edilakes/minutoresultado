# Incongruencias detectadas — portada actual vs contexto real

> Detectadas tras análisis de portada.html, app.py, inventario (00_inventario.md), contexto normativo (PROGRESO.md/RESUMEN_NORMATIVA.md), datos reales de fetch (126.991 B) y archivo G: (Database_be.accdb 16.687.104 B).

- **portada.html línea 173**: URL fija a SEP00000C1Q7 (corregida a localhost:5000)
- **portada.html línea 267**: Referencia a a.IDActuacion que NO existe en el endpoint /actuaciones_resumen (solo CodActuacion)
- **portada.html**: No muestra contexto normativo ni fecha límite (RDC 63.2: 31/12/2029) ni marco FEDER (RSO2.1/RSO2.2)
- **portada.html / app.py**: No integran datos de CreditosT (1751 filas), ExpediEntesT (46 filas, 81 cols), ni relaciones N:M (RelLoteActuacionT: 408)
- **portada.html**: No indica fuente de datos (G: / NAS / Database_be.accdb) ni estado de conexión
- **portada.html CSS**: .alerta-critica solo cambia border-color a rojo; no hay indicador de severidad en la tarjeta (normativa: alerta crítica DO pendiente debe ser visible)

# Recomendación de mejora (dashboard ajustado)
- Integrar `IDActuacion` real o eliminar referencia; usar `CodActuacion`.
- Añadir panel normativo con fecha límite 31/12/2029 (RDC art 63.2) y marco FEDER.
- Mostrar relaciones con créditos, expedientes y lotes (inventario de 49 tablas).
- Añadir indicador de fuente (`G:` / NAS) y estado de conexión en portada.
- Mejorar visualización de alertas críticas (normativa SAS 46/2022, DO pendiente).


## Corrección por teoría confirmada (CodSegFact vs IdActuacion)
- Incongruencia 1 (L267) corregida por contexto: IdActuacion = clave interna; CodSegFact = identificador oficial.
- Recomendación paso 1: reemplazar `a.IDActuacion` por `CodSegFact` (o eliminar si el endpoint no lo devuelve aún; requiere actualizar `app.py` o usar `CodActuacion`).
