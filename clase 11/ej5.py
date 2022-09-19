import string

abc=list(string.ascii_uppercase)
abecedario= list.copy(abc)
print(abc)
for letter in abc:
    if abc.index(letter)%3 == 0:
        abecedario.remove(letter)
print(abecedario)