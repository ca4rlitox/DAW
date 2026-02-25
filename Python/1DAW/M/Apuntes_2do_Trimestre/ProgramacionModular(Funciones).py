#FUNCIONES

def miFuncion(x,y): #def es para definir la funcion, luego el nombre, y luego los parámetros
    return x+y #todo lo tabulado pertenece a la funcion

print(miFuncion(3,5))
print(miFuncion(3.33,5.5))
print(miFuncion("Hola","Mundo"))

#en python no se puede llamar a una funcion antes de definirla como en Java, porque lee de arriba hacia abajo

def miOtraFuncion(x : int,y : int,z : int) -> int: #es un comentario, una indicacion pero no afecta a la funcion (no es obligatorio que sea int)
    return x+y+z
    print(variable)
    variable=2

variable=555 #las variables definidas fuera de una funcion si pueden ser accedidas desde dentro
"""print(variable2)#las variables definidas dentro de una funcion no pueden ser accedidas desde fuera"""


#FUNCIONES CON VALORES DE RETORNO MULTIPLES
def miFuncion2():
    return "Jose María",57,2400.55

nombre, edad, sueldo = miFuncion2()
print(nombre, "-", edad, "-", sueldo)

def miFuncion3(x,y,lista):
    x= x+2
    y = y**2
    return x+y

x=5
y=3
lista=[1,2,3]
print(miFuncion3(x,y,lista))
print(x)
print(y)
print(lista)