"""
========================================================
Predicción inteligente de gasto en clientes e-commerce
Módulo 6: Aprendizaje de Máquina Supervisado - Alkemy
========================================================
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import os

from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

os.makedirs('outputs', exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid')
COLORS = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B1F2B', '#44BBA4']

print("=" * 60)
print("PROYECTO: Predicción de Gasto en Clientes E-commerce")
print("=" * 60)

# ── L1: FUNDAMENTOS ───────────────────────────────────
print("\n[L1] Tipo de problema: REGRESIÓN SUPERVISADA")
print("Variable objetivo continua: monto_compra_promedio")

# ── CARGA ─────────────────────────────────────────────
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'dataset_ecommerce.csv'))
print(f"Dataset cargado: {df.shape}")

# ── L3: PREPROCESAMIENTO ──────────────────────────────
print("\n[L3] Preprocesamiento")
print(f"Nulos antes: {df.isnull().sum().sum()}")

# Imputación correcta (compatible con Copy-on-Write)
for col in ['tiempo_promedio_sesion_min', 'calificacion_promedio_dada', 'dias_desde_ultima_compra']:
    df[col] = df[col].fillna(df[col].median())

print(f"Nulos después: {df.isnull().sum().sum()}")

# Outliers IQR en target
Q1, Q3 = df['monto_compra_promedio'].quantile([0.25, 0.75])
IQR = Q3 - Q1
before = len(df)
df = df[~((df['monto_compra_promedio'] < Q1-1.5*IQR) | (df['monto_compra_promedio'] > Q3+1.5*IQR))].reset_index(drop=True)
print(f"Outliers eliminados: {before - len(df)}")

# Codificación categórica
cat_cols = ['genero', 'region', 'dispositivo', 'categoria_preferida', 'nivel_membresia']
df_enc = df.copy()
le = LabelEncoder()
for col in cat_cols:
    df_enc[col] = le.fit_transform(df_enc[col])

X = df_enc.drop('monto_compra_promedio', axis=1)
y = df_enc['monto_compra_promedio']

print(f"\nFeatures: {X.shape[1]} | Target media: ${y.mean():.2f} ± ${y.std():.2f}")
print(f"Nulos en X: {X.isnull().sum().sum()}")

# Split y escalado
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)
print(f"Train: {X_train.shape[0]} | Test: {X_test.shape[0]}")

# ── L4: REGRESIONES ───────────────────────────────────
print("\n[L4] Regresiones")
lr = LinearRegression()
lr.fit(X_train_sc, y_train)
y_pred_lr = lr.predict(X_test_sc)
mae_lr  = mean_absolute_error(y_test, y_pred_lr)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
r2_lr   = r2_score(y_test, y_pred_lr)
print(f"Lineal   → MAE:{mae_lr:.2f} RMSE:{rmse_lr:.2f} R²:{r2_lr:.4f}")

poly = PolynomialFeatures(degree=2, include_bias=False)
X_tr_poly = poly.fit_transform(X_train_sc)
X_ts_poly = poly.transform(X_test_sc)
lr_poly = LinearRegression()
lr_poly.fit(X_tr_poly, y_train)
y_pred_poly = lr_poly.predict(X_ts_poly)
mae_poly  = mean_absolute_error(y_test, y_pred_poly)
rmse_poly = np.sqrt(mean_squared_error(y_test, y_pred_poly))
r2_poly   = r2_score(y_test, y_pred_poly)
print(f"Polinomial(g=2) → MAE:{mae_poly:.2f} RMSE:{rmse_poly:.2f} R²:{r2_poly:.4f}")

coef_df = pd.DataFrame({'Feature': X.columns, 'Coef': np.abs(lr.coef_)}).sort_values('Coef', ascending=False)
print("Top 5 variables (Reg. Lineal):", coef_df.head(5)['Feature'].tolist())

# ── L5: KNN ───────────────────────────────────────────
print("\n[L5] KNN Regressor")
knn = KNeighborsRegressor(n_neighbors=7)
knn.fit(X_train_sc, y_train)
y_pred_knn = knn.predict(X_test_sc)
mae_knn  = mean_absolute_error(y_test, y_pred_knn)
rmse_knn = np.sqrt(mean_squared_error(y_test, y_pred_knn))
r2_knn   = r2_score(y_test, y_pred_knn)
print(f"KNN(k=7) → MAE:{mae_knn:.2f} RMSE:{rmse_knn:.2f} R²:{r2_knn:.4f}")

# ── L2: VALIDACIÓN CRUZADA ────────────────────────────
print("\n[L2] Validación Cruzada K-Folds (k=5)")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_lr  = cross_val_score(LinearRegression(), X_train_sc, y_train, cv=kf, scoring='r2')
cv_knn = cross_val_score(KNeighborsRegressor(n_neighbors=7), X_train_sc, y_train, cv=kf, scoring='r2')
print(f"CV R² Lineal: {cv_lr.mean():.4f} ± {cv_lr.std():.4f}")
print(f"CV R² KNN:   {cv_knn.mean():.4f} ± {cv_knn.std():.4f}")

# ── L7: RIDGE Y LASSO ─────────────────────────────────
print("\n[L7] Ridge y Lasso con GridSearchCV")
ridge_gs = GridSearchCV(Ridge(), {'alpha': [0.01,0.1,1,10,100]}, cv=5, scoring='r2')
ridge_gs.fit(X_train_sc, y_train)
y_pred_ridge = ridge_gs.best_estimator_.predict(X_test_sc)
mae_ridge  = mean_absolute_error(y_test, y_pred_ridge)
rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
r2_ridge   = r2_score(y_test, y_pred_ridge)
print(f"Ridge(alpha={ridge_gs.best_params_['alpha']}) → MAE:{mae_ridge:.2f} RMSE:{rmse_ridge:.2f} R²:{r2_ridge:.4f}")

lasso_gs = GridSearchCV(Lasso(max_iter=5000), {'alpha': [0.01,0.1,1,10]}, cv=5, scoring='r2')
lasso_gs.fit(X_train_sc, y_train)
y_pred_lasso = lasso_gs.best_estimator_.predict(X_test_sc)
mae_lasso  = mean_absolute_error(y_test, y_pred_lasso)
rmse_lasso = np.sqrt(mean_squared_error(y_test, y_pred_lasso))
r2_lasso   = r2_score(y_test, y_pred_lasso)
print(f"Lasso(alpha={lasso_gs.best_params_['alpha']}) → MAE:{mae_lasso:.2f} RMSE:{rmse_lasso:.2f} R²:{r2_lasso:.4f}")

# ── L8: GRADIENT BOOSTING ─────────────────────────────
print("\n[L8] Gradient Boosting")
gb_gs = GridSearchCV(
    GradientBoostingRegressor(random_state=42),
    {'n_estimators':[100,200], 'learning_rate':[0.05,0.1], 'max_depth':[3,4]},
    cv=3, scoring='r2', n_jobs=-1
)
gb_gs.fit(X_train_sc, y_train)
best_gb = gb_gs.best_estimator_
y_pred_gb = best_gb.predict(X_test_sc)
mae_gb  = mean_absolute_error(y_test, y_pred_gb)
rmse_gb = np.sqrt(mean_squared_error(y_test, y_pred_gb))
r2_gb   = r2_score(y_test, y_pred_gb)
print(f"GB{gb_gs.best_params_} → MAE:{mae_gb:.2f} RMSE:{rmse_gb:.2f} R²:{r2_gb:.4f}")

# ── L6: TABLA DE MÉTRICAS ─────────────────────────────
print("\n" + "=" * 65)
results = pd.DataFrame({
    'Modelo':  ['Reg. Lineal','Reg. Polinomial','KNN (k=7)','Ridge','Lasso','Gradient Boosting'],
    'MAE':     [mae_lr, mae_poly, mae_knn, mae_ridge, mae_lasso, mae_gb],
    'RMSE':    [rmse_lr, rmse_poly, rmse_knn, rmse_ridge, rmse_lasso, rmse_gb],
    'R2':      [r2_lr, r2_poly, r2_knn, r2_ridge, r2_lasso, r2_gb]
}).round(4)
print(results.to_string(index=False))
best_idx = results['R2'].idxmax()
print(f"\n✅ Mejor modelo: {results.loc[best_idx, 'Modelo']} (R²={results.loc[best_idx,'R2']})")
results.to_csv('outputs/tabla_metricas.csv', index=False)

# ─── VISUALIZACIONES ──────────────────────────────────
print("\nGenerando visualizaciones...")

# Fig 1: EDA
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Análisis Exploratorio del Dataset', fontsize=14, fontweight='bold')
axes[0].hist(df['monto_compra_promedio'], bins=40, color=COLORS[0], edgecolor='white', alpha=0.85)
axes[0].axvline(df['monto_compra_promedio'].mean(), color=COLORS[2], linestyle='--', linewidth=2,
                label=f"Media: ${df['monto_compra_promedio'].mean():.0f}")
axes[0].set_title('Distribución del Monto de Compra')
axes[0].set_xlabel('Monto ($)'); axes[0].set_ylabel('Frecuencia'); axes[0].legend()
num_cols = df_enc.select_dtypes(include=np.number).columns.tolist()
corr = df_enc[num_cols].corr()['monto_compra_promedio'].drop('monto_compra_promedio').sort_values()
colors_bar = [COLORS[2] if v > 0 else COLORS[3] for v in corr.values]
axes[1].barh(corr.index, corr.values, color=colors_bar, alpha=0.85)
axes[1].axvline(0, color='black', linewidth=0.8)
axes[1].set_title('Correlación con Monto de Compra'); axes[1].set_xlabel('Pearson r')
plt.tight_layout(); plt.savefig('outputs/fig1_eda.png', dpi=150, bbox_inches='tight'); plt.close()

# Fig 2: Métricas comparativas
fig, axes = plt.subplots(1, 3, figsize=(17, 5))
fig.suptitle('Comparación de Métricas por Modelo', fontsize=14, fontweight='bold')
for ax, metric in zip(axes, ['MAE', 'RMSE', 'R2']):
    bars = ax.bar(results['Modelo'], results[metric], color=COLORS[:6], alpha=0.85, edgecolor='white')
    ax.set_title(metric); ax.set_ylabel(metric); ax.tick_params(axis='x', rotation=45)
    for bar, val in zip(bars, results[metric]):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()*1.01, f'{val:.3f}',
                ha='center', va='bottom', fontsize=8)
    if metric == 'R2': ax.set_ylim(0, 1.1)
plt.tight_layout(); plt.savefig('outputs/fig2_metricas.png', dpi=150, bbox_inches='tight'); plt.close()

# Fig 3: Real vs Predicho
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Real vs Predicho', fontsize=14, fontweight='bold')
for ax, (name, yp) in zip(axes, [('Regresión Lineal', y_pred_lr), ('Gradient Boosting', y_pred_gb)]):
    ax.scatter(y_test, yp, alpha=0.35, color=COLORS[0], s=20)
    lims = [min(y_test.min(), yp.min()), max(y_test.max(), yp.max())]
    ax.plot(lims, lims, 'r--', linewidth=1.5, label='Perfecta')
    ax.set_xlabel('Real ($)'); ax.set_ylabel('Predicho ($)'); ax.set_title(name); ax.legend()
plt.tight_layout(); plt.savefig('outputs/fig3_real_vs_predicho.png', dpi=150, bbox_inches='tight'); plt.close()

# Fig 4: Feature importance + R² evolution
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle('Importancia de Variables y Evolución del R²', fontsize=14, fontweight='bold')
fi = pd.Series(best_gb.feature_importances_, index=X.columns).sort_values()
fi.tail(12).plot(kind='barh', ax=axes[0], color=COLORS[0], alpha=0.85)
axes[0].set_title('Feature Importance - Gradient Boosting'); axes[0].set_xlabel('Importancia')
axes[1].plot(results['Modelo'], results['R2'], 'o-', color=COLORS[0], linewidth=2, markersize=9)
axes[1].axhline(0.90, color=COLORS[3], linestyle='--', alpha=0.7, label='R²=0.90')
axes[1].set_title('Evolución R² por Modelo'); axes[1].set_ylabel('R²')
axes[1].tick_params(axis='x', rotation=35); axes[1].legend(); axes[1].set_ylim(0, 1.1)
plt.tight_layout(); plt.savefig('outputs/fig4_importancia.png', dpi=150, bbox_inches='tight'); plt.close()

# Fig 5: Residuos
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Análisis de Residuos — Gradient Boosting', fontsize=14, fontweight='bold')
residuos = y_test.values - y_pred_gb
axes[0].scatter(y_pred_gb, residuos, alpha=0.35, color=COLORS[0], s=20)
axes[0].axhline(0, color=COLORS[3], linestyle='--', linewidth=1.5)
axes[0].set_xlabel('Predichos ($)'); axes[0].set_ylabel('Residuos'); axes[0].set_title('Residuos vs Predichos')
axes[1].hist(residuos, bins=35, color=COLORS[1], edgecolor='white', alpha=0.85)
axes[1].axvline(0, color=COLORS[3], linestyle='--', linewidth=1.5)
axes[1].set_title('Distribución de Residuos'); axes[1].set_xlabel('Error ($)')
plt.tight_layout(); plt.savefig('outputs/fig5_residuos.png', dpi=150, bbox_inches='tight'); plt.close()

print("✅ 5 visualizaciones guardadas en outputs/")
print(f"\n🏆 Modelo recomendado: {results.loc[best_idx,'Modelo']}")
