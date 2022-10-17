#usando los datos cargados en el ejercicio anterior, imprimir en pantalla las 4 batallas a realizarse en la primera ronda elegidas de forma aleatoria (shuffle)

from random import shuffle
from random import choice

pokemons = [('ekans', 'veneno', 68), ('pikachu', 'electrico', 45),('raichu', 'electrico', 90),('ratata', 'normal', 5)]

participantes = pokemons.copy()
def seleccionar_participantes (lista):
    shuffle(lista)
    participante = choice(lista) 
    lista.remove(participante)
    return participante

for a in range (len(pokemons)):
    pkm= seleccionar_participantes(participantes)