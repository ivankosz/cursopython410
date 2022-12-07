
class Asignatura ():

    def __init__(self, fecha_inicio, fecha_fin, nombre ):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.nombre = nombre
        
        self.estudiantes = []
    
    def get_asignatura (self):
        return [self.nombre, self.fecha_inicio, self.fecha_fin]
    
    
    def set_estudiante (self, estudiante):
        self.estudiantes.append(estudiante)
        
    def get_estudiantes (self):
        nombres = []
        for estudiante in self.estudiantes:
            nombres.append(estudiante.nombre)
        return nombres
    
