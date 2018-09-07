"""
Test module for puzzle_parser.py
"""

# General imports
import pytest

from collections import namedtuple
from os.path import join

from ..sudoku.puzzle_parser import *

# Global variable
data_tuple = namedtuple('Test', ['name', 'data', 'fixed_data', 'puzzle_tuple'])
expected_tuple = namedtuple('Expected', ['fixed_data', 'readable_data', 'rating'])


# Fixtures
@pytest.fixture
def easy_data() -> data_tuple:
    """ Returns a namedtuple containing all the Easy data needed for tests """
    # read file and create puzzle object
    with open(join(DATA_DIR, 'easy')) as file:
        lines = file.readlines()

    puzzle_object = Puzzles('easy')

    # create data tuple
    data = data_tuple('Easy', lines, clean_up_data(lines[0])[0], puzzle_object.get_puzzle_tuple())

    yield data


@pytest.fixture
def easy_expected() -> expected_tuple:
    """ Returns a namedtuple containing all the expected results """
    # create expected value variables
    fixed_data = [0, 1, 0, 0, 4, 0, 5, 6, 0, 2, 3, 0, 6, 1, 5, 0, 8, 0, 0, 0, 0, 8, 0, 0, 1, 0, 0, 0, 5, 0, 0, 2, 0, 0,
                  0, 8, 6, 0, 0, 7, 8, 1, 0, 0, 5, 9, 0, 0, 0, 6, 0, 0, 2, 0, 0, 0, 6, 0, 0, 8, 0, 0, 0, 0, 8, 0, 4, 7,
                  3, 0, 5, 6, 0, 4, 5, 0, 9, 0, 0, 1, 0]

    readable_data = [[0, 1, 0, 0, 4, 0, 5, 6, 0], [2, 3, 0, 6, 1, 5, 0, 8, 0], [0, 0, 0, 8, 0, 0, 1, 0, 0],
                     [0, 5, 0, 0, 2, 0, 0, 0, 8], [6, 0, 0, 7, 8, 1, 0, 0, 5], [9, 0, 0, 0, 6, 0, 0, 2, 0],
                     [0, 0, 6, 0, 0, 8, 0, 0, 0], [0, 8, 0, 4, 7, 3, 0, 5, 6], [0, 4, 5, 0, 9, 0, 0, 1, 0]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.300724637681)

    yield expected


@pytest.fixture
def medium_data() -> data_tuple:
    """ Returns a namedtuple containing all the Medium data needed for tests """
    # read file and create puzzle object
    with open(join(DATA_DIR, 'medium')) as file:
        lines = file.readlines()

    puzzle_object = Puzzles('medium')

    # create data tuple
    data = data_tuple('Medium', lines, clean_up_data(lines[0])[0], puzzle_object.get_puzzle_tuple())

    yield data


@pytest.fixture
def medium_expected() -> expected_tuple:
    """ Returns a namedtuple containing all the expected results """
    # create expected value variables
    fixed_data = [0, 0, 0, 8, 1, 5, 2, 3, 0, 0, 0, 0, 9, 0, 0, 0, 0, 8, 0, 0, 2, 4, 6, 0, 5, 1, 0, 3, 0, 6, 0, 0, 0, 1,
                  0, 0, 0, 5, 0, 1, 0, 6, 0, 2, 0, 0, 0, 4, 0, 0, 0, 6, 0, 3, 0, 9, 5, 0, 4, 1, 8, 0, 0, 6, 0, 0, 0, 0,
                  9, 0, 0, 0, 0, 8, 3, 6, 5, 2, 0, 0, 0]

    readable_data = [[0, 0, 0, 8, 1, 5, 2, 3, 0], [0, 0, 0, 9, 0, 0, 0, 0, 8], [0, 0, 2, 4, 6, 0, 5, 1, 0],
                     [3, 0, 6, 0, 0, 0, 1, 0, 0], [0, 5, 0, 1, 0, 6, 0, 2, 0], [0, 0, 4, 0, 0, 0, 6, 0, 3],
                     [0, 9, 5, 0, 4, 1, 8, 0, 0], [6, 0, 0, 0, 0, 9, 0, 0, 0], [0, 8, 3, 6, 5, 2, 0, 0, 0]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.55)

    yield expected


@pytest.fixture
def hard_data() -> data_tuple:
    """ Returns a namedtuple containing all the Hard data needed for tests """
    # read file and create puzzle object
    with open(join(DATA_DIR, 'hard')) as file:
        lines = file.readlines()

    puzzle_object = Puzzles('hard')

    # create data tuple
    data = data_tuple('Hard', lines, clean_up_data(lines[0])[0], puzzle_object.get_puzzle_tuple())

    yield data


@pytest.fixture
def hard_expected() -> expected_tuple:
    """ Returns a namedtuple containing all the expected results """
    # create expected value variables
    fixed_data = [3, 5, 0, 0, 0, 9, 4, 0, 0, 0, 9, 0, 4, 0, 0, 0, 0, 3, 0, 4, 0, 8, 6, 0, 0, 9, 0, 4, 7, 0, 0, 1, 0, 9,
                  0, 0, 0, 3, 0, 6, 0, 4, 0, 2, 0, 0, 0, 2, 0, 3, 0, 0, 7, 4, 0, 6, 0, 0, 8, 2, 0, 4, 0, 7, 0, 0, 0, 0,
                  1, 0, 5, 0, 0, 0, 4, 7, 0, 0, 0, 8, 1]

    readable_data = [[3, 5, 0, 0, 0, 9, 4, 0, 0], [0, 9, 0, 4, 0, 0, 0, 0, 3], [0, 4, 0, 8, 6, 0, 0, 9, 0],
                     [4, 7, 0, 0, 1, 0, 9, 0, 0], [0, 3, 0, 6, 0, 4, 0, 2, 0], [0, 0, 2, 0, 3, 0, 0, 7, 4],
                     [0, 6, 0, 0, 8, 2, 0, 4, 0], [7, 0, 0, 0, 0, 1, 0, 5, 0], [0, 0, 4, 7, 0, 0, 0, 8, 1]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.608865248227)

    yield expected


@pytest.fixture
def very_hard_data() -> data_tuple:
    """ Returns a namedtuple containing all the Easy data needed for tests """
    # read file and create puzzle object
    with open(join(DATA_DIR, 'very_hard')) as file:
        lines = file.readlines()

    puzzle_object = Puzzles('very_hard')

    # create data tuple
    data = data_tuple('Very_hard', lines, clean_up_data(lines[0])[0], puzzle_object.get_puzzle_tuple())

    yield data


@pytest.fixture
def very_hard_expected() -> expected_tuple:
    """ Returns a namedtuple containing all the expected results """
    # create expected value variables
    fixed_data = [0, 0, 4, 1, 0, 0, 3, 0, 0, 0, 7, 0, 0, 0, 8, 0, 0, 1, 0, 0, 0, 0, 0, 0, 7, 0, 9, 8, 0, 3, 0, 5, 9, 0,
                  0, 2, 0, 0, 9, 6, 0, 1, 5, 0, 0, 1, 0, 0, 8, 2, 0, 9, 0, 4, 6, 0, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0,
                  0, 0, 9, 0, 0, 0, 8, 0, 0, 4, 2, 0, 0]

    readable_data = [[0, 0, 4, 1, 0, 0, 3, 0, 0], [0, 7, 0, 0, 0, 8, 0, 0, 1], [0, 0, 0, 0, 0, 0, 7, 0, 9],
                     [8, 0, 3, 0, 5, 9, 0, 0, 2], [0, 0, 9, 6, 0, 1, 5, 0, 0], [1, 0, 0, 8, 2, 0, 9, 0, 4],
                     [6, 0, 1, 0, 0, 0, 0, 0, 0], [4, 0, 0, 3, 0, 0, 0, 9, 0], [0, 0, 8, 0, 0, 4, 2, 0, 0]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.954248366013)

    yield expected


# Tests
def test_clean_up_data(easy_data, easy_expected, medium_data, medium_expected, hard_data, hard_expected, very_hard_data,
                       very_hard_expected):
    """ Test function for clean_up_data function """
    # easy data test
    assert easy_expected.fixed_data == clean_up_data(easy_data.data[0])[0]

    # medium data test
    assert medium_expected.fixed_data == clean_up_data(medium_data.data[0])[0]

    # hard data test
    assert hard_expected.fixed_data == clean_up_data(hard_data.data[0])[0]

    # very hard data test
    assert very_hard_expected.fixed_data == clean_up_data(very_hard_data.data[0])[0]


def test_create_readable_data(easy_data, easy_expected, medium_data, medium_expected, hard_data, hard_expected,
                              very_hard_data, very_hard_expected):
    """ Test function for create_readable_data function """
    # easy data teset
    assert easy_expected.readable_data == create_readable_data(easy_data.fixed_data)

    # medium data test
    assert medium_expected.readable_data == create_readable_data(medium_data.fixed_data)

    # hard data test
    assert hard_expected.readable_data == create_readable_data(hard_data.fixed_data)

    # very hard data test
    assert very_hard_expected.readable_data == create_readable_data(very_hard_data.fixed_data)


def test_create_list_data(easy_data, easy_expected, medium_data, medium_expected, hard_data, hard_expected,
                          very_hard_data, very_hard_expected):
    """ Test function for create_list_data function """
    # easy data test
    expected = easy_data.puzzle_tuple(easy_expected.rating, easy_expected.readable_data)
    assert expected in create_list_data(easy_data.data, easy_data.puzzle_tuple)

    # medium data test
    expected = medium_data.puzzle_tuple(medium_expected.rating, medium_expected.readable_data)
    assert expected in create_list_data(medium_data.data, medium_data.puzzle_tuple)

    # hard data test
    expected = hard_data.puzzle_tuple(hard_expected.rating, hard_expected.readable_data)
    assert expected in create_list_data(hard_data.data, hard_data.puzzle_tuple)

    # very hard data test
    expected = very_hard_data.puzzle_tuple(very_hard_expected.rating, very_hard_expected.readable_data)
    assert expected in create_list_data(very_hard_data.data, very_hard_data.puzzle_tuple)
