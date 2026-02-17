import pandas as pd
import io
import sys
import os

# Configurar pandas para mostrar mejor
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)

# Leer el CSV con ruta absoluta
ruta_csv = r'c:\Users\joset\OneDrive\Desktop\Data Science SENSE\Bootcamp\Modulo4\ProyectoM4\Extras\gaming-ratings.csv'
df = pd.read_csv(ruta_csv)

# Mostrar tabla
print("\n" + "="*150)
print("PRIMERAS 20 FILAS:")
print("="*150 + "\n")
print(df.head(20).to_string())

print("\n" + "="*150)
print("ÚLTIMAS 20 FILAS:")
print("="*150 + "\n")
print(df.tail(20).to_string())

# Exportar a HTML para visualizar mejor en el navegador
df.to_html('gaming_ratings_view.html', index=True)
print("\n" + "="*150)
print("Archivo HTML generado: gaming_ratings_view.html")
print("="*150 + "\n")
