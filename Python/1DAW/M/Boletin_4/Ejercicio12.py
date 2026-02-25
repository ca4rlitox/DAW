"""Crear un programa que lea un número de año por teclado e indique si es bisiesto o no.
Un año bisiesto es aquel que es divisible por 4, siempre y cuando no lo sea por 100. La
excepción a esta regla son los años múltiplos de 400, que siempre son bisiestos."""

año=int(input("Introduce un año: "))

if (año%4==0 and año%100 != 0) or (año%400==0):
    print("El año",año,"es bisiesto")
else:
    print("El año",año,"no es bisiesto")