# La libreria statistics se puede usar para realizar calculos estadísticos y es propia de python.
# mean: media
# stdev: desviacion
# Fuente: https://docs.python.org/3/library/statistics.html
from statistics import mean, stdev
from typing import Iterable

##################################################################################################################################################################

# Generamos una funcion para no repetir código
def calcular_media_desviacion_y_mostrar(numeros: Iterable[int]):

    # Calcula la media, la funcion mean te pide un iterable de números para funcionar. Si le hubiesemos pasado "valores" directamente, rompe diciendo que son strings no números
    media = mean(numeros)

    # Calcula la desviación, la funcion stdev te pide un iterable de números para funcionar. Si le hubiesemos pasado "valores" directamente, rompe diciendo que son strings no números
    desviacion = stdev(numeros)

    # Mostramos los datos por pantalla
    print(f"La media es {media} y la desviacion {desviacion}")


##################################################################################################################################################################

## Ejercicio : Pidiendo todos los valores por pantalla

# Pido los valores separados por comas
user_input = input("Introduce los números que quieras calcular separados por comas: ")

# Separo los valores por comas para tener un array de valores de tipo texto (str)
valores = user_input.split(",")

# Creo un nuevo array de números recorriendo el array "valores" -> for x in valores, y guardando el resultado como entero int(x). A esta forma de realizar este proceso se llama: list comprehensions.
# aunque parezca dificil de ver, es bastante explicito, lo que viene a decir es...
# por cada "valor" del array "valores", transformalo en un entero "int(valor)" y cuando hayas terminado, guardalo en un array por eso lo rodea con "[ ]".
# Impacta verlo asi de primeras, pero es una forma muy elegante y por lo que he podido ver en stackoverflow, la gente lo usa.
# Fuente: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
numeros = [int(valor) for valor in valores]

calcular_media_desviacion_y_mostrar(numeros)

##################################################################################################################################################################

## Variación 1 : Pidiendo valores uno a uno por pantalla y cuando pone 'listo', lo calcula

numeros = []
is_listo = False
while not is_listo:
    user_input = input("Introduce un número para acumular y realizar el cálculo. Cuando no quieras meter mas números, escribe 'listo': ")
    if user_input == 'listo':
        is_listo = True
    else:
        numeros.append(int(user_input))

calcular_media_desviacion_y_mostrar(numeros)


