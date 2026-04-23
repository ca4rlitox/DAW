
try:
    with open("DarLaVuelta.txt","wt") as archivo:
        archivo.write("Uno")
        archivo.write("\n")
        archivo.write("Dos")
        archivo.close()

except:
    print("error")