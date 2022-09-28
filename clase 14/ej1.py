
user=int(input("Ingrese un num: "))
numeros=list()
while user != -1:
    numeros.append(user)
    user=int(input("Ingrese un num: "))
numeros.reverse()
for i in numeros:
    print (i)
