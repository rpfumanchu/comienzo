from utils.number_generator import number_generator

def num_primitiva():
    number_generator(6, 1, 49, "Tus números son: ")
    number_generator(1, 0, 9, "Y el complementario es: ")

# Te lo escribo en todas las funciones donde estaba.

# Esto no lo hagas porque si lo haces, entonces nunca voy a poder usar esta libreria sin ejecutar nada, y el objetivo es exportar funcionalidades, no ejecutarlas para ejecutarlas, se encarga el que haga el import de esta libreria
# num_primitiva()