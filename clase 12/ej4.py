from random import choice

lugares=[]
while True:
    lugar= input("Ingrese un lugar a visitar: ")
    if lugar == "fin":
        break
    lugares.append(lugar)
print(choice(lugares))
