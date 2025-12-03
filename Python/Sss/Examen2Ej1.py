import random

numDados= int(input("¿Cuantos dados vas a tirar?"))
tirada=[]
for _ in range(numDados):
    dado = random.randint(1,6)
    tirada.append(dado)

    print("Has tirado",numDados,"y ha salido lo siguiente:")
    txtTirada=str(tirada)
    print(txtTirada[1:-1])