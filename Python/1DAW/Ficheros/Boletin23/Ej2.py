def estadisticas(fichero):
    try:
        with open(fichero, "r") as fichero:
            t = fichero.read()
            lineas = 0
            lineasEnBlanco = 0
            cantidadCaracteres = 0
            cantidadEspacios = 0
            for linea in t:
                linea+=t
                if linea == "\n":
                    lineas+=1
            

            linea = linea.replace("\n","")
            print(linea)

    except:
        print("El fichero no existe")

estadisticas("fichero.txt")