# ============================================================
# ANÁLISIS DE CASO: Técnicas de Reducción Dimensional
# DataMed Analytics — Dataset Clínico (Breast Cancer Wisconsin)
# ============================================================
# Autor: Científico/a de Datos Junior — DataMed Analytics
# Dataset: Breast Cancer Wisconsin (Scikit-learn / UCI Repository)
# Técnicas: PCA (Principal Component Analysis) + t-SNE
# ============================================================

# ── 1. IMPORTACIÓN DE LIBRERÍAS ─────────────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Paleta de colores para las dos clases
COLORS = ['#E63946', '#457B9D']   # Rojo = maligno, Azul = benigno
LABELS = ['Maligno', 'Benigno']

# ============================================================
# PASO 1: CARGA Y ANÁLISIS EXPLORATORIO DEL DATASET
# ============================================================

print("=" * 60)
print("  ANÁLISIS DE CASO — REDUCCIÓN DIMENSIONAL")
print("  DataMed Analytics")
print("=" * 60)

# Cargar dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='diagnostico')   # 0=maligno, 1=benigno

print(f"\n📊 EXPLORACIÓN INICIAL DEL DATASET")
print(f"{'─'*40}")
print(f"  • Número de muestras    : {X.shape[0]}")
print(f"  • Número de variables   : {X.shape[1]}")
print(f"  • Clases                : {list(data.target_names)}")
print(f"  • Distribución de clases:")
print(f"      Maligno  (0): {(y == 0).sum()} muestras")
print(f"      Benigno  (1): {(y == 1).sum()} muestras")
print(f"\n  Primeras 5 filas del dataset:")
print(X.head())
print(f"\n  Estadísticas descriptivas:")
print(X.describe().round(3))

# Verificar valores nulos
print(f"\n  Valores nulos por columna: {X.isnull().sum().sum()} (ninguno)")

# ============================================================
# PASO 2: ESTANDARIZACIÓN CON STANDARDSCALER
# ============================================================

print(f"\n{'='*60}")
print("  PASO 2 — ESTANDARIZACIÓN DE DATOS (StandardScaler)")
print(f"{'='*60}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"\n  ✅ StandardScaler aplicado correctamente.")
print(f"  Media antes  de escalar: {X.values.mean():.4f}")
print(f"  Media después de escalar: {X_scaled.mean():.6f}  (≈ 0)")
print(f"  Desv. estándar después : {X_scaled.std():.6f}  (≈ 1)")
print(f"\n  → Cada variable ahora tiene media 0 y varianza 1,")
print(f"    necesario para que PCA no se sesgue por escala.")

# ============================================================
# PASO 3: APLICACIÓN DE PCA
# ============================================================

print(f"\n{'='*60}")
print("  PASO 3 — PCA (Principal Component Analysis)")
print(f"{'='*60}")

# ── 3a. Determinar número óptimo de componentes ──────────────
pca_full = PCA()
pca_full.fit(X_scaled)

varianza_acumulada = np.cumsum(pca_full.explained_variance_ratio_)
n_componentes_95 = np.argmax(varianza_acumulada >= 0.95) + 1

print(f"\n  Varianza explicada por componente:")
for i, v in enumerate(pca_full.explained_variance_ratio_[:10], 1):
    barra = '█' * int(v * 50)
    print(f"    PC{i:2d}: {v*100:5.2f}% {barra}")
print(f"    ...")
print(f"\n  → Componentes necesarios para retener el 95% de varianza: {n_componentes_95}")
print(f"  → Reducción: de {X.shape[1]} variables a {n_componentes_95} componentes")

# ── 3b. PCA reducido a 2D para visualización ─────────────────
pca_2d = PCA(n_components=2)
X_pca = pca_2d.fit_transform(X_scaled)

var_pc1 = pca_2d.explained_variance_ratio_[0] * 100
var_pc2 = pca_2d.explained_variance_ratio_[1] * 100
var_total_2d = var_pc1 + var_pc2

print(f"\n  PCA reducido a 2 componentes (visualización):")
print(f"    PC1 explica: {var_pc1:.2f}% de la varianza")
print(f"    PC2 explica: {var_pc2:.2f}% de la varianza")
print(f"    Total 2D   : {var_total_2d:.2f}% de la varianza")

# ── 3c. Cargas factoriales (top variables por componente) ────
cargas = pd.DataFrame(
    pca_2d.components_.T,
    columns=['PC1', 'PC2'],
    index=data.feature_names
)

print(f"\n  Top 5 variables con mayor peso en PC1:")
top_pc1 = cargas['PC1'].abs().sort_values(ascending=False).head(5)
for feat, val in top_pc1.items():
    print(f"    {feat:<35} : {cargas.loc[feat,'PC1']:+.4f}")

print(f"\n  Top 5 variables con mayor peso en PC2:")
top_pc2 = cargas['PC2'].abs().sort_values(ascending=False).head(5)
for feat, val in top_pc2.items():
    print(f"    {feat:<35} : {cargas.loc[feat,'PC2']:+.4f}")

# ============================================================
# PASO 4: APLICACIÓN DE t-SNE
# ============================================================

print(f"\n{'='*60}")
print("  PASO 4 — t-SNE (t-distributed Stochastic Neighbor Embedding)")
print(f"{'='*60}")

# Parámetros razonados
PERPLEXITY    = 30    # Típicamente entre 5-50; 30 funciona bien para ~570 muestras
LEARNING_RATE = 200   # Rango recomendado: 10-1000; 200 es valor estándar
N_ITER        = 1000  # Mínimo recomendado; más iteraciones = mejor convergencia
RANDOM_STATE  = 42

print(f"\n  Parámetros seleccionados:")
print(f"    • perplexity    = {PERPLEXITY}  (balance local/global, ~√n_muestras)")
print(f"    • learning_rate = {LEARNING_RATE}  (tasa de aprendizaje estándar)")
print(f"    • n_iter        = {N_ITER}  (iteraciones para convergencia)")
print(f"    • random_state  = {RANDOM_STATE}  (reproducibilidad)")
print(f"\n  ⏳ Ejecutando t-SNE (puede tardar unos segundos)...")

tsne = TSNE(
    n_components=2,
    perplexity=PERPLEXITY,
    learning_rate=LEARNING_RATE,
    max_iter=N_ITER,
    random_state=RANDOM_STATE
)
X_tsne = tsne.fit_transform(X_scaled)

print(f"  ✅ t-SNE completado.")
print(f"  KL Divergence final: {tsne.kl_divergence_:.4f}  (menor = mejor)")

# ============================================================
# PASO 5: VISUALIZACIONES
# ============================================================

print(f"\n{'='*60}")
print("  PASO 5 — GENERANDO VISUALIZACIONES")
print(f"{'='*60}")

fig = plt.figure(figsize=(20, 18))
fig.patch.set_facecolor('#0F1117')
gs  = GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.35)

colores_puntos = [COLORS[c] for c in y]

# ── Gráfico 1: Varianza Explicada Acumulada (Codo PCA) ───────
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor('#1A1D27')
componentes = np.arange(1, len(varianza_acumulada) + 1)
ax1.plot(componentes, varianza_acumulada * 100,
         color='#4FC3F7', linewidth=2.5, marker='o', markersize=4)
ax1.axhline(y=95, color='#FF7043', linestyle='--', linewidth=1.5, label='95% varianza')
ax1.axvline(x=n_componentes_95, color='#FFD54F', linestyle='--', linewidth=1.5,
            label=f'{n_componentes_95} componentes')
ax1.fill_between(componentes, varianza_acumulada * 100,
                 alpha=0.15, color='#4FC3F7')
ax1.set_xlabel('Número de Componentes', color='#CCCCCC', fontsize=11)
ax1.set_ylabel('Varianza Explicada Acumulada (%)', color='#CCCCCC', fontsize=11)
ax1.set_title('Varianza Explicada Acumulada — PCA\n(Criterio del Codo)', 
              color='white', fontsize=13, fontweight='bold', pad=12)
ax1.tick_params(colors='#AAAAAA')
ax1.spines[:].set_color('#333344')
ax1.legend(facecolor='#1A1D27', labelcolor='white', fontsize=10)
ax1.grid(True, alpha=0.15, color='#AAAAAA')

# ── Gráfico 2: Varianza por componente (barras) ───────────────
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor('#1A1D27')
n_barras = 15
colores_barras = ['#E63946' if i < n_componentes_95 else '#555566'
                  for i in range(n_barras)]
ax2.bar(range(1, n_barras + 1),
        pca_full.explained_variance_ratio_[:n_barras] * 100,
        color=colores_barras, edgecolor='#0F1117', linewidth=0.8)
ax2.set_xlabel('Componente Principal', color='#CCCCCC', fontsize=11)
ax2.set_ylabel('Varianza Explicada (%)', color='#CCCCCC', fontsize=11)
ax2.set_title('Varianza Explicada por Componente\n(primeras 15 PCs)',
              color='white', fontsize=13, fontweight='bold', pad=12)
ax2.tick_params(colors='#AAAAAA')
ax2.spines[:].set_color('#333344')
ax2.grid(True, alpha=0.15, color='#AAAAAA', axis='y')
parche_rojo  = mpatches.Patch(color='#E63946', label=f'Retenidos (PC1–{n_componentes_95})')
parche_gris  = mpatches.Patch(color='#555566', label='Descartados')
ax2.legend(handles=[parche_rojo, parche_gris], facecolor='#1A1D27',
           labelcolor='white', fontsize=10)

# ── Gráfico 3: PCA 2D ────────────────────────────────────────
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_facecolor('#1A1D27')
for clase, color, label in zip([0, 1], COLORS, LABELS):
    mask = y == clase
    ax3.scatter(X_pca[mask, 0], X_pca[mask, 1],
                c=color, alpha=0.75, s=35, label=label,
                edgecolors='none')
ax3.set_xlabel(f'PC1 ({var_pc1:.1f}% varianza)', color='#CCCCCC', fontsize=11)
ax3.set_ylabel(f'PC2 ({var_pc2:.1f}% varianza)', color='#CCCCCC', fontsize=11)
ax3.set_title(f'PCA — Proyección 2D\n(varianza total retenida: {var_total_2d:.1f}%)',
              color='white', fontsize=13, fontweight='bold', pad=12)
ax3.tick_params(colors='#AAAAAA')
ax3.spines[:].set_color('#333344')
ax3.legend(facecolor='#1A1D27', labelcolor='white', fontsize=11, markerscale=1.5)
ax3.grid(True, alpha=0.12, color='#AAAAAA')

# ── Gráfico 4: t-SNE 2D ──────────────────────────────────────
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor('#1A1D27')
for clase, color, label in zip([0, 1], COLORS, LABELS):
    mask = y == clase
    ax4.scatter(X_tsne[mask, 0], X_tsne[mask, 1],
                c=color, alpha=0.75, s=35, label=label,
                edgecolors='none')
ax4.set_xlabel('Dimensión t-SNE 1', color='#CCCCCC', fontsize=11)
ax4.set_ylabel('Dimensión t-SNE 2', color='#CCCCCC', fontsize=11)
ax4.set_title(f't-SNE — Proyección 2D\n(perplexity={PERPLEXITY}, n_iter={N_ITER})',
              color='white', fontsize=13, fontweight='bold', pad=12)
ax4.tick_params(colors='#AAAAAA')
ax4.spines[:].set_color('#333344')
ax4.legend(facecolor='#1A1D27', labelcolor='white', fontsize=11, markerscale=1.5)
ax4.grid(True, alpha=0.12, color='#AAAAAA')

# ── Gráfico 5: Biplot de Cargas PCA ─────────────────────────
ax5 = fig.add_subplot(gs[2, :])
ax5.set_facecolor('#1A1D27')
# Scatter de puntos (fondo)
for clase, color, label in zip([0, 1], COLORS, LABELS):
    mask = y == clase
    ax5.scatter(X_pca[mask, 0], X_pca[mask, 1],
                c=color, alpha=0.35, s=20, label=label)
# Flechas de las 8 variables más importantes
top_features_idx = cargas['PC1'].abs().sort_values(ascending=False).head(8).index
scale = 4.5
for feat in top_features_idx:
    pc1_val = cargas.loc[feat, 'PC1'] * scale
    pc2_val = cargas.loc[feat, 'PC2'] * scale
    ax5.annotate('', xy=(pc1_val, pc2_val), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='#FFD54F',
                                 lw=1.5, mutation_scale=12))
    ax5.text(pc1_val * 1.08, pc2_val * 1.08,
             feat.replace(' (mean)', '').replace(' (worst)', '*'),
             fontsize=7.5, color='#FFD54F', ha='center', va='center')
ax5.set_xlabel(f'PC1 ({var_pc1:.1f}%)', color='#CCCCCC', fontsize=11)
ax5.set_ylabel(f'PC2 ({var_pc2:.1f}%)', color='#CCCCCC', fontsize=11)
ax5.set_title('Biplot PCA — Puntos + Cargas Factoriales (top 8 variables)',
              color='white', fontsize=13, fontweight='bold', pad=12)
ax5.tick_params(colors='#AAAAAA')
ax5.spines[:].set_color('#333344')
ax5.legend(facecolor='#1A1D27', labelcolor='white', fontsize=11, markerscale=1.5,
           loc='upper right')
ax5.axhline(0, color='#555566', linewidth=0.8)
ax5.axvline(0, color='#555566', linewidth=0.8)
ax5.grid(True, alpha=0.10, color='#AAAAAA')

# Título general
fig.suptitle(
    'Análisis de Reducción Dimensional — DataMed Analytics\n'
    'Dataset: Breast Cancer Wisconsin  |  n=569 muestras, 30 variables',
    color='white', fontsize=16, fontweight='bold', y=0.98
)

plt.savefig('/home/claude/visualizaciones_reduccion_dimensional.png',
            dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print("  ✅ Visualizaciones guardadas.")

# ============================================================
# PASO 5: ANÁLISIS COMPARATIVO
# ============================================================

print(f"\n{'='*60}")
print("  PASO 5 — ANÁLISIS COMPARATIVO: PCA vs t-SNE")
print(f"{'='*60}")

print("""
  ┌─────────────────────────────────────────────────────────┐
  │              COMPARATIVA PCA vs t-SNE                   │
  ├──────────────────┬──────────────────┬───────────────────┤
  │ Criterio         │ PCA              │ t-SNE             │
  ├──────────────────┼──────────────────┼───────────────────┤
  │ Tipo             │ Lineal           │ No lineal         │
  │ Varianza retenida│ Cuantificable    │ No aplica         │
  │ Separación visual│ Moderada         │ Alta              │
  │ Interpretabilidad│ Alta (cargas)    │ Baja              │
  │ Pipeline ML      │ ✅ Sí            │ ❌ No recomendado │
  │ Reproducibilidad │ Alta             │ Depende de seed   │
  │ Velocidad        │ Rápida           │ Lenta (O(n²))     │
  │ Preserva         │ Estructura global│ Estructura local  │
  └──────────────────┴──────────────────┴───────────────────┘
""")

print("  CONCLUSIONES:")
print(f"""
  1. VISUALIZACIÓN DE CLÚSTERES:
     → t-SNE produce una separación visual más clara y compacta
       entre tumores malignos y benignos, al preservar la
       estructura local del espacio de alta dimensión.
     → PCA, siendo lineal, muestra separación moderada pero
       deja más superposición entre clases.

  2. PIPELINE PREDICTIVO:
     → PCA es la técnica recomendada para integrarse en un
       pipeline de modelado predictivo porque:
         • Es determinista y reproducible
         • Permite transformar nuevos datos (transform())
         • Conserva información cuantificable (varianza)
         • Con {n_componentes_95} componentes retiene el 95% de la varianza
           reduciendo de {X.shape[1]} a {n_componentes_95} dimensiones
     → t-SNE NO debe usarse en pipelines: no puede transformar
       nuevos datos (solo trabaja en el conjunto de entrenamiento).

  RECOMENDACIÓN FINAL:
     • Usar PCA (n_components={n_componentes_95}) en el pipeline de clasificación
     • Usar t-SNE exclusivamente para visualización exploratoria
     • Combinar ambas: PCA para reducir ruido → t-SNE para visualizar
""")

# ============================================================
# RESUMEN FINAL
# ============================================================
print(f"{'='*60}")
print("  RESUMEN DE RESULTADOS")
print(f"{'='*60}")
print(f"""
  Dataset            : Breast Cancer Wisconsin
  Muestras           : {X.shape[0]}
  Variables originales: {X.shape[1]}

  PCA
    Componentes para 95% var : {n_componentes_95}
    Reducción lograda        : {X.shape[1]} → {n_componentes_95} dimensiones
    Var. retenida en 2D      : {var_total_2d:.1f}%

  t-SNE
    Parámetros               : perplexity={PERPLEXITY}, lr={LEARNING_RATE}, iter={N_ITER}
    KL Divergence            : {tsne.kl_divergence_:.4f}

  Archivos generados:
    📊 visualizaciones_reduccion_dimensional.png
""")
print("  ✅ Análisis completo finalizado.")
