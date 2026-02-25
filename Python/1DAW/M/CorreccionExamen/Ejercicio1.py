"""1.  Queremos hacer un programa en Python que genere de forma aleatoria códigos con un
determinado formato que debe de ser como sigue:
 45723-01204-00551-19665-36640
 Como ves, la clave está formada por cinco grupos de cinco números cada una separadas por un
guión. Tu programa debería de generar de forma automática cuatro claves generadas aleatoriamente
con ese formato cada vez que se ejecute.  Fíjate que los primeros números de cada segmento
pueden ser ceros!
 A continuación tienes un ejemplo de ejecución:
 Generando claves en el formato solicitado:
 45723-01204-00551-19665-36640
 00076-45672-19665-61640-66511
 19446-65366-40457-00812-04975
 61640-07551-36640-12376-63120
 NOTA IMPORTANTE:
 No se admitirá por buena ningúna solución que no use bucles para todo lo que se pueda"""

import random

for i in range (0,4):
    for j in range(0,5):
        for k in range(0,5):
            print(random.randint(0,9), end="")
        if j<4:
            print("-",end="")

    print()