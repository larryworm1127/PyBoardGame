"""
Mini-max Tic-Tac-Toe Player

@date: 7/7/2018
@author: Larry Shi
"""

# general imports
from . import ttt_board

# SCORING VALUES
SCORES = {ttt_board.PLAYERX: 1,
          ttt_board.DRAW: 0,
          ttt_board.PLAYERO: -1}


def get_move(board, player):
    """
    Make a move on the board.

    :param board: the given board object
    :param player: the player that is making the move
    :return: a tuple with two elements. (row, col).
    """
    return mm_move(board, player)


def mm_move(board, player):
    """
    A helper function for get_move that uses minimax algorithm to find the best move

    :param board: the given board object
    :param player: the player that is making the move
    """
    # initialize local variables
    score_dict = {-1: [], 0: [], -2: []}
    score_list = []
    other_player = ttt_board.switch_player(player)
    best_move = (-1, -1)
    best_score = -2

    # base case
    if board.check_win() is not None:
        return SCORES[board.check_win()], best_move

    # recursive case
    for move in board.get_empty_squares():
        trial = board.clone()
        trial.move(move[0], move[1], player)
        score = mm_move(trial, other_player)
        score_list.append(score[0])
        score_dict[score[0]] = move

    # calculate for the max score
    if player == ttt_board.PLAYERX:
        best_score = max(score_list)

    # calculate for the minimum score
    elif player == ttt_board.PLAYERO:
        best_score = min(score_list)

    # return the result
    best_move = score_dict[best_score]
    return best_score, best_move
