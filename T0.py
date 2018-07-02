list=[10,14,1926,27,31,33,34,42,43]
search=int(input("Ingrese el número a buscar: "))
cont=0
for i in range(0,len(list)):
    if search==list[i]:
        print(str(search)+" ,encontrado en la posicion "+str(i))
        break
    cont+=1
if cont==9:
    list.append(search)
    print("No se encontró el número, acabamos de agregarlo!",list)
print("Busquedas realizadas:",cont+1)
