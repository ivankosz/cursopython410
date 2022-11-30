from bicho import Bicho
from lucha import Lucha
from normal import Normal
from veneno import Veneno

class Pokemon:

    def __init__(self, nombre, nivel) -> None:
        self.nombre = nombre
        self.nivel = nivel
        self.salud = nivel*10
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nLvl: {self.nivel}\nSalud: {self.salud}"

    def recibir_danho (self, danho: int):
        if danho > self.salud:
            self.salud = 0
            return f"daño recibido: {self.salud}, salud: {self.salud}\n{self.nombre} ha sido derrotado"
        else:
            self.salud -= danho
            return f"daño recibido: {danho}, salud: {self.salud}"


class Ratata (Pokemon, Normal):
    def __init__(self, nombre, nivel):
        Pokemon.__init__(self, nombre, nivel)


    def atacar (self, pokemon, tipo: str):
        if tipo.capitalize() == Normal.nombre:
            self.atk = Normal.get_ataque(self)
            pokemon.recibir_danho(self.atk.atacar())
        else:
            return ("Ataque no valido")




class Machop (Pokemon, Normal, Lucha):
    def __init__(self, nombre, nivel):
        Pokemon.__init__(self, nombre, nivel)


    def atacar (self, pokemon, tipo: str):
        if tipo.capitalize() == Lucha.nombre:
            self.atk = Lucha.get_ataque(self)
            pokemon.recibir_danho(self.atk.atacar())
        elif tipo.capitalize() == Normal.nombre:
            self.atk = Normal.get_ataque(self)
            pokemon.recibir_danho(self.atk.atacar())
        else:
            return ("Ataque no valido")
        

class Venonat (Pokemon, Bicho, Veneno):
    def __init__(self, nombre, nivel):
        Pokemon.__init__(self, nombre, nivel)


    def atacar (self, pokemon, tipo: str):
        if tipo.capitalize() == Bicho.nombre:
            atk = Bicho.get_ataque()
            pokemon.recibir_danho(atk.atacar())
        elif tipo.capitalize() == Veneno.nombre:
            atk = Veneno.get_ataque(self)
            pokemon.recibir_danho(atk.atacar())
        else:
            return("ataque no valido")