# 📊 Análisis de Caso: Obtención de Datos desde Archivos con Pandas

## 🎯 Descripción del Proyecto

Este proyecto implementa una solución automatizada para la obtención, limpieza y exportación de datos utilizando Python y Pandas. Diseñado para una empresa de consultoría que maneja grandes volúmenes de datos de múltiples fuentes.

## ✨ Características

- ✅ Carga de datos desde múltiples formatos (CSV, Excel, tablas web)
- ✅ Limpieza automática de datos (valores nulos, duplicados)
- ✅ Conversión inteligente de tipos de datos
- ✅ Transformación y optimización de datasets
- ✅ Exportación a múltiples formatos (CSV, Excel)
- ✅ Generación de reportes estadísticos

## 📋 Requisitos Previos

- Python 3.8 o superior
- Visual Studio Code (recomendado) o cualquier IDE de Python
- Conexión a internet (para instalación de librerías)

## 🚀 Instalación Rápida

### 1. Clonar o descargar el proyecto

```bash
mkdir analisis_datos_pandas
cd analisis_datos_pandas
```

### 2. Crear entorno virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

O manualmente:
```bash
pip install pandas numpy openpyxl xlrd lxml html5lib beautifulsoup4
```

## ▶️ Uso

### Ejecución del Script Principal

```bash
python analisis_datos_pandas.py
```

El script:
1. Creará archivos de ejemplo si no existen
2. Cargará los datos
3. Aplicará procesos de limpieza
4. Transformará los datos
5. Exportará los resultados

### Archivos Generados

Después de ejecutar el script, encontrarás:

```
📁 analisis_datos_pandas/
├── 📄 ventas_procesadas.csv          # Datos de ventas limpios
├── 📄 clientes_procesados.csv        # Datos de clientes limpios
├── 📊 datos_procesados.xlsx          # Excel con múltiples hojas
└── 📈 reporte_estadisticas.csv       # Resumen estadístico
```

## 📁 Estructura del Proyecto

```
analisis_datos_pandas/
│
├── 📄 analisis_datos_pandas.py       # Script principal
├── 📄 requirements.txt                # Dependencias
├── 📄 README.md                       # Este archivo
│
├── 📘 Guia_Paso_a_Paso_Analisis_Datos_Pandas.docx
│   └── Manual detallado para usuarios
│
├── 📗 Informe_Tecnico_Completo.docx
│   └── Informe técnico del caso
│
└── 📂 Archivos generados (después de ejecutar)
    ├── datos_ventas.csv
    ├── datos_clientes.xlsx
    ├── ventas_procesadas.csv
    ├── clientes_procesados.csv
    ├── datos_procesados.xlsx
    └── reporte_estadisticas.csv
```

## 🔧 Personalización

### Usar tus Propios Datos

1. Reemplaza los archivos de ejemplo con tus datos:
   - `datos_ventas.csv`
   - `datos_clientes.xlsx`

2. Ajusta las columnas en el código según tus necesidades

3. Ejecuta el script nuevamente

### Modificar la Limpieza de Datos

Edita las secciones correspondientes en `analisis_datos_pandas.py`:

```python
# Personalizar estrategia de valores nulos
df_limpio['columna'].fillna(valor_personalizado, inplace=True)

# Personalizar eliminación de duplicados
df_limpio = df_limpio.drop_duplicates(subset=['columnas_clave'])
```

## 📊 Flujo del Proceso

```
1. CARGA
   ├── CSV → pandas.read_csv()
   ├── Excel → pandas.read_excel()
   └── Web → pandas.read_html()
   
2. LIMPIEZA
   ├── Identificar nulos → isnull()
   ├── Imputar valores → fillna()
   ├── Eliminar duplicados → drop_duplicates()
   └── Convertir tipos → astype()
   
3. TRANSFORMACIÓN
   ├── Seleccionar columnas
   ├── Renombrar → rename()
   ├── Ordenar → sort_values()
   └── Calcular nuevas columnas
   
4. EXPORTACIÓN
   ├── CSV → to_csv()
   ├── Excel → to_excel()
   └── Reportes personalizados
```

## 🐛 Solución de Problemas Comunes

### Error: ModuleNotFoundError

**Solución:** Asegúrate de haber instalado todas las dependencias
```bash
pip install -r requirements.txt
```

### Error: FileNotFoundError

**Solución:** El script crea archivos de ejemplo automáticamente. Verifica estar en la carpeta correcta.

### Error: PermissionError al guardar

**Solución:** Cierra los archivos Excel que puedan estar abiertos.

### Encoding de CSV

**Solución:** Si hay problemas con caracteres especiales, prueba:
```python
pd.read_csv('archivo.csv', encoding='latin-1')
```

## 📚 Documentación Adicional

- **Guía Paso a Paso**: `Guia_Paso_a_Paso_Analisis_Datos_Pandas.docx`
  - Manual detallado con instrucciones completas
  - Capturas de pantalla y ejemplos
  - Solución de problemas extendida

- **Informe Técnico**: `Informe_Tecnico_Completo.docx`
  - Justificación técnica de decisiones
  - Análisis antes/después
  - Conclusiones y recomendaciones

## 🎓 Recursos de Aprendizaje

### Documentación Oficial
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Python Official Docs](https://docs.python.org/3/)

### Tutoriales Recomendados
- [Pandas Getting Started](https://pandas.pydata.org/getting_started.html)
- [Real Python - Pandas](https://realpython.com/learning-paths/pandas-data-science/)
- [DataCamp Pandas Tutorial](https://www.datacamp.com/tutorial/pandas)

### Comunidad
- [Stack Overflow - Tag Pandas](https://stackoverflow.com/questions/tagged/pandas)
- [r/learnpython](https://www.reddit.com/r/learnpython/)
- [Python Discord](https://discord.gg/python)

## 📊 Resultados Esperados

Al completar este caso, habrás logrado:

✅ Automatizar la carga de datos de múltiples fuentes  
✅ Implementar un pipeline robusto de limpieza de datos  
✅ Aplicar transformaciones profesionales a datasets  
✅ Generar outputs estandarizados y listos para análisis  
✅ Crear reportes estadísticos automatizados  

## 🤝 Contribuciones

Este es un proyecto educativo. Siéntete libre de:
- Modificar el código para tus necesidades
- Agregar nuevas funcionalidades
- Mejorar la documentación
- Compartir con otros estudiantes

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 📧 Contacto y Soporte

Para preguntas o soporte:
- Revisa la documentación incluida
- Consulta los recursos de aprendizaje
- Busca en Stack Overflow
- Pregunta en comunidades de Python

---

## 🎯 Próximos Pasos

1. ✅ Ejecutar el script con datos de ejemplo
2. ✅ Revisar los archivos generados
3. ✅ Leer la guía paso a paso completa
4. ✅ Experimentar con tus propios datos
5. ✅ Explorar visualización de datos (Matplotlib, Seaborn)
6. ✅ Aprender análisis estadístico con Pandas

---

**¡Éxito en tu análisis de datos!** 🚀

*Última actualización: Enero 2026*
