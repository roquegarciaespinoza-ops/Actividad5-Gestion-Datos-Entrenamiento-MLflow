# Matriz de trazabilidad de la rúbrica

Los cuatro criterios valen 25 puntos cada uno. Esta matriz documenta **cobertura**, no una calificación obtenida ni garantía de 100/100.

| Criterio | Evidencia disponible | Pendientes antes del cierre |
|---|---|---|
| Gestión y preparación (25) | [Informe §1-2](reporte_tecnico.md), manifiesto v1.0.0 descrito, selección de 31 clases y análisis de discrepancias | CSV y manifiesto agregados publicados; faltan reproducción probada, revisión de licencia y diccionario completo |
| Entrenamiento y ajuste (25) | [Informe §3-4](reporte_tecnico.md), dos algoritmos, GridSearchCV y tres folds documentados | Código íntegro publicable; reproducción externa independiente |
| MLflow y reproducibilidad (25) | [Informe §7](reporte_tecnico.md), ocho ejecuciones y respaldo en Drive | CSV agregados publicados; faltan capturas originales de MLflow, restauración de artefactos e instrucciones comprobadas |
| Análisis e interpretación (25) | [Informe §4-6](reporte_tecnico.md), McNemar exploratorio, errores por clase y [MLOps](mlops_deuda_tecnica.md) | Matriz de confusión original pendiente; profundizar inferencia agrupada |

**IA responsable transversal:** [controles IER-IA](IA_RESPONSABLE.md). No publicar material identificable en ningún criterio.