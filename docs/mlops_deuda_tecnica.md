# Deuda técnica y MLOps

## Situación
Se cuenta con experimento de Colab registrado en MLflow y respaldo externo. La versión actual es un prototipo académico; no existe despliegue ni monitoreo operativo.

## Deuda priorizada
| Prioridad | Riesgo | Acción |
|---|---|---|
| Alta | Repeticiones de vehículo o coincidencias de `lp_id` oculto entre grupos | Auditoría a nivel de vehículo y partición por grupos realmente independientes |
| Alta | Excluir I, U, O | Ampliar datos por clase y revalidar con diseño aprobado |
| Alta | Diferencias entre matrículas españolas y mexicanas | Evaluación externa con datos locales lícitamente obtenidos |
| Alta | Confundir carácter implica error de placa | Medir CER, coincidencia exacta por matrícula y falsa aceptación de acceso |
| Alta | Datos e inferencias personales | Minimizar retención, controles de acceso y consentimiento/base legal según proceda |
| Media | Artefactos MLflow con rutas temporales | Migrar o reexportar a almacenamiento estable y verificar restauración |
| Media | Scripts sin prueba integral | CI, tests, versiones de paquetes y ejecución de reproducción |
| Media | Deriva y errores por entorno | Monitoreo, umbrales, revisión humana, rollback |

## MLOps propuesto
Versionado de código, datos y modelos; seguimiento de experimentos y semillas; pipeline reproducible; pruebas de integridad y métricas de calidad; monitoreo de errores y deriva; gestión de incidentes y reversión. **No se afirma haber implementado monitoreo productivo.**

**IA responsable:** revisión humana para accesos, no inferir autorización a partir de una cadena OCR sola.