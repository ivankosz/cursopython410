from ataque import Ataque
class Normal:
    ataques = [Ataque("Placaje", 10), Ataque("Embestida", 15)]
    nombre = "Normal"

    def __str__(self):
        return self.nombre
    
    def get_ataque(self):
        import random
        return random.choice(self.ataques)
    
    def agregar_ataque(self, ataque):
        self.ataques.append(ataque)