"""1. Escribir un programa que pida un número por teclado y calcule su factorial. Como
sabes, la factorial de un número se calcula multiplicando ese número por los sucesivos
factores que obtenemos restando uno hasta llegar a la unidad. Por ejemplo, el factorial
de 6 (que se representa así 6!) sería este:
6! = 6*5*4*3*2*1 = 720"""

num=int(input("Introduce un número para conocer su factorial "))
acumulador=1
for i in range(1,num+1):
    acumulador=acumulador*i

print(num,"!"," = ",acumulador,sep="")


