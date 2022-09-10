#Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés 
# separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario
#  para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.


traductor = {}
palabras = input("Eintroduce la lista de palabras y traducciones en formato ... palabra:traduccion separadas por comas: ")
for i in palabras.split(","):
    clave,valor = i.split(":")
    traductor[clave] = valor
frase = input("introduve una frase en español: ")
for i in frase.split():
    if i in traductor:
        print(traductor[i] , end=" ")
    else:
        print(i,end=" ")
