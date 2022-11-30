
class Huesped:

    def __init__(self, un_nombre, un_apellido) -> None:
        self.nombre = un_nombre
        self.apellido = un_apellido

    def __str__(self):
        return f"Huesped {self.nombre} {self.apellido}"
    
    def set_habitacion (self, una_habitacion, cant_noches):
        self.habitacion = una_habitacion
        self.noches = cant_noches

    def get_habitacion (self):
        return f"Habitacion: {self.habitacion.numero}, noches: {self.noches}"