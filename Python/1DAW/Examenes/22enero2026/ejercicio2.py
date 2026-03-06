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

def elMasInteligente(personaje1,personaje2):
    if personaje1[4] > personaje2[4]:
        print(personaje1)
    else:
        print(personaje2)

def estaVivo(personaje):
    if personaje[5] > 0:
        return True
    else:
        return False

def ataque(personaje1,personaje2):
    if personaje1 == personaje2:
        print(f"{personaje1[0]} no puede combatir contra si mismo.")
    else:
        ataque = personaje1[5]/2
        personaje2[5] = personaje2[5] - ataque
        return personaje2

personaje1= construyePersonaje(nombres,adjetivos,clases,razas)
personaje2= construyePersonaje(nombres,adjetivos,clases,razas)

print(ataque(personaje1,personaje2))

