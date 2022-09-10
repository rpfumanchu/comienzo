#Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, 
# y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

numero = int(input("Introduce u número del 1 al 10: "))
nombre_fichero = f"tabla del {str(numero)} .txt "
try:
    fichero = open(nombre_fichero,"r")
except FileNotFoundError:
    print(f"no existe el fichero con la tabla del {numero}")
else:
    print(fichero.read())
    fichero.close()
