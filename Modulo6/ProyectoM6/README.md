# 🛒 Predicción Inteligente de Gasto en Clientes E-commerce
### Módulo 6: Aprendizaje de Máquina Supervisado | Alkemy

---

## 📁 Estructura del Proyecto

```
proyecto_m6/
├── dataset_ecommerce.csv          # Dataset simulado (1.000 registros)
├── generar_dataset.py             # Script para regenerar el dataset
├── modelo_ecommerce.py            # Script principal del modelo (.py)
├── notebook_m6_ecommerce.ipynb    # Notebook completo con análisis
├── diccionario_variables.md       # Descripción de todas las variables
├── informe_final.md               # Informe técnico con conclusiones
├── README.md                      # Este archivo
└── outputs/
    ├── tabla_metricas.csv         # Comparativa de métricas
    ├── fig1_eda.png               # Distribución y correlaciones
    ├── fig2_metricas.png          # Comparación de métricas
    ├── fig3_real_vs_predicho.png  # Real vs Predicho
    ├── fig4_importancia.png       # Feature importance + R² evolution
    └── fig5_residuos.png          # Análisis de residuos
```

---

## ⚙️ Requisitos

```bash
Python >= 3.9
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter  # para abrir el notebook
```

### Instalación de dependencias

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

---

## 🚀 Paso a Paso para Reproducir el Proyecto

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/tu-usuario/proyecto-m6-ecommerce.git
cd proyecto-m6-ecommerce
```

### 2. Crear y activar entorno virtual (recomendado)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

### 4. Generar el dataset simulado

```bash
python generar_dataset.py
```
> Esto crea `dataset_ecommerce.csv` con 1.000 registros y variables simuladas.

### 5. Opción A — Ejecutar el script Python directamente

```bash
python modelo_ecommerce.py
```
> Ejecuta todo el pipeline: preprocesamiento → modelado → evaluación → visualizaciones.  
> Las figuras se guardan automáticamente en `outputs/`.

### 6. Opción B — Abrir el Notebook en VS Code

```bash
jupyter notebook notebook_m6_ecommerce.ipynb
# o abrir VS Code y seleccionar el archivo .ipynb
```

**En VS Code:**
1. Instalar la extensión **Jupyter** (Microsoft)
2. Abrir `notebook_m6_ecommerce.ipynb`
3. Seleccionar el intérprete Python correcto (el del venv)
4. Ejecutar celdas con `Shift + Enter` o `Run All`

---

## 📊 Pipeline del Modelo

```
Datos Raw
    │
    ▼
[L3] Preprocesamiento
    ├── Imputación de nulos (mediana)
    ├── Eliminación de outliers (IQR)
    ├── Label Encoding (categóricas)
    └── StandardScaler
    │
    ▼
[L2] Split 80/20 + K-Folds (k=5)
    │
    ▼
[L4/L5/L7/L8] Entrenamiento de Modelos
    ├── Regresión Lineal
    ├── Regresión Polinomial (g=2)
    ├── KNN Regressor (k=7)
    ├── Ridge (GridSearchCV)
    ├── Lasso (GridSearchCV)
    └── Gradient Boosting (GridSearchCV)
    │
    ▼
[L6] Evaluación: MAE | RMSE | R²
    │
    ▼
🏆 Modelo Final: Gradient Boosting
   R² = 0.7956 | MAE = $20.70
```

---

## 📈 Resultados Principales

| Modelo | MAE | RMSE | R² |
|---|---|---|---|
| Regresión Lineal | 22.15 | 28.15 | 0.7618 |
| KNN (k=7) | 30.64 | 37.94 | 0.5674 |
| Ridge | 22.09 | 28.12 | 0.7624 |
| **Gradient Boosting** ✅ | **20.70** | **26.08** | **0.7956** |

---

## 🔑 Variables Más Importantes

1. `nivel_membresia` — clientes Platino gastan ~$90 más que Bronce
2. `items_en_carrito` — cada ítem adicional suma ~$12 al monto
3. `paginas_vistas_sesion` — refleja intención de compra
4. `frecuencia_visitas_mes` — clientes recurrentes compran más
5. `tiempo_promedio_sesion_min` — más tiempo = mayor engagement

---

## 💡 Conceptos Cubiertos por Lección

| Lección | Tema | Implementado |
|---|---|---|
| L1 | Fundamentos ML y definición del problema | ✅ |
| L2 | Validación cruzada K-Folds | ✅ |
| L3 | Preprocesamiento, encoding, escalado | ✅ |
| L4 | Regresión lineal y polinomial | ✅ |
| L5 | KNN y diferencias clasificación/regresión | ✅ |
| L6 | Métricas MAE, RMSE, R² | ✅ |
| L7 | Ridge, Lasso, GridSearchCV | ✅ |
| L8 | Gradient Boosting | ✅ |

---

## 📚 Referencias

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Kaggle Notebooks](https://www.kaggle.com/code)
- Manuales oficiales del curso M6 — Alkemy

---

*Proyecto realizado como evaluación del Módulo 6 de Alkemy — 2026*
