# Sudoku solver using backtracking

def print_board(board):
    """Helper function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def is_valid(board, row, col, num, size):
    """Check if placing num at board[row][col] is valid."""
    # Check row
    for i in range(size):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(size):
        if board[i][col] == num:
            return False

    # Check 3x3 sub-grid
    box_size = int(size ** 0.5)
    start_row, start_col = box_size * (row // box_size), box_size * (col // box_size)
    for i in range(start_row, start_row + box_size):
        for j in range(start_col, start_col + box_size):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board, size):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(size):
        for col in range(size):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, size + 1):
                    if is_valid(board, row, col, num, size):  # Check if the number is valid
                        board[row][col] = num  # Place the number
                        if solve_sudoku(board, size):  # Recursively attempt to solve the rest
                            return True
                        board[row][col] = 0  # Reset if it leads to no solution
                return False  # Trigger backtracking
    return True  # Solved

def get_board_from_user(size):
    """Get a Sudoku board of given size from the user."""
    board = []
    print(f"Enter the Sudoku board (size {size}x{size}) row by row, using 0 for empty cells:")
    for i in range(size):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != size:
                    raise ValueError
                board.append(row)
                break
            except ValueError:
                print(f"Please enter exactly {size} numbers separated by spaces.")
    return board

# Example usage
if __name__ == "__main__":
    # Example puzzle with 0 representing empty cells
    while True:
        try:
            size = int(input("Enter Sudoku board size (choose 3, 6, or 9): "))
            if size not in {3, 6, 9}:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 3, 6, or 9.")

    # Get the board from the user
    sudoku_board = get_board_from_user(size)

    print("\nOriginal board:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board, size):
        print("Solved board:")
        print_board(sudoku_board)
    else:
        print("No solution exists.")
