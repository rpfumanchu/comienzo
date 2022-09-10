#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Escribe una palabra: ")
palabra_alreves = palabra
palabra = list(palabra)
palabra_alreves = list(palabra_alreves)
palabra_alreves.reverse()
if palabra == palabra_alreves:
    print("es un palindromo")
else:
    print("no es un palindromo")