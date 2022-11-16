import random

class MiembroBiblioteca:
    
    def __init__(self, un_dni, un_nombre, un_mail, un_password):
        self.dni = un_dni
        self.nombre = un_nombre
        self.mail = un_mail
        self.__password = un_password
        self.__libros = []
    
    # def set_id (self):
    #     for a in range (7):
    #         cadena = str(random.randint(0,9))
    #     self.id = "00/"+cadena
        
    def set_libro (self, un_libro):
        self.__libros.append(un_libro)
        
                