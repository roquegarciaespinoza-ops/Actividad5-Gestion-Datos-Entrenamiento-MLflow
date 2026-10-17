# Actividad 5 · Gestión de datos, entrenamiento y MLflow

**Proyecto de continuidad:** control de acceso vehicular por visión computacional.  
**Antecedente:** [Actividad 4 — selección de modelos y prototipado rápido](https://github.com/roquegarciaespinoza-ops/Actividad4-Seleccion-Modelos-Prototipado-Rapido).

## Propósito y alcance
Experimento académico con **clasificación de caracteres aislados** de matrículas de UC3M-LP. Se compararon LinearSVC y Random Forest, con limpieza y versionamiento, búsqueda de hiperparámetros, validación cruzada agrupada y registros MLflow. **No se desarrolló lectura integral de placas ni conexión a barreras físicas. No usar para autorizar ingresos.**

## Resultados observados (ejecución original en Colab)
| Métrica sobre 2,566 caracteres reservados | LinearSVC | Random Forest |
|---|---:|---:|
| Accuracy | **92.09 %** | 89.87 % |
| Precision macro | **89.24 %** | 88.26 % |
| Recall macro | **87.42 %** | 83.11 % |
| F1 macro | **88.17 %** | 84.91 % |
| F1 macro CV (3 folds) | **87.64 %** | 81.26 % |

El mejor candidato **experimental** es LinearSVC (pipeline con StandardScaler, C=0.1). Estas cifras provienen de la ejecución histórica observada; **no certifican ejecución independiente de los scripts publicados**. Tampoco son una tasa de reconocimiento de matrícula completa.

## Datos y limitaciones
Fuente: [UC3M-LP en Zenodo](https://zenodo.org/records/17152029), licencia de origen ODbL 1.0. Se auditaron 1,975 imágenes, 2,547 matrículas anotadas y 12,757 caracteres. Se encontraron 671 discrepancias en `imagePath`; por inspección y cotejo estructural se emplearon JPG/JSON homónimos. Se excluyeron 13 anotaciones correspondientes a I, U y O para disponer de 31 clases en el experimento. La división agrupada por identificador parcialmente oculto tiene limitaciones de independencia entre vehículos.

No se redistribuyen las imágenes originales, placas, recortes ni archivos de entrenamiento derivados. Documentar obtención y términos de uso antes de cualquier redistribución.

## Guía del repositorio
- [Informe técnico](docs/reporte_tecnico.md)
- [Rúbrica y evidencias pendientes](docs/cumplimiento_rubrica.md)
- [Reproducción](docs/reproduccion.md)
- [Decisiones técnicas](docs/decisiones_tecnicas.md)
- [Deuda técnica y MLOps](docs/mlops_deuda_tecnica.md)
- [IA responsable · IER-IA](docs/IA_RESPONSABLE.md)
- [Registro de cambios](CHANGELOG.md)

## Estado de publicación
Documentación de los resultados reales y riesgos disponible. **Pendiente:** publicar y verificar de forma segura las evidencias CSV y MLflow exportadas desde Colab, notebook sanitizado y comprobar scripts de extremo a extremo. Los resultados históricos **no deben confundirse** con ejecuciones del repositorio.

## IA responsable
Se limita el uso a investigación, se preservan originales, se documentan licencias, representatividad, filtración potencial, privacidad y revisión humana. No publicar identificadores de matrícula ni modelos serializados de origen desconocido.

## Notebook
[Consultar el notebook sanitizado de Colab](fuentes/Actividad5_notebook_historico_sanitizado.ipynb). Consta de 40 celdas y no contiene salidas de ejecución; los CSV publicados documentan los resultados históricos. **IA responsable:** las salidas y matrículas identificables no se difunden.
