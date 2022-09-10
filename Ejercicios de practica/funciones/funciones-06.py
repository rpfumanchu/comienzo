#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def calcular_media(muestra):
    media = sum(muestra)/len(muestra)
    return media

print(calcular_media([1,2,3,4,5]))
