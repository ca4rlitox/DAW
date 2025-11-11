# Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
# comunique, además de si es válido de que tipo es.
# Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a
# continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar
# escritas con mayúsculas o con minúsculas

nif = input("Introduce tu NIF/NIE: ")

if len(nif) == 9:
    numeros = nif[:8]
    letra = nif[8]

    if numeros[1:7].isdigit() and (letra[8:8].isalpha(),letra[0:0].isalpha()):
        print("NIE correcto. Proceda")

    elif numeros[0:8].isdigit() and letra[:8].isalpha():
        print("El NIF tiene un formato correcto.")
else:
    print("Algo has hecho mal. Intentalo de nuevo")
