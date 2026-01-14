def numeroExcesivo(num):
    sumaDivisores = 0
    for i in range(1,num,-1):
            if num % i == 0:
                sumaDivisores+=i
            print(i)

    print(sumaDivisores)

def ejercicio3():
    numero = int(input("Introduce un numero: "))
    numeroExcesivo(numero)


ejercicio3()

