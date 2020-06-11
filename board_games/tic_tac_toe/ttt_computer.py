"""Mini-max Tic-Tac-Toe Player

=== Module description ===
Imported from tic-tac-toe-python project with minor modifications.
This module contains function that uses minimax algorithm to get the
best move for computer given a board instance

@date: 7/7/2018
@author: Larry Shi
"""
from typing import Tuple

from .ttt_board import *

__all__ = ['get_move', 'mm_move', 'SCORES']

# Scoring values
SCORES = {PLAYERX: 1,
          DRAW: 0,
          PLAYERO: -1}


# Main functions
def get_move(board: TTTBoard, player: int) -> Tuple[int, int]:
    """Make a move on the board.

    === Attributes ===
    board: the given board object
    player: the player that is making the move

    === Returns ===
    a tuple with two elements. (row, col).
    """
    # return mm_move(board, player)
    return mm_move(board, player, -2, 2)[1]


def mm_move(board: TTTBoard, player: int, alpha: int, beta: int) -> Tuple:
    """Uses alpha beta pruning to find the best move

    === Attributes ===
    board: the given board object
    player: the player that is making the move
    alpha: the alpha score for the algorithm
    beta: the beta score for the algorithm

    === Returns ===
    the score and best move for the current state of the board
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
