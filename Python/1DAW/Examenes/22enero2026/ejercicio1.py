import random

nombres = ["Gimli", "Legolas", "Frodo", "Gandalf"]
adjetivos = ["Barbarroja", "Pies Grandes", "el Gris", "Piedradura","el Deslumbrante"]
clases = ["Mago", "Guerrero", "Ladrón", "Bardo"]
razas = ["Elfo", "Humano", "Enano"]

def fuerzaFuncion():
    fuerza = int(random.randint(0,50)+50)
    return fuerza

def inteligenciaFuncion(fuerza):
    inteligencia = 100 - fuerza
    return inteligencia

def resistenciaFuncion(fuerza):
    resistencia = fuerza * 2
    return resistencia

def construyePersonaje(nombres,adjetivos,clases, razas):
    nombre = random.choice(nombres)+" "+random.choice(adjetivos)
    clase = random.choice(clases)
    raza = random.choice(razas)
    fuerza = fuerzaFuncion()
    inteligencia = inteligenciaFuncion(fuerza)
    resistencia = resistenciaFuncion(fuerza)
    return nombre,clase,raza,fuerza,inteligencia,resistencia

print(construyePersonaje(nombres,adjetivos,clases,razas))