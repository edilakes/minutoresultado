# Modelo de dominio – Minuto y Resultado (avance ordenado)

## Entidades conocidas (de inventario + app.py)
- ActuacionesT (358 filas, 38 cols) → macroestado 1-8
- EstadosActuacionT (catálogo, 20 filas)
- OrganosGestoresT, ProvT, CreditosT, ExpediEntesT
- Relaciones: RelLoteActuacionT (408), RelActuacEdifCertT (336)

## Reglas de negocio documentadas (app.py)
- EstadoActuacion → macroestado: >=8 finalizada, 7 ejecución, 6 licitación-obra, 5 proyecto, 4 redacción, 3 licitación, else pendiente.
- Responsable según macroestado; alerta si licitacion-obra/proyecto sin Cubierta.
- ProgresoEstimado = N * 10.

## Bloqueos / siguientes pasos ordenados
1. Resolver fuente SAS46_limpio.txt para completar 06/07.
2. Completar MODELO_DOMINIO con tablas de relación completas.
3. Fase 5: prueba de comprensión con datos reales NAS (solo lectura).
