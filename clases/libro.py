class Libro:
    def __init__(self, nombre, autor, genero, cantidad, paginas):
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        self.cantidad = cantidad
        self.paginas = paginas
        
    def actualizar_cantidad(self, cantidad):
        if cantidad:
            self.cantidad = cantidad
    
    def actualizar_autor(self, autor):
        if autor:
            self.autor = autor
            
    def actualizar_genero(self, genero):
        if genero:
            self.genero = genero
            
    def actualizar_nombre(self, nombre):
        if nombre:
            self.nombre = nombre
    
    def actualizar_paginas(self, paginas):
        if paginas:
            self.paginas = paginas