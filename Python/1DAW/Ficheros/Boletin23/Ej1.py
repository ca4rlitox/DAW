fichero = input("Ingrese el nombre del fichero: ")
try:
    with open(fichero,"rt") as fichero:
        palabraBuscada = input("Ingrese la palabra a buscar: ")
        t = fichero.read()
        lineas=0
        palabras=[]
        palabra=""
        for linea in t:
            palabra+=linea
            if linea == "\n":
                lineas+=1
                palabra = palabra.replace("\n","")
                palabras.append(palabra)
                palabra=""

        contador=0
        for palabra in palabras:
            if palabra == palabraBuscada:
                contador+=1
        print("El fichero tiene",lineas,"lineas")
        print(f"La palabra {palabraBuscada} aparece {contador} veces")
        fichero.close()
except:
    print(f"El fichero {fichero} no existe")