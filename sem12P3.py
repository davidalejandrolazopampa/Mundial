alumnos=[['Harry', 14], ['Berry', 13], ['Tina', 7], ['Akriti', 16], ['Harsh', 10]]

def bubbleSort(lista):
    for num in range(len(lista) - 1, 0, -1):
        for j in range(num):
            if lista[j][1] > lista[j + 1][1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1]= aux
    return lista

print(bubbleSort(alumnos))
