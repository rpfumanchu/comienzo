#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

import math

#para el maximo comun divisor
def maxcd(n1,n2):
    a = max(n1,n2)
    b = min(n1,n2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd

def mincd(n1,n2):
    a = max(n1,n2)
    b = min(n1,n2)
    mcm = (a / maxcd(a,b)) * b
    return mcm


n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

print(f"El máximo común multiplo es: {maxcd(n1,n2)}")
print(f"El minimo común multiplo es: {mincd(n1,n2)}")