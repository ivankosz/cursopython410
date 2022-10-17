from math import pi

def calcular_area_circulo (radio =12):
    area = pi*radio**2
    return area

def calcular_volumen_cilindro (altura =25):
    area_circulo =calcular_area_circulo()
    vol = area_circulo *altura
    return vol, area_circulo

print (calcular_volumen_cilindro())    


