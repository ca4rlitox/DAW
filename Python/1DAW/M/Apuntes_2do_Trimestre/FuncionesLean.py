def suma(a,b):
    return a+b
def miFuncion() :
    return 5,6,7,10 # puede devolver varios valores
nombre,edad,sueldo,horas=miFuncion() #asigno los valores devueltos por la funcion a variables
#Funciones con parametro por defecto
def saludo (nombre,forma="buenos dias"):
    print(f"{forma} {nombre}")
saludo("Arturo")
saludo("Arturo","buenas tardes")
saludo("Arturo","Buenas noches")


#Funciones con un numero variable de parametros
def media(*numeros):#recibe una tupla de numeros ,con el asterisco hago que reciba un numero variable de parametros
    return sum(numeros)/len(numeros)
print(media(1,2,3,4,5))
print(media(1,2,3,4,5,6,7,8,9))
#Otro ejemplo funciones con un numero variable de parametros
def notaAlumno(nombre,*notas):#para que la funcion acepte un numero variable de parametros simpre debe ser el ultimo parametro
    return nombre,sum(notas)/len(notas)
print(notaAlumno("Arturo",5,6,7,8,9))
print(notaAlumno("Ana",10,9,8,7))
#Como comentar funciones
def funcion(cantidad:int,precio:float,text:str)->int:
    """Esta funcion devuelve el doble de la cantidad"""
    total=cantidad*2
    return total

print(funcion(5,1.9,"dolares"))



