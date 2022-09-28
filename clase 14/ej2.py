palindromos=list()
"""
while True:
    user= input(">> ")
    if user == user[::-1]:
        palindromos.append(user)
        if user == 'ama':
            break
print(palindromos)
"""

user= input('>> ')
while user != 'ama':
    if user == user [::-1]:
        palindromos.append(user)
    user=input('>> ')
palindromos.append(user)
print(palindromos)