#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y 
# pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
# pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
#  La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.


inaceptable = 0
aceptable = 0.4
meritorio = 0.6
bonos = 2.400
clasificacion = float(input("Introduce tu puntuación: "))
total = clasificacion * bonos
if clasificacion == inaceptable:
    nivel = "inaceptable"
elif clasificacion == aceptable:
    nivel = "aceptable"
elif clasificacion == meritorio:
    nivel = "meritorio"
else:
    nivel = ""
if nivel == "":
    print("Tu puntuacion no es valida")    
else:
    print(f"tu nivel de rendimiento es: {nivel}")    
    print(f"gracias a tu nivel te corresponde cobrar: {total}")
