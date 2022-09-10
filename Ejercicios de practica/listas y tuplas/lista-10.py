#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
numeros = [[50,75,46,22,80,65,8]]
for numero in numeros:
    minimo = min(numero)
    maximo = max(numero)
    print(f"El número minimo es: {minimo} y el numero maximo es: {maximo}")


                        # en ambos casos usamos min y max respectivamente para saber cual el el número minimo y maximo

                        #otra forma

numeros = [50,75,46,22,80,65,8]
min = max =numeros[0]
for numero in numeros:
    if numero < min:
        min = numero
    elif numero > max:
        max = numero
print(f"el número minimo es: {min} y el número maximo es: {max}")