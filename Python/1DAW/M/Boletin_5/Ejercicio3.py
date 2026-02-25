"""Escribir un programa que cuenta las palabras que tiene una frase introducida
previamente por teclado. Las palabras pueden estar separadas por más de un espacio
pero siempre debe de haber al menos uno. No tenemos en cuenta los signos de
puntuación como separadores."""

frase=input("Ingresa una frase: ")

lista = frase.split()

cantidad = len(lista)
print("la frase introducida tiene ",cantidad," de palabras")