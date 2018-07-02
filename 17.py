lista=["pollo","gallina","perro","gato"]
n=input("ingrese animal: ")
if n in lista:
    x=lista.index(n)
    print(n,", si esta en la lista, posicion: ",x)
else:
    n=-1
    print("no existe")
