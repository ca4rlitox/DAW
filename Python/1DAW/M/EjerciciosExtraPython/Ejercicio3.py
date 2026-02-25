"""Pide al usuario una frase y determina cuántas palabras son palíndromos
(es decir, se leen igual de izquierda a derecha y de derecha a izquierda,
como “ana” o “reconocer”)."""

frase=input("Ingresa una frase: ")
lista = frase.split()

contador=0
for elemento in lista:
    elemento = elemento.lower()
    elementoAlReves=elemento[::-1]
    if elemento == elementoAlReves: #tambien podria ser elemento == elemento[::-1]
        contador+=1

if contador>1:
    print("En la frase: -",frase,"- Hay ",contador," palabras que son palíndromos",sep="")
else:
    print("En la frase: -", frase, "- Hay ", contador, " palabra que es palíndromo",sep="")