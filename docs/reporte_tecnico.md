# Informe técnico · Actividad 5

## 1. Descripción del dataset
UC3M-LP ([Zenodo, registro 17152029](https://zenodo.org/records/17152029)): imágenes de matrículas españolas, anotaciones JSON con coordenadas y caracteres, licencia original ODbL 1.0. Auditoría histórica en Colab: 1,975 imágenes, 1,975 JSON, 2,547 matrículas y 12,757 caracteres.

## 2. Preparación, calidad y versionamiento
Se observaron 671 archivos JSON cuyo `imagePath` no se encontraba en el mismo directorio. Se estudió asociación JPG/JSON de igual nombre, se inspeccionaron seis ejemplos y se verificaron estructuralmente 1,975 pares. Las imágenes pasaron a escala de grises, recorte por cuadro de carácter y resolución 32 × 32, aplanadas en 1,024 características [0,1]. Se excluyeron 13 caracteres de clases I, U y O por escasez de representación y validación cruzada, quedando 31 clases y 12,744 muestras. Se generaron dos archivos NPZ (10,178 y 2,566) con huellas SHA-256 y manifiesto v1.0.0. Esos archivos **no están publicados**.

La división experimental usó identificadores de matrículas parcialmente ocultos para agrupar; hubo 107 identificadores compartidos en la división original del proveedor. La nueva separación redujo coincidencias literales a cero, pero **no prueba independencia a nivel de vehículo**. Se comprobó ausencia de duplicados exactos entre matrices normalizadas; eso no descarta casi-duplicados.

## 3. Modelos e hiperparámetros
**LinearSVC:** Pipeline StandardScaler + LinearSVC, GridSearchCV con C ∈ {0.1,1.0}; mejor C=0.1. **Random Forest:** 80/120 árboles × profundidad 15/25; mejor 120 y 25. Se empleó `StratifiedGroupKFold` de tres particiones y puntuación `f1_macro`, sin seleccionar hiperparámetros con la prueba final.

## 4. Métricas finales
| Métrica | LinearSVC | Random Forest |
|---|---:|---:|
| Accuracy | 0.920889 | 0.898675 |
| Precision macro | 0.923368 | 0.882575 |
| Recall macro | 0.874187 | 0.831095 |
| F1 macro | 0.881741 | 0.849087 |
| F1 macro CV | 0.876405 | 0.812594 |
| Latencia promedio por carácter (ms) | 0.049967 | 0.091689 |

La optimización tomó 1533.97 s en LinearSVC y 336.78 s en Random Forest, según la sesión histórica. La latencia refleja procesamiento por lote en Colab, no tiempo extremo a extremo del sistema de acceso.

## 5. Análisis de errores y estadística
En la prueba, ambos modelos acertaron 2,234 casos; solo LinearSVC acertó 129, solo Random Forest 72 y ambos fallaron 131. Diferencia en accuracy de 2.221 puntos porcentuales y en F1 macro de 3.265. La prueba exacta de McNemar dio p≈0.000071 **bajo el supuesto de observaciones independientes**. Como varios caracteres pueden pertenecer a una misma matrícula, el valor p es orientativo y no constituye evidencia inferencial definitiva a nivel de vehículo. Entre los errores observados figuran A→4, D→0, T→1 y B→8.

## 6. Decisión y límites
LinearSVC es el candidato para continuar **esta investigación de clasificación individual**, no una solución que pueda abrir barreras. Faltan pruebas en matrículas mexicanas, validación de reconocimiento completo, desempeño por condiciones, falsa aceptación/rechazo, privacidad y evaluación independiente a nivel de vehículo.

## 7. MLflow y reproducibilidad
En la sesión histórica se registraron ocho ejecuciones en MLflow con SQLite, parámetros, métricas y artefactos. Un ZIP de 18.03 MB se respaldó en Google Drive. El respaldo no está compartido en este repositorio y la portabilidad de las rutas de artefactos no ha sido validada. Los nuevos scripts no han completado una reproducción independiente.

## 8. IA responsable
Consultar [IER-IA](IA_RESPONSABLE.md). Uso exclusivamente académico, minimización de datos y supervisión humana exigida para decisiones de acceso. No divulgar matrículas ni bases de residentes.