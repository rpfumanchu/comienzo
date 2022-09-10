#Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
#  Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
# y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura,
# pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
#  Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación 
# el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

factura= {}
cobrado = 0
pendiente = 0
seguir = ""
while seguir != "terminar":
    if seguir == "añadir":
        clave = input("Introduce el número de la factura: ")
        valor = float(input("Introduce el coste de la factura: "))
        factura[clave] = valor
        pendiente += valor
    if seguir == "pagarla":
        clave = input("Introduce el numero de la factura a pagar: ")
        valor = factura.pop(clave,0)
        cobrado += valor
        pendiente -= valor
    print(f"recaudado: {cobrado}")
    print(f"pendiente de cobro: {pendiente}")
    seguir = input("¿Quieres añadir una nueva factura,`pagarla o terminar: ")
