# 📘 GUÍA PASO A PASO: Análisis de Datos UF 2025

## 📋 Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Instalación del Entorno](#instalación-del-entorno)
4. [Ejecución del Proyecto](#ejecución-del-proyecto)
5. [Explicación Detallada del Código](#explicación-detallada-del-código)
6. [Solución de Problemas](#solución-de-problemas)
7. [Glosario de Términos](#glosario-de-términos)

---

## 🎯 Introducción

Este proyecto te guiará a través de un análisis completo de datos usando Python, pandas y NumPy. Aprenderás a:

- ✅ Extraer datos desde una página web
- ✅ Limpiar datos "sucios" o con problemas
- ✅ Realizar análisis estadístico descriptivo
- ✅ Exportar resultados a archivos CSV

**Duración estimada:** 30-45 minutos  
**Nivel:** Principiante - Intermedio

---

## 💻 Requisitos Previos

### 1. Software Necesario

#### Opción A: Instalación Completa (Recomendada)

**Python 3.8 o superior**
- Descarga desde: https://www.python.org/downloads/
- Durante la instalación, marca la opción "Add Python to PATH"

**Visual Studio Code**
- Descarga desde: https://code.visualstudio.com/
- Es gratuito y multiplataforma

#### Opción B: Anaconda (Todo en uno)
- Descarga desde: https://www.anaconda.com/download
- Incluye Python, Jupyter, pandas, NumPy y más

### 2. Verificar Instalación

Abre una terminal o CMD y ejecuta:

```bash
python --version
# Debe mostrar: Python 3.8.x o superior

pip --version
# Debe mostrar la versión de pip
```

---

## 🚀 Instalación del Entorno

### PASO 1: Crear Carpeta del Proyecto

```bash
# En Windows (CMD o PowerShell)
mkdir proyecto_uf_2025
cd proyecto_uf_2025

# En Mac/Linux (Terminal)
mkdir proyecto_uf_2025
cd proyecto_uf_2025
```

### PASO 2: Copiar Archivos del Proyecto

Coloca los siguientes archivos en la carpeta `proyecto_uf_2025`:
- `analisis_uf_2025.ipynb` (el notebook principal)
- `analisis_uf_script.py` (script Python)
- `requirements.txt` (las dependencias)
- `UF_2025.csv` (los datos de entrada)

**Nota importante:** El script ahora usa **rutas absolutas**, por lo que detecta automáticamente la ubicación de los archivos. Puedes ejecutarlo desde cualquier directorio.

### PASO 3: Crear Entorno Virtual (Recomendado)

**¿Por qué un entorno virtual?**
Mantiene las dependencias del proyecto aisladas y organizadas.

```bash
# Crear entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

Cuando está activo, verás `(venv)` al inicio de la línea de comandos.

### PASO 4: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Este comando instalará:
- `pandas` - Para manipulación de datos
- `numpy` - Para operaciones numéricas
- `notebook` - Para ejecutar Jupyter Notebooks
- `matplotlib` - Para visualización (opcional)
- `lxml` - Para leer tablas HTML

**⏱️ Tiempo estimado:** 2-5 minutos

### PASO 5: Verificar Instalación

```bash
python -c "import pandas; import numpy; print('✅ Todo instalado correctamente')"
```

---

## 📓 Ejecución del Proyecto

### Método 1: Visual Studio Code (Recomendado)

1. **Abrir VS Code**
2. **Instalar extensión de Python:**
   - Ve a Extensions (Ctrl+Shift+X)
   - Busca "Python" (de Microsoft)
   - Haz clic en "Install"

3. **Instalar extensión de Jupyter:**
   - En Extensions, busca "Jupyter"
   - Instala "Jupyter" (de Microsoft)

4. **Abrir el proyecto:**
   - File → Open Folder
   - Selecciona la carpeta `proyecto_uf_2025`

5. **Abrir el notebook:**
   - Haz doble clic en `analisis_uf_2025.ipynb`
   - Selecciona el kernel de Python (arriba a la derecha)

6. **Ejecutar el código:**
   - **Opción A:** Haz clic en "Run All" (▶▶ arriba)
   - **Opción B:** Ejecuta celda por celda con Shift+Enter

### Método 2: Jupyter Notebook Clásico

```bash
# Asegúrate de estar en la carpeta del proyecto
jupyter notebook
```

Esto abrirá tu navegador. Luego:
1. Haz clic en `analisis_uf_2025.ipynb`
2. Cell → Run All (o Shift+Enter para ejecutar celda por celda)

### Método 3: JupyterLab

```bash
jupyter lab
```

Similar a Jupyter Notebook pero con interfaz más moderna.

---

## 🔍 Explicación Detallada del Código

### SECCIÓN 1: Importación de Librerías

```python
import pandas as pd
import numpy as np
import warnings
from datetime import datetime
```

**¿Qué hace cada línea?**

- `import pandas as pd`: Importa pandas (herramienta principal para datos) y le da el alias "pd"
- `import numpy as np`: Importa numpy (operaciones numéricas) con alias "np"
- `import warnings`: Para controlar mensajes de advertencia
- `from datetime import datetime`: Para trabajar con fechas

**Configuración de pandas:**
```python
pd.set_option('display.max_columns', None)  # Muestra todas las columnas
pd.set_option('display.max_rows', 100)      # Muestra hasta 100 filas
pd.set_option('display.float_format', '{:.2f}'.format)  # 2 decimales
```

---

### SECCIÓN 2: Extracción de Datos Web

```python
url = 'https://www.sii.cl/valores_y_fechas/uf/uf2025.htm'
tablas = pd.read_html(url, decimal=',', thousands='.')
df_web = tablas[0]
```

**Explicación paso a paso:**

1. **`url =`**: Guardamos la dirección web en una variable
2. **`pd.read_html()`**: Función mágica que lee TODAS las tablas HTML de una página
   - `decimal=','`: En Chile usamos coma para decimales (38.419,17)
   - `thousands='.'`: Punto para miles (38.419,17)
3. **`tablas`**: Es una LISTA de DataFrames (uno por cada tabla encontrada)
4. **`tablas[0]`**: Tomamos la primera tabla (índice 0 en Python)

**💡 Consejo:** Si la página tiene múltiples tablas, puedes ver cuántas hay con `len(tablas)` y explorar cada una.

---

### SECCIÓN 3: Carga desde CSV

```python
df_csv = pd.read_csv('UF_2025.csv', sep=';', encoding='utf-8-sig')
```

**Parámetros explicados:**

- **`'UF_2025.csv'`**: Nombre del archivo a cargar
- **`sep=';'`**: El separador de columnas es punto y coma (típico en Excel español)
- **`encoding='utf-8-sig'`**: Codificación para caracteres especiales (ñ, á, etc.)

**Alternativas de separadores:**
- `sep=','` → Archivos CSV estándar
- `sep='\t'` → Archivos separados por tabulaciones (TSV)
- `sep='|'` → Separador pipe

---

### SECCIÓN 4: Ensuciamiento de Datos

**¿Por qué ensuciar datos que ya están limpios?**

Para simular problemas reales que encontrarás en el mundo laboral:

#### Tipo 1: Valores Nulos

```python
indices_nulos = np.random.choice(df.index, size=int(len(df) * 0.05), replace=False)
df.loc[indices_nulos, mes] = np.nan
```

**Explicación:**
- Selecciona el 5% de las filas al azar
- Les asigna `NaN` (Not a Number = valor nulo)
- Simula datos faltantes o no registrados

#### Tipo 2: Duplicados

```python
filas_duplicar = df.sample(n=3, random_state=42)
df = pd.concat([df, filas_duplicar], ignore_index=True)
```

**Explicación:**
- `sample(n=3)`: Toma 3 filas al azar
- `concat()`: Pega las filas duplicadas al final
- `ignore_index=True`: Resetea los índices

#### Tipo 3: Outliers (Valores Atípicos)

```python
df.loc[idx, mes] = '99.999,99'  # Valor extremadamente alto
```

Simula errores de digitación o mediciones incorrectas.

#### Tipo 4: Espacios en Blanco

```python
df.loc[idx, mes] = df.loc[idx, mes].astype(str) + '  '
```

Espacios al final que pueden causar problemas al convertir a números.

#### Tipo 5: Formatos Inconsistentes

```python
df.loc[5, 'Día'] = '6.'        # Con punto
df.loc[10, 'Día'] = 'Día 11'   # Con texto
```

Datos ingresados de forma no estándar.

---

### SECCIÓN 5: Limpieza de Datos

#### PASO 1: Eliminar Columnas Irrelevantes

```python
if 'Comentarios' in df.columns:
    df = df.drop('Comentarios', axis=1)
```

**Explicación:**
- `'Comentarios' in df.columns`: Verifica si existe la columna
- `df.drop()`: Elimina la columna
- `axis=1`: Indica que estamos eliminando columnas (axis=0 sería filas)

#### PASO 2: Eliminar Duplicados

```python
df = df.drop_duplicates()
df = df.reset_index(drop=True)
```

**Explicación:**
- `drop_duplicates()`: Elimina filas completamente idénticas
- `reset_index(drop=True)`: Reinicia los índices (0, 1, 2, 3...)

#### PASO 3: Limpiar Columna 'Día'

```python
df['Día'] = df['Día'].astype(str).str.replace('.', '', regex=False)
df['Día'] = df['Día'].str.extract(r'(\d+)')[0]
df['Día'] = pd.to_numeric(df['Día'], errors='coerce')
```

**Paso a paso:**
1. Convertir todo a texto (string)
2. Eliminar puntos
3. Extraer solo los dígitos con expresión regular `\d+`
4. Convertir a número (valores inválidos se vuelven NaN)

**💡 Expresiones Regulares:**
- `\d` = cualquier dígito (0-9)
- `+` = uno o más
- `\d+` = uno o más dígitos seguidos

#### PASO 4: Limpiar Valores UF

```python
def limpiar_valor_uf(valor):
    if pd.isna(valor):
        return np.nan
    
    valor_str = str(valor).strip()
    valor_str = valor_str.replace('.', '')   # 38.419,17 → 38419,17
    valor_str = valor_str.replace(',', '.')  # 38419,17 → 38419.17
    
    try:
        return float(valor_str)
    except:
        return np.nan
```

**¿Qué hace?**
1. Si el valor es nulo (NaN), lo deja así
2. Convierte a texto y quita espacios (`.strip()`)
3. Elimina puntos de miles
4. Cambia coma decimal por punto (formato inglés)
5. Intenta convertir a número flotante
6. Si falla, devuelve NaN

**Aplicar la función a todas las columnas:**
```python
for mes in meses:
    if mes in df.columns:
        df[mes] = df[mes].apply(limpiar_valor_uf)
```

#### PASO 5: Eliminar Outliers

**Método IQR (Rango Intercuartílico):**

```python
Q1 = df[mes].quantile(0.25)  # Primer cuartil (25%)
Q3 = df[mes].quantile(0.75)  # Tercer cuartil (75%)
IQR = Q3 - Q1                # Rango intercuartílico
limite_inferior = Q1 - 3 * IQR
limite_superior = Q3 + 3 * IQR
```

**Visualización:**
```
       Q1        Q2         Q3
        |    IQR  |          |
|-------|---------|----------|-------|
    outlier                   outlier
```

**Regla:** Valores fuera de Q1 - 3×IQR y Q3 + 3×IQR son outliers extremos.

#### PASO 6: Imputación de Valores Nulos

```python
df[mes] = df[mes].interpolate(method='linear', limit_direction='both')
```

**Interpolación lineal:**
- Si tienes: `[10, NaN, 14]`
- Resultado: `[10, 12, 14]`
- Calcula el punto medio entre valores conocidos

**Alternativas:**
- `method='ffill'`: Forward fill (repite el valor anterior)
- `method='bfill'`: Backward fill (usa el valor siguiente)
- `fillna(df[mes].mean())`: Rellena con el promedio

---

### SECCIÓN 6: Análisis Descriptivo

#### Estadísticas Básicas

```python
df.describe()
```

Genera automáticamente:
- **count**: Cantidad de valores no nulos
- **mean**: Promedio
- **std**: Desviación estándar
- **min**: Valor mínimo
- **25%**: Primer cuartil
- **50%**: Mediana
- **75%**: Tercer cuartil
- **max**: Valor máximo

#### Estadísticas Personalizadas

```python
estadisticas_mes = pd.DataFrame({
    'Promedio': df[meses].mean(),
    'Mediana': df[meses].median(),
    'Desv_Std': df[meses].std(),
    'Mínimo': df[meses].min(),
    'Máximo': df[meses].max(),
    'Rango': df[meses].max() - df[meses].min(),
    'Coef_Variación_%': (df[meses].std() / df[meses].mean() * 100)
})
```

**Coeficiente de Variación:**
- Mide la variabilidad relativa
- Fórmula: (Desviación Estándar / Media) × 100
- Valores bajos (<10%) = datos muy consistentes
- Valores altos (>50%) = datos muy variables

---

### SECCIÓN 7: Exportación de Datos

#### Exportar a CSV

```python
df.to_csv('UF_2025_LIMPIO.csv', index=False, encoding='utf-8-sig')
```

**Parámetros:**
- `index=False`: No incluye la columna de índices
- `encoding='utf-8-sig'`: Para que Excel abra correctamente los acentos

#### Crear Reporte de Texto

```python
with open('REPORTE_UF_2025.txt', 'w', encoding='utf-8') as f:
    f.write(reporte)
```

**Explicación:**
- `open()`: Abre/crea el archivo
- `'w'`: Modo escritura (write)
- `with`: Cierra automáticamente el archivo al terminar
- `f.write()`: Escribe el contenido

---

## 🐛 Solución de Problemas

### Problema 1: "No module named 'pandas'"

**Solución:**
```bash
pip install pandas
```

### Problema 2: Error al leer el CSV

**Error:** `UnicodeDecodeError`

**Solución:**
Prueba diferentes encodings:
```python
df = pd.read_csv('archivo.csv', encoding='latin1')
# o
df = pd.read_csv('archivo.csv', encoding='ISO-8859-1')
```

### Problema 3: Jupyter no abre

**Solución:**
```bash
# Desinstalar y reinstalar
pip uninstall notebook
pip install notebook

# Limpiar caché
jupyter notebook --generate-config
```

### Problema 4: "Kernel appears to be dead"

**Soluciones:**
1. Restart Kernel (en menú Kernel)
2. Cierra Jupyter y ejecuta:
```bash
pip install --upgrade ipykernel
```

### Problema 5: read_html no funciona

**Error:** `No tables found`

**Soluciones:**
1. Instala lxml:
```bash
pip install lxml html5lib
```

2. Verifica la URL en el navegador
3. Usa el CSV como respaldo

---

## 📚 Glosario de Términos

### Conceptos de Python

**DataFrame**: Tabla de datos de pandas (como Excel en Python)  
**Series**: Una columna de un DataFrame  
**NaN**: Not a Number - valor nulo o faltante  
**Index**: Índice numérico de las filas (0, 1, 2, ...)  
**Path absoluto**: Ruta completa desde la raíz del sistema  
**Path relativo**: Ruta desde el directorio actual

### Conceptos Estadísticos

**Media/Promedio**: Suma de valores ÷ cantidad de valores  
**Mediana**: Valor del medio cuando ordenas los datos  
**Moda**: Valor que más se repite  
**Desviación Estándar**: Mide qué tan dispersos están los datos  
**Cuartil**: Divide los datos en 4 partes iguales  
**Outlier**: Valor atípico que se aleja mucho del resto  
**IQR (Rango Intercuartílico)**: Q3 - Q1, rango del 50% central de datos

### Operaciones de Pandas

**`.head(n)`**: Muestra las primeras n filas  
**`.tail(n)`**: Muestra las últimas n filas  
**`.info()`**: Información general del DataFrame  
**`.describe()`**: Estadísticas descriptivas  
**`.shape`**: Dimensiones (filas, columnas)  
**`.columns`**: Lista de nombres de columnas  
**`.dtypes`**: Tipos de datos de cada columna

### Métodos de Limpieza

**`.drop()`**: Eliminar filas o columnas  
**`.drop_duplicates()`**: Eliminar duplicados  
**`.fillna()`**: Rellenar valores nulos  
**`.interpolate()`**: Interpolar valores faltantes  
**`.replace()`**: Reemplazar valores  
**`.astype()`**: Cambiar tipo de dato

---

## 🎓 Ejercicios Propuestos

### Ejercicio 1: Básico
Modifica el código para calcular el promedio de UF solo de los meses de verano (Ene, Feb, Dic).

### Ejercicio 2: Intermedio
Crea una nueva columna llamada 'Trimestre' que indique a qué trimestre pertenece cada mes.

### Ejercicio 3: Avanzado
Implementa una función que detecte cambios bruscos (>1%) de un día a otro y los marque.

---

## 📞 Recursos Adicionales

### Documentación Oficial
- **Pandas**: https://pandas.pydata.org/docs/
- **NumPy**: https://numpy.org/doc/
- **Python**: https://docs.python.org/3/

### Tutoriales Recomendados
- **Pandas Tutorial**: https://www.w3schools.com/python/pandas/
- **Real Python**: https://realpython.com/
- **DataCamp**: https://www.datacamp.com/

### Comunidades
- **Stack Overflow**: Para preguntas técnicas
- **Reddit r/learnpython**: Comunidad de aprendizaje
- **Discord PyData**: Comunidad de ciencia de datos

---

## ✅ Checklist de Finalización

- [ ] Python instalado y funcionando
- [ ] VS Code con extensiones de Python y Jupyter
- [ ] Entorno virtual creado y activado
- [ ] Todas las dependencias instaladas
- [ ] Notebook ejecutado sin errores
- [ ] Archivos CSV exportados correctamente
- [ ] Entiendes cada sección del código
- [ ] Probaste modificar algunos parámetros

---

## 🎉 ¡Felicitaciones!

Has completado un proyecto completo de análisis de datos. Ahora tienes las habilidades para:

✅ Extraer datos de la web  
✅ Limpiar datos con problemas  
✅ Realizar análisis estadístico  
✅ Exportar resultados profesionales  

**Próximo paso:** Intenta aplicar estas técnicas a tus propios datasets.

---

## 🎯 Cambios en v1.1

✅ **Rutas absolutas implementadas**: El script detecta su ubicación automáticamente  
✅ **Validación web inteligente**: Respaldo automático a CSV  
✅ **Compatible con espacios en rutas**: OneDrive, Google Drive, etc.  
✅ **Mejor manejo de tipos**: Conversión robusta de datos chilenos  

---

**Versión:** 1.1  
**Última actualización:** Febrero 2026  
**Estado:** ✅ Productivo
