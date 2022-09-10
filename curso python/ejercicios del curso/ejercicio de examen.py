numero = 0
respuesta = input('cual es el pico mas alto del mundo :\r\n')
if respuesta == 'everest':
    print('correcto acertaste')
    print('enhorabuena has conseguido 1 punto')
    #incremento por dos
    numero += 1
    print(f'tienes {numero}')
else:
    print('lo siento estuidia un poco mas')

respuesta = input('quien escribio el quijote :\r\n')
if respuesta == 'cervantes':
    print('correcto acertaste')
    print('enhorabuena has conseguido 1 punto')
    numero += 1
    print(f'tienes {numero} puntos')
else:
    print('no seas ignorante')

respuesta = input('cuando se descubrio america :\r\n')
if respuesta == '1492':
    print('correcto acertaste')
    print('enhorabuena has conseguido 1 punto')
    numero += 1
    print(f'tienes {numero} puntos')
else:
    print('menudo cateto')