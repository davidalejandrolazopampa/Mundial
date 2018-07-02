lista=[54,26,93,17,77,31,44,55,20]
def selectionSort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i, len(lista)):
            if (lista[j]) < lista[min]:
                min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    return lista
print(lista)
print(selectionSort(lista))

