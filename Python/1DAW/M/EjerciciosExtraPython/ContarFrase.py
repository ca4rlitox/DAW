"""Pedir una frase y mostrar cuántas palabras tienen 6 letras o más"""

frase=input('Ingresa una frase: ')

listaFrase=frase.split()
contadorLetras=0
for palabra in listaFrase:
    if len(palabra)>5:
        contadorLetras+=1


print(f"hay {contadorLetras} palabras con mas de 5 letras")