#Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea
#  (url: https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), 
# pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.


def parsear_pib (url):
    ''' Función que parsea un fichero con pibs de países.
    Parámetros:
        url: Es una cadena con la url del fichero de texto que contiene el pib per cápita.
    Devuelve:
        Un diccionario con pares pais:pibs donde pibs es, a su vez, un diccionario con los años y los pibs del país.'''

    from urllib import request     #request se usa para hacer una peticion y que te la devuelva

    from urllib.error import URLError     #Los gestores lanzan esta excepción (o excepciones derivadas) cuando encuentran un problema. Es una subclase de OSError.'''

    try:
        with request.urlopen(url) as fichero: 
            datos = fichero.read().decode("utf-8").split("\n")    #Leer los datos y guardar cada línea en una lista.'''
    except URLError:
        return(f"La url {url} no existe!!!!")
    else:
        '''para obtener los datos de la primera linea del fichero'''
        años = datos.pop(0).split("\t")[1:]
        '''dicionario principal donde guardo los pibs de todos los paises'''
        diccio_pibs = {}
        '''bucle iterativo para recorrer las lineas del fichero'''
        for pais in datos:
            datos_pais = pais.split("\t")
            '''obtenemos el codigo del pais de los dos últimos caracteres del primer campo de la lista'''
            codigo_pais = datos_pais.pop(0)[-2:]
            '''un diccionario con los años y los pib del pais'''
            diccio_pais = {}
            '''bucle iterativo para recorrer los pibs del pais'''
            for i in range(len(datos_pais)):
                '''strip Este método se utiliza para eliminar todos los espacios en blanco iniciales y finales de una cadena.
                 También tiene en cuenta los tabuladores y saltos de línea. En realidad strip() devuelve una copia de 
                la cadena con los caracteres iniciales y finales en blanco eliminados.'''
                diccio_pais[años[i].strip()] = datos_pais[i].strip()
                '''añadimos el diccionario con los pib el pais al diccionario principal'''
            diccio_pibs[codigo_pais] = diccio_pais
        return diccio_pibs


def pib (pibs, pais ):
    ''' Función que recibe un diccionario con los pibs de los países y muestra por pantalla los pibs de un país dado.

    Parámetros:
        - pibs: Es un diccionario con los pibs de los países como el que devuelve la función parsear_pibs.
        - pais: Es una cadena con el código del país.

    Salida:
        Muestra por pantalla los pibs del país indicado.'''


    print("Año \t pib ")
    for i, j in pibs[pais].items():
        print(i, "\t", j)

pais = input("Introduce el codigo de un pai: ")
print(f"Producto interior bruto per capita de {pais}: ")
pib(parsear_pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)
















