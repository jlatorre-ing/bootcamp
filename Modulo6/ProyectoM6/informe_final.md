# 📋 Informe Final — Predicción de Gasto en Clientes E-commerce
**Proyecto:** Módulo 6 — Aprendizaje de Máquina Supervisado | Alkemy  
**Fecha:** Marzo 2026

---

## 1. Resumen Ejecutivo

Se desarrolló un modelo de regresión supervisada para predecir el monto promedio de compra de clientes en una plataforma e-commerce. A partir de un dataset de 1.000 registros con 15 variables de comportamiento y demografía, se entrenaron y compararon 6 algoritmos. El modelo final seleccionado fue **Gradient Boosting Regressor**, que alcanzó un **R² = 0.7956**, un **MAE = $20.70** y un **RMSE = $26.08** en el conjunto de prueba.

---

## 2. Definición del Problema

**Tipo:** Regresión supervisada  
**Variable objetivo:** `monto_compra_promedio` (continua, USD)  
**Contexto:** El Departamento de Analítica Comercial busca personalizar ofertas de marketing según el perfil de gasto esperado de cada usuario.

---

## 3. Descripción del Dataset

| Atributo | Valor |
|---|---|
| Registros | 1.000 |
| Variables | 16 (15 features + 1 target) |
| Variables categóricas | 5 |
| Variables numéricas | 10 |
| Valores nulos (antes de imputación) | 90 (~3%) |
| Outliers eliminados | 2 |

---

## 4. Preprocesamiento

- **Imputación de nulos:** mediana (variables `tiempo_promedio_sesion_min`, `calificacion_promedio_dada`, `dias_desde_ultima_compra`)
- **Tratamiento de outliers:** método IQR sobre variable target
- **Codificación categórica:** Label Encoding
- **Escalamiento:** StandardScaler (media=0, desvío=1)
- **División:** 80% entrenamiento / 20% prueba

---

## 5. Modelos Entrenados y Resultados

| Modelo | MAE | RMSE | R² |
|---|---|---|---|
| Regresión Lineal | 22.15 | 28.15 | 0.7618 |
| Regresión Polinomial (g=2) | 25.60 | 31.12 | 0.7090 |
| KNN Regressor (k=7) | 30.64 | 37.94 | 0.5674 |
| Ridge (α=10) | 22.09 | 28.12 | 0.7624 |
| Lasso (α=0.1) | 22.11 | 28.13 | 0.7622 |
| **Gradient Boosting** | **20.70** | **26.08** | **0.7956** |

> R² mide la proporción de varianza explicada (más alto = mejor). MAE y RMSE miden el error en dólares (más bajo = mejor).

### Validación Cruzada (K=5 folds)

| Modelo | CV R² (media ± desvío) |
|---|---|
| Regresión Lineal | 0.7002 ± 0.0545 |
| KNN Regressor | 0.4467 ± 0.0321 |

---

## 6. Modelo Final: Gradient Boosting Regressor

**Hiperparámetros óptimos (GridSearchCV):**
- `n_estimators`: 200
- `learning_rate`: 0.1
- `max_depth`: 3

**Variables más importantes:**
1. `nivel_membresia`
2. `items_en_carrito`
3. `paginas_vistas_sesion`
4. `tiempo_promedio_sesion_min`
5. `frecuencia_visitas_mes`

---

## 7. Análisis de Residuos

Los residuos del modelo Gradient Boosting presentan distribución aproximadamente normal centrada en 0, lo que indica buen ajuste sin sesgo sistemático. No se observan patrones heterocedásticos relevantes.

---

## 8. Conclusiones

1. **El problema es de regresión supervisada:** la variable objetivo es continua; usar clasificación implicaría pérdida de información y precisión.
2. **Gradient Boosting supera a la regresión lineal** en R² (+3.4 p.p.) y MAE (-1.45$), justificando su elección como modelo final.
3. **La regularización (Ridge/Lasso)** no mejoró significativamente respecto a la regresión lineal base, indicando que el dataset no tiene alta multicolinealidad severa.
4. **KNN Regressor** tuvo el peor desempeño, confirmando que el enfoque de vecinos más cercanos es sensible a la dimensionalidad del dataset.
5. **Las variables de comportamiento en el sitio** (items en carrito, páginas vistas, frecuencia de visitas) y el nivel de membresía son los predictores más potentes del gasto.

---

## 9. Recomendaciones

| # | Recomendación | Impacto |
|---|---|---|
| 1 | Probar XGBoost o LightGBM como alternativas de boosting más eficientes | Alto |
| 2 | Incorporar datos reales de transacciones con más meses de historial | Alto |
| 3 | Aplicar One-Hot Encoding para variables categóricas nominales (vs Label Encoding) | Medio |
| 4 | Explorar ingeniería de features: ratio gasto/visitas, recencia × frecuencia (RFM) | Medio |
| 5 | Monitorear el modelo en producción con métricas en ventana deslizante | Alto |
| 6 | Segmentar por cluster de clientes y entrenar modelos específicos por grupo | Medio |
| 7 | Reentrenar el modelo mensualmente incorporando nuevas transacciones | Alto |

---

## 10. Valor para el Negocio

Con un error promedio de **$20.70 por predicción**, el modelo permite:
- Personalizar descuentos y cupones según el perfil de gasto esperado
- Priorizar clientes con alto potencial de compra en campañas paid
- Detectar clientes en riesgo de churn (dias_desde_ultima_compra alto + predicción baja)
- Optimizar el inventory planning anticipando demanda por segmento

---

*Informe generado automáticamente — Módulo 6, Alkemy 2026*
