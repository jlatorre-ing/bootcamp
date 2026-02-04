# 📊 ANÁLISIS DE DATA WRANGLING CON PANDAS
## Caso: Empresa de Tecnología Financiera

---

## 📦 CONTENIDO DEL PAQUETE

Este paquete incluye todos los archivos necesarios para completar el análisis de caso de Data Wrangling:

### 1️⃣ **Guia_DataWrangling_PasoAPaso.docx**
   - Documento Word completo con explicaciones detalladas
   - Incluye justificación técnica de cada decisión
   - Ejemplos de código comentados
   - Tabla resumen de técnicas
   - Conclusiones y mejores prácticas

### 2️⃣ **data_wrangling_analysis.py**
   - Script Python completo listo para ejecutar
   - Implementa todos los pasos del análisis
   - Incluye comentarios explicativos
   - Genera archivos CSV y Excel de salida

### 3️⃣ **datos_financieros.csv**
   - Dataset de ejemplo con 210 registros
   - Incluye valores nulos (47 total)
   - Contiene duplicados (10 registros)
   - Datos de transacciones financieras realistas

### 4️⃣ **generar_datos_ejemplo.py**
   - Script para regenerar datos si lo necesitas
   - Puedes modificar parámetros (cantidad de registros, porcentaje de nulos, etc.)

### 5️⃣ **requirements.txt**
   - Lista de todas las bibliotecas necesarias
   - Versiones compatibles especificadas

---

## 🚀 CÓMO EMPEZAR

### Paso 1: Configurar el entorno

1. **Abre Visual Studio Code**
2. **Crea una carpeta para el proyecto** (ejemplo: `C:\DataWrangling`)
3. **Copia todos los archivos** en esa carpeta
4. **Abre la terminal** en VS Code (Terminal → New Terminal)

### Paso 2: Instalar dependencias

Ejecuta en la terminal:

```bash
pip install -r requirements.txt
```

O instala individualmente:

```bash
pip install pandas numpy openpyxl scikit-learn
```

### Paso 3: Ejecutar el análisis

```bash
python data_wrangling_analysis.py
```

---

## 📋 QUÉ VAS A OBTENER

Al ejecutar el script, se generarán:

### ✅ Archivos de salida:

1. **datos_financieros_procesados.csv**
   - Dataset limpio sin duplicados ni nulos
   - Listo para análisis posterior

2. **datos_financieros_procesados.xlsx**
   - Archivo Excel con 3 hojas:
     - `Datos Procesados`: Dataset completo
     - `Resumen Estadístico`: Análisis descriptivo
     - `Comparación`: Antes vs Después

### ✅ Información en consola:

- Reporte completo de cada paso
- Cantidad de nulos corregidos
- Duplicados eliminados
- Estadísticas descriptivas
- Resumen final del proceso

---

## 📚 ESTRUCTURA DEL ANÁLISIS

### **PASO 1: Carga y Exploración** 📊
- Importar el dataset
- Inspeccionar con `.head()`, `.info()`, `.describe()`
- Identificar valores nulos
- Detectar duplicados

### **PASO 2: Limpieza y Transformación** 🧹
- Imputar valores nulos (mediana para numéricos, moda para categóricos)
- Eliminar duplicados
- Convertir variables categóricas (One-Hot Encoding, Label Encoding)

### **PASO 3: Optimización y Estructuración** ⚙️
- Agregaciones con `groupby`
- Filtrado de datos
- Renombrar y reorganizar columnas

### **PASO 4: Exportación** 💾
- Guardar a CSV
- Exportar a Excel con múltiples hojas

---

## 💡 CONSEJOS PARA EL INFORME

Para completar el caso, tu informe debe incluir:

### 1. **Código fuente**
   ✓ Ya lo tienes en `data_wrangling_analysis.py`

### 2. **Explicación detallada**
   ✓ Usa la guía Word como referencia
   - Describe cada paso
   - Justifica técnicamente las decisiones
   - Explica por qué usaste mediana vs media, etc.

### 3. **Ejemplo antes/después**
   Incluye capturas de pantalla o tablas mostrando:
   - Dataset original con nulos y duplicados
   - Dataset procesado limpio

### 4. **Conclusiones**
   Reflexiona sobre:
   - La importancia de la calidad de datos
   - Cómo el Data Wrangling afecta análisis posteriores
   - Qué aprendiste del proceso

---

## 🎯 OBJETIVOS DE APRENDIZAJE

Al completar este caso, habrás:

- ✅ Aplicado técnicas de limpieza de datos
- ✅ Usado Pandas para transformaciones complejas
- ✅ Implementado estrategias de imputación
- ✅ Practicado agregaciones y filtrado
- ✅ Generado reportes en múltiples formatos
- ✅ Documentado decisiones técnicas

---

## 🔧 PERSONALIZACIÓN

### Modificar el dataset:

Edita `generar_datos_ejemplo.py` para cambiar:

```python
n_records = 200  # Cambia la cantidad de registros

# Ajusta el porcentaje de nulos:
null_indices_monto = np.random.choice(df.index, size=int(n_records * 0.1), replace=False)
# Cambia 0.1 por el porcentaje deseado (0.1 = 10%)
```

Luego ejecuta:
```bash
python generar_datos_ejemplo.py
```

### Adaptar el análisis:

Modifica `data_wrangling_analysis.py` para:
- Agregar nuevas transformaciones
- Incluir visualizaciones
- Aplicar filtros diferentes
- Calcular métricas adicionales

---

## 📖 RECURSOS ADICIONALES

- **Documentación Pandas**: https://pandas.pydata.org/docs/
- **Guía de Data Wrangling**: Incluida en el documento Word
- **Scikit-learn (Encoding)**: https://scikit-learn.org/stable/modules/preprocessing.html

---

## ❓ SOLUCIÓN DE PROBLEMAS

### Error: "ModuleNotFoundError: No module named 'pandas'"
**Solución**: Instala las dependencias
```bash
pip install -r requirements.txt
```

### Error: "FileNotFoundError: datos_financieros.csv"
**Solución**: Asegúrate de estar en la carpeta correcta
```bash
cd C:\DataWrangling  # o la ruta donde están los archivos
python data_wrangling_analysis.py
```

### Los archivos Excel no se abren
**Solución**: Instala openpyxl
```bash
pip install openpyxl
```

---

## 📞 NOTAS FINALES

Este paquete está diseñado para ser **educativo y práctico**. Cada paso incluye:
- Código funcional y probado
- Explicaciones técnicas claras
- Justificación de decisiones
- Ejemplos reales

**¡Éxito en tu análisis! 🚀**

---

**Fecha de creación**: Febrero 2026  
**Versión**: 1.0  
**Python**: 3.8+  
**Pandas**: 1.5.0+
