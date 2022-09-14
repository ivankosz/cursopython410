materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
APROBADO=7
mat=[]
c=0
for i in materias:
    l=[]
    nota=int(input(f"Nota {i}: "))
    if nota <APROBADO:
        l.append(i)
        l.append(nota)
        mat.append(l)
        c+=1
if c!=0:
    print("Materias Desaprobadas")
    for materia, nota in mat:
        print(f"{materia}: {nota}")
