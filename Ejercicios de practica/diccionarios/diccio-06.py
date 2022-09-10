#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
#  sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

persona ={}
continuar = True
while continuar:
    dato = input("¿Que dato deseas introducir? ")
    informacion = input(f"{dato} :")
    persona[dato] = informacion
    print(persona)
    continuar = input("¿Quieres añadir más información ( s/n ) ") =="s"