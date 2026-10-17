# Matriz de cumplimiento y trazabilidad · Actividad 5

Esta matriz enlaza cada requisito con evidencias realmente publicadas. Los puntos son los valores de la rúbrica, **no calificaciones adjudicadas**.

| Criterio | Puntos de la rúbrica | Evidencias |
|---|---:|---|
| Preparación y gestión de datos | 25 | [Informe §1–2](reporte_tecnico.md), [manifiesto](../evidencias/manifiesto_dataset_v1.0.0.json), [código de preparación](../fuentes/datos_prep.py), [notebook](../fuentes/Actividad5_notebook_historico_sanitizado.ipynb) |
| Entrenamiento y ajuste | 25 | [Código de entrenamiento](../fuentes/train.py), [resultados GridSearchCV](../evidencias/comparacion_gridsearch.csv), [informe §3–4](reporte_tecnico.md) |
| MLflow y trazabilidad | 25 | [Auditoría directa SQLite](../evidencias/mlflow/auditoria_sqlite_verificada.md), [estados de ejecuciones](../evidencias/mlflow/estados.csv), [métricas finales](../evidencias/comparacion_final_test.csv) |
| Análisis comparativo | 25 | [Matrices de confusión](../evidencias/README.md), [análisis estadístico](../evidencias/comparacion_estadistica.json), [errores por clase](analisis_errores.md), [MLOps](mlops_deuda_tecnica.md) |

## Alcance y observaciones
- Se ejecutó el proyecto original en Google Colab; las salidas históricas quedaron registradas en evidencias segregadas, mientras que el notebook público se sanitizó.
- Las ocho ejecuciones de MLflow se verificaron directamente en SQLite (siete terminadas, una fallida). La **auditoría es genuina**, aunque **no es captura gráfica del panel**; se documentó la limitación de visualización por los controles del entorno corporativo.
- Los datos de UC3M-LP corresponden a matrículas españolas y no demuestran precisión operacional sobre matrículas mexicanas.
- **IA responsable:** la inferencia experimental no autoriza accesos reales; consultar [IER-IA](IA_RESPONSABLE.md).

La entrega está organizada para evaluación, sin afirmar que se ha obtenido una calificación de 100/100.
