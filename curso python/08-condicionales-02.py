#ejemplo con elif
ocupacion = 'jubilado'

if ocupacion == 'estudiante':
    print('tienes 50% de descuento')
elif ocupacion == 'jubilado':
    print('tienes 75% de descuento')
elif ocupacion == 'desempleado':
    print('tienes un 10% de descuento')
else:
    print('debes pagar el 100%')
