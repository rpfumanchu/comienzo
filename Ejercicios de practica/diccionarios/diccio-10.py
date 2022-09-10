# Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
#  Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
#  donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) 
# Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.

clientes = {}
opciones = ""
while opciones != "6":
    if opciones == "1":
        nif = input("Introduce el NIF del cliente: ")
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la direccion del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        email = input("Introduce el correo del cliente: ")
        vip = input("¿Es un cliente preferente (S/N): ")
        cliente = {"nombre":nombre, "dirección":direccion, "teléfono":telefono, "email":email, "preferente":vip=="S"}
        clientes[nif] = cliente
    
    if opciones == "2":
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print(f"No existe el cliente con NIF: {nif}")

    if opciones == "3":
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print(f"NIF: {nif}")
            for clave,valor in clientes[nif].items():
                print(f"{clave.title()} : {valor}")
        else:
            print("Este cliente no existe: ")

    if opciones == "4":
        print("Lista de clientes: ")
        for clave,valor in clientes.items():
            print(f"{clave} {valor['nombre']} ")

    if opciones == "5":
        print("******************************")
        print("lista de clientes preferentes: ")
        for clave,valor in clientes.items():
            if valor["preferente"]:
                print(f"{clave} {valor['nombre']}") 

    
    opciones = input("Menu de opciones:\n (1) Añadir cliente\n (2) Eliminar cliente\n (3) Mostrar cliente\n (4) lista de clientes\n (5) lista clientes preferentes\n (6) Terminar\n Elije una opción: ")
