import numpy as np
import time

class Nodo:
    def __init__(self, matriz, orden, padre, fila, columna):
        self.padre = padre
        self.matriz = matriz
        self.orden = orden
        self.hojas = []
        self.fila = fila 
        self.columna = columna
    
    @property
    def copia(self):
        return self.matriz.copy()

    def encontrar_Reina(self, orden, fila, columna):
        sumatoria = 0
        contador_fila = 0
        contador_columna = 0
        while contador_fila < orden: # suma la columna
            sumatoria += self.matriz[contador_fila][columna]
            contador_fila += 1
        # print("Primero", sumatoria)
        contador_fila = 0 
        while contador_columna < orden: # suma la fila
            sumatoria += self.matriz[fila][contador_columna]
            contador_columna += 1
        # print("Segundo", sumatoria)
        contador_columna = columna
        contador_fila = fila
        while True:
            while contador_columna >= 0 and contador_fila >= 0: # Suma esquina superior izquierda
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna -= 1
                contador_fila -= 1
            # print("Tercero", sumatoria)
                # print("entra 1")
            contador_columna = columna
            contador_fila = fila
            while contador_columna >= 0 and contador_fila < orden: # Suma esquina inferior izquierda
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna -= 1
                contador_fila += 1
            # print("Cuarto", sumatoria)
                # print("entra 2")
            contador_columna = columna
            contador_fila = fila
            while contador_columna < orden and contador_fila >= 0: # Suma esquina superior derecha
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna += 1
                contador_fila -= 1
            # print("Quinto", sumatoria)
                # print("entra 3")
            contador_columna = columna
            contador_fila = fila
            while contador_columna < orden and contador_fila < orden: # Suma esquina inferior derecha
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna += 1
                contador_fila += 1
            # print("Sexto", sumatoria)
                # print("entra 4")
            break
        return sumatoria

    def agregar_Hoja(self, hoja, orden, fila, columna):
        # print(self)
        self.hojas.append(Nodo(hoja, orden, self, fila, columna))
    
    def imprimir(self):
        pos=[]
        fila=0
        columna=0
        while fila<self.orden:
            columna=0
            while columna<self.orden:
                if self.matriz[fila][columna]==1:
                    pos.append(columna)
                columna=columna+1
            fila=fila+1
        print("Solucion(columnas): "+str(pos))

def suma_Fila(matriz, orden, fila):
    contador_columna = 0
    sumatoria = 0 
    while contador_columna < orden: # suma la fila
        sumatoria += matriz[fila][contador_columna]
        contador_columna += 1
    return sumatoria



def resolver(orden,iteracion):
    start = time.time()
    fila = -1
    columna = 0
    Matriz_Inicial = np.zeros((orden,orden), dtype=int)
    root = Nodo(Matriz_Inicial, orden, None, 0, 0)
    Verificar = False
    while fila < orden:
        columna = 0
        fila += 1
        if Verificar == True:
            #print("No se encontró una solución")
            # root.imprimir()
            Verificar = False
            if root.padre != None:
                if root.columna != orden -1: 
                    #print("Hoja actual:")
                    #root.imprimir()
                    #print("Hoja padre:")
                    #print(root.padre)
                    columna = root.columna + 1
                    fila = root.fila
                    root = root.padre
                    #root.imprimir()
                else:
                    columna = root.padre.columna + 1
                    fila = root.padre.fila
                    root = root.padre.padre
                    #root.imprimir()
            else:
                #print("Hoja inicial")
                #root.imprimir()
                break
        while columna < orden:
            # if fila == 0 and columna == 0:
            #     hoja = root.copia
            #     hoja[0][0] = 1
            #     root.agregar_Hoja(hoja, orden, fila, columna)
            #     root = root.hojas[0]
            #     print("0 0")
            #     columna += 1
            # else:
            if root.encontrar_Reina(orden, fila, columna) != 0:
                #print("No se puede poner", fila, columna)
                # print(root.encontrar_Reina(orden, fila, columna))
                columna += 1
            else:
                hoja = root.copia
                hoja[fila][columna] = 1
                root.agregar_Hoja(hoja, orden, fila, columna)
                # print("Se agregó la hoja")
                root = root.hojas[len(root.hojas)-1]
                #print("Se pudo poner", fila, columna)
                #root.imprimir()
                break
            if columna == orden and suma_Fila(root.matriz, orden, fila) == 0:
                Verificar = True
                break
        if root.fila == orden - 1:
            end = time.time()
            tiempo_final=format(end-start)
            print("Representaacion "+str(iteracion))
            print("--------------------------------")
            print("Numero de reinas: "+str(orden))
            root.imprimir()
            print("Tiempo: "+str(tiempo_final)+" s")
            print("--------------------------------")

            break








if __name__ == '__main__':
    n=4
    iteracion=1
    start=time.time()
    while True:
        resolver(n,iteracion)
        n=n+1
        iteracion=iteracion+1
        end=time.time()
        if float(format(end-start))>=10:
            break

    # matrizInicial = np.zeros((4,4), dtype=int)
    # matrizInicial[0][3] = 1
    # root = Nodo(matrizInicial)
    # Matriz2 = root.copia
    # Matriz2[0][0] = 1
    # root.agregar_hoja(Matriz2)
    # print("Root:")
    # root.imprimir()
    # hijo = root.hojas[0]
    # print("Hoja:")
    # hijo.imprimir()
    # hijo2 = root.copia
    # hijo2[0][1] = 1
    # root.agregar_hoja(hijo2)
    # hijo2 = root.hojas[1]
    # print("Hoja2:")
    # hijo2.imprimir()
    # print(matrizInicial)
    # root = Nodo(matrizInicial, 4)
    # a = root.matriz[0][3]
    # print(a)
    # print(root.matriz[0][3])
    # root.imprimir()


