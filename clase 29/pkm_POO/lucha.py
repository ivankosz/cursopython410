from ataque import Ataque
class Lucha:
    ataques = [Ataque("Patada Baja", 10), Ataque("Patada Alta", 15)]
    nombre = "Lucha"

    def __str__(self):
        return self.nombre
    
    def get_ataque(self):
        import random
        return random.choice(self.ataques)
    
    def agregar_ataque(self, ataque):
        self.ataques.append(ataque)