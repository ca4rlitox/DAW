#si igualo lista2 a lista1 no creo una copia, si no que ambas apuntan a la misma lista, a la misma posicion de la memoria
lista1=[1,2]
lista2=lista1
lista2[0]=lista2[0]*5
print(lista2)
print(lista1)

#si quiero copiar una lista se pude con el metodo COPY

lista1=[1,2]
lista2= lista1.copy()
lista2[0]=lista2[0]*5
print(lista2)
print(lista1)
