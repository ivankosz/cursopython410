import sys

def menu():
    print('1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.¿Es a multiplo de b?\n6.¿Es b multiplo de a?\n7.Salir')
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b==0:
        return('No se puede dividir por Cero')
    else:
        return a/b
def multiplos(a,b):
    if a%b==0:
        return True
    else:
        return False
    
a=int(input('ingrese un numero: '))
b=int(input('ingrese otro numero: '))
menu()
choice=int(input('elija una opcion: '))
while choice!=7:
    if choice==1:
        res=sumar(a,b)
        a=res
        print(res)     
    elif choice==2:
        res=restar(a,b)
        a=res
        print(res)    
    elif choice==3:
        res=multiplicar(a,b)
        a=res
        print(res)    
    elif choice==4:
        res=dividir(a,b)
        a=res
        print(res)    
    elif choice==5:
        res=multiplos(a,b)
        print(res)    
    elif choice==6:
        res=multiplos(b,a)
        print(res)    
    b=int(input('ingrese otro numero: '))
    menu()
    choice=int(input('elija una opcion: '))
sys.exit('Vuelva prontos')
    
