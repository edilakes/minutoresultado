# Resumen de la normativa (`F:\EDG\Normativa`)

> Fase 3 del plan. Resumen de los 7 PDF de normativa, orientado a entender los datos de Access y a diseñar la nueva app.
> Texto extraído con `python -m herramientas.extraer_normativa` a `datos/normativa_txt/` (local, fuera de git).

## 0. Cobertura de la lectura (qué he leído y qué no)

La normativa suma unas 1.100 páginas. **No la he leído entera**: he leído lo que afecta a las medidas del proyecto. Lo que no figura aquí está sin revisar.

| Documento | Páginas | Leído | Sin leer |
|---|---|---|---|
| Reglamento (UE) 2021/1060 (RDC) | 548 | Arts. 49, 63, 64 (parcial), 65, 73, 74, 82, 105–109; Anexo XVII (campos 1–12) | El resto, incluidos los Anexos VII y XVII casi completos |
| Programa FEDER Andalucía 21-27 | 248 | OE RSO2.1 y RSO2.2 (tipos de acción y cuadros de importes) | Gobernanza, condiciones favorecedoras, resto de prioridades |
| Manual de indicadores 21-27 | 169 | Fichas RCO19, RCO22, RCR26, RCR29, RCR31 | Resto de indicadores |
| Instrucción SAS 46/2022 | 37 | Instrucciones 1ª–9ª, índice de anexos y parte del Anexo III | Contenido de los anexos I–XIII salvo el fragmento citado |
| Reglamento (UE) 2021/1058 (FEDER) | 34 | Índice y art. 4 (inicio) | Arts. 3, 5–8 en detalle |
| Reglamento (UE, Euratom) 2020/2093 (MFP) | 12 | Arts. 1–3 | Resto |
| Recomendación (UE) 2019/786 | 46 | Apartado 2.5.2 (bases de datos de certificados) y búsquedas puntuales | Resto |

## 1. Cómo encaja cada documento

### 1.1 Marco financiero (contexto)
- **Reglamento 2020/2093 (MFP 2021-2027):** fija los límites de gasto anuales de la UE. Es solo marco; **no impone reglas a los datos de la app**.
- **Reglamento 2021/1058 (FEDER):** reglamento específico del fondo (objetivos específicos, concentración temática, indicadores, exclusiones). Es el marco de los OE `RSO2.1` y `RSO2.2`.

### 1.2 Reglamento 2021/1060 (RDC): reglas que afectan al seguimiento
| Artículo | Regla | Implicación para la app |
|---|---|---|
| 63.2 | El gasto es elegible si se realiza y paga entre el 1/1/2021 (o la fecha de presentación del programa) y el **31/12/2029** | Fecha límite dura. Conviene un indicador de plazo restante y de riesgo por actuación |
| 63.6 | No se seleccionan operaciones **ya concluidas** antes de solicitar la financiación | Control de fechas: inicio/fin frente a fecha de selección |
| 64.1.c | El **IVA no es elegible**, salvo en operaciones de coste total < 5.000.000 € (IVA incl.) o con IVA no recuperable | Hay que saber si los importes de `ActuacionesT` son con o sin IVA y la suma por **operación** |
| 65 | **Durabilidad**: reembolso si en los **5 años** siguientes al pago final hay cese, cambio de propiedad con ventaja indebida o cambio sustancial | No se deben borrar ni sobrescribir datos de operaciones cerradas |
| 73 | Criterios de selección; la operación debe contribuir a los objetivos del programa y garantizar **protección climática** en infraestructuras con vida útil ≥ 5 años; el beneficiario recibe un documento con las condiciones de ayuda (plazo de ejecución, plan de financiación) | Posible origen de la «Climate proofing» de la medida 044 (`20250904_ClimateProofingMedida044`) |
| 74 | Verificaciones de gestión; pago al beneficiario en **80 días** desde la solicitud | Seguimiento de solicitudes de pago y plazos |
| 49.3 | **Lista pública de operaciones**, actualizada al menos cada **4 meses**, con código único, nombre, finalidad, fechas de inicio y fin, coste total, fondo, OE, % de cofinanciación, geolocalización y tipo de intervención | La app podría **generar esta lista** directamente |
| 82 | Conservar los documentos justificativos **5 años** desde el 31/12 del año del último pago | Política de retención y adjuntos |
| 105 | Desvinculación automática (regla n+3); lo abierto a 31/12/2029 se libera si no se presenta el paquete de fiabilidad | Riesgo financiero global |
| Anexo XVII | Lista de **datos que deben registrarse electrónicamente por operación** (beneficiario, descripción, fechas, importes, indicadores…) | Referencia para saber si el modelo de datos está completo |

### 1.3 Programa FEDER Andalucía 2021-2027
- Las tres medidas de `MedidasT` corresponden a códigos de intervención del Programa dentro de la **Prioridad P2A (Transición verde)**:

| Medida (Access) | Código | OE | Programa (importe total) | `MedidasT.Importe` |
|---|---|---|---|---|
| A421AA44SA | 044 Eficiencia energética en infraestructuras públicas | RSO2.1 | 79.460.688 € | 52.118.857,58 € |
| A421AA45SA | 045 Ídem, conforme a criterios de eficiencia energética | RSO2.1 | 138.507.500 € | 88.927.805,23 € |
| A421BA48SA | 048 Energía renovable: solar | RSO2.2 | 208.400.312 € | 115.953.333,18 € |

  Los importes de `MedidasT` son de un 56 % a un 66 % de los del Programa. **Hipótesis (por confirmar):** es la parte asignada al SAS.
- **RSO2.1, tipo de acción A:** renovación de infraestructuras y edificios públicos no residenciales. Incluye agua caliente, climatización, envolvente y otros sistemas. Se prioriza la renovación integral. Las líneas A–D **exigen auditoría energética previa**; los costes de auditoría, certificación y proyecto son financiables.
- **RSO2.2, tipo de acción A:** renovables en el ámbito público. Incluye solar, con almacenamiento y gestión por TIC/IoT como actuación integrada. También son financiables los costes de auditoría y proyecto.
