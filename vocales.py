def menu():
    print("Vocales")
    print("s: seguir")
    print("x: salir")
    opcion = input("ingrese opcion: ")
    return opcion
def contar_vocales(palabra):
    vocales=0
    for c in palabra.lower():
        if c in ["a","e","i","o","u"]:
            vocales = vocales + 1
    return  vocales
while 1==1:
    op=menu()
    if op == "s":
        x=input()
        print(contar_vocales(x))
    if op == "x":
        break
print("fin..")
