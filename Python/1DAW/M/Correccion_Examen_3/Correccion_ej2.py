


personaje1=['Gimbli el Gris', 'Bardo', 'Enano', 77, 23, 154]
personaje2=['Frodo el Gris', 'Ladron', 'Enano', 52, 48, 104]
personaje3=['Frodo Piedradura', 'Mago', 'Elfo', 58, 42, 116]



def esMasInteligente(*personajes):
    elQueMas=personajes[0]
    for p in personajes[1:]:
        if(p[4]>elQueMas[4]):
            elQueMas=p
    return elQueMas

def estaVivo(personaje):
    vivo=True
    if personaje[5]<=0:
        vivo=False
    return vivo

def ataque(p1,p2):
    danio= int(p1[3]/2)
    p2[5]-=danio

def recuperaResistencia(personaje, cant):
    nuevaResistencia=personaje[5]+cant
    if(nuevaResistencia> 2*personaje[3]):
        nuevaResistencia = 2*personaje[3]
        print(personaje[0]," no puede tener mas de ",)

print(esMasInteligente(personaje1,personaje2,personaje3))
print(estaVivo(personaje3))
print(personaje2)
ataque(personaje1,personaje2)
print(personaje2)
recuperaResistencia(personaje2, 20)
print(personaje2)
