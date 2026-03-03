texto1 = "Examen 1T01"
texto2 = "Octubre-2025"


cadena1 = texto1.split(" ")
cadena2 = texto2.split("-")

cadenaResultante = cadena1[1]+"-"+cadena2[1]+" "+cadena1[0]+" "+cadena2[0]
cadenaResultante = cadenaResultante + " ("+str((len(cadenaResultante)))+")"
print(cadenaResultante)
