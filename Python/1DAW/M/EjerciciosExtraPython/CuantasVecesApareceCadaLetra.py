"""Pedir una palabra y mostrar cuántas veces aparece cada letra."""

#palabra=input("Ingresa una palabra: ")

"""letras=[]
for letra in palabra:
    if letra not in letras:
        letras.append(letra)

contadorLetras=[]
contador=0
for i in range(len(letras)):
    for letra in palabra:
        if letra==letras[i]:
            contador+=1
    contadorLetras.append(contador)
    contador=0
    print(f"la letra {letras[i]} aparece {contadorLetras[i]} veces")"""

"""VERSION MEJORADA"""
palabra="banana"
letras_unicas = []
for letra in palabra:
    if letra not in letras_unicas:
        letras_unicas.append(letra)

for letra in letras_unicas:
    print(f"La letra {letra} aparece {palabra.count(letra)} veces")
