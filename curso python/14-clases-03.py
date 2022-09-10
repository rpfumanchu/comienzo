class Restaurant:

    def __init__(self,nombre, categoria,precio):   #self argumento
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.__precio = precio  #defaul public si le ponemos un guion bajo 
                               # lo hacemos protected,private doble _
    
    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}, Categoria:  {self.categoria}, Precio:  {self.__precio}')
        
        #metodos getters y setter-get obtiene un valor,set agrega un valor
    def get_precio(self):     #get usualmente se utiliza con un return
        self.__precio 
        return self.__precio

    def set_precio(self,precio):
        self.__precio = precio

        

    #instanciar la clase
restaurant = Restaurant('pizzeria carlos','comida italiana','50 euros')


        #esto es un ecapsulamiento
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()   #al ser __ private ya no podra ser modificado
print(precio)

restaurant2 = Restaurant('hamburguesas python','comida casual','15 euros')


restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
precio = restaurant2.get_precio()
print(precio)
