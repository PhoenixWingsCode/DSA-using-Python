def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # Found one solution; append the current board configuration
        solution = [''.join(row) for row in board]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'  # Place queen
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = '.'  # Backtrack

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Example usage:
n = 4
all_solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(all_solutions)}")
for solution in all_solutions:
    for row in solution:
        print(row)
    print()