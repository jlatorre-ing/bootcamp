# 🎓 Análisis Estadístico: Hábitos Saludables en Jóvenes Universitarios
### Módulo 5 — Inferencia Estadística | Alkemy

---

## 📌 Descripción del Proyecto

Investigación estadística completa que aplica el **método científico** para analizar los hábitos de sueño, alimentación y actividad física en 200 jóvenes universitarios simulados. El proyecto cubre las 6 lecciones del módulo de Inferencia Estadística.

---

## 📁 Estructura del Repositorio

```
proyecto-habitos-saludables/
│
├── habitos_saludables.py             # Script Python completo (todas las lecciones)
├── habitos_saludables.ipynb          # Notebook Jupyter interactivo
├── dataset_habitos_universitarios.csv # Dataset simulado (200 registros, 16 variables)
├── diccionario_variables.csv         # Metadatos de cada variable
├── informe_final.docx                # Informe con conclusiones y recomendaciones
├── README.md                         # Este archivo
│
└── graficos/
    ├── leccion3_distribuciones.png   # Normal, Binomial, Poisson
    ├── leccion4_tlc.png              # Teorema del Límite Central
    ├── leccion5_intervalos.png       # Intervalos de confianza
    ├── leccion6_tests.png            # Pruebas de hipótesis
    └── dashboard_general.png         # Vista exploratoria general
```

---

## ⚙️ Requisitos

### Python (≥ 3.9)

```bash
pip install numpy pandas scipy matplotlib seaborn jupyter
```

### Visual Studio Code — Extensiones recomendadas

| Extensión | Para qué sirve |
|-----------|----------------|
| **Python** (Microsoft) | Ejecución de scripts `.py` |
| **Jupyter** (Microsoft) | Abrir y ejecutar `.ipynb` |
| **Pylance** | Autocompletado avanzado |
| **Rainbow CSV** | Visualizar el dataset `.csv` |

---

## 🚀 Paso a Paso para Ejecutar el Proyecto

### Opción A — Ejecutar el Script Python (.py)

1. Abrí VS Code y abrí la carpeta del proyecto:
   ```
   Archivo → Abrir Carpeta → seleccioná la carpeta del proyecto
   ```

2. Creá un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. Instalá las dependencias:
   ```bash
   pip install numpy pandas scipy matplotlib seaborn
   ```

4. Ejecutá el script principal:
   ```bash
   python habitos_saludables.py
   ```

5. Los **gráficos** se guardarán en la carpeta `graficos/`  
   El **dataset** se guardará como `dataset_habitos_universitarios.csv`

---

### Opción B — Ejecutar el Notebook Jupyter (.ipynb)

1. Instalá Jupyter:
   ```bash
   pip install jupyter
   ```

2. Abrí el notebook en VS Code:
   - Hacé doble clic en `habitos_saludables.ipynb`
   - VS Code lo abre automáticamente con la extensión Jupyter

3. Seleccioná el kernel:
   - Click en "Select Kernel" → elegí tu entorno Python/venv

4. Ejecutá todas las celdas:
   - `Ctrl + Shift + P` → "Jupyter: Run All Cells"  
   - O usá el botón ▶▶ "Run All" en la barra superior

5. Podés ejecutar celda por celda con `Shift + Enter`

---

## 📊 Contenido por Lección

### Lección 1 — Método Científico
- Definición del problema de investigación
- Formulación de hipótesis H₀ y H₁
- Identificación de variables (cuantitativas/cualitativas, escalas de medición)
- Diseño del estudio: observacional, transversal, estratificado

### Lección 2 — Probabilidad y Muestreo
- Simulación del dataset con `numpy.random` y distribuciones definidas
- Muestreo estratificado por carrera y género
- Probabilidades: P(A), P(A∩B), P(A∪B), P(A|B), P(Aᶜ)

### Lección 3 — Distribuciones de Probabilidad
| Variable | Distribución | Justificación |
|----------|-------------|---------------|
| Horas de sueño | **Normal** N(6.2, 1.2) | Variable continua, fenómeno biológico |
| Activos en grupo | **Binomial** Bin(20, p) | Ensayos independientes Bernoulli |
| Comidas por día | **Poisson** λ=3.22 | Conteo de eventos discretos |

### Lección 4 — Distribución Muestral y TLC
- Generación de 1000 medias muestrales para n = {5, 15, 30, 50}
- Verificación empírica: σ_medias ≈ σ/√n
- Visualización de la convergencia a la Normal con el aumento de n

### Lección 5 — Intervalos de Confianza
- IC para: horas de sueño, horas de actividad física, IMC
- Comparación entre niveles: 90%, 95%, 99%
- Análisis del efecto del tamaño muestral sobre el ancho del intervalo

### Lección 6 — Pruebas de Hipótesis
| Test | H₀ | H₁ | Resultado |
|------|----|----|-----------|
| t unilateral | μ_sueño = 7h | μ_sueño < 7h | **Rechazamos H₀** (p<0.001) |
| ANOVA | igualdad entre carreras | al menos una difiere | No rechazamos (p=0.96) |
| t independiente | activos = sedentarios | activos > sedentarios | **Rechazamos H₀** (p=0.028) |
| z proporciones | p_fuma = 20% | p_fuma > 20% | No rechazamos (p=0.76) |

---

## 📋 Variables del Dataset

Ver archivo `diccionario_variables.csv` para descripción completa de cada variable.

Variables principales:

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `horas_sueno` | Continua | Horas de sueño por noche (3-10) |
| `calidad_sueno` | Ordinal | Calidad percibida (1=Muy mala, 5=Muy buena) |
| `horas_actividad` | Continua | Horas de actividad física/semana |
| `dias_actividad` | Discreta | Días/semana con actividad física |
| `comidas_dia` | Discreta | Número de comidas diarias |
| `imc` | Continua | Índice de Masa Corporal |
| `nivel_estres` | Ordinal | Estrés académico (1=Muy bajo, 5=Muy alto) |
| `rendimiento` | Ordinal | Rendimiento autopercibido (Bajo/Medio/Alto) |

---

## 📈 Principales Hallazgos

1. **Déficit de sueño:** Los universitarios duermen en promedio **6.17h** (< 7h recomendadas). Test t: p < 0.001.
2. **Alta prevalencia:** El **45%** duerme menos de 6 horas por noche.
3. **Estrés relacionado:** El **47.8%** con poco sueño reporta estrés alto.
4. **Actividad física protectora:** Quienes hacen ejercicio ≥3 días/semana tienen mejor calidad de sueño (p=0.028).
5. **Sin diferencias por carrera:** El tipo de carrera no explica las diferencias en sueño (ANOVA p=0.96).

---

## 🎯 Recomendaciones

1. Implementar **talleres de higiene del sueño** al inicio de cada ciclo lectivo.
2. Promover la **actividad física** mediante programas de bienestar estudiantil.
3. Ampliar el estudio a n ≥ 500 para mayor potencia estadística.
4. Incorporar seguimiento **longitudinal** para establecer relaciones causales.
5. Evaluar intervenciones específicas para reducir el estrés académico.

---

## 📚 Referencias

- Khan Academy — [Estadística y Probabilidad](https://es.khanacademy.org/math/statistics-probability)
- StatTrek — [Tutoriales Interactivos](https://stattrek.com)
- SocSciStatistics — [Calculadora de distribuciones](https://www.socscistatistics.com)
- Documentación SciPy: `scipy.stats` — https://docs.scipy.org/doc/scipy/reference/stats.html
- Documentación NumPy: https://numpy.org/doc/

---

## 👤 Autor

**Equipo de Investigación** — Área de Salud Universitaria  
Módulo 5: Inferencia Estadística | Programa Alkemy  
Fecha: 2026

---

> 💡 **Tip VS Code:** Usá `Ctrl+Shift+P` → "Python: Select Interpreter" para asegurarte de usar el entorno virtual correcto.
