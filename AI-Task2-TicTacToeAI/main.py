from tic_tac_toe import TicTacToe, format_board


def ask_marker() -> str:
    while True:
        marker = input("Choose your marker (X/O): ").strip().upper()
        if marker in {"X", "O"}:
            return marker
        print("Please enter X or O.")


def ask_move(game: TicTacToe) -> int:
    while True:
        choice = input("Enter your move (1-9): ").strip()
        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        index = int(choice) - 1
        if game.make_move(index, game.human_marker):
            return index

        print("That cell is not available. Try another one.")


def print_result(game: TicTacToe) -> None:
    winner = game.winner()
    if winner == game.human_marker:
        print("You won!")
    elif winner == game.ai_marker:
        print("Computer won!")
    else:
        print("It's a draw!")


def play_game() -> None:
    print("Tic-Tac-Toe AI")
    print()
    print("Board positions:")
    print(format_board([" "] * 9, show_positions=True))
    print()

    human_marker = ask_marker()
    game = TicTacToe(human_marker)

    human_turn = human_marker == "X"

    while not game.game_over():
        print()
        print(format_board(game.board))
        print()

        if human_turn:
            ask_move(game)
        else:
            move = game.best_ai_move()
            game.make_move(move, game.ai_marker)
            print(f"Computer placed {game.ai_marker} at position {move + 1}.")

        human_turn = not human_turn

    print()
    print(format_board(game.board))
    print()
    print_result(game)


if __name__ == "__main__":
    play_game()
