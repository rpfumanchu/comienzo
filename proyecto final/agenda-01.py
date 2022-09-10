from importlib.machinery import EXTENSION_SUFFIXES
import os # os libreria de python

#contactos
class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


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
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #ejecutar la opcion
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion ==2:
            editar_contacto()
            preguntar = False
        elif opcion ==3:
            print('Ver contacto')
            preguntar = False
        elif opcion ==4:
            print('Buscar contacto')
            preguntar = False
        elif opcion ==5:
            print('Eliminar contacto')
            preguntar = False
        else:
            print('opcion no valida,intente de nuevo')

def editar_contacto():
    print('Escribe el contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n')

    #revisar si el archivo ya existe antes de editar
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #resto de campos
            nombre_contacto = input('Agrega nuevo nombre:\r\n')
            telefono_contacto = input('Agregar el nuevo teléfono:\r\n')
            categoria_contacto = input('Agrega nueva categoria:\r\n')

            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            #escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n')
            archivo.write('Telefono:' + contacto.telefono + '\r\n')
            archivo.write('Categoria:' + contacto.categoria + '\r\n') 

            #renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION,CARPETA + nombre_contacto + EXTENSION)

             #monstrar mensaje de exito
        print('Contacto editado correctamente\r\n')
    else:
        print('ese contacto no existe')

        #reiniciar la app
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('nombre del contacto:\r\n')

    #revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
                     #isfile revisa si el archivo existe previamente
            
    if not existe:

        with open(CARPETA + nombre_contacto +EXTENSION, 'w') as archivo:

            #resto de los campos
            
            telefono_contacto = input('Agregar el teléfono:\r\n')
            categoria_contacto = input('Categoria contacto:\r\n')

            #instanciar la clase
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
        
            #escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n')
            archivo.write('Telefono:' + contacto.telefono + '\r\n')
            archivo.write('Categoria:' + contacto.categoria + '\r\n')

            #mostrar mensaje de exito
            print('Contacto creado con exito.\r\n')
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