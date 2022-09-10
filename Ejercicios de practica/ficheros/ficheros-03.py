#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y 
# muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

    
numero1 = int(input("Introduce un número del 1 al 10: "))
numero2 = int(input("Introduce un número del 1 al 10: "))
nombre_fichero = (f"tabla del {str(numero1)} .txt ")

try:
    with open(nombre_fichero, "r") as fichero:
        
                    '''Para leer ():
                    1. Lea todo el archivo y coloque el contenido del archivo en una variable de cadena
                    2. Si el archivo es más grande que la memoria disponible, este procesamiento no se puede utilizar
                    Para readline ():
                    1. readline () lee una línea a la vez, lo cual es mucho más lento que readlines ()
                    2, readline () devuelve unCuerdaObjeto y guarde el contenido de la línea actual
                    Para readlines ():
                    1. Lea todo el archivo a la vez y devuelva un archivo que contenga todas las líneas.Lista。
                    2. No es adecuado para usar cuando el tamaño del archivo es mayor que la memoria disponible.'''


    linea = fichero.readlines()
    print(linea[numero2 - 1])
except FileNotFoundError:
    print(f"No existe el fichero con la tabla del {numero1}")


