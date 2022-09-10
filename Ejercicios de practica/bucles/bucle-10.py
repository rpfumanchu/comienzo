#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# numero =int(input("Escribe un número entero mayor que 2: "))
# for i in range(2,numero):
#     if (numero % i) == 0:
#         break
# if (i + 1) == numero:
#     print("el numero  es primo")
# else:
#     print("el número no es primo")




    #otra forma de hacerlo

numero =int(input("Escribe un número entero mayor que 2: "))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(f"{numero} es primo.")
else: 
    print(f"{numero} no es primo")
