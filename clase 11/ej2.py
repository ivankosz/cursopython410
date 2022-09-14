
numeros=list()
while True:
    user=int(input("Numeros ganadores: "))
    if user== -1:
        break
    numeros.append(user)
numeros.sort()
print(numeros)

