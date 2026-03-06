import random
contadorUnos=0
contadorSeises=0
sumaDados=0

numDados = int(input("¿Cuantos dados vas a tirar?"))
print(f"Has tirado {numDados} dados y ha salido lo siguiente: ")
for i in range(0,numDados):
    dadoRandom = random.randint(1,6)
    sumaDados+=dadoRandom
    if dadoRandom == 1:
        contadorUnos+=1
    if dadoRandom == 6:
        contadorSeises+=1

    if i+1 == numDados:
        print(dadoRandom,end="")
    else:
        print(dadoRandom,end=", ")

print(f"\nEn {contadorUnos} dado/s ha salido un 1.")
print(f"En {contadorSeises} dado/s ha salido un 6.")
print(f"La suma de todos los dados da {sumaDados}")

encimaMitad = (numDados * 6)/2
if encimaMitad < sumaDados:
    print(f"Tu tirada está por encima de la mitad ({encimaMitad})")
elif encimaMitad > sumaDados:
    print(f"Tu tirada por debajo de la mitad ({int(encimaMitad)})")
else:
    print(f"Tu tirada es exactamente la mitad ({int(encimaMitad)})")