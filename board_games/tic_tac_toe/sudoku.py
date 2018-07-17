"""
Sudoku class that keep tracks of various game variables

@date: 7/17/2018
@author: Larry Shi
"""

# general imports
from .ttt_board import id_ref


class Sudoku:

    def __init__(self, dim, board=None):
        """
        Initialize the Sudoku object.
        """
        self._dim = dim
        self._moves = []

        if board is None:
            # Create empty board
            self._board = [[0 for _ in range(dim)]
                           for _ in range(dim)]
        else:
            # Copy board grid
            self._board = [[board[row][col] for col in range(dim)]
                           for row in range(dim)]

    def __str__(self):
        """
        Human readable representation of the board.
        """
        rep = ""
        for row in range(self._dim):
            for col in range(self._dim):
                rep += str(self._board[row][col])
                if col == self._dim - 1:
                    rep += "\n"
                else:
                    rep += " | "
            if row != self._dim - 1:
                rep += "-" * (4 * self._dim - 3)
                rep += "\n"
        return rep

    def get_dim(self):
        """
        Return the dimension of the board
        """
        return self._dim

    def get_board(self):
        """
        Return the board as a 2-dimension list
        """
        return self._board

    def get_square(self, row, col):
        """
        Get the contents of the board at position (row, col).

        :param row: the row on the board
        :param col: the column on the board
        :return: the state of the square
        """
        return self._board[row][col]

    def get_last_move(self):
        """
        Get the last move made by the user

        :return: the last ID in the moves list
        """
        if self._moves:
            return self._moves.pop()
        else:
            return None

    def set_square(self, row, col, num):
        """
        Place number on the board at position (row, col).
        .

        :param row: the row of the board
        :param col: the column of the board
        :param num: the number that is filled into the square
        """
        self._board[row][col] = num

    def add_move(self, cell_id):
        """
        Add the ID of the square to moves list

        :param cell_id: the ID of the square
        """
        self._moves.append(cell_id)
