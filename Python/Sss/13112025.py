import random
# Seguimos por conversiones entre listas y cadenas
nombres = ["Ana","Lele","Strebg"]
numeros = [12, 13, 14, 14, 14.3]

print(nombres[2:4])
print(nombres)
texto = str(nombres)
texto = texto.replace('[', "")
texto = texto.replace(']', "")

print(texto)

# Como usar separadores, en .split() ponemos que determina que se separe
cadena = "192.168.1.4"
lista = cadena.split('.')
print(lista)

# Transformar cadena en una lista
lista = list("Gilipollas")
print(lista)

# Arrays bidimensionales
matriz = [[2,3],[7,14]]
print(matriz)
print(matriz[0][0])

# Para sustituir valores de la matriz
matriz[0][0] = 8
print(matriz[0][0])
matriz[0] = [0,9]
print(matriz)

# Funcion reverse
texto1 = texto.reverse()
print(lista)