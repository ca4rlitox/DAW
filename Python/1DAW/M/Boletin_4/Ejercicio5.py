"""
5. Escribir un programa que nos diga si un número es capicúa.
"""

num=int(input("Ingrese un número"))
numTexto=str(num)

if numTexto[0:]==numTexto[-1::-1]:
    print("El número es capicua")
else:
    print("El número no es capicua")
