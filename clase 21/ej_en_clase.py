numeros = [num for num in range (1, 11)]
print (numeros)
otra_lista = list(map(lambda n:(3*n)+1, numeros))
print (otra_lista)
filter_lista = list(filter(lambda n: n>=9 and n<=20, otra_lista))
print(filter_lista)
