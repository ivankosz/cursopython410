
from random import choice
class Hotel:

    def __init__(self, un_nombre, una_direccion, un_telefono):
        self.nombre= un_nombre
        self.direccion= una_direccion
        self.telefono = un_telefono

        self.habitaciones = []
        self.huespedes = []

        self.registro = dict ()

    def set_habitacion (self, una_habitacion):
        self.habitaciones.append(una_habitacion)
    
    def set_huesped (self, un_huesped):
        self.huespedes.append(un_huesped)

    def del_huesped (self, un_huesped):
        self.huespedes.remove(un_huesped)
    
    def get_habitaciones_disponibles (self):
        habitaciones_disponibles = []
        for hab in self.habitaciones:
            if hab.estado:
                habitaciones_disponibles.append(hab)
        return habitaciones_disponibles
                
    
    def set_registro_huesped (self, un_huesped, una_habitacion, cant_noches):
        self.huespedes.append(un_huesped)
        un_huesped.set_habitacion(una_habitacion, cant_noches)
        un_huesped.habitacion.estado = False

if __name__ == "__main__":
    pass