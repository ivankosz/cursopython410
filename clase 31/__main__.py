from centro_educativo import CentroEducativo
from asignatura import Asignatura
from persona import Estudiante, Empleado, Docente, NoDocente

#creacion del establecimiento
centro = CentroEducativo("CFP 410 Omar Nuñez", "7 1429")

#creacion empleados
prof1 = Docente("33555116", "Diego Rosales", "25/8/1989", "44 555", 90000, "27-24555116-2", "Licenciado en sistemas")
prof2 = Docente("30441023", "Crisitan Giambruni", "14/6/1985", "16 258", 100000, "20-30441023-0", "Licenciado en informática")

#creacion de los cursos/asignaturas
curso1 = Asignatura("3/3/22", "12/12/22", "Programador")
curso2 = Asignatura("6/8/22", "12/12/22", "Python")

#asignar docente asignatura
prof1.set_asignatura(curso2)
prof2.set_asignatura(curso1)

#carga de asignaturas en el centro
centro.set_asignatura(curso1)
centro.set_asignatura(curso2)

#carga de docentes en el centro
centro.set_docente(prof1)
centro.set_docente(prof2)

#creacion de alumnos
#dos enuna,dos en otra, y uno en ambas asignaturas
alum1 = Estudiante("25777415","Lucia Maresca", "18/5/1978", "45 789", "4/3/2022")
alum2 = Estudiante("33589965","Nahuel Garzia", "25/9/1986", "22 66", "16/4/2022")
alum3 = Estudiante("34442369","Daniela Nuñez", "1/2/1990", "16 449", "15/8/2022")
alum4 = Estudiante("96558447","Dante Aligheri", "4/10/1999", "7 1500", "4/3/2022")
alum5 = Estudiante("29114777","Martina Muscatto", "19/6/1983", "66 123", "4/3/2022")

curso1.set_estudiante(alum1)
curso1.set_estudiante(alum4)
curso1.set_estudiante(alum5)
curso2.set_estudiante(alum3)
curso2.set_estudiante(alum2)
curso2.set_estudiante(alum5)

print(curso1.get_estudiantes())
print(curso2.get_estudiantes())

#print(prof1.evaluar())

print(prof1.get_sueldo())
print(prof2.get_sueldo())

centro.aumentar_sueldo(15)

print(prof1.get_sueldo())
print(prof2.get_sueldo())

print(centro.docente_dicta("33555116"))

print(centro.gasto_en_sueldos())

print(centro.cursan_asignaturas("Python"))