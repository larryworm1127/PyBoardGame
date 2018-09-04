"""
Virtual Tic-Tac-Toe Board

Imported from tic-tac-toe-python project with minor modifications

@date: 7/7/2018
@author: Larry Shi
"""

# general imports
from dataclasses import dataclass, field

# Constants
EMPTY = 0
PLAYERX = 1
PLAYERO = 2
DRAW = 3

# Map player constants to letters for printing
STRMAP = {PLAYERX: 'X',
          PLAYERO: 'O',
          EMPTY: ' '}


class TTTBoard:
    def __init__(self, reverse=False, board=None):
        """
        Initialize the TTTBoard object with the given dimension and
        whether or not the game should be reversed.
        """
        self._dim = 3
        self._reverse = reverse
        self._moves = []

        if board is None:
            # Create empty board
            self._board = [[EMPTY for _ in range(3)]
                           for _ in range(3)]
        else:
            # Copy board grid
            self._board = [[board[row][col] for col in range(3)]
                           for row in range(3)]

    def __str__(self):
        """
        Human readable representation of the board.
        """
        rep = ""
        for row in range(self._dim):
            for col in range(self._dim):
                rep += STRMAP[self._board[row][col]]
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

    def get_square(self, row, col):
        """
        Get one of the three constants EMPTY, PLAYERX, or PLAYERO
        that correspond to the contents of the board at position (row, col).

        :param row: the row on the board
        :param col: the column on the board
        :return: the state of the square
        """
        return self._board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        empty = []
        for row in range(self._dim):
            for col in range(self._dim):
                if self._board[row][col] == EMPTY:
                    empty.append((row, col))

        return empty

    def get_moves(self):
        """
        Returns a list of (row, col) moves made my computer and player
        """
        return self._moves

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.

        :param row: the row of the board
        :param col: the column of the board
        :param player: the player that is making the move
        """
        if self._board[row][col] == EMPTY:
            self._board[row][col] = player
            self._moves.append((row, col))

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.

        :return: the state of the game
        """
        board = self._board
        dim = self._dim
        lines = []

        # rows
        lines.extend(board)

        # columns
        cols = [[board[row][col] for row in range(dim)]
                for col in range(dim)]
        lines.extend(cols)

        # diagonals
        diag1 = [board[idx][idx] for idx in range(dim)]
        diag2 = [board[idx][dim - idx - 1]
                 for idx in range(dim)]
        lines.append(diag1)
        lines.append(diag2)

        # check all lines
        for line in lines:
            if len(set(line)) == 1 and line[0] != EMPTY:
                if self._reverse:
                    return switch_player(line[0])
                else:
                    return line[0]

        # no winner, check for draw
        if len(self.get_empty_squares()) == 0:
            return DRAW

        # game is still in progress
        return None

    def clone(self):
        """
        Return a copy of the board
        """
        return TTTBoard(self._reverse, self._board)


# setup class
@dataclass
class TTTSetUp:
    size: int
    human: int
    computer: int

    reverse: bool = False
    pvp: bool = False
    board: TTTBoard = field(init=False)

    def __post_init__(self):
        """
        Initialize any variables that requires other var to be initialized
        """
        self.board = TTTBoard(self.reverse)

    def get_comp_move(self):
        from .ttt_computer import get_move

        return get_move(self.board, self.computer)[1]


# util function
def switch_player(player):
    """
    Convenience function to switch players.

    :param player: the player that wishes to be switched
    :return: other player.
    """
    if player == PLAYERX:
        return PLAYERO
    else:
        return PLAYERX
