#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[k, z], [k, z], [k, z], [k, z]]
where `k` and `z` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for k in range(len(board)):
        for z in range(len(board)):
            if board[k][z] == "Q":
                solution.append([k, z])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for z in range(col + 1, len(board)):
        board[row][z] = "x"
    # X out all backwards spots
    for z in range(col - 1, -1, -1):
        board[row][z] = "x"
    # X out all spots below
    for k in range(row + 1, len(board)):
        board[k][col] = "x"
    # X out all spots above
    for k in range(row - 1, -1, -1):
        board[k][col] = "x"
    # X out all spots diagonally down to the right
    z = col + 1
    for k in range(row + 1, len(board)):
        if z >= len(board):
            break
        board[k][z] = "x"
        z += 1
    # X out all spots diagonally up to the left
    z = col - 1
    for k in range(row - 1, -1, -1):
        if z < 0:
            break
        board[k][z]
        z -= 1
    # X out all spots diagonally up to the right
    z = col + 1
    for k in range(row - 1, -1, -1):
        if z >= len(board):
            break
        board[k][z] = "x"
        z += 1
    # X out all spots diagonally down to the left
    z = col - 1
    for k in range(row + 1, len(board)):
        if z < 0:
            break
        board[k][z] = "x"
        z -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for z in range(len(board)):
        if board[row][z] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][z] = "Q"
            xout(tmp_board, row, z)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
