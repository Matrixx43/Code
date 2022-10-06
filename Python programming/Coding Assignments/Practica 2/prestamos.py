# -*- coding: utf-8 -*-






class Prestamo:

    # variables de clase utilizada como constante:
    MAX_EJEMPLARES_POR_USUARIO = 4

    def __init__(self, usuario, ejemplar):
        self.usuario = usuario
        self.ejemplar = ejemplar

    def __str__(self):
        """
        El metodo __str__ se utliza cuando mostramos el objeto con str(),
        con print(),...
        """
        return (f'Prestado a: {self.usuario.nombre}\n' +
                f'Signatura: {self.ejemplar.signatura}\n')
