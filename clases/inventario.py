from clases.libro import Libro

class Inventario:
    def __init__(self):
        self.contador_id = 1
        self.lista_libros = []
        
    def generar_id(self):
        id_actual = self.contador_id 
        self.contador_id += 1
        return id_actual
        
    def agregar_libro(self, nombre, autor, genero, cantidad, paginas):
        libro = Libro(nombre, autor, genero, cantidad, paginas) #instancia de la clase Libro
        libro.id = self.generar_id()
        self.lista_libros.append(libro)
        print(f"El libro '{libro.nombre}' ha sido agregado con éxito. Id: {libro.id}")
                # toma el valor del argumento                  # toma el valor del diccionario creado
    
    def actualizar_libro(self, id_libro, autor=None, nombre=None, cantidad=None, paginas=None, genero=None):
        """Actualiza los detalles de un producto por su ID."""
        libro = self.buscar_libro(id_libro)
        if libro:
            if nombre:
                libro.actualizar_nombre(nombre)
            if autor:
                libro.actualizar_autor(autor)
            if genero:
                libro.actualizar_genero(genero)
            if cantidad:
                libro.actualizar_cantidad(cantidad)
            if paginas:
                libro.actualizar_paginas(paginas)
            print(f"El libro con ID {id_libro} ha sido actualizado.")
        else:
            print(f"Libro con ID {id_libro} no encontrado.")
        
    def eliminar_libro(self, id_libro) :
        libro = self.buscar_libro(id_libro)
        if libro:
            self.lista_libros.remove(libro)
            print("Libro eliminado con éxito")
        else:
            print("Libro no encontrado")
    
    def buscar_libro(self, id_libro=None, nombre=None):
        """Busca un libro por ID o nombre y lo devuelve si lo encuentra."""
        for libro in self.lista_libros:
            if (id_libro is not None and libro.id == id_libro) or \
               (nombre is not None and libro.nombre.lower() == nombre.lower()):
                return libro
        print("Libro no encontrado.")
        return None
    

    def ver_libros(self):
        """Muestra todos los libros del inventario."""
        if not self.lista_libros:
            print("No hay libros en el inventario.")
        else:
            print("Listado de libros en el inventario:")
            for libro in self.lista_libros:
                print(f"ID: {libro.id}, Nombre: {libro.nombre}, Autor: {libro.autor}, Género: {libro.genero}, Páginas: {libro.paginas}, Cantidad: {libro.cantidad}")
                # como libro es una clase se accede a sus atributos mediante .atributo. Si fuese un diccionario sería libro['clave']

