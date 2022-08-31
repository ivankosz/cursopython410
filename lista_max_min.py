def mayor(l):
    max=-9999
    for e in l:
        if e > max:
            max=e
    return max, l.index(max)
def menor(l):
    min=99999
    for e in l:
        if e < min:
            min=e
    return min, l.index(min)

listita=list()
user=int(input('Ingrese un num: '))
while user != 0:
    listita.append(user)
    user=int(input('Ingrese un num: '))
print(listita)
print(mayor(listita))
print(menor(listita))
    