#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a 1000 € mensuales.
#  Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y 
# muestre por pantalla si el usuario tiene que tributar o no.

SALTO = "\n"
nombre = input(f"¿Como te llamas? {SALTO}")
edad = int(input(f"¿Que edad tienes? {nombre.title()} {SALTO}"))
ingresos = float(input(f"¿Cual son tus ingresoso? {nombre} {SALTO} "))
                                                                                          # forma de hacerlo con un if y and.
if edad >= 16 and ingresos >= 1000:
    print(f" {nombre.title()} : estas obligado a tributar tus impuestos")
else:
    print("Estas exento de hacer la declaración de impuestos")






    #tambien podemos hacerlo con un if y or es basicamente lo mismo pero alterando el orden

SALTO = "\n"
nombre = input(f"¿Como te llamas? {SALTO}")
edad = int(input(f"¿Que edad tienes? {nombre.title()} {SALTO}"))
ingresos = float(input(f"¿Cual son tus ingresoso? {nombre} {SALTO} "))

if edad <= 16 or ingresos < 1000:
    print("Estas exento de hacer la declaración de impuestos")
    
else:
    print(f" {nombre.title()} : estas obligado a tributar tus impuestos")

