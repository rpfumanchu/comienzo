class Restaurant:

    def agregar_restaurant(self,nombre):  #self argumento
        self.nombre = nombre #atributo

    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}')

    #instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant('pizzeria carlos')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('hamburguesas python')
restaurant2.mostrar_informacion()


#mostrar la informacion otra forma
# print(f'Nombre Restaurant:  {restaurant.nombre}')
# print(f'Nombre Restauran:  {restaurant2.nombre}')