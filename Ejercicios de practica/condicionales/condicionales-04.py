# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

print("Hola buenas.¿Quieres saber si un numero es par o impar? ")
numero = int(input("Escribe un numero: \n"))

# % 2 == 0  (se usa para calcular el resto y si es cero entonces es par)
if numero % 2 == 0:
    print("Este número es par")
else:
    print("Este numero es impar")
