"""Crear una función que reciba una lista de números y devuelva el mayor sin usar max()"""

numeros = [4, 10, 2, 8, 15, 7]

mayor = numeros[0]

for num in numeros:
    if num > mayor:
        mayor = num

print("El número mayor es:", mayor)