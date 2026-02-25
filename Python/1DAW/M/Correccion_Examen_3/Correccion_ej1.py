import random

def fuerza():
    return random.randint(50,100)

def inteligencia(f):
    return 100-f

def resistencia(f):
    return f*2

def construyePersonaje(nombres,adjetivos,clases,razas):
    personaje=[]
    nombre=random.choice(nombres)
    adjetivo=random.choice(adjetivos)
    personaje.append(nombre + " " + adjetivo)
    personaje.append(random.choice(clases))
    personaje.append(random.choice(razas))
    f=fuerza()
    personaje.append(f)
    personaje.append(inteligencia(f))
    personaje.append(resistencia(f))
    return personaje


nombres=["Gimbli","Legolas","Frodo","Gandalf"]
adjetivos=["Barbarroja","Pies Grandes","el Gris","Piedradura","el Deslumbrante"]
clases=["Mago","Guerrero","Ladron","Bardo"]
razas=["Elfo","Humano","Enano"]

print(construyePersonaje(nombres,adjetivos,clases,razas))