# 🎮 Proyecto EDA — Gaming Ratings Database
### Módulo 4: Análisis Exploratorio de Datos | Alkemy

---

## 📁 Estructura del Proyecto

```
proyecto_eda/
├── eda_gaming_ratings.ipynb          ← Notebook principal (VSC)
├── gaming-ratings-database-20260217.csv   ← Dataset IGDB
├── graficos_exportados/              ← PNGs generados al ejecutar
│   ├── 01_valores_faltantes.png
│   ├── 02_histograma_rating.png
│   ├── 03_boxplots.png
│   ├── 04_correlaciones.png
│   ├── 05_pairplot.png
│   ├── 06_regresion.png
│   ├── 07_violinplot.png
│   ├── 08_jointplot.png
│   ├── 09_heatmap_generos.png
│   ├── 10_facetgrid.png
│   ├── 11_top_generos.png
│   ├── 12_dashboard_ejecutivo.png
│   └── 13_top20_juegos.png
└── README.md                         ← Este archivo
```

---

## ⚙️ Paso 0 — Instalación del entorno

### 0.1 Requisitos previos
- Python 3.9 o superior
- Visual Studio Code instalado
- Extensión **Jupyter** de VSC instalada (`ms-toolsai.jupyter`)

### 0.2 Instalar dependencias

Abrí una terminal en VSC (`Ctrl+ñ` / `Cmd+J`) y ejecutá:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

> **Nota:** `statsmodels` también es compatible con el proyecto. Si tu entorno lo permite:
> ```bash
> pip install statsmodels
> ```

### 0.3 Verificar instalación

```python
import pandas, numpy, matplotlib, seaborn, sklearn
print("✅ Todo instalado correctamente")
```

---

## 📂 Paso 1 — Configuración del proyecto en VSC

1. Abrí VSC
2. Hacé clic en **File → Open Folder** y seleccioná la carpeta `proyecto_eda/`
3. En el explorador izquierdo vas a ver los archivos
4. Abrí `eda_gaming_ratings.ipynb` haciendo doble clic
5. En la esquina superior derecha del notebook, seleccioná el kernel de Python correcto

> 💡 **Tip:** Si no ves el kernel, presioná `Ctrl+Shift+P` → `Jupyter: Select Interpreter to Start Jupyter Server`

---

## 🗂️ Paso 2 — Cómo navegar el Notebook

El notebook está dividido en **6 lecciones** que corresponden al módulo:

| Sección | Lección | Contenido |
|---------|---------|-----------|
| Celda 1-2 | Setup | Importación de librerías y configuración global |
| Celdas 3-7 | **Lección 1** | Carga del dataset, tipos de variables, valores faltantes, limpieza |
| Celdas 8-11 | **Lección 2** | Estadística descriptiva, histogramas, boxplots, outliers |
| Celdas 12-15 | **Lección 3** | Correlación de Pearson, heatmap, pairplot, scatterplots |
| Celdas 16-18 | **Lección 4** | Regresión lineal simple y múltiple, R², RMSE, residuos |
| Celdas 19-23 | **Lección 5** | Violinplot, jointplot, heatmap de géneros, FacetGrid |
| Celdas 24-26 | **Lección 6** | Dashboard ejecutivo con Matplotlib, Top 20, resumen |

---

## ▶️ Paso 3 — Ejecutar el Notebook

### Opción A: Ejecutar todo de una vez
- Presioná `Ctrl+Shift+P` → `Jupyter: Run All Cells`
- O usá el botón **▶▶ Run All** en la barra superior del notebook

### Opción B: Ejecutar celda por celda (recomendado para aprender)
- Hacé clic en una celda y presioná `Shift+Enter` para ejecutarla y pasar a la siguiente
- O `Ctrl+Enter` para ejecutar sin avanzar

### Orden recomendado
```
Celda 1 (imports) → Celda 2 (carga) → seguir en orden secuencial
```
> ⚠️ **Importante:** Siempre ejecutá primero las celdas de importación y carga del dataset. Si ejecutás celdas fuera de orden podrías obtener errores de "variable no definida".

---

## 📊 Paso 4 — Lección por Lección

### 📌 Lección 1 — IDA (Análisis Inicial de Datos)

**¿Qué hacés en esta lección?**
1. Cargás el CSV con `pd.read_csv()`
2. Explorás estructura: `.shape`, `.dtypes`, `.head()`
3. Clasificás variables: numéricas vs categóricas
4. Buscás nulos con `.isnull().sum()`
5. Documentás el hallazgo de la columna `release_year` corrupta

**Código clave a entender:**
```python
df = pd.read_csv('gaming-ratings-database-20260217.csv')
df.info()
df.isnull().sum()
```

---

### 📌 Lección 2 — Estadística Descriptiva

**¿Qué hacés en esta lección?**
1. Calculás media, mediana, moda, varianza, desviación estándar
2. Obtenés cuartiles y percentiles con `.quantile()`
3. Generás histograma con KDE y boxplots
4. Aplicás el método IQR para detectar outliers

**Código clave a entender:**
```python
rating.mean()          # Media
rating.median()        # Mediana
rating.mode()[0]       # Moda
rating.std()           # Desv. estándar
rating.var()           # Varianza
rating.quantile(0.25)  # Cuartil Q1
rating.quantile(0.75)  # Cuartil Q3

# Límites IQR para outliers
Q1, Q3 = rating.quantile([0.25, 0.75])
IQR = Q3 - Q1
limite_inf = Q1 - 1.5 * IQR
limite_sup = Q3 + 1.5 * IQR
```

---

### 📌 Lección 3 — Correlación

**¿Qué hacés en esta lección?**
1. Preparás variables numéricas para correlación
2. Calculás la matriz de correlación de Pearson
3. Visualizás con heatmap y scatterplots
4. Identificás correlaciones espurias

**Código clave a entender:**
```python
# Coeficiente de Pearson entre dos variables
r = df['igdb_rating'].corr(df['n_genres'])

# Matriz completa de correlación
corr_matrix = df_numerico.corr(method='pearson')

# Heatmap
sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0)
```

**Interpretación del coeficiente r:**
- `|r| > 0.7` → Correlación **fuerte**
- `0.4 < |r| < 0.7` → Correlación **moderada**
- `|r| < 0.4` → Correlación **débil**

---

### 📌 Lección 4 — Regresión Lineal

**¿Qué hacés en esta lección?**
1. Implementás regresión lineal **simple** (1 predictor)
2. Implementás regresión lineal **múltiple** (varios predictores)
3. Calculás métricas: R², MSE, MAE, RMSE
4. Graficás valores reales vs predichos y los residuos

**Código clave a entender:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Simple
modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

# Métricas
r2   = r2_score(y, y_pred)
mse  = mean_squared_error(y, y_pred)
mae  = mean_absolute_error(y, y_pred)
rmse = mse ** 0.5

# Coeficiente e intercepto
print(modelo.coef_, modelo.intercept_)
```

**Interpretación de R²:**
- `R² = 1.0` → el modelo explica el 100% de la varianza
- `R² = 0.0` → el modelo no explica nada
- `R² < 0.1` → modelo con poco poder predictivo (nuestro caso)

---

### 📌 Lección 5 — Análisis Visual con Seaborn

**¿Qué hacés en esta lección?**
1. Creás un **violinplot** para comparar distribuciones por categoría
2. Creás un **jointplot** para ver relación bivariada + marginales
3. Usás un **heatmap** para visualizar matrices y presencia de géneros
4. Usás **FacetGrid** para segmentar gráficos por categorías

**Código clave a entender:**
```python
# Violinplot
sns.violinplot(data=df, x='genre_primary', y='igdb_rating', palette='Set2')

# Jointplot
sns.jointplot(data=df, x='n_genres', y='igdb_rating', kind='scatter')

# Heatmap
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdYlGn')

# FacetGrid
g = sns.FacetGrid(df, col='categoria')
g.map(sns.histplot, 'igdb_rating')
```

---

### 📌 Lección 6 — Librería Matplotlib

**¿Qué hacés en esta lección?**
1. Creás figuras con múltiples subplots (`fig.add_gridspec`)
2. Personalizás títulos, etiquetas, leyendas, colores, ticks
3. Usás anotaciones con `ax.annotate()`
4. Generás el dashboard ejecutivo final con 8 subgráficos
5. Exportás todos los gráficos en PNG/PDF

**Código clave a entender:**
```python
import matplotlib.pyplot as plt

# Crear figura con layout personalizado
fig = plt.figure(figsize=(18, 12))
gs  = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)
ax1 = fig.add_subplot(gs[0, 0])   # fila 0, col 0
ax2 = fig.add_subplot(gs[0, 1])   # fila 0, col 1
ax3 = fig.add_subplot(gs[1, :])   # fila 1, todas las cols

# Personalización
ax1.set_title('Mi gráfico', fontsize=13, fontweight='bold')
ax1.set_xlabel('Eje X')
ax1.set_ylabel('Eje Y')
ax1.legend(loc='upper right')

# Anotación
ax1.annotate('Punto importante', xy=(x_val, y_val),
             xytext=(x_text, y_text),
             arrowprops=dict(arrowstyle='->'))

# Exportar
plt.savefig('mi_grafico.png', dpi=150, bbox_inches='tight')
plt.savefig('mi_grafico.pdf', bbox_inches='tight')
```

---

## 💾 Paso 5 — Exportar los Gráficos

Los gráficos se **exportan automáticamente** al ejecutar cada celda del notebook. Se guardan en la carpeta `graficos_exportados/` en formato PNG.

### Exportar en otros formatos

Para guardar en **PDF** en lugar de PNG, cambiá la extensión:
```python
plt.savefig('mi_grafico.pdf', bbox_inches='tight')
```

Para guardar en **alta resolución** (para imprimir o presentar):
```python
plt.savefig('mi_grafico.png', dpi=300, bbox_inches='tight')
```

Para guardar **todos los gráficos** en PDF de una vez (útil para el informe):
```python
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('todos_los_graficos.pdf') as pdf:
    for fig_num in plt.get_fignums():
        pdf.savefig(plt.figure(fig_num), bbox_inches='tight')
print("✅ PDF con todos los gráficos generado")
```

### Parámetros útiles de `savefig`
| Parámetro | Descripción | Valor recomendado |
|-----------|-------------|-------------------|
| `dpi` | Resolución en puntos por pulgada | 150 (pantalla), 300 (impresión) |
| `bbox_inches` | Ajuste de márgenes | `'tight'` (siempre usar) |
| `facecolor` | Color de fondo | `fig.get_facecolor()` |
| `format` | Formato de salida | `'png'`, `'pdf'`, `'svg'` |

---

## 📝 Paso 6 — Escribir el Informe Técnico

El informe técnico debe documentar:

1. **Introducción**: Contexto del dataset, objetivo del análisis
2. **IDA (Análisis Inicial)**: Variables, tipos, nulos, inconsistencias encontradas
3. **Estadística Descriptiva**: Tabla de medidas, interpretación de distribuciones
4. **Correlaciones**: Qué variables están relacionadas y por qué
5. **Regresión**: Ecuación del modelo, R², limitaciones
6. **Visualizaciones**: Insertar los gráficos exportados con descripción
7. **Conclusiones y Recomendaciones**: Insights accionables para el negocio

> 💡 Podés usar Google Docs o Word, insertar los PNG exportados, y exportar el documento como PDF.

---

## 🐙 Paso 7 — Subir a GitHub

```bash
# En la terminal de VSC
git init
git add .
git commit -m "feat: EDA completo Gaming Ratings Database - Módulo 4 Alkemy"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/eda-gaming-ratings.git
git push -u origin main
```

### Estructura recomendada del README de GitHub
```markdown
## Contexto
Dataset de los 150 juegos mejor calificados de IGDB...

## Instalación
pip install -r requirements.txt

## Cómo ejecutar
Abrir eda_gaming_ratings.ipynb en VSC / Jupyter...

## Hallazgos principales
- Rating promedio: 96.49 ± 1.90
- Sin outliers detectados (dataset élite)
- ...

## Tecnologías
Python · Pandas · NumPy · Seaborn · Matplotlib · Scikit-learn
```

---

## ❓ Problemas Frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: seaborn` | Librería no instalada | `pip install seaborn` |
| `FileNotFoundError: gaming-ratings...` | CSV no está en la misma carpeta | Mover el CSV a la misma carpeta del notebook |
| `Kernel not found` | No hay kernel de Python seleccionado | Presionar `Ctrl+Shift+P` → "Select Kernel" |
| Gráficos no se muestran | Falta `plt.show()` | Agregar `plt.show()` al final de cada celda gráfica |
| `NameError: df not defined` | Ejecutaste celdas fuera de orden | Reiniciar kernel y ejecutar desde la primera celda |

---

## 📚 Referencias

- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [IGDB API](https://api-docs.igdb.com/)

---

*Proyecto desarrollado para el Módulo 4 — Análisis Exploratorio de Datos | Alkemy*
