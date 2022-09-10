#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

numero = int(input("introduce un número entero positivo"))
for i in range(numero):
    print("*"*(i+1))
