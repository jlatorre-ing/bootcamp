"""
=======================================================================
ANÁLISIS DE CASO: Inferencia e Intervalos de Confianza para la Media
Empresa: DataNova | Cliente: Cadena de Supermercados
Analista: Data Analyst - DataNova
=======================================================================
"""

import numpy as np
from scipy import stats

# =====================================================================
# 1. DATOS DEL PROBLEMA
# =====================================================================
n = 60                  # Tamaño de muestra
x_bar = 132.50          # Media muestral (USD)
s = 15.40               # Desviación estándar muestral (USD)
confianza_95 = 0.95     # Nivel de confianza 95%
confianza_99 = 0.99     # Nivel de confianza 99%
gl = n - 1              # Grados de libertad = 59

print("=" * 65)
print("  ANÁLISIS DE INTERVALO DE CONFIANZA - DATANOVA")
print("  Cliente: Cadena de Supermercados")
print("=" * 65)

# =====================================================================
# 2. ELECCIÓN DE DISTRIBUCIÓN
# =====================================================================
print("\n📌 ELECCIÓN DE DISTRIBUCIÓN")
print("-" * 65)
print(f"  ✔ n = {n} (≥ 30 → Teorema Central del Límite aplica)")
print(f"  ✔ Desviación poblacional σ: DESCONOCIDA")
print(f"  ✔ Se usa desviación estándar MUESTRAL (s = {s})")
print()
print("  → Se utiliza la distribución t-Student con 59 grados de")
print("    libertad, ya que σ es desconocida y se estima con s.")
print("    Aunque n ≥ 30 permite aproximar a normal, la práctica")
print("    estadística recomienda t-Student cuando σ es desconocida.")

# =====================================================================
# 3. ERROR ESTÁNDAR
# =====================================================================
error_estandar = s / np.sqrt(n)
print(f"\n📐 ERROR ESTÁNDAR DE LA MEDIA")
print("-" * 65)
print(f"  SE = s / √n = {s} / √{n} = {error_estandar:.4f} USD")

# =====================================================================
# 4. INTERVALO DE CONFIANZA AL 95%
# =====================================================================
alpha_95 = 1 - confianza_95
t_95 = stats.t.ppf(1 - alpha_95/2, df=gl)
margen_95 = t_95 * error_estandar
li_95 = x_bar - margen_95
ls_95 = x_bar + margen_95

print(f"\n📊 INTERVALO DE CONFIANZA AL 95%")
print("-" * 65)
print(f"  α = {alpha_95} | α/2 = {alpha_95/2}")
print(f"  t(α/2, gl=59) = t(0.025, 59) = {t_95:.4f}")
print(f"  Margen de error = t × SE = {t_95:.4f} × {error_estandar:.4f} = {margen_95:.4f} USD")
print(f"\n  IC 95% = x̄ ± E = {x_bar} ± {margen_95:.4f}")
print(f"\n  ┌─────────────────────────────────────────┐")
print(f"  │  IC 95%: [ ${li_95:.2f} , ${ls_95:.2f} ]  │")
print(f"  └─────────────────────────────────────────┘")

# =====================================================================
# 5. INTERPRETACIÓN AL 95%
# =====================================================================
print(f"\n💡 INTERPRETACIÓN AL 95%")
print("-" * 65)
print(f"  Con un 95% de confianza, el gasto medio semanal REAL de")
print(f"  todos los clientes frecuentes del supermercado se encuentra")
print(f"  entre ${li_95:.2f} y ${ls_95:.2f} USD.")
print()
print(f"  → Si se repitiera este muestreo 100 veces, en 95 de ellas")
print(f"    el intervalo contendría la verdadera media poblacional.")

# =====================================================================
# 6. EXTENSIÓN OPCIONAL: IC AL 99%
# =====================================================================
alpha_99 = 1 - confianza_99
t_99 = stats.t.ppf(1 - alpha_99/2, df=gl)
margen_99 = t_99 * error_estandar
li_99 = x_bar - margen_99
ls_99 = x_bar + margen_99

print(f"\n📊 EXTENSIÓN OPCIONAL - INTERVALO DE CONFIANZA AL 99%")
print("-" * 65)
print(f"  α = {alpha_99} | α/2 = {alpha_99/2}")
print(f"  t(α/2, gl=59) = t(0.005, 59) = {t_99:.4f}")
print(f"  Margen de error = {t_99:.4f} × {error_estandar:.4f} = {margen_99:.4f} USD")
print(f"\n  ┌─────────────────────────────────────────┐")
print(f"  │  IC 99%: [ ${li_99:.2f} , ${ls_99:.2f} ]  │")
print(f"  └─────────────────────────────────────────┘")

# =====================================================================
# 7. COMPARACIÓN DE INTERVALOS
# =====================================================================
amplitud_95 = ls_95 - li_95
amplitud_99 = ls_99 - li_99
diferencia = amplitud_99 - amplitud_95

print(f"\n🔍 COMPARACIÓN DE INTERVALOS")
print("-" * 65)
print(f"  {'Confianza':<15} {'Límite Inf.':<15} {'Límite Sup.':<15} {'Amplitud':<10}")
print(f"  {'-'*55}")
print(f"  {'95%':<15} ${li_95:.2f}{'':<8} ${ls_95:.2f}{'':<8} ${amplitud_95:.4f}")
print(f"  {'99%':<15} ${li_99:.2f}{'':<8} ${ls_99:.2f}{'':<8} ${amplitud_99:.4f}")
print(f"\n  → El IC al 99% es {diferencia:.4f} USD más amplio que el IC al 95%.")
print(f"  → Mayor confianza = Menor precisión (intervalo más ancho).")

# =====================================================================
# 8. RECOMENDACIÓN EJECUTIVA
# =====================================================================
print(f"\n🏢 RECOMENDACIÓN EJECUTIVA")
print("-" * 65)
print(f"  Con un 95% de confianza, estimamos que el gasto promedio")
print(f"  semanal de los clientes frecuentes es de ${x_bar:.2f} USD,")
print(f"  con un intervalo de ${li_95:.2f} a ${ls_95:.2f} USD.")
print()
print(f"  Decisiones comerciales sugeridas:")
print(f"  • Planificación de inventario basada en gasto ~${x_bar:.0f}/semana")
print(f"  • Diseñar promociones para clientes con gasto < ${li_95:.0f}")
print(f"  • Programas de fidelización para clientes con gasto > ${ls_95:.0f}")
print(f"  • Presupuesto de compras con margen de ±${margen_95:.2f} USD")

print(f"\n{'=' * 65}")
print("  Análisis completado por: DataNova Analytics Team")
print(f"{'=' * 65}\n")

# Exportar resultados como diccionario para uso en el reporte
resultados = {
    "n": n, "x_bar": x_bar, "s": s, "gl": gl,
    "error_estandar": round(error_estandar, 4),
    "t_95": round(t_95, 4), "margen_95": round(margen_95, 4),
    "li_95": round(li_95, 2), "ls_95": round(ls_95, 2),
    "amplitud_95": round(amplitud_95, 4),
    "t_99": round(t_99, 4), "margen_99": round(margen_99, 4),
    "li_99": round(li_99, 2), "ls_99": round(ls_99, 2),
    "amplitud_99": round(amplitud_99, 4),
}
print("Resultados numéricos:", resultados)
