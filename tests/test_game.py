import pytest
from game import create_board, print_board, is_valid_move, make_move, check_winner, is_draw

def test_create_board():
    board = create_board()
    assert len(board) == 3
    for row in board:
        assert len(row) == 3
        for cell in row:
            assert cell == ' '

def test_print_board(capsys):
    board = create_board()
    print_board(board)
    captured = capsys.readouterr()
    assert "1   2   3" in captured.out
    assert "|" in captured.out

def test_is_valid_move():
    board = create_board()
    # Happy path: empty cell within bounds
    assert is_valid_move(board, 0, 0) is True
    assert is_valid_move(board, 2, 2) is True
    # Error path: out of bounds
    assert is_valid_move(board, -1, 0) is False
    assert is_valid_move(board, 0, 3) is False
    assert is_valid_move(board, 3, 2) is False
    # Occupied cell
    board[0][0] = 'X'
    assert is_valid_move(board, 0, 0) is False

def test_make_move():
    board = create_board()
    make_move(board, 1, 2, 'X')
    assert board[1][2] == 'X'
    result = make_move(board, 0, 0, 'O')
    assert result is board

def test_check_winner():
    board = create_board()
    # No winner
    assert check_winner(board) is None
    # Row win for X
    board[0] = ['X', 'X', 'X']
    assert check_winner(board) == 'X'
    # Reset board, column win for O
    board = create_board()
    for i in range(3):
        board[i][1] = 'O'
    assert check_winner(board) == 'O'
    # Diagonal win
    board = create_board()
    board[0][0] = 'X'; board[1][1] = 'X'; board[2][2] = 'X'
    assert check_winner(board) == 'X'
    # Anti-diagonal win
    board = create_board()
    board[0][2] = 'O'; board[1][1] = 'O'; board[2][0] = 'O'
    assert check_winner(board) == 'O'

def test_is_draw():
    board = create_board()
    # Empty board
    assert is_draw(board) is False
    # Partially filled
    board[0][0] = 'X'
    assert is_draw(board) is False
    # Full board, no winner
    full_no_winner = [
        ['X', 'O', 'X'],
        ['X', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    assert is_draw(full_no_winner) is True
    # Full board, but there is a winner (edge case: function only checks fullness)
    full_win = [
        ['X', 'X', 'X'],
        ['O', 'O', 'X'],
        ['O', 'X', 'O']
    ]
    assert is_draw(full_win) is True