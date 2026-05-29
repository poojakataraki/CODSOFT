from __future__ import annotations

from dataclasses import dataclass


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


@dataclass
class Move:
    index: int
    score: int


class TicTacToe:
    def __init__(self, human_marker: str = "X") -> None:
        human_marker = human_marker.upper()
        if human_marker not in {"X", "O"}:
            raise ValueError("Marker must be X or O.")

        self.human_marker = human_marker
        self.ai_marker = "O" if human_marker == "X" else "X"
        self.board = [" "] * 9

    def available_moves(self) -> list[int]:
        return [index for index, cell in enumerate(self.board) if cell == " "]

    def make_move(self, index: int, marker: str) -> bool:
        if index < 0 or index >= 9:
            return False
        if self.board[index] != " ":
            return False

        self.board[index] = marker
        return True

    def winner(self) -> str | None:
        for first, second, third in WINNING_LINES:
            if (
                self.board[first] != " "
                and self.board[first] == self.board[second] == self.board[third]
            ):
                return self.board[first]
        return None

    def is_draw(self) -> bool:
        return self.winner() is None and not self.available_moves()

    def game_over(self) -> bool:
        return self.winner() is not None or self.is_draw()

    def best_ai_move(self) -> int:
        move = self._minimax(
            marker=self.ai_marker,
            depth=0,
            alpha=-100,
            beta=100,
        )
        return move.index

    def _minimax(self, marker: str, depth: int, alpha: int, beta: int) -> Move:
        winner = self.winner()
        if winner == self.ai_marker:
            return Move(index=-1, score=10 - depth)
        if winner == self.human_marker:
            return Move(index=-1, score=depth - 10)
        if self.is_draw():
            return Move(index=-1, score=0)

        if marker == self.ai_marker:
            best = Move(index=-1, score=-100)
            for index in self.available_moves():
                self.board[index] = marker
                score = self._minimax(self.human_marker, depth + 1, alpha, beta).score
                self.board[index] = " "

                if score > best.score:
                    best = Move(index=index, score=score)
                alpha = max(alpha, best.score)
                if beta <= alpha:
                    break
            return best

        best = Move(index=-1, score=100)
        for index in self.available_moves():
            self.board[index] = marker
            score = self._minimax(self.ai_marker, depth + 1, alpha, beta).score
            self.board[index] = " "

            if score < best.score:
                best = Move(index=index, score=score)
            beta = min(beta, best.score)
            if beta <= alpha:
                break
        return best


def format_board(board: list[str], show_positions: bool = False) -> str:
    cells = []
    for index, value in enumerate(board):
        if show_positions and value == " ":
            cells.append(str(index + 1))
        else:
            cells.append(value)

    return (
        f" {cells[0]} | {cells[1]} | {cells[2]}\n"
        "---+---+---\n"
        f" {cells[3]} | {cells[4]} | {cells[5]}\n"
        "---+---+---\n"
        f" {cells[6]} | {cells[7]} | {cells[8]}"
    )
