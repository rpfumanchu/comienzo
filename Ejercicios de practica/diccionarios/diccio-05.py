#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un 
# curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso,
#  y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

curso = {"Matmáticas":6, "Física":4, "Qquímica":5}
credito_total = 0
for asignatura,credito in curso.items():
    print(f"{asignatura} tiene {credito}")
    credito_total += credito
print(f"El número total de creditos del curso es: {credito_total}")