def CUMPLE(text):
    if len(text)>=2:
        MAYUSCULA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i=0
        cont=0
        while i<4:
            a=text[i]
            if a in MAYUSCULA:
                cont+=1
            i+=1
        if cont>=2:
            x=text.upper()
            return x
        else:
            return "No cumple"
    else:
        return "No cumple"
palabra=input("Ingrese palabra: ")
print(CUMPLE(palabra))
