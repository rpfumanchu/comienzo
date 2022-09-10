from loterias.bonoloto import num_bonoloto
from loterias.primitiva import num_primitiva
from loterias.euromillones import num_euro
from loterias.gordo import num_gordo

# Aqui he jugar con los números permitidos y con la opcion seleccionada, así si un día se añade otra opcion
# Empieza en -1 por ponerle un número cualquiera que no esté en el array

def mostrar_menu():

    opciones_validas = [1,2,3,4]
    opcion_seleccionada = -1

    while opcion_seleccionada not in opciones_validas:
        opcion_seleccionada = int(input(f"Elije el tipo de juego al que deseas apostar: "))
        if opcion_seleccionada == 1:
            print("$$ ESTA ES TU COMBINACION GANADORA DE BONOLOTO $$")
            num_bonoloto()
        elif opcion_seleccionada == 2:
            print("$$ ESTA ES TU COMBINACION GANADORA DE PRIMITIVA $$")
            num_primitiva()
        elif opcion_seleccionada == 3:
            print("$$ ESTA ES TU COMBINACION GANADORA DE EURO $$")
            num_euro()
        elif opcion_seleccionada == 4:
            print("$$ ESTA ES TU COMBINACION GANADORA DE GORDO $$")
            num_gordo()
        else:
            print("Elije un juego de azar existente")
            mostrar_menu()
