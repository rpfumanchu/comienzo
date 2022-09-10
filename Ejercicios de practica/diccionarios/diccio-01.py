#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.


             # damos llave y valor
monedas = {"euro":"E", "dollar": "S", "yen":"Y"}
moneda = input("Escribe el tipo de moneda:  ")
    # get () devuelve el valor de la clave especificada, si el valor no está en el diccionario o un valor predeterminado.

print(monedas.get (moneda ,"la moneda no esta disponoble"))


     # otra manera


# monedas = {"Euro":"E", "Dollar": "S", "Yen":"Y"}
# moneda = input("Escribe el tipo de moneda:  ")
# if moneda.title() in monedas:
#     print(monedas[moneda.title()])
# else:
#     print("la moneda no esta")