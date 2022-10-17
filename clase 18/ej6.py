import string

cadena = "Todas las hojas son del viento ya que las mueve hasta en la muerte. Todas las hojas son del viento menos la luz del sol"


def string_a_dict (cadena_string):
    diccionario = dict()
    cadenita = (''.join([i for i in cadena_string if i not in string.punctuation])).lower()
    print(cadenita)
    for palabra in cadenita.split():
        frecuencia = cadenita.count(palabra)
        diccionario[palabra] = frecuencia
    return diccionario

def dict_a_tuple (diccionario):
    max= -1
    for key, value in diccionario.items():
        if value > max:
            max = value
            palabra =(key, value)
    return palabra

print(string_a_dict(cadena))
mi_diccionario= string_a_dict(cadena)
print (dict_a_tuple(mi_diccionario))