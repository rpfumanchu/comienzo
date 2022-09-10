#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def decimal_binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal //2
    return str(decimal) + binario


def binario_decimal(binario):
    binario = list(binario)
    binario.reverse()
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2 **i
    return (decimal)


numero = int(input("Introduce un número para convertir en binario: "))
numero1 = str(input("Introduce un numero binario para pasar a decimal: "))
print(decimal_binario(numero))
print(binario_decimal(numero1))