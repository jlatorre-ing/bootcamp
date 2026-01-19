# 📇 Sistema de Gestión de Contactos

Sistema completo de gestión de contactos desarrollado en Python con Programación Orientada a Objetos, persistencia de datos y pruebas unitarias completas.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## 📋 Descripción

Aplicación de consola que permite gestionar contactos personales con las siguientes funcionalidades:

- ✅ **Agregar contactos** con validación de datos
- ✏️ **Editar contactos** existentes
- 🗑️ **Eliminar contactos** con confirmación
- 🔍 **Buscar** por nombre o teléfono
- 📊 **Listar** todos los contactos ordenados
- 📈 **Estadísticas** del sistema
- 💾 **Persistencia** automática en JSON

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.8 o superior
- Visual Studio Code (recomendado)

### Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/jlatorre-ing/bootcamp/tree/main/Modulo2/ProyectoM2
cd ProyectoM2
```

2. **Ejecutar la aplicación:**
```bash
python contactos.py
```

### Primer Uso

Al ejecutar el programa, verás el menú principal:

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

## 📁 Estructura del Proyecto

```
sistema-gestion-contactos/
│
├── contactos.py              # Código principal (clases y lógica)
├── contactos.json            # Base de datos 
├── README.md                 # Este archivo
├── DOCUMENTACION.md          # Documentación técnica detallada
└── .gitignore               # Archivos ignorados por Git
```

## 🎯 Características Técnicas

### Programación Orientada a Objetos

- **Encapsulación**: Atributos privados con getters/setters
- **Validación**: Control de datos en tiempo real
- **Type Hints**: Documentación clara de tipos
- **Modularidad**: Separación clara de responsabilidades

### Estructuras de Datos

```python
# Lista de contactos
contactos: List[Contacto]

# Diccionario para cada contacto
{
    'nombre': 'Juan Pérez',
    'telefono': '+56912345678',
    'correo': 'juan@email.com',
    'direccion': 'Av. Principal 123'
}
```

### Persistencia

- Formato: JSON con codificación UTF-8
- Guardado: Automático tras cada operación
- Carga: Automática al iniciar la aplicación

## 💻 Ejemplos de Uso

### Agregar un Contacto

```python
>>> # En el menú, seleccionar opción 1
>>> Nombre completo: María García
>>> Teléfono: +56987654321
>>> Correo electrónico: maria.garcia@email.com
>>> Dirección: Calle Falsa 123, Santiago

✓ Contacto agregado exitosamente!
```

### Buscar Contacto

```python
>>> # Opción 4: Buscar por nombre
>>> Ingrese el nombre a buscar: María

✓ Se encontraron 1 contacto(s):
╔═══════════════════════════════════════╗
  Nombre:    María García
  Teléfono:  +56987654321
  Correo:    maria.garcia@email.com
  Dirección: Calle Falsa 123, Santiago
╚═══════════════════════════════════════╝
```

## 📊 Validaciones Implementadas

### Validación de Correo Electrónico

```python
# Acepta:
usuario@dominio.com
nombre.apellido@empresa.cl
user123@test.org

# Rechaza:
correo_invalido
@dominio.com
usuario@
```

### Validación de Duplicados

El sistema previene contactos con el mismo número de teléfono:

```python
if telefono ya existe:
    raise ValueError("Ya existe un contacto con ese teléfono")
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **JSON**: Almacenamiento de datos
- **unittest**: Framework de pruebas
- **typing**: Type hints
- **re**: Validación con expresiones regulares

### Módulos Estándar de Python

```python
import json      # Manejo de archivos JSON
import os        # Operaciones con archivos
import re        # Expresiones regulares
from typing import List, Optional, Dict
import unittest  # Pruebas unitarias
```

## 📚 Documentación

- **[Documentación Técnica Completa](DOCUMENTACION.md)**: Guía detallada con arquitectura, instalación paso a paso y referencias
- **Comentarios en código**: Docstrings en todas las clases y métodos
- **Type hints**: Tipos claramente especificados

## 🎓 Conceptos Aplicados

Este proyecto implementa los siguientes conceptos de programación:

1. **Programación Orientada a Objetos**
   - Clases y objetos
   - Encapsulación
   - Properties (getters/setters)

2. **Estructuras de Datos**
   - Listas
   - Diccionarios
   - Type hints

3. **Manejo de Archivos**
   - Lectura/escritura JSON
   - Persistencia de datos

4. **Validación de Datos**
   - Expresiones regulares
   - Validación de entrada
   - Manejo de errores

## 🤝 Contribuciones

Este es un proyecto educativo. Si deseas mejorarlo:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Tareas Pendientes

- [ ] Agregar interfaz gráfica (GUI) con tkinter
- [ ] Implementar exportación a CSV/Excel
- [ ] Añadir fotos de perfil para contactos
- [ ] Categorías de contactos (familia, trabajo, etc.)
- [ ] Backup automático de la base de datos
- [ ] Búsqueda avanzada con filtros múltiples

## 🐛 Reporte de Bugs

Si encuentras un bug, por favor abre un issue en GitHub con:

- Descripción del problema
- Pasos para reproducirlo
- Comportamiento esperado
- Screenshots (si aplica)

## 👨‍💻 Autor

**Jose Tomas Latorre**
- GitHub: [@jlatorre-ing](https://github.com/jlatorre-ing)
- Email: j.contreraslatorre@gmail.com

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- Documentación oficial de Python
- Comunidad de Python Chile
- Real Python tutorials
- Stack Overflow community

## 📞 Soporte

¿Necesitas ayuda?

- 📖 Lee la [documentación técnica](DOCUMENTACION.md)
- 💬 Abre un issue en GitHub
- 📧 Envía un email

---

⭐ **Si este proyecto te fue útil, considera darle una estrella en GitHub**

**Hecho con ❤️ y Python**