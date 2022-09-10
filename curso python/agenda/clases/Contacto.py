SALTO_LINEA = '\n'

class Contacto:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def write_to_file(self, file):
        file.write(f'Nombre: {self.nombre}{SALTO_LINEA}')
        file.write(f'Telefono: {self.telefono}{SALTO_LINEA}')
        file.write(f'Categoria: {self.categoria}{SALTO_LINEA}')
        file.write(f'Edad: {self.edad}{SALTO_LINEA}')
        file.write(f'Genero: {self.edad}{SALTO_LINEA}')

    def request_extra_data(self):
        self.telefono = input(f'Agregar el teléfono: {SALTO_LINEA}')
        self.categoria = input(f'Categoria contacto: {SALTO_LINEA}')
        self.edad = input(f'Edad contacto: {SALTO_LINEA}')
        self.genero = input(f'Genero contacto: {SALTO_LINEA}')