"""
Análisis de Caso: Aplicación de NumPy en el Análisis de Datos Financieros
Empresa de análisis financiero - Optimización del procesamiento de datos

Autor: Analista de Datos
Fecha: Enero 2026
Versión: 1.0

Este script demuestra la aplicación de NumPy para optimizar el análisis
de datos financieros, incluyendo manipulación de arrays, operaciones
estadísticas, y comparación de rendimiento.
"""

import numpy as np
import time
import sys
from typing import Tuple, Dict, List

# Configuración de visualización de NumPy
np.set_printoptions(precision=2, suppress=True)


class AnalizadorFinanciero:
    """
    Clase para el análisis de datos financieros utilizando NumPy.
    
    Attributes:
        datos_acciones (np.ndarray): Matriz 5x5 con precios de acciones
        nombres_acciones (list): Lista con nombres de las acciones
        dias (list): Lista con los días de cotización
    """
    
    def __init__(self):
        """Inicializa el analizador con datos simulados."""
        self.nombres_acciones = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
        self.dias = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5']
        self.datos_acciones = None
        
    def crear_datos_simulados(self, seed: int = 42) -> np.ndarray:
        """
        Crea una matriz 5x5 con datos financieros simulados.
        
        Args:
            seed (int): Semilla para reproducibilidad de datos aleatorios
            
        Returns:
            np.ndarray: Matriz 5x5 con precios de acciones
            
        Documentación:
        - np.random.seed: https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html
        - np.random.uniform: https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html
        """
        print("=" * 70)
        print("TAREA 1: CARGA Y ESTRUCTURACIÓN DE DATOS")
        print("=" * 70)
        
        # Establecer semilla para reproducibilidad
        np.random.seed(seed)
        
        # Generar precios base entre 100 y 500 USD
        precios_base = np.random.uniform(100, 500, size=5)
        
        # Crear matriz 5x5 con variaciones diarias
        # Cada fila es una acción, cada columna es un día
        self.datos_acciones = np.zeros((5, 5))
        
        for i in range(5):
            # Generar variaciones diarias entre -5% y +5%
            variaciones = np.random.uniform(-0.05, 0.05, size=5)
            # Aplicar variaciones acumulativas
            for j in range(5):
                if j == 0:
                    self.datos_acciones[i, j] = precios_base[i]
                else:
                    self.datos_acciones[i, j] = self.datos_acciones[i, j-1] * (1 + variaciones[j])
        
        print("\nMatriz de precios de acciones creada exitosamente (5x5)")
        print("Filas: Acciones | Columnas: Días de cotización\n")
        
        self._imprimir_matriz_formateada()
        
        return self.datos_acciones
    
    def _imprimir_matriz_formateada(self):
        """Imprime la matriz de datos con formato legible."""
        print(f"{'Acción':<10}", end="")
        for dia in self.dias:
            print(f"{dia:>12}", end="")
        print("\n" + "-" * 70)
        
        for i, accion in enumerate(self.nombres_acciones):
            print(f"{accion:<10}", end="")
            for j in range(5):
                print(f"${self.datos_acciones[i, j]:>10.2f}", end=" ")
            print()
    
    def analisis_estadistico(self) -> Dict[str, np.ndarray]:
        """
        Calcula estadísticas descriptivas para cada acción.
        
        Returns:
            Dict con promedios, máximos y mínimos
            
        Documentación:
        - np.mean: https://numpy.org/doc/stable/reference/generated/numpy.mean.html
        - np.max: https://numpy.org/doc/stable/reference/generated/numpy.amax.html
        - np.min: https://numpy.org/doc/stable/reference/generated/numpy.amin.html
        - axis parameter: https://numpy.org/doc/stable/glossary.html#term-axis
        """
        print("\n" + "=" * 70)
        print("TAREA 2.1: ANÁLISIS ESTADÍSTICO DE DATOS")
        print("=" * 70)
        
        # Calcular estadísticas por fila (axis=1: a lo largo de las columnas)
        promedios = np.mean(self.datos_acciones, axis=1)
        maximos = np.max(self.datos_acciones, axis=1)
        minimos = np.min(self.datos_acciones, axis=1)
        
        print("\nEstadísticas por acción a lo largo del período:\n")
        print(f"{'Acción':<10} {'Promedio':>12} {'Máximo':>12} {'Mínimo':>12} {'Rango':>12}")
        print("-" * 70)
        
        for i, accion in enumerate(self.nombres_acciones):
            rango = maximos[i] - minimos[i]
            print(f"{accion:<10} ${promedios[i]:>10.2f} ${maximos[i]:>10.2f} "
                  f"${minimos[i]:>10.2f} ${rango:>10.2f}")
        
        return {
            'promedios': promedios,
            'maximos': maximos,
            'minimos': minimos
        }
    
    def calcular_variacion_porcentual(self) -> np.ndarray:
        """
        Calcula la variación porcentual diaria de cada acción.
        
        Returns:
            np.ndarray: Matriz 5x4 con variaciones porcentuales
            
        Documentación:
        - Array slicing: https://numpy.org/doc/stable/user/basics.indexing.html
        - Broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html
        """
        print("\n" + "=" * 70)
        print("TAREA 2.2: CÁLCULO DE VARIACIÓN PORCENTUAL DIARIA")
        print("=" * 70)
        
        # Calcular variación porcentual: ((precio_actual - precio_anterior) / precio_anterior) * 100
        # Usamos slicing para obtener días consecutivos
        variaciones = ((self.datos_acciones[:, 1:] - self.datos_acciones[:, :-1]) / 
                       self.datos_acciones[:, :-1]) * 100
        
        print("\nVariación porcentual diaria (%):\n")
        print(f"{'Acción':<10}", end="")
        for i in range(1, 5):
            print(f"Día {i}→{i+1}:>12", end="")
        print("\n" + "-" * 70)
        
        for i, accion in enumerate(self.nombres_acciones):
            print(f"{accion:<10}", end="")
            for j in range(4):
                color = "▲" if variaciones[i, j] > 0 else "▼"
                print(f"{color}{variaciones[i, j]:>10.2f}%", end=" ")
            print()
        
        return variaciones
    
    def aplicar_transformaciones_matematicas(self) -> Dict[str, np.ndarray]:
        """
        Aplica funciones matemáticas sobre los datos.
        
        Returns:
            Dict con transformaciones logarítmicas, exponenciales y normalizadas
            
        Documentación:
        - np.log: https://numpy.org/doc/stable/reference/generated/numpy.log.html
        - np.exp: https://numpy.org/doc/stable/reference/generated/numpy.exp.html
        - Normalización: https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
        """
        print("\n" + "=" * 70)
        print("TAREA 2.3: TRANSFORMACIONES MATEMÁTICAS")
        print("=" * 70)
        
        # Logaritmo natural (útil para rendimientos continuos)
        log_precios = np.log(self.datos_acciones)
        
        # Normalización Min-Max: (x - min) / (max - min)
        # Escala los valores entre 0 y 1
        min_vals = np.min(self.datos_acciones, axis=1, keepdims=True)
        max_vals = np.max(self.datos_acciones, axis=1, keepdims=True)
        datos_normalizados = (self.datos_acciones - min_vals) / (max_vals - min_vals)
        
        # Normalización Z-score: (x - media) / desviación estándar
        media = np.mean(self.datos_acciones, axis=1, keepdims=True)
        std = np.std(self.datos_acciones, axis=1, keepdims=True)
        z_scores = (self.datos_acciones - media) / std
        
        print("\n1. Logaritmo Natural (primeras 3 acciones):")
        print(log_precios[:3])
        
        print("\n2. Normalización Min-Max (valores entre 0 y 1):")
        print(f"{'Acción':<10}", end="")
        for dia in self.dias:
            print(f"{dia:>12}", end="")
        print("\n" + "-" * 70)
        
        for i, accion in enumerate(self.nombres_acciones):
            print(f"{accion:<10}", end="")
            for j in range(5):
                print(f"{datos_normalizados[i, j]:>12.4f}", end="")
            print()
        
        print("\n3. Z-Scores (estandarización):")
        print(f"Media ≈ 0, Desviación estándar ≈ 1")
        print(f"Rango típico: -3 a +3\n")
        
        return {
            'logaritmo': log_precios,
            'normalizado_minmax': datos_normalizados,
            'z_scores': z_scores
        }
    
    def indexacion_avanzada(self):
        """
        Demuestra técnicas de indexación avanzada de NumPy.
        
        Documentación:
        - Indexing: https://numpy.org/doc/stable/user/basics.indexing.html
        - Boolean indexing: https://numpy.org/doc/stable/reference/arrays.indexing.html
        """
        print("\n" + "=" * 70)
        print("TAREA 3.1: INDEXACIÓN AVANZADA")
        print("=" * 70)
        
        # Caso 1: Acceder a una acción específica en un día específico
        accion_idx = 2  # MSFT
        dia_idx = 3     # Día 4
        valor = self.datos_acciones[accion_idx, dia_idx]
        
        print(f"\n1. Valor específico:")
        print(f"   {self.nombres_acciones[accion_idx]} en {self.dias[dia_idx]}: ${valor:.2f}")
        
        # Caso 2: Obtener todos los precios de una acción
        precios_aapl = self.datos_acciones[0, :]
        print(f"\n2. Todos los precios de {self.nombres_acciones[0]}:")
        print(f"   {precios_aapl}")
        
        # Caso 3: Obtener precios de un día específico para todas las acciones
        precios_dia3 = self.datos_acciones[:, 2]
        print(f"\n3. Precios de todas las acciones en {self.dias[2]}:")
        for i, accion in enumerate(self.nombres_acciones):
            print(f"   {accion}: ${precios_dia3[i]:.2f}")
        
        # Caso 4: Indexación booleana - acciones con precio > 300 en día 1
        mask = self.datos_acciones[:, 0] > 300
        acciones_altas = np.array(self.nombres_acciones)[mask]
        precios_altos = self.datos_acciones[mask, 0]
        
        print(f"\n4. Acciones con precio > $300 en {self.dias[0]}:")
        for accion, precio in zip(acciones_altas, precios_altos):
            print(f"   {accion}: ${precio:.2f}")
        
        # Caso 5: Fancy indexing - seleccionar múltiples acciones específicas
        indices_seleccion = [0, 2, 4]  # AAPL, MSFT, TSLA
        datos_seleccionados = self.datos_acciones[indices_seleccion, :]
        
        print(f"\n5. Datos de acciones seleccionadas (AAPL, MSFT, TSLA):")
        print(datos_seleccionados)
    
    def broadcasting_demo(self):
        """
        Demuestra el uso de broadcasting para operaciones eficientes.
        
        Documentación:
        - Broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html
        """
        print("\n" + "=" * 70)
        print("TAREA 3.2: BROADCASTING Y OPERACIONES VECTORIZADAS")
        print("=" * 70)
        
        # Ejemplo 1: Aplicar una comisión del 0.5% a todas las transacciones
        comision = 0.005
        precios_con_comision = self.datos_acciones * (1 + comision)
        
        print("\n1. Aplicar comisión del 0.5% (broadcasting escalar):")
        print(f"   Original (AAPL): {self.datos_acciones[0]}")
        print(f"   Con comisión:     {precios_con_comision[0]}")
        
        # Ejemplo 2: Aplicar diferentes factores de ajuste por día
        # Simula ajustes de mercado diferentes cada día
        factores_ajuste = np.array([1.00, 1.02, 0.98, 1.01, 0.99])  # 1x5
        datos_ajustados = self.datos_acciones * factores_ajuste  # 5x5 * 1x5 (broadcasting)
        
        print(f"\n2. Factores de ajuste por día (broadcasting 1D):")
        print(f"   Factores: {factores_ajuste}")
        print(f"   AAPL original:  {self.datos_acciones[0]}")
        print(f"   AAPL ajustado:  {datos_ajustados[0]}")
        
        # Ejemplo 3: Calcular rendimiento relativo al primer día
        precios_iniciales = self.datos_acciones[:, 0:1]  # 5x1
        rendimiento_relativo = ((self.datos_acciones - precios_iniciales) / 
                                precios_iniciales * 100)  # Broadcasting
        
        print(f"\n3. Rendimiento relativo al primer día (%):")
        print(f"{'Acción':<10}", end="")
        for dia in self.dias:
            print(f"{dia:>12}", end="")
        print("\n" + "-" * 70)
        
        for i, accion in enumerate(self.nombres_acciones):
            print(f"{accion:<10}", end="")
            for j in range(5):
                print(f"{rendimiento_relativo[i, j]:>11.2f}%", end="")
            print()
    
    def comparacion_rendimiento(self):
        """
        Compara el rendimiento de NumPy vs métodos tradicionales (listas Python).
        
        Documentación:
        - Performance: https://numpy.org/doc/stable/user/whatisnumpy.html#why-is-numpy-fast
        """
        print("\n" + "=" * 70)
        print("TAREA 4: COMPARACIÓN DE RENDIMIENTO - NUMPY VS PYTHON PURO")
        print("=" * 70)
        
        # Crear dataset más grande para comparación
        tamano = 1000
        np.random.seed(42)
        datos_numpy = np.random.uniform(100, 500, size=(tamano, tamano))
        datos_lista = datos_numpy.tolist()
        
        print(f"\nDataset de prueba: Matriz {tamano}x{tamano} = {tamano*tamano:,} elementos\n")
        
        # Test 1: Calcular promedio
        print("Test 1: Calcular promedio de todas las filas")
        print("-" * 50)
        
        # NumPy
        inicio = time.time()
        promedio_numpy = np.mean(datos_numpy, axis=1)
        tiempo_numpy = time.time() - inicio
        
        # Python puro
        inicio = time.time()
        promedio_python = [sum(fila) / len(fila) for fila in datos_lista]
        tiempo_python = time.time() - inicio
        
        print(f"NumPy:       {tiempo_numpy:.6f} segundos")
        print(f"Python puro: {tiempo_python:.6f} segundos")
        print(f"Speedup:     {tiempo_python/tiempo_numpy:.1f}x más rápido con NumPy")
        
        # Test 2: Operaciones elemento a elemento
        print("\nTest 2: Multiplicar matriz por escalar y sumar constante")
        print("-" * 50)
        
        # NumPy (vectorizado)
        inicio = time.time()
        resultado_numpy = datos_numpy * 1.05 + 10
        tiempo_numpy = time.time() - inicio
        
        # Python puro (bucles)
        inicio = time.time()
        resultado_python = [[valor * 1.05 + 10 for valor in fila] for fila in datos_lista]
        tiempo_python = time.time() - inicio
        
        print(f"NumPy:       {tiempo_numpy:.6f} segundos")
        print(f"Python puro: {tiempo_python:.6f} segundos")
        print(f"Speedup:     {tiempo_python/tiempo_numpy:.1f}x más rápido con NumPy")
        
        # Test 3: Calcular varianza
        print("\nTest 3: Calcular varianza de cada columna")
        print("-" * 50)
        
        # NumPy
        inicio = time.time()
        varianza_numpy = np.var(datos_numpy, axis=0)
        tiempo_numpy = time.time() - inicio
        
        # Python puro
        inicio = time.time()
        # Transponer y calcular varianza
        datos_transpuestos = list(zip(*datos_lista))
        varianza_python = []
        for columna in datos_transpuestos:
            media = sum(columna) / len(columna)
            varianza = sum((x - media) ** 2 for x in columna) / len(columna)
            varianza_python.append(varianza)
        tiempo_python = time.time() - inicio
        
        print(f"NumPy:       {tiempo_numpy:.6f} segundos")
        print(f"Python puro: {tiempo_python:.6f} segundos")
        print(f"Speedup:     {tiempo_python/tiempo_numpy:.1f}x más rápido con NumPy")
        
        # Resumen
        print("\n" + "=" * 70)
        print("VENTAJAS DE NUMPY:")
        print("=" * 70)
        print("""
1. RENDIMIENTO:
   - Operaciones vectorizadas en C (10-100x más rápido)
   - Uso eficiente de memoria contigua
   - Optimizaciones SIMD (Single Instruction, Multiple Data)

2. CÓDIGO MÁS LIMPIO:
   - Sintaxis concisa y expresiva
   - Menos líneas de código
   - Mayor legibilidad

3. FUNCIONALIDAD:
   - Amplia biblioteca de funciones matemáticas
   - Broadcasting automático
   - Operaciones de álgebra lineal optimizadas

4. MEMORIA:
   - Arrays de tipo homogéneo (menor uso de memoria)
   - Mejor localidad de caché
        """)


def main():
    """Función principal para ejecutar el análisis completo."""
    print("\n" + "=" * 70)
    print("  ANÁLISIS DE CASO: APLICACIÓN DE NUMPY EN ANÁLISIS FINANCIERO")
    print("  Empresa de Análisis Financiero - Optimización de Datos")
    print("=" * 70)
    print("\nPython:", sys.version.split()[0])
    print("NumPy:", np.__version__)
    
    # Crear instancia del analizador
    analizador = AnalizadorFinanciero()
    
    # Ejecutar todas las tareas
    try:
        # Tarea 1: Carga y estructuración
        analizador.crear_datos_simulados()
        
        # Tarea 2: Análisis y transformación
        analizador.analisis_estadistico()
        analizador.calcular_variacion_porcentual()
        analizador.aplicar_transformaciones_matematicas()
        
        # Tarea 3: Optimización y selección
        analizador.indexacion_avanzada()
        analizador.broadcasting_demo()
        
        # Tarea 4: Comparación
        analizador.comparacion_rendimiento()
        
        print("\n" + "=" * 70)
        print("  ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error durante el análisis: {e}")
        raise


if __name__ == "__main__":
    main()