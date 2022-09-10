# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
# hasta que introduzca la contraseña correcta.

clave = "roberto"
contraseña=""
while contraseña != clave:
    contraseña = input("introduce tu contraseña: ")
    if contraseña == clave: 
        print("contraseña correcta")
    