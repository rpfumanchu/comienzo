#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.




                       #opcion 1

# numeros = [1,2,3,4,5,6,7,8,9,10]
# for i in range(1, 11):
#     print(numeros[-i] , end= ",")




                        #opcion 2




numeros = [1,2,3,4,5,6,7,8,9,10]
         # se usa reverse para que te de el valor invertido de la lista
numeros.reverse()
for numero in numeros:
    print(numero, end= ",")