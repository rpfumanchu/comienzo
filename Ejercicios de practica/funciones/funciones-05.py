#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
#area = a numero pi * radio al cuadrado y el volumen es π r² h

def area_circulo(r):
    pi = 3.14
    area = pi*r**2
    return area
print(area_circulo(3))

def volumen_circulo(r,h):

    pi =3.14
    volumen = pi*r**2*h
    return volumen


print(volumen_circulo(3,10))