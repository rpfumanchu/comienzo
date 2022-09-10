#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

while True:

    try:
        x = float(input("Introduce numero: "))

        raise IOError("He roto porque me da la gana")

        a = 5/x
        print(a)
    except SyntaxError:
        print("Error de sintaxis")
    except ZeroDivisionError:
        print("No se puede dividir por 0")


    
    print("Hola buenas vamos a hacer una división \n")
    print("********************")
    numero_1 = float(input("Introduce un número: \n"))
    numero_2 =float(input("Introducca el numero por el que quiera dividir: \n"))
    if numero_2 == 0:
        print("todo numero dividido por 0 es igual a 0 ")
    else:
        print(numero_1 / numero_2)