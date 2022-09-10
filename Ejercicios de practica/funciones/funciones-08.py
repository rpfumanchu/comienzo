#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

import numpy as np

def media (n):
    lista = []
    for i in n:
        lista.append(int(i))
    return lista



def estadistica(n):
    diccio = {}
    diccio["media"] = np.mean(media(n))
    diccio["varianza"] = np.var(media(n))
    diccio["desviacion"] = np.std(media(n))
    return diccio
print(estadistica([1,2,3,4,5]))