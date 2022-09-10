import random

def number_generator(loteria_numbers: int, start_sequence: int, stop_sequence: int, message: str = None):

    """
    Genera números y envia un mensaje personalizado por pantalla a partir de parámetros.
    
    Parámetros:

    loteria_numbers: La cantidad de números que va a generar
    start_sequence: Limite mínimo del número a generar
    stop_sequence: Limite máximo del número a generar
    step_sequence: Incremental que se va a usar para el random
    message: Mensaje que va a salir por pantalla, si vale None, no muestra nada (por defecto, si no lo pones, vale None)
    """

    if(message != None):
        print(message.lower().capitalize())

    for _ in range(loteria_numbers):
        print(f"**\t{random.randint(start_sequence, stop_sequence)}")



