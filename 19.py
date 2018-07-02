medidas=[]
for x in range(1,6):
    medidas.append(int(input("Agregar Lista: ")))
y=(medidas[0]+medidas[1]+medidas[2]+medidas[3]+medidas[4])/5
desviación=[abs(medidas[0]-y),abs(medidas[1]-y),abs(medidas[2]-y),abs(medidas[3]-y),abs(medidas[4]-y)]
print(medidas)
print(desviación)
