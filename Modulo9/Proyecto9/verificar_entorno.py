"""
verificar_entorno.py
====================
Ejecuta este script PRIMERO para saber qué tienes instalado
y qué te falta antes de empezar el proyecto.

Uso:
    python verificar_entorno.py
"""
import sys, subprocess, importlib

OK  = "[OK]"
ERR = "[FALTA]"
WARN= "[AVISO]"

print("=" * 58)
print("  VERIFICADOR DE ENTORNO — Retail Analytics Pipeline")
print("=" * 58)

errores = []

# 1. Python
major, minor = sys.version_info[:2]
if major == 3 and minor >= 8:
    print(f"{OK}  Python {major}.{minor} detectado")
else:
    print(f"{ERR} Python {major}.{minor} — se necesita 3.8 o superior")
    errores.append("Actualizar Python a 3.8+")

# 2. Java
print()
try:
    result = subprocess.run(
        ["java", "-version"],
        capture_output=True, text=True
    )
    output = result.stderr or result.stdout
    first_line = output.strip().splitlines()[0]
    print(f"{OK}  Java encontrado: {first_line}")
    if "11" in first_line or "17" in first_line or "21" in first_line:
        print(f"      Version compatible con Spark.")
    else:
        print(f"{WARN} Se recomienda Java 11. Tu version podria tener problemas.")
        errores.append("Instalar Java 11 desde https://adoptium.net/")
except FileNotFoundError:
    print(f"{ERR} Java NO encontrado.")
    print(f"      -> Descargar JDK 11 desde: https://adoptium.net/temurin/releases/")
    print(f"      -> Seleccionar: JDK 11, Windows, x64, .msi")
    print(f"      -> Instalar y REINICIAR la terminal.")
    errores.append("Instalar Java 11 (OBLIGATORIO para Spark)")

# 3. Paquetes Python
print()
paquetes = [
    ("pyspark",     "pip install pyspark"),
    ("numpy",       "pip install numpy"),
    ("pandas",      "pip install pandas"),
    ("matplotlib",  "pip install matplotlib"),
    ("seaborn",     "pip install seaborn"),
]

falta_paquetes = []
for pkg, cmd in paquetes:
    try:
        mod = importlib.import_module(pkg)
        version = getattr(mod, "__version__", "?")
        print(f"{OK}  {pkg:<15} version {version}")
    except ImportError:
        print(f"{ERR} {pkg:<15} NO instalado  ->  {cmd}")
        falta_paquetes.append(pkg)

if falta_paquetes:
    errores.append(f"Instalar paquetes: pip install {' '.join(falta_paquetes)}")

# 4. JAVA_HOME variable de entorno
print()
import os
java_home = os.environ.get("JAVA_HOME", "")
if java_home:
    print(f"{OK}  JAVA_HOME definida: {java_home}")
else:
    print(f"{WARN} JAVA_HOME no definida.")
    print(f"      PySpark puede fallar en Windows si esta variable no existe.")
    print(f"      Solucion: ver README seccion 'Configurar JAVA_HOME en Windows'")
    errores.append("Configurar variable JAVA_HOME (ver README)")

# 5. Dataset
print()
train = os.path.join("data", "fashion_mnist", "fashion_train.csv")
test  = os.path.join("data", "fashion_mnist", "fashion_test.csv")
if os.path.exists(train) and os.path.exists(test):
    size = os.path.getsize(train) / (1024**2)
    print(f"{OK}  Dataset encontrado (train: {size:.0f} MB)")
else:
    print(f"{ERR} Dataset NO generado.")
    print(f"      Ejecutar: python setup_dataset.py")
    errores.append("Generar dataset: python setup_dataset.py")

# Resumen final
print()
print("=" * 58)
if not errores:
    print("  TODO LISTO. Podes ejecutar los notebooks.")
    print("  Empieza con: leccion_01_fundamentos_bigdata.ipynb")
else:
    print(f"  ACCION REQUERIDA ({len(errores)} item/s):")
    for i, e in enumerate(errores, 1):
        print(f"  {i}. {e}")
print("=" * 58)
