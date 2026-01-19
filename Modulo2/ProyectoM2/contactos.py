"""
Sistema de Gestión de Contactos
Autor: [Jose Latorre]
Fecha: Enero 2026
Descripción: Sistema para gestionar contactos con funcionalidades CRUD completas
"""

import json
import os
from typing import List, Optional, Dict
import re


class Contacto:
    """
    Clase que representa un contacto individual.
    Implementa encapsulación de datos y validaciones.
    """
    
    def __init__(self, nombre: str, telefono: str, correo: str, direccion: str):
        """
        Constructor de la clase Contacto.
        
        Args:
            nombre (str): Nombre completo del contacto
            telefono (str): Número telefónico
            correo (str): Dirección de correo electrónico
            direccion (str): Dirección física
        """
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo
        self._direccion = direccion
    
    # Propiedades con getters y setters (encapsulación)
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()
    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("El teléfono no puede estar vacío")
        self._telefono = valor.strip()
    
    @property
    def correo(self) -> str:
        return self._correo
    
    @correo.setter
    def correo(self, valor: str):
        if not self._validar_correo(valor):
            raise ValueError("Formato de correo inválido")
        self._correo = valor.strip()
    
    @property
    def direccion(self) -> str:
        return self._direccion
    
    @direccion.setter
    def direccion(self, valor: str):
        self._direccion = valor.strip() if valor else ""
    
    @staticmethod
    def _validar_correo(correo: str) -> bool:
        """Valida el formato básico de un correo electrónico."""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, correo))
    
    def to_dict(self) -> Dict[str, str]:
        """Convierte el contacto a diccionario para serialización."""
        return {
            'nombre': self._nombre,
            'telefono': self._telefono,
            'correo': self._correo,
            'direccion': self._direccion
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'Contacto':
        """Crea un contacto desde un diccionario."""
        return cls(
            nombre=data['nombre'],
            telefono=data['telefono'],
            correo=data['correo'],
            direccion=data['direccion']
        )
    
    def __str__(self) -> str:
        """Representación en string del contacto."""
        return f"""
╔═══════════════════════════════════════╗
  Nombre:    {self._nombre}
  Teléfono:  {self._telefono}
  Correo:    {self._correo}
  Dirección: {self._direccion}
╚═══════════════════════════════════════╝
"""
    
    def __repr__(self) -> str:
        return f"Contacto(nombre='{self._nombre}', telefono='{self._telefono}')"


class GestorContactos:
    """
    Clase principal para gestionar la colección de contactos.
    Implementa operaciones CRUD y persistencia de datos.
    """
    
    def __init__(self, archivo: str = 'contactos.json'):
        """
        Constructor del gestor de contactos.
        
        Args:
            archivo (str): Nombre del archivo JSON para persistencia
        """
        self._contactos: List[Contacto] = []
        self._archivo = archivo
        self._cargar_contactos()
    
    def agregar_contacto(self, contacto: Contacto) -> bool:
        """
        Agrega un nuevo contacto al sistema.
        
        Args:
            contacto (Contacto): Objeto contacto a agregar
            
        Returns:
            bool: True si se agregó exitosamente
        """
        # Verificar si ya existe un contacto con el mismo teléfono
        if self.buscar_por_telefono(contacto.telefono):
            raise ValueError(f"Ya existe un contacto con el teléfono {contacto.telefono}")
        
        self._contactos.append(contacto)
        self._guardar_contactos()
        return True
    
    def editar_contacto(self, telefono: str, nuevo_contacto: Contacto) -> bool:
        """
        Edita un contacto existente.
        
        Args:
            telefono (str): Teléfono del contacto a editar
            nuevo_contacto (Contacto): Nuevos datos del contacto
            
        Returns:
            bool: True si se editó exitosamente
        """
        for i, contacto in enumerate(self._contactos):
            if contacto.telefono == telefono:
                self._contactos[i] = nuevo_contacto
                self._guardar_contactos()
                return True
        return False
    
    def eliminar_contacto(self, telefono: str) -> bool:
        """
        Elimina un contacto del sistema.
        
        Args:
            telefono (str): Teléfono del contacto a eliminar
            
        Returns:
            bool: True si se eliminó exitosamente
        """
        for i, contacto in enumerate(self._contactos):
            if contacto.telefono == telefono:
                self._contactos.pop(i)
                self._guardar_contactos()
                return True
        return False
    
    def buscar_por_nombre(self, nombre: str) -> List[Contacto]:
        """
        Busca contactos por nombre (búsqueda parcial, case-insensitive).
        
        Args:
            nombre (str): Nombre o parte del nombre a buscar
            
        Returns:
            List[Contacto]: Lista de contactos encontrados
        """
        nombre_lower = nombre.lower()
        return [c for c in self._contactos if nombre_lower in c.nombre.lower()]
    
    def buscar_por_telefono(self, telefono: str) -> Optional[Contacto]:
        """
        Busca un contacto por número de teléfono.
        
        Args:
            telefono (str): Número de teléfono a buscar
            
        Returns:
            Optional[Contacto]: Contacto encontrado o None
        """
        for contacto in self._contactos:
            if contacto.telefono == telefono:
                return contacto
        return None
    
    def listar_todos(self) -> List[Contacto]:
        """Retorna todos los contactos ordenados por nombre."""
        return sorted(self._contactos, key=lambda c: c.nombre.lower())
    
    def obtener_estadisticas(self) -> Dict[str, int]:
        """Retorna estadísticas del sistema."""
        return {
            'total_contactos': len(self._contactos),
            'con_correo': sum(1 for c in self._contactos if c.correo),
            'con_direccion': sum(1 for c in self._contactos if c.direccion)
        }
    
    def _guardar_contactos(self) -> None:
        """Guarda los contactos en el archivo JSON."""
        try:
            datos = [contacto.to_dict() for contacto in self._contactos]
            with open(self._archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error al guardar contactos: {e}")
    
    def _cargar_contactos(self) -> None:
        """Carga los contactos desde el archivo JSON."""
        if os.path.exists(self._archivo):
            try:
                with open(self._archivo, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    self._contactos = [Contacto.from_dict(d) for d in datos]
            except Exception as e:
                print(f"Error al cargar contactos: {e}")
                self._contactos = []


class InterfazUsuario:
    """
    Clase que gestiona la interfaz de usuario por consola.
    """
    
    def __init__(self):
        self.gestor = GestorContactos()
    
    def mostrar_menu(self) -> None:
        """Muestra el menú principal."""
        print("\n" + "="*50)
        print("  SISTEMA DE GESTIÓN DE CONTACTOS".center(50))
        print("="*50)
        print("\n1. Agregar contacto")
        print("2. Editar contacto")
        print("3. Eliminar contacto")
        print("4. Buscar contacto por nombre")
        print("5. Buscar contacto por teléfono")
        print("6. Listar todos los contactos")
        print("7. Ver estadísticas")
        print("8. Salir")
        print("-"*50)
    
    def ejecutar(self) -> None:
        """Ejecuta el bucle principal de la aplicación."""
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == '1':
                self._agregar_contacto()
            elif opcion == '2':
                self._editar_contacto()
            elif opcion == '3':
                self._eliminar_contacto()
            elif opcion == '4':
                self._buscar_por_nombre()
            elif opcion == '5':
                self._buscar_por_telefono()
            elif opcion == '6':
                self._listar_contactos()
            elif opcion == '7':
                self._mostrar_estadisticas()
            elif opcion == '8':
                print("\n¡Gracias por usar el sistema! Hasta pronto.\n")
                break
            else:
                print("\n❌ Opción inválida. Por favor, intente nuevamente.")
    
    def _agregar_contacto(self) -> None:
        """Solicita datos y agrega un nuevo contacto."""
        try:
            print("\n--- AGREGAR NUEVO CONTACTO ---")
            nombre = input("Nombre completo: ").strip()
            telefono = input("Teléfono: ").strip()
            correo = input("Correo electrónico: ").strip()
            direccion = input("Dirección: ").strip()
            
            contacto = Contacto(nombre, telefono, correo, direccion)
            self.gestor.agregar_contacto(contacto)
            print("\n✓ Contacto agregado exitosamente!")
        except ValueError as e:
            print(f"\n❌ Error: {e}")
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
    
    def _editar_contacto(self) -> None:
        """Solicita datos y edita un contacto existente."""
        print("\n--- EDITAR CONTACTO ---")
        telefono = input("Ingrese el teléfono del contacto a editar: ").strip()
        
        contacto_actual = self.gestor.buscar_por_telefono(telefono)
        if not contacto_actual:
            print("\n❌ Contacto no encontrado.")
            return
        
        print("\nContacto actual:")
        print(contacto_actual)
        
        try:
            print("\nIngrese los nuevos datos (presione Enter para mantener el actual):")
            nombre = input(f"Nombre [{contacto_actual.nombre}]: ").strip() or contacto_actual.nombre
            telefono_nuevo = input(f"Teléfono [{contacto_actual.telefono}]: ").strip() or contacto_actual.telefono
            correo = input(f"Correo [{contacto_actual.correo}]: ").strip() or contacto_actual.correo
            direccion = input(f"Dirección [{contacto_actual.direccion}]: ").strip() or contacto_actual.direccion
            
            nuevo_contacto = Contacto(nombre, telefono_nuevo, correo, direccion)
            self.gestor.editar_contacto(telefono, nuevo_contacto)
            print("\n✓ Contacto editado exitosamente!")
        except ValueError as e:
            print(f"\n❌ Error: {e}")
    
    def _eliminar_contacto(self) -> None:
        """Solicita confirmación y elimina un contacto."""
        print("\n--- ELIMINAR CONTACTO ---")
        telefono = input("Ingrese el teléfono del contacto a eliminar: ").strip()
        
        contacto = self.gestor.buscar_por_telefono(telefono)
        if not contacto:
            print("\n❌ Contacto no encontrado.")
            return
        
        print("\nContacto a eliminar:")
        print(contacto)
        
        confirmacion = input("¿Está seguro de eliminar este contacto? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.gestor.eliminar_contacto(telefono)
            print("\n✓ Contacto eliminado exitosamente!")
        else:
            print("\n❌ Operación cancelada.")
    
    def _buscar_por_nombre(self) -> None:
        """Busca y muestra contactos por nombre."""
        print("\n--- BUSCAR POR NOMBRE ---")
        nombre = input("Ingrese el nombre a buscar: ").strip()
        
        contactos = self.gestor.buscar_por_nombre(nombre)
        if contactos:
            print(f"\n✓ Se encontraron {len(contactos)} contacto(s):")
            for contacto in contactos:
                print(contacto)
        else:
            print("\n❌ No se encontraron contactos con ese nombre.")
    
    def _buscar_por_telefono(self) -> None:
        """Busca y muestra un contacto por teléfono."""
        print("\n--- BUSCAR POR TELÉFONO ---")
        telefono = input("Ingrese el teléfono a buscar: ").strip()
        
        contacto = self.gestor.buscar_por_telefono(telefono)
        if contacto:
            print("\n✓ Contacto encontrado:")
            print(contacto)
        else:
            print("\n❌ No se encontró ningún contacto con ese teléfono.")
    
    def _listar_contactos(self) -> None:
        """Lista todos los contactos."""
        contactos = self.gestor.listar_todos()
        if contactos:
            print(f"\n--- LISTA DE CONTACTOS ({len(contactos)}) ---")
            for i, contacto in enumerate(contactos, 1):
                print(f"\n{i}. {contacto}")
        else:
            print("\n❌ No hay contactos registrados.")
    
    def _mostrar_estadisticas(self) -> None:
        """Muestra estadísticas del sistema."""
        stats = self.gestor.obtener_estadisticas()
        print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
        print(f"Total de contactos:        {stats['total_contactos']}")
        print(f"Contactos con correo:      {stats['con_correo']}")
        print(f"Contactos con dirección:   {stats['con_direccion']}")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = InterfazUsuario()
    app.ejecutar()