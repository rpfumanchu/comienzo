#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
#  Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


nombre = input("¿Como te llamas? \n")
genero = input("¿Cual es tu genero? \n")
if genero == "M":
    if nombre < "M":
        group = "A"
    else:
        group = "B"
else:
    if nombre >"N":
        group = "A"
    else:
        group = "B"
print("Tu grupo es :" +group)
