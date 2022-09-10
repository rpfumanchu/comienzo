#print('hey','hi','hello', sep='_')
#print('hey','hi','hello', sep='\t')           ejemplos con sep 
#print('hey','hi','hello', sep='\n')

#hey_hi_hello
#hey	hi	hello
#hey
#hi
#hello





#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	Tipo impositivo

#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

      # total a pagar : renta x tipo / 100

while True:
    renta = float(input("¿Cual es tu renta anual?  "))
    if renta < 10000:
        tipo = 5
    elif renta < 20000:
        tipo = 15
    elif renta < 35000:
        tipo = 20
    elif renta < 60000:
        tipo = 30
    else:
        tipo = 45
    total = renta * tipo / 100
    print(f"Se te aplica un {tipo} % y tienes que pagar: {total}  euros. " )
    continue
