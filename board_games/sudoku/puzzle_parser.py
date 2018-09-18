"""Puzzle Parser for Sudoku Puzzle

=== Module description ===
Imported from Pydoku project with slight modification.
Python module to parse existing file containing various difficulties
of Sudoku puzzles.

@date: 8/18/2018
@author: Larry Shi
"""

# General imports
from collections import namedtuple
from dataclasses import dataclass, field
from os.path import join
from typing import List, Tuple, Union

from board_games import PROJECT_DIR

__all__ = ['Puzzles', 'create_list_data', 'create_readable_data',
           'clean_up_data', 'DATA_DIR', 'LINE_NUM']

# Constants
DATA_DIR = join(PROJECT_DIR, 'assets', 'data')
LINE_NUM = 150


# Puzzle class
@dataclass
class Puzzles:
    """Class handling all the Sudoku puzzle

    === Attributes ===
    difficulty: the difficulty of the puzzle
    puzzle_tuple: a namedtuple used for storing puzzles used by other functions
    data: the original data read from file
    list_data: the parsed puzzle data
    """

    _difficulty: str
    _puzzle_tuple: namedtuple = namedtuple('Puzzles', ['rating', 'puzzle'])
    _data: list = field(init=False)
    _list_data: list = field(init=False)

    def __post_init__(self) -> None:
        """Initialize variables in post init"""
        # read data file
        with open(join(DATA_DIR, self._difficulty)) as file:
            self._data = file.readlines()

        self._list_data = create_list_data(self._data, self._puzzle_tuple)

    def get_list_data(self) -> List:
        """Returns the listed sudoku puzzle data"""
        return self._list_data

    def get_puzzle_tuple(self) -> namedtuple:
        """Returns the namedtuple for storing puzzle data"""
        return self._puzzle_tuple


# Helper functions
def create_list_data(data: List[str], puzzle_tuple: namedtuple) -> List:
    """Create listed sudoku puzzle data given the file data

    === Attributes ===
    data: the original data
    puzzle_tuple: named tuple used to store the data and its rating

    === Returns ===
    the created listed data
    """
    # create variables
    result = []
    length = len(data)

    # loop through every line in the data file and extract the rating and puzzle
    for index in range(length):
        puzzle, rating = clean_up_data(data[index])

        # add namedtuple into result list containing the rating and the puzzle
        fixed_data = create_readable_data(puzzle)
        result.append(puzzle_tuple(rating, fixed_data))

    # sort the result from easiest to hardest
    result.sort()

    return result


def clean_up_data(data: str) -> Tuple[List[int], Union[int, float]]:
    """Remove all the extra non-data related characters in the data

    === Attribute ===
    data: the original data

    === Returns ===
    the cleaned up data
    """
    puzzle = []
    rating = 1
    line = data.split(' ')

    # loop through every single item in the line
    for item in line:
        # extract rating
        if '\t' in item or '\n' in item:
            puzzle.append(int(item[0]))
            item = item[1:]
            rating = float(item.strip())

        # extract puzzle
        else:
            puzzle.append(int(item))

    return puzzle, rating


def create_readable_data(data: List[int]) -> List[list]:
    """Create a program readable sudoku puzzle given a list of numbers

    === Attributes ===
    data: a list of numbers containing sudoku puzzle

    === Returns ===
    a readable sudoku puzzle
    """
    # create result variables
    result = [[] for _ in range(9)]

    # loop through all number in data to create readable data
    index = 0
    for row in range(9):
        for _ in range(9):
            result[row].append(data[index])
            index += 1

    return result
