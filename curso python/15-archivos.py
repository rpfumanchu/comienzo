def app():
    #crear el archivo
    archivo = open('archivo.txt','w') # w es escritura si existe lo creara

    #generar numeros en archivo
    for i in range(0,20):
        archivo.write('lo vas hacer' + str(i) + "\r\n")

        #cerrar el archivo
    archivo.close()


app()
