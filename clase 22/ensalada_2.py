import random
import json

def mezclar (lista):
    #mezcla las palabras en una lista, y devuelve una lista con ambas versiones de la palabra
    lista_mezclada=list()
    for a in lista:
        palabra_mezclada = "".join(random.sample(a, len(a)))
        while palabra_mezclada == a:
            palabra_mezclada = "".join(random.sample(a, len(a)))
        lista_mezclada.append((a, palabra_mezclada))
    return(lista_mezclada)
            
def ensalada_de_letras(category):
    #diccionario de categorias
    try:
        archivo=open("palabras.json", "r")
        d=json.load(archivo)

        if category == 1:
            palabras = random.sample(d["colores"], 5)
            return mezclar(palabras)        
        elif category ==2:
            palabras = random.sample(d["animales"], 5)
            return mezclar(palabras) 
        elif category ==3:
            palabras = random.sample(d["paises"], 5)
            return mezclar(palabras)
        elif category ==4:
            palabras = random.sample(d["frutas"], 5)
            return mezclar(palabras)
        
        archivo.close()
    except FileNotFoundError:
        print("No se encontró el archivo json")
    except:
        print("Oops")
    else:
        print("no hubo ningun error")
    finally:
        print("Se ejecuta siempre")

def puntaje (cantidad):
    #calcula el puntaje segun la cantidad de aciertos
    puntos_acierto= 200   
    return cantidad*puntos_acierto

def guardar_puntaje (jugador, puntos):
    puntajes_json= {
        "jugador": jugador,
        "puntaje": puntos,
    }
    try:
        archivo= open("puntajes.json", "r+")
        r = json.load(archivo)
        json.dump(puntajes_json, archivo)
              
    except FileNotFoundError:
        print("no se encontro el archivo json")
    else:            
        archivo= open("puntajes.json", "w")
        json.dump(puntajes_json, archivo)
        
#jugar
def intro ():
    print("""
        Bienvenido a Ensalada de Letras
        deberás elegir una categoria y adivinar
        la palabra que se muestra desordenada.
        Tendrás 5 palabras para adivinar.
        Acierta mas palabras para ganar. Cada acierto
        tendra un valor de 100 puntos. 
        """)


intro()
player = input("ingresa tu nombre: ")
while True:
    elegir_cat = int(input("elija una categoria: \n1.colores\n2.animales\n3.paises\n4.frutas\nopcion: "))
    lista= ensalada_de_letras(elegir_cat)
    copia_lista = lista.copy()

    correctas =0

    for palabra, palabra_mezclada in lista:
        print(palabra_mezclada.upper())
        usuario = input("Ordene la palabra: ").lower()
        if usuario == palabra:
            correctas +=1
        else:
            print(f"Error. La palabra era {palabra}")

    print(f"Bien {player}, acertaste {correctas} {'palabra' if correctas ==1 else 'palabras'}. Tu puntaje es de {puntaje(correctas)}")

    guardar_puntaje(player, puntaje(correctas))
    seguir_jugando =input("Desea volver a jugar?\n-si\n-no\n").lower()
    while seguir_jugando != "si" and seguir_jugando !="no":
        print("Elija si para seguir jugando, o no para terminar el programa")
        seguir_jugando =input("Desea volver a jugar?\n-si\n-no\n").lower()
    if seguir_jugando == "no" :
        break
    elif seguir_jugando == "si":
        pass