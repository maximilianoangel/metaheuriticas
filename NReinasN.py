import numpy as np
import time
import matplotlib.pyplot as plt

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
        contador_fila = 0 
        while contador_columna < orden: # suma la fila
            sumatoria += self.matriz[fila][contador_columna]
            contador_columna += 1
        contador_columna = columna
        contador_fila = fila
        while True:
            while contador_columna >= 0 and contador_fila >= 0: # Suma esquina superior izquierda
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna -= 1
                contador_fila -= 1
            contador_columna = columna
            contador_fila = fila
            while contador_columna >= 0 and contador_fila < orden: # Suma esquina inferior izquierda
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna -= 1
                contador_fila += 1
            contador_columna = columna
            contador_fila = fila
            while contador_columna < orden and contador_fila >= 0: # Suma esquina superior derecha
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna += 1
                contador_fila -= 1
            contador_columna = columna
            contador_fila = fila
            while contador_columna < orden and contador_fila < orden: # Suma esquina inferior derecha
                sumatoria += self.matriz[contador_fila][contador_columna]
                contador_columna += 1
                contador_fila += 1
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
            Verificar = False
            if root.padre != None:
                if root.columna != orden -1:
                    columna = root.columna + 1
                    fila = root.fila
                    root = root.padre
                else:
                    columna = root.padre.columna + 1
                    fila = root.padre.fila
                    root = root.padre.padre
            else:
                break
        while columna < orden:
            if root.encontrar_Reina(orden, fila, columna) != 0:
                columna += 1
            else:
                hoja = root.copia
                hoja[fila][columna] = 1
                root.agregar_Hoja(hoja, orden, fila, columna)
                root = root.hojas[len(root.hojas)-1]
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
            print("Tiempo: "+str(float(tiempo_final))+" s")
            print("--------------------------------")

            break
    return float(tiempo_final)

if __name__ == '__main__':
    n=4
    iteracion=1
    tiempos = []
    start=time.time()
    while True:
        tiempo = resolver(n,iteracion)
        n=n+1
        iteracion=iteracion+1
        end=time.time()
        tiempos.append(tiempo)
        if float(format(end-start))>=180:
            break
    coronas = []
    for i in range(0, len(tiempos)):
        coronas.append(i +4)
    print(tiempos)
    plt.bar(coronas, tiempos, color = 'lime', label = 'Tiempos')
    plt.xlabel('Numero de reinas')
    plt.ylabel('Tiempo [s]')
    plt.title('Tiempo para relver problema N reinas / N')
    plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
    plt.tight_layout(rect=[0,0,1,1])
    plt.show()