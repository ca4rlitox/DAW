
# contar espacios

try:
    with open("/Ficheros/ficheroEspacios.txt", "rt") as cursor:
        lista = cursor.readlines()
    contador = 0
    for caracter in lista:
        contador = contador + caracter.count(" ")
    print(f"El fichero tiene {contador} espacios en blanco")

except:
    print("El fichero no existe")