#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y
#  muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
#  el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

# format se usa para ordenar el contenido de la variablle dentro de una cadena de texto


producto = input("Escribe el nombre del producto:  ")
precio =float(input ("Escribe el precio unitario del producto:  "))
unidades = int(input ("Introduce el numero de unidades"))
print("{producto}: {unidades:3d} unidades x {precio:9.2f} euros ={total:11.2f} euros" .format(producto = producto , unidades = unidades, precio = precio, total = unidades * precio))
print(f"{producto}: {unidades:3d} unidades x {precio:9.2f} euros ={unidades * precio:11.2f} euros")

                     #no lo entiendo         #no lo entiendo       tampoco        



                     