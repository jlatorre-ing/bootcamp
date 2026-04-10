# 🛍️ Retail Analytics Pipeline — RetailMax
### Proyecto de Evaluación — Módulo 9: Fundamentos de Big Data | Alkemy

---

## 📋 Descripción del Proyecto

Pipeline completo de **Big Data + Machine Learning escalable** usando Apache Spark (PySpark).
Procesa el dataset **Fashion-MNIST** (imágenes de prendas de moda) para demostrar el flujo
completo: ingesta → RDDs → DataFrames → Spark SQL → MLlib.

---

## 🗂️ Estructura del Proyecto

```
retail_analytics_pipeline/
│
├── 📒 notebooks/
│   ├── leccion_01_fundamentos_bigdata.ipynb
│   ├── leccion_02_spark_configuracion.ipynb
│   ├── leccion_03_rdd_transformaciones.ipynb
│   ├── leccion_04_spark_sql_dataframes.ipynb
│   └── leccion_05_mllib_pipeline.ipynb
│
├── 📁 data/fashion_mnist/
│   ├── fashion_train.csv    (generado por setup_dataset.py)
│   └── fashion_test.csv
│
├── 📁 outputs/              (generado al ejecutar los notebooks)
├── 📁 visualizations/       (gráficos PNG por lección)
├── 📁 reports/
│   └── informe_final.pdf
│
├── setup_dataset.py         ← Genera el dataset Fashion-MNIST
├── verificar_entorno.py     ← Comprueba que todo esté instalado
└── README.md
```

---

## ⚙️ Instalación en Windows — Paso a Paso

> Ya tenés Python instalado. Te falta: Java JDK 11 + PySpark + algunas librerías.

---

### PASO 1 — Instalar Java JDK 11 (obligatorio para Spark)

1. Ir a: https://adoptium.net/temurin/releases/
2. Filtrar: Version=11, OS=Windows, Architecture=x64, Package=JDK
3. Descargar el .msi e instalarlo
4. Verificar: abrir cmd y ejecutar `java -version`

---

### PASO 2 — Configurar JAVA_HOME (si PySpark falla)

Si ves el error "Java gateway process exited":

1. Win+R → sysdm.cpl → Opciones avanzadas → Variables de entorno
2. En "Variables del sistema" → Nueva:
   - Nombre: JAVA_HOME
   - Valor: C:\Program Files\Eclipse Adoptium\jdk-11.0.xx.x-hotspot
3. Aceptar → cerrar VS Code → reabrirlo

---

### PASO 3 — Crear entorno virtual en VS Code

Abrir terminal integrada (Ctrl+ñ):

```cmd
python -m venv venv
venv\Scripts\activate
```

---

### PASO 4 — Instalar librerías Python

```cmd
pip install pyspark numpy pandas matplotlib seaborn
```

PySpark incluye Spark internamente — no necesitás instalar Apache Spark por separado.

---

### PASO 5 — Instalar extensiones VS Code

Ctrl+Shift+X → instalar:
- Python (Microsoft)
- Jupyter (Microsoft)

Ctrl+Shift+P → "Python: Select Interpreter" → elegir el de venv

---

### PASO 6 — Verificar entorno

```cmd
python verificar_entorno.py
```

Deberías ver [OK] en todos los ítems.

---

### PASO 7 — Generar el dataset

```cmd
python setup_dataset.py
```

---

### PASO 8 — Ejecutar los notebooks en orden

| # | Archivo | Tiempo est. |
|---|---------|-------------|
| 1 | leccion_01_fundamentos_bigdata.ipynb | 1-2 min |
| 2 | leccion_02_spark_configuracion.ipynb | 2-3 min |
| 3 | leccion_03_rdd_transformaciones.ipynb | 3-5 min |
| 4 | leccion_04_spark_sql_dataframes.ipynb | 5-8 min |
| 5 | leccion_05_mllib_pipeline.ipynb | 8-15 min |

Abrir cada .ipynb en VS Code → Select Kernel → elegir venv → Shift+Enter celda a celda.

> La primera celda que arranca Spark puede tardar 30-60 segundos. Es normal.

---

## 🔍 Spark UI

Mientras corre cualquier notebook, abrir en el navegador:
```
http://localhost:4040
```

---

## 🛠️ Errores Comunes en Windows

| Error | Causa | Solución |
|-------|-------|----------|
| Java gateway process exited | Java no instalado o JAVA_HOME no definida | Pasos 1 y 2 |
| java is not recognized | Java no está en el PATH | Reinstalar JDK con "Add to PATH" |
| Port 4040 already in use | Otra sesión Spark activa | Reiniciar kernel del notebook anterior |
| No module named pyspark | Intérprete equivocado | Ctrl+Shift+P → Select Interpreter → venv |
| Path does not exist (CSV) | Notebook ejecutado desde otra carpeta | Abrir VS Code desde la raíz del proyecto |

---

## 📚 Referencias

- Apache Spark Docs: https://spark.apache.org/docs/latest/
- PySpark API: https://spark.apache.org/docs/latest/api/python/
- Spark MLlib: https://spark.apache.org/docs/latest/ml-guide.html
- Fashion-MNIST: https://github.com/zalandoresearch/fashion-mnist
- JDK 11: https://adoptium.net/temurin/releases/

---

Proyecto desarrollado para el Módulo 9 — Alkemy
