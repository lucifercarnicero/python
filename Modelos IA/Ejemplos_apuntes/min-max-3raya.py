MAX = 1
MIN = -1
jugada_maquina = None

def minimax(tablero, jugador):
    global jugada_maquina

    if game_over(tablero):
        return [ganador(tablero), 0]

    movimientos = []
    for jugada in range(0, len(tablero)):
        if tablero[jugada] == 0:
            tableroaux = tablero[:]
            tableroaux[jugada] = jugador
            puntuacion = minimax(tableroaux, jugador * (-1))
            movimientos.append([puntuacion, jugada])

    if jugador == MAX:
        movimiento = max(movimientos)
        jugada_maquina = movimiento[1]
        return movimiento[0]
    else:
        movimiento = min(movimientos)
        return movimiento[0]

def game_over(tablero):
    if ganador(tablero) != 0 or 0 not in tablero:
        return True
    return False

def ganador(tablero):
    # Verificar filas, columnas y diagonales
    lineas_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]

    for linea in lineas_ganadoras:
        if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]] != 0:
            return tablero[linea[0]]

    return 0

def imprimir_tablero(tablero):
    for i in range(0, 9, 3):
        print(tablero[i:i + 3])

def turno_jugador(tablero):
    jugada = int(input("Ingresa tu jugada (0-8): "))
    while tablero[jugada] != 0:
        print("¡Espacio ocupado! Elige otro.")
        jugada = int(input("Ingresa tu jugada (0-8): "))
    tablero[jugada] = MIN

def juego_tres_en_raya():
    tablero = [0] * 9
    while not game_over(tablero):
        imprimir_tablero(tablero)
        turno_jugador(tablero)
        if not game_over(tablero):
            minimax(tablero, MAX)
            tablero[jugada_maquina] = MAX

    imprimir_tablero(tablero)

    if ganador(tablero) == MIN:
        print("¡Has ganado!")
    elif ganador(tablero) == MAX:
        print("¡La máquina ha ganado!")
    else:
        print("¡Empate!")

if __name__ == "__main__":
    juego_tres_en_raya()
