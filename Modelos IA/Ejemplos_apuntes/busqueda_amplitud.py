from nodos import Nodo


def buscar_solucion_BFS(estado_inicial,solucion):

    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodoInicial=Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while(not solucionado) and len(nodos_frontera)!=0:

        nodo=nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos()==solucion:
            # solucion encontrada
            solucionado=True
            return nodo
        else:
            # expandir nodos hijo 
            dato_nodo=nodo.get_datos()

            hijo=[dato_nodo[1],dato_nodo[0],dato_nodo[2],dato_nodo[3]]
            hijo_izq=Nodo(hijo)
            if not hijo_izq.en_lista(nodos_visitados) and not hijo_izq.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izq)
            hijo=[dato_nodo[0],dato_nodo[2],dato_nodo[1],dato_nodo[3]]

            hijo_central=Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)

            hijo=[dato_nodo[0],dato_nodo[1],dato_nodo[3],dato_nodo[2]]

            hijo_der=Nodo(hijo)
            if not hijo_der.en_lista(nodos_visitados) and not hijo_der.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_der)

            nodo.set_hijos([hijo_izq,hijo_central,hijo_der])

#aquí esta el problema probando lo de antes
if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    
    # Mostrar estado inicial
    print("Estado Inicial:", estado_inicial)

    # Mostrar pasos intermedios
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    # Mostrar pasos intermedios en orden
    for paso in reversed(resultado):
        print("Paso Intermedio:", paso)

    # Mostrar solución final
    print("Solución Final:", solucion)




