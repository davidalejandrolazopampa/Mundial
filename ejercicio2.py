from random import randint

#Función para crear una tupla para el juego "campo minado"
def tupla_minada():
    lista = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
    print(lista)
    contador = 0
    minas = 0
    while minas < 3:
        mina = randint(0,5)
        if mina == 1:
            lista[contador] = "*!"
            minas = minas + 1
        contador = contador + 1
        if contador == 20:
            contador = 0
    tupla_llena = tuple(lista)
    return tupla_llena

#Invocar a la función "tupla_minada" y devolver el valor a una variable "tupla"
tupla = tupla_minada()
print(tupla)

#Desarrollar el ejercicio 1, Mostrar en pantalla como en el ejemplo de la diapositiva
print('\n',tupla[0],tupla[1],tupla[2],tupla[3],'\n',tupla[4],tupla[5],tupla[6],tupla[7],"\n",tupla[8],tupla[9],tupla[10],tupla[11],"\n",tupla[12],tupla[13],tupla[14],tupla[15],"\n",tupla[16],tupla[17],tupla[18],tupla[19])

#Desarrollar el ejercicio 2, Solicitar ingresar los número para jugar.


def buscar_valor():
    i=0
    while i<=5:
        x=int(input("n!: "))
        if tupla[x-1] == "*!":
            print("boom")
            break
        i=i+1
buscar_valor()
