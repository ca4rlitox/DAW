"""Escribir un programa que nos pida por teclado primero una cadena y luego un carácter.
A continuación debe de imprimirnos cuantas veces aparece dicho carácter y en las
posiciones de la cadena donde lo hace. Por ejemplo, si nuestra cadena es Hola Mundo
y el carácter la o nos debería de decir algo así:
La o aparece en 2 ocasiones
Las posiciones en las que aparece son: 1,9"""

cadena=input("Introduce una cadena de texto: ")
caracter=input("Ahora introduce un caracter a buscar en la cadena que escribiste: ")

cantidad=cadena.count(caracter)
print(caracter," aparece ", cantidad, " de veces en tu cadena")

print("Las posiciones en las que aparece el carácter ",caracter, " en tu cadena son",end=": ")
for indice, car in enumerate(cadena):
    if car==caracter:
        print(indice+1,end=", ")