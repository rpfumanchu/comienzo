class Restaurant:

    def __init__(self,nombre, categoria,precio):   #self argumento
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.precio = precio  #defaul public si le ponemos un guion bajo 
                               # lo hacemos protected,private doble _
    
    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}, Categoria:  {self.categoria}, Precio:  {self.precio}')
        
        #metodos getters y setter-get obtiene un valor,set agrega un valor
    def get_precio(self):     #get usualmente se utiliza con un return
        self.precio 
        return self.precio

    def set_precio(self,precio):
        self.precio = precio

        #crear una clase hijo de Restaurant "HERENCIA"
class Hotel(Restaurant):
    def __init__(self,nombre,categoria,precio,piscina):
        super().__init__(nombre,categoria,precio) 
        self.piscina = piscina

       #reescribir un metodo debe llamarse igual
    def mostrar_informacion(self):
        print(f'nombre: {self.nombre}, Categoria:  {self.categoria}, Precio:  {self.precio}, piscina: {self.piscina}')    

        #agrgar un metodo especifico de hotel "poliformismo"
    def get_piscina(self):
        return self.piscina    #solo existe en la clase hijo


hotel = Hotel('Hotel poo',' 5 estrellas',200,'si')      
hotel.mostrar_informacion()
piscina = hotel.get_piscina()
print(piscina)