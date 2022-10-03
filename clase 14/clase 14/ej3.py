
lista=list()    
while True:
    user=input('pkm: ')
    lista.append(user)
    if user == 'ekans':
        break
for i in lista:
    print(i.capitalize(), i[::-1].capitalize())