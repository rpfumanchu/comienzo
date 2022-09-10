#revisar si un valor es mayor a
from operator import truediv


balance = 500
if balance > 0:
    print('puedes pagar')
    
#otra condicion
else:
    print('no tienes saldo')

#likes
likes = 200 
if likes >= 200:
    print('Excelente, 200 Likes')

# if con texto
lenguaje = 'python'
if lenguaje == 'python': #se pone if not si es para otra decision
    print('buena eleccion')

#evaluar un boolean
usuario_valido = True

if usuario_valido :
    print('aceso confirmado')
else:
    print('debes registrarte')
#evaluar un elemento de una lista
lenguajes = ['python','kotlin','java','javaScript','ruby','go']
if 'php' in lenguajes:
    print('php si existe')
else:
    print('no no esta en la lista')

#if anidados

usuario_valido = True
usuario_admin = False

if usuario_valido :
    if usuario_admin:
        print('acceso total')
    else:
        print('debes iniciar sesion')
else:
    print('debes registrarte')