# Tic-Tac-Toe AI

A simple command-line Tic-Tac-Toe game where a human player plays against an unbeatable computer opponent. The AI uses the Minimax algorithm with alpha-beta pruning, so it always chooses the best available move.

## Features

- Human vs computer gameplay
- Unbeatable AI using Minimax
- Alpha-beta pruning for faster search
- Option to choose your marker
- Input validation for occupied or invalid cells
- Clean Python code with unit tests

## Project Structure

```text
.
├── main.py
├── tic_tac_toe.py
├── test_tic_tac_toe.py
├── requirements.txt
└── README.md
```

## How to Run

Make sure Python 3.9 or newer is installed.

```bash
python main.py
```

The board positions are numbered like this:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Enter the number of the cell where you want to place your mark.

## Running Tests

```bash
python -m unittest
```

## How the AI Works

The AI checks every possible future board state and gives each result a score:

- Win for AI: positive score
- Draw: zero
- Win for human: negative score

Minimax chooses the move that gives the AI the best final outcome. Alpha-beta pruning skips branches that cannot improve the final choice, which keeps the search efficient.

## Notes

Since Tic-Tac-Toe is a solved game, the best result a human can get against this AI is a draw.
