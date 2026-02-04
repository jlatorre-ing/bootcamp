"""
ANÁLISIS DE CASO: DATA WRANGLING CON PANDAS
Empresa de Tecnología Financiera
Autor: Científico de Datos
Fecha: Febrero 2026
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("ANÁLISIS DE CASO: DATA WRANGLING CON PANDAS")
print("Empresa de Tecnología Financiera")
print("="*80)

# ============================================================================
# PASO 1: CARGA Y EXPLORACIÓN DE DATOS
# ============================================================================
print("\n📊 PASO 1: CARGA Y EXPLORACIÓN DE DATOS")
print("-"*80)

# Cargar el dataset
print("\n✓ Cargando datos del archivo CSV...")
df = pd.read_csv('datos_financieros.csv')
print(f"Dataset cargado exitosamente: {df.shape[0]} filas, {df.shape[1]} columnas")

# Inspección inicial con head()
print("\n📋 Primeras 5 filas del dataset:")
print(df.head())

# Información general con info()
print("\n📋 Información del dataset:")
print(df.info())

# Estadísticas descriptivas con describe()
print("\n📋 Estadísticas descriptivas:")
print(df.describe())

# Identificar valores nulos
print("\n⚠️  Valores nulos por columna:")
null_counts = df.isnull().sum()
print(null_counts[null_counts > 0])
print(f"\nTotal de valores nulos: {df.isnull().sum().sum()}")

# Identificar duplicados
print("\n⚠️  Registros duplicados:")
duplicates = df.duplicated().sum()
print(f"Total de duplicados encontrados: {duplicates}")
if duplicates > 0:
    print("\nEjemplo de registros duplicados:")
    print(df[df.duplicated(keep=False)].head())

# ============================================================================
# PASO 2: LIMPIEZA Y TRANSFORMACIÓN DE DATOS
# ============================================================================
print("\n\n🧹 PASO 2: LIMPIEZA Y TRANSFORMACIÓN DE DATOS")
print("-"*80)

# Guardar el estado original para comparación
df_original = df.copy()

# 2.1 Imputación de valores nulos
print("\n✓ Imputando valores nulos...")

# Para columnas numéricas: usar la mediana (más robusta ante outliers)
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        median_value = df[col].median()
        df[col].fillna(median_value, inplace=True)
        print(f"  - {col}: {null_counts[col]} valores nulos imputados con mediana ({median_value:.2f})")

# Para columnas categóricas: usar la moda
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        mode_value = df[col].mode()[0]
        df[col].fillna(mode_value, inplace=True)
        print(f"  - {col}: {null_counts[col]} valores nulos imputados con moda ({mode_value})")

# 2.2 Eliminación de duplicados
print("\n✓ Eliminando registros duplicados...")
initial_rows = len(df)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
removed_duplicates = initial_rows - len(df)
print(f"  - {removed_duplicates} registros duplicados eliminados")
print(f"  - Dataset resultante: {len(df)} filas")

# 2.3 Conversión de variables categóricas a numéricas
print("\n✓ Convirtiendo variables categóricas a numéricas...")

# Ejemplo: One-Hot Encoding para columna 'tipo_transaccion'
if 'tipo_transaccion' in df.columns:
    df_encoded = pd.get_dummies(df, columns=['tipo_transaccion'], prefix='tipo')
    print("  - Columna 'tipo_transaccion' convertida usando One-Hot Encoding")
    print(f"  - Nuevas columnas creadas: {[col for col in df_encoded.columns if col.startswith('tipo_')]}")
    df = df_encoded

# Ejemplo: Label Encoding para columna 'estado'
if 'estado' in df.columns:
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    df['estado_encoded'] = le.fit_transform(df['estado'])
    print(f"  - Columna 'estado' codificada: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# ============================================================================
# PASO 3: OPTIMIZACIÓN Y ESTRUCTURACIÓN DE DATOS
# ============================================================================
print("\n\n⚙️  PASO 3: OPTIMIZACIÓN Y ESTRUCTURACIÓN DE DATOS")
print("-"*80)

# 3.1 Agregaciones con groupby
print("\n✓ Aplicando agregaciones...")

# Agrupar por cliente y calcular estadísticas
if 'cliente_id' in df.columns and 'monto' in df.columns:
    agg_cliente = df.groupby('cliente_id').agg({
        'monto': ['sum', 'mean', 'count'],
        'fecha': 'max'
    }).round(2)
    print("\n📊 Resumen por Cliente (primeros 5):")
    print(agg_cliente.head())

# Agrupar por tipo de transacción
tipo_cols = [col for col in df.columns if col.startswith('tipo_')]
if tipo_cols and 'monto' in df.columns:
    print("\n📊 Resumen por Tipo de Transacción:")
    for col in tipo_cols:
        if df[col].sum() > 0:
            total = df[df[col] == 1]['monto'].sum()
            count = df[col].sum()
            print(f"  - {col}: ${total:,.2f} ({count} transacciones)")

# 3.2 Filtrado de datos
print("\n✓ Filtrando datos de interés...")

# Ejemplo: Transacciones mayores a $1000
if 'monto' in df.columns:
    df_high_value = df[df['monto'] > 1000]
    print(f"  - Transacciones > $1,000: {len(df_high_value)} registros")
    print(f"  - Monto total: ${df_high_value['monto'].sum():,.2f}")

# Ejemplo: Transacciones del último mes
if 'fecha' in df.columns:
    df['fecha'] = pd.to_datetime(df['fecha'])
    ultimo_mes = df['fecha'].max() - pd.Timedelta(days=30)
    df_recent = df[df['fecha'] >= ultimo_mes]
    print(f"  - Transacciones últimos 30 días: {len(df_recent)} registros")

# 3.3 Renombrar y reorganizar columnas
print("\n✓ Reorganizando estructura del DataFrame...")

# Renombrar columnas para mejor interpretación
rename_dict = {
    'cliente_id': 'ID_Cliente',
    'monto': 'Monto_Transaccion',
    'fecha': 'Fecha_Transaccion'
}
df.rename(columns=rename_dict, inplace=True)
print(f"  - Columnas renombradas: {list(rename_dict.keys())}")

# Reorganizar columnas (ID primero, luego fecha, luego monto, etc.)
priority_cols = ['ID_Cliente', 'Fecha_Transaccion', 'Monto_Transaccion']
other_cols = [col for col in df.columns if col not in priority_cols]
df = df[priority_cols + other_cols]
print(f"  - Columnas reorganizadas (orden prioritario)")

# ============================================================================
# PASO 4: EXPORTACIÓN DE DATOS
# ============================================================================
print("\n\n💾 PASO 4: EXPORTACIÓN DE DATOS")
print("-"*80)

# 4.1 Exportar a CSV sin índice
csv_output = 'datos_financieros_procesados.csv'
df.to_csv(csv_output, index=False)
print(f"✓ Datos exportados a CSV: {csv_output}")

# 4.2 Exportar a Excel
excel_output = 'datos_financieros_procesados.xlsx'
with pd.ExcelWriter(excel_output, engine='openpyxl') as writer:
    # Hoja 1: Datos procesados
    df.to_excel(writer, sheet_name='Datos Procesados', index=False)
    
    # Hoja 2: Resumen estadístico
    summary = df.describe()
    summary.to_excel(writer, sheet_name='Resumen Estadístico')
    
    # Hoja 3: Valores nulos originales vs procesados
    comparison = pd.DataFrame({
        'Columna': df_original.columns,
        'Nulos_Original': df_original.isnull().sum().values,
        'Nulos_Procesado': [0] * len(df.columns)
    })
    comparison.to_excel(writer, sheet_name='Comparación', index=False)

print(f"✓ Datos exportados a Excel: {excel_output}")
print("  - Hoja 'Datos Procesados': Dataset completo limpio")
print("  - Hoja 'Resumen Estadístico': Estadísticas descriptivas")
print("  - Hoja 'Comparación': Comparación antes/después")

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n\n📈 RESUMEN DEL PROCESO")
print("="*80)
print(f"✓ Registros originales: {len(df_original)}")
print(f"✓ Registros procesados: {len(df)}")
print(f"✓ Registros eliminados: {len(df_original) - len(df)}")
print(f"✓ Valores nulos corregidos: {df_original.isnull().sum().sum()}")
print(f"✓ Columnas finales: {len(df.columns)}")
print("\n✅ Proceso de Data Wrangling completado exitosamente!")
print("="*80)
