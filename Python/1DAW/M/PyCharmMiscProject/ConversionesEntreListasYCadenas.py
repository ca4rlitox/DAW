#podemos convertir un string en una lista y una lista en un string

nombres = ["Manuel", "pepe", "Luis", "Maria"]

numeros=[23,14.5,7,123,5,67]

texto=str(nombres) #convierto la lista en un string
print(texto) #ya no es una lista, es una cadena de texto (puedo manipularla)
texto=texto.replace('[','') #reemplazo los corchetes por espacio
texto=texto.replace(']','')
print(texto) #aqui vemos que ya no tiene los corchetes

#SPLIT
cadena = "En un lugar de la Mancha"
lista = cadena.split() #por defecto separa por done hay espacios
print(lista) #aqui vemos que es una lista

ip= "192.168.5.5"
listaIP = ip.split(".") #me crea una lista separada por los .
print(listaIP)

lista= list("Hola Mundo")  #convierto la cadena en una lista donde cada uno de los caracteres es un elemnto de la lista
print(lista)

