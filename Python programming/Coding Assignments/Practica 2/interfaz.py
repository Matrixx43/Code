


"""
Este modulo exporta las siguientes funciones:

pedir_campos(campos,titulo="",permite_vacios=False):
notificar(msg,titulo="",ok=False,esperar=True):
listar(lista,titulo="",esperar=True):
menu(title,options,clear_screen=True):
seleccionar_fichero(msg, save_mode=False):

"""

import os

def pedir_campos(campos,titulo="", permite_vacios=False):
    if titulo!='':
        print("\n--- "+titulo+" ---")
    resul = []
    for campo in campos:
        respuesta =input(campo+": ")
        while respuesta=="" and permite_vacios==False:
            respuesta =input(campo+": ")
        resul.append(respuesta)
    return tuple(resul)

def pedir_campo(campo,titulo='',permite_vacio=False):
    return pedir_campos([campo],titulo=titulo,
                        permite_vacios=permite_vacio)[0]

def notificar(msg,titulo="",ok=False,esperar=True):
    if titulo!='':
        print("\n--- "+titulo+" ---")
    print(msg)
    if esperar:
        input("Pulse enter para continuar")

def listar(lista,titulo="",esperar=True):
    if titulo!='':
        print("\n--- "+titulo+" ---")
    for item in lista:
        print(item)
    if esperar:
        input("Pulse enter para continuar")

def menu(titulo, options, clear_screen=True):
    while True:
        if clear_screen:
            os.system("cls" if os.name=="nt" else "clear")
        if len(titulo)>0:
            print(titulo)
            print("-"*len(titulo))
        for i,(descr,value) in enumerate(options):
            print(f" {i+1:>2}) {descr}")
        op = 0
        try:
            op = int(input("Opcion: "))
        except ValueError as err:
            op = 0
        if 0<op<=len(options):
            return options[op-1][1]
        print("Debes introducir una opcion correcta")
        if clear_screen:
            input("Pulsa enter para continuar")
    
def seleccionar_fichero(msg, es_directorio=False, save_mode=False):
    return pedir_campo(msg)

