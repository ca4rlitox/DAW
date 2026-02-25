import random
# Append añade un elemento a la ultima posicion de la lista array
enteros = [1,2,3,4,"gil","gil","gil","gil","gil","gil"]
enteros.append(33)

# Insertar elemento donde queramos.
# En index en la posicion que se quiere poner y object el valor que se quiere poner
enteros.insert(2,4)

# Tambien podemos concatenar las listas
masEnteros = [6,7,8]

todosJuntos = enteros + masEnteros
print(todosJuntos)
# También se puede hacer con la funcion extend
enteros.extend(masEnteros)
print(enteros)

# La funcion pop sin nada, coge el dato de la última posicion
# Si ponemos la posicion en la que está nos extrae el que está ahi
numero = todosJuntos.pop(3)
print(enteros)
print(numero)

# La funcion clear limpia la lista
todosJuntos.clear()
print(todosJuntos)

# La funcion remove para eliminar un determinado elemento de la lista, se pueden poner comillas o la posicion
# Solo borra la posicion dada o si se pone un valor repetido en la lista, borra el primero que haya, los de mas no
enteros.remove(2)
print(enteros)

# La funcion sort ordena la lista, tienen que ser int, float o string, no se pueden mezclar.
# Si ponemos en el paréntesis reverse=True, ponemos la lista descentente. Si no lo ponemos, ascendente
#enteros.sort()
print(enteros)
# Para strings, lo ordena alfabeticamente pero hay que tener cuidado con las mayusculas y minúsculas, ya que lo ordena segun esté, primero mayus

# Interrogar la lista con
if "pepe" not in todosJuntos:
    print("pepe no esta")
else:
    print("pepe está")

# Saber la posición
posicion = enteros.index("gil")
print(posicion)
# Contar los elementos repetidos
veces = enteros.count("gil")
print(veces)

# Para hacer numeros pares
secuencia = [i for i in range(2,50,2)]
print(secuencia)

secuencia = [random.randint(1,4) for _ in range (0,4)]
print(secuencia)

