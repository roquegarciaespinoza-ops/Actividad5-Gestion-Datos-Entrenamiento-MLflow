# Código experimental

- `datos_prep.py`: convierte anotaciones UC3M-LP en matrices normalizadas NPZ, verificando estructura y particiones por grupos.
- `train.py`: entrena LinearSVC y Random Forest con GridSearchCV y MLflow SQLite.

**Advertencia de reproducibilidad:** la lógica está disponible y se comprobó sintácticamente, pero no existe una ejecución integral verificada del código publicado sobre el dataset completo. La separación actual usa identificadores parcialmente ocultos, por lo que no puede equipararse a agrupación independiente por vehículo. Una nueva ejecución puede producir muestras y métricas diferentes de las históricas. No usar resultados de Colab como evidencia de ejecución de estos scripts.

No subir datos, fotografías, matrículas ni credenciales. Los modelos serializados deben cargarse solo desde fuentes confiables.
