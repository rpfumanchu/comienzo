#Escribir un programa que lea un entero porsitivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
#  La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:   suma=n(n+1)2

n = int(input('Introduce un numero entero'))
suma = n * (n + 1) /2
print("la suma de los primeros numeros enteros desde 1 hasta:" +str(n) ,"es:"  "\n" +str(suma))

                                                              