# -*- coding: utf-8 -*-

######################################################################
# Poned/pon aquÃ­ vuestros/tu nombre/s y apellidos:
#
######################################################################

from ipaddress import summarize_address_range
import pathlib

# actividad 1
def explorar(fs_node):
    if not fs_node.is_dir(): # Si es un fichero
        print(fs_node) # Muestra nombre del fichero
    else: # Si es un directorio
        print(fs_node) # Muestra nombre del directorio
        for entry in fs_node.iterdir():
            explorar(entry)


# actividad 2
def contar_lineas(fs_node, word):
    """
    'fs_node' es un objeto creado con pathlib de tipo fichero.
    Esta funciÃ³n asume que 'word' es una palabra EN MINÃšSCULA.
    Debe contar y devolver el nÃºmero de lÃ­neas del fichero
    'fs_node' que contiene la palabra 'word'
    """
    cont = 0 # Contador de lineas
    palabra = word.lower() # Reducir la palabra a minusculas
    with fs_node.open() as f: # Abrir el fichero
        for line in f: # Iterar las lineas
            line = line.lower().split() # Pasar todo a minuscula y separar en palabras
            if palabra in line:
                cont += 1
    return cont


# actividad 3
def explorar_contar(fs_node, word):
    """
    'fs_node' es un objeto creado con pathlib de tipo directorio.
    Asume que 'word' es una palabra EN MINÃšSCULA
    """
    if not fs_node.is_dir(): # Si es un fichero
        num_lineas = contar_lineas(fs_node, word)
        print(f'{num_lineas:4d}', fs_node)
 # Muestra nombre del fichero y el numero de lineas
        return num_lineas # Devuelve el numero de lineas del fichero
    else: # Si es un directorio
        suma_lineas = 0
        for entry in fs_node.iterdir():
            #print(type(explorar_contar(entry, word)))
            suma_lineas += explorar_contar(entry, word)
        print(f'{suma_lineas:4d}', fs_node) # Muestra nombre del directorio y el numero de lineas totales
        return suma_lineas

# programa principal (no cambiÃ©is nada en esta parte)
def main():
    opcion = ""
    while opcion not in ('1','2','3'):
        opcion = input('Elige actividad:\n 1) Recorrido recursivo\n'+
                       ' 2) Contar lineas\n 3) Recorrido recursivo '+
                       'contando lineas\nOpcion: ')
        if opcion not in ('1','2','3'):
            print('Opcion incorrecta')

    ruta = input("Nombre del fichero o carpeta (enter para 'GCD'): ")
    if ruta == '':
        ruta = 'GCD'
    fs_node = pathlib.Path(ruta)
    
    if not fs_node.exists():
        print(f"Error: no se encuentra el fichero o carpeta '{fs_node}'")
        return
    
    elif opcion == '1':
        if not fs_node.is_dir():
            print(f"Error: {fs_node} no es un directorio")
            return
        explorar(fs_node)
    else:
        word = input('Palabra a buscar: ').lower()
        if opcion == '2':
            if not fs_node.is_file():
                print(f"Error: {fs_node} no es un fichero")
                return
            cuenta = contar_lineas(fs_node, word)
            print(f'Hay {cuenta} lineas con la palabra {word}')
        else:
            explorar_contar(fs_node, word)

if __name__ == '__main__':
    main()

#fs_node = pathlib.Path("GCD")
#explorar("GCD")

