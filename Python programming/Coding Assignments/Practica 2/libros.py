# -*- coding: utf-8 -*-




class Libro:
    def __init__(self, titulo, isbn, fecha, editorial, autor):
        self.titulo = titulo
        self.isbn = isbn
        self.fecha = fecha
        self.editorial = editorial
        self.autor = autor
        self.ejemplares = []

    def anyadir_ejemplar(self, Ejemplar):
            self.ejemplares.append(Ejemplar) 
        
    def eliminar_ejemplar(self, Ejemplar):
        try:
            self.ejemplares.remove(Ejemplar)
        except:
            pass
    
    def __str__(self):

        return(f"\nTitulo: {self.titulo}\n " +
                f"Autor: {self.autor}\n " +
                f"Editorial: {self.editorial}\n " +
                f"Fecha : {self.fecha}\n " +
                f"ISBN: {self.isbn}\n " +
                f"Nº de ejmplares: {len(self.ejemplares)} ")
        
    pass 
   # 9058093239
   # B 5-4/00971
   
class Ejemplar:
    def __init__(self, signatura, libro):
        self.signatura = signatura
        self.libro = libro
        self.prestamo = None

    def disponibilidad(self):
        if self.prestamo is None:
            estado = 'Disponible'
        else:
            estado = f'Prestado hasta {self.prestamo.prestado_hasta}'
        return estado

    def __str__(self):
        """
        El metodo __str__ se utliza cuando mostramos el objeto con str(),
        con print(),...
        """
        return (f'\nSignatura: {self.signatura}\n'+
                f'Estado: {self.disponibilidad()}')
                                     
