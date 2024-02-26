def es_estado_valido(estado):
    # Verifica si el estado es válido según las restricciones del problema
    izquierda = estado['Izquierda']
    derecha = estado['Derecha']

    if ('H' in izquierda and ('L' in izquierda or 'P' in izquierda or 'R' in izquierda)) or \
       ('H' in derecha and ('L' in derecha or 'P' in derecha or 'R' in derecha)):
        return False
    return True

def imprimir_estado(estado):
    print("\nEstado actual:")
    print(f"Orilla Izquierda: {', '.join(estado['Izquierda'])}")
    print(f"Orilla Derecha: {', '.join(estado['Derecha'])}")

def cruzar_calle(estado_actual):
    while estado_actual != {'H', 'L', 'P', 'R'}:
        imprimir_estado(estado_actual)
        acciones_posibles = []

        elementos_en_orilla_izquierda = estado_actual['Izquierda']
        elementos_en_orilla_derecha = estado_actual['Derecha']

        for elemento in elementos_en_orilla_izquierda:
            nuevo_estado = estado_actual.copy()
            nuevo_estado['Izquierda'].remove(elemento)
            nuevo_estado['Derecha'].add(elemento)
            if es_estado_valido(nuevo_estado):
                acciones_posibles.append(f"Cruza a la izquierda con {elemento}")

        for lado in ('Izquierda', 'Derecha'):
            for elemento in elementos_en_orilla_izquierda:
                nuevo_estado = estado_actual.copy()
                nuevo_estado['Izquierda'].remove(elemento)
                nuevo_estado[lado].add(elemento)
                if es_estado_valido(nuevo_estado):
                    acciones_posibles.append(f"Cruza a la izquierda solo a {lado}")

        for lado1, lado2 in [('Izquierda', 'Derecha'), ('Derecha', 'Izquierda')]:
            for elemento1 in elementos_en_orilla_izquierda:
                for elemento2 in elementos_en_orilla_izquierda:
                    nuevo_estado = estado_actual.copy()
                    nuevo_estado['Izquierda'].remove(elemento1)
                    nuevo_estado['Izquierda'].remove(elemento2)
                    nuevo_estado[lado1].add(elemento1)
                    nuevo_estado[lado2].add(elemento2)
                    if es_estado_valido(nuevo_estado):
                        acciones_posibles.append(f"Cruza a la izquierda con {elemento1} y {elemento2} de {lado1} a {lado2}")

        print("\nAcciones posibles:")
        for i, accion in enumerate(acciones_posibles):
            print(f"{i + 1}. {accion}")

        seleccion = input("Selecciona una acción (1-{len(acciones_posibles)}) o 'q' para salir: ")
        if seleccion == 'q':
            print("¡Abandonaste el juego!")
            return

        try:
            seleccion = int(seleccion) - 1
            if 0 <= seleccion < len(acciones_posibles):
                accion_elegida = acciones_posibles[seleccion]
                print(f"\nElegiste: {accion_elegida}")
                if "Cruza a la izquierda solo" in accion_elegida:
                    print("¡Oh no! Dejaste a los elementos solos. Has perdido.")
                    return
                estado_actual = nuevo_estado
            else:
                print("Selección no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Selección no válida. Inténtalo de nuevo.")

    imprimir_estado(estado_actual)
    print("¡Felicidades! Has cruzado la calle con éxito con todos los elementos.")

if __name__ == "__main__":
    estado_inicial = {'H': {'H'}, 'Izquierda': {'L', 'P', 'R'}, 'Derecha': {}}
    cruzar_calle(estado_inicial)
