#Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.


frase = input("Escribe una frase")
letra = input("escribe una letra")
numero = 0
for i in frase:
    if i == letra:
        numero +=1
print(f"la letra: {letra}  aparece {numero} veces en la frase: {frase}")
