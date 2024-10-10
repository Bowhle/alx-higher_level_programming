#!/usr/bin/python3
import sys


def print_solutions(solutions):
    """Print the list of solutions."""
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    # Check this column on upper side
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, solutions):
    """Utilize backtracking to solve the N queens problem."""
    if row >= len(board):
        solutions.append(board[:])  # Found a valid solution
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            solve_n_queens_util(board, row + 1, solutions)  # Recur
            board[row] = -1  # Backtrack


def solve_n_queens(n):
    """Solve the N queens problem and print all solutions."""
    board = [-1] * n  # Initialize board with -1 (no queens placed)
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)

    # Format and print solutions
    formatted_solutions = []
    for solution in solutions:
        formatted_solutions.append([(i, solution[i]) for i in range(n)])
    print_solutions(formatted_solutions)
