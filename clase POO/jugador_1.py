
class Jugador:
    
    def __init__(self, un_nombre, un_email, un_password, un_telefono):
        self.nombre = un_nombre
        self.email = un_email
        self.__password = un_password
        self.__telefono = un_telefono
        
    def __str__(self):
        return """\
            Nombre: {}
            Email: {}
            """.format(self.nombre, self.email)

    def get_password (self, p):
        if p == self.__password:
            return self.__password
        else:
            return "contraseña incorrecta"

    def get_telefono (self,p):
        if p == self.__password:
            return self.__telefono
        else:
            return "contraseña incorrecta"

if __name__ =="__main__":
                
    player = Jugador("ivan","nada@gmail.com", "4456hola", "2216661234")
    
    print(player)

    print(player.nombre)

    print(player.get_password("4456chau"))
    print(player.get_telefono("4456hola"))