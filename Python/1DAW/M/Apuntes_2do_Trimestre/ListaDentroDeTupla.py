
tupla1=(1,"Ana",[1,2,3]) #tupla con una lista. Puedo modificar la lista porque es una referencia a la ubicacion de la lista
print(tupla1)

tupla1[2].append(7) #agrego un 7 a la lista dentro de la tupla
print(tupla1)

#para las tuplas funcionan los mismos recorridos que las listas (con for) y los metodos como count() y index(), o los emparedados
#Mientras no alteren el orden y el contenido de las tuplas funcionan todos

