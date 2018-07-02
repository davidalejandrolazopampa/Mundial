def picachu():
    x=input("palabra 1: ")
    y=input("palabra 2: ")
    a=x[2:]
    b=y[2:]
    uno=x[0]+x[1]+b
    dos=y[0]+y[1]+a
    return print(dos,uno)
picachu()
