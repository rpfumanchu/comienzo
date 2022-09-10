#Escribir un programa que almacene las asignaturas de un curso
#  (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
#  pregunte al usuario la nota que ha sacado en cada asignatura,
#  y después las muestre por pantalla con el mensaje 
# En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista
#  y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignatura = ["Matematicas","Fisica","Lengua"]
clasificacion = []
for tema in asignatura:
    nota = int(input(f"¿que nota has sacado en:  {tema} ?"))

                  # append nos permite agregar nuevos elementos a una lista
    clasificacion.append (nota)

                # len se usa para hacer un conteo
for i in range(len(asignatura)):
    print(f"En: {asignatura[i]} has sacado: {clasificacion[i]}")
