
#Herencias multiples

class A:

    def funcion1 (self):
        return ("Hola")

class B:

    def funcion1 (self):
        return ("Buen día")

class C (A, B):

    def funcion1 (self):
        return
    
    def saludo (self):
        r = self.funcion1()
        #r = A.funcion1()
        #r = B.funcion1()


# los objetos creados como instancias de C, pueden heredar los atributos tanto de A como de B, según se requiera.


#Herencias multiples

class A:
    def __init__(self, edad, mayor = True):
        self.edad = edad
        self.mayor = mayor
    def funcion1 (self):
        return ("Hola")
class B:
    def __init__(self, edad, mayor = False):
        self.edad = edad
        self.mayor = mayor
    def funcion1 (self):
        return (" Buen día")

class C (A, B):

    def __init__(self, edad):
        if edad > 17:
            A.__init__(self, edad)
        else:
            B.__init__(self,edad)

    def funcion1 (self):
        return A.funcion1(self) #puedo llamar directamente una funcion de cualquier clase padre
    
objc = C(14)
print("soy mayor?", objc.mayor)
