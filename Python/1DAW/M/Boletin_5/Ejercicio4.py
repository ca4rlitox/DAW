"""Escribir un programa que nos pida una cadena por teclado y luego cuente cuantas
palabras hay en ella con cuatro o más vocales diferentes. Por ejemplo, si introducimos
la frase “Crisis constitucional por culpa del murcielago guineoecuatorial” Nos debería de
decir que 3. Tendrías que tener en cuenta que las vocales pueden ir en mayúsculas o no
y son la misma letra. Presupón que ninguna vocal va acentuada de ninguna forma."""

frase=input("Introduce una frase: ").lower()

listaFrase=frase.split()
"""vocalesDiferentes=[0]
vocales= "aeiou"
contador=0
for palabra in listaFrase:
    for vocal in palabra:
        if vocal not in vocalesDiferentes:
            if vocal in vocales:
                vocalesDiferentes.append(vocal)
                if len(vocalesDiferentes)>3:
                    contador+=1
print(contador)"""


#OTRA FORMA (pero no muy optima)
"""contadorPalabras=0

for palabra in listaFrase:
    contadorVocales = 0
    if(palabra.find("a")!=-1): #find si no encuentra la vocal devuelve -1 por eso si no es -1 es que la vocal si esta
        contadorVocales += 1
    if(palabra.find("e")!=-1):
        contadorVocales += 1
    if(palabra.find("i")!=-1):
        contadorVocales += 1
    if(palabra.find("o")!=-1):
        contadorVocales += 1
    if(palabra.find("u")!=-1):
        contadorVocales += 1
    if contadorVocales > 3:
        contadorPalabras += 1
        
print("En tu frase hay",contadorPalabras,"palabras con 4 o más vocales diferentes.")"""

#OTRA FORMA (pero mas optima)

contadorPalabras=0
vocales=["a","e","i","o","u"]
for palabra in listaFrase:
    contadorVocales = 0
    for vocal in vocales:
        if palabra.find(vocal) != -1:
            contadorVocales += 1
    if contadorVocales > 3:
        contadorPalabras += 1

print("En tu frase hay",contadorPalabras,"palabras con 4 o más vocales diferentes.")