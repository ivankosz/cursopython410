materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
c=0
c2=0
for i in materias:
    nota=int(input(f"Nota {i}: "))
    notas.append(nota) 
    c+=nota
promedio=c/len(materias)
print(f"Promedio: {promedio}")
for n in notas:
    if n<promedio:
        c2+=1
print(f"Cantidad de materias debajo del promedio: {c2}")
