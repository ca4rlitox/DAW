# Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
# vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”.

texto = input("Introduce el texto y lo recibirás sin vocales")

sin_vocales = (texto.replace("a","")
               .replace("e","")
               .replace("i","")
               .replace("o", "")
               .replace("u","")
               .replace("A", "")
               .replace("E","")
               .replace("I","")
               .replace("O", "")
               .replace("U",""))

print(sin_vocales)