def picachu() :
    x=input("palabra: ")
    if len(x)<2:
        print("error")
    else:
        z=str(x[-2]+x[-1]+x[-2]+x[-1]+x[-2]+x[-1]+x[-2]+x[-1])
        return print(z)

picachu()
