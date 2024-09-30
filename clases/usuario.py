from datetime import datetime

listado_usuarios = [] # listado global

class Usuario:
    contador_id = 1  # mantiene el siguiente ID disponible
    
    def __init__(self, nombre, fecha_nacimiento, direccion, telefono, email):
        self.id = Usuario.generar_id()  # Llamada al método de clase para generar el ID único
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")  # Convierte la fecha ingresada
        self.edad = self.calcular_edad()  # Llama a la función calcular_edad
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.fecha_registro = datetime.now()
        self.historial_alquiler_usuario = []
        
        # Agrega el usuario al listado global
        listado_usuarios.append(self)

    @classmethod
    def generar_id(cls):
        """Genera un ID único para cada usuario."""
        id_actual = cls.contador_id
        cls.contador_id += 1
        return id_actual
    
    def calcular_edad(self):
        """Calcula la edad del usuario en función de su fecha de nacimiento."""
        hoy = datetime.now()
        edad = hoy.year - self.fecha_nacimiento.year
        
        # Si aún no fue su cumpleaños este año, le resta 1 a la edad
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        
        return edad
    
    def actualizar_informacion(self, direccion=None, telefono=None):
        """Actualiza la dirección y/o teléfono del usuario."""
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
    
    def registrar_alquiler(self, alquiler):
        """Registra un nuevo alquiler para el usuario."""
        self.historial_alquiler_usuario.append(alquiler)
    
    @staticmethod
    def eliminar_usuario(id_usuario):
        """Elimina un usuario del listado de usuarios global por su ID."""
        global listado_usuarios
        for usuario in listado_usuarios:
            if usuario.id == id_usuario:
                listado_usuarios.remove(usuario)
                print(f"Usuario con ID {id_usuario} ha sido eliminado.")
                return
        print(f"No se encontró un usuario con ID {id_usuario}.")
    
    def mostrar_informacion(self):
        """Muestra la información detallada del usuario."""
        return f'''
        Usuario: {self.nombre}
        Edad: {self.edad} años
        Dirección: {self.direccion}
        Teléfono: {self.telefono}
        Email: {self.email}
        Fecha de registro: {self.fecha_registro.strftime('%d-%m-%Y %H:%M:%S')}
        '''


