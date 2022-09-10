#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


# asignaturas = ["matematicas","Física","Literatura"]
# notas = []

# for asignatura in asignaturas:
#     nota = float(input(f"¿Que nota has sacado en  {asignatura} ?"))
#     if nota >= 5:
#         notas.append (asignatura)

# for asignatura in notas:
                  # .remove se usa para eliminar por nombre
#     asignaturas.remove(asignatura)
# print(f"Tienes que repetir: {asignaturas}")



                                # otra forma


asignaturas = ["matematicas","Física","Literatura"]

             #inicio = len(s)-1
             #fin = -1
             #paso = -1
for i in range(len(asignaturas)-1, -1, -1):
    nota = float(input(f"¿Que nota has sacado en : {asignaturas[i]} ? "))
    if nota >= 5:

                # .pop se usa para eliminar
     asignaturas.pop (i)
print(f"tienes que repetir: {asignaturas}")




    