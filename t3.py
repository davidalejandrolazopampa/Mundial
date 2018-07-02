def picachu():
    x=input("palabra 1: ")
    z=x[-1]+x[-2]+x[-3]
    if len(x)<4:
        print(x)
    else:
        if z=="ing":
            print(x[-3:]+ "ing")
        else:
            print(x[:-3]+ "ly")
picachu()
