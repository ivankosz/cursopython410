
class Biblioteca:
        
    def __init__(self, un_nombre, una_direccion, un_telefono):
        self.nombre = un_nombre
        self.dir = una_direccion
        self.tel = un_telefono
        self.__inventario = []
        self.__miembros = []
        self.__prestamos =dict()
        
    def set_inventario (self, un_libro):
        self.__inventario.append(un_libro)
    
    def set_miembro (self, un_miembro):
        self.__miembros.append(un_miembro)
    
    def get_cant_inventario (self):
        return len(self.__inventario)
    
    def get_cant_miembros (self):
        return len(self.__miembros)
    
    def print_prestamos (self):
        for miembro, libro in self.__prestamos.items():
            print(f"{miembro.nombre}: {libro.titulo}")
    
    def print_inventario (self):
        for libro in self.__inventario:
            print(f"{libro.titulo} ({libro.isbn})")
            
    def get_inventario (self):
        return self.__inventario
    
    def get_prestamos(self):
        return self.__prestamos
    
    def set_prestamos (self, libro, miembro):
        libro.set_prestamos()
        self.__inventario.remove(libro)
        self.__prestamos[miembro]=libro
    
    def set_devoluciones (self, libro, miembro):
        libro.set_devoluciones()
        self.__inventario.append(libro)
        self.__prestamos[miembro] = None
        
    def get_cant_genero(self, genero):
        c=0
        for k, v in self.__prestamos.items():
            if v.genero == genero:
                c+=1
        return c