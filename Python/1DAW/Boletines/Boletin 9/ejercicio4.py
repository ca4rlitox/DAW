def diccionario(frase):
    diccionario = {}
    palabras = frase.split(" ")
    for i in palabras:
        if palabras.count(i):
            diccionario[i] = palabras.count(i)

    print(diccionario)



frase = input("Ingrese una frase: ")
diccionario(frase)