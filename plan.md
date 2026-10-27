# Plan: entender los datos de Access y diseñar la versión mejorada de "Minuto y Resultado"

> Objetivo: que el asistente comprenda a fondo los datos de actuaciones (tablas de Access, relaciones, significado de cada campo y reglas de negocio) para poder actuar como experto en la materia y co-diseñar con el usuario una versión mejorada de la app actual.

**Cómo usar este documento:** es la hoja de ruta viva del proyecto. Cada fase tiene casillas `[ ]` que se marcan como `[x]` al completarse. Los resultados de cada fase se guardan en `docs/` para que cualquier sesión futura parta del mismo contexto.

---

## 1. Punto de partida (comprobado)

| Elemento | Estado |
|---|---|
| Base Access (`Database_be.accdb`) | No está en el workspace, pero **es accesible desde este equipo** por la ruta del NAS (`Test-Path` → `True`). |
| Driver ODBC | `Microsoft Access Driver (*.mdb, *.accdb)` de **64 bits**; Python también es de **64 bits**. Coinciden. |
| Librerías Python disponibles | `pyodbc 5.3`, `pandas 2.3`, `openpyxl 3.1`, `Flask 3.1`, `flask-cors 6.0`, `PyPDF2 3.0`. No hace falta instalar nada para empezar. |
| App actual | Flask (`app.py`) + `portada.html`. Solo usa la tabla `ActuacionesT`. Lógica: `EstadoActuacion` → macroestado → responsable → alerta → progreso (`N × 10`). |
| Lo que **no** se sabe aún | Qué otras tablas existen, cómo se relacionan, qué significan los códigos (`EstadoActuacion`, `Cubierta`, `N`, `FE04`, `Operacion`, `Medida`…) ni los procesos reales que hay detrás. |

La app actual muestra solo una parte de los datos. Primero se hace inventario de lo que hay y después se decide qué mejorar.

## 2. Principios de trabajo

- **No se trabaja sobre la base de producción en el NAS.** Se usa una copia local o una conexión de solo lectura (`ReadOnly=1`), para no bloquear el `.accdb` a otros usuarios ni arriesgar los datos.
- **El conocimiento se guarda en archivos del repositorio** (diccionario de datos, glosario, registro de decisiones), no en la memoria de la conversación.
- **Ciclo de cada tabla:** el asistente muestra → el usuario explica → el asistente documenta.
- **Los datos corporativos no se suben a git** (la copia local va al `.gitignore`).

## 3. Estructura de carpetas propuesta

```
MinutoResultado/
├─ plan.md              # este documento
├─ herramientas/        # scripts de inventario, perfilado y consultas rápidas
├─ datos/               # copia local de Access (ignorada por git)
├─ docs/
│  ├─ datos/            # 00_inventario.md, ActuacionesT.md, ...
│  ├─ contexto/         # PDF / Excel / capturas aportados por el usuario
│  ├─ GLOSARIO.md
│  ├─ MODELO_DOMINIO.md
│  ├─ REGLAS_NEGOCIO.md
│  └─ DECISIONES.md     # registro de decisiones de diseño
└─ (app actual: app.py, portada.html, README.md, ...)
```

## 4. Fases

### Fase 0 – Preparar el acceso a los datos (una sola vez)
- [x] Crear `herramientas/acceso.py` con `conectar(readonly=True)` y las rutas configurables por variable de entorno (`MR_DB_BE`, `MR_DB_FE`, `MR_NORMATIVA`).
- [x] ~~Copia local de la base~~ **Descartada por decisión del usuario:** se lee el NAS directamente en solo lectura (`ReadOnly=1`). `datos/` se añadió al `.gitignore` para los JSON de metadatos generados.
- [x] Comprobada la conexión. `MSysObjects`, `MSysRelationships` y `MSysQueries` **no son legibles** por ODBC (sin permiso). Alternativas usadas: **DAO** (`herramientas/extraer_metadatos.ps1`, abre en solo lectura y modo compartido) para campos, índices, SQL de consultas y lista de formularios/informes; y la tabla propia `RelacionesAccessT` del backend para las relaciones.

### Fase 1 – Inventario automático (lo hace el asistente)
Un script genera `docs/datos/00_inventario.md` con:
Resultado: `docs/datos/00_inventario.md` (backend) y `docs/datos/01_frontend.md` (frontend). Se regeneran con `python -m herramientas.inventario`.
- [x] Lista de **tablas y consultas guardadas**, distinguiendo datos, catálogos, relaciones N:M, marco FEDER y revisiones puntuales.
- [x] Por tabla: nº de filas, columnas, tipos, clave primaria y **relaciones declaradas** (57 en `RelacionesAccessT`, sin integridad referencial).
- [x] Por columna: % de nulos, nº de valores distintos, mín/máx y los 6 valores más frecuentes, más la descripción que ya tenga en Access (90 campos la tienen).
- [~] **SQL de las consultas guardadas:** extraído a `datos/metadatos_fe.json` (180 consultas, local), pero **todavía sin analizar**. Es el siguiente paso de lectura.
- [ ] Detección de **claves foráneas implícitas** (columnas con el mismo nombre o valores coincidentes aunque Access no declare la relación).
- [x] **Diagrama ER en Mermaid** a partir de las relaciones declaradas.

### Fase 2 – Exploración guiada, tabla por tabla (interactiva)
Se empieza por `ActuacionesT` y se sigue por orden de importancia. Para cada tabla:
- [ ] El asistente muestra la estructura, **10–20 filas representativas** (incluidos extremos y nulos) y los valores frecuentes de las columnas categóricas.
- [ ] El asistente plantea preguntas concretas. Ejemplos:
  - ¿Qué significan los valores 1–8 de `EstadoActuacion`?
  - ¿Qué es `Cubierta` en términos de negocio?
  - ¿Por qué `N × 10` es el progreso?
  - ¿Qué diferencia hay entre `Medida` y `MedidaUnificada`?
  - ¿Qué son `FE04` y `Operacion`?
- [ ] Las respuestas se guardan en `docs/datos/<tabla>.md` con tres bloques: **significado**, **reglas** y **dudas abiertas**.
- [ ] Se registran las **anomalías** (duplicados, estados incoherentes, fechas imposibles, textos sucios, columnas sin uso) y el usuario indica cuáles son errores y cuáles son normales.
- [ ] **Vistas transversales** cuando haga falta: una actuación completa de principio a fin, resúmenes por provincia u órgano gestor, actuaciones en un estado concreto.

Seguimiento por tabla (se completa tras la Fase 1):

| Tabla | Mostrada | Explicada por el usuario | Documentada |
|---|---|---|---|
| `ActuacionesT` | [ ] | [ ] | [ ] |
| _(resto, pendiente de inventario)_ | | | |

### Fase 3 – Documentos de contexto aportados por el usuario
Para completar lo que los datos no dicen. El asistente puede leer:
- [ ] **PDF** (con PyPDF2): normativa, instrucciones, convocatoria de fondos europeos, memorias.
- [ ] **Excel / CSV** (openpyxl, pandas): informes que hoy se hacen a mano, listados que se piden con frecuencia.
- [ ] **Word y texto**: procedimientos internos, correos relevantes, actas.
- [ ] **Capturas de pantalla** de formularios e informes de Access: lo más útil para ver cómo trabaja hoy la gente.
- [ ] **Frontend de Access** (si existe un `.accdb` con formularios, además del `_be`): se pueden extraer nombres de formularios, informes y macros. El VBA no se lee por ODBC, pero el usuario puede exportarlo.

Todo se guarda en `docs/contexto/` y se resume en `docs/GLOSARIO.md`.

### Fase 4 – Modelo de dominio y reglas de negocio
- [ ] `docs/MODELO_DOMINIO.md`: entidades (actuación, centro, órgano gestor, medida, operación, DO, proyecto, contrato, empresa…), su ciclo de vida y quién es responsable en cada etapa.
- [ ] `docs/REGLAS_NEGOCIO.md`: sustituto correcto de lo que hoy está fijo en `app.py`. Incluye máquina de estados, alertas, cálculo de progreso e indicadores económicos.
- [ ] **Validación de las reglas contra los datos reales.** Ejemplo: «¿cuántas actuaciones en estado 6 tienen `Cubierta = False`?» y comprobar que coincide con lo que espera el usuario.

### Fase 5 – Prueba de comprensión
Antes de diseñar, el asistente se examina con el usuario:
- [ ] Explica con sus palabras el proceso completo y el usuario lo corrige.
- [ ] Responde **10–15 preguntas de negocio** planteadas por el usuario, con consultas reales. Ejemplo: «¿qué actuaciones de Málaga llevan más tiempo bloqueadas esperando DO?».
- [ ] Lista sus **dudas pendientes** y lo que los datos no permiten responder.

Criterio de paso: el usuario confirma que el asistente ya puede ayudarle como experto en la materia.

### Fase 6 – Diseño de la versión mejorada (co-diseño)
- [ ] **Levantamiento de necesidades:** quién usa la app (gestores, dirección, contratación), qué decisiones toma y qué preguntas hace cada semana.
- [ ] **Backlog priorizado**, partiendo de los problemas ya recogidos en `README.md` (sección «Problemas conocidos») más los que surjan del análisis: seguridad de `/db_query` y `/db_data`, `request` sin importar, paginación sin `offset`, etc.
- [ ] **Decisión de arquitectura** (se registra en `docs/DECISIONES.md`):

  | Opción | Descripción | Ventajas | Inconvenientes |
  |---|---|---|---|
  | A. Evolución incremental | Mantener Flask + Access; mejorar API y HTML | Rápida, bajo riesgo | Access sigue limitando concurrencia y crecimiento |
  | B. Capa de datos intermedia | ETL periódico de Access a SQLite/DuckDB; la app lee de ahí | Evita bloqueos, permite históricos y análisis | Hay que mantener la sincronización |
  | C. Migración completa | Pasar a una base de datos de servidor | Es la más sólida | Exige coordinación con TI y con quien edita Access hoy |

- [ ] **Maquetas** de pantallas (dashboard, ficha de actuación, vistas por responsable, exportación a Excel) validadas antes de programar.
- [ ] **Implementación por iteraciones pequeñas con tests**, sobre la copia de datos.

## 5. Cómo interactuamos en la práctica

- El usuario pide cosas como «muéstrame las actuaciones de Cádiz en licitación» o «¿cuántas tienen alerta?». El asistente ejecuta consultas de **solo lectura** y muestra tablas.
- El usuario corrige («ese estado 5 en realidad significa…») y el asistente actualiza el glosario en el momento.
- Cada sesión empieza leyendo `docs/` y este `plan.md`, de modo que no se pierde contexto.

## 6. Consideraciones y riesgos

- **Datos sensibles o corporativos:** la copia local queda fuera de git. Revisar si hay datos personales (nombres de técnicos, empresas) antes de compartir nada fuera del equipo.
- **Seguridad de la app actual:** `/db_query`, `/db_data`, `/db_tables` y `/db_schema` están abiertos a cualquiera de la red y con CORS abierto. Es prioridad en la Fase 6.
- **Límites de Access:** `MSysObjects` y `MSysRelationships` pueden estar restringidos por permisos. Plan B: metadatos de `pyodbc` e inferencia por contenido.
- **Bloqueos:** aun en solo lectura, abrir el `.accdb` en red crea un `.laccdb` temporal. Por eso se prefiere la copia local.
- **Posible desfase entre copia y producción:** definir cada cuánto se refresca la copia y dejar constancia de la fecha de cada extracción en `docs/datos/00_inventario.md`.

## 7. Decisiones y preguntas abiertas

Pendientes de respuesta del usuario; se irán trasladando a `docs/DECISIONES.md`.

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Se trabaja sobre una **copia local** (más seguro) o directamente sobre el NAS en solo lectura? | **Directamente sobre el NAS en solo lectura** (`ReadOnly=1`). No se hace copia local. |
| 2 | ¿Existe un **frontend de Access** (formularios e informes) además de `Database_be.accdb`? | **Sí:** `C:\Users\lagosedgar20p\Desktop\Database_fe.accdb` (~29 MB). |
| 3 | ¿Qué **documentos** hay a mano para empezar (normativa, procedimiento, informes en Excel)? | **Normativa** en `F:\EDG\Normativa` (7 PDF). Procedimientos e informes: _pendiente_. |
| 4 | ¿Cuáles son las **3–5 preguntas de negocio** que hoy cuesta más responder con la app? | _pendiente_ |
| 5 | ¿Quién va a **usar** la nueva versión y qué le falta más hoy (alertas, histórico, edición de datos, informes…)? | _pendiente_ |

## 8. Hallazgos iniciales (a confirmar con el usuario)

**Dimensión de lo que hay**
- **Backend:** 49 tablas (358 actuaciones, 95 operaciones, 46 expedientes, 485 lotes, 717 contratos, 1.751 créditos, 712 apuntes de bitácora…). **Frontend:** 180 consultas, 57 formularios, 54 informes, 2 módulos VBA y 2 macros.
- **Normativa disponible** (`F:\EDG\Normativa`, 7 PDF): Manual de indicadores FEDER 21-27, Programa FEDER Andalucía 21-27, Reglamentos UE 2021/1058, 2021/1060 y 2020/2093, Recomendación UE 2019/786 e Instrucción 46/2022 del SAS. Aún sin leer.

**Discrepancias entre la app actual y los datos reales**
1. **`EstadoActuacion` va de 8 a 18**, no de 1 a 8. Los valores 8–16 son fases del expediente: «01 PRY IPA favorable» (8) → «09 OBRA cert fin de obra» (16). Los valores 17 «Decae», 18 «Previa», 19 y 20 son «En evaluación». Los valores 1–7 son estados genéricos del marco FEDER. Con la regla actual (`≥ 8 → finalizada`) **las 358 actuaciones salen como "finalizada"**. Distribución real: 8 → 167, 9 → 121, 11 → 64, 14 → 2, 18 → 2, 10 → 1, 16 → 1.
2. **`Cubierta` parece ser un tipo de instalación** (fotovoltaica en cubierta frente a otras ubicaciones, junto a `Marquesina` e `Hospitalaria`), no «DO adjudicada» como supone el README. Valores: 301 verdaderos y 57 falsos. Las alertas actuales se basan en esa lectura, así que serían falsas alertas.
3. **`N`** vale 1 en 314 de 358 filas (rango 1–5). Con `N × 10`, el «progreso estimado» sería 10 % en casi todas. Probablemente `N` sea otra cosa, como el nº de ubicaciones o de unidades.
4. `Estado` vale 6 en las 358 filas (columna inútil) y `IdLote`, `Observaciones` y `Proy` están vacías o constantes. `Operacion` (texto) y `Oper` (entero) parecen duplicar la misma clave.
5. `ActuacionesT` no tiene clave primaria declarada (`IDActuacion` es único pero no figura como PK).
6. `Resp` solo tiene 2 valores (dos gestores), por lo que no representa a «Órgano gestor / DO / Contratación / Empresa».
7. Las 57 relaciones **no tienen integridad referencial**, así que pueden existir registros huérfanos.

**Hipótesis de dominio** (por confirmar): las actuaciones son instalaciones de **paneles fotovoltaicos (319) y eficiencia energética (39)** en centros sanitarios de Andalucía. Se financian con FEDER 21-27 a través de las medidas **A421AA44SA, A421AA45SA y A421BA48SA** (la 48 concentra 298 de 358). Cada actuación pasa por una fase de **proyecto** (redacción y dirección de obra) y otra de **obra**, agrupadas en lotes y expedientes de contratación.

## 9. Siguiente paso

Arrancar la **Fase 2 con `ActuacionesT`**. Presentar filas representativas y preguntar por las dudas del apartado 8, empezando por el significado real de `EstadoActuacion`, `Cubierta`, `N` y `Resp`. En paralelo: leer las 180 consultas del frontend y resumir la normativa.

## 10. Registro de avance

| Fecha | Hito |
|---|---|
| 2026-10-27 | Plan creado y aprobado por el usuario. |
| 2026-10-27 | Respondidas las preguntas 1–3 de la sección 7 (NAS solo lectura, frontend y normativa localizados). |
| 2026-10-27 | **Fase 0 completada:** `herramientas/acceso.py`, `herramientas/extraer_metadatos.ps1`, `datos/` en `.gitignore`. |
| 2026-10-27 | **Fase 1 completada** (salvo SQL de consultas y FK implícitas): `herramientas/inventario.py`, `docs/datos/00_inventario.md`, `docs/datos/01_frontend.md`. |

