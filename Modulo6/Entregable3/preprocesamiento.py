# =============================================================================
# RetailData Analytics - Preprocesamiento y Escalamiento de Datos
# Lección 3: Fundamentos del Aprendizaje de Máquina
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer

# ─── 1. DATASET ORIGINAL ─────────────────────────────────────────────────────
print("=" * 60)
print("PREPROCESAMIENTO Y ESCALAMIENTO DE DATOS - RetailData Analytics")
print("=" * 60)

data = {
    'ID':       [1, 2, 3, 4],
    'Edad':     [25, 45, 30, 40],
    'Ciudad':   ['Madrid', 'Sevilla', 'Madrid', 'Barcelona'],
    'Ingresos': [30000, 50000, np.nan, 40000]
}
df = pd.DataFrame(data)

print("\n[1] Dataset original:")
print(df.to_string(index=False))
print(f"\nValores nulos por columna:\n{df.isnull().sum()}")

# ─── 2. IMPUTACIÓN DE VALORES NULOS ──────────────────────────────────────────
print("\n" + "─" * 60)
print("[2] Imputación de valores nulos (media de Ingresos)")

imputer = SimpleImputer(strategy='mean')
df['Ingresos'] = imputer.fit_transform(df[['Ingresos']])
media_ingresos = df['Ingresos'].mean()
print(f"    Media calculada: ${media_ingresos:,.2f}")
print(f"    Ingresos después de imputación: {df['Ingresos'].tolist()}")

# ─── 3. LABEL ENCODING ───────────────────────────────────────────────────────
print("\n" + "─" * 60)
print("[3] Label Encoding para columna Ciudad")

le = LabelEncoder()
df['Ciudad_LabelEnc'] = le.fit_transform(df['Ciudad'])
mapping = dict(zip(le.classes_, le.transform(le.classes_)))
print(f"    Mapeo: {mapping}")
print(df[['Ciudad', 'Ciudad_LabelEnc']].to_string(index=False))

# ─── 4. ONE-HOT ENCODING ─────────────────────────────────────────────────────
print("\n" + "─" * 60)
print("[4] One-Hot Encoding para columna Ciudad")

ohe_df = pd.get_dummies(df['Ciudad'], prefix='Ciudad')
df_ohe = pd.concat([df, ohe_df], axis=1)
print(df_ohe[['Ciudad'] + list(ohe_df.columns)].to_string(index=False))

# ─── 5. VARIABLES DUMMY ───────────────────────────────────────────────────────
print("\n" + "─" * 60)
print("[5] Variables Dummy (drop_first=True para evitar multicolinealidad)")

dummy_df = pd.get_dummies(df['Ciudad'], prefix='Ciudad', drop_first=True)
df_dummy = pd.concat([df[['ID', 'Edad', 'Ciudad', 'Ingresos']], dummy_df], axis=1)
print(df_dummy.to_string(index=False))
print("    Referencia omitida: Barcelona")

# ─── 6. ESCALAMIENTO: MIN-MAX ─────────────────────────────────────────────────
print("\n" + "─" * 60)
print("[6] Normalización Min-Max (rango [0, 1])")

scaler_mm = MinMaxScaler()
cols_escalar = ['Edad', 'Ingresos']
mm_scaled = scaler_mm.fit_transform(df[cols_escalar])
df_minmax = pd.DataFrame(mm_scaled, columns=[f'{c}_MinMax' for c in cols_escalar])
print(df_minmax.round(4).to_string(index=False))

# ─── 7. ESCALAMIENTO: Z-SCORE ─────────────────────────────────────────────────
print("\n" + "─" * 60)
print("[7] Estandarización Z-Score (media=0, std=1)")

scaler_zs = StandardScaler()
zs_scaled = scaler_zs.fit_transform(df[cols_escalar])
df_zscore = pd.DataFrame(zs_scaled, columns=[f'{c}_ZScore' for c in cols_escalar])
print(df_zscore.round(4).to_string(index=False))

# ─── 8. DATASET FINAL COMPLETO ────────────────────────────────────────────────
print("\n" + "─" * 60)
print("[8] Dataset final preprocesado:")

df_final = pd.concat([
    df[['ID', 'Edad', 'Ciudad', 'Ingresos', 'Ciudad_LabelEnc']],
    ohe_df,
    df_minmax,
    df_zscore
], axis=1)

print(df_final.round(4).to_string(index=False))

# ─── 9. VISUALIZACIÓN ────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 10))
fig.suptitle('Visualización de Datos Escalados — RetailData Analytics', 
             fontsize=14, fontweight='bold', y=0.98)

gs = gridspec.GridSpec(2, 2, hspace=0.45, wspace=0.35)

colors_original = ['#2E74B5', '#1F4E79', '#4A9CC7', '#1F4E79']
colors_mm       = ['#27AE60', '#1E8449', '#52BE80', '#1E8449']
colors_zs       = ['#E74C3C', '#C0392B', '#EC7063', '#C0392B']

ids = df_final['ID'].astype(str)
x   = np.arange(len(ids))
w   = 0.35

# -- Subplot 1: Edad original vs Min-Max
ax1 = fig.add_subplot(gs[0, 0])
ax1.bar(x - w/2, df_final['Edad'], w, label='Edad original', color=colors_original, alpha=0.85)
ax1.bar(x + w/2, df_final['Edad_MinMax'], w, label='Min-Max [0,1]', color=colors_mm, alpha=0.85)
ax1.set_title('Edad: Original vs Min-Max', fontweight='bold')
ax1.set_xticks(x); ax1.set_xticklabels([f'ID {i}' for i in ids])
ax1.legend(fontsize=8); ax1.set_ylabel('Valor'); ax1.grid(axis='y', alpha=0.3)

# -- Subplot 2: Ingresos original vs Min-Max
ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(x - w/2, df_final['Ingresos'] / 1000, w, label='Ingresos (miles)', color=colors_original, alpha=0.85)
ax2.bar(x + w/2, df_final['Ingresos_MinMax'], w, label='Min-Max [0,1]', color=colors_mm, alpha=0.85)
ax2.set_title('Ingresos: Original vs Min-Max', fontweight='bold')
ax2.set_xticks(x); ax2.set_xticklabels([f'ID {i}' for i in ids])
ax2.legend(fontsize=8); ax2.set_ylabel('Valor (miles USD / escala)'); ax2.grid(axis='y', alpha=0.3)

# -- Subplot 3: Edad Z-Score
ax3 = fig.add_subplot(gs[1, 0])
bars = ax3.bar(x, df_final['Edad_ZScore'], color=colors_zs, alpha=0.85, edgecolor='white')
ax3.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax3.set_title('Edad: Estandarización Z-Score', fontweight='bold')
ax3.set_xticks(x); ax3.set_xticklabels([f'ID {i}' for i in ids])
ax3.set_ylabel('Z-Score'); ax3.grid(axis='y', alpha=0.3)
for bar, val in zip(bars, df_final['Edad_ZScore']):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
             f'{val:.2f}', ha='center', va='bottom', fontsize=9)

# -- Subplot 4: Ingresos Z-Score
ax4 = fig.add_subplot(gs[1, 1])
bars2 = ax4.bar(x, df_final['Ingresos_ZScore'], color=colors_zs, alpha=0.85, edgecolor='white')
ax4.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax4.set_title('Ingresos: Estandarización Z-Score', fontweight='bold')
ax4.set_xticks(x); ax4.set_xticklabels([f'ID {i}' for i in ids])
ax4.set_ylabel('Z-Score'); ax4.grid(axis='y', alpha=0.3)
for bar, val in zip(bars2, df_final['Ingresos_ZScore']):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
             f'{val:.2f}', ha='center', va='bottom', fontsize=9)

plt.savefig('/home/claude/visualizacion_escalado.png', dpi=150, bbox_inches='tight')
print("\n[9] Visualización guardada: visualizacion_escalado.png")

# ─── 10. EXPORTAR CSV Y EXCEL ─────────────────────────────────────────────────
df_final.round(4).to_csv('/home/claude/datos_preprocesados.csv', index=False)
print("[10] Dataset exportado: datos_preprocesados.csv")
print("\n" + "=" * 60)
print("Preprocesamiento completado exitosamente.")
print("=" * 60)
