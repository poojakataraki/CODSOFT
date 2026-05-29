import unittest

from tic_tac_toe import TicTacToe, format_board


class TicTacToeTests(unittest.TestCase):
    def test_detects_winner(self):
        game = TicTacToe()
        game.board = ["X", "X", "X", " ", "O", " ", "O", " ", " "]

        self.assertEqual(game.winner(), "X")

    def test_detects_draw(self):
        game = TicTacToe()
        game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]

        self.assertTrue(game.is_draw())

    def test_rejects_taken_cell(self):
        game = TicTacToe()

        self.assertTrue(game.make_move(0, "X"))
        self.assertFalse(game.make_move(0, "O"))

    def test_ai_takes_winning_move(self):
        game = TicTacToe(human_marker="X")
        game.board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]

        self.assertEqual(game.best_ai_move(), 2)

    def test_ai_blocks_human_win(self):
        game = TicTacToe(human_marker="X")
        game.board = ["X", "X", " ", "O", " ", " ", " ", "O", " "]

        self.assertEqual(game.best_ai_move(), 2)

    def test_format_board_can_show_positions(self):
        board = format_board([" "] * 9, show_positions=True)

        self.assertIn("1", board)
        self.assertIn("9", board)


if __name__ == "__main__":
    unittest.main()
