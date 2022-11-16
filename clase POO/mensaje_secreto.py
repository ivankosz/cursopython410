
class MensajeSecreto:
    
    def __init__(self, un_mensaje, una_clave):
        self.__mensaje = un_mensaje
        self.__clave = una_clave
        
    def get_mensaje_secreto (self, otra_clave):
        if otra_clave == self.__clave:
            return self.__mensaje
        else:
            return f"Error"
        
mensajito =MensajeSecreto("hola mundo", "chaumundo333")

print(mensajito.get_mensaje_secreto("chaumundo222"))
print(mensajito.get_mensaje_secreto("chaumundo333"))
        