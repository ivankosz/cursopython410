
participantes=list()
part= int(input("Cantidad participantes: "))
for i in range (part):
    print('datos pokemon')
    name=input("name: ")
    tipo=input("type: ")
    lvl= int(input("lvl: "))
    datos= (name, tipo, lvl)
    participantes.append(datos)
for pkm, tipo, lvl in participantes:
    print(f'Pokemon: {pkm}. Tipo: {tipo}. Nivel: {lvl}.')