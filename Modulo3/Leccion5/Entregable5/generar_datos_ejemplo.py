"""
Script para generar datos de ejemplo para el análisis de Data Wrangling
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurar semilla para reproducibilidad
np.random.seed(42)

# Parámetros
n_records = 200

# Generar datos
print("Generando datos de ejemplo...")

# IDs de clientes (algunos repetidos para crear duplicados)
cliente_ids = np.random.choice(range(1001, 1051), n_records)

# Fechas en los últimos 90 días
fecha_inicio = datetime.now() - timedelta(days=90)
fechas = [fecha_inicio + timedelta(days=np.random.randint(0, 90)) for _ in range(n_records)]

# Montos de transacciones
montos = np.random.lognormal(mean=6, sigma=1.5, size=n_records)
montos = np.round(montos, 2)

# Tipos de transacción
tipos = np.random.choice(['Deposito', 'Retiro', 'Transferencia', 'Pago'], n_records)

# Estados
estados = np.random.choice(['Completado', 'Pendiente', 'Cancelado'], n_records, p=[0.7, 0.2, 0.1])

# Sucursal
sucursales = np.random.choice(['Norte', 'Sur', 'Este', 'Oeste', 'Centro'], n_records)

# Crear DataFrame
df = pd.DataFrame({
    'cliente_id': cliente_ids,
    'fecha': fechas,
    'monto': montos,
    'tipo_transaccion': tipos,
    'estado': estados,
    'sucursal': sucursales
})

# Introducir valores nulos de manera intencional (10-15% en algunas columnas)
null_indices_monto = np.random.choice(df.index, size=int(n_records * 0.1), replace=False)
df.loc[null_indices_monto, 'monto'] = np.nan

null_indices_estado = np.random.choice(df.index, size=int(n_records * 0.08), replace=False)
df.loc[null_indices_estado, 'estado'] = np.nan

null_indices_sucursal = np.random.choice(df.index, size=int(n_records * 0.05), replace=False)
df.loc[null_indices_sucursal, 'sucursal'] = np.nan

# Crear registros duplicados (agregar 10 duplicados exactos)
duplicates_indices = np.random.choice(df.index, size=10, replace=False)
df_duplicates = df.loc[duplicates_indices].copy()
df = pd.concat([df, df_duplicates], ignore_index=True)

# Mezclar el DataFrame
df = df.sample(frac=1).reset_index(drop=True)

# Guardar a CSV
df.to_csv('datos_financieros.csv', index=False)

print(f"✓ Archivo 'datos_financieros.csv' creado exitosamente")
print(f"  - Total de registros: {len(df)}")
print(f"  - Valores nulos introducidos: {df.isnull().sum().sum()}")
print(f"  - Duplicados introducidos: 10")
print(f"  - Rango de fechas: {df['fecha'].min()} a {df['fecha'].max()}")
print(f"  - Rango de montos: ${df['monto'].min():.2f} a ${df['monto'].max():.2f}")
