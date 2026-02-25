vector=[] #inicializamos un vector, nombre del vector, = , corchetes indica que es array>>vector es sinonimo de array-- este es un vector vacio
#EN PYTHON SE LLAMAN LISTAS
vector2 = [1,2,3] #vector con tres numeros enteros
estudiantes = ["Ana","Pepe","Juan"] #vector de 3 Strings

fichaPersonal = ["Manuel", "Rey Laguarde", 29, True, 1200.45] #puede tener el tipo de dato que quiera

"""print(fichaPersonal)#puedo mostrar el vector entero
print(fichaPersonal[2]) #imprime la edad"""

#COMO RECORRO EL CONTENIDO: POR ELEMENTOS DE LA LISTA

"""for elemento in fichaPersonal: #elemento es el nombre que le pongo a cada lugar que ocupa el vector
    print(elemento) #imprime el contenido de cada posicion"""

#POR POSICION Y ELEMENTO (tengo el elemento y la posicion que ocupa en el array
"""
for i, elemento in enumerate(fichaPersonal): #utilizo la funcion enumerate para  -- tengo que separar las variables con coma
    print(i, "-", elemento)
"""
#POR POSICION Y ELEMENTO pero con
"""
for i in range(len(fichaPersonal)): #range toma los valores desde el primer valor hasta el ultimo -1 -- es el mas versátil
    print(i, "-", fichaPersonal[i]) #con range puedo invertir el orden del vector (revisar con cadenas de texto)
"""
"""
for i in range(len(fichaPersonal)-1,-1,-1): #el ultimo parametro es el paso, incremento o decremento // termina en -1 porque es el valor anterior a 0 (y -1 no esta incluido)
    print(i, "-", fichaPersonal[i]) #usamos len porque en principio yo no se el tamaño del vector
"""
"""print(fichaPersonal[-1]) #asi me imprime el contenido del ultimo valor de mi array"""

#MODIFICAR EL ARRAY

"""fichaPersonal[-1]=1300.50 #cambio el ultimo elemento del array por otro valor, puede ser cualquiera, que tenga que ver o no
print(fichaPersonal)"""



