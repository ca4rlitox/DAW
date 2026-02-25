biblioteca = {
    "Cien años de soledad": {"novela", "realismo mágico", "clásico"},
    "El principito": {"infantil", "filosofía", "clásico"},
    "1984": {"distopía", "política", "clásico"},
    "Harry Potter": {"fantasía", "juvenil", "aventura"},
    "El hobbit": {"fantasía", "aventura", "clásico"},
    "La sombra del viento": {"fantasía", "juvenil", "aventura"},
}

def libros_por_genero(genero):
    libros_del_genero=set()
    for titulo, caracteristicas in biblioteca.items():
        for c in caracteristicas:
            if c==genero:
                libros_del_genero.add(titulo)

    return libros_del_genero

def generos_comunes(titulo1, titulo2):
    if titulo1 in biblioteca and titulo2 in biblioteca:
        return biblioteca[titulo1] & biblioteca[titulo2]
    return None

def todos_los_generos():
    total_generos=set()
    for titulo in biblioteca:
        total_generos=total_generos | biblioteca[titulo]
    return total_generos

def recomendar_por_gusto(generos_usuario):
    libros_recomendados=[]
    for titulo in biblioteca:
        if generos_usuario & biblioteca[titulo]:
            libros_recomendados.append(titulo)
    return libros_recomendados

def libros_unicos_genero():
    es_unico=False
    print("Libros que tienen géneros únicos:")
    for titulo in biblioteca:
        for t in biblioteca:
            if t!=titulo:
                if biblioteca[t] - biblioteca[titulo]:
                    es_unico=True
                else:
                    es_unico=False
        if es_unico:
            print(titulo)

print(libros_por_genero("novela"))
print(generos_comunes("La sombra del viento","Cien años de soledad"))
print(todos_los_generos())
print(recomendar_por_gusto({"novela","juvenil","fantasía"}))
libros_unicos_genero()