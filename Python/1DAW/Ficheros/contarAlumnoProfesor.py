try:
    with open("/home/alumno/DAW/Python/1DAW/Ficheros/alumnosYprofesores.txt","rt") as archivo:
        lista = archivo.readlines()
        profe=[]
        contProfe=0
        alumno= []
        contAlumno=0
        for linea in lista:
            elementos = linea.split(": ")
            elementos[1] = elementos[1].replace("\n","")
            if elementos[0] == "Profesor":
                profe.append(elementos[1])
            else:
                alumno.append(elementos[1])
        print(f"Profesores: {profe}")
        print(f"Alumnos: {alumno}")



except:
    print("El archivo no existe")