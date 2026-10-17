# IA responsable · Indicador IER-IA

El **IER-IA** es un checklist documental de seis controles. **No mide seguridad del modelo, ausencia de sesgos ni conformidad legal**. Cada control se considera cumplido solo con evidencia y alcance explícitos.

| Control | Evidencia observada | Estado |
|---|---|---|
| Procedencia | Fuente Zenodo UC3M-LP identificada | Documentado |
| Integridad | MD5 del original, SHA-256 de derivados y auditoría estructural en sesión histórica | Documentado; exportación pública pendiente |
| Licencia | ODbL 1.0 identificada | Pendiente comprobar condiciones aplicables a derivados y redistribución |
| Privacidad | Notebook con salidas sensibles sanitizado; datos y matrículas fuera del repositorio | Pendiente auditoría de todos los artefactos antes de publicar |
| Sesgos y representatividad | Escasez de clases, exclusiones, origen europeo y errores por clase identificados | Riesgos identificados; mitigación pendiente |
| Supervisión humana | Política: ninguna predicción autoriza aperturas automáticas | Restricción de diseño; no existe validación operativa |

**No se publica un porcentaje IER-IA como certificación.** La revisión documental inicial en Colab contó tres de seis controles; el checklist actual distingue controles documentados, pendientes y riesgos no mitigados.

## Salvaguardas
- No publicar placas, datos personales de residentes, matrículas completas, imágenes o recortes identificables.
- No incorporar el modelo a barreras reales; exigir verificación de padrón, reglas de negocio y alternativa manual.
- Evitar métricas engañosas: accuracy por carácter ≠ por matrícula; identificar dependencias entre observaciones.
- Revisar licencias, hashes, artefactos y permisos antes de compartir.
- Tratar modelos serializados `pickle/cloudpickle` como código ejecutable de confianza limitada.

La política aplica al README, notebook, código, evidencias, resultados y entregables posteriores.