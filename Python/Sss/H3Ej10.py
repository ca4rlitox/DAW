# Escribe un programa que valide si un NIF español introducido por teclado es correcto.
# La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
# ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar escrita en mayúsculas o minúsculas

nif = input("Introduce tu NIF: ")

if len(nif) == 9:
    numeros = nif[:8]
    letra = nif[8]

    if numeros.isdigit() and letra.isalpha():
        print("El NIF tiene un formato correcto.")
    else:
        print("El NIF no es válido: los primeros 8 deben ser números y el último una letra.")
else:
    print("El NIF no es válido: debe tener exactamente 9 caracteres.")