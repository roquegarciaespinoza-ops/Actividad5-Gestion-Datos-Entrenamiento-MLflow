# Registro de decisiones técnicas

1. **Continuidad:** Actividad 5 en repositorio independiente, enlazado a [Actividad 4](https://github.com/roquegarciaespinoza-ops/Actividad4-Seleccion-Modelos-Prototipado-Rapido).
2. **Alcance:** clasificación de recortes individuales; no lectura integral de placas.
3. **Dataset:** UC3M-LP por disponibilidad de anotaciones de caracteres; dominio español no equivalente a México.
4. **Correspondencias:** ante 671 discrepancias `imagePath`, asociación provisional por nombre homónimo con auditoría estructural y revisión visual limitada.
5. **Clases:** excluir I, U, O por baja frecuencia y fallos de cobertura de validación; no reconstruir su desempeño con datos sintéticos.
6. **Separación:** grupos por `lp_id` parcialmente anonimizado, con advertencia de colisiones y casi-duplicados.
7. **Optimización:** F1 macro para atender desequilibrio; tres pliegues `StratifiedGroupKFold`, prueba reservada.
8. **Elección:** LinearSVC presentó mejor F1 macro en prueba; no equivale a eficacia de control físico.
9. **Métricas:** McNemar exploratorio porque se viola potencial independencia por caracteres de la misma matrícula.
10. **Versiones:** separar resultados históricos y reproducibilidad futura; registrar licencias y huellas.

**IA responsable:** minimización, no publicación de identificadores y revisión humana previa a cualquier decisión de seguridad.