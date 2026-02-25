"""
1. Escribir un programa que nos pida tres palabras por teclado en cualquier orden y nos
las muestre en pantalla ordenadas alfabeticamente en orden ascendente
"""
"""
palabra1=input("Introduce una palabra: ")
palabra2=input("Introduce otra palabra: ")
palabra3=input("Introduce otra palabra mas: ")

if(palabra1<palabra2 and palabra2<palabra3):
    print(palabra1,palabra2,palabra3)
elif(palabra1<palabra3 and palabra3<palabra2):
    print(palabra1,palabra3,palabra2)
elif(palabra2<palabra1 and palabra1<palabra3):
    print(palabra2,palabra1,palabra3)
elif(palabra2<palabra3 and palabra3<palabra1):
    print(palabra2,palabra3,palabra1)
elif(palabra3<palabra1 and palabra1<palabra2):
    print(palabra3,palabra1,palabra2)
elif(palabra3<palabra2 and palabra2<palabra1):
    print(palabra3,palabra2,palabra1)
"""
"""
2. Idem al anterior pero ordenando ahora en orden descendente
"""
"""
palabra1=input("Introduce una palabra: ")
palabra2=input("Introduce otra palabra: ")
palabra3=input("Introduce otra palabra mas: ")

if(palabra1>palabra2 and palabra2>palabra3):
    print(palabra1,palabra2,palabra3)
elif(palabra1>palabra3 and palabra3>palabra2):
    print(palabra1,palabra3,palabra2)
elif(palabra2>palabra1 and palabra1>palabra3):
    print(palabra2,palabra1,palabra3)
elif(palabra2>palabra3 and palabra3>palabra1):
    print(palabra2,palabra3,palabra1)
elif(palabra3>palabra1 and palabra1>palabra2):
    print(palabra3,palabra1,palabra2)
elif(palabra3>palabra2 and palabra2>palabra1):
    print(palabra3,palabra2,palabra1)
"""
"""
3. Escribir un programa que pida un número por teclado al usuario que simule ser el
precio de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado
debe de estar redondeado a dos decimales.
"""

#precio=float(input("Introduce el precio para sumarle el IVA "))

#precioIva=round((precio*1.21),2)
#print(precioIva)

"""
4. Escribir un programa que nos pida por teclado dos calificaciones numéricas de un
alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las
notas introducidas deben de estar entre 0 y 10 y admiten decimales. Caso de que una
entrada sea errónea debería de advertirnos de ello y no hacer el cálculo
"""

nota1=float(input("Escribe la primer calificacion (entre 1 y 10) "))
nota2=float(input("Escribe la segunda calificacion (entre 1 y 10) "))

while ((nota1 <1 or nota1 >10) or (nota2 <1 or nota2 >10)):
    print("la nota no puede ser mayor a 10 o menor a 1 vuelve a ingresar")
    nota1=float(input())
    nota2=float(input())

media=round(((nota1+nota2)/2),)
print("la nota media es ",media)