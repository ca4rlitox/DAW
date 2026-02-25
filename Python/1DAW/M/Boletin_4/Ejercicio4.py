"""
4. Escribir un programa que cuente el número de cifras que tiene un número (por ejemplo,
el 8 tiene una cifra, el 221 tres y el 456789 seis).
"""

num=int(input("Ingrese un número para conocer cuantas cifras tiene "))
numTexto=str(num)

print("El número ",num," tiene ",len(numTexto)," cifras.")