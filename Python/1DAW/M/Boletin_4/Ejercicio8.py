"""Escribe un programa que sume por un lado las cifras pares y por otro las impares de un
número y nos muestre ambos resultados. Por ejemplo, si el número en cuestión es el
128 nos debería e decir que la suma de las cifras pares es 9 y la de las impares 2
"""

num=int(input("Ingrese un numero: "))
numTexto=str(num)
lista=list(numTexto)
sumaPares=0
sumaImpares=0
for elemento in lista:
    if int(elemento)%2==0:
        sumaPares=sumaPares+int(elemento)
    else:
        sumaImpares=sumaImpares+int(elemento)

print("La suma de las cifras pares es ",sumaPares)
print("La suma de las cifras impares es ",sumaImpares)