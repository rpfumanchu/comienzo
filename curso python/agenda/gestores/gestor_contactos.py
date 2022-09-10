#import os # os libreria de python
from os import rename, path
from ..clases.Contacto import Contacto

#en mayusculas para dar a entender que es una constante y no la borren
SALTO_LINEA = '\n'
CARPETA = 'contactos/'  #hacemos una variable carpeta de contactos
EXTENSION = '.txt'  #extension de archivos

def agregar_contacto():

    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input(f'nombre del contacto: {SALTO_LINEA}')

    #revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(f'{CARPETA}{nombre_contacto}{EXTENSION}', 'w') as archivo:

            #instanciar la clase
            contacto = Contacto(nombre_contacto)

            #resto de los campos
            contacto.request_extra_data()
        
            #escribir en el archivo
            contacto.write_to_file(archivo)

            #mostrar mensaje de exito
            print(f'Contacto creado con exito.{SALTO_LINEA}')
    else:
        print('Ese contacto ya existe.')

def editar_contacto():

    print('Escribe el contacto a editar')
    nombre_anterior = input(f'Nombre del contacto que desea editar: {SALTO_LINEA}')

    #revisar si el archivo ya existe antes de editar
    existe = existe_contacto(nombre_anterior)
    if existe:
        
        with open(f'{CARPETA}{nombre_anterior}{EXTENSION}', 'w') as archivo:

            #pedir nombre contacto
            nombre_contacto = input(f'Agrega nuevo nombre: {SALTO_LINEA}')

            #instanciar
            contacto = Contacto(nombre_contacto)

            #resto de campos
            contacto.request_extra_data()
            
            #escribir en el archivo
            contacto.write_to_file(archivo)

            #renombrar el archivo
            rename(f'{CARPETA}{nombre_anterior}{EXTENSION}', f'{CARPETA}{nombre_contacto}{EXTENSION}')

    else:
        print('ese contacto no existe')

def existe_contacto(nombre):
    #isfile revisa si el archivo existe previamente
    return path.isfile(f'{CARPETA}{nombre}{EXTENSION}')