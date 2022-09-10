from utils.number_generator import number_generator

def num_euro():
    number_generator(5, 1, 50, "Tus números son: ")
    number_generator(2, 0, 12, "y tus estrellas: ")

# Te lo escribo en todas las funciones donde estaba.

# Esto no lo hagas porque si lo haces, entonces nunca voy a poder usar esta libreria sin ejecutar nada, y el objetivo es exportar funcionalidades, no ejecutarlas para ejecutarlas, se encarga el que haga el import de esta libreria
# num_euro()