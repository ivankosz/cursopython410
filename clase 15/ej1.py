def mayor_nota (lista):
    max = -999
    for nom, nota in lista:
        if nota > max:
            max = nota
            alumno = (nom, nota)
    print(alumno)
    return alumno


def mayor_nom (lista):
    min= "z"
    for nom, nota in lista:
        if nom < min:
            min = nom
            alumno = (nom, nota)
    print(alumno)
    return alumno

def promedio_alumnos (lista):
    suma = 0
    for nom, nota in lista:
        suma += nota
    promedio = suma/len(lista)
    print (promedio)
    return promedio

def eliminar_alumno (lista):
    x= input("Alumno a eliminar: ")
    for nom, nota in lista:
        if x.lower() == nom.lower():
            alumno = (nom, nota)
    lista.remove(alumno)

def buscar_alumno (lista):
    x= input("Buscar alumno: ")
    for nom, nota in lista:
        if x.lower() == nom.lower():
            buscar= (nom, nota)
            print (buscar)
    return buscar
    
alumnos = list()

nombre = input("nombre alumno: ")
while nombre != "-1":
    nota = int(input(f"nota de {nombre}: "))
    alumnos.append((nombre,nota))
    nombre = input("nombre alumno: ")

print(alumnos)

menu = """Menu
1) Mostrar listado ordenado por nota
2) Mostrar listado ordenado por nombre
3) Buscar alumno/a
4) Eliminar alumno/a
5) Mostrar promedio
6) Salir
"""

print(menu)

opcion= int(input("Ingrese una opcion: "))

copia_lista = alumnos.copy()

while opcion != 6:
    if opcion == 1:
        for i in range (len(alumnos)):
            copia_lista.remove(mayor_nota(copia_lista))
        copia_lista = alumnos.copy()
    if opcion == 2:
        for i in range (len(alumnos)):
            copia_lista.remove(mayor_nom(copia_lista))
        copia_lista = alumnos.copy()
    elif opcion == 3:
        buscar_alumno(alumnos)
    elif opcion == 4:
        eliminar_alumno(alumnos)
    elif opcion == 5:
        promedio_alumnos (alumnos)
    
    print(menu)
    opcion= int(input("Ingrese una opcion: "))
    
   