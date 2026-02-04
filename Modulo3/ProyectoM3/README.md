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
- Conexión a Internet (para extracción de datos web)

**Nota:** El script ahora usa rutas absolutas, por lo que funciona correctamente incluso si se ejecuta desde directorios diferentes.

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
| html5lib | >=1.1.0 | Parser alternativo para read_html |
| matplotlib | >=3.7.0 | Visualización (opcional) |

## 🔍 Características Principales

### Extracción Automática Web con Validación
```python
url = 'https://www.sii.cl/valores_y_fechas/uf/uf2025.htm'
tablas = pd.read_html(url, decimal=',', thousands='.')
df_web = tablas[0]

# Validación inteligente de estructura
meses_encontrados = [mes for mes in MESES if mes in df_web.columns]
if len(meses_encontrados) >= 10: (chilenos y estándar)
- Detección inteligente de outliers usando método IQR (3×desviación)
- Interpolación lineal para valores nulos
- Conversión segura de tipos de datos
- Manejo de valores con espacios en blanco
- Soporte para caracteres especiales (ñ, á, é, etc.)
    df = pd.read_csv(ARCHIVO_ENTRADA)  # Respaldo a CSV local
```

**Ventaja:** Si la estructura web cambia, automáticamente usa el archivo CSV local como respaldo.

### Limpieza Robusta
- Manejo automático de diferentes formatos
- Detección inteligente de outliers usando IQR
- 7+ métricas estadísticas por mes (promedio, mediana, desv. estándar, etc.)
- Análisis de variación mensual y anual
- Identificación de valores extremos
- Coeficiente de variación para análisis de dispersión
- Resumen anual conompleto
- 15+ métricas estadísticas
- Análisis de correlación
- Detección de tendencias

## 📝 Ejemplos de Uso

### Cargar datos con rutas absolutas
```python
import pandas as pd
import os

# Rutas absolutas basadas en la ubicación del script
script_dir = os.path.dirname(os.path.abspath(__file__))
archivo_entrada = os.path.join(script_dir, 'UF_2025.csv')

# Leer CSV
df = pd.read_csv(archivo_entrada, sep=';', encoding='utf-8-sig')
print(f"Datos cargados desde: {archivo_entrada}")
```

### Limpiar valores UF (formato chileno)
```python
def limpiar_valor_uf(valor):
    if pd.isna(valor):
        return np.nan
    valor_str = str(valor).strip()
    valor_str = valor_str.replace('.', '')      # Eliminar miles
    valor_str = valor_str.replace(',', '.')     # Decimal a punto
    try:
        return float(valor_str)
    except:
        return np.nan

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

### Detectar outliers con IQR
```python
def detectar_outliers(data, columna, k=3):
    """Detecta outliers usando método IQR
    k=3 es método conservador (99.7% de confianza)
    """
    Q1 = data[columna].quantile(0.25)
    Q3 = data[columna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inf = Q1 - k * IQR
    limite_sup = Q3 + k * IQR
    return data[(data[columna] < limite_inf) | (data[columna] > limite_sup)]

outliers = detectar_outliers(df, 'Ene', k=3)
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
pip install pandas numpy
```

### Error: "FileNotFoundError: UF_2025.csv not found"
**Causa:** El script se ejecuta desde otro directorio.

**Solución:** El script ahora usa rutas absolutas automáticamente. Asegúrate de ejecutar desde la carpeta correcta:
```bash
cd ruta/al/proyecto
python analisis_uf_script.py
```

### Error al leer HTML: "No tables found"
```bash
pip install lxml html5lib
```
Si persiste, el script usa automáticamente el CSV local como respaldo.

### El notebook no abre
```bash
pip install --upgrade notebook ipykernel
jupyter notebook
```

## 📈 Resultados Esperados

Al finalizar la ejecución, obtendrás 3 archivos en la misma carpeta del proyecto:

1. **UF_2025_LIMPIO.csv**: Datos limpios y estructurados (34 filas × 13 columnas)
2. **UF_2025_ESTADISTICAS.csv**: Tabla con todas las métricas (12 meses × 7 estadísticas)
3. **REPORTE_UF_2025.txt**: Resumen ejecutivo del análisis

### Métricas Principales por Mes
- **Promedio**: Valor medio de UF
- **Mediana**: Valor del medio
- **Desv_Std**: Desviación estándar
- **Mínimo/Máximo**: Valores extremos
- **Rango**: Diferencia entre máximo y mínimo
- **CV_%**: Coeficiente de variación (dispersión relativa)

### Resumen Anual
- UF inicio (01-Ene): ~$38,419.17
- UF final (31-Dic): ~$39,727.96
- Variación anual: +3.41%

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

## ⚙️ Características Técnicas Importantes

### Rutas Absolutas (Portabilidad)
```python
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_ENTRADA = os.path.join(SCRIPT_DIR, 'UF_2025.csv')
```
✅ El script funciona desde cualquier directorio  
✅ Perfecto para clonarlo en cualquier máquina

### Validación Inteligente de Datos
- Si la web está disponible → Usa datos frescos
- Si la estructura web cambió → Automáticamente respaldo a CSV
- Si ambos fallan → Muestra error claro

### Conversión de Tipos Robusta
- Maneja formatos chilenos (38.419,17)
- Maneja formatos internacionales (38419.17)
- Convierte con seguridad a float

## ✨ Próximos Pasos Sugeridos

1. **Visualización**: Agregar gráficos con matplotlib/seaborn
2. **Análisis temporal**: Estudiar patrones estacionales
3. **Comparación histórica**: Comparar UF 2024 vs 2025
4. **Predicción**: Implementar modelos de series temporales
5. **Dashboard**: Crear un dashboard interactivo con Streamlit o Dash
6. **API**: Exponer los resultados vía API REST con Flask/FastAPI

---

## 🎯 Cambios Recientes (v1.1)

✅ **Rutas absolutas**: El script ahora funciona desde cualquier directorio  
✅ **Validación web inteligente**: Respaldo automático a CSV si la web falla  
✅ **Mejor manejo de tipos**: Conversión robusta de datos chilenos  
✅ **Soporte completo de rutas**: Compatible con espacios en rutas (OneDrive, etc.)  
✅ **Compatibilidad notebook**: Sincronizado con analisis_uf_2025.ipynb  

---

**Versión:** 1.1  
**Fecha:** Febrero 2026  
**Nivel:** Principiante - Intermedio  
**Estado:** ✅ Producción - Probado y funcional  

**Autor:** Analista de Datos  
**Fuente de datos:** Servicio de Impuestos Internos (SII) Chile

¡Feliz análisis de datos! 📊🚀
