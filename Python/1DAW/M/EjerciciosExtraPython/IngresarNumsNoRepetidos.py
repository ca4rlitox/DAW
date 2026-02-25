"""Ingresar números hasta escribir “fin” y guardar solo los que no se repiten."""
nums=input("Ingrese un número. Para terminar ingrese 'fin'\n")
numeros=[]
while nums != 'fin':
    if nums.isdigit():
        nums=int(nums)
        if nums not in numeros:
            numeros.append(int(nums))
    else:
        print("valor ingresado inválido. por favor ingrese un número. Para terminar"
              "ingrese 'fin'\n")
    nums = input("Ingrese un número. Para terminar ingrese 'fin'\n")

print(numeros)


