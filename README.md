# Actividad 5 · Gestión de datos, entrenamiento y MLflow

**Proyecto:** control de acceso vehicular mediante visión computacional. Continuidad de la [Actividad 4](https://github.com/roquegarciaespinoza-ops/Actividad4-Seleccion-Modelos-Prototipado-Rapido).

## Resumen ejecutivo
Proyecto académico de clasificación de **caracteres individuales** de matrículas a partir del dataset público UC3M-LP. En Google Colab se realizó auditoría de datos, preparación y versionamiento, entrenamiento de **LinearSVC y Random Forest**, ajuste mediante GridSearchCV, evaluación y registro de experimentos con MLflow.

El modelo de continuidad elegido es **LinearSVC**, por su mejor desempeño sobre el conjunto de prueba reservado.

| Métrica final en 2,566 caracteres | LinearSVC | Random Forest |
|---|---:|---:|
| Accuracy | **92.09 %** | 89.87 % |
| Precision macro | **89.24 %** | 88.26 % |
| Recall macro | **87.42 %** | 83.11 % |
| F1 macro | **88.17 %** | 84.91 % |
| F1 macro en CV (tres pliegues) | **87.64 %** | 81.26 % |

**Alcance:** estos resultados corresponden a reconocimiento de caracteres recortados; no constituyen desempeño de lectura de matrículas completas ni permiten autorizar la apertura de una barrera.

## Fuente y metodología
- [UC3M-LP en Zenodo](https://zenodo.org/records/17152029), anotaciones de matrículas españolas; revisar licencia ODbL 1.0 antes de reutilizar o redistribuir datos.
- 1,975 imágenes y 12,757 caracteres originales auditados; 31 clases y 12,744 caracteres seleccionados para el experimento (exclusión documentada de I, U y O).
- Imágenes en escala de grises normalizadas a 32 × 32; partición experimental 10,178 entrenamiento / 2,566 prueba.
- Validación cruzada con tres pliegues, agrupación por identificadores parcialmente ocultos y optimización por F1 macro. La agrupación no garantiza independencia total entre vehículos.
- Seguimiento mediante **ocho ejecuciones de MLflow**: siete finalizaron y una falló durante la serialización inicial de Random Forest; el modelo se recuperó y registró después.

## Entregables principales
- [Notebook de Colab sanitizado](fuentes/Actividad5_notebook_historico_sanitizado.ipynb) (código conservado, salidas eliminadas por privacidad)
- [Preparación de datos](fuentes/datos_prep.py) y [entrenamiento](fuentes/train.py)
- [Informe técnico](docs/reporte_tecnico.md) y [rúbrica vinculada a evidencias](docs/cumplimiento_rubrica.md)
- [Matriz de confusión LinearSVC](evidencias/matriz_confusion_linearsvc.png) y [Random Forest](evidencias/matriz_confusion_randomforest.png)
- [Evaluación final CSV](evidencias/comparacion_final_test.csv), [ajuste CSV](evidencias/comparacion_gridsearch.csv), [informes por clase](evidencias/README.md)
- [Auditoría auténtica de MLflow desde SQLite](evidencias/mlflow/auditoria_sqlite_verificada.md)
- [Decisiones técnicas](docs/decisiones_tecnicas.md), [MLOps y deuda técnica](docs/mlops_deuda_tecnica.md), [IA responsable e IER-IA](docs/IA_RESPONSABLE.md)
- [Pruebas automatizadas en GitHub Actions](https://github.com/roquegarciaespinoza-ops/Actividad5-Gestion-Datos-Entrenamiento-MLflow/actions/workflows/validacion.yml)

## Evidencia y transparencia
El experimento fue **ejecutado en Colab**, y sus métricas y matrices se conservaron desde esa ejecución. El repositorio incluye scripts, documentación, pruebas automatizadas y evidencias seleccionadas. La auditoría de MLflow proviene de su base SQLite original y **no se presenta como captura de pantalla del panel web**.

No se publican imágenes de origen, placas, datos de residentes, dataset derivado ni modelos serializados. El uso es estrictamente académico: el sistema **no opera torniquetes ni toma decisiones de acceso**.

## IA responsable
Se documentan procedencia, integridad, licencia, privacidad, representatividad, errores por clase y supervisión humana en [IER-IA](docs/IA_RESPONSABLE.md). No se interpreta el checklist como una certificación ética o legal.
