pregunta = 'di un numero y te dire si es par o impar :\r\n'
pregunta += '(escribe "cerrar" para salir de la app):\r\n'

preguntar = True

while preguntar:
  
#mezclar con operadores

   numero = input(pregunta)

   if numero == 'cerrar':
    preguntar = False
   else:
    numero = int(numero)


    if numero % 2 == 0:
        print(f'el numero {numero} es par')
    else:
        print(f'el numero {numero} es impar')
