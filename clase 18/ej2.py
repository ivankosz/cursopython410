
def calcular_iva (factura, iva = 21):
    total = factura + (factura*(iva/100))
    return total

print(calcular_iva(1000, 80))