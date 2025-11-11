# if / else tomar una decisión en función de lo que hata
# for nos permiten repetir algo un número de veces (número de operaciones determinado)
# while nos permiten repetir algo un número de veces (número de operaciones indeterminado)
#do/while se obliga a que al menos una vez se ejecuten las instrucciones (EN PYTHON NO ESTÁ)
#Switch/Match -> tomar una decisión en función de una variable

#if/elif/else
#import random

#dado = random.randint(1,6)

#if dado <= 2:
#    print("Has sacado un", dado, "le has fallado...")
#elif dado <=4:
#    print("Has sacado un", dado, "le has herido :D")
#else:
#    print("Has sacado un", dado, "le has matado!!!")
#print("Fin del dado")

#while
print("Inicio")

numero = 1
while numero <= 10000:
    print(numero)
    numero+=1
print("FIN")
