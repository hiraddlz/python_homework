class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class Board:
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        for i in range(3):
            lines.append(
                f" {self.board_array[i][0]} | {self.board_array[i][1]} | {self.board_array[i][2]} "
            )
            if i < 2:
                lines.append("-----------")
        return "\n".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        col = move_index % 3

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check rows
        for row in self.board_array:
            if row[0] == row[1] == row[2] != " ":
                return (True, f"{row[0]} wins!")

        # Check columns
        for col in range(3):
            if (
                self.board_array[0][col]
                == self.board_array[1][col]
                == self.board_array[2][col]
                != " "
            ):
                return (True, f"{self.board_array[0][col]} wins!")

        # Check diagonals
        if (
            self.board_array[0][0]
            == self.board_array[1][1]
            == self.board_array[2][2]
            != " "
        ):
            return (True, f"{self.board_array[0][0]} wins!")
        if (
            self.board_array[0][2]
            == self.board_array[1][1]
            == self.board_array[2][0]
            != " "
        ):
            return (True, f"{self.board_array[0][2]} wins!")

        # Check for tie
        if all(cell != " " for row in self.board_array for cell in row):
            return (True, "Cat's Game")

        return (False, f"{self.turn}'s turn")


if __name__ == "__main__":
    board = Board()
    print("Welcome to Tic Tac Toe!")

    while True:
        print("\n" + str(board))
        status, message = board.whats_next()
        if status:
            print(message)
            break

        print(message)
        try:
            print("Valid moves are:")
            for move in Board.valid_moves:
                print(f"- {move}")
            move = input("Enter your move: ").strip().lower()
            board.move(move)
        except TictactoeException as e:
            print(f"Error: {e}")
