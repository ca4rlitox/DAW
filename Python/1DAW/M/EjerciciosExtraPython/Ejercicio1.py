"""Escribe un programa que pida una frase al usuario y diga cuántas letras distintas
tiene (ignorando mayúsculas/minúsculas y sin contar espacios ni números)."""

frase=input("Ingresa una frase: ").lower()

letrasDistintas=[0]
for letra in frase: #recorremos todas las letras de la frase (incluyendo espacios y números)
    if 'a' <=letra <= 'z': #comprobamos que es una letra, ya que letra es mayor o igual a 'a' y menor o igual a 'z'
                    #otra manera podria ser con isalpha()
        if letra not in letrasDistintas: #si letra no esta en letras distintas....
            letrasDistintas.append(letra)#.... la añadimos

print("Cantidad de letras distintas: ", len(letrasDistintas))
