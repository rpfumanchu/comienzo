#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

catalogo = {"platano":1.35, "manzana":0.80, "pera":0.85, "naranja":0.70}
fruta = input("¿Que fruta deseas llevarte? ")
kilos = float(input("¿Cuantos kilos quieres llevarte?"))
if fruta in catalogo:
    print(f"{kilos} kilos de {fruta} valen {catalogo[fruta]*kilos} euros")
else:
    print(f"lo siento la fruta {fruta} no esta disponible")
