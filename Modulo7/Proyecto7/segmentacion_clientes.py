# =============================================================================
# SEGMENTADOR INTELIGENTE DE CLIENTES MINORISTAS
# Retail Insights S.A. — Módulo 7: Aprendizaje No Supervisado
# =============================================================================
# Autor: Equipo de Analítica
# Dataset: Customer Segmentation (Train.csv)
# =============================================================================

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, silhouette_samples
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist

import os

# Directorio de salida para visualizaciones
OUTPUT_DIR = "visualizaciones"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta de colores consistente
PALETTE = ['#2196F3', '#FF5722', '#4CAF50', '#9C27B0', '#FF9800']

print("=" * 65)
print("   SEGMENTADOR INTELIGENTE DE CLIENTES MINORISTAS")
print("   Retail Insights S.A. — Módulo 7")
print("=" * 65)

# =============================================================================
# ETAPA 1 — CARGA Y EXPLORACIÓN DEL DATASET
# =============================================================================
print("\n[1/6] Cargando y explorando el dataset...")

df_raw = pd.read_csv("Train.csv")
print(f"  • Dimensiones originales: {df_raw.shape[0]} filas × {df_raw.shape[1]} columnas")
print(f"  • Columnas: {list(df_raw.columns)}")
print(f"  • Valores nulos por columna:\n{df_raw.isnull().sum().to_string()}")

# =============================================================================
# ETAPA 2 — PREPROCESAMIENTO Y LIMPIEZA
# =============================================================================
print("\n[2/6] Preprocesando datos...")

df = df_raw.copy()

# Eliminar columna ID (no aporta información de comportamiento)
df.drop(columns=['ID'], inplace=True)

# --- Imputación de valores nulos ---
# Numéricas: mediana (robusta a outliers)
df['Work_Experience'].fillna(df['Work_Experience'].median(), inplace=True)
df['Family_Size'].fillna(df['Family_Size'].median(), inplace=True)

# Categóricas: moda
for col in ['Ever_Married', 'Graduated', 'Profession', 'Var_1']:
    df[col].fillna(df[col].mode()[0], inplace=True)

print(f"  • Nulos restantes: {df.isnull().sum().sum()}")

# --- Encoding de variables categóricas ---
# Mapeos ordinales con sentido semántico
df['Gender_enc']         = df['Gender'].map({'Male': 0, 'Female': 1})
df['Ever_Married_enc']   = df['Ever_Married'].map({'No': 0, 'Yes': 1})
df['Graduated_enc']      = df['Graduated'].map({'No': 0, 'Yes': 1})
df['Spending_Score_enc'] = df['Spending_Score'].map({'Low': 0, 'Average': 1, 'High': 2})

# Label encoding para Profession y Var_1
le = LabelEncoder()
df['Profession_enc'] = le.fit_transform(df['Profession'])
df['Var_1_enc']      = le.fit_transform(df['Var_1'])

# Columnas de features para el modelo
FEATURES = ['Age', 'Work_Experience', 'Family_Size',
            'Gender_enc', 'Ever_Married_enc', 'Graduated_enc',
            'Spending_Score_enc', 'Profession_enc', 'Var_1_enc']

X = df[FEATURES].copy()

# --- Detección y eliminación de outliers (IQR sobre variables numéricas) ---
num_cols = ['Age', 'Work_Experience', 'Family_Size']
mask = pd.Series([True] * len(X), index=X.index)
for col in num_cols:
    Q1, Q3 = X[col].quantile(0.25), X[col].quantile(0.75)
    IQR = Q3 - Q1
    mask &= (X[col] >= Q1 - 3 * IQR) & (X[col] <= Q3 + 3 * IQR)

X = X[mask].reset_index(drop=True)
df = df[mask].reset_index(drop=True)

# Aseguramos que no queden NaN tras el filtrado
X = X.fillna(X.median(numeric_only=True))
print(f"  • Registros tras limpiar outliers: {len(X)}")
print(f"  • NaN restantes en X: {X.isnull().sum().sum()}")

# --- Normalización (StandardScaler) ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("  • Normalización aplicada (StandardScaler)")

# =============================================================================
# ETAPA 3 — REDUCCIÓN DIMENSIONAL: PCA y t-SNE
# =============================================================================
print("\n[3/6] Aplicando reducción dimensional...")

# -- PCA --
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)
var_exp = pca.explained_variance_ratio_
print(f"  • PCA: varianza explicada PC1={var_exp[0]:.2%}, PC2={var_exp[1]:.2%} "
      f"(total={sum(var_exp):.2%})")

# PCA completo para análisis de varianza acumulada
pca_full = PCA(random_state=42)
pca_full.fit(X_scaled)
cum_var = np.cumsum(pca_full.explained_variance_ratio_)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Análisis de Componentes Principales (PCA)", fontsize=14, fontweight='bold')

# Varianza explicada acumulada
axes[0].plot(range(1, len(cum_var)+1), cum_var, 'o-', color='#2196F3', lw=2)
axes[0].axhline(0.80, color='#FF5722', ls='--', label='80% umbral')
axes[0].axhline(0.90, color='#4CAF50', ls='--', label='90% umbral')
axes[0].set_xlabel("Número de componentes")
axes[0].set_ylabel("Varianza explicada acumulada")
axes[0].set_title("Varianza Acumulada por Componentes")
axes[0].legend()
axes[0].grid(alpha=0.3)

# Barras de varianza por componente
axes[1].bar(range(1, len(pca_full.explained_variance_ratio_)+1),
            pca_full.explained_variance_ratio_, color='#2196F3', alpha=0.8)
axes[1].set_xlabel("Componente")
axes[1].set_ylabel("Varianza explicada")
axes[1].set_title("Varianza por Componente PCA")
axes[1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_pca_varianza.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/01_pca_varianza.png")

# -- t-SNE --
print("  • Ejecutando t-SNE (puede tardar unos segundos)...")
tsne = TSNE(n_components=2, random_state=42, perplexity=40, max_iter=1000)
X_tsne = tsne.fit_transform(X_scaled)
print("  • t-SNE completado")

# Visualización PCA vs t-SNE coloreados por Segmentation original
seg_labels = df['Segmentation'].values
seg_unique = sorted(df['Segmentation'].unique())
color_map  = {seg: PALETTE[i] for i, seg in enumerate(seg_unique)}
colors     = [color_map[s] for s in seg_labels]

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle("Reducción Dimensional — PCA vs t-SNE\n(coloreado por segmentación original)",
             fontsize=13, fontweight='bold')

for ax, X_2d, title in zip(axes,
                             [X_pca, X_tsne],
                             ["PCA (2 componentes)", "t-SNE (perplexity=40)"]):
    ax.scatter(X_2d[:, 0], X_2d[:, 1], c=colors, alpha=0.5, s=12, edgecolors='none')
    ax.set_title(title, fontsize=12)
    ax.set_xlabel("Dimensión 1")
    ax.set_ylabel("Dimensión 2")
    ax.grid(alpha=0.2)

patches = [mpatches.Patch(color=color_map[s], label=f"Seg {s}") for s in seg_unique]
axes[1].legend(handles=patches, loc='upper right', fontsize=9)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_pca_vs_tsne.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/02_pca_vs_tsne.png")

# =============================================================================
# ETAPA 4 — MÉTODO DEL CODO (K óptimo para K-Means)
# =============================================================================
print("\n[4/6] Determinando número óptimo de clústeres (método del codo + silueta)...")

k_range = range(2, 11)
inertias, silhouettes = [], []

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_scaled, labels))

# Detectar el codo automáticamente (máxima segunda derivada)
inertia_arr = np.array(inertias)
diffs2 = np.diff(np.diff(inertia_arr))
k_opt = list(k_range)[np.argmax(diffs2) + 1]
sil_opt = list(k_range)[np.argmax(silhouettes)]
print(f"  • K sugerido por el codo:   {k_opt}")
print(f"  • K con mayor silueta:      {sil_opt}  (score={max(silhouettes):.4f})")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Determinación del Número Óptimo de Clústeres", fontsize=13, fontweight='bold')

axes[0].plot(list(k_range), inertias, 'o-', color='#2196F3', lw=2)
axes[0].axvline(k_opt, color='#FF5722', ls='--', label=f'Codo en k={k_opt}')
axes[0].set_xlabel("Número de clústeres (k)")
axes[0].set_ylabel("Inercia (WCSS)")
axes[0].set_title("Método del Codo")
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].plot(list(k_range), silhouettes, 's-', color='#4CAF50', lw=2)
axes[1].axvline(sil_opt, color='#FF5722', ls='--', label=f'Máx silueta en k={sil_opt}')
axes[1].set_xlabel("Número de clústeres (k)")
axes[1].set_ylabel("Coeficiente de silueta")
axes[1].set_title("Coeficiente de Silueta vs k")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_codo_silueta.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/03_codo_silueta.png")

K_FINAL = 4  # Alineado con las 4 segmentaciones del dataset original

# =============================================================================
# ETAPA 5 — ALGORITMOS DE CLUSTERIZACIÓN
# =============================================================================
print(f"\n[5/6] Aplicando algoritmos de clusterización (k={K_FINAL})...")

# --- 5A. K-Means ---
kmeans = KMeans(n_clusters=K_FINAL, random_state=42, n_init=10)
labels_km = kmeans.fit_predict(X_scaled)
sil_km = silhouette_score(X_scaled, labels_km)
print(f"  • K-Means    → Silueta: {sil_km:.4f}")

# --- 5B. DBSCAN ---
# Determinamos eps con heurística de la distancia al vecino más cercano
from sklearn.neighbors import NearestNeighbors
nbrs = NearestNeighbors(n_neighbors=5).fit(X_scaled)
distances, _ = nbrs.kneighbors(X_scaled)
dist_sorted = np.sort(distances[:, -1])

# eps en el "codo" de la curva de distancias
eps_val = float(np.percentile(dist_sorted, 90))
dbscan = DBSCAN(eps=eps_val, min_samples=5)
labels_db = dbscan.fit_predict(X_scaled)
n_clusters_db = len(set(labels_db)) - (1 if -1 in labels_db else 0)
n_noise_db    = (labels_db == -1).sum()
mask_valid_db = labels_db != -1
sil_db = silhouette_score(X_scaled[mask_valid_db], labels_db[mask_valid_db]) if n_clusters_db > 1 else -1
print(f"  • DBSCAN     → Clústeres: {n_clusters_db}, Ruido: {n_noise_db}, Silueta: {sil_db:.4f}")

# --- 5C. Agrupamiento Jerárquico ---
hc = AgglomerativeClustering(n_clusters=K_FINAL, linkage='ward')
labels_hc = hc.fit_predict(X_scaled)
sil_hc = silhouette_score(X_scaled, labels_hc)
print(f"  • Jerárquico → Silueta: {sil_hc:.4f}")

# ---- Visualizaciones de clusterización sobre PCA ----
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle(f"Resultados de Clusterización — Proyección PCA (k={K_FINAL})",
             fontsize=13, fontweight='bold')

configs = [
    (labels_km, f"K-Means (Silueta={sil_km:.3f})"),
    (labels_db, f"DBSCAN  (eps={eps_val:.2f}, Silueta={sil_db:.3f})"),
    (labels_hc, f"Jerárquico Ward (Silueta={sil_hc:.3f})"),
]

for ax, (labels, title) in zip(axes, configs):
    unique_labels = sorted(set(labels))
    cmap = plt.cm.get_cmap('tab10', len(unique_labels))
    for i, lbl in enumerate(unique_labels):
        mask = labels == lbl
        name = "Ruido" if lbl == -1 else f"Clúster {lbl}"
        color = 'gray' if lbl == -1 else cmap(i)
        ax.scatter(X_pca[mask, 0], X_pca[mask, 1],
                   c=[color], alpha=0.5, s=10, label=name, edgecolors='none')
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.legend(fontsize=7, markerscale=2)
    ax.grid(alpha=0.2)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_clustering_pca.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/04_clustering_pca.png")

# ---- Mismos clusters sobre t-SNE ----
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle(f"Resultados de Clusterización — Proyección t-SNE (k={K_FINAL})",
             fontsize=13, fontweight='bold')

for ax, (labels, title) in zip(axes, configs):
    unique_labels = sorted(set(labels))
    cmap = plt.cm.get_cmap('tab10', len(unique_labels))
    for i, lbl in enumerate(unique_labels):
        mask = labels == lbl
        name = "Ruido" if lbl == -1 else f"Clúster {lbl}"
        color = 'gray' if lbl == -1 else cmap(i)
        ax.scatter(X_tsne[mask, 0], X_tsne[mask, 1],
                   c=[color], alpha=0.5, s=10, label=name, edgecolors='none')
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("Dim 1")
    ax.set_ylabel("Dim 2")
    ax.legend(fontsize=7, markerscale=2)
    ax.grid(alpha=0.2)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/05_clustering_tsne.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/05_clustering_tsne.png")

# ---- Dendrograma (muestra sobre sample de 500 registros) ----
print("  • Generando dendrograma...")
sample_idx = np.random.default_rng(42).choice(len(X_scaled), size=500, replace=False)
Z = linkage(X_scaled[sample_idx], method='ward')

fig, ax = plt.subplots(figsize=(14, 5))
dendrogram(Z, ax=ax, truncate_mode='lastp', p=30, leaf_rotation=90,
           color_threshold=Z[-K_FINAL+1, 2])
ax.axhline(Z[-K_FINAL+1, 2], color='#FF5722', ls='--', lw=1.5,
           label=f'Corte para k={K_FINAL}')
ax.set_title("Dendrograma — Agrupamiento Jerárquico Ward (muestra n=500)", fontsize=12, fontweight='bold')
ax.set_xlabel("Índice de muestra")
ax.set_ylabel("Distancia Ward")
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/06_dendrograma.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/06_dendrograma.png")

# ---- Gráfico de silueta (K-Means como mejor modelo) ----
sil_vals = silhouette_samples(X_scaled, labels_km)
fig, ax = plt.subplots(figsize=(10, 6))
y_lower = 10
cmap_sil = plt.cm.get_cmap('tab10')
for i in range(K_FINAL):
    ith_sil = np.sort(sil_vals[labels_km == i])
    size_i  = len(ith_sil)
    y_upper = y_lower + size_i
    color   = cmap_sil(i / K_FINAL)
    ax.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_sil, alpha=0.7, color=color)
    ax.text(-0.05, y_lower + 0.5 * size_i, str(i))
    y_lower = y_upper + 10
ax.axvline(sil_km, color='#FF5722', ls='--', lw=1.5, label=f'Silueta media={sil_km:.3f}')
ax.set_title("Gráfico de Silueta — K-Means", fontsize=12, fontweight='bold')
ax.set_xlabel("Coeficiente de silueta")
ax.set_ylabel("Clúster")
ax.legend()
ax.grid(alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/07_silueta_kmeans.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/07_silueta_kmeans.png")

# =============================================================================
# ETAPA 6 — ANÁLISIS E INTERPRETACIÓN DE SEGMENTOS
# =============================================================================
print("\n[6/6] Analizando perfil de cada segmento...")

# Usamos K-Means como modelo final (mejor silueta + interpretable)
df['Cluster_KMeans'] = labels_km

# Perfil medio por clúster
profile = df.groupby('Cluster_KMeans')[
    ['Age', 'Work_Experience', 'Family_Size', 'Spending_Score_enc']
].mean().round(2)
profile['Spending_Score_enc'] = profile['Spending_Score_enc'].map(
    {0: 'Low', 1: 'Average', 2: 'High',
     0.0: 'Low~', 1.0: 'Average~', 2.0: 'High~'}).fillna(
    profile['Spending_Score_enc'].round(2))

profile['n'] = df.groupby('Cluster_KMeans').size()
print(profile.to_string())

# ---- Heatmap de características por clúster ----
cluster_means = df.groupby('Cluster_KMeans')[FEATURES].mean()
cluster_means_z = (cluster_means - cluster_means.mean()) / cluster_means.std()

fig, ax = plt.subplots(figsize=(12, 5))
sns.heatmap(cluster_means_z.T, annot=True, fmt=".2f", cmap='RdBu_r',
            center=0, linewidths=0.5, ax=ax, cbar_kws={'label': 'Z-score'})
ax.set_title("Perfil de Clústeres — Valores Z (K-Means)", fontsize=12, fontweight='bold')
ax.set_xlabel("Clúster")
ax.set_ylabel("Feature")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/08_heatmap_clusters.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/08_heatmap_clusters.png")

# ---- Distribuciones por clúster ----
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Distribuciones Clave por Clúster (K-Means)", fontsize=13, fontweight='bold')

cmap4 = plt.cm.get_cmap('tab10')
clust_colors = {c: cmap4(c / K_FINAL) for c in range(K_FINAL)}

# Age
for c in range(K_FINAL):
    subset = df[df['Cluster_KMeans'] == c]['Age']
    axes[0, 0].hist(subset, bins=20, alpha=0.5, color=clust_colors[c], label=f'C{c}')
axes[0, 0].set_title("Distribución de Edad")
axes[0, 0].set_xlabel("Edad")
axes[0, 0].legend()
axes[0, 0].grid(alpha=0.3)

# Spending Score
spend_counts = df.groupby(['Cluster_KMeans', 'Spending_Score']).size().unstack(fill_value=0)
spend_counts.plot(kind='bar', ax=axes[0, 1], colormap='Set2', edgecolor='white')
axes[0, 1].set_title("Nivel de Gasto por Clúster")
axes[0, 1].set_xlabel("Clúster")
axes[0, 1].set_ylabel("Cantidad")
axes[0, 1].tick_params(axis='x', rotation=0)
axes[0, 1].grid(alpha=0.3, axis='y')

# Work Experience
for c in range(K_FINAL):
    subset = df[df['Cluster_KMeans'] == c]['Work_Experience']
    axes[1, 0].hist(subset, bins=15, alpha=0.5, color=clust_colors[c], label=f'C{c}')
axes[1, 0].set_title("Distribución de Experiencia Laboral")
axes[1, 0].set_xlabel("Años de experiencia")
axes[1, 0].legend()
axes[1, 0].grid(alpha=0.3)

# Profession
top_profs = df['Profession'].value_counts().head(6).index
prof_counts = df[df['Profession'].isin(top_profs)].groupby(
    ['Cluster_KMeans', 'Profession']).size().unstack(fill_value=0)
prof_counts.plot(kind='bar', ax=axes[1, 1], colormap='tab20', edgecolor='white')
axes[1, 1].set_title("Profesión por Clúster (top 6)")
axes[1, 1].set_xlabel("Clúster")
axes[1, 1].tick_params(axis='x', rotation=0)
axes[1, 1].legend(fontsize=7)
axes[1, 1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/09_distribuciones_clusters.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/09_distribuciones_clusters.png")

# ---- Comparativa de silueta entre modelos ----
fig, ax = plt.subplots(figsize=(8, 5))
modelos = ['K-Means', 'DBSCAN\n(puntos válidos)', 'Jerárquico\nWard']
scores  = [sil_km, sil_db, sil_hc]
bar_colors = ['#2196F3', '#FF5722', '#4CAF50']
bars = ax.bar(modelos, scores, color=bar_colors, edgecolor='white', width=0.5)
ax.set_ylim(0, max(scores) * 1.3)
ax.set_ylabel("Coeficiente de silueta")
ax.set_title("Comparativa de Silueta — Tres Algoritmos", fontsize=12, fontweight='bold')
for bar, score in zip(bars, scores):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
            f"{score:.4f}", ha='center', va='bottom', fontweight='bold')
ax.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/10_comparativa_silueta.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"  • Guardado: {OUTPUT_DIR}/10_comparativa_silueta.png")

# =============================================================================
# RESUMEN FINAL
# =============================================================================
print("\n" + "=" * 65)
print("   RESUMEN DE RESULTADOS")
print("=" * 65)
print(f"  Dataset:         {len(X)} registros procesados")
print(f"  Features usados: {len(FEATURES)}")
print(f"  K óptimo (codo): {k_opt}  |  K óptimo (silueta): {sil_opt}")
print(f"  Modelo final:    K-Means con k={K_FINAL}")
print(f"  ┌─────────────┬──────────┬──────────┐")
print(f"  │ Algoritmo   │ Silueta  │ Clústeres│")
print(f"  ├─────────────┼──────────┼──────────┤")
print(f"  │ K-Means     │ {sil_km:.4f}   │    {K_FINAL}     │")
print(f"  │ DBSCAN      │ {sil_db:.4f}   │    {n_clusters_db}     │")
print(f"  │ Jerárquico  │ {sil_hc:.4f}   │    {K_FINAL}     │")
print(f"  └─────────────┴──────────┴──────────┘")
print(f"\n  Visualizaciones guardadas en: ./{OUTPUT_DIR}/")
print("\n  ¡Pipeline completado con éxito!\n")
