
pokemons = [('ekans', 'veneno', 68), ('pikachu', 'electrico', 45),('raichu', 'electrico', 90)]

def mayor_nivel (lista):
    max = -1
    max_pkm= ""
    for poke, tipo, lvl in lista:
        if lvl > max:
            max = lvl
            pokemon = (poke, tipo,lvl)
    print (pokemon)
    return pokemon

copia_lista = pokemons.copy()
for i in range (len(pokemons)):
    copia_lista.remove(mayor_nivel(copia_lista))
copia_lista = pokemons.copy()
