estudiantes = {
    "Ana": (7.5, 8.0, 9.0),
    "Luis": (5.0, 6.5, 4.0),
    "María": (9.0, 9.5, 10.0),
    "Pedro": (4.0, 3.5, 5.0)
}

def calcula_media(nombre):
    if nombre in estudiantes:
        return round(sum(estudiantes[nombre]) / len(estudiantes[nombre]),2)
    return None

def aprobados_suspensos():
    aprobados={}
    suspensos={}
    for nombre in estudiantes:
        media=calcula_media(nombre)
        if media >= 5:
            aprobados[nombre]=media
        else:
            suspensos[nombre]=media
    print("APROBADOS:")
    for nombre, media in aprobados.items():
        print(f"- {nombre}: {media}")
    print("SUSPENSOS:")
    for nombre, media in suspensos.items():
        print(f"- {nombre}: {media}")

def mejor_estudiante():
    mejor=0
    for nombre, nota in estudiantes.items():
        if calcula_media(nombre) > mejor:
            mejor=calcula_media(nombre)
    for nombre,nota in estudiantes.items():
        if calcula_media(nombre) == mejor:
            return nombre

def agregar_nota(nombre,trimestre,nota:float):
    if nombre in estudiantes:
        notas_lista=list(estudiantes[nombre])
        notas_lista[trimestre-1]=nota
        estudiantes[nombre]=tuple(notas_lista)


aprobados_suspensos()
print(mejor_estudiante())
agregar_nota("Luis",2,8)
