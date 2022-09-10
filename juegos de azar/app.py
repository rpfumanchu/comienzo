

SALTO = "\n"


from menu import mostrar_menu


def app():
    
  
    
    preguntar = True
    while preguntar:
        
        opcion = int(input(f"Elije el tipo de juego al que deseas apostar: "))
        if opcion == 1:
            print("$$ ESTA ES TU COMBINACION GANADORA $$")
            from bonoloto import num_bonoloto
            preguntar = False
        elif opcion == 2:
            print("$$ ESTA ES TU COMBINACION GANADORA $$")
            from primitiva import num_primitiva
            preguntar = False
        elif opcion == 3:
            print("$$ ESTA ES TU COMBINACION GANADORA $$")
            from euromillones import num_euro
            preguntar = False
        elif opcion == 4:
            print("$$ ESTA ES TU COMBINACION GANADORA $$")
            from gordo import num_gordo
            preguntar = False
        else:
            print("Elije un juego de azar existente")
    app()
        

app()
        
