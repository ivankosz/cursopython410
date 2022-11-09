import json
import random

def menu ():
    print("Elija una categoria para jugar:")
    print("1.Peliculas\n2.Refranes\n3.Mostrar puntajes\n4.Salir")

def abrir_json(file):
    try:
        f = open(file, "r")
        d = json.load(f)
        f.close()
        return d
    except FileNotFoundError:
        f = open(file, "w")
        d = dict()
        json.dump(d, f)
        f.close()
        return d

def guardar_json(d,file):
    f = open(file, "w+")
    json.dump(d, f)
    f.close()
    
def mostrar_puntajes ():
    with open ("puntajes_adivina.json", "r") as f:
        d = json.load(f)
        for k, v in d.items():
            print(k, v)
        
def puntaje (correctas):
    valor = 200
    return correctas*valor

def guardar_puntaje (jugador, puntos):
    try:
        f= open("puntajes_adivina.json", "r")
        d= json.load(f)
        d[jugador]=puntos
        f.close()
        f = open("puntajes_adivina.json", "w")
        json.dump(d, f)
        f.close()
              
    except FileNotFoundError:
        f = open("puntajes_adivina.json", "w")
        d=dict()
        d[jugador]=puntos
        json.dump(d, f)
        f.close() 

if __name__=="__main__":
    name = input("Ingresa tu nombre: ")
    menu()
    d = abrir_json("emojis_ascii.json")
    correctas = 0
    entry = input("> ")
    while entry !="4":
        if entry =="1":
            for categoria in d.keys():           
                l = random.sample(list(d["peliculas"].items()), 5)
            print("Adivina la película!")
            for a, b in l:
                print(b)
                entry2 = input("> ")
                if entry2 == a:
                    correctas+=1
                    print("Acertaste!")
                else:
                    print(f"La película era {a}")
            print(f"tu puntaje fue de {puntaje(correctas)}")
            guardar_puntaje(name, puntaje(correctas))
        elif entry =="2":
            for categoria in d.keys():           
                l = random.sample(list(d["refranes"].items()), 5)
            print("Adivina el refran!")
            for a, b in l:
                print(b)
                entry2 = input("> ")
                if entry2 == a:
                    correctas+=1    
                    print("Acertaste!")
                else:
                    print(f"El refran era {a}")
            print(f"tu puntaje fue de {puntaje(correctas)}")
            guardar_puntaje(name, puntaje(correctas))
        elif entry == "3":
            mostrar_puntajes()
            input()
        menu()
        entry = input("> ")