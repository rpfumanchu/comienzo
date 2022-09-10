#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

print("hola buenas")
edad = int(input("¿Cuantos años tienes?"))
for i in range(edad):
    print(f"Has cumplido: {i+1} años")
    