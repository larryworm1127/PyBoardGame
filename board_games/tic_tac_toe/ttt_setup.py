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
    def __init__(self, size, human, reverse=False, pvp=False):
        # game board
        self.size = size
        self.reverse = reverse
        self.pvp = pvp
        self.board = TTTBoard(self.reverse)

        # player setup
        self.human = PLAYERX if human == 'X' else PLAYERO
        self.computer = switch_player(self.human)

    def __str__(self):
        rep = ""
        rep += "size: " + str(self.size) + "\n"
        rep += "reverse: " + str(self.reverse) + "\n"
        rep += "pvp: " + str(self.pvp) + "\n"
        rep += "human: " + str(STRMAP[self.human]) + "\n"
        rep += "computer: " + str(STRMAP[self.computer]) + "\n"

        return rep

    def get_comp_move(self):
        return get_move(self.board, self.computer)[1]
