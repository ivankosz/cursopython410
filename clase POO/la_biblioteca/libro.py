import random

class Libro:
    
    def __init__(self, un_titulo, un_autor, un_genero):
        self.isbn = "778-"
        self.estado = False
        self.titulo = un_titulo
        self.autor = un_autor
        self.genero = un_genero
        
    def set_isbn (self):
        for a in range (10):
            isbn = str(random.randint(0,9))
            self.isbn+=isbn
        
    def set_prestamos (self):
        if self.estado == False:
            self.estado = True
        else:
            print(f"El libro {self.titulo} no se encuentra en inventario")
    def set_devoluciones(self):
        if self.estado == True:
            self.estado = False
        else:
            print(f"El libro {self.titulo} ya se encuentra en inventario")
        
if __name__ == "__main__":
    
    librito = Libro("harry potter", "j.k.rowling", "fantasía")
    
    librito.set_isbn()
    
    print(librito.isbn)