# Minuto y Resultado – Actuaciones

Panel web de seguimiento del estado de las **actuaciones en centros sanitarios** (Fondos Europeos, SAS – Junta de Andalucía).

Consta de un backend Flask que lee una base de datos Microsoft Access alojada en un NAS corporativo y de una página HTML estática (`portada.html`) que muestra los datos en forma de KPIs, filtros y tarjetas.

---

## Funcionalidades

- **KPIs**: total de actuaciones, en curso, con alerta y finalizadas (se recalculan según los filtros activos).
- **Filtros**: provincia, órgano gestor, macroestado y búsqueda de texto libre (código de actuación, centro, provincia, órgano gestor, medida, FE04, operación).
- **Tarjetas** por actuación, con estado, responsable actual, progreso estimado y alertas. Cada macroestado tiene su color, y las alertas críticas se marcan en rojo.
- **Sin instalación para el usuario final**: basta con abrir `portada.html` en el navegador.

## Arquitectura

```
┌────────────────────┐   HTTP/JSON    ┌───────────────────────┐   ODBC    ┌────────────────────────┐
│ Navegador          │ ─────────────▶ │ Servidor Flask        │ ────────▶ │ Database_be.accdb      │
│ (portada.html)     │  puerto 5000   │ (app.py, SEP00000C1Q7)│           │ (NAS corporativo)      │
└────────────────────┘                └───────────────────────┘           └────────────────────────┘
```

Los usuarios **no necesitan acceso al NAS**: solo el servidor accede a la base de datos.

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `app.py` | Backend Flask (API JSON + lógica de macroestado, responsable y alertas). |
| `portada.html` | Frontend estático (HTML + CSS + JavaScript, sin dependencias). |
| `LEEME_USUARIOS.txt` | Instrucciones de uso para usuarios. |
| `LEEME_ADMIN.txt` | Requisitos del servidor para administradores. |
| `CHECKLIST.txt` | Checklist de despliegue. |
| `README.md` | Este documento. |

## Requisitos

**Servidor**
- Windows con Python 3.
- Paquetes Python: `flask`, `flask-cors`, `pyodbc`.
- Driver ODBC **Microsoft Access Database Engine** (`Microsoft Access Driver (*.mdb, *.accdb)`). Su arquitectura (32 o 64 bits) debe coincidir con la de Python.
- Permisos de lectura sobre la carpeta del NAS donde está `Database_be.accdb`.
- Puerto **5000** abierto en la red SAS.

**Cliente**
- Un navegador moderno (Chrome, Edge o Firefox) y conexión a la red corporativa SAS.

## Instalación y ejecución

```powershell
pip install flask flask-cors pyodbc
python app.py
```

El servidor escucha en `0.0.0.0:5000`. Para comprobarlo, abre:

```
http://SEP00000C1Q7.DMSAS.sda.sas.junta-andalucia.es:5000/actuaciones_resumen
```

Debe devolver un JSON con la lista de actuaciones.

## Configuración

Hoy los valores están fijos en el código:

| Qué | Dónde | Valor actual |
|---|---|---|
| Ruta de la base Access | `conectar()` en `app.py` (`DB_PATH`) | `\\nas.cifs.cti-sevilla.sas.junta-andalucia.es\SSCC-CONSTITUCION-1\SSCC\Sb-ServiciosGestionCentros\FondosEuropeos\Database_be.accdb` |
| URL del backend | `fetch(...)` en `portada.html` | `http://SEP00000C1Q7.DMSAS.sda.sas.junta-andalucia.es:5000/actuaciones_resumen` |
| Host y puerto | `app.run(...)` en `app.py` | `0.0.0.0:5000` |

Si cambia el servidor o el NAS, hay que actualizar estos valores.

## API

Todos los endpoints son `GET` y devuelven JSON.

| Endpoint | Descripción |
|---|---|
| `/actuaciones_resumen` | Lista de actuaciones de la tabla `ActuacionesT` con macroestado, responsable, alerta y progreso. Es el que usa `portada.html`. |
| `/db_tables` | Lista de tablas de la base de datos. |
| `/db_schema/<tabla>` | Columnas, tipos y nulabilidad de una tabla. |
| `/db_data/<tabla>?page=1&limit=100` | Datos de una tabla (máximo 1000 filas por llamada). |
| `/db_query?sql=SELECT ...` | Ejecuta una consulta personalizada (solo debe empezar por `SELECT`). |

Ejemplo de elemento de `/actuaciones_resumen`:

```json
{
  "CodActuacion": "XX-000",
  "CentroSanitario": "Hospital ...",
  "Provincia": "Sevilla",
  "OrganoGestor": "...",
  "Medida": "...",
  "EstadoActuacion": 6,
  "Macroestado": "licitacion-obra",
  "ResponsableActual": "Contratación",
  "Alerta": "⚠️ DO pendiente (crítica)",
  "ProgresoEstimado": 60,
  "ImporteTotal": 123456.78,
  "FE04": "...",
  "Operacion": "...",
  "IDActuacion": 1
}
```

## Reglas de negocio

### Macroestado y responsable

Se calculan a partir del campo `EstadoActuacion`:

| EstadoActuacion | Macroestado | Responsable actual |
|---|---|---|
| < 3 | `pendiente` | Órgano gestor |
| 3 | `licitacion` | Proyecto |
| 4 | `redaccion` | Proyecto |
| 5 | `proyecto` | DO |
| 6 | `licitacion-obra` | Contratación |
| 7 | `ejecucion` | Empresa |
| ≥ 8 | `finalizada` | — |

### Alertas

Se disparan cuando el campo `Cubierta` es falso (DO no adjudicada):

| Macroestado | Alerta |
|---|---|
| `licitacion-obra` | ⚠️ DO pendiente (crítica) |
| `proyecto` | ⚠️ Proyecto recibido sin DO adjudicada |

### Progreso estimado

`ProgresoEstimado = N × 10` (%), donde `N` es un campo de la tabla `ActuacionesT`.

## Uso (usuarios)

1. Abrir `portada.html` con doble clic.
2. Esperar a que carguen los datos desde el servidor corporativo.
3. Filtrar por provincia, órgano gestor, macroestado o texto.

Si no carga, comprueba que estás en la red corporativa SAS y que el servidor es accesible. Más detalle en `LEEME_USUARIOS.txt`.

## Despliegue (administradores)

- Requisitos del servidor: `LEEME_ADMIN.txt`.
- Lista de verificación: `CHECKLIST.txt`.
- Para actualizar la aplicación basta con reemplazar `portada.html`; no hay que tocar los equipos cliente.

## Problemas conocidos y mejoras recomendadas

Detectados en la revisión del código (no corregidos todavía):

**Errores**
1. `app.py` no importa `request` de Flask (`from flask import Flask, jsonify, request`). Por eso `/db_data` y `/db_query` fallan con `NameError`.
2. `app.run(...)` se ejecuta a nivel de módulo. Conviene envolverlo en `if __name__ == "__main__":`.
3. `/db_data` calcula `offset` pero no lo aplica, así que `page` no cambia el resultado: siempre devuelve la primera página.
4. Si `EstadoActuacion` es `NULL`, `macroestado()` lanza `TypeError` (comparación con `None`). Usar `a.get("EstadoActuacion") or 0`.

**Seguridad**
5. `/db_query`, `/db_tables`, `/db_schema` y `/db_data` exponen toda la base sin autenticación, y CORS está abierto a cualquier origen. Se recomienda eliminarlos o protegerlos, o al menos limitarlos a una lista blanca de tablas.
6. Los nombres de tabla se interpolan directamente en el SQL (`[{table_name}]`), y `/db_query` solo comprueba el prefijo `SELECT`.
7. `portada.html` inserta datos en `innerHTML` sin escapar. Conviene sanear los textos para evitar XSS.

**Mantenimiento**
8. Externalizar la ruta del NAS y la URL del backend a variables de entorno o a un archivo de configuración.
9. Añadir un `requirements.txt`.
10. Unificar el nombre del servidor en `CHECKLIST.txt` (host corto) con el resto de documentos (FQDN).
11. Usar un servidor WSGI de producción (p. ej. `waitress`) en lugar del servidor de desarrollo de Flask.

