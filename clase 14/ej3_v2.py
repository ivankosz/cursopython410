import csv

try:
    file= open('pokemon151.csv')
except FileNotFoundError:
    print('no se encontró la pokedex')
pokedex= csv.DictReader(file)   
pokeball=list()
while True:
    pkm= input("pkm: ").capitalize()
    for i in pokedex:
        if i['Name'] ==pkm:
            pokeball.append(pkm)
            if pkm == 'Ekans':
                break
        else:
            print('No se reconoce ese pokemon')
print(pokeball)