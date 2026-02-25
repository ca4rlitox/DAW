#Control de EXCEPCIONES:

print("Inicio del Programa")
num=input("Escribe un número")
#try y except son los dos bloques obligatorios
try:
    print("antes del posible error")
    numero=int(num) #intenta convertir la entrada a entero. EN EL MOMENTO QUE HAY UN ERROR EL TRY SE SUPENDE Y PASA A OTRO BLOQUE
    print("Despues del posible error") #si no provoca un error imprime esta parte y no entra en el except
except:
    print("No puedo convertir eso en un número") #su provoca un error salta a este bloque e imprime esto y continua el programa

print("Fin del Programa")

#bloque ELSE:

print("Inicio del Programa")
num = input("Escribe un número")

try:
    print("antes del posible error")
    numero = int(num)
    print("Despues del posible error")
except:
    print(
        "No puedo convertir eso en un número")
else:
    print("No ha habido errores") #el else se ejecuta solo si no hay errores en el try


print("Fin del Programa")

#Bloque FINALLY:

print("Inicio del Programa")
num = input("Escribe un número")

try:
    print("antes del posible error")
    numero = int(num)
    print("Despues del posible error")
except:
    print(
        "No puedo convertir eso en un número")
else:
    print("No ha habido errores")
finally:
    print("Esto se ejecuta siempre")# el finally siempre se ejecuta

print("Fin del Programa")

#CAPTURAR EXCEPCIONES

print("Inicio del Programa")
num = input("Escribe un número")


try:
    print("antes del posible error")
    numero = int(num)
    division = 50/numero
    print("Despues del posible error")
except ValueError:
    print("No puedo convertir eso en un número") #si ingrese un tipo no válido
except ZeroDivisionError:
    print("No puedo dividir entre 0") #si ingrese 0 y no puedo dividir por 0
except:
    print("Ha ocurrido un error pero no se cual es") #una excepcion genérica
else:
    print("No ha habido errores")
finally:
    print("Esto se ejecuta siempre")# el finally siempre se ejecuta

print("Fin del Programa")

#Para saber que excepcion es (el nombre de la excepcion) provoco el error para verla

