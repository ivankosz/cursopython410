
numero= int(input("Ingrese un número entero positivo: "))
num_list=""
for i in range (numero):
    if (i+1) %2!= 0:
        num_list+=(str(i+1))+", "
print(num_list)

