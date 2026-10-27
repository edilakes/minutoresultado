# Inventario del frontend Access (`Database_fe.accdb`)

- Generado: **2026-10-27 17:32** · Origen: `C:\Users\lagosedgar20p\Desktop\Database_fe.accdb`
- Tablas vinculadas al backend: **49**
- Consultas: **180** · Formularios: **57** · Informes: **54** · Módulos VBA: **2** · Macros: **2**
- El SQL completo de cada consulta está en `datos/metadatos_fe.json` (local, fuera de git).

## Formularios

`_ContinuousF`, `_SingleF`, `20250630_RevDocumF`, `20250912_ClimateProofing044F`, `ActuacionesF`, `ActuacionExpedientesGeneralSF`, `ActualizacionDiariaExpedientesF`, `BitacoraF`, `BitacoraFichaF`, `BitacoraListaF`, `CargarEstadoF`, `CEE2F`, `CEEF`, `ContratosF`, `Creditos2F`, `Creditos3F`, `CreditosF`, `DatosActuacionesF`, `DosColumnasFichasEtiquetasArriba`, `ExpedienteActuacionesSF`, `ExpedienteActualizarEstadoF`, `Expedientes_v0F`, `Expedientes_v1F`, `ExpedientesF`, `ExpedientesListaF`, `ExpedientesT`, `FaseExpedientesF`, `FasesExpedienteSF`, `FlujoCargarFechas_ExpedienteF`, `FlujoCargarFechas_lotesF`, `IndicadoresAnualizados`, `IndicadoresAnualizadosConsultaGeneralF`, `IPAExpedientesF`, `IPAExpedientesSF`, `Lotes2F`, `Lotes2SF`, `LotesF`, `LotesSF`, `MAEsF`, `MedidasF`, `MenuF`, `MenuPrincipalF`, `NuevoExpedienteF`, `Operaciones2F`, `OperacionesF`, `ProyectosF`, `ProyectosQ`, `RCR26F`, `RCR29F`, `RelActuacCertF`, `RelActuacDNSHF`, `RelActuacEdifCertF`, `RelLoteActuacionF`, `TempModoInstF`, `TextosF`, `UsuariosF`, `VincularLoteActuacion`

## Informes

`20250730_RevFVPliegosAxarquia`, `20250904_ClimateProffingMedida044R`, `20250910ActuacionesR`, `20250915ActuacionesR`, `20261016_ImportesMedida44`, `Actuaciones2R`, `Actuaciones3R`, `ActuacionesCreditosR`, `ActuacionesR`, `ActuacionesT`, `AgrupacionExpedientes`, `BitacoraR`, `Copia de SumatoriosActuaciones`, `Creditos5Q`, `CreditosFE04R`, `CreditosRefQ`, `CuadroImportesR`, `DesgloseHospitalariaR`, `EdificiosQ`, `ExpedienteLotesSR`, `ExpedientesR`, `ExpedientesT`, `FE04R`, `GIRO_FE04_Edgar`, `IM_044R`, `IM_048R`, `ImportesExpedienteSR`, `InfJusitificaFE04P01R`, `InfJustFE04Tabla01R`, `InformeActuaciones`, `IPA_AnexoI`, `IPAComprobacionImportesR`, `IPAExpedientesT`, `IS_044R`, `LotesR`, `MAEs`, `MAEsImporte`, `MedidasR`, `ModoInstalacion`, `ObjetivosEspecificosR`, `OperacionesR`, `ProyConSupervisionR`, `RC019AnualizadosUnidosR`, `RC022AnualizadosUnidosR`, `RCR26AnualizadosUnidosR`, `ResumenMAEsR`, `RevisionProyectosR`, `SeguimientoSemanalProvinciasR`, `Subinforme InfTabla01Q`, `Subinforme InfTabla01Q1`, `SumatoriosActuacionesR`, `SumatoriosOperacionesR`, `TablasPriorizacionR`, `TextosR`

## Módulos y macros

`Módulo1`, `Módulo2`, `~TMPCLP619511`, `~TMPCLPMacro`

## Consultas guardadas

| Consulta | Tipo | Lee de (tablas/consultas) |
|---|---|---|
| 044TablaCoordinacionGeneralQ | select | ActuacionesT, ContratosT, ExpedientesT, LotesT, MedidasT, OperacionesT, TiposObjetosContratosT |
| 048TablaCoordinacionGeneralQ | select | ActuacionesT, ContratosT, ExpedientesT, LotesT, MedidasT, OperacionesT, TiposObjetosContratosT |
| 20250801RevisiónDescripExcelCompartidoQ | select | 20250801RevisiónDescripExcelCompartido, ActuacionesT |
| 20250904_ClimateProffingMedida044Q | select | 20250904_ClimateProofingMedida044, ActuacionesT |
| 20250910_ActuacionesQ | select | ActuacionesT, MedidasT, ObjetivosEspecificosT |
| 20250911_ActuacionesPriorizadas | select | ActuacionesT, RelLoteActuacionT |
| 20250915_ActuacionesQ | select | ActuacionesT, MedidasT, ObjetivosEspecificosT |
| 20260127_ConsultaAAEMedida44 | select | ImportesActuacionesUnificadasQ, RCO19AbsQ, ActuacionesT |
| 20260127_ConsultaAAEMedida48 | select | RCO22AbsQ, ActuacionesT |
| 20260921_ConsultaJulioHU | select | Edificios2Q, RCO22AbsQ, RCR31AbsQ, ActuacionesT, EstadosActuacionT, MedidasT, RelLoteActuacionT |
| 20261006CentrosFVRD413_2014 | select | ContratosQ, RCO22AbsQ |
| 20261016_ConsultaFFEE | select | ActuacionesT, ObjetivosEspecificosT, OperacionesT |
| A421AA44SA | select | IndicadoresMedidaOperacionQ, ActuacionesT, ExpedientesT, LotesT, MedidasT, OperacionesT, RelLoteActuacionT |
| AAETrim2_1Q | select | RCO19AbsActuacionQ, ActuacionesT, EstadosActuacionT, MedidasT |
| AAETrim2_2Q | select | Edificios2Q, RCO22AbsQ, RCR31AbsQ, ActuacionesT, EstadosActuacionT, MedidasT, RelLoteActuacionT |
| AOC_Actuaciones | select | RelLoteActuacion4Q, ActuacionesT, EstadosActuacionT |
| AOC_Expedientes | select | EstadosExpedienteT, ExpedientesT, LotesT, ProvT |
| AOC_Fechas | select | ActuacionesFechasObrQ, ActuacionesFechasPryQ, ActuacionesT |
| AOC_Operaciones | select | RelOperRespQ, OperacionesT |
| ActuaExpSQ | select | ExpedientesT, LotesT, RelLoteActuacionT |
| ActuaExpSQ2 | select | ExpedientesT, LotesT, RelLoteActuacionT |
| ActuaOGQ | select | ActuacionesT, EdificiosT, OrganosGestoresT |
| ActuacEdifiRefCatastral | select | EdificiosQ, ActuacionesT |
| ActuacExpedQ | select | ActuaExpSQ, ActuacionesT |
| ActuacionEstadoExpedientesQ | select | LoteFechasQ, ActuacionesT, ExpedientesT, LotesT, RelLoteActuacionT |
| ActuacionExpedientesGeneralQ | select | ActuacionEstadoExpedientesQ, ExpedientesQ, ActuacionesT |
| ActuacionExpedientesQ | select | AOC_Fechas, ActuacionesT |
| Actuaciones1Q | select | ActuacionesT |
| ActuacionesEEUnificadasQ | select | ActuacionesT |
| ActuacionesFVUnificadasQ | select | ActuacionesT |
| ActuacionesFechasObrQ | select | LoteFechasObraQ, ActuacionesT, RelLoteActuacionT |
| ActuacionesFechasPryQ | select | LoteFechasPyDoQ, ActuacionesT, RelLoteActuacionT |
| ActuacionesQ | select | ActuaExpSQ, IndicadoresActuacionesQ, ActuacionesT, CampusT, EdificiosT |
| ActuacionesSinCEEQ | select | ActuacionesT, RelActuacEdifCertT |
| ActuacionesTyS | select | ActuacionesT |
| ActuacionesUpdateQ | update |  |
| ActualizGranada048 | update | ActuacionesT |
| ActualizacionDiariaExpedientesQ | select | ExpedientesT |
| ActualizarImportePro5 | select | ActuacionesT |
| BitacoraQ | select | BitacoraT |
| BuscarActuacionesQ | select | ActuacionesT |
| CapacidadRenovableQ | select | ActuacionesT, CEET, RelActuacEdifCertT |
| CodSegFact2Q | select | ActuacionesT, ContratosT, OperacionesT |
| CodSegFactQ | select | ActuacionesT, ContratosT, LotesT, ProvT, TiposObjetosContratosT |
| ContratosGeneralQ | select | ActuacionesT, ContratosT, EstadosExpedienteT, ExpedientesT, LotesT |
| ContratosQ | select | ContratosT |
| Copia de CreditosAnualizadosQ | crosstab | ActuacionesT, CreditosT |
| Copia de OperacionesFe04Q | select | ActuacionesT, OperacionesT |
| CreditoMedidaQ | select | ActuacionesT, CreditosT |
| Creditos2Q | select | ActuacionesT, CreditosT |
| Creditos3Q | select | ActuacionesT, CreditosT |
| Creditos4Q | select | ActuacionesT, CreditosT |
| Creditos5Q | select | ActuacionesT, CreditosT, OperacionesT |
| Creditos6Q | select | ActuacionesT, CreditosT, OperacionesT |
| CreditosActuaciones2SQ | select | ActuacionesT, ContratosT, LotesT |
| CreditosActuacionesSQ | select | ActuacionesT, ContratosT, LotesT |
| CreditosAnualizadosQ | crosstab | ActuacionesT, CreditosT |
| CreditosCoordinacion44Q | crosstab | Creditos5Q, ActuacionesT |
| CreditosCoordinacion48Q | crosstab | Creditos5Q, ActuacionesT |
| CreditosFE04Q | crosstab | ActuacionesT, CreditosT |
| CreditosQ | select | ActuacionesT, CreditosT |
| CreditosRefQ | crosstab | CreditosT |
| DatosCEEActuacion | select | ActuacionesT, CEET, RelActuacEdifCertT |
| DatosFVMensualQ | select | IM_048Q, RCO22AbsQ, RCR31AbsQ, ActuacionesT, CampusT, EdificiosT, EstadosExpedienteT |
| DescripcionActuacion | select | ActuacionesT |
| Docum044Q | select | ActuacionesT, AuditoriasT, ProyectosT |
| Docum048Q | select | ActuacionesT, CEET, ProyectosT, RelActuacEdifCertT |
| Edificios2Q | select | ActuacionesT, CampusT, EdificiosT |
| EdificiosQ | select | ActuacionesT, CampusT, EdificiosT, RelActuacEdifCertT |
| EnvolventeQ | select |  |
| EstudioTempogranada048 | select | ActuacionesQ |
| ExpDOQ | select | ExpedientesT |
| ExpObraQ | select | ExpedientesT |
| ExpProyQ | select | ExpedientesT |
| ExpedComproSumLotesQ | select | ExpedientesT, LotesT |
| ExpedienteActuacionesSQ | select | ActuacionesQ, ActuaExpSQ |
| ExpedienteActualizarEstadoUQ | update | BitacoraQ, ExpedienteEstadosDeBitacoraQ, ExpedientesT |
| ExpedienteDesdeActuacionQ | select | ActuacionesT, LotesT, RelLoteActuacionT |
| ExpedienteEstadosDeBitacoraQ | select | BitacoraT |
| ExpedienteLotesQ | select | ActuacionesT, ExpedientesT, LotesT, RelLoteActuacionT |
| ExpedientesQ | select | ExpedientesT, TextosT |
| ExportQ | select |  |
| FE04ActuacionesQ | select | ActuacionesT |
| FE04CreditosSQ | select | ActuacionesQ, CreditosRefQ, FE04ActuacionesQ |
| FE04deGIROQ | select | OperacionesT |
| Fe04MedidaQ | select | ActuacionesT |
| FiltroEdificioQ | select | EdificiosT |
| GiroFE04Q | select | GIRO_FE04_Edgar, OperacionesT |
| IMActuaciones44Q | select | ActuacionesT, OperacionesT |
| IM_044Q | select | RelLoteActuacion5Q, ActuacionesT, MedidasT, OperacionesT |
| IM_048Q | select | RelLoteActuacion5Q, ActuacionesT, MedidasT, OperacionesT |
| IPAExpedientesQ | select | ExpedientesT, IPAExpedientesT |
| IPAImportesQ | select | ActuacionesT, ContratosT, LotesT, RelLoteActuacionT |
| IS_044Q | select | RelLoteActuacion5Q, ActuacionesT, ExpedientesT, MedidasT, OperacionesT |
| IS_048Q | select | IM_048Q, RCO22AbsQ, RCR31AbsQ, ActuacionesT, CampusT, EdificiosT, EstadosExpedienteT, OperacionesT |
| ImportesAQ | select | ExpedientesT, LotesT, RelLoteActuacionT |
| ImportesActuacionesUnificadasQ | select | ActuacionesEEUnificadasQ, ActuacionesFVUnificadasQ |
| ImportesComprometidosLotesActuacionQ | select | ActuacionesT, LotesT, RelLoteActuacionT |
| ImportesExpedienteSQ | select | CreditosActuaciones2SQ, ActuacionesT, EstadosExpedienteT, ExpedientesT, LotesT, RelLoteActuacionT |
| ImportesRCQ | select | CreditosT |
| Indicadores044Q | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| Indicadores048Q | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| IndicadoresActuacionesAnualizadosQ | select | IndicadoresAnualizados, ActuacionesT |
| IndicadoresActuacionesQ | select | ActuacionesQ, DatosCEEActuacion, InicioFinActuacionesQ, ActuacionesT, FechaFin |
| IndicadoresActuacionesUnidosQ | select | ActuacionesQ, DatosCEEActuacion, InicioFinActuacionesQ, ActuacionesT, FechaFin |
| IndicadoresAnualizados | crosstab | TodosIndicadoresQ |
| IndicadoresAnualizados48Q | crosstab | TodosIndicadoresQ |
| IndicadoresAnualizadosConsultaGeneralQ | select | IndicadoresAnualizadosUnidosQ, ActuacionesT, OperacionesT |
| IndicadoresAnualizadosRLCQ | select | IndicadoresAnualizadosUnidosQ, ActuacionesT |
| IndicadoresAnualizadosUnidosQ | crosstab | TodosIndicadoresUnidosQ |
| IndicadoresCoord044Q | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| IndicadoresCoord048Q | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| IndicadoresMedidaOperacionQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| IndicadoresOperacionesUnidosQ | crosstab | TodosIndicadoresUnidosQ |
| InfTabla01Q | select | InformeFE04Q, OperacionesFe04Q, OperacionesQ, RelLoteActuacionQ, SumatoriosOperacionesQ, ActuacionesT, ExpedientesT |
| InformeFE04Q | select | ActuacionesT |
| InicioFinActuacionesQ | select | ActuacionesT, CreditosT, FechaFin |
| ListadoActuaciones | select | RelLoteActuacionQ, ActuacionesT |
| LoteFechasObraQ | select | LoteFechasQ |
| LoteFechasPyDoQ | select | LoteFechasQ |
| LoteFechasQ | select | ExpedientesT, LotesT |
| Medida044DatosAnualizados | select | TodosIndicadoresQ, ActuacionesT |
| Medida044DatosUnicos | select | ActuacionesT |
| OperAnyadirFe04 | update | OperacionesFe04Q, OperacionesT |
| OperacVacias | select | ActuacionesT, OperacionesT |
| Operacionanadir | select | OperacionesFe04Q, OperacionesT |
| Operaciones2Q | select | ActuacionesT, OperacionesT |
| Operaciones3Q | select | ActuacionesT, OperacionesT |
| Operaciones4Q | select | OperacionesT |
| OperacionesFe04Q | select | OperacionesT |
| OperacionesImporteTotalQ | select | ActuacionesT, OperacionesT |
| OperacionesQ | select | OperacionesT |
| OperacionesRespQ | select | ActuacionesT, OperacionesT |
| ProyConSupervisionQ | select | ActuacionesT |
| ProyectosQ | select | ProyectosT |
| RC019AnualizadosUnidos | crosstab | TodosIndicadoresUnidosQ |
| RC022AnualizadosUnidos | crosstab | TodosIndicadoresUnidosQ |
| RCO19Abs | crosstab | IndicadoresMedidaOperacionQ |
| RCO19AbsActuacionQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCO19AbsQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCO19Base | crosstab | IndicadoresMedidaOperacionQ |
| RCO19BaseQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCO22Abs | crosstab | IndicadoresMedidaOperacionQ |
| RCO22AbsActuacionQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCO22AbsQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT, ContratosT, OperacionesT, TiposObjetosContratosT |
| RCO22BaseQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCR26AbsQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCR26AnualizadosUnidos | crosstab | TodosIndicadoresUnidosQ |
| RCR26BaseQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCR29AbsDeRCR31Q | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCR29AbsQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCR29AnualizadosUnidos | crosstab | TodosIndicadoresUnidosQ |
| RCR29BaseQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCR31AbsQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| RCR31AnualizadosUnidos | crosstab | TodosIndicadoresUnidosQ |
| RCR31BaseQ | select | ActuacionesQ, IndicadoresActuacionesQ, ActuacionesT |
| Ratio€RCO22 | select | RCO22AbsQ, ActuacionesT |
| RelActuacEdifCertQ | select | ActuacionesT, RelActuacEdifCertT |
| RelActuacExpedProDOObrQ | select | ActuaExpSQ2, ExpDOQ, ExpObraQ, ExpProyQ, ActuacionesT |
| RelLoteActuacion2Q | select | ActuacionesT, ExpedientesT, LotesT, RelLoteActuacionT |
| RelLoteActuacion3Q | select | ActuacionesT, ExpedientesT, LotesT, RelLoteActuacionT |
| RelLoteActuacion4Q | select | ExpedientesT, LotesT, RelLoteActuacionT |
| RelLoteActuacion5Q | select | ExpedientesT, LotesT, RelLoteActuacionT |
| RelLoteActuacion6Q | select | ExpedientesT, LotesT, RelLoteActuacionT |
| RelLoteActuacionQ | select | ActuacionesT, ExpedientesT, LotesT, RelLoteActuacionT |
| RelOperRespQ | select | ActuacionesT, OperacionesT |
| SeguimientoSemanalProvinciasQ | select | BitacoraT, ExpedientesT |
| SumatoriosActuacionesQ | select | RelLoteActuacionQ, ActuacionesT |
| SumatoriosOperacionesQ | select | RelLoteActuacionQ, ActuacionesT |
| TablaPriorizacionQ | select | ActuacionesT, ContratosT, ExpedientesT, LotesT, MedidasT, OperacionesT, TiposObjetosContratosT |
| Temp | select | ActuacionesT |
| TempFE04_Medida | select | ActuacionesT |
| TempModoInstQ | select | ActuacionesT |
| Temp_Operacion_FE04_Operac | select | ActuacionesT |
| TodosIndicadoresQ | union | Creditos4Q, RCO19AbsQ, RCO19BaseQ, RCO22AbsQ, RCO22BaseQ, RCR26AbsQ, RCR26BaseQ, RCR29AbsQ |
| TodosIndicadoresUnidosQ | select | TodosIndicadoresQ |
| VinculaLoteQ | select | ActuacionesT, LotesT |
| carpetasQ | select | ActuacionesT |
| temp2 | select | FechaFin, OperacionesT |
| tempCampos | select | ActuacionesT |