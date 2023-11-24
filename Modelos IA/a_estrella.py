class Nodo:
    def __init__(self, datos, coste=0, padre=None):
        self.datos = datos
        self.coste = coste
        self.padre = padre
        self.hijos = []

    def get_datos(self):
        return self.datos

    def set_datos(self, datos):
        self.datos = datos

    def get_coste(self):
        return self.coste

    def set_coste(self, coste):
        self.coste = coste

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def get_hijos(self):
        return self.hijos

    def set_hijos(self, hijos):
        self.hijos = hijos

    def igual(self, nodo):
        return self.datos == nodo.get_datos()

    def en_lista(self, lista):
        return any(self.igual(nodo) for nodo in lista)

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = [Nodo(estado_inicial)]
    
    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            return nodo
        
        dato_nodo = nodo.get_datos()
        lista_hijos = []
        
        for un_hijo in conexiones[dato_nodo]:
            hijo = Nodo(un_hijo)
            coste = conexiones[dato_nodo][un_hijo]
            hijo.set_coste(nodo.get_coste() + coste)
            lista_hijos.append(hijo)
            
            if not hijo.en_lista(nodos_visitados):
                if hijo.en_lista(nodos_frontera):
                    for n in nodos_frontera:
                        if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                            nodos_frontera.remove(n)
                            nodos_frontera.append(hijo)
                else:
                    nodos_frontera.append(hijo)
        
        nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'Ciudad_A': {'Ciudad_C': 125, 'Ciudad_E': 513},
        'Ciudad_B': {'Ciudad_E': 514},
        'Ciudad_C': {'Ciudad_A': 125, 'Ciudad_E': 423, 'Ciudad_D': 491},
        'Ciudad_D': {'Ciudad_C': 491, 'Ciudad_E': 356, 'Ciudad_I': 309, 'Ciudad_J': 346},
        'Ciudad_E': {'Ciudad_F': 203, 'Ciudad_B': 514, 'Ciudad_A': 513, 'Ciudad_C': 423, 'Ciudad_J': 603, 'Ciudad_H': 437,
                     'Ciudad_D': 356, 'Ciudad_I': 313, 'Ciudad_H': 437, 'Ciudad_G': 599},
        'Ciudad_F': {'Ciudad_G': 390, 'Ciudad_E': 203},
        'Ciudad_G': {'Ciudad_F': 390, 'Ciudad_E': 599},
        'Ciudad_H': {'Ciudad_E': 437, 'Ciudad_I': 394},
        'Ciudad_I': {'Ciudad_J': 296, 'Ciudad_D': 309, 'Ciudad_E': 313},
        'Ciudad_J': {'Ciudad_I': 296, 'Ciudad_E': 603, 'Ciudad_D': 346}
    }
    
    coord = {
        'Ciudad_A': (36.43, -4.24), 'Ciudad_B': (37.23, -5.59),
        'Ciudad_C': (37.11, -3.35), 'Ciudad_D': (39.28, -0.22),
        'Ciudad_E': (40.24, -3.41), 'Ciudad_F': (40.57, -5.40),
        'Ciudad_G': (42.52, -8.33), 'Ciudad_H': (43.28, -3.48),
        'Ciudad_I': (41.39, -0.52), 'Ciudad_J': (41.23, +2.11)
    }
    
    estado_inicial = 'Ciudad_A'
    solucion = 'Ciudad_G'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    resultado.append(estado_inicial)
    resultado.reverse()
    print("Camino encontrado:", resultado)
    print("Coste:", nodo_solucion.get_coste())
