#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad = float(input("¿Que cantidad desea invertir"))
interes = float(input("¿A que tipo de inters anual?"))
años = int(input("¿A cuantos años deseas ponerlo?"))
for i in range(años):
    cantidad *= 1 + interes /100
    print(f"capital tras años: {i+1} años : {round(cantidad ,2)}")
    

