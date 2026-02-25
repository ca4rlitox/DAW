"""1. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
ninguno de ellos esté repetido (simulando una lotería primitiva)."""

import random

numeros= random.sample(range(1,50),6)
print(numeros)