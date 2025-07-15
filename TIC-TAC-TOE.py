import math

# Initialize board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Function to check if there's a winner
def winner(b, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False

# Function to check if board is full
def is_draw():
    return ' ' not in board

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if winner(b, 'O'):
        return 1
    elif winner(b, 'X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function for AI move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Function to handle player move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is taken!")
        except (ValueError, IndexError):
            print("Invalid input. Enter number from 1 to 9.")

# Main game loop
def play_game():
    print("Tic-Tac-Toe: You (X) vs AI (O)")
    print_board()

    while True:
        player_move()
        print_board()
        if winner(board, 'X'):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("AI's move:")
        ai_move()
        print_board()
        if winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

# Start the game
play_game()
