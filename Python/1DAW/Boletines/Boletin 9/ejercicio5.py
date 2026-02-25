frutas = {"Aguacate":4.35,
          "Mandarina":2.60,
          "Kiwi": 3.75,
          "Naranja":1.80}

def comprarFruta(nomFruta, kgFruta):
    try:
        kgFruta = float(kgFruta)
        if frutas.get(nomFruta) is None:
            print("No tenemos eso...")
        else:
            precio = frutas.get(nomFruta) * kgFruta
            print(f"{kgFruta}kg de {nomFruta} cuestan {round(precio,2)}€")
    except ValueError,TypeError:
        print("Has introducido la cantidad incorrectamente")






nomFruta = input("¿Qué fruta quieres comprar?")
if nomFruta.lower() != "fin":
    nomFruta = nomFruta.capitalize()
    kgFruta = input("¿Cuantos kilos quieres?")
    comprarFruta(nomFruta,kgFruta)
