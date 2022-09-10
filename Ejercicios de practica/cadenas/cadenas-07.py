#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
# otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


email = input("Escribe tu correo")
print(email [:email.find("@")] ,"@ceu.es")    #se usa [:*****find ("lo que buscas")]
print(f"{email [:email.find('@')]}@ceu.es", "hey")    #se usa [:*****find ("lo que buscas")]