
num = input("Ingrese sus numeros separados por coma: ")
numeros= num.split(",")
lista= [int(string) for string in numeros]
promedio= sum(lista)/len(lista)
print(lista)
print(promedio)