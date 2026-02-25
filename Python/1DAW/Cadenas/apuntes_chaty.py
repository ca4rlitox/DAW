# -*- coding: utf-8 -*-
"""
CHULETA RÁPIDA — FUNCIONES Y COSAS CLAVE DEL EXAMEN (Boletines 1, 2 y 3)
Todo con ejemplos simples y comentarios cortos.
Para ver los ejemplos, ejecuta este archivo: python chuleta_examen_funciones.py
"""

import random
import math
import re

def seccion(titulo):
    print("\n" + "="*70)
    print(titulo)
    print("="*70)

# 1) print() e f-strings: imprimir texto y valores
def demo_print_y_fstrings():
    seccion("1) print() y f-strings")
    nombre = "Carlos"
    nota = 7.5
    print("Hola", nombre)                     # múltiples cosas separadas por espacio
    print(f"Tu nota es {nota}")               # f-string: meter variables dentro del texto
    print(f"Redondeada a 2 decimales: {nota:.2f}")

# 2) int(), float(), round(): convertir y redondear
def demo_conversion_y_redondeo():
    seccion("2) int(), float(), round()")
    s = "12"
    print(int(s) + 3)                         # 15
    x = 3.14159
    print(float("2.5") * x)                   # 7.853975...
    print(round(x, 2))                        # 3.14 (redondeo a 2 dec)
    print(int(7.9))                           # 7 (trunca la parte decimal)

# 3) range() y for: recorrer series de números
def demo_range_y_for():
    seccion("3) range() y for")
    # 1..10
    for i in range(1, 11):
        print(i, end=" ")
    print()
    # pares hasta 10
    for i in range(2, 11, 2):
        print(i, end=" ")
    print()

# 4) if/elif/else y % (módulo): comprobar condiciones
def demo_if_elif_else_y_modulo():
    seccion("4) if/elif/else y % (módulo)")
    n = 9
    if n % 2 == 0:
        print("par")
    elif n % 3 == 0:
        print("divisible por 3")
    else:
        print("ninguna de las anteriores")

# 5) while, break, continue: bucles que repiten
def demo_while_break_continue():
    seccion("5) while, break, continue")
    # contar hasta que salga un 6 aleatorio
    intentos = 0
    while True:
        d = random.randint(1, 6)
        intentos += 1
        if d == 6:
            print(f"Salió 6 tras {intentos} tiradas")
            break
        # si sale 1 no mostramos nada y seguimos
        if d == 1:
            continue
        print("Salió", d)

# 6) len(), slicing y trucos de cadenas
def demo_len_y_slicing():
    seccion("6) len(), slicing y trucos de cadenas")
    s = "Hola mundo"
    print("len:", len(s))          # caracteres
    print("al revés:", s[::-1])    # invertir una cadena
    print("pares:", s[0::2])       # posiciones 0,2,4,...
    print("impares:", s[1::2])     # posiciones 1,3,5,...

# 7) Métodos de str: strip, lower, upper, replace, split, join, isdigit/isalpha
def demo_metodos_str():
    seccion("7) Métodos de str útiles")
    s = "  Python Básico  "
    print(s.strip())              # quita espacios de los lados
    print(s.lower(), "|", s.upper())
    print("hola mundo".replace(" ", ""))           # quitar espacios
    print("a,b,c".split(","))                      # separar por comas -> lista
    print("-".join(["2025","10","30"]))            # unir con guiones
    print("12345".isdigit(), "ABC".isalpha())      # comprobar dígitos/letras

# 8) sorted(), min(), max(), sum()
def demo_sorted_min_max_sum():
    seccion("8) sorted(), min(), max(), sum()")
    nums = [5, 2, 9, 1]
    print(sorted(nums))                  # [1,2,5,9]
    palabras = ["perA", "Manzana", "uva"]
    print(sorted(palabras, key=str.lower))  # orden alfabético sin importar mayúsculas
    print("min:", min(nums), "max:", max(nums), "sum:", sum(nums))

# 9) random.randint(a, b): números aleatorios
def demo_random_randint():
    seccion("9) random.randint(a, b)")
    print("dado 1..6:", random.randint(1, 6))
    print("número 10..50:", random.randint(10, 50))

# 10) math: isqrt (raíz entera) y uso típico en primos
def es_primo(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    # probar divisores impares hasta la raíz
    limite = math.isqrt(n)
    for i in range(3, limite+1, 2):
        if n % i == 0:
            return False
    return True

def demo_math_y_primos():
    seccion("10) math.isqrt() + función es_primo()")
    print("¿29 es primo?:", es_primo(29))
    print("¿100 es primo?:", es_primo(100))

# 11) Listas por comprensión: crear listas rápido
def demo_list_comprehensions():
    seccion("11) Listas por comprensión")
    pares = [i for i in range(2, 21, 2)]
    cuadrados = [i*i for i in range(1, 6)]
    print("pares:", pares)
    print("cuadrados:", cuadrados)

# 12) Diccionarios y match-case: elegir una respuesta según la clave
def demo_diccionarios_y_match():
    seccion("12) Diccionarios y match-case")
    capital = {"francia": "París", "italia": "Roma", "chile": "Santiago de Chile", "japon": "Tokio"}
    pais = "italia"
    print("diccionario:", capital[pais])
    # match-case (Python 3.10+)
    destino = "japón"
    match destino.lower():
        case "francia": print("París")
        case "italia":  print("Roma")
        case "chile":   print("Santiago de Chile")
        case "japón" | "japon": print("Tokio")
        case _:         print("Opción no válida")

# 13) str.maketrans() y translate(): cambiar letras (leet) o quitar vocales
def demo_translate_y_vocales():
    seccion("13) translate(): leet y quitar vocales")
    s = "Hola Amigo"
    leet = str.maketrans("aeioAEIO", "43104310")
    print("leet:", s.translate(leet))
    vocales = set("aeiouAEIOU")
    sin_vocales = "".join(ch for ch in s if ch not in vocales)
    print("sin vocales:", sin_vocales)

# 14) re (regex) básico: patrones para matrículas y NIF
def demo_regex_basico():
    seccion("14) re.match() básico")
    mat = "1234BCD"
    patron_matricula = r"^[0-9]{4}[BCDFGHJKLMNPRSTVWXYZ]{3}$"
    print("Matrícula válida:", re.match(patron_matricula, mat) is not None)

    nif = "12345678Z"
    patron_nif = r"^[0-9]{8}[A-Za-z]$"
    print("NIF con formato válido:", re.match(patron_nif, nif) is not None)

# 15) Calcular la letra del NIF/NIE (módulo 23)
def demo_letra_nif_nie():
    seccion("15) Letra NIF/NIE (módulo 23)")
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    def letra_para(numero):
        return letras[numero % 23]
    print("12345678 ->", letra_para(12345678))  # debería dar 'Z'

    # NIE: X/Y/Z equivalen a 0/1/2 delante del número
    def letra_nie(cuerpo):  # p.ej. 'X1234567'
        mapa = {"X": "0", "Y": "1", "Z": "2"}
        numero = int(mapa[cuerpo[0]] + cuerpo[1:])
        return letra_para(numero)
    print("X1234567 ->", letra_nie("X1234567"))

# 16) Fechas DD/MM/YYYY sencillas (con bisiesto simple)
def demo_fecha_simple():
    seccion("16) Fecha DD/MM/YYYY (comprobación simple)")
    s = "29/02/2024"
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", s):
        print("Formato no válido")
        return
    d, m, y = map(int, s.split("/"))
    dias_mes = [31, 29 if y % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ok = 1 <= m <= 12 and 1 <= d <= dias_mes[m-1]
    print(s, "=>", "válida" if ok else "no válida")

# 17) IVA y áreas/perímetros: operaciones con números
def demo_iva_y_geometria():
    seccion("17) IVA y geometría (números)")
    precio = 100.0
    total = precio * 1.21
    print(f"IVA 21% de {precio}€ => {total:.2f}€")
    r = 3
    pi = 3.14159
    area = pi * r * r
    longitud = 2 * pi * r
    print(f"Área círculo r=3 => {area:.5f}")
    print(f"Longitud circunferencia r=3 => {longitud:.5f}")

# 18) Lecturas y medias sin pedir input: contar válidos, media, min y max
def demo_medias_y_estadisticos():
    seccion("18) Media, mínimo y máximo (sin pedir input)")
    datos = [10, 99, 101, 50, -5, 70, 100]
    # válidos 1..100
    validos = [n for n in datos if 1 <= n <= 100]
    if validos:
        media = sum(validos) / len(validos)
        print("válidos:", validos)
        print("media:", media, "min:", min(validos), "max:", max(validos))
    else:
        print("No hay válidos")

if __name__ == "__main__":
    demo_print_y_fstrings()
    demo_conversion_y_redondeo()
    demo_range_y_for()
    demo_if_elif_else_y_modulo()
    demo_while_break_continue()
    demo_len_y_slicing()
    demo_metodos_str()
    demo_sorted_min_max_sum()
    demo_random_randint()
    demo_math_y_primos()
    demo_list_comprehensions()
    demo_diccionarios_y_match()
    demo_translate_y_vocales()
    demo_regex_basico()
    demo_letra_nif_nie()
    demo_fecha_simple()
    demo_iva_y_geometria()
    demo_medias_y_estadisticos()
