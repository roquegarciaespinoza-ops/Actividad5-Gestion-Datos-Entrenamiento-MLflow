# Auditoría del registro MLflow original (SQLite)

Se inspeccionó la base SQLite incluida en el ZIP de Colab y se consultó la tabla de ejecuciones sin publicar bases, modelos ni rutas internas. **Ocho ejecuciones**: siete con estado `FINISHED` y una con estado `FAILED` (primer intento de registrar Random Forest por serialización).

[Resumen de estados](resumen_ejecuciones.csv). Las métricas finales cotejadas están publicadas en [comparación de prueba](../comparacion_final_test.csv), [GridSearchCV](../comparacion_gridsearch.csv) y [comparación estadística](../comparacion_estadistica.json). Hay rastros genuinos de seguimiento MLflow, pero **no constituye una captura del panel MLflow**.

Para reproducir el panel y sus artefactos se requiere restaurar la base SQLite y reubicar rutas originales; esa restauración aún no ha sido comprobada. No publicar `model.pkl`, otros modelos serializados, imágenes originales ni información identificable.

**IA responsable:** documentar incluso la ejecución fallida y evitar presentar ocho entrenamientos exitosos cuando uno falló al serializar.
