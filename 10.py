f=int(input("ingrese F°: "))
c=((f-32)*5)/9
if 46>f and 29<f:
    print(c)
elseif f==46:
    print("Limite Inferior")
else :
    print("Limite Superior")
