import random
import sys

print("***Adivine el número***")
pc=random.randint(1,10)
lifes=5
print(pc)
while True:
    user=int(input("Su número: "))
    if user == pc:
        sys.exit(f"Acertaste!, el numero era {pc}")
    lifes-=1
    if lifes ==0:
        print("Perdiste")
        break
    else:
        print(f"Le {'queda' if lifes == 1 else 'quedan'} {lifes} {'vida' if lifes == 1 else 'vidas'}")  
        
print("Fin del Juego")
