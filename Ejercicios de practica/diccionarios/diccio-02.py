#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
 #Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input("Escribe tu nombre:  ")
edad = input("¿Cuantos años tienes? ")
direccion = input("¿Donde vives? ")
telefono = input("¿Cual es tu telefono? ")

persona = {"nombre":nombre, "edad":edad, "direccion":direccion, "telefono":telefono}
print(persona ["nombre"], "tiene", persona["edad"], "años y vive en", persona["direccion"], " y su número de teléfono es", persona["telefono"])
