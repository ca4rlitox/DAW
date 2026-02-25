#Utilizacion de f String
# f (de formato) le da un formato especial a la cadena
#imprime con formato

lenguaje="python"
alumno= "Pepe"
edad= 24
print("Hola, me llamo",alumno,"tengo",edad,"años y estoy estudiando",lenguaje) #esta es la manera que veníamos trabajando hasta ahora

#otra forma pero todavia sin usar f String
print("Hola, me llamo %s tengo %d años y estoy estudiando %s"%(alumno,edad,lenguaje)) #s de string , d para numero entero, f para float
#ponemos la variables entre paréntesis en orden de como van apareciendo en la cadena, con su tipo correspondiente, y tiene que ser la misma cantidad sino me da un error


#las f string llevan una f delante de las comillas
print(f"Hola, me llamo {alumno} tengo {edad} años y estoy estudiando {lenguaje}") #va todo entre comillas y las variables entre comillas
#es el formato de impresion mas comodo en python, sobre todo cuando mezclamos texto con variables

#PROPIEDADES CON F STRING

n1=34.567
n2=123.555467
print(f"Los números son {n1:.2f} y {n2:.2f}") #dentro de la variable pongo dos puntos para especificar que modificaremos esa variable
#en este caso redondea con 2 decimales y si el número no tiene decimales lo completa

#porcentajes
n3=0.34
n4=0.5555014789

print(f"Los porcentajes son {n3:.2%} y {n4:.2%}") #aca nos conviete a porcentaje y respeta los dos decimales y el redondeo

#separador de miles

poblacion=1546545456
print(f"la poblacion del pais es de {poblacion:,} habitantes") #nos da el formato separado por comas donde dividen los mil


#para mejorar como se imprime una lista, de manera tabulada y mejor visualmente
lista=[234,45,765,6,562,33,1245,56]

for n in lista:
    print(f"{n:5d}") #salida tabulada en columnas, le indicamos el número de cifras que nos corre a la derecha, si le pongo menos desordena un poco el formato pero se puede hacer

#y si tuvieramos decimales....
print()
lista=[234,45.55,765,6.1,562,33.134,1245,56.1234]

for n in lista:
    print(f"{n:7.2f}") #el primer número es el total de caracteres que tabula, y la otra pate redondea como antes, no influye en la longitud de tabulado

print()

#aca delimitamos un espacio dentro de la variable
print(f"A la izquierda: ***{lenguaje:<20}***") #con : y <20 se entiende que formatea 20 caracteres a la izquierda

#a la derecha
print(f"A la derecha: ***{lenguaje:>20}***")

#y centrado (centra el contenido de la variable)
print(f"A la centrado: ***{lenguaje:^20}***") #la longitud total sera 20, lo que ocupa "python" y lo que sobre seran espacios

print()

#el fString no hay porque ponerlo dentro del print, es una variable de tipo cadena, puedo utilizarlo como un string

cadenaConFormato=f"A la centrado: ***{lenguaje:^20}***"
print(cadenaConFormato)
#Imprimir varias filas, potente para hacer fichas

nombre="Manuel"
apellidos="Rey Laguarde"
telefono= 12345644
libro="El hobbit"
fechaDecolucion="12/03/2026"

#cuando es en varias lineas pongo tres comillas """
fichaLibro= f""" 
Nombre: {nombre}
Apellidos: {apellidos}
Teléfono: {telefono}
Libro: {libro} - Fecha de devolución - {fechaDecolucion}
"""
print(fichaLibro)


#que hacemos cuando queremos imprimir una { en una fString?????
print(f"A {{la}} derecha: ***{{{lenguaje:>20}}}***") #lo duplicamos si es parte del texto, y lo triplicamos si es una variable