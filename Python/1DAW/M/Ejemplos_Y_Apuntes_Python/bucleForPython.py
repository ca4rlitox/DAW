import random
"""
for i in range(0,5): #para i se le asignara un valor entre 0 y 5 pero el ultimo valor del rango no se cuenta, no esta incluido
    print(i)        #y yo se que se repetira 5 veces
print ("FIN")

for i in range (1,30):
    print(i)
print ("FIN")
"""

"""
for _ in range(1,4): #en python si no voy a usar la variable y solamente quiero ejecutar algo (en este caso 3 veces) pongo un "_"
    dado = random.randint(1,6)
    print (dado)
print ("FIN")
"""

"""
texto= "HOLA"
for caracter in texto: #para la variable texto voy a imprimir cada caracter por vuelta
    print(caracter)
print("FIN")
"""

"""
for i in range(1,10,2): #puedo poner un tercer parametro que en este caso saltea de 2 en 2 los numeros del 1 al 9
    print(i)
print ("FIN")
"""

for i in range(100,0,-2): #tambien puedo hacerlo de manera decreciente
    print(i)
print("FIN")