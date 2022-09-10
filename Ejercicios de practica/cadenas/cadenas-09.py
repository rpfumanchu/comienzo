#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("introduce una fecha en este formato: dd/mm/aaaa  ")
print("dia",fecha[:2])
print("mes",fecha[3:5])
print("año",fecha[6:])


fecha = input("introduce una fecha en este formato: dd/mm/aaaa  ")
dia = fecha[:fecha.find("/")]
mes_año = fecha[fecha.find("/") +1:]
mes = mes_año[:mes_año.find("/")]
año = mes_año[mes_año.find("/") +1:]      # es muy importante el orden de los : para saber a partir de donde empezar
print(f"dia {dia}")
print(f"mes {mes}")
print(f"año {año}")