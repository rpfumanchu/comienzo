def app():

    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip())

app()


# con with open no hace falta cerrar con close