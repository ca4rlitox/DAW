# Escribir un programa que pida por teclado una cadena de texto y la escriba con el
# alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
# el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
# las vocales pueden estar escritas en mayúsculas o minúsculas, pero no hace falta que
# tengas en cuenta que además podrían ir acentuadas

texto = input("Escribe lo que quieres cifrar")

cifrado = (texto
        .replace('a', '4').replace('A', '4')
        .replace('e', '3').replace('E', '3')
        .replace('i', '1').replace('I', '1')
        .replace('o', '0').replace('O', '0'))

print(cifrado)