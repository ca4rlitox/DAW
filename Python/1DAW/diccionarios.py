#La diferencia de diccionario es el uso de key  y value
diccionario={}#diccionario vacio
diccionario2=dict()# otro forma de crear diccionario vacio
liga={"Real Madrid":1,"Barcelona":2,"Atletico":3}#diccionario con key y value,las key son los nombres de los equipos y los value son los puntos que tienen
print(liga)# mostraria {'Real Madrid': 1, 'Barcelona': 2, 'Atletico': 3}
print(liga["Real Madrid"])# mostraria 1 q es el valor de la key "Real Madrid" -- en caso de que no exista se produce un error
print(liga.get("Real Madrid","No existe"))# mostraria 1 q es el valor de la key "Real Madrid" -- en caso de que no exista la key mostraria No existe
print(liga.keys())# mostraria ['Real Madrid', 'Barcelona', 'Atletico']

for equipo in liga:#mostraria los equipos
    print(equipo)

for puntos in liga.values():#mostraria los puntos
    print(puntos)

for equipo,puntos in liga.items():#mostraria los equipos y los puntos
    print(equipo,puntos)

liga['Barcelona'] = 44

for equipo,puntos in liga.items():#mostraria los equipos y los puntos
    print(liga)

 # liga.clear() #Esto borra el diccionario entero
 # liga.pop("clave") #Esto elimina contenido del diccionario. Si pongo algo que no existe, provocaria una excepcion.
 # liga.popitem() #Elimina el ultimo elemento introducido en el diccionario.
 # liga.update() se añade un diccionario sobre otro diccionario.
