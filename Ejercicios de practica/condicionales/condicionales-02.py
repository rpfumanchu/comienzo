#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
#  por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide
# con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = "ferpen05"
clave = input("introduce tu contraseña: \n")

        # casefold se usa para implementar la cadena de coincidencia de cadenas sin mayusculas ni minusculas.elimina todas las distinciones.
        
if clave.casefold() == contraseña.casefold():
    print("La contraseña es correcta")
else:
    print("contraseña no valida")
    
