"""
ANÁLISIS DE CASO: OBTENCIÓN DE DATOS DESDE ARCHIVOS
Empresa de Consultoría - Automatización con Pandas

Autor: Analista de Datos
Fecha: Enero 2026
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("SISTEMA DE ANÁLISIS DE DATOS CON PANDAS")
print("="*80)
print()

# ============================================================================
# PARTE 1: CARGA DE DATOS DESDE DISTINTOS ARCHIVOS
# ============================================================================

print("📂 PASO 1: CARGA DE DATOS DESDE DISTINTOS ARCHIVOS")
print("-" * 80)

# 1.1 Cargar datos desde archivo CSV
print("\n1.1 Cargando datos desde archivo CSV...")
try:
    df_csv = pd.read_csv('datos_ventas.csv', encoding='utf-8')
    print(f"✓ CSV cargado exitosamente: {df_csv.shape[0]} filas, {df_csv.shape[1]} columnas")
    print("\nPrimeras 3 filas del CSV:")
    print(df_csv.head(3))
except FileNotFoundError:
    print("⚠ Archivo CSV no encontrado. Creando datos de ejemplo...")
    # Crear datos de ejemplo para demostración
    df_csv = pd.DataFrame({
        'ID': [1, 2, 3, 4, 5, 6, 7, 8],
        'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Laptop', 'Mouse', None, 'Auriculares'],
        'Cantidad': [5, 10, 8, 3, 5, 15, 7, None],
        'Precio': [1200.50, 25.99, 45.00, 350.00, 1200.50, 25.99, 30.00, 89.99],
        'Fecha': ['2024-01-15', '2024-01-16', '2024-01-17', None, '2024-01-15', '2024-01-18', '2024-01-19', '2024-01-20']
    })
    # Guardar para referencia
    df_csv.to_csv('datos_ventas.csv', index=False)
    print("✓ Datos de ejemplo creados y guardados")

# 1.2 Cargar datos desde archivo Excel
print("\n1.2 Cargando datos desde archivo Excel...")
try:
    df_excel = pd.read_excel('datos_clientes.xlsx', sheet_name='Clientes')
    print(f"✓ Excel cargado exitosamente: {df_excel.shape[0]} filas, {df_excel.shape[1]} columnas")
except FileNotFoundError:
    print("⚠ Archivo Excel no encontrado. Creando datos de ejemplo...")
    df_excel = pd.DataFrame({
        'ClienteID': [101, 102, 103, 104, 105, 106],
        'Nombre': ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Juan Pérez', 'Luis Rodríguez'],
        'Email': ['juan@email.com', 'maria@email.com', 'carlos@email.com', None, 'juan@email.com', 'luis@email.com'],
        'Ciudad': ['Santiago', 'Viña del Mar', 'Valparaíso', 'Santiago', 'Santiago', 'Concepción'],
        'Edad': [35, 28, 42, None, 35, 31]
    })
    df_excel.to_excel('datos_clientes.xlsx', sheet_name='Clientes', index=False)
    print("✓ Datos de ejemplo creados y guardados")

# 1.3 Extraer datos de una tabla web (simulación)
print("\n1.3 Extrayendo datos de tabla web...")
try:
    # Ejemplo real de extracción de tabla web
    # url = 'https://es.wikipedia.org/wiki/Anexo:Países_por_población'
    # df_web = pd.read_html(url)[0]
    
    # Para este ejemplo, creamos datos simulados
    print("⚠ Creando datos simulados de tabla web...")
    df_web = pd.DataFrame({
        'País': ['Chile', 'Argentina', 'Brasil', 'Perú', 'Colombia'],
        'Población': [19116201, 45195774, 212559417, 32971854, 50882891],
        'Superficie_km2': [756102, 2780400, 8515767, 1285216, 1141748]
    })
    print("✓ Datos web simulados creados exitosamente")
except Exception as e:
    print(f"✗ Error al extraer datos web: {e}")
    df_web = pd.DataFrame()

print("\n" + "="*80)

# ============================================================================
# PARTE 2: LIMPIEZA Y ESTRUCTURACIÓN DE DATOS
# ============================================================================

print("\n📊 PASO 2: LIMPIEZA Y ESTRUCTURACIÓN DE DATOS")
print("-" * 80)

# 2.1 Análisis de valores nulos
print("\n2.1 Identificando valores nulos...")
print("\nValores nulos en CSV:")
print(df_csv.isnull().sum())
print("\nValores nulos en Excel:")
print(df_excel.isnull().sum())

# Decisión sobre valores nulos
print("\n🔧 Aplicando estrategia de limpieza de valores nulos:")

# Para CSV: imputar cantidad con mediana, eliminar filas con producto nulo
print("- CSV: Eliminando filas sin producto...")
df_csv_limpio = df_csv.dropna(subset=['Producto']).copy()
print(f"  Filas eliminadas: {len(df_csv) - len(df_csv_limpio)}")

print("- CSV: Imputando cantidad faltante con mediana...")
mediana_cantidad = df_csv_limpio['Cantidad'].median()
df_csv_limpio['Cantidad'].fillna(mediana_cantidad, inplace=True)

print("- CSV: Rellenando fechas faltantes con fecha actual...")
df_csv_limpio['Fecha'].fillna(datetime.now().strftime('%Y-%m-%d'), inplace=True)

# Para Excel: imputar email vacío, edad con promedio
print("- Excel: Rellenando emails faltantes...")
df_excel_limpio = df_excel.copy()
df_excel_limpio['Email'].fillna('sin_email@ejemplo.com', inplace=True)

print("- Excel: Imputando edad con promedio...")
promedio_edad = df_excel_limpio['Edad'].mean()
df_excel_limpio['Edad'].fillna(promedio_edad, inplace=True)

# 2.2 Eliminar duplicados
print("\n2.2 Identificando y eliminando duplicados...")
print(f"\nDuplicados en CSV: {df_csv_limpio.duplicated().sum()}")
print(f"Duplicados en Excel: {df_excel_limpio.duplicated().sum()}")

df_csv_limpio = df_csv_limpio.drop_duplicates()
df_excel_limpio = df_excel_limpio.drop_duplicates()
print("✓ Duplicados eliminados")

# 2.3 Verificar y ajustar tipos de datos
print("\n2.3 Verificando y ajustando tipos de datos...")
print("\nTipos de datos ANTES (CSV):")
print(df_csv_limpio.dtypes)

# Convertir tipos de datos
df_csv_limpio['Cantidad'] = df_csv_limpio['Cantidad'].astype(int)
df_csv_limpio['Precio'] = df_csv_limpio['Precio'].astype(float)
df_csv_limpio['Fecha'] = pd.to_datetime(df_csv_limpio['Fecha'])
df_csv_limpio['Producto'] = df_csv_limpio['Producto'].astype(str)

df_excel_limpio['Edad'] = df_excel_limpio['Edad'].astype(int)
df_excel_limpio['Ciudad'] = df_excel_limpio['Ciudad'].astype('category')

print("\nTipos de datos DESPUÉS (CSV):")
print(df_csv_limpio.dtypes)

print("\n" + "="*80)

# ============================================================================
# PARTE 3: TRANSFORMACIÓN Y OPTIMIZACIÓN DE DATOS
# ============================================================================

print("\n⚙️ PASO 3: TRANSFORMACIÓN Y OPTIMIZACIÓN DE DATOS")
print("-" * 80)

# 3.1 Seleccionar columnas relevantes
print("\n3.1 Seleccionando columnas relevantes...")
columnas_csv = ['ID', 'Producto', 'Cantidad', 'Precio', 'Fecha']
df_csv_optimizado = df_csv_limpio[columnas_csv].copy()

columnas_excel = ['ClienteID', 'Nombre', 'Ciudad', 'Edad']
df_excel_optimizado = df_excel_limpio[columnas_excel].copy()
print("✓ Columnas seleccionadas")

# 3.2 Renombrar columnas
print("\n3.2 Renombrando columnas para mejorar legibilidad...")
df_csv_optimizado.rename(columns={
    'ID': 'id_venta',
    'Producto': 'nombre_producto',
    'Cantidad': 'unidades_vendidas',
    'Precio': 'precio_unitario',
    'Fecha': 'fecha_venta'
}, inplace=True)

df_excel_optimizado.rename(columns={
    'ClienteID': 'id_cliente',
    'Nombre': 'nombre_completo',
    'Ciudad': 'ciudad_residencia',
    'Edad': 'edad_anos'
}, inplace=True)

print("✓ Columnas renombradas")
print("\nNuevas columnas CSV:", list(df_csv_optimizado.columns))
print("Nuevas columnas Excel:", list(df_excel_optimizado.columns))

# 3.3 Ordenar datos
print("\n3.3 Ordenando datos por columna clave...")
df_csv_optimizado = df_csv_optimizado.sort_values('fecha_venta', ascending=False)
df_excel_optimizado = df_excel_optimizado.sort_values('id_cliente')
print("✓ Datos ordenados")

# Crear columnas calculadas adicionales
print("\n3.4 Creando columnas calculadas...")
df_csv_optimizado['total_venta'] = df_csv_optimizado['unidades_vendidas'] * df_csv_optimizado['precio_unitario']
print("✓ Columna 'total_venta' creada")

print("\n" + "="*80)

# ============================================================================
# PARTE 4: EXPORTACIÓN DE DATOS
# ============================================================================

print("\n💾 PASO 4: EXPORTACIÓN DE DATOS PROCESADOS")
print("-" * 80)

# 4.1 Exportar a CSV
print("\n4.1 Exportando a CSV...")
df_csv_optimizado.to_csv('ventas_procesadas.csv', index=False, encoding='utf-8')
print("✓ Archivo 'ventas_procesadas.csv' creado exitosamente")

df_excel_optimizado.to_csv('clientes_procesados.csv', index=False, encoding='utf-8')
print("✓ Archivo 'clientes_procesados.csv' creado exitosamente")

# 4.2 Exportar a Excel
print("\n4.2 Exportando a Excel...")
with pd.ExcelWriter('datos_procesados.xlsx', engine='openpyxl') as writer:
    df_csv_optimizado.to_excel(writer, sheet_name='Ventas', index=False)
    df_excel_optimizado.to_excel(writer, sheet_name='Clientes', index=False)
    if not df_web.empty:
        df_web.to_excel(writer, sheet_name='Paises', index=False)
print("✓ Archivo 'datos_procesados.xlsx' creado con múltiples hojas")

# 4.3 Crear reporte de estadísticas
print("\n4.3 Generando reporte de estadísticas...")
reporte = {
    'Métrica': [
        'Total de Ventas',
        'Productos Únicos',
        'Venta Promedio',
        'Total Clientes',
        'Edad Promedio Clientes'
    ],
    'Valor': [
        f"${df_csv_optimizado['total_venta'].sum():,.2f}",
        df_csv_optimizado['nombre_producto'].nunique(),
        f"${df_csv_optimizado['total_venta'].mean():,.2f}",
        len(df_excel_optimizado),
        f"{df_excel_optimizado['edad_anos'].mean():.1f} años"
    ]
}
df_reporte = pd.DataFrame(reporte)
df_reporte.to_csv('reporte_estadisticas.csv', index=False)
print("✓ Reporte de estadísticas generado")

print("\n" + "="*80)

# ============================================================================
# RESUMEN Y COMPARACIÓN
# ============================================================================

print("\n📋 RESUMEN DEL PROCESO")
print("="*80)

print("\n🔍 DATOS ANTES DE LA LIMPIEZA:")
print("\nCSV Original:")
print(df_csv.head())
print(f"\nForma: {df_csv.shape}")
print(f"Valores nulos: {df_csv.isnull().sum().sum()}")
print(f"Duplicados: {df_csv.duplicated().sum()}")

print("\n✨ DATOS DESPUÉS DE LA LIMPIEZA:")
print("\nCSV Procesado:")
print(df_csv_optimizado.head())
print(f"\nForma: {df_csv_optimizado.shape}")
print(f"Valores nulos: {df_csv_optimizado.isnull().sum().sum()}")
print(f"Duplicados: {df_csv_optimizado.duplicated().sum()}")

print("\n📊 ESTADÍSTICAS DESCRIPTIVAS:")
print(df_csv_optimizado.describe())

print("\n" + "="*80)
print("\n✅ PROCESO COMPLETADO EXITOSAMENTE")
print("="*80)
print("\n📁 Archivos generados:")
print("  1. ventas_procesadas.csv")
print("  2. clientes_procesados.csv")
print("  3. datos_procesados.xlsx")
print("  4. reporte_estadisticas.csv")
print("\n¡Gracias por utilizar el sistema de análisis de datos!")
print("="*80)
