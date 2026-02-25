#isdigit es un metodo
#isalpha es un metodo
#existen para no tener que generar una excepcion, sirven en ciertos casos particulares

#ejemplo con isdigit
edad=input("Introduce tu edad: ")
if edad.isdigit()==True: #si lo que ingresamos isdigit puede convertirlo a entero el programa funciona, sino si se evalua como false nos devuelve el otro mensaje
    edad=int(edad)
    print ("En tu proximo cumpleaños tendras: ", edad + 1)
else:
    print("Lo que has escrito no puede ser tu edad")


#str
precio = float(input("Escribe el precio: "))
precioTXT = str(precio) #con este metodo convertimos el float en cadena de texto
print("El precio convertido a texto es: ", precioTXT) #se mostrara lo mismo pero es una cadena de texto

#contar cuantas cifras, o cuantos decimales, tiene un numero (mucho mas sencillo si es cadena de texto)
