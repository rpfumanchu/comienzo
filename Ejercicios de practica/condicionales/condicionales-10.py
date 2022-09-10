#\ t: Representa un espacio en blanco de 4 caracteres, similar a la función de sangría en el documento, que es equivalente a presionar una tecla Tab.
# \ n: significa salto de línea, equivalente a presionar una tecla enter
# \ n \ t: Significa que 4 caracteres están en blanco mientras se envuelve.



#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


print("Hola bienvenido a pizzeria Bella Napoli\n")
print("tenemos dos tipos de pizza:\n tipo 1 Vegetariana  \n tipo 2 no vegetariana")
tipo = int(input("Elije el tipo de pizza que quieres: "))
if tipo == 1:
    print("Los ingredientes de las pizzas vegetarianas son:\n\t - 1 Pimiento\n\t - 2 Tofu\n\t")
    ingrediente = input("Selecciona un ingrediente: ")
    print("Pizza vegetariana con Tomate,mozzarella y " ,end ="")
    if ingrediente == "1":
        print("Pimiento")
    else:
        print("Tofu")
else:
    print("ingredientes de pizzas no vegenarianas son:\n\t - 1 peperoni\n\t - 2 jamón\n\t - 3 Salmón\n\t")
    ingrediente = input("Selecciona un ingrediente: ")
    print("Pizza no vegetariana con Tomate,mozzarella y " ,end ="")
    if ingrediente == "1":
        print("Peperoni")
    elif ingrediente == "2":
            print("Jamón")
    else:
        print("Salmón")
