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
    # Calcular h*(n) como el número de bloques descolocados
    return sum(1 for i, j in zip(nodo.estado, estado_final) if i != j)

def calcular_f(nodo, estado_final):
    # Calcular f(n) = g(n) + h*(n)
    h = calcular_h(nodo, estado_final)
    return nodo.costo + h

def expandir_nodo(nodo, estado_final):
    movimientos = []
    estado = nodo.estado[:]
    
    for i in range(len(estado)):
        for j in range(i+1, len(estado)):
            # Intercambiar dos bloques
            nuevo_estado = estado[:]
            nuevo_estado[i], nuevo_estado[j] = nuevo_estado[j], nuevo_estado[i]
            movimientos.append(EstadoBloques(nuevo_estado, nodo, f"Mover {estado[i]} a la posición {j}", nodo.costo + 1))

    return movimientos

def imprimir_camino(solucion):
    if solucion is None:
        print("No se encontró solución.")
    else:
        camino = []
        nodo_actual = solucion
        while nodo_actual:
            camino.append((nodo_actual.movimiento, nodo_actual.estado, nodo_actual.costo))
            nodo_actual = nodo_actual.padre

        camino.reverse()
        for paso, estado, costo in camino:
            print(f"Paso: {paso}, Estado: {estado}, Costo: {costo}")

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

# Imprimir el camino de la solución y la heurística final
imprimir_camino(solucion)
heuristica_final = calcular_h(solucion, estado_final)
print(f"Heurística final (h*): {heuristica_final}")
