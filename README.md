# Tic Tac Toe

A simple command-line Tic Tac Toe game implemented in Python.

## Getting Started

### Prerequisites
- Python 3.6+

### Run the game

```bash
python main.py
```

## How to Play

- Players take turns entering coordinates in the form `row,column` (e.g., `1,1` for top-left).
- Rows and columns are numbered 1 to 3.
- Player 1 uses `X`, Player 2 uses `O`.
- The board is displayed after each move.
- Game ends when a player wins or the board is full (draw).

## Project Structure

- `game.py` – Game logic (board, win/draw detection)
- `main.py` – Command-line entry point
- `requirements.txt` – Empty (no external dependencies)

## Architecture Decision Record

This project follows the ADR specifying:
- In-memory state machine (Python module)
- Command-line interface (CLI)
- No external dependencies

See ADR-001 and ADR-002 for details.