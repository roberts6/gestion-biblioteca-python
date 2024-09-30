from datetime import datetime

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo=None, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo if fecha_prestamo else datetime.now()
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False
    
    def devolver_libro(self):
        """Marca el libro como devuelto y registra la fecha de devolución."""
        if not self.devuelto:
            self.fecha_devolucion = datetime.now()
            self.devuelto = True
            print(f"Libro '{self.libro.nombre}' devuelto por {self.usuario.nombre} el {self.fecha_devolucion.strftime('%d-%m-%Y')}")
        else:
            print(f"El libro '{self.libro.nombre}' ya fue devuelto.")
    
    def mostrar_informacion(self):
        """Muestra la información del préstamo."""
        estado = "Devuelto" if self.devuelto else "En préstamo"
        info_prestamo = f"""
        Libro: {self.libro.nombre}
        Usuario: {self.usuario.nombre}
        Fecha de Préstamo: {self.fecha_prestamo.strftime('%d-%m-%Y')}
        Estado: {estado}
        """
        if self.fecha_devolucion:
            info_prestamo += f"Fecha de Devolución: {self.fecha_devolucion.strftime('%d-%m-%Y')}"
        
        print(info_prestamo)


