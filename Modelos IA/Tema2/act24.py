class Node:
    def __init__(self, data, nivel, fval):
        """ Inicializa el nodo con los datos, el nivel del nodo y el valor f calculado """
        self.data = data
        self.nivel = nivel
        self.fval = fval

    def generar_hijos(self):
        """ Genera nodos hijos a partir del nodo dado moviendo el espacio en blanco
            en las cuatro direcciones {arriba, abajo, izquierda, derecha} """
        x, y = self.encontrar(self.data, '_')
        """ val_list contiene valores de posición para mover el espacio en blanco en cualquiera de
            las 4 direcciones [arriba, abajo, izquierda, derecha] respectivamente. """
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        hijos = []
        for i in val_list:
            hijo = self.mezclar(self.data, x, y, i[0], i[1])
            if hijo is not None:
                nodo_hijo = Node(hijo, self.nivel + 1, 0)
                hijos.append(nodo_hijo)
        return hijos

    def mezclar(self, puz, x1, y1, x2, y2):
        """ Mueve el espacio en blanco en la dirección dada y si los valores de posición están fuera
            de límites, devuelve None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copiar(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copiar(self, raiz):
        """ Función de copia para crear una matriz similar al nodo dado """
        temp = []
        for i in raiz:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def encontrar(self, puz, x):
        """ Usado específicamente para encontrar la posición del espacio en blanco """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Rompecabezas:
    def __init__(self, tamaño):
        """ Inicializa el tamaño del rompecabezas, listas abierta y cerrada vacías """
        self.n = tamaño
        self.abierta = []
        self.cerrada = []

    def aceptar(self):
        """ Acepta el rompecabezas del usuario """
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, inicio, objetivo):
        """ Función heurística para calcular el valor heurístico f(x) = h(x) + g(x) """
        return self.h(inicio.data, objetivo) + inicio.nivel

    def h(self, inicio, objetivo):
        """ Calcula la diferencia entre los rompecabezas dados """
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if inicio[i][j] != objetivo[i][j] and inicio[i][j] != '_':
                    temp += 1
        return temp

    def procesar(self):
        """ Acepta el estado inicial y el estado objetivo del rompecabezas """
        print("Ingrese la matriz de estado inicial \n")
        inicio = self.aceptar()
        print("Ingrese la matriz de estado objetivo \n")        
        objetivo = self.aceptar()

        inicio = Node(inicio, 0, 0)
        inicio.fval = self.f(inicio, objetivo)
        """ Coloca el nodo inicial en la lista abierta """
        self.abierta.append(inicio)
        print("\n\n")
        while True:
            actual = self.abierta[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in actual.data:
                for j in i:
                    print(j, end=" ")
                print("")
            """ Si la diferencia entre el nodo actual y el objetivo es 0, hemos llegado al nodo objetivo """
            if(self.h(actual.data, objetivo) == 0):
                break
            for i in actual.generar_hijos():
                i.fval = self.f(i, objetivo)
                self.abierta.append(i)
            self.cerrada.append(actual)
            del self.abierta[0]

            """ Ordena la lista abierta en función del valor f """
            self.abierta.sort(key=lambda x: x.fval, reverse=False)

rompecabezas = Rompecabezas(3)
rompecabezas.procesar()
