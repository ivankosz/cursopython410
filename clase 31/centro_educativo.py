
class CentroEducativo:
    
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede
        
        self.asignaturas = []
        self.empleados = []
        self.estudiantes = []
        
    def set_asignatura (self, asignatura):
        self.asignaturas.append (asignatura)
        
    def set_docente (self, empleado):
        self.empleados.append(empleado)
    
    def set_nodocente(self, empleado):
        self.empleados.append(empleado)
        
    def set_estudiante (self, estudiante):
        self.estudiantes.append(estudiante)
                
    def aumentar_sueldo (self, porcentaje):
        """se aumenta todos los sueldos en un porcentaje"""
        for e in self.empleados:
            e.sueldo *= (1+(porcentaje/100))
    
    def docente_dicta (self, dni):
        from persona import Docente
        for e in self.empleados:
            if e.dni == dni and isinstance(e, Docente):
                return f"{e.nombre} dicta {e.asignatura.nombre}"
    
    def gasto_en_sueldos (self):
        total_sueldos = 0
        for e in self.empleados:
            total_sueldos += e.sueldo
        return "{0:.2f}".format(total_sueldos)
    
    def cursan_asignaturas (self, asignatura):
        for e in self.asignaturas:
            if e.nombre == asignatura:
                return e.get_estudiantes()
