import pandas as pd
import os

# Lista de archivos que vimos en tu captura
archivos = [
    'Modulo3/ProyectoM3/UF 2025Excel.csv', 
    'Modulo3/ProyectoM3/UF_2025Cvs.csv'
]

for archivo in archivos:
    try:
        # Intentamos leer el archivo
        df = pd.read_csv(archivo)
        print(f"✅ ¡Éxito! El archivo '{archivo}' se leyó correctamente.")
        print(f"Primeras 3 filas de {archivo}:")
        print(df.head(3))
        print("-" * 30)
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{archivo}'. Verifica que estés en la carpeta correcta.")
    except Exception as e:
        print(f"❌ Ocurrió un error al leer '{archivo}': {e}")