x=int(input("ingrese cantidad de Clientes: " ))
clientes=[]
for x in range(1,x+1):
    clientes.append(input("Nombre: "))
print(clientes)

consulta=input("ingrese Clientes Atendido: " )

if consulta in clientes:
    x=clientes.index(consulta)
    x=clientes.remove(consulta)
    print(", Cliente atendido")
    clientes.append(consulta)
    print(clientes)
else:
    n=-1



