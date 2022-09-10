#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y 
# muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

#   IMC   Ejemplo: Peso = 68 kg, Estatura = 165 cm (1.65 m)Cálculo: 68 ÷ (1.65)2 = 24.98

peso = int(input("dime tu peso en Kilos:"))
altura = float(input("dime tu altura en metros:"))
          #permite un numero con decimales

imc = round((peso) /(altura)**2) 
      #sirve para redondear el numero


print("tu indice de masa corporal es :" +str(imc))

    
if imc < 30:
    print("estas en tu peso ideal")

else:
    print("estas muy gordo")