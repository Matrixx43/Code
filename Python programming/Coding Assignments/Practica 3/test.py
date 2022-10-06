diccionarios = [
{ 'casa ':10 , 'coche ':15 , 'manzana ':20 } ,
{ 'silla ':7 , 'casa ':2 , 'coche ':3 , 'naranja ':7 } ,
{ 'casa ':10 , 'manzana ':2 , 'naranja ':4 }
]

for i in range(3):
    suma = 0
    for key, value in diccionarios[i].items():
        suma += value
    print(f"Los valores del diccionario {i} suman: {suma}")

d = {}
for diccionario in diccionarios:
    for key, value in diccionario.items():
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]
print(d)

def agrupa(lista):
    solucion = {}
    for diccionario in lista:
        for key in diccionario.keys():
            if key in solucion:
                solucion[key].append(diccionario[key])
            else:
                solucion[key] = [diccionario[key]]
    return solucion

print(agrupa(diccionarios))