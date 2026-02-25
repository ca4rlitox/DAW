"""Pedir una contraseña y validar que:
    -tenga al menos 8 caracteres
    -incluya una mayúscula
    -incluya un número"""

contrasenia=input("Ingrese una contraseña\nDebe tener al menos 8 caracteres sin espacios "
                  "incluir una mayúscula y un número:\n")

contraseniaValida=False
mayus=0
digit=0
espacio=0
while(contraseniaValida==False):
    if len(contrasenia)>=8:
        for caracter in contrasenia:
            if caracter==' ':
                espacio+=1
            if 'A'<=caracter<='Z':
                mayus+=1
            if caracter.isdigit():
                digit+=1
    if mayus==1 and digit==1 and espacio==0:
        contraseniaValida=True
    else:
        contrasenia=input("La contraseña ingresada no es válida\n"
              "Ingrese una contraseña\nDebe tener al menos 8 caracteres sin espacios "
              "incluir una mayúscula y un número:\n")
        espacio=0
        mayus=0
        digit=0
print("Contraseña validada")

