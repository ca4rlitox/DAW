""". Queremos crear una función que valide la fortaleza de una contraseña. La función recibirá
como argumento una cadena de texto y hará un análisis diciendo la longitud, el número de
letras mayúsculas, el número de letras minúsculas, el número de cifras y el número de otros
caracteres diferentes que tiene la contraseña y presentará estos datos en consola. Cada uno
de los elementos antes enumerados se calculará con una función diferente"""

contrasenia=input("Ingrese una contraseña: ")

def longitud(contrasenia):
    return len(contrasenia)

def letrasMayusculas(contrasenia):
    cont=0
    for letra in contrasenia:
        if letra.isupper():
            cont+=1
    return cont

def letrasMinusculas(contrasenia):
    cont=0
    for letra in contrasenia:
        if letra.islower():
            cont+=1
    return cont

def cifras(contrasenia):
    cont=0
    for cifra in contrasenia:
        if cifra.isdigit():
            cont+=1
    return cont

def otrosCaracteres(contrasenia):
    cont=0
    for caracter in contrasenia:
        if not caracter.isdigit() and not caracter.isalpha():
            cont+=1
    return cont

print("Longitud de la contraseña: ",longitud(contrasenia))
print("Cantidad de mayúsculas: ",letrasMayusculas(contrasenia))
print("Cantidad de minúsculas: ",letrasMinusculas(contrasenia))
print("Cantidad de cifras: ",cifras(contrasenia))
print("Cantidad de carácteres especiales: ",otrosCaracteres(contrasenia))