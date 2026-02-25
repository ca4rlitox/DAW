"""
5. Escribir un programa que nos pida las notas obtenidas en un trimestre y nos muestre
la media ponderada sabiendo que;
1. La primera nota corresponde al trabajo en clase y cuenta como un 5% del total
2. La segunda corresponde a los ejercicios prácticos: 15%
3. La tercera la nota del examen: 80%
El resultado debería de mostrarse de dos formas: redondeado con dos decimales
(nota real) y sin redpmdeada sin decimales (nota de boletín).
"""
"""
nota1=float(input("Ingrese la nota correspondiente al trabajo en clase: "))
nota2=float(input("Ingrese la nota correspondiente a los ejercicios prácticos: "))
nota3=float(input("Ingrese la nota correspondiente al examen: "))


notaReal=round(((nota1*0.05)+(nota2*0.15)+(nota3*0.8)),2)
notaBoletin=round(((nota1*0.05)+(nota2*0.15)+(nota3*0.8)),)

print("la nota real es: ",notaReal)
print("la nota del boletín es: ",notaBoletin)
"""
"""
6. Modifica el ejercicio anterior para que la nota del boletín se redondee
matemáticamente si es superior a 5 pero se trunquen los decimales si es inferior a 5
"""
"""
if (notaBoletin>=5):
    print(round(notaBoletin),)
else:
    print(int(notaBoletin))
"""

"""
7. Escribir un programa que pida un número por teclado y nos imprima la tabla de
multiplicar de dicho número del 1 al 10. Por ejemplo, si introducimos el 74 el
resultado será algo así:
74 x 1 = 74
74 x 2 = 148
…
74 x 10 = 740
"""

"""
num=int(input("Escribe un número para conocer su tabla de multiplicar: "))

for i in range(1,11):
    print(num,"x",i,"=",num*i)
"""


"""
8. Escribe un programa que pida un número por teclado y escriba todos sus divisores
separados por comas (y evitando poner una coma al final). Por ejemplo, si el número
introducido es el 14 tu programa debería de mostrar lo siguiente:
Divisores del número 14: 1, 2, 7, 14
"""
num=int(input("Ingrese un número: "))

for i in range(1,num):
    if(num%i==0):
        print(i,end=",")
print(num)