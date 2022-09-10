class Restaurant:

    def __init__(self,nombre, categoria,precio):   #self argumento
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.precio = precio
    
    
    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}, Categoria:  {self.categoria}, Precio:  {self.precio}')
        

    #instanciar la clase
restaurant = Restaurant('pizzeria carlos','comida italiana','50 euros')
restaurant.mostrar_informacion()

restaurant2 = Restaurant('hamburguesas python','comida casual','15 euros')
restaurant2.mostrar_informacion()

