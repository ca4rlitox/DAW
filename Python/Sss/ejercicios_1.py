# Soluciones simples en Python — Ejercicios 1–25
# Cada ejercicio está en una función independiente (ej1, ej2, ... ej25).
# Ejecuta la función que quieras probar. Todas usan solo la librería estándar.

import random
import math

# 1. Mostrar los 10 primeros números enteros
def ej1():
    for i in range(1, 11):
        print(i)

# 2. Mostrar los 50 primeros números pares
def ej2():
    for i in range(2, 2*50 + 1, 2):
        print(i)

# 3. Mostrar los 5 primeros múltiplos de un número dado por el usuario
def ej3():
    n = int(input("Número: "))
    for i in range(1, 6):
        print(n * i)

# 4. Mostrar todos los números divisibles por 7 menores a 10000
def ej4():
    for i in range(7, 10000, 7):
        print(i)

# 5. Pedir un número y decir si es par o impar
def ej5():
    n = int(input("Número: "))
    print("par" if n % 2 == 0 else "impar")

# 6. Pedir un número y decir si es divisible por 3
def ej6():
    n = int(input("Número: "))
    print("divisible por 3" if n % 3 == 0 else "no divisible por 3")

# 7. Precio con IVA 21%
def ej7():
    precio = float(input("Precio (€): "))
    total = precio * 1.21
    print(f"Total con IVA (21%): {total:.2f} €")

# 8. Prorrateo de pago sin intereses, redondeado a 2 decimales
def ej8():
    importe = float(input("Importe total (€): "))
    meses = int(input("Meses: "))
    cuota = importe / meses
    print(f"Cuota mensual: {cuota:.2f} €")

# 9. Número aleatorio entre 0 y 50
def ej9():
    print(random.randint(0, 50))

# 10. Dos dados (1..6)
def ej10():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(d1, d2)

# 11. Tirar dos dados hasta que salgan iguales, mostrar nº de tiradas
def ej11():
    tiradas = 0
    while True:
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        tiradas += 1
        if d1 == d2:
            break
    print(f"Tardó {tiradas} tiradas en salir {d1} y {d2} iguales.")

# 12. Asistente de rol: n dados de m caras
def ej12():
    n = int(input("Número de dados: "))
    caras = int(input("Número de caras (4,6,8,12...): "))
    tirada = [random.randint(1, caras) for _ in range(n)]
    print("Tirada:", *tirada)

# 13. Como el anterior, pero solo admite nº de caras par
def ej13():
    n = int(input("Número de dados: "))
    while True:
        caras = int(input("Número de caras (par): "))
        if caras % 2 == 0:
            break
        print("Error: el número de caras debe ser par.")
    tirada = [random.randint(1, caras) for _ in range(n)]
    print("Tirada:", *tirada)

# 14. Aleatorio entre dos números dados (asumiendo orden correcto)
def ej14():
    a = int(input("Límite inferior: "))
    b = int(input("Límite superior: "))
    print(random.randint(a, b))

# 15. Como el anterior pero aceptando cualquier orden
def ej15():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    lo, hi = (a, b) if a <= b else (b, a)
    print(random.randint(lo, hi))

# 16. Seis números aleatorios 1..49 (con repetición)
def ej16():
    nums = [random.randint(1, 49) for _ in range(6)]
    print(*nums)

# 17. Quiniela: 15 resultados (1, X, 2)
def ej17():
    res = []
    for _ in range(15):
        n = random.randint(1, 3)
        res.append("X" if n == 3 else str(n))
    print(" ".join(res))

# 18. Generar números 1..1000 hasta que salga 666; contar los anteriores
def ej18():
    cuenta = 0
    while True:
        n = random.randint(1, 1000)
        if n == 666:
            break
        cuenta += 1
    print(f"¡Faltan {cuenta} días para que se acabe todo!")

# 19. Pedir un número y mostrar sus divisores
def ej19():
    n = int(input("Número (>0): "))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

# 20. Pedir 3 números y mostrarlos ordenados de menor a mayor
def ej20():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print(sorted(a, b, c))

# 21. Comprobar si un número es primo
def es_primo(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def ej21():
    n = int(input("Número: "))
    print("primo" if es_primo(n) else "no primo")

# 22. Primo aleatorio entre 10_000_000 y 50_000_000
def ej22():
    lo, hi = 10_000_000, 50_000_000
    while True:
        n = random.randint(lo, hi)
        if es_primo(n):
            print(n)
            return

# 23. Todos los primos entre 1 y 100
def ej23():
    for n in range(2, 101):
        if es_primo(n):
            print(n)

# 24. Primos entre dos números dados por el usuario (en cualquier orden)
def ej24():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    lo, hi = (a, b) if a <= b else (b, a)
    for n in range(lo, hi + 1):
        if es_primo(n):
            print(n)

# 25. Dividir sucesivamente entre 2 hasta <= 1, mostrando con 2 decimales si hace falta
def ej25():
    valor = float(input("Número: "))
    print(f"Has introducido el número {int(valor) if valor.is_integer() else valor}")
    while valor > 1:
        valor = valor / 2
        if valor.is_integer():
            print(int(valor))
        else:

