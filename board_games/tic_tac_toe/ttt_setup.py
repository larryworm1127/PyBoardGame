"""
Module that helps communication bewteen front-end and back-end

@date: 7/8/2018
@author: Larry Shi
"""

# general imports
from .ttt_board import *
from .ttt_computer import get_move


# setup class
class TTTSetUp:
    def __init__(self, size, human, reverse=False):
        # game board
        self._size = size
        self._reverse = reverse
        self._board = TTTBoard(self._size, self._reverse)

        # player setup
        self._human = PLAYERX if human == 'x' else PLAYERO
        self._computer = switch_player(self._human)


