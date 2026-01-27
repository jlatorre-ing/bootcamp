# 📊 Análisis de Caso: NumPy en Análisis Financiero

## 🎯 Objetivo del Proyecto

Implementar una solución de análisis financiero utilizando NumPy para optimizar el procesamiento de grandes volúmenes de datos sobre el rendimiento de activos en bolsa.

## 📋 Requerimientos del Sistema

### Requerimientos Generales
- **Sistema Operativo**: Windows 10/11, macOS 10.15+, o Linux
- **Python**: Versión 3.8 o superior
- **Espacio en disco**: 100 MB mínimo
- **RAM**: 2 GB mínimo (4 GB recomendado)

### Requerimientos Técnicos
- **Python 3.8+**: Lenguaje de programación principal
- **NumPy 1.24.0+**: Librería para computación numérica
- **Visual Studio Code**: Editor de código recomendado

## 🚀 Instalación y Configuración

### 1. Verificar Python
```bash
python --version
# Debe mostrar Python 3.8.x o superior
```

### 2. Crear entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Verificar instalación
```bash
python -c "import numpy; print(f'NumPy versión: {numpy.__version__}')"
```

## 📁 Estructura del Proyecto

```
proyecto-numpy-financiero/
│
├── analisis_numpy_financiero.py    # Script principal de análisis
├── requirements.txt                 # Dependencias del proyecto
├── README.md                        # Este archivo
└── Documentacion_Analisis_NumPy.docx  # Documento explicativo detallado
```

## 💻 Uso del Programa

### Ejecución en Visual Studio Code

1. **Abrir el proyecto**:
   - Abrir VS Code
   - File > Open Folder > Seleccionar carpeta del proyecto

2. **Configurar el intérprete**:
   - Ctrl+Shift+P (Cmd+Shift+P en Mac)
   - Escribir "Python: Select Interpreter"
   - Seleccionar el entorno virtual creado

3. **Ejecutar el script**:
   - Abrir `analisis_numpy_financiero.py`
   - Presionar F5 o click derecho > "Run Python File"
   - O desde terminal: `python analisis_numpy_financiero.py`

### Ejecución desde Terminal

```bash
# Activar entorno virtual
source venv/bin/activate  # macOS/Linux
# o
venv\Scripts\activate  # Windows

# Ejecutar análisis
python analisis_numpy_financiero.py
```

## 📊 Funcionalidades Implementadas

### ✅ Tarea 1: Carga y Estructuración de Datos
- Creación de array NumPy con datos simulados
- Organización en matriz 5×5 (5 acciones × 5 días)
- Visualización formateada de datos

### ✅ Tarea 2: Análisis y Transformación
- Cálculo de estadísticas (promedio, máximo, mínimo)
- Variación porcentual diaria
- Transformaciones matemáticas (logaritmo, normalización, z-scores)

### ✅ Tarea 3: Optimización y Selección
- Indexación avanzada (slicing, boolean, fancy indexing)
- Broadcasting para operaciones sin bucles
- Selección eficiente de datos específicos

### ✅ Tarea 4: Comparación de Rendimiento
- Benchmarking NumPy vs Python puro
- Análisis de speedup (mejora de velocidad)
- Justificación técnica del uso de NumPy

## 🔍 Salida Esperada

El programa genera un reporte completo en consola con:

1. **Matriz de precios**: Visualización 5×5 de datos financieros
2. **Estadísticas**: Promedios, máximos, mínimos por acción
3. **Variaciones**: Cambios porcentuales día a día
4. **Transformaciones**: Datos normalizados y estandarizados
5. **Ejemplos de indexación**: Acceso a datos específicos
6. **Broadcasting**: Operaciones vectorizadas eficientes
7. **Comparación**: Benchmarks de rendimiento NumPy vs Python

## 📚 Fuentes y Referencias

### Documentación Oficial NumPy
1. **NumPy User Guide**: https://numpy.org/doc/stable/user/index.html
2. **Array Creation**: https://numpy.org/doc/stable/user/basics.creation.html
3. **Indexing**: https://numpy.org/doc/stable/user/basics.indexing.html
4. **Broadcasting**: https://numpy.org/doc/stable/user/basics.broadcasting.html
5. **Mathematical Functions**: https://numpy.org/doc/stable/reference/routines.math.html
6. **Statistics**: https://numpy.org/doc/stable/reference/routines.statistics.html

### Artículos Académicos y Técnicos
1. **"NumPy: A Guide to NumPy"** - Travis Oliphant (Creador de NumPy)
   - https://numpy.org/doc/stable/

2. **"Array programming with NumPy"** - Harris et al. (2020)
   - Nature, 585, 357–362
   - DOI: 10.1038/s41586-020-2649-2
   - https://www.nature.com/articles/s41586-020-2649-2

3. **"Performance Python"** - Real Python
   - https://realpython.com/numpy-array-programming/

### Tutoriales y Recursos
1. **NumPy Quickstart**: https://numpy.org/doc/stable/user/quickstart.html
2. **NumPy for MATLAB Users**: https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
3. **SciPy Lectures**: https://scipy-lectures.org/intro/numpy/index.html

### Optimización y Rendimiento
1. **"Why NumPy is Fast"**: https://numpy.org/doc/stable/user/whatisnumpy.html#why-is-numpy-fast
2. **"Writing Fast NumPy Code"**: https://numpy.org/doc/stable/user/c-info.how-to-extend.html

## 🎓 Conceptos Clave Implementados

### 1. Arrays Multidimensionales
- Creación con `np.zeros()`, `np.random.uniform()`
- Operaciones vectorizadas
- Manipulación de shapes y dimensiones

### 2. Operaciones Estadísticas
- `np.mean()`: Cálculo de promedios
- `np.max()`, `np.min()`: Valores extremos
- `np.std()`, `np.var()`: Desviación y varianza

### 3. Indexación
- **Slicing**: `array[start:end]`
- **Boolean indexing**: `array[array > threshold]`
- **Fancy indexing**: `array[[0, 2, 4]]`

### 4. Broadcasting
- Operaciones escalares: `array * scalar`
- Arrays de diferentes shapes
- Optimización automática de bucles

### 5. Funciones Matemáticas
- `np.log()`: Logaritmo natural
- Normalización Min-Max
- Z-score standardization

## ⚡ Ventajas de NumPy

| Aspecto | Python Puro | NumPy |
|---------|-------------|-------|
| **Velocidad** | Bucles en Python | Operaciones en C (10-100x más rápido) |
| **Memoria** | Listas heterogéneas | Arrays homogéneos (menor uso) |
| **Código** | Verbose, muchos bucles | Conciso, vectorizado |
| **Funcionalidad** | Limitada | Extensa biblioteca matemática |

## 🐛 Solución de Problemas

### Error: "No module named 'numpy'"
```bash
pip install numpy
```

### Error: "Python no reconocido como comando"
- Verificar que Python esté en el PATH del sistema
- Reinstalar Python marcando "Add to PATH"

### Error de versión de NumPy
```bash
pip install --upgrade numpy
```

## 📧 Contacto y Soporte

Para preguntas o problemas:
1. Revisar la documentación oficial de NumPy
2. Consultar Stack Overflow: https://stackoverflow.com/questions/tagged/numpy
3. GitHub Issues de NumPy: https://github.com/numpy/numpy/issues

## 📄 Licencia

Este proyecto es material educativo para análisis de caso académico.

---

**Nota**: Este proyecto fue desarrollado como parte de un análisis de caso para demostrar la aplicación práctica de NumPy en el análisis de datos financieros.