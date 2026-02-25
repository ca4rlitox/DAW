clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}


def mostrar_clientes(diccionario):

    lista_temporal = []

    for nombre_completo, edad in diccionario.items():
        apellidos, nombre = nombre_completo.split(", ")
        lista_temporal.append((nombre, apellidos, edad))
    lista_temporal.sort()

    for nombre, apellidos, edad in lista_temporal:
        print(f"{nombre} {apellidos} ({edad})")


def añadirCliente(nombre, apellido, edad):
    nomCompleto = apellido + ", " + nombre
    clientes[nomCompleto] = edad
    return clientes

def añadirAño (nombre, apellido):
    i = 0
    nomCompleto = apellido + ", " + nombre
    for i in clientes.items():
        if nombre == clientes[i]:
            break
    


añadirCliente("Tomas", "Turbado",34)
mostrar_clientes(clientes)
añadirAño("Tomas","Turbado")
mostrar_clientes(clientes)
