# -*- coding: utf-8 -*-





class Usuario:
    def __init__(self, dni, nombre, tipo):
        self.dni = dni
        self.nombre = nombre
        self.tipo = tipo
        self.prestamos = [] # lista de objetos de tipo Prestamo

    def ejemplares_prestados(self):
        return len(self.prestamos)

    def __str__(self):
        """
        El metodo __str__ se utliza cuando mostramos el objeto con str(),
        con print(),...
        """
        resul = f'\nDNI: {self.dni}\nNombre: {self.nombre}\nTipo: {self.tipo}'
        if len(self.prestamos)>0:
            resul += f'\nLibros por devolver: {len(self.prestamos)}'
        return resul

