"""6. Escribir un programa que pida por teclado una cadena de texto y la separe en dos
distintas. En la primera de ellas estarían las letras que ocupan una posición par y en la
segunda las que ocupan una posición impar. Por ejemplo, si el usuario escribe Hola
Mundo la primera cadena sería Hl ud y la segunda oaMno
"""
"""
texto=input("Ingresa una cadena de texto: ")
print(texto[::2])
print(texto[1::2])
"""

"""
7. Escribir un programa que pida por teclado una cadena de texto y la escriba con el
alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
las vocales pueden estar escritas en mayúsculas o minúsculas, pero no hace falta que
tengas en cuenta que además podrían ir acentuadas
"""
"""texto=input("Ingresa una cadena de texto: ")

print(texto.replace("a","4").replace("e","3")
      .replace("i","1").replace("o","0").replace("A","4")
      .replace("E","3").replace("I","1").replace("O","0"))
"""

"""
8. Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”.
"""
"""
texto=input("Ingresa una cadena de texto: ")
print(texto.replace("a","").replace("e","")
      .replace("i","").replace("o","").replace("u","")
      .replace("A","").replace("E","")
      .replace("I","").replace("O","").replace("U",""))
"""

"""
9. Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
nuestro destino (París, Roma, Santiago de Chile o Tokio)"""

destinosTuristicos=input("Ingresa el destino que te gustaria visitar: \n"
                         "Ingresa 1 para Francia \n"
                         "Ingresa 2 para Italia \n"
                         "Ingresa 3 para Chile \n"
                         "Ingresa 4 para Japon \n")

match destinosTuristicos:
    case "1":
        print("La capital de Francia es Paris")
    case "2":
        print("La capital de Italia es Roma")
    case "3":
        print("La capital de Chile es Santiago")
    case "4":
        print("La capital de Japon es Tokio")
