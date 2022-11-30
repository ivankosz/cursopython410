import pokemones as pkm

pkm1 = pkm.Ratata("Ratata", 17)

pkm2 = pkm.Machop("Machop", 23)

print(pkm1.atacar(pkm2, "Normal"))

(pkm2.atacar(pkm1, "Lucha"))

print(pkm1.__str__())
print(pkm2.__str__())

print(pkm1.atacar(pkm2, "Normal"))

print(pkm2.__str__())

pkm3 = pkm.Venonat("Venonat", 30)

print(pkm3.atacar(pkm2, "Veneno"))

print(pkm2.__str__())

