#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


while True:
    frase = input("Escribe lo que quieras:  ")
    if frase == "salir":
        break
    print(frase)