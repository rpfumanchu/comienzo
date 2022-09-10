#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

SALTO = "\n"

nombre = input(f"cual es tu nombre: {SALTO} ")
print(f"Hola bienbenido:  {nombre.title()}")

edad = int(input(f"cual es tu edad {SALTO}"))
if edad <18:
    print("todavia eres menor: ")
else:
    print(f"Eres mayor de edad {nombre.title()}")
