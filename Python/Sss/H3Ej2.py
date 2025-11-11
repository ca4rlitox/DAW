# Escribir un programa que nos pida nuestro nombre y apellidos (dos peticiones
# diferentes hechas en ese orden) y nos lo escriba formateado de la siguiente forma:

nombre = input("Indica tu nombre.\n")
apellidos = input("Introduce tus apellidos.\n")

print(apellidos,nombre,sep=", ")