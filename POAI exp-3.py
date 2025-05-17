import math

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a winner
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player] * 3 in win_conditions

# Function to check if moves are left
def is_moves_left(board):
    return any(EMPTY in row for row in board)

# Minimax Algorithm
def minimax(board, is_max):
    if check_winner(board, PLAYER_X):
        return -10
    if check_winner(board, PLAYER_O):
        return 10
    if not is_moves_left(board):
        return 0

    best_score = -math.inf if is_max else math.inf

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O if is_max else PLAYER_X
                score = minimax(board, not is_max)
                board[row][col] = EMPTY
                best_score = max(best_score, score) if is_max else min(best_score, score)

    return best_score

# Find the best move for the AI (PLAYER_O)
def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                score = minimax(board, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

# Get user input for a 3×3 Tic-Tac-Toe board
def get_user_board():
    print("Enter your Tic-Tac-Toe board row by row (use 'X', 'O', or '_' for empty cells):")
    board = []
    for i in range(3):
        row = input().strip().split()
        board.append(row)  # Append the row to maintain the 3×3 format
    return board

# Start Game
board = get_user_board()
print_board(board)

# AI makes its move
move = find_best_move(board)
if move != (-1, -1):
    board[move[0]][move[1]] = PLAYER_O
    print(f"\nAI chose position {move}")

print_board(board)
