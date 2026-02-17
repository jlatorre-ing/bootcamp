import pandas as pd
import json

# Leer el CSV con ruta absoluta
ruta_csv = r'c:\Users\joset\OneDrive\Desktop\Data Science SENSE\Bootcamp\Modulo4\ProyectoM4\gaming-ratings-database-20260217.csv'
df = pd.read_csv(ruta_csv)

# Mostrar información general
print("=" * 80)
print(f"Total de filas: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")
print("\n" + "=" * 80)
print("Columnas:")
print(df.columns.tolist())
print("\n" + "=" * 80)

# Mostrar primeras filas
print("PRIMERAS 5 FILAS:")
print(df.head())

print("\n" + "=" * 80)
print("TIPOS DE DATOS:")
print(df.dtypes)

print("\n" + "=" * 80)
print("INFORMACIÓN DE VALORES NULOS:")
print(df.isnull().sum())

print("\n" + "=" * 80)
print("ESTADÍSTICAS BÁSICAS:")
print(df.describe())

print("\n" + "=" * 80)
print("EJEMPLO DE FILA COMPLETA (primera fila):")
print(df.iloc[0])

# Si quieres ver datos específicos
print("\n" + "=" * 80)
print("TOP 10 JUEGOS CON MAYOR CALIFICACIÓN:")
print(df.nlargest(10, 'igdb_rating')[['name', 'igdb_rating', 'release_year']])
