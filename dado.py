from random import randint
def dado():
    valor=randint(1, 6)
    return valor
def suma(a,b):
    c=a+b
    return c
def jugador():
    n1=input("jugador 1: ")
    x1=dado()
    x2=dado()
    n2=input("jugador 2: ")
    y1=dado()
    y2=dado()

    print("jugador 1, ", n1 ," ",x1,x2)
    print("jugador 2, ", n2 ," ",y1,y2)

    x=suma(x1,x2)
    y=suma(y1,y2)
    if x>y :
        print("Gano el jugador ",n1)
        print(x)
    elif x<y:
        print("Gano el jugador ", n2)
        print(y)
    else:
        print("empate")
jugador()

