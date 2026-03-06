# =============================================================================
# AutoPredict S.A. — Métricas de Desempeño de Regresión Lineal
# Lección 6: Métricas de desempeño de un algoritmo de regresión
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, LeaveOneOut, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# ─── 1. DATASET ──────────────────────────────────────────────────────────────
print("=" * 65)
print("  AutoPredict S.A. — Análisis de Métricas de Regresión Lineal")
print("=" * 65)

data = {
    'ID':            [1,     2,     3,     4    ],
    'Antiguedad':    [5,     3,     7,     2    ],
    'Kilometraje':   [50000, 30000, 70000, 25000],
    'Puertas':       [4,     2,     4,     2    ],
    'Precio':        [12000, 15000, 9000,  16000]
}
df = pd.DataFrame(data)

print("\n[1] Dataset original:")
print(df.to_string(index=False))

# ─── 2. VARIABLES ─────────────────────────────────────────────────────────────
X = df[['Antiguedad', 'Kilometraje', 'Puertas']]
y = df['Precio']

print(f"\n[2] Variables predictoras: {list(X.columns)}")
print(f"    Variable objetivo: Precio (USD)")

# ─── 3. DIVISIÓN TRAIN/TEST ───────────────────────────────────────────────────
# Con solo 4 registros, 80/20 deja 3 train y 1 test.
# Se usa random_state=42 para reproducibilidad.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
print(f"\n[3] División 80/20:")
print(f"    Entrenamiento: {len(X_train)} registros  — IDs: {list(df.loc[X_train.index, 'ID'])}")
print(f"    Prueba:        {len(X_test)}  registro   — IDs: {list(df.loc[X_test.index,  'ID'])}")

# ─── 4. ENTRENAMIENTO Y PREDICCIÓN ───────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"\n[4] Coeficientes del modelo:")
for feat, coef in zip(X.columns, model.coef_):
    print(f"    {feat:15s}: {coef:+.4f}")
print(f"    {'Intercepto':15s}: {model.intercept_:+.4f}")

print(f"\n    Predicciones sobre conjunto de prueba:")
for real, pred, idx in zip(y_test, y_pred, y_test.index):
    print(f"    ID={df.loc[idx,'ID']} | Real: ${real:,}  | Predicho: ${pred:,.2f}  | Error: ${abs(real-pred):,.2f}")

# ─── 5. MÉTRICAS ─────────────────────────────────────────────────────────────
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n" + "─" * 65)
print("[5] Métricas de desempeño (conjunto de prueba):")
print(f"    MAE  (Error Absoluto Medio)        : ${mae:,.2f}")
print(f"    MSE  (Error Cuadrático Medio)      : ${mse:,.2f}")
print(f"    RMSE (Raíz del Error Cuadrático)   : ${rmse:,.2f}")
print(f"    R²   (Coeficiente de Determinación): {r2:.4f}  ({r2*100:.2f}%)")

# ─── 6. VALIDACIÓN CRUZADA LOO (más robusta con n=4) ─────────────────────────
loo = LeaveOneOut()
cv_scores = cross_val_score(LinearRegression(), X, y,
                             cv=loo, scoring='neg_mean_absolute_error')
mae_cv = -cv_scores.mean()
print(f"\n    MAE — Validación Cruzada LOO (más robusta con n=4): ${mae_cv:,.2f}")

# ─── 7. ANÁLISIS ─────────────────────────────────────────────────────────────
print("\n" + "─" * 65)
print("[6] Análisis de resultados:")
print(f"""
    Con solo 4 registros, el modelo tiene capacidad limitada.
    • MAE  = ${mae:,.0f}: el error promedio es de ${mae:,.0f} por vehículo.
    • RMSE = ${rmse:,.0f}: penaliza más los errores grandes.
    • R²   = {r2:.4f}: el modelo explica el {r2*100:.1f}% de la varianza.

    Con n=4, la métrica de LOO (${mae_cv:,.0f}) es más representativa
    del desempeño real que el split 80/20 con 1 solo punto de prueba.
""")

# ─── 8. COMPARACIÓN CON MODELOS ALTERNATIVOS (LOO) ───────────────────────────
models = {
    'Regresión Lineal':        LinearRegression(),
    'Random Forest':           RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting':       GradientBoostingRegressor(n_estimators=50, random_state=42),
}
print("[8] Comparación de modelos (MAE — LOO cross-validation):")
model_maes = {}
for name, m in models.items():
    scores = cross_val_score(m, X, y, cv=loo, scoring='neg_mean_absolute_error')
    mae_m = -scores.mean()
    model_maes[name] = mae_m
    print(f"    {name:25s}: ${mae_m:,.2f}")

# ─── 9. VISUALIZACIÓN ────────────────────────────────────────────────────────
# Predecir sobre todos los registros para la visualización comparativa
y_all_pred = model.predict(X)

fig = plt.figure(figsize=(14, 9))
fig.suptitle('AutoPredict S.A. — Análisis de Métricas de Regresión Lineal',
             fontsize=13, fontweight='bold', y=0.98)
gs = gridspec.GridSpec(2, 2, hspace=0.45, wspace=0.38)

ids   = df['ID'].astype(str)
x_pos = np.arange(len(ids))
w     = 0.35
BLUE  = '#2E74B5'
GREEN = '#27AE60'
RED   = '#E74C3C'
GRAY  = '#85929E'

# ── Panel 1: Precios reales vs predichos ──
ax1 = fig.add_subplot(gs[0, 0])
bars1 = ax1.bar(x_pos - w/2, df['Precio'], w, label='Real', color=BLUE, alpha=0.88)
bars2 = ax1.bar(x_pos + w/2, y_all_pred,  w, label='Predicho', color=GREEN, alpha=0.88)
for b, v in zip(bars1, df['Precio']):
    ax1.text(b.get_x()+b.get_width()/2, v+150, f'${v/1000:.0f}k', ha='center', fontsize=8.5, color='#1A1A1A')
for b, v in zip(bars2, y_all_pred):
    ax1.text(b.get_x()+b.get_width()/2, v+150, f'${v/1000:.1f}k', ha='center', fontsize=8.5, color='#1E5631')
ax1.set_title('Precios Reales vs. Predichos', fontweight='bold', fontsize=10)
ax1.set_xticks(x_pos); ax1.set_xticklabels([f'ID {i}' for i in ids])
ax1.set_ylabel('Precio (USD)'); ax1.legend(fontsize=8.5)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'${v:,.0f}'))
ax1.grid(axis='y', alpha=0.3)

# ── Panel 2: Error absoluto por vehículo ──
ax2 = fig.add_subplot(gs[0, 1])
errors = np.abs(df['Precio'].values - y_all_pred)
bar_colors = [RED if e > mae else GREEN for e in errors]
bars3 = ax2.bar(x_pos, errors, color=bar_colors, alpha=0.85, edgecolor='white')
ax2.axhline(mae, color=BLUE, linestyle='--', linewidth=1.5, label=f'MAE = ${mae:,.0f}')
for b, v in zip(bars3, errors):
    ax2.text(b.get_x()+b.get_width()/2, v+30, f'${v:,.0f}', ha='center', fontsize=8.5)
ax2.set_title('Error Absoluto por Vehículo', fontweight='bold', fontsize=10)
ax2.set_xticks(x_pos); ax2.set_xticklabels([f'ID {i}' for i in ids])
ax2.set_ylabel('Error Absoluto (USD)')
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'${v:,.0f}'))
ax2.legend(fontsize=8.5); ax2.grid(axis='y', alpha=0.3)

# ── Panel 3: Scatter real vs predicho ──
ax3 = fig.add_subplot(gs[1, 0])
ax3.scatter(df['Precio'], y_all_pred, s=100, color=BLUE, zorder=5, edgecolors='white', linewidths=1.5)
for i, (r, p) in enumerate(zip(df['Precio'], y_all_pred)):
    ax3.annotate(f'ID {i+1}', (r, p), textcoords="offset points",
                 xytext=(6, 4), fontsize=8.5, color='#1A1A1A')
lims = [min(df['Precio'].min(), y_all_pred.min())-500,
        max(df['Precio'].max(), y_all_pred.max())+500]
ax3.plot(lims, lims, '--', color=GRAY, linewidth=1.2, label='Predicción perfecta')
ax3.set_xlabel('Precio Real (USD)'); ax3.set_ylabel('Precio Predicho (USD)')
ax3.set_title('Real vs. Predicho — Dispersión', fontweight='bold', fontsize=10)
ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'${v/1000:.0f}k'))
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'${v/1000:.0f}k'))
ax3.legend(fontsize=8.5); ax3.grid(alpha=0.3)

# ── Panel 4: Comparación de modelos (MAE LOO) ──
ax4 = fig.add_subplot(gs[1, 1])
names = list(model_maes.keys())
values = list(model_maes.values())
colors4 = [BLUE, GREEN, RED]
bars4 = ax4.bar(names, values, color=colors4, alpha=0.85, edgecolor='white')
for b, v in zip(bars4, values):
    ax4.text(b.get_x()+b.get_width()/2, v+30, f'${v:,.0f}', ha='center', fontsize=9, fontweight='bold')
ax4.set_title('Comparación de Modelos\n(MAE — LOO Cross-Validation)', fontweight='bold', fontsize=10)
ax4.set_ylabel('MAE (USD)'); ax4.grid(axis='y', alpha=0.3)
ax4.tick_params(axis='x', labelsize=8.5)
ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_: f'${v:,.0f}'))

plt.savefig('/home/claude/grafico_regresion.png', dpi=150, bbox_inches='tight')
print("\n[9] Gráfico guardado: grafico_regresion.png")
print("=" * 65)
print("Análisis completado exitosamente.")
print("=" * 65)
