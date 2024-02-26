class EstadoBloques:
    def __init__(self, estado, padre=None, movimiento=None, costo=0):
        self.estado = estado
        self.padre = padre
        self.movimiento = movimiento
        self.costo = costo

    def __eq__(self, otro):
        return self.estado == otro.estado

    def __lt__(self, otro):
        return self.costo < otro.costo

def calcular_h(nodo, estado_final):
    # Calcular h(n) como el número de bloques descolocados
    return sum(1 for i, j in zip(nodo.estado, estado_final) if i != j)

def calcular_f(nodo, estado_final):
    # Calcular f(n) = g(n) + h(n)
    h = calcular_h(nodo, estado_final)
    return nodo.costo + h

def expandir_nodo(nodo, estado_final):
    movimientos = []
    estado = nodo.estado[:]
    espacio = estado.index(" ")
    
    if espacio > 0:
        # Mover el bloque hacia la izquierda
        nuevo_estado = estado[:]
        nuevo_estado[espacio], nuevo_estado[espacio - 1] = nuevo_estado[espacio - 1], nuevo_estado[espacio]
        movimientos.append(EstadoBloques(nuevo_estado, nodo, "Mover izquierda", nodo.costo + 1))

    if espacio < len(estado) - 1:
        # Mover el bloque hacia la derecha
        nuevo_estado = estado[:]
        nuevo_estado[espacio], nuevo_estado[espacio + 1] = nuevo_estado[espacio + 1], nuevo_estado[espacio]
        movimientos.append(EstadoBloques(nuevo_estado, nodo, "Mover derecha", nodo.costo + 1))

    return movimientos

def imprimir_camino(solucion):
    if solucion is None:
        print("No se encontró solución.")
    else:
        camino = []
        nodo_actual = solucion
        while nodo_actual:
            camino.append((nodo_actual.movimiento, nodo_actual.estado))
            nodo_actual = nodo_actual.padre

        camino.reverse()
        for movimiento, estado in camino:
            print(f"{movimiento}: {estado}")

def buscar_solucion(estado_inicial, estado_final):
    nodo_inicial = EstadoBloques(estado_inicial)
    lista_abierta = [nodo_inicial]
    lista_cerrada = []

    while lista_abierta:
        lista_abierta.sort(key=lambda x: calcular_f(x, estado_final))
        nodo_actual = lista_abierta.pop(0)

        if nodo_actual.estado == estado_final:
            return nodo_actual  # Se encontró la solución

        lista_cerrada.append(nodo_actual)
        vecinos = expandir_nodo(nodo_actual, estado_final)

        for vecino in vecinos:
            if vecino in lista_cerrada:
                continue

            if vecino in lista_abierta:
                existente = lista_abierta[lista_abierta.index(vecino)]
                if vecino.costo < existente.costo:
                    lista_abierta.remove(existente)
                else:
                    continue

            lista_abierta.append(vecino)

    return None  # No se encontró solución

# Estado inicial y final
estado_inicial = ["B", "C", "A"]
estado_final = ["A", "B", "C"]

# Buscar solución
solucion = buscar_solucion(estado_inicial, estado_final)

# Imprimir el camino de la solución
imprimir_camino(solucion)
