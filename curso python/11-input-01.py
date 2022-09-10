nombre = input('cual es tu nombre') #: \r\n voy a producir un salto de linea para que no quede tan junto

print(f'hola {nombre}')

#como leer datos que seran numeros
edad = input('cual es tu edad')
#convertir edad strings a entero se usa int
edad = int(edad)

if edad >= 18:
    print('puedes votar')
else:
    print('todavia eres un pipiolo')

    #mezclar con operadores
numero = input('di un numero y te dire si es par o impar :\r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'el numero {numero} es par')
else:
    print(f'el numero {numero} es impar')
