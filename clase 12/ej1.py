import random
import string

nombre= input("Ingrese un nombre: ")
usuarios = []
pool= string.ascii_letters + string.digits

while nombre != "-1":
    l=list()
    l.append(nombre)
    password=""
    for i in range (10):
        char= random.choice(pool)
        password += char
    l.append(password)
    usuarios.append(l)
    nombre= input("Ingrese un nombre: ")

for usuario, contraseña in usuarios:
    print(f"Usuario: {usuario}/ Contraseña: {contraseña}")
