# -*- coding: utf-8 -*-





from biblioteca import Biblioteca
from interfaz import *

class AppBiblioteca:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def run(self):
        while True:
            op = menu('Menú principal',
                      (('Gestión usuarios',  self.gestion_usuarios),
                       ('Gestión libros',    self.gestion_libros),
                       ('Gestión préstamos', self.gestion_prestamos),
                       ('Leer base de datos', self.leer_datos),
                       ('Guardar base de datos', self.guardar_datos),
                       ('Salir del programa',None)))
            if op is None:
                return
            op()

    ######################################################################
    # LEER Y GUARDAR BASE DE DATOS
    ######################################################################

    def leer_datos(self):
        directorio = seleccionar_fichero('Nombre de la carpeta a leer',
                                         es_directorio=True)

        ok, msg = self.biblioteca.leer_datos_biblioteca(directorio)
        notificar(msg, ok=ok, titulo='Leyendo datos')

    def guardar_datos(self):
        directorio = seleccionar_fichero('Nombre de la carpeta para guardar los datos',
                                         es_directorio=True,
                                         save_mode=True)
        print(directorio)
        ok, msg = self.biblioteca.guardar_datos_biblioteca(directorio)
        notificar(msg, ok=ok, titulo='Guardando datos')

    ######################################################################
    # GESTION DE USUARIOS
    ######################################################################

    def gestion_usuarios(self):
        while True:
            op = menu('Gestión de usuarios',
                      (('Alta usuario',   self.alta_usuario),
                       ('Baja usuario',   self.baja_usuario),
                       ('Buscar usuario por DNI', self.buscar_usuario_dni),
                       ('Búsqueda avanzada de usuarios', self.listar_usuarios),
                       ('Salir de gestión de usuarios', None)))
            if op is None:
                return
            op()

    def alta_usuario(self):
        dni, nombre = pedir_campos(('DNI','Nombre'),titulo='Alta de usuario')
        tipo = menu('Tipo de usuario',
                    (('personal','personal'),
                     ('estudiante','estudiante'),
                     ('externo','externo')))
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg = self.biblioteca.alta_usuario(dni,nombre,tipo)
        notificar(msg, ok=ok, titulo='Alta de usuario')

    def baja_usuario(self):
        dni = pedir_campo('DNI', titulo='Baja de usuario')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg = self.biblioteca.baja_usuario(dni)
        notificar(msg, ok=ok, titulo='Baja de usuario')

    def buscar_usuario_dni(self):
        dni = pedir_campo('DNI', titulo='Búsqueda de usuario')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg = self.biblioteca.buscar_usuario_dni(dni)
        if not ok:
            notificar(msg ,ok=False,
                      titulo='Buscar usuario')
        else:
            listar([msg], titulo='Usuario:')

    def listar_usuarios(self):
        nom, tip = pedir_campos(
            ('Nombre contiene',
             'And tipo (personal, estudiante, externo) contiene'),
            permite_vacios=True)
        listado = self.biblioteca.listar_usuarios(nom,tip)
        resultados = len(listado)
        if resultados == 0:
            notificar('No se ha encontrado ningún usuario',ok=False,
                      titulo='Listar usuarios')
        else:
            listar(listado, titulo=f'Listado de usuarios ({resultados} resultados)')

    ######################################################################
    # GESTION DE LIBROS
    ######################################################################

    def gestion_libros(self):
        while True:
            op = menu('Gestión de libros',
                      (('Alta libro', self.alta_libro),
                       ('Baja libro', self.baja_libro),
                       ('Alta ejemplar', self.alta_ejemplar),
                       ('Baja ejemplar', self.baja_ejemplar),
                       ('Búsqueda avanzada de libros', self.busqueda_avanzada_libros),
                       ('Listar libros', self.listar_libros),
                       ('Listar ejemplares de un libro', self.listar_ejemplares),
                       ('Salir de gestión de libros', None)))
            if op is None:
                return
            op()

    def alta_libro(self):
        isbn, titulo, autor, editorial, fecha = pedir_campos(
            ('ISBN',
             'Título',
             'Autor',
             'Editorial',
             'Fecha'),
            titulo='Alta de libro')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg = self.biblioteca.alta_libro(titulo, isbn, fecha, editorial, autor)
        notificar(msg,ok=ok,titulo='Alta de libro')

    def baja_libro(self):
        isbn = pedir_campo('Introduce ISBN', titulo='Baja de libro')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg = self.biblioteca.baja_libro(isbn)
        notificar(msg,ok=ok,titulo='Baja de libro')

    def alta_ejemplar(self):
        isbn, signatura = pedir_campos(('ISBN','Signatura'),
                                       titulo='Alta de ejemplar')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, mensaje = self.biblioteca.alta_ejemplar(isbn,signatura)
        notificar(mensaje, ok=ok, titulo='Alta de ejemplar')

    def baja_ejemplar(self):
        signatura = pedir_campo('Signatura', titulo='Baja de ejemplar')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, mensaje = self.biblioteca.baja_ejemplar(signatura)
        notificar(mensaje, ok=ok, titulo='Baja de ejemplar')

    def busqueda_avanzada_libros(self):
        tit, aut, edi = pedir_campos(
            ('Título contiene',
             'And autor contiene',
             'And editorial contiene'),
            permite_vacios=True)
        resultado = self.biblioteca.busqueda_avanzada(tit, aut, edi)
        numresultados = len(resultado)
        if numresultados==0:
            notificar('No se ha encontrado ningún libro',ok=False)
        else:
            listar(resultado, titulo=f'Libros ({numresultados} resultados)')

    def listar_libros(self):
        listado = self.biblioteca.listado_libros()
        numlibros = len(listado)
        if numlibros==0:
            notificar('No se ha encontrado ningún libro',ok=False)
        else:
            listar(listado, titulo=f'Listado de libros ({numlibros} resultados)')

    def listar_ejemplares(self):
        isbn = pedir_campo('Introduce ISBN',
                           titulo='Listar ejemplares')
        ok, ejemplares = self.biblioteca.listar_ejemplares(isbn)
        if not ok:
            notificar('No hay libros con ese ISBN',ok=False,
                      titulo='Listar ejemplares')
        else:
            numejemplares = len(ejemplares)
            if numejemplares==0:
                notificar('No hay ejemplares disponibles',ok=False,
                          titulo='Listar ejemplares')
            else:
                listar(ejemplares, titulo=f'{numejemplares} Ejemplares:')

    ######################################################################
    # GESTION DE PRESTAMOS
    ######################################################################

    def gestion_prestamos(self):
        while True:
            op = menu('Gestión de préstamos',
                      (('Prestamos usuario', self.prestamos_usuario),
                       ('Disponibilidad de ejemplar', self.disponibilidad_ejemplar),
                       ('Solicitar préstamo', self.solicitar_prestamo),
                       ('Devolver prestado', self.devolver_prestamo),
                       ('Salir de gestión de préstamos', None)))
            if op is None:
                return
            op()

    def prestamos_usuario(self):
        dni = pedir_campo('DNI',titulo='Prestamos del usuario')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, prestamos = self.biblioteca.ver_prestamos_usuario(dni)
        if not ok:
            notificar('Usuario no encontrado',ok=False)
        else:
            numprestamos = len(prestamos)
            if numprestamos==0:
                notificar('El usuario no tienen ningún préstamo',ok=False)
            else:
                listar(prestamos, titulo=f'Prestamos del usuario ({numprestamos} prestamos)')

    def disponibilidad_ejemplar(self):
        signatura = pedir_campo('signatura',titulo='Disponibilidad del ejemplar')
        ok, disponibilidad = self.biblioteca.disponibilidad_ejemplar(signatura)
        notificar(disponibilidad, ok=ok, titulo='Disponibilidad del ejemplar')

    def solicitar_prestamo(self):
        dni, signatura = pedir_campos(
                ('DNI usuario',
                 'Signatura ejemplar'),
                titulo='Solicitar préstamo')
        ok, mensaje = self.biblioteca.solicitar_prestamo(dni,signatura)
        notificar(mensaje, ok=ok, titulo='Solicitar préstamo')

    def devolver_prestamo(self):
        dni, signatura = pedir_campos(
                ('DNI usuario',
                 'Signatura ejemplar'),
                titulo='Devolver préstamo')
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, mensaje = self.biblioteca.devolver_prestamo(dni,signatura)
        notificar(mensaje, ok=ok, titulo='Devolver préstamo')


######################################################################
# PROGRAMA PRINCIPAL
######################################################################

if __name__ == '__main__':
    app = AppBiblioteca()
    app.run()

