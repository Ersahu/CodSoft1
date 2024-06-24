board = [' ' for _ in range(9)]

def print_board():
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-------------')

def is_board_full(board):
    return ' ' not in board

def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
    if check_win(board, 'X'):
        return -10 + depth
    if check_win(board, 'O'):
        return 10 - depth
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

while True:
    print_board()
    while True:
        try:
            player_move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= player_move <= 8 and board[player_move] == ' ':
                board[player_move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

    if check_win(board, 'X'):
        print_board()
        print("You win!")
        break
    if is_board_full(board):
        print_board()
        print("It's a draw!")
        break

    # AI player's turn
    ai_move = find_best_move(board)
    board[ai_move] = 'O'

    if check_win(board, 'O'):
        print_board()
        print("AI wins!")
        break
    if is_board_full(board):
        print_board()
        print("It's a draw!")
        break
