# 📊 Proyecto Análisis UF 2025

## Descripción del Proyecto

Proyecto completo de análisis de datos que extrae, limpia y analiza los valores de la Unidad de Fomento (UF) del año 2025 desde el sitio web del Servicio de Impuestos Internos (SII) de Chile.

## 🎯 Objetivos de Aprendizaje

- Extracción de datos desde páginas web usando `pd.read_html()`
- Lectura y escritura de archivos CSV
- Limpieza y preparación de datos
- Análisis estadístico descriptivo con pandas y NumPy
- Exportación de resultados en múltiples formatos

## 📁 Estructura del Proyecto

```
proyecto_uf_2025/
│
├── analisis_uf_2025.ipynb      # Notebook principal con todo el análisis
├── requirements.txt            # Dependencias del proyecto
├── UF_2025.csv                # Datos de entrada (valores UF)
├── GUIA_PASO_A_PASO.md        # Guía detallada de implementación
├── README.md                  # Este archivo
│
└── Archivos generados (después de ejecutar):
    ├── UF_2025_LIMPIO.csv         # Datos limpios
    ├── UF_2025_ESTADISTICAS.csv   # Estadísticas descriptivas
    └── REPORTE_UF_2025.txt        # Reporte resumido
```

## 🚀 Inicio Rápido

### 1. Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Visual Studio Code (recomendado) o Jupyter Notebook

### 2. Instalación

```bash
# Clonar o descargar el proyecto
cd proyecto_uf_2025

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Ejecución

**Opción A: Visual Studio Code**
1. Abrir VS Code
2. Abrir la carpeta del proyecto
3. Abrir `analisis_uf_2025.ipynb`
4. Hacer clic en "Run All"

**Opción B: Jupyter Notebook**
```bash
jupyter notebook analisis_uf_2025.ipynb
```

**Opción C: JupyterLab**
```bash
jupyter lab
```

## 📊 Flujo del Proyecto

### 1. Extracción de Datos 🌐
- Extracción desde web usando `pd.read_html()`
- Lectura de archivo CSV local como alternativa

### 2. Ensuciamiento de Datos 🎭
Simulación de problemas reales:
- Valores nulos (NaN)
- Filas duplicadas
- Outliers (valores atípicos)
- Espacios en blanco
- Formatos inconsistentes
- Columnas irrelevantes

### 3. Limpieza de Datos 🧼
- Eliminación de duplicados
- Conversión de tipos de datos
- Normalización de formatos
- Detección y tratamiento de outliers
- Imputación de valores nulos
- Ordenamiento de datos

### 4. Análisis Descriptivo 📈
- Estadísticas básicas (media, mediana, desviación estándar)
- Valores extremos por mes
- Variaciones mensuales
- Correlaciones entre meses
- Análisis de tendencias anuales

### 5. Exportación 💾
- Datos limpios en CSV
- Estadísticas descriptivas en CSV
- Reporte resumido en TXT

## 📚 Librerías Utilizadas

| Librería | Versión | Uso |
|----------|---------|-----|
| pandas | >=2.0.0 | Manipulación y análisis de datos |
| numpy | >=1.24.0 | Operaciones numéricas |
| notebook | >=7.0.0 | Entorno Jupyter |
| lxml | >=4.9.0 | Parsing de HTML para read_html |
| matplotlib | >=3.7.0 | Visualización (opcional) |

## 🔍 Características Principales

### Extracción Automática Web
```python
url = 'https://www.sii.cl/valores_y_fechas/uf/uf2025.htm'
tablas = pd.read_html(url, decimal=',', thousands='.')
df = tablas[0]
```

### Limpieza Robusta
- Manejo automático de diferentes formatos
- Detección inteligente de outliers usando IQR
- Interpolación lineal para valores nulos

### Análisis Completo
- 15+ métricas estadísticas
- Análisis de correlación
- Detección de tendencias

## 📝 Ejemplos de Uso

### Cargar y limpiar datos
```python
import pandas as pd

# Leer CSV
df = pd.read_csv('UF_2025.csv', sep=';', encoding='utf-8-sig')

# Limpiar valores
def limpiar_valor_uf(valor):
    valor_str = str(valor).strip()
    valor_str = valor_str.replace('.', '').replace(',', '.')
    return float(valor_str)

df['Ene'] = df['Ene'].apply(limpiar_valor_uf)
```

### Análisis básico
```python
# Estadísticas descriptivas
print(df.describe())

# Valor promedio de UF
promedio_anual = df[meses].mean().mean()
print(f"UF Promedio 2025: ${promedio_anual:,.2f}")
```

### Detectar outliers
```python
Q1 = df['Ene'].quantile(0.25)
Q3 = df['Ene'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Ene'] < Q1 - 3*IQR) | (df['Ene'] > Q3 + 3*IQR)]
```

## 🎓 Conceptos Aprendidos

### Pandas
- `read_html()` - Extracción de tablas web
- `read_csv()` - Lectura de archivos CSV
- `drop_duplicates()` - Eliminación de duplicados
- `interpolate()` - Imputación de valores nulos
- `describe()` - Estadísticas descriptivas
- `corr()` - Matriz de correlación

### NumPy
- `np.random` - Generación de números aleatorios
- `np.nan` - Representación de valores nulos
- Operaciones vectorizadas

### Limpieza de Datos
- Detección de outliers con IQR
- Normalización de formatos
- Conversión de tipos de datos
- Manejo de valores nulos

## 🔧 Solución de Problemas Comunes

### Error: "No module named 'pandas'"
```bash
pip install pandas
```

### Error al leer HTML
```bash
pip install lxml html5lib
```

### El notebook no abre
```bash
pip install --upgrade notebook ipykernel
jupyter notebook
```

## 📈 Resultados Esperados

Al finalizar la ejecución, obtendrás:

1. **UF_2025_LIMPIO.csv**: Datos limpios y estructurados
2. **UF_2025_ESTADISTICAS.csv**: Tabla con todas las métricas
3. **REPORTE_UF_2025.txt**: Resumen ejecutivo del análisis

### Métricas Principales
- UF Promedio Anual
- UF Mínima y Máxima
- Variación Anual (%)
- Desviación Estándar por mes
- Coeficiente de Variación

## 🤝 Contribuciones

Este es un proyecto educativo. Siéntete libre de:
- Modificar el código
- Agregar visualizaciones
- Experimentar con diferentes datasets
- Compartir mejoras

## 📖 Recursos Adicionales

- **Documentación Pandas**: https://pandas.pydata.org/docs/
- **Documentación NumPy**: https://numpy.org/doc/
- **Tutorial Jupyter**: https://jupyter.org/documentation
- **Guía detallada**: Ver `GUIA_PASO_A_PASO.md`

## 📧 Soporte

Para preguntas o problemas:
1. Revisa la `GUIA_PASO_A_PASO.md`
2. Consulta la sección de Solución de Problemas
3. Revisa la documentación oficial de las librerías

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## ✨ Próximos Pasos Sugeridos

1. **Visualización**: Agregar gráficos con matplotlib/seaborn
2. **Análisis temporal**: Estudiar patrones estacionales
3. **Comparación histórica**: Comparar con años anteriores
4. **Predicción**: Implementar modelos de series temporales
5. **Dashboard**: Crear un dashboard interactivo con Streamlit

---

**Versión:** 1.0  
**Fecha:** Febrero 2025  
**Nivel:** Principiante - Intermedio  

¡Feliz análisis de datos! 📊🚀
