def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != '':
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    # Check for a tie
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return ''

    return 'tie'


def get_score(result):
    if result == 'O':
        return 1  # AI wins
    elif result == 'X':
        return -1  # Opponent wins
    else:
        return 0  # Tie


def minimax(board, is_maximizing):
    result = check_winner(board)

    if result != '':
        return get_score(result)

    if is_maximizing:
        best_score = float('-inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'  # Assume the AI player is 'O'
                    score = minimax(board, False)
                    board[i][j] = ''  # Undo the move
                    best_score = max(score, best_score)

        return best_score
    else:
        best_score = float('inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'  # Assume the opponent is 'X'
                    score = minimax(board, True)
                    board[i][j] = ''  # Undo the move
                    best_score = min(score, best_score)

        return best_score


def get_next_move(board):
    # Convert the board to a 2D list
    board = [[board[i * 3 + j] for j in range(3)] for i in range(3)]

    # Find the best move using the Minimax algorithm
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'  # Assume the AI player is 'O'
                score = minimax(board, False)
                board[i][j] = ''  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move
