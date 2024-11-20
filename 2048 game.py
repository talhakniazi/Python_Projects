import random
import numpy as np

class Game2048:
    def __init__(self):
        self.board = np.zeros((4, 4), dtype=int)
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        empty_tiles = list(zip(*np.where(self.board == 0)))
        if not empty_tiles:
            return
        row, col = random.choice(empty_tiles)
        self.board[row, col] = 2 if random.random() < 0.9 else 4

    def compress(self, row):
        """Slide non-zero elements to the left in a row."""
        new_row = [i for i in row if i != 0]
        return new_row + [0] * (4 - len(new_row))

    def merge(self, row):
        """Merge adjacent equal elements."""
        for i in range(3):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(self):
        """Move the tiles to the left and merge them."""
        for i in range(4):
            row = self.compress(self.board[i])
            row = self.merge(row)
            self.board[i] = self.compress(row)

    def move_right(self):
        """Move tiles to the right by reversing each row, moving left, and reversing back."""
        self.board = np.fliplr(self.board)
        self.move_left()
        self.board = np.fliplr(self.board)

    def move_up(self):
        """Move tiles up by rotating, moving left, and rotating back."""
        self.board = np.rot90(self.board, -1)
        self.move_left()
        self.board = np.rot90(self.board)

    def move_down(self):
        """Move tiles down by rotating, moving left, and rotating back."""
        self.board = np.rot90(self.board)
        self.move_left()
        self.board = np.rot90(self.board, -1)

    def can_move(self):
        """Check if any moves are possible."""
        if 0 in self.board:
            return True
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j + 1] or self.board[j][i] == self.board[j + 1][i]:
                    return True
        return False

    def print_board(self):
        print("Current Board:")
        print(self.board)

    def play(self):
        print("Welcome to 2048! Use W/A/S/D to move tiles up, left, down, or right.")
        self.print_board()
        
        while True:
            move = input("Enter move (W/A/S/D): ").strip().upper()
            valid_move = True

            if move == "W":
                self.move_up()
            elif move == "A":
                self.move_left()
            elif move == "S":
                self.move_down()
            elif move == "D":
                self.move_right()
            else:
                print("Invalid move! Use W, A, S, or D.")
                valid_move = False

            if valid_move:
                self.spawn_tile()
                self.print_board()

                if not self.can_move():
                    print("Game Over! No more moves available.")
                    break

            if 2048 in self.board:
                print("Congratulations! You've reached 2048!")
                break

# Play the game
if __name__ == "__main__":
    game = Game2048()
    game.play()
