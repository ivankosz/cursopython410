class Ataque:
    def __init__(self, nombre_atk, danho_atk):
        self.nombre = nombre_atk
        self.danho = danho_atk
    
    def __str__(self):
        return self.nombre
    
    def atacar(self):
        return self.danho 