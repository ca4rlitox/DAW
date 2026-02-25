"""1. Escribir un programa que pida una contraseña por teclado (dos veces) y si no
coinciden nos lo vuelva a pedir hasta que lo hagan
"""
"""
contrasenia=input("Ingrese una contraseña: ")
confirmacion=input("Vuelve a introducir la contraseña (debe coincidir con la anterior): ")

while contrasenia!=confirmacion:
    contrasenia=input("Las contraseñas no coinciden, por favor vuelve a ingresarlas: ")
    confirmacion=input("Confirma la contraseña: ")

print("Contraseña guardada correctamente")
"""
"""2. Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
informe del número de intentos inválidos
"""
"""
contrasenia=input("Ingrese una contraseña: ")
confirmacion=input("Vuelve a introducir la contraseña (debe coincidir con la anterior): ")
intentos= 0
while contrasenia!=confirmacion:
    contrasenia=input("Las contraseñas no coinciden, por favor vuelve a ingresarlas: ")
    confirmacion=input("Confirma la contraseña: ")
    intentos+=1

print("Contraseña guardada correctamente")
print(intentos," intentos invalidos")
"""
"""
3. Escribir un programa que nos pida nuestro nombre y apellidos (dos peticiones
diferentes hechas en ese orden) y nos lo escriba formateado de la siguiente forma:
Morales Vázquez, José María
"""
"""
nombre=input("Ingrese su nombre: ")
apellidos=input("Ingrese sus apellidos: ")

print(apellidos,", ",nombre)
"""
"""
4. Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
que ha encontrado y suprimido.
"""
"""
texto=input("Ingrese una cadena de texto: ")
espacios=texto.count(" ")
print(texto.replace(" ",""))
print(espacios)
"""

"""
5. Escribir un programa que pida por teclado una cadena de texto y la imprima escrita al
reves (es decir, si el usuario escribe Hola Mundo el programa debería de escribir
odnuM aloH)"""

texto=input("Ingrese una cadena de texto: ")
print(texto[::-1])