lista=[54,26,93,17,77,31,44,55,20]

def bubbleSort(lista):
    for num in range(len(lista) - 1, 0, -1):
        for j in range(num):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista
print(lista)
print(bubbleSort(lista))
