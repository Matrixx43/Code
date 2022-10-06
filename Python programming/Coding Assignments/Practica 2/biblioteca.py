# -*- coding: utf-8 -*-




from inspect import signature
from libros import Libro, Ejemplar
from usuarios import Usuario
from prestamos import Prestamo

import csv
import os

class Biblioteca:
    def __init__(self):
        self._libros     = {} # diccionario que asocia isbn a su libro
        self._ejemplares = {} # diccionario que asocia signatura a ejemplar
        self._usuarios   = {} # diccionario que asocia dni al usuario

    ######################################################################
    # GESTION LIBROS
    ######################################################################

    # AQUI va el metodo alta_libro
    def alta_libro(self, titulo, isbn, fecha, editorial, autor):
        if isbn in self._libros:
            return False, "Ya existe un libro con ese isbn"
        else:
            self._libros[isbn] = Libro(titulo, isbn, fecha, editorial, autor)
            return True, "Dado de alta Correctamente"

    # AQUI va el metodo baja_libro
    def baja_libro(self, isbn):
        if isbn not in self._libros:
            return  False, "No existe un libro con ese isbn"
        elif isbn in self._libros:
            if len(self._libros[isbn].ejemplares) > 0:
               return False, "No se puede dar de baja un libro con ejemplares"

            else:
                del self._libros[isbn]
                return True, "Dado de baja correctamente"


    # AQUI va el metodo alta_ejemplar
    def alta_ejemplar(self, isbn, signatura):
        if isbn not in self._libros:
            return False, "El libro no esta catalogado"

        elif signature in self._ejemplares:
            False, f"Ya hay un ejemplar con signatura: {signatura}"

        else:
            nuevoEjemplar = Ejemplar(signatura, self._libros[isbn])
            Libro.anyadir_ejemplar(self._libros[isbn], nuevoEjemplar)
            self._ejemplares[signatura] = nuevoEjemplar

            return True, "Ejemplar añadido satisfactoriamente"

    # AQUI va el metodo baja_ejemplar
    def baja_ejemplar(self, signatura):
        if signatura not in self._ejemplares:
            return False, "Ningun ejemplar con esa signatura"

        elif self._ejemplares[signatura].prestamo is not None:
            return False, "No se puede dar de baja un ejemplar mientras esta prestado"
            
        else:
           
           self._ejemplares[signatura].libro.eliminar_ejemplar(self._ejemplares[signatura])
           del self._ejemplares[signatura]
           return True, "Ejemplar eliminado satisfactoriamente"
        


            
            

    

    def listado_libros(self):
        # alternativamente:
        # return [str(libro) for libro in self._libros.values()]
        # o bien:
        # return map(str,self._libros.values())
        resul = []
        for libro in self._libros.values():
            resul.append(str(libro))
        return resul

    def busqueda_avanzada(self, tit, aut, edi):
        tit, aut, edi = tit.lower(), aut.lower(), edi.lower()
        resultado = []
        for libro in self._libros.values():
            if (tit in libro.titulo.lower() and
                aut in libro.autor.lower() and
                edi in libro.editorial.lower()):
                resultado.append(str(libro))
        return resultado

    def listar_ejemplares(self, isbn):
        if isbn not in self._libros:
            return False, f'No consta ningun libro con isbn {isbn}'
        resultado = []
        libro = self._libros[isbn]
        for ejemplar in libro.ejemplares:
            resultado.append(str(ejemplar))
        return True, resultado

    def leer_fichero_libros(self, filename):
        try:
            with open("libros.csv",'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                leidos = 0 # contador con propositos informativos
                next(reader) # nos saltamos la cabecera
                for tit, isbn, fecha, edi, aut in reader:
                    try:
                        self.alta_libro(tit, isbn, fecha, edi, aut)
                        leidos += 1
                    except Exception as msg:
                        return False, f"Error al leer fichero de libros: {msg}"
                   
                    # FIN COMPLETAR
                return True, f'{leidos} libros leidos correctamente'
        except Exception as ex:
            return (False, 'Error al leer fichero de libros. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')
        # no hay return en este punto porque se sale siempre en un return anterior

    def guardar_fichero_libros(self, filename):
        try:
            with open(filename,'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                # escribimos la cabecera:
                writer.writerow(['Titulo','ISBN','Fecha','Editorial','Autor'])
                # y el resto de filas:
                for lib in self._libros.values():
                    writer.writerow([lib.titulo, lib.isbn, lib.fecha,
                                     lib.editorial, lib.autor])
                return True, f'{len(self._libros)} libros guardados correctamente'
        except Exception as ex:
            return (False,'Error al guardar fichero de libros. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')
        # no hay return en este punto porque se sale siempre en un return anterior

    # AQUI va el metodo leer_fichero_ejemplares
    def leer_fichero_ejemplares(self, filename):
        try:
            with open("ejemplares.csv",'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                leidos = 0 # contador con propositos informativos
                next(reader) # nos saltamos la cabecera
                for isbn, signatura in reader:
                    try:
                        self.alta_ejemplar(isbn, signatura)
                        leidos += 1
                    except Exception as msg:
                        return False, f"Error al leer ejemplares en asignatura: {signatura}\n{msg}"
                   
                    # FIN COMPLETAR
                return True, f'{leidos} ejemplares leidos correctamente'
        except Exception as ex:
            return (False, 'Error al leer fichero de ejemplares. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')


    def guardar_fichero_ejemplares(self, filename):
        try:
            with open(filename,'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                # escribimos la cabecera:
                writer.writerow(['ISBN','Signatura'])
                # y el resto de filas:
                for ejemplar in self._ejemplares.values():
                    writer.writerow([ejemplar.libro.isbn, ejemplar.signatura])
                return True, f'{len(self._ejemplares)} Ejemplares guardados correctamente'
        except Exception as ex:
            return (False,'Error al guardar fichero de ejemplares. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')
        # no hay return en este punto porque se sale siempre en un return anterior

    ######################################################################
    # GESTION USUARIOS
    ######################################################################


    # AQUI va el metodo alta_usuario
    def alta_usuario(self, dni, nombre, tipo):
        if dni in self._usuarios:
            return False, "Ya existe un usuario con ese dni"
        else:
            self._usuarios[dni]= Usuario(dni, nombre, tipo)
            return True, str(self._usuarios[dni])
            

    # AQUI va el metodo baja_usuario
    def baja_usuario(self, dni):
        if dni not in self._usuarios:
            return False, "No existe un usuario con ese dni"
        elif Usuario.ejemplares_prestados(self._usuarios[dni]) > 0:
            return False, "No se puede dar de baja sin que devuelva lo que tiene prestado"
        else:
            del self._usuarios[dni]
            return True, "Usuario dado de baja correcramente"

    # AQUI va el metodo buscar_usuario_dni
    def buscar_usuario_dni(self, dni):
        if dni not in self._usuarios:
            return False, "No existe un usuario con ese dni"
        else:
            usuario = self._usuarios[dni]
            return True, str(usuario)

    def listar_usuarios(self, nombre, tipo):
        resultado = []
        nombre, tipo = nombre.lower(), tipo.lower()
        for usuario in self._usuarios.values():
            if nombre in usuario.nombre.lower() and tipo in usuario.tipo.lower():
                resultado.append(str(usuario))
        return resultado

    # AQUI va el metodo leer_fichero_usuarios
    def leer_fichero_usuarios(self, filename):
        try:
            with open("usuarios.csv",'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                leidos = 0 # contador con propositos informativos
                next(reader) # nos saltamos la cabecera
                for dni, nombre, tipo  in reader:
                    try:
                        self.alta_usuario(dni, nombre, tipo)
                        leidos += 1
                    except Exception as msg:
                        return False, f"Error al leer fichero de usuarios: {msg}"
                   
                    # FIN COMPLETAR
                return True, f'{leidos} usuarios leidos correctamente'
        except Exception as ex:
            return (False, 'Error al leer fichero de ejemplares. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')


    def guardar_fichero_usuarios(self, filename):
        try:
            with open(filename,'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                # escribimos la cabecera:
                writer.writerow(['DNI','Nombre','Tipo'])
                # y el resto de filas:
                for u in self._usuarios.values():
                    writer.writerow([u.dni, u.nombre, u.tipo])
                return True, f'{len(self._usuarios)} usuarios guardados correctamente'
        except Exception as ex:
            return (False,'Error al guardar fichero de usuarios. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')
        # no hay return en este punto porque se sale siempre en un return anterior

    ######################################################################
    # GESTION PRESTAMOS
    ######################################################################

    # AQUI va el metodo ver_prestamos_usuario
    def ver_prestamos_usuario(self, dni):
        # Comprobarsi el dni esta en los ususarios
        if dni not in self._usuarios:
            return False, 'No existe un usuario con ese dni'
        else:
            # Consigue el objeto usuario
            usuario = self._usuarios[dni]
            # Consigue la lista de prestamos
            prestamos = usuario.prestamos
            return True, prestamos

    def disponibilidad_ejemplar(self, signatura):
        if signatura not in self._ejemplares:
            return False, f'Ejemplar {signatura} no encontrado'
        ejemplar = self._ejemplares[signatura]
        return True, ejemplar.disponibilidad()

    def solicitar_prestamo(self, dni, signatura):
        if dni not in self._usuarios:
            return False, f'Usuario {dni} no encontrado'
        usuario = self._usuarios[dni]
        if signatura not in self._ejemplares:
            return False, f'Ejemplar {signatura} no encontrado'
        ejemplar = self._ejemplares[signatura]
        disponibilidad = ejemplar.disponibilidad()
        if disponibilidad != 'Disponible':
            return False, 'Ejemplar no disponible:\n'+disponibilidad
        ejemplares_prestados = usuario.ejemplares_prestados()
        if ejemplares_prestados >= Prestamo.MAX_EJEMPLARES_POR_USUARIO:
            return False, 'El usuario no puede pedir mas ejemplares en este momento'
        prestamo = Prestamo(usuario, ejemplar)
        # anyadimos el prestamo en la lista del usuario:
        usuario.prestamos.append(prestamo)
        # y nos lo apuntamos tambien en el propio ejemplar:
        ejemplar.prestamo = prestamo
        return True, str(prestamo)

    # AQUI va el metodo devolver_prestamo(self, dni, signatura)
    def devolver_prestamo(self, dni, signatura):
        # Comprobarsi el dni esta en los ususarios
        if dni not in self._usuarios:
            return False, 'Usuario no encontrado'
        # Comprobar si esta la signatura
        if signatura not in self._ejemplares:
            False, 'Ejemplar no encontrado'
        # COnseguir objetos usuario y ejemplar
        usuario = self._usuarios[dni]
        ejemplar = self._ejemplares[signatura]
        prestamo = ejemplar.prestamo
        if prestamo == None or usuario != prestamo.usuario:
            return False, 'Los datos del prestamo son incorrectos'
        resul = f'Eliminado el prestamo: {prestamo}'
        # Eliminar el objeto prestamo
        usuario.prestamos.remove(prestamo)
        ejemplar.prestamo = None
        # Return
        return True, resul

    def leer_fichero_prestamos(self, filename):
        # si el fichero no existe no pasa nada, no hay prestamos
        
            try:
                with open(filename,'r', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile, delimiter=';')
                    leidos = 0
                    next(reader) # nos saltamos la cabecera:
                    # 'DNI','Signatura'
                    for dni,signatura in reader:
                        ok, msg = self.solicitar_prestamo(dni,
                                                          signatura)
                        if ok:
                            leidos += 1
                        else:
                            return (False,'Error al leer fichero de ejemplares '+
                                    f'en signatura {signatura}\n{msg}')
                    return True,f'{leidos} prestamos leidos correctamente'
            except Exception as ex:
                return (False,'Error al leer fichero de ejemplares. Excepcion de tipo '+
                        f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                        f'Directorio actual:{os.getcwd()}')
            # no hay return en este punto porque se sale siempre en un return anterior

    def guardar_fichero_prestamos(self, filename):
        try:
            with open(filename,'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                # escribimos la cabecera:
                writer.writerow(['DNI','Signatura'])
                escritos = 0
                # y el resto de filas:
                for usuario in self._usuarios.values():
                    for i in usuario.prestamos:
                        writer.writerow([usuario.dni, i.ejemplar.signatura])
                        escritos += 1
                return True, f'{escritos} prestamos guardados correctamente'
        except Exception as ex:
            return (False,'Error al guardar fichero de ejemplares. Excepcion de tipo '+
                    f'{type(ex).__name__}\nArgumentos:{ex.args}. \n'+
                    f'Directorio actual:{os.getcwd()}')
        # no hay return en este punto porque se sale siempre en un return anterior

    ######################################################################
    # LECTURA Y ESCRITURA DE TODOS LOS DATOS
    ######################################################################

    def leer_datos_biblioteca(self, directorio):
        resul = ["Datos leidos correctamente:"] # provisionalmente

        filename = os.path.join(directorio, "usuarios.csv")
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg_u = self.leer_fichero_usuarios(filename)
        if not ok:
            return False, f'Error leyendo {filename}:\n'+msg_u
        resul.append(msg_u)

        filename = os.path.join(directorio, "libros.csv")
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg_l = self.leer_fichero_libros(filename)
        if not ok:
            return False, f'Error leyendo {filename}:\n'+msg_l
        resul.append(msg_l)

        filename = os.path.join(directorio, "ejemplares.csv")
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg_e = self.leer_fichero_ejemplares(filename)
        if not ok:
            return False, f'Error leyendo {filename}:\n'+msg_e
        resul.append(msg_e)

        filename = os.path.join(directorio, "prestamos.csv")
        # DESCOMENTAR CUANDO CORRESPONDA:
        ok, msg_p = self.leer_fichero_prestamos(filename)
        if not ok:
            return False, f'Error leyendo {filename}:\n'+msg_p
        resul.append(msg_p)

        return True, "\n".join(resul)

    def guardar_datos_biblioteca(self, directorio):
        filename = os.path.join(directorio, "usuarios.csv")
        ok, msg_u = self.guardar_fichero_usuarios(filename)
        if not ok:
            return False, f'Error guardando {filename}:\n'+msg_u

        filename = os.path.join(directorio, "libros.csv")
        ok, msg_l = self.guardar_fichero_libros(filename)
        if not ok:
            return False, f'Error guardando {filename}:\n'+msg_l

        filename = os.path.join(directorio, "ejemplares.csv")
        ok, msg_e = self.guardar_fichero_ejemplares(filename)
        if not ok:
            return False, f'Error guardando {filename}:\n'+msg_e

        filename = os.path.join(directorio, "prestamos.csv")
        ok, msg_p = self.guardar_fichero_prestamos(filename)
        if not ok:
            return False, f'Error guardando {filename}:\n'+msg_p

        resul = "\n".join(["Datos guardados correctamente:",
                           msg_u, msg_l, msg_e, msg_p])
        return True, resul

