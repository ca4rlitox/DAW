animes = {}
try:
    with open("/home/alumno/DAW/Python/1DAW/animes.txt", 'r') as fichAnime:
        for linea in fichAnime:
            linea2 = linea.strip()
            if linea2 != "":
                partes = linea2.split(' ', 1)

                if len(partes) == 2:
                    idAnime = partes[0]
                    nombreAnime = partes[1]
                    animes[idAnime] = nombreAnime

    print("Animes:", animes)
except:
    print("Error, el archivo no existe")

personajes = {}
try:
    with open("/home/alumno/DAW/Python/1DAW/personajes.txt", 'r') as fichPersonajes:
        for linea in fichPersonajes:
            linea2 = linea.strip()
            if linea2 != "":
                partes = linea2.split(' ', 1)
                if len(partes) == 2:
                    idAnime = partes[0]
                    nomPersonaje = partes[1]
                    if idAnime in personajes:
                        personajes[idAnime].append(nomPersonaje)
                    else:
                        personajes[idAnime] = []
                        personajes[idAnime].append(nomPersonaje)

    print("Personajes:", personajes)
except:
    print("Error, el archivo no existe")

try:
    with open("salida.txt", 'wt') as fichSalida:
        for idAnime in animes:
            nombreAnime = animes[idAnime]
            fichSalida.write(nombreAnime + "\n")
            if idAnime in personajes:
                lista_personajes = personajes[idAnime]
                for personaje in lista_personajes:
                    fichSalida.write("- " + personaje + "\n")
            else:
                fichSalida.write("- No hay personajes\n")

except:
    print("Error al crear el fichero.")