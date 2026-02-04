"""
Script de Análisis de Datos: Valores UF 2025

Este script realiza el análisis completo de los valores de la Unidad de Fomento
desde el sitio web del SII, incluyendo limpieza de datos y análisis estadístico.

Uso:
    python analisis_uf_script.py

Autor: Analista de Datos
Fecha: Febrero 2025
"""

import pandas as pd
import numpy as np
import warnings
from datetime import datetime
import os

# Configuración
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

# Constantes
URL_SII = 'https://www.sii.cl/valores_y_fechas/uf/uf2025.htm'
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_ENTRADA = os.path.join(SCRIPT_DIR, 'UF_2025.csv')
ARCHIVO_SALIDA_LIMPIO = os.path.join(SCRIPT_DIR, 'UF_2025_LIMPIO.csv')
ARCHIVO_SALIDA_STATS = os.path.join(SCRIPT_DIR, 'UF_2025_ESTADISTICAS.csv')
ARCHIVO_REPORTE = os.path.join(SCRIPT_DIR, 'REPORTE_UF_2025.txt')
MESES = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']


def imprimir_banner(texto, caracter='='):
    """Imprime un banner decorativo"""
    linea = caracter * 60
    print(f"\n{linea}")
    print(f"{texto.center(60)}")
    print(f"{linea}\n")


def extraer_datos_web():
    """
    Extrae datos desde el sitio web del SII
    
    Returns:
        DataFrame con los datos extraídos o None si falla
    """
    print("🌐 Intentando extraer datos desde el sitio web del SII...")
    try:
        tablas = pd.read_html(URL_SII, decimal=',', thousands='.')
        print(f"✅ Se encontraron {len(tablas)} tabla(s)")
        df = tablas[0]
        print(f"✅ Tabla extraída: {df.shape[0]} filas x {df.shape[1]} columnas")
        return df
    except Exception as e:
        print(f"❌ Error al extraer datos web: {e}")
        return None


def cargar_datos_csv(archivo):
    """
    Carga datos desde archivo CSV local
    
    Args:
        archivo: Ruta del archivo CSV
        
    Returns:
        DataFrame con los datos cargados
    """
    print(f"📥 Cargando datos desde {archivo}...")
    df = pd.read_csv(archivo, sep=';', encoding='utf-8-sig')
    print(f"✅ Datos cargados: {df.shape[0]} filas x {df.shape[1]} columnas")
    return df


def ensuciar_datos(df):
    """
    Introduce problemas comunes en los datos para simular escenario real
    
    Args:
        df: DataFrame original
        
    Returns:
        DataFrame con datos ensuciados
    """
    imprimir_banner("ENSUCIANDO DATOS", "🎭")
    
    df = df.copy()
    np.random.seed(42)
    
    # 1. Valores nulos
    print("1️⃣ Introduciendo valores nulos (5% de los datos)...")
    for mes in MESES:
        if mes in df.columns:
            indices = np.random.choice(df.index, size=int(len(df) * 0.05), replace=False)
            df.loc[indices, mes] = np.nan
    
    # 2. Duplicados
    print("2️⃣ Introduciendo filas duplicadas...")
    filas_dup = df.sample(n=3, random_state=42)
    df = pd.concat([df, filas_dup], ignore_index=True)
    
    # 3. Outliers
    print("3️⃣ Introduciendo outliers...")
    for mes in ['Ene', 'Feb', 'Mar']:
        if mes in df.columns:
            idx = np.random.choice(df.index, 2)
            df.loc[idx, mes] = '99.999,99'
    
    # 4. Espacios en blanco
    print("4️⃣ Introduciendo espacios en blanco...")
    for mes in ['Abr', 'May']:
        if mes in df.columns:
            idx = np.random.choice(df.index, 2)
            df.loc[idx, mes] = str(df.loc[idx, mes].iloc[0]) + '  '
    
    # 5. Formatos inconsistentes
    print("5️⃣ Introduciendo formatos inconsistentes...")
    # Convertir columna Día a object para permitir strings
    if 'Día' in df.columns:
        df['Día'] = df['Día'].astype(object)
        df.loc[5, 'Día'] = '6.'
        df.loc[10, 'Día'] = 'Día 11'
    
    # 6. Columna irrelevante
    print("6️⃣ Agregando columna irrelevante...")
    df['Comentarios'] = np.random.choice(['OK', 'Revisar', '', np.nan], size=len(df))
    
    print(f"\n✅ Datos ensuciados: {df.shape}")
    print(f"   Valores nulos: {df.isnull().sum().sum()}")
    
    return df


def limpiar_valor_uf(valor):
    """
    Limpia y convierte un valor UF a formato numérico
    
    Args:
        valor: Valor UF en formato string chileno
        
    Returns:
        Valor flotante o NaN si no se puede convertir
    """
    if pd.isna(valor):
        return np.nan
    
    valor_str = str(valor).strip()
    valor_str = valor_str.replace('.', '')
    valor_str = valor_str.replace(',', '.')
    
    try:
        return float(valor_str)
    except:
        return np.nan


def limpiar_datos(df):
    """
    Limpia el DataFrame eliminando problemas comunes
    
    Args:
        df: DataFrame con datos sucios
        
    Returns:
        DataFrame limpio
    """
    imprimir_banner("LIMPIANDO DATOS", "🧼")
    
    df = df.copy()
    
    # PASO 1: Eliminar columnas irrelevantes
    print("📌 PASO 1: Eliminando columnas irrelevantes...")
    if 'Comentarios' in df.columns:
        df = df.drop('Comentarios', axis=1)
        print("   ✅ Columna 'Comentarios' eliminada")
    
    # PASO 2: Eliminar duplicados
    print("\n📌 PASO 2: Eliminando duplicados...")
    filas_antes = len(df)
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    print(f"   ✅ {filas_antes - len(df)} filas duplicadas eliminadas")
    
    # PASO 3: Limpiar columna Día
    print("\n📌 PASO 3: Limpiando columna 'Día'...")
    df['Día'] = df['Día'].astype(str).str.replace('.', '', regex=False)
    df['Día'] = df['Día'].str.extract(r'(\d+)')[0]
    df['Día'] = pd.to_numeric(df['Día'], errors='coerce')
    print("   ✅ Columna 'Día' convertida a numérico")
    
    # PASO 4: Limpiar valores UF
    print("\n📌 PASO 4: Limpiando valores UF...")
    for mes in MESES:
        if mes in df.columns:
            df[mes] = df[mes].apply(limpiar_valor_uf)
    print("   ✅ Valores UF convertidos a numérico")
    
    # PASO 5: Eliminar outliers
    print("\n📌 PASO 5: Eliminando outliers...")
    outliers_total = 0
    for mes in MESES:
        if mes in df.columns:
            Q1 = df[mes].quantile(0.25)
            Q3 = df[mes].quantile(0.75)
            IQR = Q3 - Q1
            limite_inf = Q1 - 3 * IQR
            limite_sup = Q3 + 3 * IQR
            
            outliers = ((df[mes] < limite_inf) | (df[mes] > limite_sup)).sum()
            outliers_total += outliers
            
            df.loc[(df[mes] < limite_inf) | (df[mes] > limite_sup), mes] = np.nan
    
    print(f"   ✅ {outliers_total} outliers marcados como NaN")
    
    # PASO 6: Imputar valores nulos
    print("\n📌 PASO 6: Imputando valores nulos...")
    nulos_antes = df.isnull().sum().sum()
    for mes in MESES:
        if mes in df.columns:
            df[mes] = df[mes].interpolate(method='linear', limit_direction='both')
    
    nulos_despues = df.isnull().sum().sum()
    print(f"   ✅ Valores nulos: {nulos_antes} → {nulos_despues}")
    
    # PASO 7: Ordenar
    print("\n📌 PASO 7: Ordenando datos...")
    df = df.sort_values('Día').reset_index(drop=True)
    print("   ✅ Datos ordenados por día")
    
    imprimir_banner("LIMPIEZA COMPLETADA", "✅")
    print(f"Dimensiones finales: {df.shape}")
    print(f"Valores nulos: {df.isnull().sum().sum()}")
    
    return df


def analisis_descriptivo(df):
    """
    Realiza análisis estadístico descriptivo
    
    Args:
        df: DataFrame limpio
        
    Returns:
        DataFrame con estadísticas por mes
    """
    imprimir_banner("ANÁLISIS DESCRIPTIVO", "📊")
    
    print("📋 Información del DataFrame:")
    print(df.info())
    
    print("\n📈 Estadísticas Descriptivas:")
    print(df.describe())
    
    # Estadísticas personalizadas
    print("\n📊 Estadísticas por Mes:")
    estadisticas = pd.DataFrame({
        'Promedio': df[MESES].mean(),
        'Mediana': df[MESES].median(),
        'Desv_Std': df[MESES].std(),
        'Mínimo': df[MESES].min(),
        'Máximo': df[MESES].max(),
        'Rango': df[MESES].max() - df[MESES].min(),
        'CV_%': (df[MESES].std() / df[MESES].mean() * 100).round(2)
    })
    
    print(estadisticas)
    
    # Valores extremos
    print("\n⚡ Valores Extremos:")
    print("\n🔝 Máximos por mes:")
    for mes in MESES:
        if mes in df.columns:
            max_val = df[mes].max()
            dia = df.loc[df[mes] == max_val, 'Día'].values[0]
            print(f"   {mes}: ${max_val:,.2f} (Día {dia})")
    
    print("\n🔽 Mínimos por mes:")
    for mes in MESES:
        if mes in df.columns:
            min_val = df[mes].min()
            dia = df.loc[df[mes] == min_val, 'Día'].values[0]
            print(f"   {mes}: ${min_val:,.2f} (Día {dia})")
    
    # Variación anual
    print("\n📅 Resumen Anual:")
    uf_inicio = df['Ene'].iloc[0]
    uf_fin = df['Dic'].iloc[-1]
    variacion = uf_fin - uf_inicio
    variacion_pct = (variacion / uf_inicio) * 100
    
    print(f"   UF inicio (01-Ene): ${uf_inicio:,.2f}")
    print(f"   UF final (31-Dic): ${uf_fin:,.2f}")
    print(f"   Variación anual: ${variacion:+,.2f} ({variacion_pct:+.2f}%)")
    print(f"   UF promedio año: ${df[MESES].mean().mean():,.2f}")
    
    return estadisticas


def exportar_resultados(df, estadisticas):
    """
    Exporta los resultados del análisis
    
    Args:
        df: DataFrame con datos limpios
        estadisticas: DataFrame con estadísticas
    """
    imprimir_banner("EXPORTANDO RESULTADOS", "💾")
    
    # Exportar datos limpios
    print(f"📄 Exportando {ARCHIVO_SALIDA_LIMPIO}...")
    df.to_csv(ARCHIVO_SALIDA_LIMPIO, index=False, encoding='utf-8-sig')
    print("   ✅ Datos limpios exportados")
    
    # Exportar estadísticas
    print(f"\n📄 Exportando {ARCHIVO_SALIDA_STATS}...")
    estadisticas.to_csv(ARCHIVO_SALIDA_STATS, encoding='utf-8-sig')
    print("   ✅ Estadísticas exportadas")
    
    # Crear reporte
    print(f"\n📄 Generando {ARCHIVO_REPORTE}...")
    
    uf_inicio = df['Ene'].iloc[0]
    uf_fin = df['Dic'].iloc[-1]
    variacion = uf_fin - uf_inicio
    variacion_pct = (variacion / uf_inicio) * 100
    
    reporte = f"""
{'='*60}
REPORTE DE ANÁLISIS - VALORES UF 2025
{'='*60}
Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

1. INFORMACIÓN DEL DATASET
   - Registros totales: {len(df)}
   - Columnas: {len(df.columns)}
   - Periodo: Enero - Diciembre 2025

2. VALORES DESTACADOS
   - UF Promedio Anual: ${df[MESES].mean().mean():,.2f}
   - UF Mínima: ${df[MESES].min().min():,.2f}
   - UF Máxima: ${df[MESES].max().max():,.2f}
   - Variación Anual: {variacion_pct:+.2f}%

3. CALIDAD DE DATOS
   - Valores nulos: {df.isnull().sum().sum()}
   - Duplicados: 0
   - Estado: ✅ DATOS LIMPIOS

4. ESTADÍSTICAS POR MES

{estadisticas.to_string()}

{'='*60}
Fin del reporte
{'='*60}
"""
    
    with open(ARCHIVO_REPORTE, 'w', encoding='utf-8') as f:
        f.write(reporte)
    
    print("   ✅ Reporte generado")
    
    print("\n✅ Todos los archivos exportados exitosamente:")
    print(f"   • {ARCHIVO_SALIDA_LIMPIO}")
    print(f"   • {ARCHIVO_SALIDA_STATS}")
    print(f"   • {ARCHIVO_REPORTE}")


def main():
    """Función principal que ejecuta todo el proceso"""
    
    imprimir_banner("ANÁLISIS DE DATOS UF 2025", "🚀")
    
    print(f"Inicio del análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # 1. Extracción de datos
    df_web = extraer_datos_web()
    
    # Verificar si los datos web tienen la estructura esperada
    df = None
    if df_web is not None:
        # Verificar si tiene las columnas esperadas
        meses_encontrados = [mes for mes in MESES if mes in df_web.columns]
        if len(meses_encontrados) >= 10:  # Al menos 10 meses
            df = df_web
            print("✅ Estructura de datos web validada correctamente")
        else:
            print(f"⚠️ Los datos web no tienen la estructura esperada (solo se encontraron {len(meses_encontrados)} meses)")
            print("   Usando archivo CSV local como alternativa...")
            df = cargar_datos_csv(ARCHIVO_ENTRADA)
    else:
        print("⚠️ Usando archivo CSV local como alternativa...")
        df = cargar_datos_csv(ARCHIVO_ENTRADA)
    
    # 2. Mostrar datos originales
    print("\n👁️ Muestra de datos originales:")
    print(df.head())
    
    # 3. Ensuciar datos
    df_sucio = ensuciar_datos(df)
    
    # 4. Limpiar datos
    df_limpio = limpiar_datos(df_sucio)
    
    # 5. Análisis descriptivo
    estadisticas = analisis_descriptivo(df_limpio)
    
    # 6. Exportar resultados
    exportar_resultados(df_limpio, estadisticas)
    
    # Mensaje final
    imprimir_banner("PROCESO COMPLETADO EXITOSAMENTE", "🎉")
    print(f"Fin del análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nRevisa los archivos generados para ver los resultados completos.")
    

if __name__ == "__main__":
    main()
