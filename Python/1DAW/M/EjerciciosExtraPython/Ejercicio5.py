"""Pide una frase al usuario y muestra cuántas veces se repite cada palabra
(ignora mayúsculas/minúsculas). Por ejemplo, si el usuario escribe:"""

frase=input("Ingresa una frase: ").lower()

lista = frase.split()
palabrasDistintas=[]
for palabra in lista:
    if palabra not in palabrasDistintas:
        cantidad=lista.count(palabra)
        print(palabra ,"->",cantidad)
        palabrasDistintas.append(palabra)
