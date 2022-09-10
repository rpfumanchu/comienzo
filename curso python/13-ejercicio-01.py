from operator import truediv


playlist = {} #diccionario vacio
playlist['canciones'] = []  #lista vacia de canciones

#funcion principal
def app():

   #agregar playlist
   agregar_playlist = True

   while agregar_playlist:
       nombre_playlist = input('¿Como deseas llamar la playlist?: \r\n')

       if nombre_playlist:
        playlist['nombre'] = nombre_playlist

#ya tenemos un nombre desactivar el true
       agregar_playlist = False
    

       #mandar llamar la funcion para agregar canciones
       agregar_canciones()

def agregar_canciones():
    #bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #preguntar al usuario que cancion deseea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'agrega canciones para la playlist {nombre_playlist} :  \r\n'
        pregunta += 'escribe "x" para dejar de agregar canciones:  \r\n'

        cancion = input(pregunta)

        if cancion == 'x':
            print('finalizando')
            #dejar de agregar canciones a la playlist
        else:
            #agregar canciones a la playlist
            playlist['canciones'].append(cancion)  #.append para ir aañadiendo elementos

            print(playlist)


app()