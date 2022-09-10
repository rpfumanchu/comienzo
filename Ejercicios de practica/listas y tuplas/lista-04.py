#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
numeros_ganadores =[]
for i in range(6):
    numeros_ganadores.append(int(input("introduce un numero ganador")))

                  #  .sort para ordenar de menor a mayor dentro de una lista
numeros_ganadores.sort()
print(f"los numeros ganadores son: {numeros_ganadores}")
