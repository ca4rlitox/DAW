import random

clientes = ["Diego Norrea", "Ines Perado", "Demetrio Imedio",
            "Roberto Rija", "Ruben Tosidad", "Armando Adistancia",
            "German Tequilla"]

try:
    premiosArepartir = int(input("¿Cuántos premios vas a repartir?"))
    if premiosArepartir ==  len(clientes):
        print(f"Tienes solo {len(clientes)}. Les puedes dar un premio a cada uno.")
    elif premiosArepartir > len(clientes):
        print(f"Tienes sólo {len(clientes)} clientes. Les puedes dar un premio a cada uno."
              f"Te sobran {premiosArepartir-len(clientes)} premios sin repartir. ¡Guárdalos para el siguiente sorteo!")
    else:
        print("Los/as afortunados/as son:\n")
        for i in range(premiosArepartir):
            afortunado = random.choice(clientes)
            afortunado = afortunado.split(" ")
            print(afortunado[1],", ",afortunado[0],sep="")
        print(f"\n{len(clientes)-premiosArepartir} clientes se han quedado sin premio. ¡Mucha suerte en el próximo sorteo!")

except:
    print("El número de premios ha de ser entero positivo mayor o igual a 1")