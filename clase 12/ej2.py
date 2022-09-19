numero= int(input("Ingrese un número entero positivo: "))
num_list=[]
for i in range (numero+1):
    num_list.append(str(i))
num_list.reverse()
joined_string = ", ". join(num_list)
print(joined_string)