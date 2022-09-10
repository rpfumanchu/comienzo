#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

#     cantdad %  * años = beneficio

cantidad = float(input("Que cantidad deseas invertir:"))
interes = float(input("A que tipo de interes vas a realizar la inversion:"))
años = float(input("Cuantos años va a durar la inversion:"))
beneficio = (((cantidad) * (interes) / 100) * (años),)
print("El beneficio que has obtenido es:"+str(beneficio) , "Euros")
