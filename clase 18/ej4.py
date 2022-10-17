
def calcular_promedio (lista):
    res =0
    for numero in lista:
        res +=numero
    return res/len(lista)

muestra_numeros = [2, 5, 7, 10, 8]
print(calcular_promedio(muestra_numeros))