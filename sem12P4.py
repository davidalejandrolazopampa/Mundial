alumnos2 = [['Harry',[15, 18]], ['Berry',[9,13]], ['Tina',[12,15]], ['Akriti',[17,10]], ['Harsh',[15,19]]]
def promedio(lista):
    for i in range(len(lista)):
        suma = lista[i][1]
        promedio=sum(suma)/2
        lista[i].append(promedio)
        return lista

def eliminar(lista):
    lista.pop((0))
    return lista
print(promedio(alumnos2))
print(eliminar(promedio(alumnos2)))
