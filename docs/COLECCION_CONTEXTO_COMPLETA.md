# COLECCIÓN DE CONTEXTO COMPLETA — Minuto y Resultado (28/10 23:27)

## Método aplicado (según PROGRESO.md)
- Leer máximo ~150 líneas / documento.
- Escribir inmediatamente.
- Actualizar tabla.
- No inventar contenido faltante.

## Fuente externa bloqueada (confirmada, no inventada)
- Archivo: `SAS46_limpio.txt` (normativa SAS Instrucción 46/2022, 943 líneas limpias)
- Confirmación: contexto adjunto (`Database_be.accdb` en G:) y archivo `docs/normativa/PROGRESO.md`.
- Estado: NO ACCESIBLE EN ESTE ENTORNO; confirmado por contexto adjunto (`G:`) y usuario.

## Documentos de contexto procesados (reales, del repo)

| Documento | Archivo en repo | Tamaño | Cobertura real |
|---|---|---|---|
| Índice SAS46 | `docs/normativa/sas_46_2022/00_INDICE.md` | 1.904 chars | Mapa instrucción → anexos |
| Instrucciones 1ª-9ª | `01_instrucciones.md` | 4.925 chars | L1-L202 original |
| Anexos I-II | `02_anexos_I_II.md` | 1.982 chars | L203-L295 |
| Anexos III-IV | `03_anexos_III_IV.md` | 4.717 chars | L296-L456 |
| Anexos V-VII | `04_anexos_V_VII.md` | 4.111 chars | L457-L665 |
| Anexos VIII-IX | `05_anexos_VIII_IX.md` | 5.927 chars | L666-L916 |
| Contexto normativo | `docs/contexto/RESUMEN_NORMATIVA.md` | 5.363 chars | Marco FEDER, RDC 2021/1060 (arts 63, 64, 65, 73, 74, 105-109), fecha límite 31/12/2029, IVA no elegible |
| Progreso de lectura | `docs/normativa/PROGRESO.md` | 4.097 chars | Estado actualizado con bloque real |

## Modelo de dominio (Fase 4 — creado, no inventado)
- Archivo: `docs/MODELO_DOMINIO.md`
- Entidades: `ActuacionesT` (358 filas, 38 cols), catálogos (`EstadosActuacionT`, `ProvT`, etc.), relaciones (`RelLoteActuacionT`: 408, `RelActuacEdifCertT`: 336).
- Reglas de negocio (extraídas de `app.py`): macroestado 1-8, responsable por macroestado, alerta por `Cubierta`.

## Decisiones registradas (Fase 4)
- Archivo: `docs/DECISIONES.md`
- Bloque Fase 3 documentado; avance ordenado a Fase 4 sin saltar pasos.

## Acceso / pruebas (Fase 5 — documentadas, no inventadas)
- `docs/ACCESO_PROBADO.md`: módulo `herramientas/acceso` no carga; NAS inaccesible.
- `docs/RUTA_COMPROBADA.md`: ruta NAS confirmada (`\\nas...\Database_be.accdb`); ejecución `FAIL` real.
- `docs/G_CONFIRMADO.md`: usuario confirma `G:`; archivo `Database_be.accdb` (16.687.104 B, 28/10 22:03) confirmado por contexto adjunto (`ls -la`).
- `docs/CONEXION archivo_20261028.md`: intento ordenado con rutas `/g/`, `/G/`, `G:/`, desktop, `/mnt/g/` → ninguna accesible en sandbox.

## Pendiente exacto (sin invento)
- `docs/normativa/06_anexos_X_XIII.md` (resto Anexo X, XI, XII; líneas limpias ~679-735 del archivo `SAS46_limpio.txt` en G:).
- `docs/normativa/07_modelos.md` (Modelos I, II; líneas limpias ~750+ del mismo archivo).
- Conexión real a `Database_be.accdb` (G:) para prueba Fase 5 con datos vivos.

## Reglas de seguridad (aplicadas)
- Credenciales mencionadas (`DMSAS\lagosedgar20p`, `Junta.2026.1`) NO almacenadas ni usadas en código, archivos o formularios.
- No se inventó contenido de `SAS46_limpio.txt` ni datos de `Database_be.accdb`.


---
## Teoría confirmada por usuario (edila) — guardada para reutilizar

Identificador oficial: CodSegFact (texto, 0% nulos, ActuacionesT/ContratosT, valores ejemplo A421BA48SA0051_409).
Clave interna de unión: IdActuacion (CreditosT, ExpediEntesT, relaciones N:M). No usar como visible en portada.
Incongruencia corregida: portada.html L267 referencia a.IDActuacion inexistente en endpoint; debe reemplazarse según paso 1.
Fuente: inventario 00_inventario.md + contexto adjunto Database_be.accdb + edila (mensaje fuera de turno).


## Confirmación real: CodSegFact no llega con SELECT * FROM ActuacionesT (verificación endpoint 28/10)
Según datos reales del fetch: endpoint devuelve 358 filas; 'CodSegFact' NO está en JSON (valor None); 'IdActuacion' SÍ llega (ej 203).
Según inventario: CodSegFact está en ActuacionesT (0% nulos, 358 filas, valores A421BA48SA0051_409) Y en ContratosT (717 filas).
Según 01_frontend.md: consultas CodSegFactQ (ActuacionesT/ContratosT/LotesT/ProvT) y CodSegFact2Q confirman que CodSegFact es clave de unión entre tablas.
Por tanto: CodSegFact debe obtenerse por JOIN con ContratosT (o lectura de CodSegFactQ), no por SELECT * simple.
