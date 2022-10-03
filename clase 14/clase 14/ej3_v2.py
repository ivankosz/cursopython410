import csv

with open ('./clase 14/pokemon151.csv') as archivo:
    pokedex= csv.DictReader(archivo)   
    pokeball=list()
    print(pokedex)
    while True:
        pkm= input("pkm: ").capitalize()
        choose = False
        for i in pokedex:
            if i['Name'] ==pkm:
                pokeball.append(pkm)
                choose = True
                if pkm == 'Ekans':
                    break
        if choose:
            print("No se reconoce ese pokemon")
            
    print(pokeball)