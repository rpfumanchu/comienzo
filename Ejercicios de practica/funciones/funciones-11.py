#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def contar_palabras (texto):
    texto = texto.split()
    palabra = {}
    for i in texto:
        if i in palabra:
            palabra[i] += 1
        else:
            palabra[i] = 1
    return palabra


def palabras_repetidas (palabra):
    lista_palabra = ""
    maxima_freq = 0
    for palabra, freq in palabra.items():
        if freq > maxima_freq:
            lista_palabra = palabra
            maxima_freq = freq
    return lista_palabra, maxima_freq

texto = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"
print(contar_palabras(texto))
print(palabras_repetidas(contar_palabras(texto)))
