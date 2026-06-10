import pytest
from unittest.mock import patch, MagicMock, call
import main

@pytest.fixture
def mock_game():
    with patch('main.game') as mock:
        yield mock

def test_play_game_x_wins(mock_game):
    mock_game.create_board.return_value = [[' ']*3 for _ in range(3)]
    mock_game.is_valid_move.side_effect = [True, True, True, True, True]
    mock_game.check_winner.side_effect = [None, None, None, None, 'X']
    mock_game.is_draw.return_value = False
    inputs = ['1,1', '2,1', '1,2', '2,2', '1,3']
    with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
        main.play_game()
    # Verify winner message printed
    mock_print.assert_any_call("Player X wins!")
    assert mock_game.make_move.call_count == 5

def test_play_game_draw(mock_game):
    mock_game.create_board.return_value = [[' ']*3 for _ in range(3)]
    mock_game.is_valid_move.return_value = True
    mock_game.check_winner.return_value = None
    mock_game.is_draw.side_effect = [False, False, False, False, False, False, False, False, True]
    # 9 valid moves, then draw
    inputs = ['1,1','2,1','3,1','1,2','2,2','3,2','1,3','2,3','3,3']
    with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
        main.play_game()
    mock_print.assert_any_call("It's a draw!")
    assert mock_game.make_move.call_count == 9

def test_invalid_input_format_caught(mock_game):
    mock_game.create_board.return_value = [[' ']*3 for _ in range(3)]
    # First input invalid, then valid moves leading to X win
    mock_game.is_valid_move.side_effect = [True, True, True]
    mock_game.check_winner.side_effect = [None, None, 'X']
    mock_game.is_draw.return_value = False
    inputs = ['abc', '1,1', '2,1', '1,2']
    with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
        main.play_game()
    # Should print invalid message
    mock_print.assert_any_call('\nInvalid input. Please enter row and column numbers separated by a comma.\n')
    # Game continues and X wins
    mock_print.assert_any_call("Player X wins!")

def test_invalid_move_occupied_or_out_of_range(mock_game):
    mock_game.create_board.return_value = [[' ']*3 for _ in range(3)]
    # is_valid_move returns False first, then True for next moves
    mock_game.is_valid_move.side_effect = [False, True, True, True]
    mock_game.check_winner.side_effect = [None, None, 'X']
    mock_game.is_draw.return_value = False
    inputs = ['1,1', '1,1', '2,1', '1,2']  # 1,1 invalid first, then valid
    with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
        main.play_game()
    mock_print.assert_any_call('\nInvalid move. Cell occupied or out of range. Try again.\n')
    mock_print.assert_any_call("Player X wins!")

def test_value_error_from_parsing_caught(mock_game):
    mock_game.create_board.return_value = [[' ']*3 for _ in range(3)]
    # 1. input causes ValueError during int conversion, then valid
    mock_game.is_valid_move.side_effect = [True, True, True]
    mock_game.check_winner.side_effect = [None, None, 'X']
    mock_game.is_draw.return_value = False
    inputs = ['x,y', '1,1', '2,1', '1,2']
    with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
        main.play_game()
    mock_print.assert_any_call('\nInvalid input. Please enter row and column numbers separated by a comma.\n')
    mock_print.assert_any_call("Player X wins!")