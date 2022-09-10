#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input("Escribe una palabra: ")
vocales = ["a","e","i","o","u"]
for vocal in vocales:
    repetir = 0
    for letra in palabra:
        if letra == vocal:
            repetir +=1
    print(f"la vocal: {vocal} aparece: {repetir} veces ")