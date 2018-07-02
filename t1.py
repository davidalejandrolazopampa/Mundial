
def picachu() :
    x=input("palabra: ")
    if len(x)<3:
        print("error")
    else:
        z=str(x[0]+x[1]+x[-2]+x[-1])
        return print(z)

picachu()
