# Informe: Reducción Dimensional — VisionData
**Especialista:** Ciencia de Datos | **Dataset:** survey_data.csv (500 clientes × 60 variables)

---

## Técnica Recomendada: PCA para presentaciones ejecutivas

Para presentar insights al equipo de **marketing y ventas**, se recomienda **PCA** como técnica principal. Si bien t-SNE genera clusters visualmente más compactos y separados, PCA presenta ventajas decisivas en este contexto:

- Los **ejes son interpretables**: PC1 y PC2 tienen carga sobre variables concretas del dataset (demográficas, consumo, digitales), lo que permite explicar *por qué* los segmentos difieren.
- Es **reproducible y estable**: dos corridas con los mismos datos producen exactamente el mismo resultado, requisito para reportes ejecutivos periódicos.
- Permite **proyectar nuevos clientes** sobre los mismos ejes sin reentrenar el modelo.
- Los 2 primeros componentes capturan el **69.8% de la varianza total** del dataset, suficiente para identificar los cuatro segmentos con claridad.

---

## Principales Hallazgos

El análisis identificó **4 agrupamientos naturales** de clientes en el espacio reducido:

| Segmento | Perfil |
|---|---|
| Jóvenes digitales | Alto score en variables demográficas de edad joven y preferencias digitales |
| Adultos conservadores | Patrón bajo en demo, moderado consumo, neutral en digital |
| Seniors offline | Fuerte en preferencias digitales básicas, bajo consumo online |
| Profesionales tech | Alto consumo, bajo en indicadores digitales avanzados |

Ambas técnicas confirman la separación de los segmentos; t-SNE los muestra más compactos y separados, pero sin interpretabilidad de los ejes.

---

## Reflexión Crítica

La reducción dimensional es poderosa pero conlleva **pérdida de información**: con PCA 2D se descarta el 30.2% de la varianza. Para modelos predictivos, sería preferible conservar más componentes (10 PCs capturan el 76.4%).

**t-SNE** no debe usarse para más que visualización exploratoria: sus distancias entre clusters no son comparables entre ejecuciones, y escala mal con millones de registros.

Para conjuntos de datos mucho mayores, la estrategia recomendada es: **PCA incremental → UMAP** (más rápido que t-SNE, con mejor preservación de estructura global y soporte para proyección de nuevos puntos).
