"""Queremos crear una función que reciba un número variable e indeterminado de argumentos
numéricos y nos diga: el máximo, el mínimo y la media aritmética. Calcular cada una de
estos elementos mediante una función diferente"""

def numeroMax(*args):
    return max(args)

def numeroMin(*args):
    return min(args)

def media(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print("Numero mas alto: ",numeroMax(1,2,3,4,5,6,7,8,9,10))
print("Numero mas bajo: ",numeroMin(1,2,3,4,5,6,7,8,9,10))
print("Promedio: ",media(1,2,3,4,5,6,7,8,9,10))