def suma(a,b):
    c=a+b
    return c
def resta(a,b):
    c=a-b
    return c
def multiplicacion(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c
print("SUM: SUMA")
print("RES: RESTA")
print("SUM: SUMA")
print("MULTI: MULTIPLICACION")
print("fin: Salir")
i=0
while i==0 :
    h=input("seguir enter, acabar fin: ")
    if h!="fin":
        x=int(input("Ingrese datos: "))
        y=int(input("Ingrese datos: "))
        operacion=input("Ingrese OperacioN: ")

        if operacion=="SUM" :
            print("la suma" , suma(x,y))
        elif operacion=="RES" :
            print("la RESTA" , resta(x,y))
        elif operacion== "MULTI" :
            print("la multiplicacion" , multiplicacion(x,y))
        elif operacion=="DIV" :
            if y>0:
                print("la division" , division(x,y))
        elif y==0:
            print("No se divide entre cero")
    else:
        i+=1
