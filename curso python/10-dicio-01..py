10
5
10
5
#creando un diccionario simple
cancion = {
    'artista': 'metallica', #llave y valor
    'cancion' : 'enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}
#acceder a los elemntos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

#mezclar con un stringns
artista = cancion['artista']
print(f'estoy escuchando a {artista}')

print(cancion)

#agregar nuevos valores
cancion['playlist'] = 'heavy metal'
print(cancion)

#remplazar valor existente
cancion['cancion'] = 'seek & destroy'
print(cancion)

#eliminar u valor
del cancion['lanzamiento']
print(cancion)