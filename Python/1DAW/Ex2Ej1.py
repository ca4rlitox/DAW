import random

numDados = int(input("Cuantos dados vas a tirar?"))
numUno = 0
numSeis = 0
suma = 0
print(f"Has tirado {numDados} dados y ha salido lo siguiente:")
for i in range(numDados):
    num = random.randint(1, 6)
    if i == numDados - 1:
        print(num)
    else:
        print(num, end=", ")
    if num == 6:
        numSeis += 1
    if num == 1:
        numUno += 1
    suma+=num

maximoDados = (numDados * 6) / 2

print(f"La suma de todos los dados da {suma}")
if maximoDados < suma:
    print(f"Tú tirada está por encima de la mitad ({maximoDados})")
elif maximoDados > suma:
    print(f"Tu tirada está por debajo de la mitad ({maximoDados})")
else:
    print(f"Tu tirada es exactamente la mitad {maximoDados}")