# Soluciones simples en Python — Ejercicios genéricos de programación 3
# Cada ejercicio es una función: ej1(), ej2(), ..., ej15().
# Ejecuta la que quieras probando desde el bloque __main__ al final.

import re

# 1. Pedir contraseña dos veces hasta que coincidan
def ej1():
    while True:
        a = input("Contraseña: ")
        b = input("Repite contraseña: ")
        if a == b:
            print("Coinciden.")
            break
        print("No coinciden, inténtalo otra vez.")

# 2. Igual que el anterior pero al acertar decir cuántos intentos inválidos hubo
def ej2():
    intentos_invalidos = 0
    while True:
        a = input("Contraseña: ")
        b = input("Repite contraseña: ")
        if a == b:
            print(f"Coinciden. Intentos inválidos: {intentos_invalidos}")
            break
        print("No coinciden.")
        intentos_invalidos += 1

# 3. Nombre y apellidos -> 'Apellidos, Nombre'
def ej3():
    nombre = input("Nombre (puede incluir segundo nombre): ").strip()
    apellidos = input("Apellidos: ").strip()
    print(f"{apellidos}, {nombre}")

# 4. Quitar espacios y contar cuántos se quitaron
def ej4():
    s = input("Texto: ")
    sin_espacios = s.replace(" ", "")
    quitados = len(s) - len(sin_espacios)
    print(sin_espacios)
    print(f"Espacios quitados: {quitados}")

# 5. Mostrar el texto al revés
def ej5():
    s = input("Texto: ")
    print(s[::-1])

# 6. Separar en posiciones pares e impares (empezando en 0)
def ej6():
    s = input("Texto: ")
    pares = s[0::2]
    impares = s[1::2]
    print("Pares :", pares)
    print("Impares:", impares)

# 7. Leet simple: a->4, e->3, i->1, o->0 (may/min)
def ej7():
    s = input("Texto: ")
    mapa = str.maketrans("aeioAEIO", "43104310")
    print(s.translate(mapa))

# 8. Quitar vocales (may/min)
def ej8():
    s = input("Texto: ")
    vocales = set("aeiouAEIOU")
    res = "".join(ch for ch in s if ch not in vocales)
    print(res)

# 9. Capital según destino (Francia, Italia, Chile, Japón)
def ej9():
    pais = input("Destino: ").strip().lower()
    match pais:
        case "francia":
            print("París")
        case "italia":
            print("Roma")
        case "chile":
            print("Santiago de Chile")
        case "japón" | "japon":
            print("Tokio")
        case _:
            print("Opción no válida.")

# 10. Validar NIF (solo formato: 8 dígitos + 1 letra)
def ej10():
    s = input("NIF: ").strip()
    ok = len(s) == 9 and s[:8].isdigit() and s[-1].isalpha()
    print("Válido" if ok else "No válido")

# 11. Detectar si es NIF o NIE y si es válido (solo formato)
def ej11():
    s = input("Documento: ").strip()
    if len(s) == 9 and s[:8].isdigit() and s[-1].isalpha():
        print("NIF válido")
    elif len(s) == 9 and s[0].upper() in "XYZ" and s[1:8].isdigit() and s[-1].isalpha():
        print("NIE válido")
    else:
        print("No válido")

# 12. Validar matrícula: 4 dígitos + 3 letras (sin A,E,I,O,U, Ñ, Q; mayúsculas)
def ej12():
    s = input("Matrícula: ").strip()
    patron = r"^[0-9]{4}[BCDFGHJKLMNPRSTVWXYZ]{3}$"
    ok = re.match(patron, s) is not None
    print("Válida" if ok else "No válida")

# 13. Igual, pero permitir un espacio o guión entre números y letras
def ej13():
    s = input("Matrícula: ").strip()
    patron = r"^[0-9]{4}(?: |\-)?[BCDFGHJKLMNPRSTVWXYZ]{3}$"
    ok = re.match(patron, s) is not None
    print("Válida" if ok else "No válida")

# 14. Comprobar letra del NIF/NIE (método estándar con módulo 23)
def ej14():
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    s = input("NIF/NIE: ").strip().upper()
    if len(s) != 9 or not s[-1].isalpha():
        print("No válido")
        return
    cuerpo = s[:-1]
    letra = s[-1]
    if cuerpo[0] in "XYZ":  # NIE
        reemplazo = {"X": "0", "Y": "1", "Z": "2"}[cuerpo[0]]
        numero = int(reemplazo + cuerpo[1:])
    elif cuerpo.isdigit():   # NIF
        numero = int(cuerpo)
    else:
        print("No válido")
        return
    letra_ok = letras[numero % 23]
    if letra == letra_ok:
        print("Válido")
    else:
        print(f"No válido (debería ser {letra_ok})")

# 15. Validar fecha DD/MM/YYYY (bisiestos: años divisibles entre 4)
def ej15():
    s = input("Fecha (DD/MM/YYYY): ").strip()
    # Comprobar formato
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", s):
        print("Fecha no válida")
        return
    d, m, y = map(int, s.split("/"))
    if not (1 <= m <= 12):
        print("Fecha no válida")
        return
    # Días por mes (febrero 28, salvo bisiesto según regla simple del enunciado)
    dias_mes = [31, 29 if y % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_dia = dias_mes[m-1]
    if 1 <= d <= max_dia:
        print("Fecha válida")
    else:
        print("Fecha no válida")


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
