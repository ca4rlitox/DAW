# Las matrículas españolas constan de un número de cuatro dígitos y tres letras
# cualesquiera en mayúsculas a excepción de las vocales, la Ñ y la Q. Escribe un
# programa que detecte si una matrícula introducida por teclado es válida o no

matricula = input("Introduce la matricula")
matricula_sin_espacios = (matricula.replace(" ", ""),matricula.replace("-",""))
matricula_sin_espacios1 = matricula_sin_espacios.count(matricula_sin_espacios)

print(matricula_sin_espacios1)

if len(matricula_sin_espacios) == 7 and matricula_sin_espacios.isalpha[4,7]:
    print("Correcto")
else:
    print("Incorrecto.")