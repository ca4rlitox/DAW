#DICCIONARIOS
#Los diccionarios tampoco tienen orden, podemos distinguir dos elementos con un papel diferente
#Un elemento es lo que se llama clave (key) y el otro valor (value)
#La clave es lo que nos permite hacer una busqueda rapida. Nos ahorra recorrer los elementos uno a uno

#La clave no se puede repertir - Si pongo una clave repetida me la sobreescribe, no la duplica

#el elemento distintivo son las llaves {} podemos crearlos de estas formas:

diccionario={}

diccionario2= dict()

print(diccionario)
print(diccionario2)

#Crear diccionario con contenido:
liga= {'equipo1':34, 'equipo2':45, 'equipo3':14,} #tanto la clave como el valor puede ser cualquier tipo (int, str, lista, char, etc)

print(liga)

#Como puedo recuperar valores en los diccionarios
print(liga['equipo1']) #como en las listas para recuperar un índice pero con la clave no el índice, y recupero el valor
print(liga.get('equipo2')) #tambien existe el método get, si no se encuentra la clave devuelve "none" por defecto

print(liga.get('equipo22','esa clave no existe')) #el metodo get permite escribir un mensaje en caso de que no exista la clave


    #la clave es el equipo                    el valor es la lista
liga2={'equipo1':[0,0,0,0,0,0,0,0], 'equipo2':[0,0,0,0,0,0,0,0], 'equipo3':[0,0,0,0,0,0,0,0]}

#Como recorreer un diccionario (recordamos que no tienen orden)
#tengo distintas maneras de recorrerlos, para recuperar solo claves, para recuperar solo valores, y para recuperar ambos

#clave
for elemento in liga: #así solo recupero las claves del diccionario
    print(elemento)

#valor
for elemento in liga: #asi recupero los valores
    print(liga[elemento])

#clave y valor
for clave, valor in liga.items(): #asi recupero ambos, clave y valor
    print(clave,"puntos: ", valor)

#clave y valor
#(una segunda forma)
for elemento in liga:
    print(elemento, "-", liga[elemento])

#podemos obtener una lista con todas las claves del diccionario o bien una lista con todos los valores del diccionario

claves=list(liga.keys())
valores=list(liga.values())

print(claves)
print(valores)

#como se añaden elemento a un diccionario, como se modifican y como se eliminan

#MODIFICAR Y AÑADIR UN ELEMENTO (hay que recordar que las claves no pueden estar repetidas,los valores si)
#si añado un elemento nuevo y la clave de ese elemento ya existe lo que hace es sobreescribir la clave anterior con los valores nuevos

#asi añadimos
#en caso que no exista lo añade sin problema
liga['equipo4']=77
#en caso de que exista sobreescribe el valor
liga['equipo2']=22
print(liga)

personas={913285666: "Jose María", 666333444:"Manuel", 9456123564:"María"}
personas[913285666]="Ines"
personas[654212354]="Antonio"

print(personas)

telefono=611232456
personas[telefono]="Antionio"
print(personas)

#METODO CLEAR BORRA EL DICCIONARIO

liga2.clear()
print(liga2)

#para borrar SOLO UN ELEMENTO USAMOS POP

liga.pop("equipo2")
print(liga)

#si el parametro que le paso, osea el elemento no existe me provoca una excepcion
"""liga.pop("equipo22")"""
#por otro lado si le agrego un mensaje me imprime ese mensaje
valor=liga.pop("equipo22", "ese elemento no existe") #ademas pop nos devuelve solo el valor
print(valor)
print(liga)

valor=liga.popitem() #POPITEM borra y nos devuelve el último introducido
                    #pop item nos devuelve la clave y el valor
print(valor)

#FUCIONAR DICCIONARIOS
#Las claves duplicadas las sobreescribe por los valores del diccionario añadido (osea del segundo)
#Las claves que no estén duplicadas nos los añade
print(liga)
supercopa={'equipo6':11,'equipo1':55,'equipo4':33}

liga.update(supercopa)
print(liga)

#puedo tambien copiar el diccionario para luego modificar el nuevo y mantener el diccionario anterior con los valores anteriores
nuevaLiga=liga.copy()

nuevaLiga.update(supercopa)
print(supercopa)
print(nuevaLiga)



