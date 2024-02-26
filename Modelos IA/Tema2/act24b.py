class Node:
    def __init__(self, data, nivel, fval, padre=None):
        self.data = data
        self.nivel = nivel  # Coste g(n)
        self.fval = fval  # Valor total f(n)
        self.padre = padre

    def generar_hijos(self):
        x, y = self.encontrar(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        hijos = []
        for i in val_list:
            hijo = self.mezclar(self.data, x, y, i[0], i[1])
            if hijo is not None:
                nodo_hijo = Node(hijo, self.nivel + 1, 0, self)
                hijos.append(nodo_hijo)
        return hijos

    def mezclar(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = [fila[:] for fila in puz]
            temp_puz[x1][y1], temp_puz[x2][y2] = temp_puz[x2][y2], temp_puz[x1][y1]
            return temp_puz
        else:
            return None

    def encontrar(self, puz, x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if puz[i][j] == x:
                    return i, j

    def h(self, objetivo):
        # Implementación de P(n) y S(n) para la heurística h(n)
        # Aquí debes agregar la lógica para calcular P(n) y S(n)
        return 0  # Reemplaza esto con el cálculo real de la heurística

    def imprimir_nodo(self):
        print("Estado:")
        for fila in self.data:
            print(" ".join(fila))
        print(f"Nivel (g(n)): {self.nivel}, Heurística (h(n)): {self.h(None)}, Valor f: {self.fval}")
        print("-----")


class Rompecabezas:
    def __init__(self, tamaño):
        self.n = tamaño
        self.abierta = []
        self.cerrada = []

    def f(self, nodo, objetivo):
        return nodo.h(objetivo) + nodo.nivel

    def procesar(self):
        inicio = [['2', '8', '3'], ['1', '6', '4'], ['7', '_', '5']]
        objetivo = [['1', '2', '3'], ['8', '_', '4'], ['7', '6', '5']]

        nodo_inicial = Node(inicio, 0, 0, None)
        nodo_inicial.fval = self.f(nodo_inicial, objetivo)
        self.abierta.append(nodo_inicial)

        while self.abierta:
            actual = self.abierta.pop(0)
            self.cerrada.append(actual)
            if actual.data == objetivo:
                self.imprimir_solucion(actual)
                return
            hijos = actual.generar_hijos()
            for hijo in hijos:
                hijo.fval = self.f(hijo, objetivo)
                if hijo.data not in [nodo.data for nodo in self.cerrada]:
                    self.abierta.append(hijo)
            self.abierta.sort(key=lambda x: x.fval)

    def imprimir_solucion(self, nodo_final):
        camino = []
        while nodo_final:
            camino.append(nodo_final)
            nodo_final = nodo_final.padre
        camino.reverse()
        for nodo in camino:
            nodo.imprimir_nodo()


rompecabezas = Rompecabezas(3)
rompecabezas.procesar()
