lista=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]
n=input("ingrese Mes: ")
if n in lista:
    x=lista.index(n)
    print(n,", si esta en la lista, posicion: ",x)
else:
    n=-1
    print("no existe")




nn=input("ingrese Mes que desea Eliminar: ")
if nn in lista:
    xx=lista.remove(nn)
    print("Mes eliminado")
    print(lista)
else:
    nn=-1
    print("no existe")
