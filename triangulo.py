from cmath import sqrt
def existe(a,b,c):
    if a+b>c and a+c>b and b+c>a :
        return 1
def area(a,b,c):
    s=(a+b+c)/2
    are=sqrt((s-a)*(s-b)*(s-c))
    return are
def triangulo():
    x=int(input("lado 1: "))
    y=int(input("lado 2: "))
    z=int(input("lado 3: "))
    if existe(x,y,z)==1:
        print("1 = Es un triangulo")
        print("Su area es ",area(x,y,z))
    else:
        print(" 0 = NO es un triangulo")
triangulo()
