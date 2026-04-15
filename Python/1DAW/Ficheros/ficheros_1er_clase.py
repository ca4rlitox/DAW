#vamos a empezar con leer ficheros

try:
    cursor=open("/Ficheros/ficheroEspacios.txt", "rt") #abrimos el fichero y cualquier referencia que quiera hacer sobre el fichero utilizaré la variable que creé (cursor)
                                # rt significa el modo en el que estamos trabajando, por defecto es modo lectura y modo texto (rt) pero sino necesitamos especificar el modo
                                #si pongo el nombre del fichero solamente, el programa buscara el fichero donde se encuentra el programa.
                                #lo mejor es trabajar con rutas absolutas para no tener problemas

    #primer method: leemos el fichero entero
    """texto=cursor.read()
    print(texto)"""

    #segundo method: leemos línea a línea
    """linea=cursor.readline()
    while linea!="": #mientras la línea no esté vacía nos imprime la línea
        print(linea, end="") #como el print tambien te pone un salto de línea tenemos que poner el end, sino aparecerán dos saltos, el propio del fichero y el del print
        linea=cursor.readline()"""

    #otro method para leer línea a línea
    """for linea in cursor:
        print(linea,end="")"""

    lista=cursor.readlines() #me lee todas las líneas y lo mete en una lista: transforma cada línea en un elemneto de una lista
    print(lista)
    #

    cursor.close()

    #si quiero leer un fichero que no existe me va a dar un error
except:
    print("Error trabajando con el fichero")