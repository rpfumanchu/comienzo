

nombre = input('¿como te llamas?: \r\n')



if nombre == 'Jesus':
    print('sabia que dirias eso')
elif nombre == 'Leti':
    print('ers mi hermana no necesito calcular tu edad')
else:
    print('no me suenas')


año = int(input('por favor indica en que año naciste: \r\n'))



if año >= 2023:
    print('todavia no has nacido,no hago viajes en el tiempo')
else:
    print('voy a calcular tu edad')

 

año_actual = int(input('indica el año actual: \r\n'))

edad = año_actual - año
print(f'tienes: {edad} años actualmente.')   
