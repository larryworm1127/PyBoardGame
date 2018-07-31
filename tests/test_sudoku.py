"""
Test module for sudoku.py

@date: 7/27/2018
@author: Larry Shi
"""
# general imports
from board_games.tic_tac_toe.sudoku import *

# constants
SOLVED_BOARD = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

INVALID_BOARD = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [8, 2, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

INCOMPLETE_BOARD = [
    [8, 1, 0, 0, 2, 9, 0, 0, 0],
    [4, 0, 6, 0, 7, 3, 0, 5, 1],
    [0, 7, 0, 0, 0, 0, 8, 0, 2],
    [0, 0, 4, 5, 0, 0, 0, 0, 6],
    [7, 6, 0, 0, 0, 0, 0, 1, 3],
    [1, 0, 0, 0, 0, 6, 2, 0, 0],
    [2, 0, 7, 0, 0, 0, 0, 8, 0],
    [6, 9, 0, 2, 8, 0, 3, 0, 5],
    [0, 0, 0, 9, 6, 0, 0, 2, 4]
]


# test classes
class TestSudoku:
    def test_get_row_col_cell(self):
        """
        Test if get_row_col_cell method get the correct
        rows, columns and cells given a board
        """
        cols = [
            [5, 6, 1, 8, 4, 7, 9, 2, 3],
            [3, 7, 9, 5, 2, 1, 6, 8, 4],
            [4, 2, 8, 9, 6, 3, 1, 7, 5],
            [6, 1, 3, 7, 8, 9, 5, 4, 2],
            [7, 9, 4, 6, 5, 2, 3, 1, 8],
            [8, 5, 2, 1, 3, 4, 7, 9, 6],
            [9, 3, 5, 4, 7, 8, 2, 6, 1],
            [1, 4, 6, 2, 9, 5, 8, 3, 7],
            [2, 8, 7, 3, 1, 6, 4, 5, 9]
        ]

        cells = [
            [5, 3, 4, 6, 7, 2, 1, 9, 8],
            [8, 5, 9, 4, 2, 6, 7, 1, 3],
            [9, 6, 1, 2, 8, 7, 3, 4, 5],
            [6, 7, 8, 1, 9, 5, 3, 4, 2],
            [7, 6, 1, 8, 5, 3, 9, 2, 4],
            [5, 3, 7, 4, 1, 9, 2, 8, 6],
            [9, 1, 2, 3, 4, 8, 5, 6, 7],
            [4, 2, 3, 7, 9, 1, 8, 5, 6],
            [2, 8, 4, 6, 3, 5, 1, 7, 9]
        ]

        game_board = Sudoku(9, SOLVED_BOARD)
        lst = game_board.get_row_col_cell()

        for row in lst[0]:
            assert row in SOLVED_BOARD, "row not in board"

        for col in lst[1]:
            assert col in cols, "column not in board"

        for cell in lst[2]:
            assert cell in cells, "cell not in board"

    def test_verify_board(self):
        """
        Test if verify_board function recognizes a complete,
        incomplete, and incorrect board
        """
        game_board = Sudoku(9, SOLVED_BOARD)
        result = game_board.verify_board()
        assert result is True, "board solved but not recognized"

        game_board = Sudoku(9, INVALID_BOARD)
        result = game_board.verify_board()
        assert result == [8, 2], "board incorrect but not recognized"

        game_board = Sudoku(9, INCOMPLETE_BOARD)
        result = game_board.verify_board()
        assert not result, "board incomplete but not recognized"
