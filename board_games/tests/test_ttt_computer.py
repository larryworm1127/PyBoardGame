"""
Test module for ttt_computer.py

@date: 7/7/2018
@author: Larry Shi
"""
from ..tic_tac_toe.ttt_board import PLAYERX, PLAYERO, EMPTY, TTTBoard
from ..tic_tac_toe.ttt_computer import *


# test classes
def test_minimax_win_row():
    """
    x x o | o x x | o o
      x x |   o o | x x o
    o   o | x   x | x

    Test if COMPUTER can win game with win case on a row of the board.
    """
    game_board = [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX],
                  [PLAYERO, EMPTY, PLAYERO]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 1), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERX, PLAYERX], [EMPTY, PLAYERO, PLAYERO],
                  [PLAYERX, EMPTY, PLAYERX]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (1, 0), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERO, EMPTY], [PLAYERX, PLAYERX, PLAYERO],
                  [PLAYERX, EMPTY, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (0, 2), "Bad Move: " + str(move)


def test_minimax_win_col():
    """
    x     | x   o | o o x
    o o x |     x |   o x
    x o x | x o o | x

    Test if COMPUTER can win game with win case on a column of the board.
    """
    game_board = [[PLAYERX, EMPTY, EMPTY], [PLAYERO, PLAYERO, PLAYERX],
                  [PLAYERX, PLAYERO, PLAYERX]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERX)
    assert move == (0, 2), "Bad Move: " + str(move)

    game_board = [[PLAYERX, EMPTY, PLAYERO], [EMPTY, EMPTY, PLAYERX],
                  [PLAYERX, PLAYERO, PLAYERO]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERX)
    assert move == (1, 0), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERO, PLAYERX], [EMPTY, PLAYERO, PLAYERX],
                  [PLAYERX, EMPTY, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERX)
    assert move == (2, 2), "Bad Move: " + str(move)


def test_minimax_win_diag():
    """
    x x   | o x x | x     |
    o o x | x o   |   x o |   x o
    o     | o     |   o   |   o x

    Test if COMPUTER can win game with win case on a diagonal of the board.
    """
    game_board = [[PLAYERX, PLAYERX, EMPTY], [PLAYERO, PLAYERO, PLAYERX],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (0, 2), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERX, PLAYERX], [PLAYERX, PLAYERO, EMPTY],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 2), "Bad Move: " + str(move)

    game_board = [[PLAYERX, EMPTY, EMPTY], [EMPTY, PLAYERX, PLAYERO],
                  [EMPTY, PLAYERO, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERX)
    assert move == (2, 2) or move == (0, 1), "Bad Move: " + str(move)

    game_board = [[EMPTY, EMPTY, EMPTY], [EMPTY, PLAYERX, PLAYERO],
                  [EMPTY, PLAYERO, PLAYERX]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERX)
    assert move == (0, 0), "Bad Move: " + str(move)


def test_minimax_def_row():
    """
    x x   | o x   | x o
    x o   | x x   | o
    o o x | o o x | x x

    Test if COMPUTER can defend with a lose case on a row of the board.
    """
    game_board = [[PLAYERX, PLAYERX, EMPTY], [PLAYERX, PLAYERO, EMPTY],
                  [PLAYERO, PLAYERO, PLAYERX]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (0, 2), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERX, EMPTY], [PLAYERX, PLAYERX, EMPTY],
                  [PLAYERO, PLAYERO, PLAYERX]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (1, 2), "Bad Move: " + str(move)

    game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERO, EMPTY, EMPTY],
                  [PLAYERX, PLAYERX, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 2), "Bad Move: " + str(move)


def test_minimax_def_col():
    """
    x o x | o x o | o o x
    x x o | x x o | x o x
        o |     x |   x

    Test if COMPUTER can defend with a lose case on a column of the board.
    """
    game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERX, PLAYERX, PLAYERO],
                  [EMPTY, EMPTY, PLAYERO]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 0), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERX, PLAYERO], [PLAYERX, PLAYERX, PLAYERO],
                  [EMPTY, EMPTY, PLAYERX]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 1), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERO, PLAYERX], [PLAYERX, PLAYERO, PLAYERX],
                  [EMPTY, PLAYERX, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 2), "Bad Move: " + str(move)


def test_minimax_def_diag():
    """
    x o x | o o x
    x x o | x x o
    o     |     x

    Test if COMPUTER can defend with lose case on a diagonal of the board.
    """
    game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERX, PLAYERX, PLAYERO],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 2), "Bad Move: " + str(move)

    game_board = [[PLAYERO, PLAYERO, PLAYERX], [PLAYERX, PLAYERX, PLAYERO],
                  [EMPTY, EMPTY, PLAYERX]]
    board = TTTBoard(board=game_board)
    move = get_move(board, PLAYERO)
    assert move == (2, 0), "Bad Move: " + str(move)


if __name__ == '__main__':
    import pytest

    pytest.main(["test_ttt_computer.py"])
