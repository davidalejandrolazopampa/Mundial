def invertir():
    a=int(input("Ingresar un Número: "))
    x=0
    z=len(str(a))
    for i in range(z):
        b=a%10
        a=a//10
        x=x*10+b
    return x
invertir()
