"""texto = "Hola mundo"
texto = "Adios mundo"
texto = texto + " cruel" #la cadena no puede modificarse, se le puede asignar (concatenar) mas cosas
print (texto)
texto[2] = "x" #no puedo modificar el segundo indice, (el tercer caracter)
print(texto)"""

"""texto = "Hola mundo cruel"
print(texto[2])
print(texto[2:8])#recupero el trozo de la cadena que va desde el indice dos hasta el 8 (el 8 excluido)
print(texto[:8])#me toma desde el comienzo hasta el indice 8
print(texto[2:])#me toma desde el indice 2 hasta el final
subtexto=(texto[2]+texto[6])#es una manera para seleccionar dos indices (indice 2 e indice 6)
print(subtexto)

print(texto[2:8:2])#va del indice 2 al 8 pero de dos en dos

print(texto[-4:])#imprime los ultimos 4 indices de la cadena

print(texto[::-1])#me muestra la cadena desde el primer indice hasta el ultimo pero al reves, va descontando (-1)

for caracter in texto: #me recorre toda la cadena imprimiendo uno a uno los caracteres
    print(caracter)

print(len(texto)) # "len" me devuelve la longitud de la cadena

for posicion in range (0,len(texto)): #asi puedo ver que posicion tiene cada caracter en la cadena
    print(posicion,"-", texto[posicion])
"""

valor = 345
valorTexto = str(valor) #str es una funcion que convierte el objeto "valor" en cadena

print(valorTexto[1]) #puedo controlar mejor ese número, por ejemplo se que un telefono tiene tantos digitos asi puedo corroborar que
                    #para que un dato sea un telefono tenga tantos dígitos
"""
texto="Hola mundo"
print(texto.upper()) #el metodo upper convierte todo a mayúsculas. los metodos van despues de la variable y dos parentesis y las funciones antes

print(texto)#el metodo no cambia el objeto, el objeto sigue siendoo el mismo solo que lo convierte en mayúsculas.

print(texto.swapcase())#este metodo cambia mayusculas a minusculas y biseversa, minusculas a mayusculas

print("Hola a todos los de DAW1".upper()) #el metodo lo puedo poner directamente en la variable

print(texto[1:6].upper())#en este caso me mostrara solo los caracteres entre esos indices pero en mayusculas"""
"""
texto="Hola mundo"

print(texto.find("la"))#el metodo find, busca si la porcion de texto (en este caso) y muestra cuantas coincidencias hay
print(texto.find("o",3,8)) #aca busca la "o" pero comienza desde la posicion 3 y finaliza en la 8
                                            #de otra forma solo muestra la primer o que aparece solamente
                                            #devuelve -1 porque no hay ninguna

print(texto.count("o"))#cuenta cuantas "o" aparecen en el texto, si no hay devuelve 0

print(texto.replace("o", "***")) #este metodo remplaza un caracter (en este caso la "o") por lo que pongamos nosotros ("***")
"""
