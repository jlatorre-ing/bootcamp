# 📚 Sistema de Gestión de Contactos - Documentación Técnica

## 📋 Tabla de Contenidos
1. [Descripción General](#descripción-general)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Arquitectura del Proyecto](#arquitectura-del-proyecto)
4. [Instalación y Configuración](#instalación-y-configuración)
5. [Guía de Uso](#guía-de-uso)
6. [Estructura del Código](#estructura-del-código)
7. [Características Técnicas](#características-técnicas)
8. [Referencias y Fuentes](#referencias-y-fuentes)

---

## 📝 Descripción General

Sistema de gestión de contactos desarrollado en Python que permite almacenar, editar, buscar y eliminar información de contactos personales. El proyecto implementa Programación Orientada a Objetos (POO) con encapsulación completa, persistencia de datos en formato JSON y una interfaz de usuario por consola intuitiva.

### ✨ Funcionalidades Principales
- ✅ Agregar nuevos contactos con validación de datos
- ✏️ Editar contactos existentes
- 🗑️ Eliminar contactos con confirmación
- 🔍 Búsqueda por nombre (parcial, case-insensitive)
- 📞 Búsqueda por número de teléfono
- 📊 Listado completo ordenado alfabéticamente
- 📈 Estadísticas del sistema
- 💾 Persistencia automática de datos

---

## 🖥️ Requisitos del Sistema

### Software Necesario
- **Python**: Versión 3.8 o superior
- **Visual Studio Code**: Editor recomendado
- **Sistema Operativo**: Windows, macOS o Linux

### Librerías Utilizadas (Estándar de Python)
Todas las librerías son parte de la biblioteca estándar de Python, no requieren instalación adicional:
- `json`: Manejo de archivos JSON
- `os`: Operaciones con archivos del sistema
- `typing`: Type hints para mejor documentación
- `re`: Expresiones regulares para validación
- `unittest`: Framework de pruebas unitarias

---

## 🏗️ Arquitectura del Proyecto

```
sistema-gestion-contactos/
│
├── contactos.py              # Código principal del sistema
├── contactos.json            # Base de datos (generado automáticamente)
├── README.md                 # Documentación del proyecto
└── .gitignore               # Archivos ignorados por Git
```

### Diagrama de Clases

```
┌─────────────────────────┐
│      Contacto           │
├─────────────────────────┤
│ - _nombre: str          │
│ - _telefono: str        │
│ - _correo: str          │
│ - _direccion: str       │
├─────────────────────────┤
│ + __init__()            │
│ + to_dict()             │
│ + from_dict()           │
│ + propiedades (getters/ │
│   setters)              │
└─────────────────────────┘
           ▲
           │ usa
           │
┌─────────────────────────┐
│   GestorContactos       │
├─────────────────────────┤
│ - _contactos: List      │
│ - _archivo: str         │
├─────────────────────────┤
│ + agregar_contacto()    │
│ + editar_contacto()     │
│ + eliminar_contacto()   │
│ + buscar_por_nombre()   │
│ + buscar_por_telefono() │
│ + listar_todos()        │
│ + obtener_estadisticas()│
└─────────────────────────┘
           ▲
           │ usa
           │
┌─────────────────────────┐
│   InterfazUsuario       │
├─────────────────────────┤
│ - gestor: GestorContactos│
├─────────────────────────┤
│ + mostrar_menu()        │
│ + ejecutar()            │
│ + métodos privados      │
│   para cada opción      │
└─────────────────────────┘
```

---

## 🚀 Instalación y Configuración

### Paso 1: Instalar Python

**Windows:**
1. Descargar Python desde https://www.python.org/downloads/
2. Ejecutar el instalador
3. ✅ **IMPORTANTE**: Marcar "Add Python to PATH"
4. Verificar instalación:
   ```bash
   python --version
   ```

**macOS:**
```bash
# Usando Homebrew
brew install python3
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

### Paso 2: Instalar Visual Studio Code

1. Descargar desde https://code.visualstudio.com/
2. Instalar la extensión de Python:
   - Abrir VS Code
   - Ir a Extensiones (Ctrl+Shift+X)
   - Buscar "Python"
   - Instalar la extensión de Microsoft

### Paso 3: Configurar el Proyecto

1. **Crear carpeta del proyecto:**
   ```bash
   mkdir sistema-gestion-contactos
   cd sistema-gestion-contactos
   ```

2. **Abrir en VS Code:**
   ```bash
   code .
   ```

3. **Crear archivos:**
   - Crear `contactos.py` y copiar el código principal
   - Crear `README.md` con la documentación

4. **Crear archivo .gitignore:**
   ```
   # Python
   __pycache__/
   *.py[cod]
   *$py.class
   *.so
   .Python
   
   # Archivos de datos
   contactos.json
   contactos_test.json
   contactos_integracion.json
   
   # VS Code
   .vscode/
   
   # Entorno virtual
   venv/
   env/
   ```

---

## 📖 Guía de Uso

### Ejecutar la Aplicación

1. **Desde la terminal:**
   ```bash
   python contactos.py
   ```

2. **Desde VS Code:**
   - Abrir `contactos.py`
   - Presionar F5 o clic en "Run" > "Run Without Debugging"

### Uso del Menú Principal

```
==================================================
       SISTEMA DE GESTIÓN DE CONTACTOS
==================================================

1. Agregar contacto
2. Editar contacto
3. Eliminar contacto
4. Buscar contacto por nombre
5. Buscar contacto por teléfono
6. Listar todos los contactos
7. Ver estadísticas
8. Salir
--------------------------------------------------
```

### Ejemplos de Uso

#### 1️⃣ Agregar un Contacto
```
Seleccione una opción: 1

--- AGREGAR NUEVO CONTACTO ---
Nombre completo: Juan Pérez
Teléfono: +56912345678
Correo electrónico: juan.perez@email.com
Dirección: Av. Principal 123, Valparaíso

✓ Contacto agregado exitosamente!
```

#### 2️⃣ Buscar por Nombre
```
Seleccione una opción: 4

--- BUSCAR POR NOMBRE ---
Ingrese el nombre a buscar: Juan

✓ Se encontraron 1 contacto(s):
╔═══════════════════════════════════════╗
  Nombre:    Juan Pérez
  Teléfono:  +56912345678
  Correo:    juan.perez@email.com
  Dirección: Av. Principal 123, Valparaíso
╚═══════════════════════════════════════╝
```

#### 3️⃣ Editar un Contacto
```
Seleccione una opción: 2

--- EDITAR CONTACTO ---
Ingrese el teléfono del contacto a editar: +56912345678

Contacto actual:
[Se muestra el contacto]

Ingrese los nuevos datos (presione Enter para mantener el actual):
Nombre [Juan Pérez]: Juan Carlos Pérez
Teléfono [+56912345678]: 
Correo [juan.perez@email.com]: juanc.perez@email.com
Dirección [Av. Principal 123, Valparaíso]: 

✓ Contacto editado exitosamente!
```

#### 4️⃣ Ver Estadísticas
```
Seleccione una opción: 7

--- ESTADÍSTICAS DEL SISTEMA ---
Total de contactos:        15
Contactos con correo:      15
Contactos con dirección:   12
```

---

## 🔧 Estructura del Código

### Clase `Contacto`

**Responsabilidad**: Representar un contacto individual con encapsulación completa.

**Atributos privados:**
- `_nombre`: Nombre del contacto
- `_telefono`: Número telefónico
- `_correo`: Dirección de correo electrónico
- `_direccion`: Dirección física

**Métodos principales:**

```python
# Constructor
__init__(nombre, telefono, correo, direccion)

# Propiedades (getters y setters)
@property
def nombre(self) -> str

@nombre.setter
def nombre(self, valor: str)

# Conversión de datos
to_dict() -> Dict[str, str]          # Contacto → Diccionario
from_dict(data) -> Contacto          # Diccionario → Contacto

# Validaciones
_validar_correo(correo) -> bool      # Valida formato email
```

**Principios aplicados:**
- ✅ **Encapsulación**: Atributos privados con acceso controlado
- ✅ **Validación**: Datos validados en setters
- ✅ **Type hints**: Documentación clara de tipos

### Clase `GestorContactos`

**Responsabilidad**: Gestionar la colección de contactos y persistencia.

**Atributos:**
- `_contactos`: Lista de objetos Contacto
- `_archivo`: Nombre del archivo JSON para persistencia

**Métodos CRUD:**

```python
# Create
agregar_contacto(contacto: Contacto) -> bool

# Read
buscar_por_nombre(nombre: str) -> List[Contacto]
buscar_por_telefono(telefono: str) -> Optional[Contacto]
listar_todos() -> List[Contacto]

# Update
editar_contacto(telefono: str, nuevo_contacto: Contacto) -> bool

# Delete
eliminar_contacto(telefono: str) -> bool

# Estadísticas
obtener_estadisticas() -> Dict[str, int]

# Persistencia
_guardar_contactos() -> None
_cargar_contactos() -> None
```

**Características:**
- ✅ Validación de duplicados (por teléfono)
- ✅ Búsqueda case-insensitive
- ✅ Persistencia automática
- ✅ Manejo robusto de errores

### Clase `InterfazUsuario`

**Responsabilidad**: Interactuar con el usuario a través de la consola.

**Métodos públicos:**
```python
mostrar_menu() -> None    # Muestra el menú principal
ejecutar() -> None         # Bucle principal de la aplicación
```

**Métodos privados (uno por cada opción):**
```python
_agregar_contacto()
_editar_contacto()
_eliminar_contacto()
_buscar_por_nombre()
_buscar_por_telefono()
_listar_contactos()
_mostrar_estadisticas()
```

**Características:**
- ✅ Validación de entrada de usuario
- ✅ Mensajes claros de error
- ✅ Confirmación para operaciones destructivas
- ✅ Formateo visual atractivo

---

## 🎯 Características Técnicas

### 1. Programación Orientada a Objetos

**Encapsulación:**
```python
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self._nombre = nombre      # Atributo privado
        self._telefono = telefono
        # ...
    
    @property
    def nombre(self):              # Getter
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):       # Setter con validación
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()
```

### 2. Estructuras de Datos

**Lista de contactos:**
```python
self._contactos: List[Contacto] = []
```

**Diccionario para serialización:**
```python
def to_dict(self) -> Dict[str, str]:
    return {
        'nombre': self._nombre,
        'telefono': self._telefono,
        'correo': self._correo,
        'direccion': self._direccion
    }
```

### 3. Persistencia de Datos

**Formato JSON:**
```json
[
  {
    "nombre": "Juan Pérez",
    "telefono": "+56912345678",
    "correo": "juan@email.com",
    "direccion": "Av. Principal 123"
  }
]
```

**Operaciones:**
- Guardado automático después de cada modificación
- Carga automática al iniciar el programa
- Codificación UTF-8 para caracteres especiales
- Manejo de errores robusto

### 4. Validaciones

**Validación de correo electrónico:**
```python
@staticmethod
def _validar_correo(correo: str) -> bool:
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))
```

**Validación de duplicados:**
```python
if self.buscar_por_telefono(contacto.telefono):
    raise ValueError(f"Ya existe un contacto con el teléfono {contacto.telefono}")
```

### 5. Manejo de Errores

```python
try:
    contacto = Contacto(nombre, telefono, correo, direccion)
    self.gestor.agregar_contacto(contacto)
    print("\n✓ Contacto agregado exitosamente!")
except ValueError as e:
    print(f"\n❌ Error: {e}")
except Exception as e:
    print(f"\n❌ Error inesperado: {e}")
```

---

## 📚 Referencias y Fuentes

### Documentación Oficial de Python

1. **Python Official Documentation**
   - URL: https://docs.python.org/3/
   - Uso: Referencia general de Python 3.8+

2. **Python Tutorial - Classes**
   - URL: https://docs.python.org/3/tutorial/classes.html
   - Uso: Programación orientada a objetos en Python

3. **JSON Module Documentation**
   - URL: https://docs.python.org/3/library/json.html
   - Uso: Manejo de archivos JSON para persistencia

4. **unittest — Unit Testing Framework**
   - URL: https://docs.python.org/3/library/unittest.html
   - Uso: Framework de pruebas unitarias

5. **re — Regular Expression Operations**
   - URL: https://docs.python.org/3/library/re.html
   - Uso: Validación de correo electrónico

6. **typing — Support for Type Hints**
   - URL: https://docs.python.org/3/library/typing.html
   - Uso: Type hints para mejor documentación

### Tutoriales y Guías

7. **Real Python - OOP in Python**
   - URL: https://realpython.com/python3-object-oriented-programming/
   - Uso: Mejores prácticas de POO

8. **PEP 8 — Style Guide for Python Code**
   - URL: https://peps.python.org/pep-0008/
   - Uso: Convenciones de estilo de código

9. **Python Package Index (PyPI)**
   - URL: https://pypi.org/
   - Uso: Referencia de paquetes (aunque no usamos externos)

### Conceptos Aplicados

10. **CRUD Operations**
    - Concepto: Create, Read, Update, Delete
    - Implementado en: GestorContactos

11. **Encapsulation in Python**
    - Concepto: Uso de atributos privados (_attribute)
    - Implementado en: Clase Contacto

12. **Properties and Decorators**
    - Concepto: @property, @setter
    - Implementado en: Getters y setters de Contacto

### Herramientas de Desarrollo

13. **Visual Studio Code**
    - URL: https://code.visualstudio.com/docs/python/python-tutorial
    - Uso: Editor de código principal

14. **Git Documentation**
    - URL: https://git-scm.com/doc
    - Uso: Control de versiones

15. **GitHub Guides**
    - URL: https://guides.github.com/
    - Uso: Repositorio y colaboración

---

## 🎓 Conceptos Teóricos Implementados

### 1. Encapsulación
- Atributos privados con prefijo `_`
- Acceso controlado mediante propiedades
- Validación en setters

### 2. Abstracción
- Clases que representan conceptos del mundo real
- Interfaces claras y simples para el usuario
- Complejidad oculta en implementación privada

### 3. Modularidad
- Separación de responsabilidades por clase
- Funciones y métodos con propósito único
- Código reutilizable y mantenible

### 4. Persistencia de Datos
- Serialización a JSON
- Carga automática al iniciar
- Guardado automático tras modificaciones

### 5. Validación de Datos
- Validación de entrada de usuario
- Validación de formato (email)
- Prevención de datos duplicados

### 6. Testing
- Pruebas unitarias automatizadas
- Pruebas de integración
- Cobertura completa de funcionalidades

---

## 📞 Contacto y Soporte

Para preguntas sobre el proyecto:
- Revisar la documentación en el README
- Consultar la documentación oficial de Python
- Verificar los comentarios en el código fuente

---

## 📄 Licencia

Este proyecto es educativo y está disponible para uso académico.

---

**Última actualización**: Enero 2026  
**Versión**: 1.0.0  
**Autor**: José Tomás Latorre