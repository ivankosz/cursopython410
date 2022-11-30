from ataque import Ataque
class Bicho:
    ataques = [Ataque("Picotazo", 10), Ataque("Picadura", 15)]
    nombre = "Bicho"
    
    def __str__(self):
        return self.nombre
    
    def get_ataque(self):
        import random
        return random.choice(self.ataques)

    def agregar_ataque(self, ataque):
        self.ataques.append(ataque)