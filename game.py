"""
Core game logic for Tic Tac Toe.
Board is represented as a list of lists (3x3).
State is managed in-memory via function calls.
"""

def create_board():
    """Return an empty 3x3 board filled with spaces."""
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_board(board):
    """Display the board in ASCII format."""
    print('\n  1   2   3')
    for i, row in enumerate(board):
        print(f'{i+1} ' + ' | '.join(row))
        if i < 2:
            print('  ---+---+---')
    print()


def is_valid_move(board, row, col):
    """Check if the move at (row, col) is within bounds and cell is empty."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


def make_move(board, row, col, player):
    """Place player's symbol on board at (row, col). Returns new board."""
    board[row][col] = player
    return board


def check_winner(board):
    """Return 'X' or 'O' if that player wins, else None."""
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def is_draw(board):
    """Return True if board is full and no winner."""
    for row in board:
        if ' ' in row:
            return False
    return True
