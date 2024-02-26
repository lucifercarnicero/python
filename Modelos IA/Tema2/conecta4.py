import numpy as np

# Definir el tamaño del tablero
ROWS = 6
COLS = 7

# Definir los posibles movimientos (colocar una ficha en una columna)
POSSIBLE_MOVES = list(range(COLS))

# Valor de evaluación para estados de juego
WINNING_SCORE = 1000
LOSING_SCORE = -1000

# Crear una clase para representar el estado del juego
class Connect4State:
    def __init__(self, board=None, player='X'):
        if board is None:
            self.board = np.full((ROWS, COLS), ' ')
        else:
            self.board = board
        self.player = player

    def is_valid_move(self, col):
        return self.board[0][col] == ' '  # Si la columna no está llena

    def make_move(self, col):
        new_board = self.board.copy()  # Copia el tablero actual para evitar modificaciones en el estado original
        for row in range(ROWS - 1, -1, -1):
            if new_board[row][col] == ' ':
                new_board[row][col] = self.player
                return Connect4State(new_board, 'X' if self.player == 'O' else 'O')

    def is_terminal(self):
        # Verificar si hay un ganador
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != ' ':
                    player = self.board[row][col]
                    if (
                        col + 3 < COLS and all(self.board[row][col + i] == player for i in range(4)) or
                        row + 3 < ROWS and all(self.board[row + i][col] == player for i in range(4)) or
                        col + 3 < COLS and row + 3 < ROWS and all(self.board[row + i][col + i] == player for i in range(4)) or
                        col - 3 >= 0 and row + 3 < ROWS and all(self.board[row + i][col - i] == player for i in range(4))
                    ):
                        return True, player

        # Verificar si hay empate
        if ' ' not in self.board:
            return True, None

        return False, None

    def __str__(self):
        return "\n".join([" ".join(row) for row in self.board])

# Función de evaluación simple para el estado del juego
def evaluate_state(state, player):
    if state.is_terminal()[0]:
        winner = state.is_terminal()[1]
        if winner == player:
            return WINNING_SCORE
        elif winner:
            return LOSING_SCORE
    return 0

# Implementar el algoritmo Minimax con poda alfa-beta
def minimax(state, depth, alpha, beta, maximizing_player):
    if depth == 0 or state.is_terminal()[0]:
        return evaluate_state(state, 'X')  # Cambiar 'X' por el jugador de la IA

    if maximizing_player:
        max_eval = float('-inf')
        for move in POSSIBLE_MOVES:
            if state.is_valid_move(move):
                new_state = state.make_move(move)
                eval = minimax(new_state, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in POSSIBLE_MOVES:
            if state.is_valid_move(move):
                new_state = state.make_move(move)
                eval = minimax(new_state, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Función para seleccionar el mejor movimiento usando Minimax
def best_move(state):
    best_eval = float('-inf')
    best_move = None
    for move in POSSIBLE_MOVES:
        if state.is_valid_move(move):
            new_state = state.make_move(move)
            eval = minimax(new_state, 5, float('-inf'), float('inf'), False)  # Profundidad de búsqueda 5 (ajusta según tus necesidades)
            if eval > best_eval:
                best_eval = eval
                best_move = move
    return best_move

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" ".join(row))
    print("1 2 3 4 5 6 7")  # Etiquetas de las columnas

# Juego principal
def main():
    current_player = 'O'  # Comienza el jugador humano
    initial_state = Connect4State(player=current_player)
    print_board(initial_state.board)

    while True:
        if current_player == 'O':
            # Turno del jugador humano
            human_col = int(input(f'Jugador {current_player}, elige una columna (1-7): ')) - 1
            while not initial_state.is_valid_move(human_col):
                print('Movimiento no válido. Inténtalo de nuevo.')
                human_col = int(input(f'Jugador {current_player}, elige una columna (1-7): ')) - 1
            initial_state = initial_state.make_move(human_col)
        else:
            # Turno de la computadora (usando Minimax con poda alfa-beta)
            computer_col = best_move(initial_state)
            initial_state = initial_state.make_move(computer_col)

        print_board(initial_state.board)

        is_terminal, winner = initial_state.is_terminal()
        if is_terminal:
            if winner:
                print(f'El ganador es el jugador {winner}.')
            else:
                print('Empate.')
            break

        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    main()
