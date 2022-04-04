import numpy as np

i=4

def matriz_generator(i): #genera la matriz

    matriz=np.zeros((i,i))


    return matriz

def summation(matriz,fila,columna,i): #suma y decide si poner o no la reina
    aux1=0
    aux2=0
    aux3=5
    aux4=0
    posC=columna
    posF=fila
    var=0
    posFF=fila
    posCC=columna
    n=5
    while var<i:
        aux1=matriz[fila][var]+aux1
        aux2=matriz[var][columna]+aux2
        if (fila==0 and columna==0) or (fila ==i-1 and columna==i-1):
            aux3=matriz[var][var]+aux3
        elif (fila==0 and columna>0 and columna<i) or (fila==i-1 and columna<i):
            aux4=matriz[var][posC]+aux4
            posC=posC-1
        elif columna==0 and fila>0 and fila<i:
            aux4=matriz[posF][var]
            posF=posF-1
        var=1+var
    if columna>0 and columna<i-1 and fila >0 and fila<i-1:
        while posFF>0 or posCC>0:
            if posFF>0 and posFF<posCC and posCC>=0:
                posCC=posCC-1
                posFF=posFF-1
                if posFF==0:
                    aux3=int(sum(np.diag(matriz,k=posCC)))
                    break
            elif posFF>0 and posFF>posCC and posCC>=0:
                posCC=posCC-1
                posFF=posFF-1
                if posCC==0:
                    aux3=int(sum(np.diag(matriz,k=posFF*-1)))
                    break
            else:
                break

    if aux1==0 and aux2==0 and aux3==0:
        return 0
    elif aux1==1 or aux2==1 or aux3==1:
        return 1
    else:
        return 2


def solver(i): #hace los llamados para generar la matriz y calcular si poner o no la reina
    matriz=matriz_generator(i)
    aux=(i*i)+1
    fila=0
    columna=0
    var=1
    while var<aux:
        Mvar=summation(matriz,fila,columna,i)
        if Mvar==0:
            matriz[fila][columna]=1
        elif Mvar==1:
            if columna<i and fila<i:
                columna=columna+1
                Mvar=summation(matriz,fila,columna,i)
        elif Mvar==2:
            print("Error fatal garrafal")
        if var%i==0:
            fila=fila+1
            columna=0
        else:
            columna=columna+1
        var=var+1
    print(matriz)
    print(sum(sum(matriz)))

solver(i)

