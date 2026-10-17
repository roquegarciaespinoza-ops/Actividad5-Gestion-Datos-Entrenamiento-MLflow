# Análisis detallado de errores por clase

Fuente: informes CSV originales de la evaluación final sobre 2,566 caracteres; no se inventaron nuevas inferencias.

| Clase | Soporte en prueba | Recall LinearSVC | Recall Random Forest | Observación |
|---|---:|---:|---:|---|
| A | 6 | 0.00 % | 0.00 % | Ambos fallaron los seis caracteres |
| B | 56 | 67.86 % | 55.36 % | Confusión frecuente con 8 |
| D | 43 | 69.77 % | 39.53 % | Random Forest confunde muchos con 0 |
| T | 48 | 75.00 % | 68.75 % | Confusión notable con 1 |
| W | 36 | 77.78 % | 80.56 % | Random Forest ligeramente mejor |
| 3 | 157 | 96.82 % | 100.00 % | Random Forest mejor en esta clase |

La tabla ilustra por qué accuracy global y F1 macro no describen por sí solas el riesgo operativo. Excluir I, U y O deja una limitación explícita de cobertura. El número reducido de A afecta a la incertidumbre de su rendimiento.

La decisión de continuidad favorece a LinearSVC en desempeño agregado, pero se requieren datos mexicanos y evaluación **a nivel de matrícula completa** antes de pretender integrarlo a un control físico. Las predicciones no autorizan ingreso ni sustituyen revisión humana.
