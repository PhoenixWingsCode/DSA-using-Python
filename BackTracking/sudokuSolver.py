def is_valid(board, row, col, num):
    # Check if num is not in the current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num is not in the current column
    for y in range(9):
        if board[y][col] == num:
            return False

    # Check if num is not in the current 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True

def solve_sudoku(board):
    # Find an empty spot on the board (denoted by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try all digits from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Recursively solve the rest
                        if solve_sudoku(board):
                            return True

                        # Backtrack if num did not lead to a solution
                        board[row][col] = 0
                return False  # trigger backtracking
    return True  # solved

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i!= 0:
            print("-" * 21)  # print horizontal separator
        for j in range(9):
            if j % 3 == 0 and j!= 0:
                print("|", end=" ")
            val = board[i][j]
            print(val if val!= 0 else ".", end=" ")
        print()

# Example Sudoku puzzle (0 means empty cell)
example_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]


print("Original Sudoku Board:")
print_board(example_board)

if solve_sudoku(example_board):
    print("Solved Sudoku Board:")
    print_board(example_board)
else:
    print("No solution exists.")