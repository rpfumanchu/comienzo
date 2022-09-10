from mailbox import NoSuchMailboxError


lenguajes = ['python','kotlin','java','javaScript']

print(lenguajes)

# Los arrays (list) comienzan en la posicion 0
print(lenguajes[0]) # Python

#ordenar los elementos
lenguajes.sort() #.sort para ordenar alfabeticamente
print(lenguajes)

#Acceder a un elemento dentro de un texto
# utilizas f para mezclar un strings con una variable
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificando valores de un arreglo (list)
lenguajes[2] = 'php'
print(lenguajes)

#agregar elementos a un arreglo se usa append.
lenguajes.append('ruby')
print(lenguajes)

#eliminar de un arreglo (list) se usa del
del lenguajes [1]
print(lenguajes)

#otro metodo de eliminar
lenguajes.pop() #elimina el ultimo elemento
print(lenguajes)

#eliminar con pop una posicion especifica
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre se usa remove
lenguajes.remove('php')
print(lenguajes)