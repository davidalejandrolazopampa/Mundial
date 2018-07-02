##4
cantidad=int(input(""))
lista=[]
lista0=[]
while cantidad>0:
    num=int(input(""))
    if num % 2 == 0:
        lista.append(num)
    else:
        lista0.append(num)
    cantidad=cantidad-1
print(len(lista))

##2
list=[]
i = 5
while i > 0:
    num = int(input(""))
    list.append(num)
    i = i - 1
print(max(list),"-",min(list))

##3
list=[]
i = 5
while i > 0:
    num = int(input(""))
    list.append(num)
    i = i - 1
prom=float((list[0]+list[1]+list[2]+list[3]+list[4])/5)
print(prom)

##1
list=[]
i = 5
while i > 0:
    num = int(input(""))
    list.append(num)
    i = i - 1
list.remove(max(list))
list.remove(min(list))
promedio = float((list[0]+list[1]+list[2])/3)
print(round(promedio,1))
