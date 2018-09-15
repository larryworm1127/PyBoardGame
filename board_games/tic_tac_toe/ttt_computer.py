"""
Mini-max Tic-Tac-Toe Player

Imported from tic-tac-toe-python project with minor modifications

@date: 7/7/2018
@author: Larry Shi
"""

# General imports
from typing import Tuple

from .ttt_board import *

__all__ = ['get_move', 'mm_move', 'SCORES']

# Scoring values
SCORES = {PLAYERX: 1,
          DRAW: 0,
          PLAYERO: -1}


# Main functions
def get_move(board: TTTBoard, player: int) -> Tuple[int, Tuple[int, int]]:
    """
    Make a move on the board.

    :param board: the given board object
    :param player: the player that is making the move
    :return: a tuple with two elements. (row, col).
    """
    # return mm_move(board, player)
    return mm_move(board, player, -2, 2)


def mm_move(board: TTTBoard, player: int, alpha: int, beta: int) -> Tuple[int, Tuple[int, int]]:
    """
    A helper function for get_move that uses alpha beta pruning to find
    the best move

    :param board: the given board object
    :param player: the player that is making the move
    :param alpha: the alpha score for the algorithm
    :param beta: the beta score for the algorithm
    :return: the score and best move for the current state of the board
    """
    # initialize local variables
    other_player = switch_player(player)
    best_move = (-1, -1)
    best_score = -2

    # base case
    if board.check_win() is not None:
        return SCORES[board.check_win()], best_move

    # recursive cases
    for move in board.get_empty_squares():
        trial = board.clone()
        trial.move(move[0], move[1], player)
        score = mm_move(trial, other_player, -beta, -max(alpha, best_score))[0]
        alpha = score * SCORES[player]

        # pruning
        if alpha == 1:
            return score, move
        elif alpha > best_score:
            best_score = alpha
            best_move = move

        if best_score >= beta:
            break

    return best_score * SCORES[player], best_move
