
participantes=list()
for i in range (8):
    print('datos pokemon')
    name=input("name: ")
    tipo=input("type: ")
    lvl= int(input("lvl: "))
    datos= (name, tipo, lvl)
    participantes.append(datos)
for pkm, tipo, lvl in participantes:
    print(f'Pokemon: {pkm}. Tipo: {tipo}. Nivel: {lvl}.')