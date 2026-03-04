#fstring = format string, es decir, darle formato al print de python

lenguaje = "java"
alumno = "francisco"
edad = 21
print("Hola, me llamo",alumno,"tengo",edad,"años y estoy estudiando",lenguaje)
print("Hola, me llamo %s tengo %d años y estoy estudiando %s"%(alumno,edad,lenguaje))

# %s -> string
# %d -> entero
# %f -> float

# Las fstring delante tienen que tener una f delante de las comillas
# Esto es mejor que lo de arriba
print(f"Hola, me llamo {alumno} tengo {edad} años y estoy {lenguaje}")

num1 = 34.567
num2 = 21.2341
# Para redondear los decimales con los f strings se hace de la siguiente manera:
print(f"Los numeros son {num1:.2f} y {num2:.2f}")

# Para calcular porcentajes se hace de la siguiente manera, con el %:
n1 = 0.34
n2 = 0.66
print(f"Los numeros son {n1:.2%} y {n2:.2%}")

# Para poner separador en numeros grandes para hacerlos mas legibles.
poblacion = 49440000
print(f"La poblacion es {poblacion:,}")

# Para formatear con el numero más grande (alinearlas) con numeros enteros
lista = [3,43,432,12,89,334]
lista.sort() # Para ordenar
for n in lista:
    print(f"{n:3d}")

# Para formatear con el numero más grande (alinearlas) con numeros decimales
lista = [3.43,43.3,432.65,12,89,334.5645]
lista.sort() # Para ordenar
for n in lista:
    print(f"{n:7.2f}")

# Para delimitarlas a la izquierda, derecha o centro. lenguaje:<10 por ejemplo le dedica 10 espacios
#Izquierda
print(f"A la izquierda: -----{lenguaje:<10}----- maricon")
#Derecha
print(f"A la derecha: -----{lenguaje:>10}----- maricon")
#Centrado
print(f"Centrada: -----{lenguaje:^20}----- maricon")

#Para combinar diferentes tipo de datos con el fstring lo definimos en varias partes
nombre = "Carlos"
apellidos = "Martin Codina"
libro = "Marie Curie en salsa"
fechadevolucion = "12/02/2026"

fichaLibro = f"""
Nombre: {nombre}
Apellidos: {apellidos}
Libro: {libro} - Fecha de devolución: {fechadevolucion}
"""
print(fichaLibro)