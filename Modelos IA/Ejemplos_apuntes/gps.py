import heapq

class Ciudad:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

def distancia_en_linea_recta(ciudad1, ciudad2):
    # Calcula la distancia en línea recta entre dos ciudades
    # Puedes utilizar la fórmula de la distancia euclidiana
    return ((ciudad1.latitud - ciudad2.latitud) ** 2 + (ciudad1.longitud - ciudad2.longitud) ** 2) ** 0.5

def a_estrella(ciudad_inicial, ciudad_final, grafo):
    heap = [(0, ciudad_inicial)]  # (costo acumulado + heurística, nodo)
    visitados = set()

    while heap:
        costo_acumulado, nodo_actual = heapq.heappop(heap)

        if nodo_actual == ciudad_final:
            # Se alcanzó el destino, construir el camino
            camino = [ciudad_final.nombre]
            while nodo_actual != ciudad_inicial:
                nodo_actual = nodo_actual.padre
                camino.append(nodo_actual.nombre)
            camino.reverse()
            return camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for vecino, costo in grafo[nodo_actual]:
                if vecino not in visitados:
                    heuristica = distancia_en_linea_recta(vecino, ciudad_final)
                    heapq.heappush(heap, (costo + costo_acumulado + heuristica, vecino))
                    vecino.padre = nodo_actual

    return None  # No se encontró un camino

# Ejemplo de uso
ciudad_a = Ciudad("Ciudad A", 0, 0)
ciudad_b = Ciudad("Ciudad B", 1, 1)
ciudad_c = Ciudad("Ciudad C", 2, 2)

# Grafo: {nodo: [(vecino, costo)]}
grafo = {
    ciudad_a: [(ciudad_b, 1), (ciudad_c, 2)],
    ciudad_b: [(ciudad_a, 1), (ciudad_c, 1)],
    ciudad_c: [(ciudad_a, 2), (ciudad_b, 1)]
}

resultado = a_estrella(ciudad_a, ciudad_c, grafo)

if resultado:
    print("Camino encontrado:", resultado)
else:
    print("No hay camino posible.")
