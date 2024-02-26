from collections import deque

# Función para verificar si un jugador ha ganado la partida
def verificar_victoria(tablero, jugador):
    # Verificar en horizontal
    for fila in range(6):
        for columna in range(4):
            if all(tablero[fila][columna + i] == jugador for i in range(4)):
                return True

    # Verificar en vertical
    for fila in range(3):
        for columna in range(7):
            if all(tablero[fila + i][columna] == jugador for i in range(4)):
                return True

    # Verificar en diagonal hacia abajo y hacia la derecha
    for fila in range(3):
        for columna in range(4):
            if all(tablero[fila + i][columna + i] == jugador for i in range(4)):
                return True

    # Verificar en diagonal hacia abajo y hacia la izquierda
    for fila in range(3):
        for columna in range(3, 7):
            if all(tablero[fila + i][columna - i] == jugador for i in range(4)):
                return True

    return False

# Función para encontrar el ganador o empate utilizando BFS
def encontrar_ganador_o_empate(tablero, jugador_actual):
    cola = deque()
    estado_inicial = (tablero, jugador_actual)  # Suponemos que es el turno del jugador actual
    cola.append(estado_inicial)

    while cola:
        tablero_actual, jugador_actual = cola.popleft()

        # Verificar si el jugador actual ha ganado
        if verificar_victoria(tablero_actual, jugador_actual):
            return jugador_actual, tablero_actual

        # Verificar si la partida termina en empate
        if all(casilla != "_" for fila in tablero_actual for casilla in fila):
            return "Empate", tablero_actual

        # Generar posibles movimientos para el jugador actual
        for columna in range(7):
            for fila in range(5, -1, -1):
                if tablero_actual[fila][columna] == "_":
                    nuevo_tablero = [fila[:] for fila in tablero_actual]
                    nuevo_tablero[fila][columna] = jugador_actual
                    cola.append((nuevo_tablero, jugador_actual))

    return None, tablero

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print("\n")

# Tablero inicial
tablero = [
    ["_", "X", "_", "O", "_", "X", "_"],
    ["_", "O", "_", "O", "O", "X", "_"],
    ["_", "O", "_", "X", "X", "O", "_"],
    ["X", "O", "_", "O", "O", "X", "_"],
    ["O", "X", "_", "O", "X", "O", "_"],
    ["X", "X", "X", "O", "X", "X", "_"]
]

# Iniciar el juego y mostrar el tablero inicial
print("Tablero Inicial:")
imprimir_tablero(tablero)

# Encontrar el ganador o empate en los próximos movimientos
ganador, nuevo_tablero = encontrar_ganador_o_empate(tablero, "X")

# Mostrar el tablero final y al ganador
if ganador:
    if ganador == "Empate":
        print("La partida terminó en empate.")
    else:
        print(f"¡El ganador es el jugador {ganador}!")
    print("Tablero Final:")
    imprimir_tablero(nuevo_tablero)
