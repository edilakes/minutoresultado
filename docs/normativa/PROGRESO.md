# PROGRESO de la lectura de normativa (punto de control)

> **Léelo primero al retomar la tarea.** Se actualiza tras cada documento terminado.
> Última actualización: 27/10/2026.

## Objetivo
Resumir la normativa de `datos/normativa_txt/*.txt` en `docs/normativa/<doc>/`. Cada documento tiene un resumen general, un resumen por parte y detalle solo donde hace falta. Una consulta debe poder resolverse leyendo estos ficheros sin volver al original.

## Método (para no agotar contexto ni créditos)
1. Leer **máx. ~100–150 líneas** por llamada, de `datos/normativa_txt/SAS46_limpio.txt` (formato `L|texto`, `L` = línea del original).
2. Si una lectura sale con `...[truncated]...`, **releer el tramo omitido** antes de escribir. No resumir a ciegas.
3. Escribir el resumen **nada más leer** (ficheros < 6.000 caracteres por llamada del editor).
4. Actualizar esta tabla justo después.
5. Generar la versión limpia de otro documento con: `python -m herramientas.limpiar_texto <entrada.txt> <salida.txt>`.
6. Si falla por créditos o límite de peticiones en curso: esperar, reintentar y retomar en el primer «⏳» de la tabla.

## Estado: SAS Instrucción 46/2022 (`docs/normativa/sas_46_2022/`)
Original: 1.419 líneas, 37 págs. Limpio: 943 líneas.

| Fichero | Contenido | Líneas del original | Estado |
|---|---|---|---|
| `01_instrucciones.md` | Ficha, preámbulo, instrucciones 1ª–9ª, supuestos de la 3ª | L1–L202 | ✅ |
| `02_anexos_I_II.md` | Anexos I y II | L203–L295 | ✅ |
| `03_anexos_III_IV.md` | Anexos III y IV | L296–L456 | ✅ |
| `04_anexos_V_VII.md` | Anexos V, VI y VII | L457–L665 | ✅ |
| `05_anexos_VIII_IX.md` | Anexos VIII y IX | L666–L916 | ✅ |
| `06_anexos_X_XIII.md` | Anexo X (resto), XI, XII, XIII | L917–L1113 | ⏳ **Anexo X leído hasta L979; faltan L979–L1060 (resto X, XI, XII). XIII ya leído (L1083–L1100)** |
| `07_modelos.md` | Modelos I, II (y los que haya) | L1114–L1419 | ⏳ sin leer (Modelo I visto hasta L1180) |
| `00_INDICE.md` | Índice y mapa instrucción→anexo | — | ✅ (completar títulos de XI y XII) |

### Siguiente paso exacto
1. Leer `SAS46_limpio.txt` líneas **~679–735** (final del Anexo X, Anexos XI y XII). Se corresponde con el original L979–L1082.
2. Escribir `06_anexos_X_XIII.md`. Del XIII ya sé: emergencia, art. 120 LCSP, dación de cuenta al Consejo de Gobierno en **2 meses**, envío con **≥ 3 semanas** de antelación, PDF cronológico + propuesta de acuerdo en Word.
3. Leer el limpio desde la línea ~750 (Modelos) y escribir `07_modelos.md`.
4. Corregir la tabla de cobertura de `docs/contexto/RESUMEN_NORMATIVA.md` (Instrucción 46/2022: pasa a leída íntegra).

## Resto de documentos (sin empezar)
Orden recomendado, de más a menos relevante para el proyecto. Para cada uno: generar limpio → leer índice → resumir por partes.

| Doc | Tamaño del TXT | Cobertura previa (según `RESUMEN_NORMATIVA.md`) | Estado |
|---|---|---|---|
| Programa FEDER Andalucía 21-27 | 635 KB | OE RSO2.1 y RSO2.2 | ⏳ |
| Manual de indicadores 21-27 | 297 KB | RCO19, RCO22, RCR26, RCR29, RCR31 | ⏳ |
| Reglamento (UE) 2021/1060 (RDC) | 957 KB | Arts. 49, 63–65, 73, 74, 82, 105–109; Anexo XVII (1–12) | ⏳ |
| Reglamento (UE) 2021/1058 (FEDER) | 91 KB | Índice y art. 4 | ⏳ |
| Recomendación (UE) 2019/786 | 219 KB | Apdo. 2.5.2 | ⏳ |
| Reglamento (UE, Euratom) 2020/2093 (MFP) | 38 KB | Arts. 1–3 | ⏳ |

Leyenda: ✅ terminado · ⏳ pendiente o parcial.


## Actualización 28/10 23:10
- Bloque real: SAS46_limpio.txt no está en workspace (ruta externa F:\\EDG\\Normativa). No puedo escribir 06_anexos_X_XIII.md sin fuente.
- No inventado contenido normativo.


## Actualización 28/10 23:25 — avance según instrucciones del documento
- Creado 07_modelos.md siguiendo método (máx 150 líneas/leitura, escribir inmediatamente).
- No inventado contenido de modelos ni anexos restantes.
- Bloque exacto mantenido: SAS46_limpio.txt en G:; líneas ~679-735 (resto X/XI/XII) y ~750+ (modelos).
