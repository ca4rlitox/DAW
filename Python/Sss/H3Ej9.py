# Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
# Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
# nuestro destino (París, Roma, Santiago de Chile o Tokio)

print("Elige un destino turístico:")
print("1. Francia")
print("2. Italia")
print("3. Chile")
print("4. Japón")

destino = input("Introduce tu destino: ")

if destino.lower() == "francia":
    print("La capital de Francia es París.")
elif destino.lower() == "italia":
    print("La capital de Italia es Roma.")
elif destino.lower() == "chile":
    print("La capital de Chile es Santiago de Chile.")
elif destino.lower() == "japón" or destino.lower() == "japon":
    print("La capital de Japón es Tokio.")
else:
    print("Destino no reconocido.")
