from itertools import count

texto1 = "Examen 1T01"
texto2 = "Octubre-2025"

texto3 = texto1.replace(" ","-")
texto4 = texto2.replace("-"," ")

texto5 = len(texto1)
texto6 = len(texto2)
texto7 = texto5 + texto6

print("Resultado:",texto3,texto4,"(",texto7,")")


