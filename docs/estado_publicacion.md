# Auditoría de publicación — alcance y pendientes

**Publicados:** README, documentación técnica, rúbrica, decisiones, MLOps, controles éticos, dependencias, preparación y entrenamiento en Python, controles de prueba básicos.

**Publicación adicional:** CSV agregados de prueba y GridSearchCV, comparación estadística y manifiesto sanitizado publicados y contrastados contra ZIP de Colab. **Sin publicar todavía:** notebook sanitizado (disponible como archivo aparte), matrices PNG originales, informes por clase completos, capturas de MLflow y dataset derivado. Los dos últimos requieren una evaluación de licencias y privacidad previa a cualquier difusión.

**Sin validar:** ejecución de extremo a extremo desde el repositorio con datos oficiales y restauración portable del respaldo MLflow.

**Próximos pasos:** incorporar notebook sanitizado desde un archivo verificado, evidencia externa depurada; validar reproducción de scripts y CI; complementar inferencia estadística agrupada por matrícula.

Los datos numéricos del informe se atribuyen a la sesión original de Colab, no a una reproducción nueva.

**IA responsable:** mantener público solo contenido sin matrículas ni información personal.


## Actualización — notebook cargado
Notebook sanitizado publicado en [`fuentes/Actividad5_notebook_historico_sanitizado.ipynb`](../fuentes/Actividad5_notebook_historico_sanitizado.ipynb), verificado con 40 celdas (31 código), cero salidas y cero contadores de ejecución. Pendientes: gráficos originales y evidencia visual MLflow, reproducción independiente. La presencia del notebook no acredita ejecución nueva.


## Cierre de verificaciones automatizadas
Se agregó el flujo [Validación básica](https://github.com/roquegarciaespinoza-ops/Actividad5-Gestion-Datos-Entrenamiento-MLflow/actions/workflows/validacion.yml) que compila el código y ejecuta pruebas sin dataset personal. La primera ejecución terminó correctamente; la ejecución tras añadir la prueba de integración sintética debe consultarse en Actions. **Estas pruebas no sustituyen la reproducción integral con UC3M-LP.**

Se extrajeron los PNG originales de matrices de confusión y CSV de informes por clase del respaldo de Colab para resguardo fuera de GitHub. La conexión de publicación actual no admite transferir esos binarios originales, por lo que **continúan pendientes de publicación en el repositorio**. Tampoco se dispone de capturas genuinas del panel web de MLflow.


## Cierre de alternativa MLflow (sin alterar seguridad de red)
Por las restricciones de visualización de MLflow vía proxy, se preparó una [auditoría tabulada directamente sobre la base SQLite original](../evidencias/mlflow/auditoria_sqlite_verificada.md), publicada y trazable a 8 runs, 61 registros de parámetros y 35 registros de métricas. No se afirma que sea captura del panel. Reproducción total del dataset oficial: aún no verificada.
