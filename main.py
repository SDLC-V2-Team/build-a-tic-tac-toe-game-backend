"""
Command-line interface for two-player Tic Tac Toe.
Players enter moves as 'row,col' (e.g., '1,1').
"""
import game

def play_game():
    board = game.create_board()
    current_player = 'X'
    while True:
        game.print_board(board)
        print(f"Player {current_player}'s turn.")
        move = input('Enter row,column (e.g., 1,1): ').strip()
        try:
            parts = move.split(',')
            if len(parts) != 2:
                raise ValueError
            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
            if not game.is_valid_move(board, row, col):
                print('\nInvalid move. Cell occupied or out of range. Try again.\n')
                continue
        except (ValueError, IndexError):
            print('\nInvalid input. Please enter row and column numbers separated by a comma.\n')
            continue

        game.make_move(board, row, col, current_player)
        winner = game.check_winner(board)
        if winner:
            game.print_board(board)
            print(f'Player {winner} wins!')
            break
        if game.is_draw(board):
            game.print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    play_game()
