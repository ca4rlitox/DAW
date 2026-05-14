import random

clientes = ["Diego Norrea", "Inés Perado", "Demetrio Imedio", "Roberto Rija", "Rubén Tosidad", "Armando Adistancia", "Germán Tequilla"]

numClientes = len(clientes)
numAfortunados = input("¿Cuantos premios vas a repartir?")

if numAfortunados.isnumeric() and int(numAfortunados) > 0:
    numAfortunados = int(numAfortunados)
    if numAfortunados == numClientes:
        print(f"Tienes sólo {numClientes} clientes. Les puedes dar un premio a cada uno.")
    if numAfortunados > numClientes:
        print(
            f"Tienes sólo {numClientes} clientes. Les puedes dar un premio a cada uno. Te sobran {numAfortunados - numClientes} premios sin repartir. ¡Guárdalos para el siguiente sorteo!")
    if numAfortunados < numClientes:
        listaClientes = clientes.copy()
        print("Los afortunados son: ")
        for i in range(numAfortunados):
            afortunado = random.choice(listaClientes)
            listaClientes.remove(afortunado)
            afortunado = afortunado.split(" ")
            print(afortunado[1],", ",afortunado[0],sep="")


else:
    print("El número de premios ha de ser entero positivo mayor o igual a 1")

