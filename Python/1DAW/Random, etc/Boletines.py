import random
import math

# Boletín 1 - Ejercicio 1
# Muestra los 10 primeros números enteros
for i in range(1, 11):
    print(i)

# Boletín 1 - Ejercicio 2
# Muestra los 50 primeros números pares
for i in range(1, 51):
    print(2 * i)

# Boletín 1 - Ejercicio 3
# Muestra los 5 primeros múltiplos de un número dado por el usuario
num = int(input("Introduce un número: "))
for i in range(1, 6):
    print(num * i)

# Boletín 1 - Ejercicio 4
# Muestra todos los números divisibles por 7 menores a 10000
for n in range(7, 10000, 7):
    print(n)

# Boletín 1 - Ejercicio 5
# Indica si un número introducido es par o impar
n = int(input("Introduce un número: "))
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Boletín 1 - Ejercicio 6
# Indica si un número introducido es divisible por 3
n = int(input("Introduce un número: "))
if n % 3 == 0:
    print("El número es divisible por 3")
else:
    print("El número no es divisible por 3")

# Boletín 1 - Ejercicio 7
# Calcula el precio tras aplicarle el IVA del 21%
precio = float(input("Introduce un precio: "))
precio_con_iva = precio * 1.21
print(f"Precio con IVA (21%): {precio_con_iva}")

# Boletín 1 - Ejercicio 8
# Calcula el pago mensual dado un importe y número de meses (sin intereses)
importe = float(input("Introduce el importe: "))
meses = int(input("Introduce el número de meses: "))
pago_mensual = round(importe / meses, 2)
print(f"Pago mensual: {pago_mensual}")

# Boletín 1 - Ejercicio 9
# Genera un número aleatorio entre 0 y 50
numero = random.randint(0, 50)
print(f"Número aleatorio generado: {numero}")

# Boletín 1 - Ejercicio 10
# Genera dos números aleatorios entre 1 y 6 (tirada de dos dados)
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
print(f"Dado 1: {dado1}, Dado 2: {dado2}")

# Boletín 1 - Ejercicio 11
# Tira dos dados repetidamente hasta que salga el mismo número en ambos
tiros = 0
while True:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    tiros += 1
    if d1 == d2:
        break
print(f"Ha necesitado {tiros} tiradas para obtener dos dados iguales")

# Boletín 1 - Ejercicio 12
# Asistente para juego de rol: tira una cantidad de dados con un número de caras dado
dados = int(input("Introduce el número de dados: "))
caras = int(input("Introduce el número de caras: "))
resultado = []
for i in range(dados):
    resultado.append(random.randint(1, caras))
print("Resultado de la tirada:", resultado)

# Boletín 1 - Ejercicio 13
# Versión del anterior que no admite dados con caras impares (vuelve a preguntar)
dados = int(input("Introduce el número de dados: "))
while True:
    caras = int(input("Introduce el número de caras (par): "))
    if caras % 2 == 0:
        break
    print("Número de caras erróneo, debe ser par.")
resultado = []
for i in range(dados):
    resultado.append(random.randint(1, caras))
print("Resultado de la tirada:", resultado)

# Boletín 1 - Ejercicio 14
# Genera un número aleatorio entre dos números dados por el usuario (sin validar orden)
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
numero = random.randint(a, b)
print(f"Número aleatorio entre {a} y {b}: {numero}")

# Boletín 1 - Ejercicio 15
# Versión del anterior que corrige el orden si el primer número es mayor
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
lo = min(a, b)
hi = max(a, b)
numero = random.randint(lo, hi)
print(f"Número aleatorio entre {lo} y {hi}: {numero}")

# Boletín 1 - Ejercicio 16
# Genera seis números aleatorios entre 1 y 49 (lotería primitiva, permite repetidos)
numeros = []
for i in range(6):
    numeros.append(random.randint(1, 49))
print("Números generados:", ", ".join(map(str, numeros)))

# Boletín 1 - Ejercicio 17
# Genera quince resultados de quiniela (números aleatorios 1-3, con 3 interpretado como 'X')
resultados = []
for i in range(15):
    valor = random.randint(1, 3)
    if valor == 3:
        resultados.append("X")
    else:
        resultados.append(str(valor))
print("Quiniela:", " ".join(resultados))

# Boletín 1 - Ejercicio 18
# Genera números aleatorios entre 1 y 1000 hasta que salga 666, cuenta cuántos generó
contador = 0
while True:
    n = random.randint(1, 1000)
    contador += 1
    if n == 666:
        break
dias_restantes = contador - 1
print(f"¡Faltan {dias_restantes} días para que se acabe todo!")

# Boletín 1 - Ejercicio 19
# Muestra los divisores de un número introducido
num = int(input("Introduce un número: "))
print(f"Divisores del número {num}:", end=" ")
divs = []
for i in range(1, num + 1):
    if num % i == 0:
        divs.append(str(i))
print(", ".join(divs))

# Boletín 1 - Ejercicio 20
# Ordena tres números introducidos de menor a mayor
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))
nums = [a, b, c]
nums.sort()
print("Números ordenados:", nums)

# Boletín 1 - Ejercicio 21
# Determina si un número es primo o no
n = int(input("Introduce un número: "))
es_primo = True
if n < 2:
    es_primo = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            es_primo = False
            break
if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")

# Boletín 1 - Ejercicio 22
# Genera un número primo aleatorio entre 10,000,000 y 50,000,000
while True:
    candidato = random.randint(10000000, 50000000)
    es_primo = True
    for i in range(2, int(math.sqrt(candidato)) + 1):
        if candidato % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"Número primo aleatorio generado: {candidato}")
        break

# Boletín 1 - Ejercicio 23
# Muestra todos los números primos del 1 al 100
primos = []
for num in range(2, 101):
    es_primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(str(num))
print("Primos entre 1 y 100:", ", ".join(primos))

# Boletín 1 - Ejercicio 24
# Pide dos números y muestra los primos que hay entre ellos
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
lo = min(a, b)
hi = max(a, b)
primos = []
for num in range(max(lo, 2), hi + 1):
    es_primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(str(num))
print(f"Números primos entre {lo} y {hi}:", ", ".join(primos))

# Boletín 1 - Ejercicio 25
# Divide sucesivamente un número por 2 hasta que sea <= 1, mostrando los resultados
valor = float(input("Introduce un número: "))
print(f"Has introducido el número {valor}")
while True:
    valor = valor / 2
    # Redondear a 2 decimales si es necesario
    if round(valor, 2).is_integer():
        print(int(round(valor, 2)))
    else:
        print(round(valor, 2))
    if valor <= 1:
        break

# Boletín 2 - Ejercicio 1
# Pide tres palabras y las muestra ordenadas alfabéticamente (ascendente)
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")
palabra3 = input("Introduce la tercera palabra: ")
palabras = [palabra1, palabra2, palabra3]
palabras.sort()
print("Palabras en orden alfabético:", palabras)

# Boletín 2 - Ejercicio 2
# Igual que el anterior pero ordenando en orden descendente
palabras_desc = sorted(palabras, reverse=True)
print("Palabras en orden descendente:", palabras_desc)

# Boletín 2 - Ejercicio 3
# Calcula el precio final aplicando IVA del 21%, redondeado a dos decimales
precio = float(input("Introduce un precio: "))
precio_final = round(precio * 1.21, 2)
print(f"Precio con IVA: {precio_final}")

# Boletín 2 - Ejercicio 4
# Calcula la media de dos calificaciones (0-10 con decimales), redondeada sin decimales
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Entrada de nota no válida")
else:
    media = (nota1 + nota2) / 2
    media_redondeada = round(media)
    print(f"Media redondeada: {media_redondeada}")

# Boletín 2 - Ejercicio 5
# Calcula la media ponderada de tres notas (5%,15%,80%) y la muestra con 2 decimales (nota real) y sin decimales (nota de boletín truncada)
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))
ponderada = nota1 * 0.05 + nota2 * 0.15 + nota3 * 0.80
nota_real = round(ponderada, 2)
nota_boletin = int(ponderada)
print(f"Nota real (con decimales): {nota_real}")
print(f"Nota de boletín (sin decimales): {nota_boletin}")

# Boletín 2 - Ejercicio 6
# Modifica el ejercicio anterior: si la nota de boletín es >5, redondea normalmente; si <5, trunca decimales
nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))
ponderada = nota1 * 0.05 + nota2 * 0.15 + nota3 * 0.80
nota_real = round(ponderada, 2)
if ponderada >= 5:
    nota_boletin = int(ponderada + 0.5)
else:
    nota_boletin = int(ponderada)
print(f"Nota real (con decimales): {nota_real}")
print(f"Nota de boletín: {nota_boletin}")

# Boletín 2 - Ejercicio 7
# Imprime la tabla de multiplicar (1 al 10) de un número introducido
num = int(input("Introduce un número: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

# Boletín 2 - Ejercicio 8
# Muestra los divisores de un número separados por comas, sin coma final
num = int(input("Introduce un número: "))
divisores = []
for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(str(i))
print(f"Divisores del número {num}: " + ", ".join(divisores))

# Boletín 2 - Ejercicio 9
# Pide números entre 1 y 100 hasta que se introduzca "FIN". Ignora entradas inválidas y muestra cuántos válidos se introdujeron.
validos = 0
while True:
    entrada = input("Introduce un número (1-100) o FIN para terminar: ")
    if entrada == "FIN":
        break
    try:
        numero = int(entrada)
        if 1 <= numero <= 100:
            validos += 1
        else:
            print("Entrada inválida (fuera de rango)")
    except:
        print("Entrada inválida (no es un número)")
print(f"Se introdujeron {validos} entradas válidas")

# Boletín 2 - Ejercicio 10
# Modifica el anterior: al final muestra la media aritmética de los números válidos
validos = 0
suma = 0
while True:
    entrada = input("Introduce un número (1-100) o FIN para terminar: ")
    if entrada == "FIN":
        break
    try:
        numero = int(entrada)
        if 1 <= numero <= 100:
            validos += 1
            suma += numero
        else:
            print("Entrada inválida (fuera de rango)")
    except:
        print("Entrada inválida (no es un número)")
if validos > 0:
    media = suma / validos
    print(f"Se introdujeron {validos} entradas válidas")
    print(f"Media aritmética: {round(media, 2)}")
else:
    print("No se introdujeron números válidos")

# Boletín 2 - Ejercicio 11
# Modifica el anterior: al final muestra también el número mayor y menor introducidos
validos = 0
suma = 0
minimo = None
maximo = None
while True:
    entrada = input("Introduce un número (1-100) o FIN para terminar: ")
    if entrada == "FIN":
        break
    try:
        numero = int(entrada)
        if 1 <= numero <= 100:
            validos += 1
            suma += numero
            if minimo is None or numero < minimo:
                minimo = numero
            if maximo is None or numero > maximo:
                maximo = numero
        else:
            print("Entrada inválida (fuera de rango)")
    except:
        print("Entrada inválida (no es un número)")
if validos > 0:
    media = suma / validos
    print(f"Se introdujeron {validos} entradas válidas")
    print(f"Media aritmética: {round(media, 2)}")
    print(f"Número menor: {minimo}")
    print(f"Número mayor: {maximo}")
else:
    print("No se introdujeron números válidos")

# Boletín 2 - Ejercicio 12
# Juego de adivinar un número entre 1 y 50 con 5 intentos máximo
secreto = random.randint(1, 50)
intentos = 5
acertado = False
for i in range(intentos):
    guess = int(input("Adivina el número (1-50): "))
    if guess == secreto:
        print("¡Has acertado!")
        acertado = True
        break
    elif guess < secreto:
        print("Te has quedado corto")
    else:
        print("Te has pasado")
if not acertado:
    print(f"No has adivinado el número. Era el {secreto}")

# Boletín 2 - Ejercicio 13
# Versión del anterior con intentos ilimitados, informa cuántos fallos antes de acertar
secreto = random.randint(1, 50)
fallos = 0
while True:
    guess = int(input("Adivina el número (1-50): "))
    if guess == secreto:
        print(f"¡Acertaste! Fallaste {fallos} vez/veces antes de lograrlo.")
        break
    else:
        fallos += 1
        if guess < secreto:
            print("Te has quedado corto")
        else:
            print("Te has pasado")

# Boletín 2 - Ejercicio 14
# Versión del anterior que al final pregunta si jugar de nuevo
while True:
    secreto = random.randint(1, 50)
    fallos = 0
    while True:
        guess = int(input("Adivina el número (1-50): "))
        if guess == secreto:
            print(f"¡Acertaste! Fallaste {fallos} vez/veces antes de lograrlo.")
            break
        else:
            fallos += 1
            if guess < secreto:
                print("Te has quedado corto")
            else:
                print("Te has pasado")
    jugar = input("¿Quieres volver a jugar? (S/N): ")
    if jugar.strip().lower() != 's':
        break

# Boletín 2 - Ejercicio 15
# Versión del juego anterior que al iniciar pide número máximo y número de intentos
while True:
    max_num = int(input("Introduce el número máximo: "))
    max_intentos = int(input("Introduce el número de intentos: "))
    secreto = random.randint(1, max_num)
    acertado = False
    for i in range(max_intentos):
        guess = int(input(f"Adivina el número (1-{max_num}): "))
        if guess == secreto:
            print("¡Has acertado!")
            acertado = True
            break
        elif guess < secreto:
            print("Te has quedado corto")
        else:
            print("Te has pasado")
    if not acertado:
        print(f"No has adivinado el número. Era el {secreto}")
    jugar = input("¿Quieres volver a jugar? (S/N): ")
    if jugar.strip().lower() != 's':
        break

# Boletín 2 - Ejercicio 16
# Calcula la longitud y el área de una circunferencia dado su radio, con 5 decimales
radio = float(input("Introduce el radio de la circunferencia: "))
area = 3.14159 * (radio ** 2)
longitud = 2 * 3.14159 * radio
print(f"Área = {round(area, 5)}")
print(f"Longitud = {round(longitud, 5)}")

# Boletín 2 - Ejercicio 17
# Convierte una temperatura introducida con unidad (C, F o K) a las otras dos unidades
entrada = input("Introduce una temperatura (ej. 12C, 98.6F, 280.57K): ")
unidad = entrada[-1].upper()
valor = float(entrada[:-1])
if unidad == 'C':
    f = valor * 1.8 + 32
    k = valor + 273.15
    print(f"{valor}°C son {round(f, 2)}°F y {round(k, 2)}°K")
elif unidad == 'F':
    c = (valor - 32) / 1.8
    k = (valor - 32) * 5/9 + 273.15
    print(f"{valor}°F son {round(c, 2)}°C y {round(k, 2)}°K")
elif unidad == 'K':
    c = valor - 273.15
    f = 1.8 * (valor - 273.15) + 32
    print(f"{valor}°K son {round(c, 2)}°C y {round(f, 2)}°F")
else:
    print("Formato de entrada no válido")

# Boletín 2 - Ejercicio 18
# Calcula el porcentaje de retención IRPF según sueldo anual 2022, e indica retención e importe neto
sueldo = float(input("Introduce tu sueldo anual (€): "))
if sueldo <= 12450:
    porcentaje = 19
elif sueldo <= 20200:
    porcentaje = 24
elif sueldo <= 35200:
    porcentaje = 30
elif sueldo <= 60000:
    porcentaje = 37
elif sueldo <= 300000:
    porcentaje = 45
else:
    porcentaje = 47
retencion = sueldo * porcentaje / 100
neto = sueldo - retencion
print(f"Porcentaje de retención: {porcentaje}%")
print(f"Importe retenido: {round(retencion, 2)} €")
print(f"Sueldo neto: {round(neto, 2)} €")

# Boletín 3 - Ejercicio 1
# Pide una contraseña dos veces hasta que coincidan
while True:
    pwd1 = input("Introduce la contraseña: ")
    pwd2 = input("Repite la contraseña: ")
    if pwd1 == pwd2:
        break
    print("Las contraseñas no coinciden, inténtalo de nuevo")

# Boletín 3 - Ejercicio 2
# Modifica el anterior para informar del número de intentos inválidos
intentos_invalidos = 0
while True:
    pwd1 = input("Introduce la contraseña: ")
    pwd2 = input("Repite la contraseña: ")
    if pwd1 == pwd2:
        print(f"Número de intentos inválidos: {intentos_invalidos}")
        break
    else:
        intentos_invalidos += 1
        print("No coinciden, vuelve a intentarlo")

# Boletín 3 - Ejercicio 3
# Pide nombre y apellidos y los muestra formateados "Apellidos, Nombre"
nombre = input("Introduce tu nombre: ")
apellidos = input("Introduce tus apellidos: ")
print(f"{apellidos}, {nombre}")

# Boletín 3 - Ejercicio 4
# Pide una cadena de texto y la muestra sin espacios, indicando cuántos espacios se eliminaron
cadena = input("Introduce una cadena de texto: ")
sin_espacios = ""
espacios_eliminados = 0
for ch in cadena:
    if ch != " ":
        sin_espacios += ch
    else:
        espacios_eliminados += 1
print(sin_espacios)
print(f"Se eliminaron {espacios_eliminados} espacios")

# Boletín 3 - Ejercicio 5
# Pide una cadena de texto y la imprime al revés
cadena = input("Introduce una cadena: ")
invertida = ""
for ch in cadena:
    invertida = ch + invertida
print(invertida)

# Boletín 3 - Ejercicio 6
# Pide una cadena de texto y la separa en dos: caracteres en posiciones pares e impares
cadena = input("Introduce una cadena: ")
pares = ""
impares = ""
for i, ch in enumerate(cadena):
    if i % 2 == 0:
        pares += ch
    else:
        impares += ch
print("Primera cadena (posiciones pares):", pares)
print("Segunda cadena (posiciones impares):", impares)

# Boletín 3 - Ejercicio 7
# Pide una cadena de texto y la escribe en 'alfabeto hacker'
texto = input("Introduce una cadena: ")
traduccion = ""
for ch in texto:
    if ch in "Aa":
        traduccion += "4"
    elif ch in "Ee":
        traduccion += "3"
    elif ch in "Ii":
        traduccion += "1"
    elif ch in "Oo":
        traduccion += "0"
    else:
        traduccion += ch
print(traduccion)

# Boletín 3 - Ejercicio 8
# Pide una cadena y la muestra sin vocales
texto = input("Introduce una cadena: ")
resultado = ""
for ch in texto:
    if ch.lower() not in ['a', 'e', 'i', 'o', 'u']:
        resultado += ch
print(resultado)

# Boletín 3 - Ejercicio 9
# Ofrece cuatro destinos (Francia, Italia, Chile, Japón) y muestra la capital según el destino elegido
destino = input("Elige un destino (Francia, Italia, Chile o Japón): ")
d = destino.strip().lower()
if d == "francia":
    print("La capital de Francia es París")
elif d == "italia":
    print("La capital de Italia es Roma")
elif d == "chile":
    print("La capital de Chile es Santiago de Chile")
elif d == "japon" or d == "japón":
    print("La capital de Japón es Tokio")
else:
    print("Destino no reconocido")

# Boletín 3 - Ejercicio 10
# Valida si un NIF español introducido es correcto (8 dígitos + 1 letra)
dni = input("Introduce un NIF: ")
if len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha():
    print("NIF con formato válido")
else:
    print("NIF con formato incorrecto")

# Boletín 3 - Ejercicio 11
# Mejora el anterior: detecta si es NIF o NIE y lo indica si es válido
doc = input("Introduce un NIF o NIE: ")
doc_upper = doc.upper()
es_valido = False
tipo = ""
if len(doc_upper) == 9 and doc_upper[-1].isalpha():
    if doc_upper[0].isdigit():
        # Comienza con dígito: posible NIF
        if doc_upper[:8].isdigit():
            es_valido = True
            tipo = "NIF"
    elif doc_upper[0] in ['X', 'Y', 'Z']:
        # NIE: X/Y/Z + 7 dígitos + letra
        if doc_upper[1:8].isdigit():
            es_valido = True
            tipo = "NIE"
if es_valido:
    print(f"Es un {tipo} válido")
else:
    print("El documento no es válido")

# Boletín 3 - Ejercicio 12
# Valida si una matrícula española introducida (1234XXX) es válida
matricula = input("Introduce una matrícula: ")
mat = matricula.replace(" ", "").upper()
valida = False
if len(mat) == 7 and mat[:4].isdigit() and mat[4:].isalpha():
    letras = mat[4:]
    # Comprueba que las letras no sean vocales, Ñ ni Q
    permitido = True
    for ch in letras:
        if ch in "AEIOUÑQ":
            permitido = False
            break
    if permitido:
        valida = True
if valida:
    print("Matrícula válida")
else:
    print("Matrícula no válida")

# Boletín 3 - Ejercicio 13
# Versión del anterior que admite un espacio o guion entre los números y las letras
matricula = input("Introduce una matrícula: ")
m = matricula.upper()
if len(m) == 8 and (m[4] == " " or m[4] == "-"):
    m = m[0:4] + m[5:]
# Ahora 'm' debería tener 7 caracteres
valida = False
if len(m) == 7 and m[:4].isdigit() and m[4:].isalpha():
    permitido = True
    for ch in m[4:]:
        if ch in "AEIOUÑQ":
            permitido = False
            break
    if permitido:
        valida = True
if valida:
    print("Matrícula válida")
else:
    print("Matrícula no válida")

# Boletín 3 - Ejercicio 14
# Comprueba si un NIF es correcto incluyendo la validación de la letra
dni = input("Introduce un NIF: ").upper()
if len(dni) == 9 and dni[:8].isdigit() and dni[8].isalpha():
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(dni[:8])
    letra_correcta = letras[numero % 23]
    if dni[8] == letra_correcta:
        print("NIF válido")
    else:
        print("NIF no válido (letra incorrecta)")
else:
    print("Formato de NIF incorrecto")

# Boletín 3 - Ejercicio 15
# Comprueba si una fecha introducida (DD/MM/YYYY) es correcta
fecha = input("Introduce una fecha (DD/MM/YYYY): ")
valida = True
# Chequea formato
if len(fecha) != 10 or fecha[2] != '/' or fecha[5] != '/':
    valida = False
else:
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    anio = int(fecha[6:10])
    if mes < 1 or mes > 12:
        valida = False
    else:
        # Días máximos según mes
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            max_dia = 31
        elif mes in [4, 6, 9, 11]:
            max_dia = 30
        else:
            # Febrero
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                max_dia = 29
            else:
                max_dia = 28
        if dia < 1 or dia > max_dia:
            valida = False
if valida:
    print("Fecha correcta")
else:
    print("Fecha no válida")

# Boletín 4 - Ejercicio 1
# Calcula el factorial de un número introducido
n = int(input("Introduce un número: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"El factorial de {n} es {factorial}")

# Boletín 4 - Ejercicio 2
# Calcula los primeros N números de la sucesión de Fibonacci
N = int(input("Introduce cuántos números de Fibonacci calcular: "))
fibo = []
for i in range(N):
    if i == 0 or i == 1:
        fibo.append(i)
    else:
        fibo.append(fibo[-1] + fibo[-2])
print(", ".join(map(str, fibo)))

# Boletín 4 - Ejercicio 3
# Muestra todos los números de Fibonacci <= un número dado
limite = int(input("Introduce un número: "))
fibo = [0, 1]
while fibo[-1] + fibo[-2] <= limite:
    fibo.append(fibo[-1] + fibo[-2])
fibo_filtrada = [x for x in fibo if x <= limite]
print(", ".join(map(str, fibo_filtrada)))

# Boletín 4 - Ejercicio 4
# Cuenta el número de cifras de un número
num = int(input("Introduce un número: "))
if num == 0:
    cifras = 1
else:
    cifras = 0
    temp = abs(num)
    while temp > 0:
        temp //= 10
        cifras += 1
print(f"El número {num} tiene {cifras} cifras")

# Boletín 4 - Ejercicio 5
# Determina si un número es capicúa (palíndromo)
num = input("Introduce un número: ")
if num == num[::-1]:
    print("El número es capicúa")
else:
    print("El número no es capicúa")

# Boletín 4 - Ejercicio 6
# Muestra los 50 primeros números primos con sus raíces cuadradas, cuadrados y cubos
cont = 0
num = 2
while cont < 50:
    es_primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        raiz = math.sqrt(num)
        print(f"{num} -> sqrt={round(raiz, 2)}, cuadrado={num**2}, cubo={num**3}")
        cont += 1
    num += 1

# Boletín 4 - Ejercicio 7
# Calcula la primera pareja de números primos gemelos por encima de 50
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 51
while True:
    if es_primo(n) and es_primo(n + 2):
        print(f"Primos gemelos encontrados: {n} y {n+2}")
        break
    n += 1

# Boletín 4 - Ejercicio 8
# Suma por separado las cifras pares y las impares de un número
num = int(input("Introduce un número: "))
suma_pares = 0
suma_impares = 0
temp = abs(num)
if temp == 0:
    suma_pares = 0  # 0 se puede considerar par
while temp > 0:
    digito = temp % 10
    if digito % 2 == 0:
        suma_pares += digito
    else:
        suma_impares += digito
    temp //= 10
print(f"La suma de las cifras pares es {suma_pares}")
print(f"La suma de las cifras impares es {suma_impares}")

# Boletín 4 - Ejercicio 9
# Cuenta las ocurrencias de un carácter en una cadena y sus posiciones
cadena = input("Introduce una cadena: ")
car = input("Introduce un carácter: ")
count = 0
posiciones = []
for i, ch in enumerate(cadena):
    if ch == car:
        count += 1
        posiciones.append(i)
print(f"La '{car}' aparece en {count} ocasiones")
if count > 0:
    print("Las posiciones en las que aparece son:", ", ".join(map(str, posiciones)))

# Boletín 4 - Ejercicio 10
# Muestra solo las cifras que aparecen en una cadena de texto
cadena = input("Introduce una cadena: ")
digitos = ""
for ch in cadena:
    if ch.isdigit():
        digitos += ch
print(digitos)

# Boletín 4 - Ejercicio 11
# Separa todos los caracteres de las palabras de una frase con guiones
frase = input("Introduce una frase: ")
resultado = ""
for i, ch in enumerate(frase):
    if ch == " ":
        resultado += " "
    else:
        resultado += ch
        if i != len(frase) - 1 and frase[i+1] != " ":
            resultado += "-"
print(resultado)

# Boletín 4 - Ejercicio 12
# Indica si un año es bisiesto o no
anio = int(input("Introduce un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

# Boletín 4 - Ejercicio 13
# Muestra una matriz NxN con un carácter dado
n = int(input("Introduce un número: "))
ch = input("Introduce un carácter: ")
for i in range(n):
    print(ch * n)

# Boletín 4 - Ejercicio 14
# Determina a qué parte del día corresponde una hora dada (24h o 12h con am/pm)
entrada = input("Introduce una hora: ")
entrada = entrada.strip()
if entrada.lower().endswith("am") or entrada.lower().endswith("pm"):
    sufijo = entrada[-2:].lower()
    hora_min = entrada[:-2]
    if ":" in hora_min:
        partes = hora_min.split(":")
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            hora = int(partes[0])
            minuto = int(partes[1])
        else:
            hora = -1
            minuto = -1
    else:
        hora = -1
        minuto = -1
    # Convertir a formato 24h
    if hora < 1 or hora > 12 or minuto < 0 or minuto > 59:
        valido = False
    else:
        valido = True
        if sufijo == "am":
            hora24 = 0 if hora == 12 else hora
        else:  # pm
            hora24 = 12 if hora == 12 else hora + 12
else:
    # Formato 24h
    if entrada.count(":") == 1:
        partes = entrada.split(":")
        if partes[0].isdigit() and partes[1].isdigit():
            hora24 = int(partes[0])
            minuto = int(partes[1])
            valido = (0 <= hora24 <= 23 and 0 <= minuto <= 59)
        else:
            valido = False
    else:
        valido = False
if not 'valido' in locals() or not valido:
    print("No es una hora válida")
else:
    hora24 = hora24 if 'hora24' in locals() else hora
    # Determinar parte del día
    if 6 <= hora24 <= 11:
        parte = "mañana"
    elif 12 <= hora24 <= 19:
        parte = "tarde"
    elif 20 <= hora24 <= 23:
        parte = "noche"
    else:
        parte = "madrugada"
    print(f"Son las {hora24:02d}:{minuto:02d} de la {parte}")

# Boletín 5 - Ejercicio 1
# Genera seis números aleatorios entre 1 y 49 sin repeticiones
numeros = []
while len(numeros) < 6:
    x = random.randint(1, 49)
    if x not in numeros:
        numeros.append(x)
print("Números generados:", ", ".join(map(str, numeros)))

# Boletín 5 - Ejercicio 2
# Calcula todos los divisores comunes a dos números introducidos
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
limite = min(a, b)
div_comunes = []
for i in range(1, limite + 1):
    if a % i == 0 and b % i == 0:
        div_comunes.append(str(i))
print("Divisores comunes:", ", ".join(div_comunes))

# Boletín 5 - Ejercicio 3
# Cuenta las palabras de una frase introducida (palabras separadas por espacios)
frase = input("Introduce una frase: ")
palabras = frase.split()
print(f"La frase tiene {len(palabras)} palabras")

# Boletín 5 - Ejercicio 4
# Cuenta cuántas palabras de una frase tienen 4 o más vocales diferentes
frase = input("Introduce una frase: ")
palabras = frase.split()
count = 0
for palabra in palabras:
    vocales_en_palabra = set()
    for ch in palabra:
        if ch.lower() in 'aeiou':
            vocales_en_palabra.add(ch.lower())
    if len(vocales_en_palabra) >= 4:
        count += 1
print(f"Hay {count} palabra(s) con cuatro o más vocales diferentes")

# Boletín 5 - Ejercicio 5
# Genera 100 números aleatorios (1-50) y obtiene el mayor, el menor y el que más se repite
numeros = [random.randint(1, 50) for _ in range(100)]
mayor = max(numeros)
menor = min(numeros)
frecuencias = {}
for x in numeros:
    frecuencias[x] = frecuencias.get(x, 0) + 1
moda = None
max_freq = 0
for num, freq in frecuencias.items():
    if freq > max_freq:
        max_freq = freq
        moda = num
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Número que más se repite: {moda} (aparece {max_freq} veces)")

# Boletín 5 - Ejercicio 6
# Cuenta las veces que se repite cada cifra en un número
numero = input("Introduce un número: ")
contador = [0] * 10
for ch in numero:
    if ch.isdigit():
        contador[int(ch)] += 1
print("Tu número tiene:")
for digito in range(9, -1, -1):
    if contador[digito] != 0:
        if contador[digito] == 1:
            print(f"{contador[digito]} número {digito}")
        else:
            print(f"{contador[digito]} números {digito}")

# Boletín 6 - Ejercicios
# (No se encontraron los ejercicios del Boletín 6 en las fuentes proporcionadas)

# Boletín 7 - Ejercicio 1
# Calculadora básica: suma, resta, multiplicación, división
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
op = input("Introduce la operación (S para suma, R para resta, M para multiplicación, D para división): ").upper()
resultado = None
if op == 'S':
    resultado = a + b
elif op == 'R':
    resultado = a - b
elif op == 'M':
    resultado = a * b
elif op == 'D':
    if b != 0:
        resultado = a / b
    else:
        print("Error: División por cero")
else:
    print("Operación no válida")
if resultado is not None:
    print(f"Resultado: {resultado}")

# Boletín 7 - Ejercicio 2
# Calculadora extendida con operaciones adicionales: raíz cuadrada, cuadrado, cubo
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
op = input("Operación (S,R,M,D,A=raíz,C=cuadrado,U=cubo): ").upper()
resultado = None
if op == 'S':
    resultado = a + b
elif op == 'R':
    resultado = a - b
elif op == 'M':
    resultado = a * b
elif op == 'D':
    if b != 0:
        resultado = a / b
    else:
        print("Error: División por cero")
elif op == 'A':
    if a >= 0:
        resultado = math.sqrt(a)
    else:
        print("Error: raíz de número negativo")
elif op == 'C':
    resultado = a ** 2
elif op == 'U':
    resultado = a ** 3
else:
    print("Operación no válida")
if resultado is not None:
    print(f"Resultado: {resultado}")

# Boletín 7 - Ejercicio 3
# Pide un número del 1 al 12 y muestra el nombre del mes correspondiente
mes_num = int(input("Introduce un número de mes (1-12): "))
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
if 1 <= mes_num <= 12:
    print("Mes:", meses[mes_num - 1])
else:
    print("Número de mes inválido")

# Boletín 7 - Ejercicio 4
# Pide una nota (1-10) y devuelve la calificación según la escala dada
nota = int(input("Introduce una nota (1-10): "))
if 1 <= nota <= 2:
    print("Muy deficiente")
elif 3 <= nota <= 4:
    print("Insuficiente")
elif nota == 5:
    print("Suficiente")
elif nota == 6:
    print("Bien")
elif 7 <= nota <= 8:
    print("Notable")
elif 9 <= nota <= 10:
    print("Sobresaliente")
else:
    print("Nota fuera de rango")

# Boletín 7 - Ejercicio 5
# Crea un array de enteros del tamaño indicado, rellénalo con aleatorios (10-1000) y muestra el máximo, mínimo y media
tam = int(input("Introduce el tamaño del array: "))
array = [random.randint(10, 1000) for _ in range(tam)]
max_val = max(array) if tam > 0 else None
min_val = min(array) if tam > 0 else None
media = sum(array) / tam if tam > 0 else 0
if tam > 0:
    print(f"Máximo: {max_val}")
    print(f"Mínimo: {min_val}")
    print(f"Media: {round(media, 2)}")
else:
    print("Array vacío")

# Boletín 7 - Ejercicio 6
# Modifica el ejercicio anterior: muestra las posiciones en el array del máximo y mínimo (todas si hay repetidos)
tam = int(input("Introduce el tamaño del array: "))
array = [random.randint(10, 1000) for _ in range(tam)]
if tam > 0:
    max_val = max(array)
    min_val = min(array)
    posiciones_max = [i for i, v in enumerate(array) if v == max_val]
    posiciones_min = [i for i, v in enumerate(array) if v == min_val]
    pos_max_str = ", ".join(map(str, posiciones_max))
    pos_min_str = ", ".join(map(str, posiciones_min))
    if len(posiciones_max) > 1:
        print(f"Valor máximo {max_val} en posiciones: {pos_max_str}")
    else:
        print(f"Valor máximo {max_val} en posición: {pos_max_str}")
    if len(posiciones_min) > 1:
        print(f"Valor mínimo {min_val} en posiciones: {pos_min_str}")
    else:
        print(f"Valor mínimo {min_val} en posición: {pos_min_str}")
else:
    print("Array vacío")

# Boletín 7 - Ejercicio 7
# Crea un array de enteros del tamaño indicado, rellénalo con aleatorios (10-1000) y permite consultar un valor por su índice
tam = int(input("Introduce el tamaño del array: "))
array = [random.randint(10, 1000) for _ in range(tam)]
pos = int(input("Introduce la posición a consultar: "))
if 0 <= pos < tam:
    print(f"El valor en la posición {pos} es {array[pos]}")
else:
    print("Error: posición fuera de rango")

# Boletín 7 - Ejercicio 8
# Implementación de Buscaminas: genera tablero 5x5 con 5 minas (1) en posiciones aleatorias y lo muestra
filas = 5
columnas = 5
minas = 5
tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
colocadas = 0
while colocadas < minas:
    f = random.randint(0, filas - 1)
    c = random.randint(0, columnas - 1)
    if tablero[f][c] == 0:
        tablero[f][c] = 1
        colocadas += 1
print("Tablero 5x5 con 5 minas:")
for fila in tablero:
    print(" ".join(str(x) for x in fila))

# Modificación: permite tamaño de tablero y número de minas indicados por el usuario
n = int(input("Introduce el tamaño del tablero (n x n): "))
m = int(input("Introduce el número de minas: "))
if m > n * n:
    print("No se pueden poner más minas que las posiciones del tablero")
else:
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    colocadas = 0
    while colocadas < m:
        f = random.randint(0, n - 1)
        c = random.randint(0, n - 1)
        if tablero[f][c] == 0:
            tablero[f][c] = 1
            colocadas += 1
    print(f"Tablero {n}x{n} con {m} minas:")
    for fila in tablero:
        print(" ".join(str(x) for x in fila))
