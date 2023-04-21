import math

# Récupérer le symbole de l'adversaire
def get_opponent_symbol(symbol):
    return "O" if symbol == "X" else "X"

# Évaluer l'état actuel de la grille
def evaluate_board(board, symbol):
    # Évaluer les lignes
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == symbol:
            return 10
        elif board[row][0] == board[row][1] == board[row][2] == get_opponent_symbol(symbol):
            return -10
    # Évaluer les colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == get_opponent_symbol(symbol):
            return -10
    # Évaluer les diagonales
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return 10
    elif board[0][0] == board[1][1] == board[2][2] == get_opponent_symbol(symbol):
        return -10
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return 10
    elif board[0][2] == board[1][1] == board[2][0] == get_opponent_symbol(symbol):
        return -10
    # Si aucun joueur n'a gagné, retourner 0
    return 0

# Vérifier si la partie est terminée
def is_game_over(board):
    # Vérifier les lignes
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return True
    # Vérifier les colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True
    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    # Vérifier si la grille est pleine
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

# Obtenir les coups valides pour un état donné de la grille
def get_valid_moves(board):
    valid_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                valid_moves.append((row, col))
    return valid_moves

# Minimax avec élagage alpha-bêta
def minimax(board, depth, alpha, beta, maximizing_player, symbol):
    # Vérifier si la partie est terminée ou si la profondeur maximale est atteinte
    if is_game_over(board) or depth == 0:
        return evaluate_board(board, symbol)

    # Maximiser le score pour l'ordinateur
    if maximizing_player:
        max_score = -math.inf
        for move in get_valid_moves(board):
            row, col = move
            board[row][col] = symbol
            score = minimax(board, depth - 1, alpha, beta, False, symbol)
            board[row][col] = ""
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score

    # Minimiser le score pour le joueur humain
    else:
        min_score = math.inf
        for move in get_valid_moves(board):
            row, col = move
            board[row][col] = get_opponent_symbol(symbol)
            score = minimax(board, depth - 1, alpha, beta, True, symbol)
            board[row][col] = ""
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score


# Fonction pour obtenir le meilleur coup possible
def get_best_move(board, symbol):
    best_score = -math.inf
    best_move = None
    for move in get_valid_moves(board):
        row, col = move
        board[row][col] = symbol
        score = minimax(board, 5, -math.inf, math.inf, False, symbol)
        board[row][col] = ""
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
