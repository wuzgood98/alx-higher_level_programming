#!/usr/bin/python3
# 101-nqueens.py
# Gideon O Addo
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
from sys import exit, argv


def print_usage_and_exit():
    """
    Prints the usage message and exits the program with status code 1
    """
    print('Usage: nqueens N')
    exit(1)


def print_error_and_exit(message):
    """
    Prints an error message and exits the program with status code 1.

    Args:
        message (str): The error message to be printed.
    """
    print(message)
    exit(1)


def is_valid(board, row, col):
    """
    Checks if placing a queen at the given row and column is valid.

    Args:
        board (list): The current state of the board.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.

    Returns:
        bool: true if the position is valid, False otherwise.
    """
    for i in range(row):
        if ((board[i] == col)
                or (board[i] - i == col - row)
                or (board[i] + i == col + row)):
            return False
    return True


def solve_nqueens(N):
    """
    Solves the N Queens problem and returns all possible solutions.

    Args:
        N (int): The size of the board (N x N) and the number of queens.

    Returns:
        list: A list of solutions where each solution is a list representating
              the column positions of queens in each row.
    """
    def solve(row, board):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    solutions = []
    solve(0, [-1] * N)
    return solutions


def main():
    """
    The main function that parses the command-line arguments, validates them,
    and solves the N Queens problem.
    """
    if len(argv) != 2:
        print_usage_and_exit()

    try:
        N = int(argv[1])
    except ValueError:
        print_error_and_exit('N must be a number')

    if N < 4:
        print_error_and_exit('N must be at least 4')

    solutions = solve_nqueens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == '__main__':
    main()
