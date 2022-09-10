from importlib.machinery import EXTENSION_SUFFIXES
import os
from tempfile import TemporaryFile # os libreria de python

#contactos
class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

SALTO = '\n'
CARPETA = 'contactos/'  #hacemos una variable carpeta de contactos
#en mayusculas para dar a entender que es una constante y no la borren
EXTENSION = '.txt'  #extension de archivos


def app():
     #revisa si la carpeta existe
    crear_directorio()

    #segunda funcion muestra el menu de opciones
    mostrar_menu()

    #preguntar al usuario la accion a realizar

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \n')
        opcion = int(opcion)

        #ejecutar la opcion
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion ==2:
            editar_contacto()
            preguntar = False
        elif opcion ==3:
            mostrar_contactos()
            preguntar = False
        elif opcion ==4:
            buscar_contacto()
            preguntar = False
        elif opcion ==5:
            borrar_contacto()
            preguntar = False
        else:
            print('opcion no valida,intente de nuevo')

def borrar_contacto():
    nombre = input(f'escriba el contacto que desea borrar: {SALTO}')
    
    try:
        #           CARPETA + nombre + EXTENSION
        os.remove(f"{CARPETA}{nombre}{EXTENSION}")           #os.remove   sesa para eliminar
        print(f'{SALTO} : Eliminado correctamente.')
    except IOError:                                # IOEror es lo que se suele poner para dar un error
        print('No existe ese contacto')

    app()

def buscar_contacto():
    nombre = input(f'introduce el contacto que desea buscar: {SALTO}')
    
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print(f'{SALTO} informacion del contacto: {SALTO}')
            for linea in contacto:
                print(linea.rstrip())                                    #usamos try except para hacer una excepcion y si no existe el archivo nos marque un error.

                                                                      #no abusar de try,gasta memoria

                                                                      #esto podria hacerse tambien con un if y else
        print(f'{SALTO}')                                           
    except IOError:
        print('El archivo no existe.')
        print(IOError)
        

    
    app()
    
    
def mostrar_contactos():   #listdir permite listar los archivos de un directorio
    archivos = os.listdir(CARPETA)
                                     #CON ESTO HACEMOS QUE CORRA DE UNA EN UNA LAS LINEAS
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
                    #ITERADOR
    
    for archivo in archivos_txt:
        with open(f'{CARPETA}{archivo}') as contacto:
            for linea in contacto:
                # imprime los cada linea
                # rstrip: borra los espacios en blanco al final de la cadena
                # lstrip: borra los espacios en blanco al principio de la cadena
                # strip: borra los espacios en blanco a ambos lados de la cadena
                # strip("0"): borra los 0s a ambos lados de la cadena
                print(linea.rstrip())
            print('\n')
    app()

def editar_contacto():
    print('Escribe el contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\n')

    #revisar si el archivo ya existe antes de editar
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #resto de campos
            nombre_contacto = input('Agrega nuevo nombre:\n')
            telefono_contacto = input('Agregar el nuevo teléfono:\n')
            categoria_contacto = input('Agrega nueva categoria:\n')

            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            #escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\n')
            archivo.write('Telefono:' + contacto.telefono + '\n')
            archivo.write('Categoria:' + contacto.categoria + '\n') 

            #renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION,CARPETA + nombre_contacto + EXTENSION)

             #monstrar mensaje de exito
        print('Contacto editado correctamente\n')
    else:
        print('ese contacto no existe')

        #reiniciar la app
    app()

def agregar_contacto():

    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('nombre del contacto:\n')

    #revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
                     #isfile revisa si el archivo existe previamente
                     #     
    if not existe:

        with open(CARPETA + nombre_contacto +EXTENSION, 'w') as archivo:

            #resto de los campos
            
            telefono_contacto = input('Agregar el teléfono:\n')
            categoria_contacto = input('Categoria contacto:\n')

            #instanciar la clase
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
        
            #escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\n')
            archivo.write('Telefono:' + contacto.telefono + '\n')
            archivo.write('Categoria:' + contacto.categoria + '\n')

            #mostrar mensaje de exito
            print('Contacto creado con exito.\n')
    else:
        print('Ese contacto ya existe.')
    #reiniciar la app
    app()    
def mostrar_menu():
    print('Seleccione del menu lo que desea hacer.')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):   #para ver si una carpeta existe y si no la crea
        os.makedirs(CARPETA)
         #crear la carpeta
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre +EXTENSION)

app()