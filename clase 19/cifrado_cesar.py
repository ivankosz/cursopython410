import string
ejemplo = 'Hola Mundo!!'

def cifrar (mensaje): 
    mensaje_cifrado = '' 
    abc = string.ascii_lowercase
    for car in mensaje.lower():
        if car in abc:
            #if abc.index(car) % len(abc) == 0:
            #    mensaje_cifrado += abc[0]   
            indice = (abc.index(car)+1) % len(abc)       
            mensaje_cifrado += abc[indice]
        else:
            mensaje_cifrado +=car
    
    return mensaje_cifrado
           
def descifrar (mensaje): 
    mensaje_descifrado = '' 
    abc = string.ascii_lowercase
    for car in mensaje.lower():
        if car in abc:    
            indice = (abc.index(car)-1) % len(abc)       
            mensaje_descifrado += abc[indice]
        else:
            mensaje_descifrado +=car
    
    return mensaje_descifrado

print(cifrar(ejemplo))  
cifrado = cifrar(ejemplo)
print(descifrar(cifrado))