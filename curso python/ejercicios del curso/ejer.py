# de la libreria datetime importamos el objeto date
from datetime import date

# guardamos el año actual al principio. El año lo obtenemos del objeto date que está importado al principio del fichero
today_year = date.today().year

# creamos un listado de nombres
names = [
    "Jesus",
    "Leticia",
    "Rober",
    "Alina"
]

# y otro listado para nombres en minuscula
lowered_names = []

# pedimos el nombre por input
input_name = input(f'¿como te llamas?:\r\n')

# pasamos el nombre recibido a minuscula para asi validarlo con los demas
input_name = input_name.lower()

# rellenamos lowered_names con los nombres en minuscula, esto hay mchas maneras de hacerlo y esta es la menos... efectiva, pero funciona
for name in names:
    lowered_names.append(name.lower())

# buscamos el nombre en el listado de nombres o en el de minusculas, a ver si lo encontramos
if input_name in names or input_name in lowered_names:
    print(f"Bienvenido de nuevo, {input_name}.")
else:
    print(f'Mmm... no me suenas {input_name}... Pero eso no es problema!')
    # si no lo encontramos, comparamos lo que ha metido el usuario con Robby o Jezu en minusculas
    if input_name == "Robby".lower() or input_name == "Jezu".lower():
        print(f"Te reconozco {input_name} porque me han programado para ello. Bienvenido !")

# preparamos una variable para que, mientras no tenga un valor distinto de None, no salga del bucle while
input_year = None
while input_year == None:
    input_raw_year = input('¿me puedes decir tu año de nacimiento?:\r\n')

    # si el valor metido no es numerico, no lo damos por bueno
    if not input_raw_year.isnumeric():
        print("Cabrit@, meteme un año real.")
    else:
        # si es numerico, entonces lo pasamos a entero y lo guardamos en la variable que controla el bucle
        input_year = int(input_raw_year)

# si el valor añadido es mayor que el año actual
if input_year >= today_year:
    print('todavia no has nacido, no hago viajes en el tiempo.')
else:
    print('voy a calcular tu edad...') 

#año_actual = int(input('indica el año actual: \r\n'))

# por ultimo calculas la edad con la resta
edad = today_year - input_year
print(f'{input_name} tienes: {edad} años actualmente.')   
