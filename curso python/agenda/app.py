#import os # os libreria de python
from os import path, makedirs


#en mayusculas para dar a entender que es una constante y no la borren
SALTO_LINEA = '\n'
CARPETA = 'contactos/'  #hacemos una variable carpeta de contactos
EXTENSION = '.txt'  #extension de archivos

def app():

    #revisa si la carpeta existe
    crear_directorio()

    close_menu = False

    while not close_menu:

        #segunda funcion muestra el menu de opciones
        mostrar_menu()

        #preguntar al usuario la accion a realizar
        opcion = input(f'Seleccione una opción: {SALTO_LINEA}')
        opcion = int(opcion)

        #ejecutar la opcion
        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            editar_contacto()
        elif opcion == 3:
            print('Ver contacto')
        elif opcion == 4:
            print('Buscar contacto')
        elif opcion == 5:
            print('Eliminar contacto')
        elif opcion == 0:
            close_menu = True
            print('Hasta luego !!!')
        else:
            print('opcion no valida, intente de nuevo')

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer.')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')
    print('0) Para cerrar el menu')

def crear_directorio():
    """crear_directorio()

    Esta funcion sirve para crear un directorio a través de la constante CARPETA, SOLO si no existe

    """
    if not path.exists(CARPETA):   #para ver si una carpeta existe y si no la crea
        #crear la carpeta
        makedirs(CARPETA)
         


# launch app
app()