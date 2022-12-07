
class Persona:
    
    def __init__(self, dni, nombre, fecha_nac, domicilio):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.domicilio = domicilio
        


class Empleado (Persona):
    
    def __init__(self, dni, nombre, fecha_nac, domicilio, sueldo, cuil):
        super().__init__(dni, nombre, fecha_nac, domicilio)
        self.sueldo = sueldo
        self.cuil = cuil
        
    def get_sueldo (self):
        
        return "{0:.2f}".format(self.sueldo)
    

class Estudiante (Persona):
    
    def __init__(self, dni, nombre, fecha_nac, domicilio, fecha_ingreso):
        super().__init__(dni, nombre, fecha_nac, domicilio)
        self.fecha_ingreso = fecha_ingreso
        
        self.asignaturas = []
        
    def set_asignatura (self, asignatura):
        
        self.asignaturas.append(asignatura)
    
    def get_asignaturas (self):
        return self.asignaturas
    
class Docente (Empleado):
    
    def __init__(self, dni, nombre, fecha_nac, domicilio, sueldo, cuil, titulo):
        super().__init__(dni, nombre, fecha_nac, domicilio, sueldo, cuil)
        self.titulo = titulo
        
        self.asignatura = None
    
    def set_asignatura (self, asignatura):
        self.asignatura = asignatura
        
    def evaluar (self):
        notas = []
        for i in self.asignatura.estudiantes:
            nota = input(f"Nota {i.nombre}: ")
            tupla = (i.nombre, nota)
            notas.append(tupla)
        return notas
        

class NoDocente (Empleado):
    
    def __init__(self, dni, nombre, fecha_nac, domicilio, sueldo, cuil, cargo):
        super().__init__(dni, nombre, fecha_nac, domicilio, sueldo, cuil)
        self.cargo = cargo
    