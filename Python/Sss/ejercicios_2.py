# Soluciones simples en Python — Ejercicios genéricos de programación 2
# Cada ejercicio es una función: ej1(), ej2(), ..., ej18().
# Ejecuta la que quieras probando desde el bloque __main__ al final.

import random
import math

# 1. Tres palabras y mostrarlas en orden alfabético ascendente
def ej1():
    p1 = input("Palabra 1: ")
    p2 = input("Palabra 2: ")
    p3 = input("Palabra 3: ")
    orden = sorted([p1, p2, p3], key=lambda s: s.lower())
    print(*orden, sep=", ")

# 2. Igual que el anterior pero descendente
def ej2():
    p1 = input("Palabra 1: ")
    p2 = input("Palabra 2: ")
    p3 = input("Palabra 3: ")
    orden = sorted([p1, p2, p3], key=lambda s: s.lower(), reverse=True)
    print(*orden, sep=", ")

# 3. Precio con IVA 21% (redondeado a 2 decimales)
def ej3():
    precio = float(input("Precio (€): "))
    total = round(precio * 1.21, 2)
    print(f"Total con IVA (21%): {total:.2f} €")

# 4. Media de dos notas (0..10). Si alguna es inválida, avisar y no calcular
def ej4():
    try:
        n1 = float(input("Nota 1 (0-10): "))
        n2 = float(input("Nota 2 (0-10): "))
    except ValueError:
        print("Entrada inválida.")
        return
    if not (0 <= n1 <= 10) or not (0 <= n2 <= 10):
        print("Entrada inválida.")
        return
    media = round((n1 + n2) / 2)
    print(f"Media (redondeada sin decimales): {int(media)}")

# 5. Media ponderada: 5%, 15%, 80%. Mostrar con 2 decimales y sin decimales (truncada)
def ej5():
    try:
        clase = float(input("Trabajo en clase (0-10): "))
        pract = float(input("Ejercicios prácticos (0-10): "))
        examen = float(input("Examen (0-10): "))
    except ValueError:
        print("Entrada inválida.")
        return
    real = clase * 0.05 + pract * 0.15 + examen * 0.80
    boletin = int(real)  # sin decimales (truncada)
    print(f"Nota real: {real:.2f}")
    print(f"Nota de boletín: {boletin}")

# 6. Como el anterior, pero si la real >= 5 se redondea; si <5 se trunca
def ej6():
    try:
        clase = float(input("Trabajo en clase (0-10): "))
        pract = float(input("Ejercicios prácticos (0-10): "))
        examen = float(input("Examen (0-10): "))
    except ValueError:
        print("Entrada inválida.")
        return
    real = clase * 0.05 + pract * 0.15 + examen * 0.80
    if real >= 5:
        boletin = int(real + 0.5)  # redondeo simple
    else:
        boletin = int(real)        # truncado
    print(f"Nota real: {real:.2f}")
    print(f"Nota de boletín: {boletin}")

# 7. Tabla de multiplicar 1..10
def ej7():
    n = int(input("Número: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# 8. Divisores separados por comas (sin coma final)
def ej8():
    n = int(input("Número (>0): "))
    divisores = [str(i) for i in range(1, n+1) if n % i == 0]
    print(f"Divisores del número {n}: " + ", ".join(divisores))

# 9. Pedir números 1..100 hasta escribir FIN. Contar entradas válidas.
def ej9():
    validos = 0
    while True:
        s = input("Número 1..100 o FIN: ").strip()
        if s == "FIN":
            break
        try:
            n = int(s)
            if 1 <= n <= 100:
                validos += 1
            else:
                print("Entrada inválida.")
        except ValueError:
            print("Entrada inválida.")
    print(f"Entradas válidas: {validos}")

# 10. Como el anterior pero mostrando la media de las válidas
def ej10():
    validos = 0
    suma = 0
    while True:
        s = input("Número 1..100 o FIN: ").strip()
        if s == "FIN":
            break
        try:
            n = int(s)
            if 1 <= n <= 100:
                validos += 1
                suma += n
            else:
                print("Entrada inválida.")
        except ValueError:
            print("Entrada inválida.")
    if validos == 0:
        print("No hay entradas válidas.")
    else:
        media = suma / validos
        print(f"Media: {media}")

# 11. Como el anterior, además mostrar mayor y menor
def ej11():
    validos = 0
    suma = 0
    mayor = None
    menor = None
    while True:
        s = input("Número 1..100 o FIN: ").strip()
        if s == "FIN":
            break
        try:
            n = int(s)
            if 1 <= n <= 100:
                validos += 1
                suma += n
                if mayor is None or n > mayor: mayor = n
                if menor is None or n < menor: menor = n
            else:
                print("Entrada inválida.")
        except ValueError:
            print("Entrada inválida.")
    if validos == 0:
        print("No hay entradas válidas.")
    else:
        media = suma / validos
        print(f"Media: {media}")
        print(f"Mayor: {mayor}")
        print(f"Menor: {menor}")

# 12. Adivinar número 1..50. Máx 5 intentos
def ej12():
    objetivo = random.randint(1, 50)
    intentos = 5
    for i in range(1, intentos+1):
        n = int(input(f"Intento {i}/{intentos}. Número 1..50: "))
        if n == objetivo:
            print("¡Acertaste!")
            return
        elif n > objetivo:
            print("Te pasaste.")
        else:
            print("Te quedaste corto.")
    print(f"Sin intentos. El número era {objetivo}.")

# 13. Adivinar sin límite de intentos; al acertar decir cuántas veces falló
def ej13():
    objetivo = random.randint(1, 50)
    fallos = 0
    while True:
        n = int(input("Número 1..50: "))
        if n == objetivo:
            print(f"¡Acertaste! Fallaste {fallos} vez/veces.")
            return
        elif n > objetivo:
            print("Te pasaste.")
        else:
            print("Te quedaste corto.")
        fallos += 1

# 14. Igual, pero al final preguntar si quieres volver a jugar
def ej14():
    while True:
        objetivo = random.randint(1, 50)
        fallos = 0
        while True:
            n = int(input("Número 1..50: "))
            if n == objetivo:
                print(f"¡Acertaste! Fallaste {fallos} vez/veces.")
                break
            print("Te pasaste." if n > objetivo else "Te quedaste corto.")
            fallos += 1
        otra = input("¿Jugar otra vez? (s/n): ").strip().lower()
        if otra != "s":
            print("Fin del juego.")
            return

# 15. Igual, pero al empezar pedir máximo y nº de intentos
def ej15():
    maximo = int(input("Número máximo (ej. 50): "))
    intentos = int(input("Número de intentos (ej. 5): "))
    objetivo = random.randint(1, maximo)
    for i in range(1, intentos+1):
        n = int(input(f"Intento {i}/{intentos}. Número 1..{maximo}: "))
        if n == objetivo:
            print("¡Acertaste!")
            return
        print("Te pasaste." if n > objetivo else "Te quedaste corto.")
    print(f"Sin intentos. El número era {objetivo}.")

# 16. Longitud y área de circunferencia, 5 decimales
def ej16():
    r = float(input("Radio: "))
    pi = 3.14159
    area = pi * (r ** 2)
    longitud = 2 * pi * r
    print(f"Área: {area:.5f}")
    print(f"Longitud: {longitud:.5f}")

# 17. Convertir temperatura (entrada tipo 12C, 280.57K, 98.6F), salida con 2 decimales
def ej17():
    s = input("Temperatura (ej. 12C, 98.6F, 280.57K): ").strip()
    unidad = s[-1].upper()
    valor = float(s[:-1])
    if unidad == "C":
        c = valor
        f = c * 1.8 + 32
        k = c + 273.15
    elif unidad == "F":
        f = valor
        c = (f - 32) / 1.8
        k = (5/9) * (f - 32) + 273.15
    elif unidad == "K":
        k = valor
        c = k - 273.15
        f = 1.8 * (k - 273.15) + 32
    else:
        print("Unidad no válida.")
        return
    if unidad == "C":
        print(f"{f:.2f}F, {k:.2f}K")
    elif unidad == "F":
        print(f"{c:.2f}C, {k:.2f}K")
    else:
        print(f"{c:.2f}C, {f:.2f}F")

# 18. Retención IRPF 2022 (tabla simple estatal) y neto
# Tramos (euros): 0-12,450:19% ; 12,450-20,200:24% ; 20,200-35,200:30% ;
# 35,200-60,000:37% ; 60,000-300,000:45% ; >300,000:47%
def ej18():
    salario = float(input("Sueldo anual bruto (€): "))
    tramos = [
        (0,       12450,   0.19),
        (12450,   20200,   0.24),
        (20200,   35200,   0.30),
        (35200,   60000,   0.37),
        (60000,   300000,  0.45),
        (300000,  float('inf'), 0.47),
    ]
    retenido = 0.0
    restante = salario
    for i, (a, b, tipo) in enumerate(tramos):
        if salario > a:
            base = min(salario, b) - a
            cuota = base * tipo
            retenido += cuota
        else:
            break
    porcentaje_aprox = (retenido / salario * 100) if salario > 0 else 0
    neto = salario - retenido
    print(f"Porcentaje aprox.: {porcentaje_aprox:.2f}%")
    print(f"Importe retenido: {retenido:.2f} €")
    print(f"Importe neto: {neto:.2f} €")


# if __name__ == "__main__":
#     ej1()
#     ej2()
#     ej3()
#     ej4()
#     ej5()
#     ej6()
#     ej7()
#     ej8()
#     ej9()
#     ej10()
#     ej11()
#     ej12()
#     ej13()
#     ej14()
#     ej15()
#     ej16()
#     ej17()
#     ej18()
