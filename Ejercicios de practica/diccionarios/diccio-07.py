#Escribir un programa que cree un diccionario simulando una cesta de la compra.
#  El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste


cesta = {}
continuar = True
while continuar:
    articulo = input("¿Que articulo has comprado? ")
    precio = float(input(f"¿Cuanto te ha costado {articulo} : "))
    cesta[articulo] = precio
    continuar = input(f"¿Quieres seguir comprando ( s/n )") == "s"
coste = 0
print("lista de la compra")
for articulo,precio in cesta.items():
    print(f"{articulo} \t {precio}")
    coste += precio
print(f"El coste total es: {coste}")


