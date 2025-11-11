texto = "Hola Mundooooooooooooooooooooooooooooooooooooooooooooooooooooo"
print(texto[::1])
print(texto[3] + texto[2])

subtexto = texto[0] + texto[2]

print(subtexto)

for catracter in range(0,len(texto)):
    print(catracter, "-", texto.replace("o","l"))