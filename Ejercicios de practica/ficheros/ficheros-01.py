#Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
# fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.


numero = int(input("Introduce u número del 1 al 10: "))
nombre_fichero = f"tabla del {str(numero)} .txt "
fichero = open(nombre_fichero, "w")
for i in range(1,11):
    fichero.write(f"{str(numero)} x {str(i)} =  {str(numero * i)}\n") 
fichero.close()



'''otra forma'''


numero = int(input("Introduce un número del 1, 10: "))
nombre_fichero = f"tabla del {str(numero)}  .txt "
with open(nombre_fichero, "w") as fichero :
    for i in range(1,11):
        fichero.write(f"{str(numero)} x {str(i)} = {str(numero*i)}\n")