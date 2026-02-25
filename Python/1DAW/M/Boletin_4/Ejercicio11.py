"""Escribir un programa que nos pida una frase por teclado y luego nos la imprima
separando todos los caracteres de sus palabras (excepto los espacios) con un guión.
Por ejemplo, si la frase introducida es “esto es una prueba” la salida del programa
debería de ser “e-s-t-o e-s u-n-a p-r-u-e-b-a”"""


"""frase= input("Introduce una frase: ")
for elemento in frase:
    if elemento != " ":
        print(elemento, end="-")

    else:
        print(elemento, end="")"""

"""frase=frase.replace("","-") #otra solucion pero que no es correcta tampoco
print(frase)"""

#FORMA CORRECTA VISTA EN CLASE

frase= input("Introduce una frase: ")
fraseNueva=""
for posicion in range(0, len(frase)):
    if posicion != len(frase)-1:
        if frase[posicion] == " " or frase[posicion+1] == " ":
            fraseNueva = fraseNueva + frase[posicion]
        else:
            fraseNueva=fraseNueva+frase[posicion]+"-"
    else:
        fraseNueva=fraseNueva+frase[posicion]

print(fraseNueva)