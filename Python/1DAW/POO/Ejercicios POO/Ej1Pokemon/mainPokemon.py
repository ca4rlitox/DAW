from Pokemon import Pokemon,Entrenador,Equipo

poke1 = Pokemon(493,"Charmander",4,2,5,2,"maricon")
poke2 = Pokemon(584,"Bulbasour",4,2,5,2,"alvestruz")
poke3 = Pokemon(142,"Pikachu",4,2,5,2,"mecago")
entre = Entrenador(1,"Malika",1,4,4,6,"chupadora")

equipo1 = Equipo(entre,poke1,poke2,poke3)

Equipo.verDatos(equipo1)