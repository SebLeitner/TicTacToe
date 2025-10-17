"""Simple command-line Tic-Tac-Toe game for two players.

Run the module directly to start a game in the terminal::

    python main.py
"""
from __future__ import annotations

import itertools
from typing import List, Optional


Board = List[str]


def create_board() -> Board:
    """Return a new empty tic-tac-toe board."""
    return [" "] * 9


def render_board(board: Board) -> str:
    """Return a string representation of the board."""
    rows = [" | ".join(board[i : i + 3]) for i in range(0, 9, 3)]
    divider = "\n---------\n"
    return divider.join(rows)


def available_moves(board: Board) -> List[int]:
    """Return the list of indices for empty positions."""
    return [idx for idx, value in enumerate(board) if value == " "]


def has_winner(board: Board) -> Optional[str]:
    """Return the winning symbol if a player has won, otherwise ``None``."""
    winning_positions = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def is_draw(board: Board) -> bool:
    """Return ``True`` if the board is full and there is no winner."""
    return " " not in board and has_winner(board) is None


def prompt_move(player: str, board: Board) -> int:
    """Prompt the given player to choose a move.

    The user is repeatedly asked until a valid move is provided.
    """
    valid_choices = {str(i + 1): i for i in available_moves(board)}

    while True:
        print(render_board(board))
        print()
        choice = input(f"Spieler {player}, wähle ein Feld (1-9): ").strip()
        if choice not in valid_choices:
            print("Ungültige Eingabe. Bitte wähle eine freie Zahl zwischen 1 und 9.\n")
            continue
        return valid_choices[choice]


def play_game() -> None:
    """Play a single round of Tic-Tac-Toe."""
    board = create_board()
    players = itertools.cycle(["X", "O"])

    for player in players:
        move = prompt_move(player, board)
        board[move] = player

        winner = has_winner(board)
        if winner:
            print(render_board(board))
            print(f"\nGlückwunsch! Spieler {winner} hat gewonnen!\n")
            return

        if is_draw(board):
            print(render_board(board))
            print("\nUnentschieden! Keine weiteren Züge möglich.\n")
            return


def main() -> None:
    """Main entry point that allows repeated play."""
    print("Willkommen zu Tic-Tac-Toe!\n")
    while True:
        play_game()
        again = input("Noch einmal spielen? (j/n): ").strip().lower()
        print()
        if again not in {"j", "ja"}:
            print("Danke fürs Spielen!")
            return


if __name__ == "__main__":
    main()
