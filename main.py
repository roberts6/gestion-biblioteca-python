'''
problemática:
 modernizar el sistema de gestión de la biblioteca usando programación orientada a objetos. El sistema debe
 permitir registrar libros, usuarios, realizar préstamos, devoluciones y consultar el estado del libro
'''

from clases.inventario import Inventario
from clases.usuario import Usuario, listado_usuarios
from clases.prestamo import Prestamo
from clases.libro import Libro

# Creo instancia de Inventario y un estado global de préstamos 
inventario = Inventario()
prestamos = []

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n--- Menú de Gestión de Libros ---")
    print("1. Registrar nuevo usuario")
    print("2. Agregar libro al inventario")
    print("3. Ver libros en el inventario")
    print("4. Registrar préstamo de libro")
    print("5. Ver préstamos activos")
    print("6. Devolver un libro")
    print("7. Ver usuarios registrados")
    print("8. Eliminar libro")
    print("9. Salir")

def registrar_usuario():
    """Registra un nuevo usuario en el sistema."""
    nombre = input("Nombre del usuario: ")
    fecha_nacimiento = input("Fecha de nacimiento (dd-mm-yyyy): ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    usuario = Usuario(nombre, fecha_nacimiento, direccion, telefono, email)
    print(f"Usuario {usuario.nombre} registrado con éxito.")

def agregar_libro():
    """Agrega un libro al inventario."""
    nombre = input("Nombre del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    try:
        cantidad = int(input("Cantidad disponible: "))
        paginas = int(input("Número de páginas: "))
        inventario.agregar_libro(nombre, autor, genero, cantidad, paginas)
    except ValueError:
        print("Por favor, ingresa números válidos para la cantidad y páginas.")

def registrar_prestamo():
    """Registra un préstamo de un libro a un usuario."""
    nombre_usuario = input("Nombre del usuario que toma el préstamo: ")
    usuario = next((u for u in listado_usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print(f"Usuario {nombre_usuario} no encontrado.")
        return
    
    nombre_libro = input("Nombre del libro a prestar: ")
    libro = inventario.buscar_libro(nombre=nombre_libro)
    if not libro:
        print(f"Libro {nombre_libro} no encontrado en el inventario.")
        return
    
    if libro.cantidad < 1:
        print(f"No hay copias disponibles de '{libro.nombre}'.")
        return

    libro.cantidad -= 1  # Reducir la cantidad disponible en el inventario
    prestamo = Prestamo(libro, usuario)
    prestamos.append(prestamo)
    print(f"Préstamo de '{libro.nombre}' a {usuario.nombre} registrado con éxito.")

def ver_prestamos():
    """Muestra los préstamos activos."""
    if not prestamos:
        print("No hay préstamos activos.")
    else:
        for prestamo in prestamos:
            prestamo.mostrar_informacion()

def devolver_libro():
    """Devuelve un libro prestado."""
    nombre_usuario = input("Nombre del usuario que devuelve el libro: ")
    usuario = next((u for u in listado_usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print(f"Usuario {nombre_usuario} no encontrado.")
        return
    
    nombre_libro = input("Nombre del libro a devolver: ")
    prestamo = next((p for p in prestamos if p.libro.nombre == nombre_libro and p.usuario.nombre == nombre_usuario and not p.devuelto), None)
    
    if not prestamo:
        print(f"No se encontró un préstamo activo para el libro '{nombre_libro}' y el usuario {nombre_usuario}.")
        return
    
    prestamo.devolver_libro()
    prestamo.libro.cantidad += 1  # Restaurar la cantidad en el inventario

def ver_usuarios():
    """Muestra los usuarios registrados."""
    if not listado_usuarios:
        print("No hay usuarios registrados.")
    else:
        for usuario in listado_usuarios:
            print(usuario.mostrar_informacion())
            
def eliminar_libro(inventario):
    id_libro = int(input("Por favor ingresa el id del libro que quieras eliminar "))
    if id_libro is not None:
        inventario.eliminar_libro(id_libro)
        print(f"Libro con ID: {id_libro} eliminado correctamente")
    else:
        print("Por favor, proporciona un ID válido.")
        
            
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            inventario.ver_libros()
        elif opcion == "4":
            registrar_prestamo()
        elif opcion == "5":
            ver_prestamos()
        elif opcion == "6":
            devolver_libro()
        elif opcion == "7":
            ver_usuarios()
        elif opcion == "8":
            eliminar_libro(inventario)
        elif opcion == "9":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
