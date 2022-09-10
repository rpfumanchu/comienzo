#iniciar un diccionario vacio
jugador ={}
print(jugador)

#se une un jugador
jugador['nombre'] = 'Roberto'
jugador['puntos'] = 0
print(jugador)
#incrementando puntos
jugador['puntos'] = 100
print(jugador)

#incrementando puntos
jugador['puntos'] = 200
print(jugador)

#acceder a un valor
print(jugador.get('consola','no existe ese valor'))

#iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)


#eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntos']
print(jugador)