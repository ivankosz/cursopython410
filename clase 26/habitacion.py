
class Habitacion:

    def __init__(self, un_precio, un_numero) -> None:
        self.estado = True
        self.precio = un_precio
        self.numero = un_numero
    
    def get_estado (self):
        if self.estado:
            return "Ocupado"
        else:
            return "Disponible"

    def __str__(self):
        return f"Habitacion {self.numero}, estado: {self.get_estado()}, precio: ${self.precio}"