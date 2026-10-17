# Auditoría verificable de MLflow desde SQLite

**Origen:** archivo `mlflow/mlflow.db` extraído del respaldo original `Actividad5_Respaldo_20261017_222015.zip`. Se consultaron directamente las tablas `runs`, `params` y `metrics`, sin arrancar un servidor web ni cargar modelos serializados.

**Conteos inspeccionados:** 8 ejecuciones, 61 registros de parámetros, 35 registros de métricas. **Estados:** 7 `FINISHED` y 1 `FAILED`.

| Ejecución | Estado | Identificador abreviado | Métrica principal |
|---|---|---|---|
| LinearSVC_Base | FINISHED | `b73fa40fbe89` | F1 macro 0.902522 (validación simple) |
| RandomForest_Base | FAILED | `6e217f94d7c9` | F1 macro 0.837321 (calculada antes del fallo de serialización) |
| RandomForest_Base_Recuperado | FINISHED | `76a993e707af` | F1 macro 0.837321 (validación simple) |
| LinearSVC_GridSearchCV | FINISHED | `05cbd6f332ea` | Mejor F1 macro CV 0.876405 |
| RandomForest_GridSearchCV | FINISHED | `f4af5a5b0631` | Mejor F1 macro CV 0.812594 |
| LinearSVC_Evaluacion_Final | FINISHED | `efa69b248d92` | F1 macro test 0.881741 |
| RandomForest_Evaluacion_Final | FINISHED | `661d111dc3b4` | F1 macro test 0.849087 |
| Comparacion_Estadistica_Final | FINISHED | `697a40b60a` | McNemar exploratorio p=0.000070514 |

## Parámetros de optimización registrados
- **LinearSVC:** 3 folds; optimización por F1 macro; `modelo__C=0.1`; 2 combinaciones; 1533.97 segundos de GridSearchCV.
- **Random Forest:** 3 folds; F1 macro; `max_depth=25`, `n_estimators=120`; 4 combinaciones; 336.78 segundos de GridSearchCV.

## Métricas de evaluación final
| Métrica | LinearSVC | Random Forest |
|---|---:|---:|
| Accuracy | 0.920889 | 0.898675 |
| Precision macro | 0.892368 | 0.882575 |
| Recall macro | 0.874187 | 0.831095 |
| F1 macro | 0.881741 | 0.849087 |

**Aclaración:** el intento `RandomForest_Base` con estado `FAILED` **sí registró** `tiempo_entrenamiento_seg=22.7483` antes del fallo al serializar, aunque ese dato no quedó registrado en la ejecución `RandomForest_Base_Recuperado`. No equivale a medir un entrenamiento nuevo.

## Integridad y límites
Este documento es una **transcripción auditada de registros originales en SQLite**, **no una captura de la interfaz gráfica de MLflow**. Los nombres y estados provienen de la base; los identificadores están abreviados para exposición. Los artefactos pueden mantener rutas del entorno temporal original y su restauración no se ha validado. El entrenamiento end-to-end con el dataset oficial tampoco se ha repetido desde GitHub.

**IER-IA / IA responsable:** no se publican imágenes, matrículas, la base SQLite ni archivos `pickle/cloudpickle`. Las métricas corresponden a clasificación de caracteres, no a reconocimiento íntegro de matrículas ni a autorización de acceso físico.