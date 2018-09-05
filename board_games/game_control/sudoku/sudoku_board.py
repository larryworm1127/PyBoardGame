"""
Sudoku class that keep tracks of various game variables

@date: 7/17/2018
@author: Larry Shi
"""

# General imports
from typing import NoReturn, Union, Any

__all__ = ['Sudoku', 'CELL_IDX']

# Constants
CELL_IDX = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# Main class
class Sudoku:

    def __init__(self, dim, board=None) -> NoReturn:
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

    def __str__(self) -> str:
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

    def get_dim(self) -> int:
        """
        Return the dimension of the board
        """
        return self._dim

    def get_board(self) -> list:
        """
        Return the board as a 2-dimension list
        """
        return self._board

    def get_square(self, row, col) -> Any:
        """
        Get the contents of the board at position (row, col).

        :param row: the row on the board
        :param col: the column on the board
        :return: the state of the square
        """
        return self._board[row][col]

    def get_last_move(self) -> Union[tuple, None]:
        """
        Get the last move made by the user

        :return: the last ID in the moves list
        """
        if self._moves:
            return self._moves.pop()
        else:
            return None

    def set_square(self, row, col, num) -> NoReturn:
        """
        Place number on the board at position (row, col).

        :param row: the row of the board
        :param col: the column of the board
        :param num: the number that is filled into the square
        """
        self._board[row][col] = num

    def add_move(self, pos, num, pencil) -> NoReturn:
        """
        Add the ID of the square to moves list

        :param pos: the position of the square
        :param num: the number placed on the move
        :param pencil: bool that indicate whether pencil is toggled
        """
        self._moves.append((pos, num, pencil))

    def get_pos_from_num(self, num) -> list:
        """
        Get all number: num, positions (row, col) on the board

        :param num: the number that will be searched
        :return: a list of (row, col) positions
        """
        # initialize variable
        result = []

        # search for num
        for row in range(self._dim):
            for col in range(self._dim):
                if self._board[row][col] == num:
                    result.append((row, col))

        return result

    def get_row_col_cell(self) -> tuple:
        """
        Get all the rows, columns, and cells from board variable

        :return: rows, columns and cells of the board
        """
        # row
        rows = self._board.copy()

        # column
        cols = []
        for col in range(self._dim):
            column = []
            for row in range(self._dim):
                column.append(self._board[row][col])
            cols.append(column)

        # cell
        cells = []
        for idx1 in CELL_IDX:
            for idx2 in CELL_IDX:
                cell = []
                for row in idx1:
                    for col in idx2:
                        cell.append(self._board[row][col])

                cells.append(cell)

        # return row, column and cell in one 2D-list
        return rows, cols, cells

    def verify_board(self) -> Union[bool, set]:
        """
        Verify whether the board is complete

        :return: either the state of the board as a bool or a set of duplicated numbers
        """
        # store all rows, columns, and cells in one list
        row_col_cells = self.get_row_col_cell()
        lst = [config for item in row_col_cells for config in item]
        state = True

        # check whether the board is incomplete or not
        for row in self._board:
            if 0 in row:
                state = False

        # check for duplicate number
        duplicate_num = set([])
        for config in lst:
            for num in set(config):
                if config.count(num) > 1 and num != 0:
                    duplicate_num.add(num)

        if not duplicate_num:
            return state
        else:
            return duplicate_num
