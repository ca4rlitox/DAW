#IF / ELSE

import random

numero = 30

if numero < 20:  #en Python se ponen dos puntos ':' cuando empieza la estructura de control
    pass #instruccion que sirve para "pasar" de esta parte del codigo, en este caso evalua la condicion solamente del else (falso) y puedo precindir del if
    print("El número es menor a 20")  #y no hay llaves, para que funcione se tabula
    print("Es un numero muy pequeño")  #todo lo que este tabulado se considera parte de la estructura
else: #siempre poner los dos puntos :
    print ("El numero es mayor o igual que 20")

print("Fin del programa")

dado = random.randint(1,6) #abro los parentesis y pongo el valor separdo por comas y completa

""""
if dado <= 4:
    print("Has sacado un", dado, "has fallado")
else:
    print("Has sacado un", dado, "hecho daño")
"""

if dado >= 5:
    print("Has sacado un", dado, "has matado al monstruo")
elif dado >=3: #condicion adicional <- puedo poner todas las que quiera
    print("Has sacado un", dado, "hecho daño al monstruo")
else:
    print ("Has sacado un", dado, "has fallado")


#WHILE

numero = 1
while numero <=10:
    print(numero)
    numero+=1
print ("FIN")

# en python and, or, y not se ponen tal cual: and, or, not

