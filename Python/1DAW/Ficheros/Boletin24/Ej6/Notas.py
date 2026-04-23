notasXalumno = []
soluciones = []
alumnos = []
notaPorAlumno = []
try:
    with open('respuestas.txt',"r") as archivo:
        lineas = archivo.readlines()

        for line in lineas:
            hola = line.split(": ")
            alumnos.append(hola[0])
            notasXalumno.append(hola[1].replace("\n", ""))

    print(alumnos)
    print(notasXalumno)

    with open ("soluciones.txt",'r') as archivo:
        soluciones = archivo.readlines()
        for line in soluciones:
            soluciones = line.split(", ")
        print(soluciones)

    with open("notas.txt",'wt') as archivo:
        comparar = []
        contador = 0

        for nota in notasXalumno:
            comparar = notasXalumno[nota]



except:
    print("Error")