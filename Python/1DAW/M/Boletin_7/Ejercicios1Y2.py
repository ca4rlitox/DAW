"""Vamos a hacer una pequeña calculadora. Solicita dos números al usuario
y luego que escriba la operación que quiere hacer
(S para suma, R para resta, M para multiplicar y D para dividir).
Realiza la operación con un switch.
2. Incluye operaciones adicionales (raiz cuadrada, cuadrado, cubo, por ejemplo)
"""

opcion=input("Ingrese la operación que desea realizar: \n"
             "S para sumar, R para resta, M para multiplicar, D para dividir \n"
             "RA para raiz cuadrada, P2 para potencia de 2, P3 para potencia de 3 \n"
             "para terminar pulse 'T'\n")
while 't'!= opcion!='T':
    match opcion.upper():
        case 'S':
            num1 = int(input("Ingrese el primer número a sumar: "))
            num2 = int(input("Ingrese el segundo número a sumar: "))
            suma=num1 + num2
            print("El resultado es: ", suma)
        case 'R':
            num1 = int(input("Ingrese el primer número a restar: "))
            num2 = int(input("Ingrese el segundo número: "))
            resta=num1 - num2
            print("El resultado es: ", resta)
        case 'M':
            num1 = int(input("Ingrese el primer número a multiplicar:  "))
            num2 = int(input("Indique por cuanto quiere multiplicarlo: "))
            print("El resultado es: ", num1 * num2)
        case 'D':
            num1 = float(input("Ingrese el primer número a dividir: "))
            num2 = float(input("Ingrese por cuanto quiere dividirlo: "))
            dividir=num1 / num2
            print("El resultado es: ", round(dividir,2))
        case 'RA':
            num1 = int(input("Ingrese el número para conocer su raiz cuadrada: "))
            raiz=num1 ** 0.5
            print("El resultado es: ", round(float(raiz),2))
        case 'P2':
            num1 = int(input("Ingrese el número para elevarlo a la potencia 2: "))
            potencia2=num1 ** 2
            print("El resultado es: ", potencia2)
        case 'P3':
            num= int(input("Ingrese el número para elevarlo a la potencia 3: "))
            potencia3=num ** 3
            print("El resultado es: ", potencia3)
        case 'T':
            print("Has salido")
        case _:
            print("Opción no válida")
    opcion = input("Ingrese la operación que desea realizar: \n"
                   "S para sumar, R para resta, M para multiplicar, D para dividir \n"
                   "RA para raiz cuadrada, P2 para potencia de 2, P3 para potencia de 3 \n"
                   "para terminar pulse 'T'\n")
