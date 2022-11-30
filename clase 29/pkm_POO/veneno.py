from ataque import Ataque
class Veneno:
    ataques = [Ataque("Puya Nociva", 10), Ataque("Veneno", 15)]
    nombre = "Veneno"
    
    def __str__(self):
        return self.nombre
    
    def get_ataque(self):
        import random
        return random.choice(self.ataques)
    
    def agregar_ataque(self, ataque):
        self.ataques.append(ataque)