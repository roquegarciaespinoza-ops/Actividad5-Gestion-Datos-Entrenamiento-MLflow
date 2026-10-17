# Evidencias recuperadas del respaldo original de Colab

Se inspeccionó `Actividad5_Respaldo_20261017_222015.zip`, generado durante el experimento. Contiene 52 entradas, incluidas comparaciones de métricas, resultados de GridSearchCV, informes por clase, matrices PNG y la base `mlflow.db` con artefactos asociados.

Se publican aquí únicamente **resultados numéricos agregados** cotejados contra los archivos del respaldo:
- [Comparación final sobre prueba](comparacion_final_test.csv).
- [GridSearchCV](comparacion_gridsearch.csv).
- [Comparación estadística](comparacion_estadistica.json).
- [Manifiesto sin datos de imágenes](manifiesto_dataset_v1.0.0.json).

**Verificación importante:** el CSV original indica precisión macro LinearSVC **0.892368**, y se corrigió el valor erróneo previamente transcrito en README e informe.

**No se publican** la base de datos SQLite, modelos serializados, recortes, imágenes, identificadores de matrículas ni el ZIP completo. Las matrices de confusión originales siguen pendientes de incorporación como imágenes verificables.

Los valores publicados corresponden a **la ejecución original del notebook**, no a una nueva ejecución de los scripts del repositorio. La independencia de vehículos y la generalización al escenario mexicano siguen pendientes.

**IA responsable:** métricas por carácter y decisión exclusivamente experimental; no autorizan acceso vehicular.