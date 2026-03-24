# 🛒 Segmentador Inteligente de Clientes Minoristas
### Retail Insights S.A. — Módulo 7: Aprendizaje No Supervisado

Pipeline completo de segmentación usando ML no supervisado:
**PCA · t-SNE · K-Means · DBSCAN · Agrupamiento Jerárquico**

---

## 📁 Estructura del Proyecto

```
segmentacion_clientes/
│
├── Train.csv                           # Dataset de entrada
├── segmentacion_clientes.py            # Script Python principal
├── segmentacion_clientes.ipynb         # Notebook Jupyter
├── informe_final.docx                  # Informe final con conclusiones
├── README.md                           # Este archivo
│
└── visualizaciones/
    ├── 01_pca_varianza.png
    ├── 02_pca_vs_tsne.png
    ├── 03_codo_silueta.png
    ├── 04_clustering_pca.png
    ├── 05_clustering_tsne.png
    ├── 06_dendrograma.png
    ├── 07_silueta_kmeans.png
    ├── 08_heatmap_clusters.png
    ├── 09_distribuciones_clusters.png
    └── 10_comparativa_silueta.png
```

---

## ⚙️ Requisitos Previos

- Python 3.8+
- Visual Studio Code con extensiones: **Python** y **Jupyter** (Microsoft)

---

## 🚀 Instalación Paso a Paso

### Paso 1 — Abrir el proyecto en VS Code

```bash
code segmentacion_clientes
```
O desde VS Code: **File → Open Folder**.

### Paso 2 — Crear entorno virtual

Terminal integrada (**Ctrl + `**):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 3 — Instalar dependencias

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy notebook ipykernel
```

### Paso 4 — Verificar dataset

Confirma que `Train.csv` esté en la raíz del proyecto.

---

## ▶️ Ejecución

### Opción A — Script directo

```bash
python segmentacion_clientes.py
```

Genera las 10 visualizaciones en `visualizaciones/` y muestra el resumen en consola.

### Opción B — Notebook Jupyter (recomendado)

1. Registra el kernel:
   ```bash
   python -m ipykernel install --user --name=venv --display-name "Python (venv)"
   ```
2. Abre `segmentacion_clientes.ipynb` en VS Code
3. Selecciona el kernel `Python (venv)` (esquina superior derecha)
4. Ejecuta con **Shift+Enter** celda a celda, o **Run All**

---

## 🔄 Pipeline Resumido

```
Train.csv (8.068 registros)
    │
    ▼  Preprocesamiento
       Imputación → Encoding → Outliers → StandardScaler
       → 6.969 registros × 9 features
    │
    ▼  Reducción Dimensional
       PCA (41.45% varianza, 2 comp.) + t-SNE (perplexity=40)
    │
    ▼  Selección de K
       Codo → k=5 | Silueta → k=2 | Decisión: k=4
    │
    ▼  Clusterización
       K-Means (0.168) ✅ | Jerárquico (0.128) | DBSCAN (0.108)
    │
    ▼  4 Segmentos identificados
       Seg 0: Adultos mayores (n=944)
       Seg 1: Adultos maduros familiares (n=2.950)
       Seg 2: Jóvenes con familia grande (n=1.561)
       Seg 3: Profesionales independientes (n=1.514)
```

---

## 📊 Resultados Clave

| Algoritmo | Silueta | Clústeres |
|-----------|---------|-----------|
| **K-Means** | **0.1680** ✅ | 4 |
| Jerárquico Ward | 0.1285 | 4 |
| DBSCAN | 0.1085 | 35 + ruido |

> Scores entre 0.1–0.2 son normales en datos mixtos reales. No indican mala
> calidad: reflejan que los segmentos se solapan naturalmente, como ocurre
> con clientes reales.

---

## 🔧 Parámetros Ajustables

```python
K_FINAL = 4   # Cambiar para explorar otros valores
# t-SNE: perplexity y max_iter ajustables en el script
```

---

## 🐛 Problemas Frecuentes

| Error | Solución |
|-------|----------|
| `No module named 'sklearn'` | `pip install scikit-learn` |
| `unexpected keyword argument 'n_iter'` | `pip install --upgrade scikit-learn` |
| Notebook sin kernel | `python -m ipykernel install --user` |

---

## 📚 Referencias

- [scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [Dataset Kaggle](https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation)
- Proyecto evaluación Módulo 7 — Alkemy, Marzo 2026
