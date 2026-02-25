precio = 75.5 #el signo igual es de asignacion, le asigno 75.5 al precio del producto
pvp = precio + (precio * 0.21) #pvp es precio para venta al publico
print (pvp)

#print (precio + (precio * 0.21))

#   "%" es el resto de la division entera
#   "//" es el cociente de la division entera (no existe en Java)

print (5%2)
print(5//2)

""" operadores de asignacion 

+= -> x= x+1 -> x+=1
-=
*=
/= -> y= y/2 -> y/= 2
%=
//= -> no existe en Java

++ y -- no existen en Python

"""
radio = 2.5
PI = 3.14159
area = PI * radio * radio
longitud = 2 * PI * radio

print("el area de la circunferencia de radio", radio, "es" , area) #hay que separar los elementos (las variables y cadenas) con comas ,
print("la longitud es: ", longitud)

#parametros
# end ->se pone al final de la linea de print para que el siguiente print este a continuacion del texto y no un salto de linea
# sep -> se pone al final y actua en las separaciones de las comas

print("el area de la circunferencia de radio", radio, "es", end= " ")
print(area)

print("el area de la circunferencia de radio", radio, "es", sep= "      ") #en este caso el sep da mas espacio entre en donde estan las comas
print (area)

print("el area de la circunferencia de radio", radio, "es", end= " ", sep= " - ") #combinamos los dos (siempre al final)
print (area)

# \n -> salto de linea

print("el area de la circunferencia \nde radio", radio, "es    ", end= " ")
print (area)

