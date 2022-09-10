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

        #crear una clase hijo de Restaurant "HERENCIA"
class Hotel(Restaurant):
    def __init__(self,nombre,categoria,precio):
        super().__init__(nombre,categoria,precio) 
hotel = Hotel('Hotel poo',' 5 estrellas',200)      
hotel.mostrar_informacion()