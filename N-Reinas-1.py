import numpy as np

def matriz_generator(i): #genera la matriz

    matriz=np.zeros((i,i))


    return matriz

def summation(matriz,fila,columna,i): #suma y decide si poner o no la reina
    sumatoria1 = 0
    sumatoria2 = 0
    sumatoria3 = 0
    sumatoria4 = 0
    sumatoria5 = 0
    sumatoria6 = 0
    contador_fila = 0
    contador_columna = 0
    while contador_fila < i: # suma la columna
        sumatoria1 += matriz[contador_fila][columna]
        contador_fila += 1
    contador_fila = 0 
    while contador_columna <= columna: # suma la fila
        sumatoria2 += matriz[fila][contador_columna]
        contador_columna += 1
    contador_columna = columna
    contador_fila = fila
    while True:
        while contador_columna >= 0 and contador_fila >= 0: # Suma esquina superior izquierda
            sumatoria3 += matriz[contador_fila][contador_columna]
            contador_columna -= 1
            contador_fila -= 1
            # print("entra 1")
        contador_columna = columna
        contador_fila = fila
        while contador_columna >= 0 and contador_fila < i: # Suma esquina inferior izquierda
            sumatoria4 += matriz[contador_fila][contador_columna]
            contador_columna -= 1
            contador_fila += 1
            # print("entra 2")
        contador_columna = columna
        contador_fila = fila
        while contador_columna < i and contador_fila >= 0: # Suma esquina superior derecha
            sumatoria5 += matriz[contador_fila][contador_columna]
            contador_columna += 1
            contador_fila -= 1
            # print("entra 3")
        contador_columna = columna
        contador_fila = fila
        while contador_columna < i and contador_fila < i: # Suma esquina inferior derecha
            sumatoria6 += matriz[contador_fila][contador_columna]
            contador_columna += 1
            contador_fila += 1
            # print("entra 4")
        break
    if sumatoria6==0 and sumatoria1==0 and sumatoria2==0 and sumatoria3==0 and sumatoria4==0 and sumatoria5==0:
        return 0
    elif sumatoria6==1 or sumatoria1==1 or sumatoria2==1 or sumatoria3==1 or sumatoria4==1 or sumatoria5==1:
        return 1
    elif sumatoria6>1 or sumatoria1>1 or sumatoria2>1 or sumatoria3>1 or sumatoria4>1 or sumatoria5>1:
        return 2

def solver_complement(matriz,filaF,columnaF,i):
    mat=matriz_generator(i)
    mat=matriz+mat
    fila=0
    columna=0
    while True:
        Mvar=summation(mat,fila,columna,i)
        if Mvar==0:
            mat[fila][columna]=1
            print("complemento "+str(mat))
            print("lugar "+str(fila)+" "+str(columna))
            if columna<i and fila<i:
                columna=columna+1
        elif Mvar==1:
            if columna<i and fila<i:
                columna=columna+1
        elif Mvar==2:
            print("Error fatal garrafal")
        if columna%i==0 and fila<i-1 and columna!=0:
            fila=fila+1
            columna=0
        if filaF+1==fila and columnaF+1==columna:
            break
    return mat

def solver(i,fila,columna,iteracion): #hace los llamados para generar la matriz y calcular si poner o no la reina
    matriz=matriz_generator(i)
    aux=(i*i)
    filaI=fila
    ColumnaI=columna
    print("iteracion " + str(iteracion))
    while True:
        print("fila " + str(fila))
        Mvar=summation(matriz,fila,columna,i)
        if Mvar==0:
            matriz[fila][columna]=1
            print(matriz)
            if columna<i and fila<i:
                print("columa "+ str(columna))
                columna=columna+1
            if int(sum(sum(matriz)))==1 and filaI>0:
                matriz=solver_complement(matriz,filaI,ColumnaI,i)
        elif Mvar==1:
            if columna<i and fila<i:
                print(columna)
                columna=columna+1
        elif Mvar==2:
            print("Error fatal garrafal")
        if columna%i==0 and fila<i-1 and columna!=0:
            fila=fila+1
            columna=0
        if fila+1==i and columna+1==i:
            break
    if sum(sum(matriz))==i:
        print ("solucion!!")
        print (matriz)
    else:
        if ColumnaI+1%i==0:
            print("llegue " + str(filaI+1))
            solver(i,filaI+1,0,iteracion+1)
        else:
            print("aca")
            print(matriz)
            if ColumnaI+1==i:
                print("entro")
                ColumnaI=-1
                filaI=filaI+1
                print("Fila inicial " + str(filaI))
            solver(i,filaI,ColumnaI+1,iteracion+1)
    if iteracion==aux:
        return matriz
i=4
solver(8,0,0,0)


