"""
9. Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que
escribamos la palabra FIN (con mayúsculas). Si el usuario introduce una entrada
inválida (números superiores a 100, otras cadenas de caracteres que no sean FIN, etc.)
no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá
su curso. Cuando terminamos (al introducir la palabra FIN, recuerda) mostraremos
por pantalla el numero de entradas válidas que hemos hecho (sin contar esta última
que sólo sirve para finalizar el programa)
"""
"""
opcion=input("Ingresa los números que quieras entre el 1 y el 100. Para finalizar escribe 'FIN' ")

contador=0
while opcion!="FIN":
    if opcion.isdigit():
       #if 1 <= int(opcion) <= 100: <------ OPCION MEJORADA DE PYCHARM
        if int(opcion)>=1 and int(opcion)<=100:
            contador+=1
        else:
            print("error")
    else:
        print("error")
    opcion=input()
print(contador)
"""
"""
10. Modificar el programa anterior para que nos muestre al final la media aritmética de
las entradas válidas
"""
"""
opcion=input("Ingresa los números que quieras entre el 1 y el 100. Para finalizar escribe 'FIN' ")

contador=0
suma=0
while opcion!="FIN":
    if opcion.isdigit():
       #if 1 <= int(opcion) <= 100: <------ OPCION MEJORADA DE PYCHARM
        if int(opcion)>=1 and int(opcion)<=100:
            contador+=1
            suma=suma+int(opcion)
        else:
            print("error")
    else:
        print("error")
    opcion=input()
print(contador)
print("la media es ",suma/contador)
"""

"""
11. Modificar el programa anterior para que, además, nos diga al final cual han sido el
número mayor y el menor que has introducido
"""

opcion=input("Ingresa los números que quieras entre el 1 y el 100. Para finalizar escribe 'FIN' ")

contador=0
suma=0
mayor=1
menor=1
while opcion!="FIN":
    if opcion.isdigit():
       #if 1 <= int(opcion) <= 100: <------ OPCION MEJORADA DE PYCHARM
        if int(opcion)>=1 and int(opcion)<=100:
            contador+=1
            suma=suma+int(opcion)
            if int(opcion)>mayor:
                mayor=int(opcion)
            elif int(opcion)<menor:
                menor=int(opcion)
        else:
            print("error")
    else:
        print("error")
    opcion=input()
print(contador)
print("la media es ",suma/contador)
print("el mayor es: ",mayor)
print("el menor es: ",menor)