#INTERSECCION '&' - 'intersection'
profes1 = {"Yago","Natalia","José María","Paul","Eduardo","Javier"}
profes2 = {"Natalia","Puche","José María","Ana María","Israel"}

profesComun=profes1 & profes2 #interseccion que nos devuelve los elementos comunes, que estan tanto en uno como en otro
print(profesComun)

print(profes1.intersection(profes2))

#UNION '|' - 'union'

profesDAM = profes1 | profes2 #union que nos devuelve los elementos que estan en uno o en otro o en ambos pero sin repeticiones
print(profesDAM)

print(profes1.union(profes2))


#EXCLUSIVE OR (OR exclusivo) '^' - 'symmetric_difference'

profesEnUnoOEnOtroNoenLosDos=profes1 ^ profes2 #nos devuelve los elementos que estan en uno o en otro pero no en ambos
print(profesEnUnoOEnOtroNoenLosDos)

print(profes1.symmetric_difference(profes2))


#DIFERENCIA '-' - 'difference'
print(profes1 - profes2) #nos devuelve los profesores de primero que no estan en segundo
print(profes2 - profes1) #nos devuelve los profesores de segundo que no estan en primero
print(profes1.difference(profes2))

print(profes2.difference(profes1))