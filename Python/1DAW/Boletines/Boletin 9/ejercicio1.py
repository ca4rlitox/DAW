clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, "
                                                         "Francisco": 44, "Cotón, Carmelo": 56 }

def ordenacion():
    nomClientes = list(clientes.keys())
    print(nomClientes)
    nombres = []
    apellido = []
    for nomClientes in nomClientes:
        separadorNombre = nomClientes.split(", ")
        separadorNombre = separadorNombre[1]
        nombres.append(separadorNombre)
    nombres.sort()

    nomClientes = list(clientes.keys())
    for nomClientes in nomClientes:
        separadorApellido = nomClientes.split(", ")
        separadorApellido = separadorApellido[0]
        apellido.append(separadorApellido)

    for i in range (len(nombres)):
        print(f"{nombres[i]} {apellido[i]} ({clientes.values()})")



ordenacion()