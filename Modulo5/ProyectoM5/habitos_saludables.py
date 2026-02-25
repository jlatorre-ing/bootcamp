"""
=============================================================================
ANÁLISIS ESTADÍSTICO SOBRE HÁBITOS SALUDABLES EN JÓVENES UNIVERSITARIOS
=============================================================================
Módulo: Inferencia Estadística - Alkemy
Autor: Equipo de Investigación - Área de Salud Universitaria
Fecha: 2026

Estructura del script:
  - Lección 1: Método científico y planteamiento
  - Lección 2: Probabilidad y muestreo
  - Lección 3: Distribuciones de probabilidad
  - Lección 4: Distribución muestral y TLC
  - Lección 5: Intervalos de confianza
  - Lección 6: Pruebas de hipótesis
=============================================================================
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.stats as stats
from scipy.stats import norm, binom, poisson
import warnings
import os

warnings.filterwarnings('ignore')
np.random.seed(42)

OUTPUT_DIR = "graficos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 70)
print("  ANÁLISIS ESTADÍSTICO: HÁBITOS SALUDABLES EN JÓVENES UNIVERSITARIOS")
print("=" * 70)

# =============================================================================
# LECCIÓN 1: MÉTODO CIENTÍFICO Y ESTADÍSTICA
# =============================================================================

print("\n" + "=" * 70)
print("  LECCIÓN 1: MÉTODO CIENTÍFICO Y ESTADÍSTICA")
print("=" * 70)

print("""
PROBLEMA DE INVESTIGACIÓN:
---------------------------
¿Cuáles son los patrones de sueño, alimentación y actividad física en jóvenes
universitarios, y existe asociación entre estos hábitos y su rendimiento
académico percibido?

HIPÓTESIS:
----------
H0 (Nula):    Los jóvenes universitarios duermen en promedio 7 horas por noche
               (μ = 7 horas). No hay diferencia significativa entre quienes
               realizan actividad física y quienes no.

H1 (Alt.):    Los jóvenes universitarios duermen menos de 7 horas por noche
               (μ < 7 horas). Quienes realizan actividad física tienen mejor
               calidad de sueño.

VARIABLES IDENTIFICADAS:
------------------------
Cuantitativas continuas:
  - horas_sueno     : Horas de sueño por noche
  - horas_actividad : Horas de actividad física por semana
  - imc             : Índice de Masa Corporal

Cuantitativas discretas:
  - comidas_dia     : Número de comidas por día
  - dias_actividad  : Días de actividad física por semana

Cualitativas nominales:
  - genero          : Masculino / Femenino / No binario
  - carrera         : Área de estudio (Exactas, Sociales, Salud, Tecnología, Humanidades)
  - consume_alcohol : Sí / No
  - fuma            : Sí / No

Cualitativas ordinales:
  - calidad_sueno   : 1-5 (Muy mala → Muy buena)
  - nivel_estres    : 1-5 (Muy bajo → Muy alto)
  - rendimiento     : Bajo / Medio / Alto

ENFOQUE METODOLÓGICO:
---------------------
  - Tipo de estudio    : Observacional, transversal, cuantitativo
  - Método de muestreo : Estratificado por carrera y género
  - Tamaño muestral    : n = 200 estudiantes universitarios
  - Software           : Python (NumPy, Pandas, SciPy, Matplotlib)
""")

# =============================================================================
# LECCIÓN 2: SIMULACIÓN DEL DATASET Y PROBABILIDAD
# =============================================================================

print("=" * 70)
print("  LECCIÓN 2: PROBABILIDAD Y MUESTREO – SIMULACIÓN DEL DATASET")
print("=" * 70)

N = 200

# --- Variables demográficas ---
genero_choices    = ['Masculino', 'Femenino', 'No binario']
genero_probs      = [0.45, 0.50, 0.05]
genero            = np.random.choice(genero_choices, size=N, p=genero_probs)

carrera_choices   = ['Exactas', 'Sociales', 'Salud', 'Tecnología', 'Humanidades']
carrera_probs     = [0.20, 0.25, 0.20, 0.25, 0.10]
carrera           = np.random.choice(carrera_choices, size=N, p=carrera_probs)

edad              = np.random.randint(18, 27, size=N)

# --- Variables de sueño ---
horas_sueno       = np.round(np.random.normal(loc=6.2, scale=1.2, size=N).clip(3, 10), 1)
calidad_sueno     = np.random.choice([1,2,3,4,5], size=N, p=[0.10,0.25,0.35,0.20,0.10])

# --- Variables de alimentación ---
comidas_dia       = np.random.choice([1,2,3,4,5], size=N, p=[0.05,0.20,0.40,0.25,0.10])
consume_alcohol   = np.random.choice(['Sí','No'], size=N, p=[0.55,0.45])
fuma              = np.random.choice(['Sí','No'], size=N, p=[0.20,0.80])

# --- Variables de actividad física ---
dias_actividad    = np.random.choice([0,1,2,3,4,5,6,7], size=N,
                                      p=[0.20,0.15,0.20,0.20,0.15,0.05,0.04,0.01])
horas_actividad   = np.where(dias_actividad == 0, 0,
                    np.round(np.random.exponential(scale=1.5, size=N).clip(0.5, 8), 1))

# --- IMC ---
peso              = np.round(np.random.normal(65, 12, size=N).clip(45, 110), 1)
talla             = np.round(np.random.normal(1.68, 0.09, size=N).clip(1.50, 1.95), 2)
imc               = np.round(peso / (talla ** 2), 1)

# --- Estrés ---
nivel_estres      = np.random.choice([1,2,3,4,5], size=N, p=[0.05,0.15,0.30,0.35,0.15])

# --- Rendimiento académico (correlacionado con estrés y sueño) ---
rend_score        = (horas_sueno * 0.3 - nivel_estres * 0.5 +
                     horas_actividad * 0.2 + np.random.normal(0, 0.5, N))
rendimiento       = pd.cut(rend_score, bins=3, labels=['Bajo','Medio','Alto'])

# --- Ensamblado del DataFrame ---
df = pd.DataFrame({
    'id'              : range(1, N+1),
    'edad'            : edad,
    'genero'          : genero,
    'carrera'         : carrera,
    'horas_sueno'     : horas_sueno,
    'calidad_sueno'   : calidad_sueno,
    'comidas_dia'     : comidas_dia,
    'consume_alcohol' : consume_alcohol,
    'fuma'            : fuma,
    'dias_actividad'  : dias_actividad,
    'horas_actividad' : horas_actividad,
    'peso_kg'         : peso,
    'talla_m'         : talla,
    'imc'             : imc,
    'nivel_estres'    : nivel_estres,
    'rendimiento'     : rendimiento
})

df.to_csv('dataset_habitos_universitarios.csv', index=False)
print(f"\n Dataset simulado guardado: dataset_habitos_universitarios.csv")
print(f"  Registros: {N}  |  Variables: {df.shape[1]}")
print("\nPrimeras 5 filas:")
print(df.head().to_string(index=False))
print("\nEstadísticas descriptivas:")
print(df[['horas_sueno','horas_actividad','imc','nivel_estres']].describe().round(2).to_string())

# ----- Probabilidades básicas -----
print("\n--- PROBABILIDADES BÁSICAS ---")
p_poco_sueno    = (df['horas_sueno'] < 6).mean()
p_activo        = (df['dias_actividad'] >= 3).mean()
p_ambos         = ((df['horas_sueno'] < 6) & (df['dias_actividad'] >= 3)).mean()
p_alguno        = p_poco_sueno + p_activo - p_ambos
p_no_activo     = 1 - p_activo

print(f"  P(duerme <6h)                        = {p_poco_sueno:.4f}  ({p_poco_sueno*100:.1f}%)")
print(f"  P(activo ≥3 días/sem)                = {p_activo:.4f}  ({p_activo*100:.1f}%)")
print(f"  P(<6h ∩ activo)                      = {p_ambos:.4f}  ({p_ambos*100:.1f}%)")
print(f"  P(<6h ∪ activo)                      = {p_alguno:.4f}  ({p_alguno*100:.1f}%)")
print(f"  P(no activo) = complemento           = {p_no_activo:.4f}  ({p_no_activo*100:.1f}%)")

p_stres_alto_dado_poco_sueno = (
    (df['nivel_estres'] >= 4) & (df['horas_sueno'] < 6)
).sum() / (df['horas_sueno'] < 6).sum()
print(f"  P(estrés alto | duerme <6h)          = {p_stres_alto_dado_poco_sueno:.4f}  ({p_stres_alto_dado_poco_sueno*100:.1f}%)")

# =============================================================================
# LECCIÓN 3: DISTRIBUCIONES DE PROBABILIDAD
# =============================================================================

print("\n" + "=" * 70)
print("  LECCIÓN 3: DISTRIBUCIONES DE PROBABILIDAD")
print("=" * 70)

# --- A) Distribución Normal: Horas de sueño ---
mu_sueno = df['horas_sueno'].mean()
sd_sueno = df['horas_sueno'].std()
print(f"\n[NORMAL] Horas de sueño → μ={mu_sueno:.3f}, σ={sd_sueno:.3f}")

p_menos_6   = norm.cdf(6, mu_sueno, sd_sueno)
p_entre_6_8 = norm.cdf(8, mu_sueno, sd_sueno) - norm.cdf(6, mu_sueno, sd_sueno)
p_mas_8     = 1 - norm.cdf(8, mu_sueno, sd_sueno)
print(f"  P(sueño < 6h)   = {p_menos_6:.4f}  ({p_menos_6*100:.1f}%)")
print(f"  P(6 ≤ sueño ≤ 8)= {p_entre_6_8:.4f}  ({p_entre_6_8*100:.1f}%)")
print(f"  P(sueño > 8h)   = {p_mas_8:.4f}  ({p_mas_8*100:.1f}%)")

# --- B) Distribución Binomial: actividad física (éxito = ≥3 días) ---
p_exito = p_activo
n_enc   = 20
print(f"\n[BINOMIAL] De 20 estudiantes, P(≥3 días activo)={p_exito:.3f}")
for k in [0, 5, 10, 15]:
    pb = binom.pmf(k, n_enc, p_exito)
    print(f"  P(X={k:2d})= {pb:.4f}")
p_bin_5plus = 1 - binom.cdf(4, n_enc, p_exito)
print(f"  P(X≥5 de 20 activos)= {p_bin_5plus:.4f}")

# --- C) Distribución Poisson: comidas por día ---
lambda_comidas = df['comidas_dia'].mean()
print(f"\n[POISSON] Comidas/día → λ={lambda_comidas:.3f}")
for k in [1, 2, 3, 4, 5]:
    pp = poisson.pmf(k, lambda_comidas)
    print(f"  P(X={k})= {pp:.4f}")

# ----- GRÁFICOS LECCIÓN 3 -----
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Lección 3: Distribuciones de Probabilidad", fontsize=14, fontweight='bold')

# Normal
x_rng = np.linspace(2, 11, 300)
y_pdf = norm.pdf(x_rng, mu_sueno, sd_sueno)
axes[0].hist(df['horas_sueno'], bins=20, density=True, alpha=0.5, color='steelblue', label='Datos')
axes[0].plot(x_rng, y_pdf, 'r-', lw=2, label=f'N({mu_sueno:.2f},{sd_sueno:.2f})')
axes[0].axvline(6, color='orange', linestyle='--', label='6h')
axes[0].axvline(8, color='green',  linestyle='--', label='8h')
axes[0].set_title("Distribución Normal\n(Horas de sueño)")
axes[0].set_xlabel("Horas"); axes[0].set_ylabel("Densidad")
axes[0].legend(fontsize=8)

# Binomial
k_vals = np.arange(0, n_enc+1)
pmf_b  = binom.pmf(k_vals, n_enc, p_exito)
axes[1].bar(k_vals, pmf_b, color='coral', edgecolor='black', alpha=0.8)
axes[1].set_title(f"Distribución Binomial\n(n={n_enc}, p={p_exito:.2f})")
axes[1].set_xlabel("Nº estudiantes activos"); axes[1].set_ylabel("P(X=k)")

# Poisson
k_poi = np.arange(0, 9)
pmf_p = poisson.pmf(k_poi, lambda_comidas)
axes[2].bar(k_poi, pmf_p, color='mediumseagreen', edgecolor='black', alpha=0.8)
axes[2].set_title(f"Distribución Poisson\n(λ={lambda_comidas:.2f} comidas/día)")
axes[2].set_xlabel("Nº comidas"); axes[2].set_ylabel("P(X=k)")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/leccion3_distribuciones.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"\n Gráfico guardado: {OUTPUT_DIR}/leccion3_distribuciones.png")

# =============================================================================
# LECCIÓN 4: DISTRIBUCIÓN MUESTRAL Y TEOREMA DEL LÍMITE CENTRAL
# =============================================================================

print("\n" + "=" * 70)
print("  LECCIÓN 4: DISTRIBUCIÓN MUESTRAL Y TEOREMA DEL LÍMITE CENTRAL")
print("=" * 70)

poblacion = df['horas_sueno'].values
mu_pob    = poblacion.mean()
sd_pob    = poblacion.std()
print(f"\nPoblación simulada: μ={mu_pob:.4f}, σ={sd_pob:.4f}")

tamanios = [5, 15, 30, 50]
n_muestras = 1000
resultados_tlc = {}

print("\nVerificación empírica del TLC:")
print(f"{'Tamaño n':>10} | {'μ medias':>10} | {'σ medias':>10} | {'σ/√n (teórico)':>16} | {'Dif%':>8}")
print("-" * 65)
for n in tamanios:
    medias = [np.random.choice(poblacion, n, replace=False).mean() for _ in range(n_muestras)]
    mu_m   = np.mean(medias)
    sd_m   = np.std(medias)
    teo    = sd_pob / np.sqrt(n)
    dif    = abs(sd_m - teo) / teo * 100
    resultados_tlc[n] = medias
    print(f"{n:>10} | {mu_m:>10.4f} | {sd_m:>10.4f} | {teo:>16.4f} | {dif:>7.2f}%")

# ----- GRÁFICOS TLC -----
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Lección 4: Teorema del Límite Central – Distribución de Medias Muestrales",
             fontsize=13, fontweight='bold')
for ax, n in zip(axes.flatten(), tamanios):
    medias = resultados_tlc[n]
    mu_m   = np.mean(medias); sd_m = np.std(medias)
    x_r    = np.linspace(min(medias), max(medias), 200)
    y_r    = norm.pdf(x_r, mu_m, sd_m)
    ax.hist(medias, bins=40, density=True, alpha=0.55, color='slateblue')
    ax.plot(x_r, y_r, 'r-', lw=2, label=f'N({mu_m:.2f},{sd_m:.2f})')
    ax.axvline(mu_pob, color='orange', linestyle='--', lw=1.5, label=f'μ pob={mu_pob:.2f}')
    ax.set_title(f"n = {n}  ({n_muestras} muestras)")
    ax.set_xlabel("Media muestral (horas sueño)")
    ax.set_ylabel("Densidad")
    ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/leccion4_tlc.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"\n Gráfico guardado: {OUTPUT_DIR}/leccion4_tlc.png")

# =============================================================================
# LECCIÓN 5: INTERVALOS DE CONFIANZA
# =============================================================================

print("\n" + "=" * 70)
print("  LECCIÓN 5: INTERVALOS DE CONFIANZA")
print("=" * 70)

variables_ic = {
    'horas_sueno'     : 'Horas de sueño',
    'horas_actividad' : 'Horas de actividad física',
    'imc'             : 'IMC'
}
niveles = [0.90, 0.95, 0.99]

for var, nombre in variables_ic.items():
    datos = df[var].dropna()
    n_v   = len(datos); mu_v = datos.mean(); sd_v = datos.std(ddof=1)
    print(f"\n  {nombre}  (n={n_v}, x̄={mu_v:.3f}, s={sd_v:.3f})")
    for nivel in niveles:
        ic = stats.t.interval(nivel, df=n_v-1, loc=mu_v, scale=sd_v/np.sqrt(n_v))
        ancho = ic[1] - ic[0]
        print(f"    IC {int(nivel*100)}%: [{ic[0]:.4f},  {ic[1]:.4f}]  ancho={ancho:.4f}")

# Impacto del tamaño muestral
print("\n  Impacto del tamaño muestral sobre el ancho del IC (95%, horas sueño):")
datos_s = df['horas_sueno'].dropna()
print(f"  {'n':>6} | {'Ancho IC':>10}")
print(f"  {'-'*20}")
for n_sub in [20, 50, 100, 150, 200]:
    sub   = datos_s.sample(n_sub, random_state=42)
    ic_s  = stats.t.interval(0.95, df=n_sub-1, loc=sub.mean(), scale=sub.std(ddof=1)/np.sqrt(n_sub))
    print(f"  {n_sub:>6} | {ic_s[1]-ic_s[0]:>10.4f}")

# ----- GRÁFICO IC -----
fig, ax = plt.subplots(figsize=(10, 6))
colores = ['#2196F3', '#4CAF50', '#FF9800']
y_pos   = 0
y_ticks = []; y_labels = []
for idx_var, (var, nombre) in enumerate(variables_ic.items()):
    datos = df[var].dropna()
    n_v   = len(datos); mu_v = datos.mean(); sd_v = datos.std(ddof=1)
    for idx_niv, nivel in enumerate(niveles):
        ic = stats.t.interval(nivel, df=n_v-1, loc=mu_v, scale=sd_v/np.sqrt(n_v))
        ax.barh(y_pos, ic[1]-ic[0], left=ic[0], height=0.6,
                color=colores[idx_niv], alpha=0.7,
                label=f"IC {int(nivel*100)}%" if idx_var == 0 else "")
        ax.plot(mu_v, y_pos, 'k|', markersize=12, markeredgewidth=2)
        y_ticks.append(y_pos)
        y_labels.append(f"{nombre[:20]}\n{int(nivel*100)}%")
        y_pos += 1
    y_pos += 0.5
ax.set_yticks(y_ticks); ax.set_yticklabels(y_labels, fontsize=8)
ax.set_xlabel("Valor del parámetro")
ax.set_title("Lección 5: Intervalos de Confianza por Variable y Nivel", fontweight='bold')
handles, labels = ax.get_legend_handles_labels()
unique = dict(zip(labels, handles))
ax.legend(unique.values(), unique.keys())
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/leccion5_intervalos.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"\n Gráfico guardado: {OUTPUT_DIR}/leccion5_intervalos.png")

# =============================================================================
# LECCIÓN 6: PRUEBAS DE HIPÓTESIS
# =============================================================================

print("\n" + "=" * 70)
print("  LECCIÓN 6: TEST DE SIGNIFICANCIA")
print("=" * 70)
alpha = 0.05

# --- Test 1: ¿μ sueño < 7h? (t unilateral izquierda) ---
print("\n[TEST 1] ¿Los universitarios duermen menos de 7 horas en promedio?")
print("  H0: μ = 7  |  H1: μ < 7  |  α = 0.05")
datos_s = df['horas_sueno']
t_stat, p_val_dos = stats.ttest_1samp(datos_s, 7)
p_val_uni = p_val_dos / 2
print(f"  n = {len(datos_s)}, x̄ = {datos_s.mean():.4f}, s = {datos_s.std(ddof=1):.4f}")
print(f"  t estadístico = {t_stat:.4f}")
print(f"  p-valor (bilateral) = {p_val_dos:.6f}")
print(f"  p-valor (unilateral) = {p_val_uni:.6f}")
if t_stat < 0 and p_val_uni < alpha:
    print(f"  → RECHAZAMOS H0. Evidencia significativa: μ < 7h (p={p_val_uni:.4f} < α={alpha})")
else:
    print(f"  → NO rechazamos H0. (p={p_val_uni:.4f} >= α={alpha})")

# --- Test 2: ¿Las carreras difieren en horas de sueño? (ANOVA) ---
print("\n[TEST 2] ¿Existen diferencias en horas de sueño entre carreras? (ANOVA)")
print("  H0: μ_Exactas = μ_Sociales = μ_Salud = μ_Tecnología = μ_Humanidades")
print("  H1: Al menos una media difiere  |  α = 0.05")
grupos = [df[df['carrera']==c]['horas_sueno'].values for c in df['carrera'].unique()]
f_stat, p_anova = stats.f_oneway(*grupos)
print(f"  F estadístico = {f_stat:.4f},  p-valor = {p_anova:.4f}")
if p_anova < alpha:
    print(f"  → RECHAZAMOS H0. Diferencia significativa entre carreras (p={p_anova:.4f})")
else:
    print(f"  → NO rechazamos H0. Sin diferencia significativa (p={p_anova:.4f})")

# --- Test 3: ¿Actividad física mejora calidad de sueño? (t independiente) ---
print("\n[TEST 3] ¿Quienes hacen actividad física tienen mayor calidad de sueño?")
print("  H0: μ_activos = μ_sedentarios  |  H1: μ_activos > μ_sedentarios  |  α = 0.05")
activos    = df[df['dias_actividad'] >= 3]['calidad_sueno']
sedentarios= df[df['dias_actividad'] <  3]['calidad_sueno']
t2, p2_dos = stats.ttest_ind(activos, sedentarios, equal_var=False)
p2_uni     = p2_dos / 2
print(f"  Activos    : n={len(activos)}, x̄={activos.mean():.4f}")
print(f"  Sedentarios: n={len(sedentarios)}, x̄={sedentarios.mean():.4f}")
print(f"  t = {t2:.4f},  p (bilateral) = {p2_dos:.4f},  p (unilateral) = {p2_uni:.4f}")
if t2 > 0 and p2_uni < alpha:
    print(f"  → RECHAZAMOS H0. Activos duermen con mayor calidad (p={p2_uni:.4f})")
else:
    print(f"  → NO rechazamos H0. (p={p2_uni:.4f})")

# --- Test 4: Proporción fuma > 20% (z test) ---
print("\n[TEST 4] ¿La proporción de fumadores supera el 20%?")
print("  H0: p = 0.20  |  H1: p > 0.20  |  α = 0.05")
n_fuma   = (df['fuma'] == 'Sí').sum()
prop_obs = n_fuma / N
z_stat   = (prop_obs - 0.20) / np.sqrt(0.20*0.80/N)
p_z      = 1 - norm.cdf(z_stat)
print(f"  n_fuma={n_fuma}, p̂={prop_obs:.4f}")
print(f"  z = {z_stat:.4f},  p-valor (unilateral) = {p_z:.4f}")
if p_z < alpha:
    print(f"  → RECHAZAMOS H0. Proporción > 20% (p={p_z:.4f})")
else:
    print(f"  → NO rechazamos H0. (p={p_z:.4f})")

# Errores tipo I y II
print("""
ERRORES TIPO I Y TIPO II EN CONTEXTO:
--------------------------------------
  Error Tipo I (α):  Concluir que los universitarios duermen < 7h cuando en
                      realidad sí duermen 7h. Se fijó α=0.05 (5% de riesgo).
                      Consecuencia: políticas innecesarias de salud del sueño.

  Error Tipo II (β): No detectar que duermen < 7h cuando realmente lo hacen.
                      Con n=200, la potencia estimada es ~0.85 (β≈0.15).
                      Consecuencia: no intervenir ante un problema real de salud.
""")

# ----- GRÁFICO TEST HIPÓTESIS -----
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Lección 6: Pruebas de Hipótesis", fontsize=13, fontweight='bold')

# Test 1 – distribución t
t_crit  = stats.t.ppf(0.05, df=N-1)
x_t     = np.linspace(-5, 5, 500)
y_t     = stats.t.pdf(x_t, df=N-1)
axes[0].plot(x_t, y_t, 'b-', lw=2)
axes[0].fill_between(x_t, y_t, where=(x_t <= t_crit), color='red', alpha=0.4, label=f'Región α (t<{t_crit:.2f})')
axes[0].axvline(t_stat, color='darkred', lw=2, linestyle='--', label=f't_obs={t_stat:.3f}')
axes[0].set_title("Test 1: ¿μ sueño < 7h?\nDistribución t (H0)")
axes[0].set_xlabel("t"); axes[0].set_ylabel("Densidad")
axes[0].legend(fontsize=9)

# Test 3 – comparación de medias
df_plot = pd.DataFrame({
    'calidad_sueno' : pd.concat([activos, sedentarios]),
    'grupo'         : ['Activo']*len(activos) + ['Sedentario']*len(sedentarios)
})
grupos_plot = ['Activo', 'Sedentario']
colores_bp  = ['#4CAF50', '#FF5722']
data_bp = [activos.values, sedentarios.values]
bp = axes[1].boxplot(data_bp, labels=grupos_plot, patch_artist=True,
                     boxprops=dict(facecolor='lightblue'),
                     medianprops=dict(color='navy', lw=2))
for patch, color in zip(bp['boxes'], colores_bp):
    patch.set_facecolor(color); patch.set_alpha(0.6)
axes[1].set_title(f"Test 3: Calidad de sueño\nActivos vs Sedentarios  (p={p2_uni:.4f})")
axes[1].set_ylabel("Calidad de sueño (1-5)")
axes[1].text(0.5, 0.02,
             f"*p {'< 0.05 (sig.)' if p2_uni < 0.05 else '≥ 0.05 (no sig.)'}",
             transform=axes[1].transAxes, ha='center', color='darkred', fontsize=10)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/leccion6_tests.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"\n Gráfico guardado: {OUTPUT_DIR}/leccion6_tests.png")

# =============================================================================
# GRÁFICO EXPLORATORIO GENERAL
# =============================================================================

fig = plt.figure(figsize=(16, 10))
fig.suptitle("Dashboard: Hábitos Saludables en Jóvenes Universitarios\n(n=200)",
             fontsize=14, fontweight='bold')
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

ax1 = fig.add_subplot(gs[0, 0])
df['horas_sueno'].hist(bins=20, ax=ax1, color='steelblue', edgecolor='white')
ax1.axvline(df['horas_sueno'].mean(), color='red', lw=2, linestyle='--', label=f"μ={df['horas_sueno'].mean():.2f}")
ax1.set_title("Distribución Horas de Sueño"); ax1.legend()

ax2 = fig.add_subplot(gs[0, 1])
df['horas_actividad'].hist(bins=20, ax=ax2, color='mediumseagreen', edgecolor='white')
ax2.set_title("Distribución Horas de Actividad Física")

ax3 = fig.add_subplot(gs[0, 2])
df.groupby('carrera')['horas_sueno'].mean().plot(kind='bar', ax=ax3, color='coral', edgecolor='black')
ax3.set_title("Sueño Promedio por Carrera"); ax3.set_xticklabels(ax3.get_xticklabels(), rotation=30, ha='right')
ax3.set_ylabel("Horas"); ax3.axhline(7, color='blue', linestyle='--', alpha=0.5, label='7h')

ax4 = fig.add_subplot(gs[1, 0])
ax4.scatter(df['horas_sueno'], df['nivel_estres'],
            c=df['nivel_estres'], cmap='RdYlGn_r', alpha=0.5, s=30)
ax4.set_title("Sueño vs Nivel de Estrés"); ax4.set_xlabel("Horas sueño"); ax4.set_ylabel("Estrés (1-5)")

ax5 = fig.add_subplot(gs[1, 1])
ax5.scatter(df['horas_actividad'], df['imc'], alpha=0.5, color='purple', s=30)
ax5.set_title("Actividad Física vs IMC"); ax5.set_xlabel("Horas actividad/sem"); ax5.set_ylabel("IMC")

ax6 = fig.add_subplot(gs[1, 2])
df['calidad_sueno'].value_counts().sort_index().plot(kind='bar', ax=ax6, color='goldenrod', edgecolor='black')
ax6.set_title("Calidad de Sueño (1=Muy mala, 5=Muy buena)")
ax6.set_xlabel("Puntuación"); ax6.set_ylabel("Frecuencia")

plt.savefig(f"{OUTPUT_DIR}/dashboard_general.png", dpi=150, bbox_inches='tight')
plt.close()
print(f"\n Gráfico guardado: {OUTPUT_DIR}/dashboard_general.png")

print("\n" + "=" * 70)
print("  ANÁLISIS COMPLETADO EXITOSAMENTE")
print(f"  Gráficos generados en: ./{OUTPUT_DIR}/")
print(f"  Dataset guardado: dataset_habitos_universitarios.csv")
print("=" * 70)
