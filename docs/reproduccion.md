# Reproducción y alcance de la evidencia

## Fuente
Descargar UC3M-LP desde [Zenodo](https://zenodo.org/records/17152029). Verificar integridad y licencia. **No se incluye el ZIP de 4.55 GB ni sus imágenes.**

## Experimento histórico
Notebook ejecutado en Google Colab (sesión de 2026-10-17), con semilla 42, NumPy 2.1.3, scikit-learn 1.6.1, MLflow 3.17.1 y SQLite. Resultados se resumen en [informe](reporte_tecnico.md). Ocho ejecuciones MLflow fueron respaldadas externamente; la base SQLite y sus rutas de artefactos no están publicadas.

## Procedimiento lógico
1. Descargar el ZIP y validar hash, pares JPG/JSON y anotaciones.
2. Asociar JPG y JSON por nombre homónimo con advertencia de discrepancias `imagePath`.
3. Excluir clases I, U y O en el experimento histórico, conservar originales.
4. Transformar cada carácter a escala de grises 32×32 y vector 1024, valores [0,1].
5. Dividir por grupos derivados de IDs parcialmente ocultos; revisar solapamientos y cobertura de las 31 clases.
6. GridSearchCV con 3 folds estratificados por grupo y F1 macro; guardar ejecuciones con MLflow SQLite.
7. Comparar predicciones en prueba solo después de selección; generar matriz de confusión, métricas y análisis de errores.
8. Mantener evidencia del código, semillas, versiones, artefactos y riesgos éticos.

## Condición de reproducibilidad
Esta documentación describe la sesión histórica. **No se ha verificado una ejecución limpia de extremo a extremo sobre el dataset original desde este repositorio.** Una ejecución nueva puede producir otra partición por grupos o distintas métricas. No equiparar reproducciones con las métricas históricas sin cotejo independiente.

**IA responsable:** no subir fotografías, identificadores ni bases de datos privadas al repositorio.