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
expected_tuple = namedtuple('Expected', ['fixed_data', 'clean_data', 'rating'])


# Fixtures
@pytest.fixture
def ez_data() -> data_tuple:
    """Returns a namedtuple containing all the Easy data needed for tests"""
    # read file and create puzzle object
    with open(join(DATA_DIR, 'easy')) as file:
        lines = file.readlines()

    instance = Puzzles('easy')

    # create data tuple
    fixed_data = clean_up_data(lines[0])[0]
    puzzle_tuple = instance.get_puzzle_tuple()
    data = data_tuple('Easy', lines, fixed_data, puzzle_tuple)

    yield data


@pytest.fixture
def ez_expect() -> expected_tuple:
    """Returns a namedtuple containing all the expected results"""
    # create expected value variables
    fixed_data = [0, 1, 0, 0, 4, 0, 5, 6, 0, 2, 3, 0, 6, 1, 5, 0, 8, 0, 0, 0, 0,
                  8, 0, 0, 1, 0, 0, 0, 5, 0, 0, 2, 0, 0, 0, 8, 6, 0, 0, 7, 8, 1,
                  0, 0, 5, 9, 0, 0, 0, 6, 0, 0, 2, 0, 0, 0, 6, 0, 0, 8, 0, 0, 0,
                  0, 8, 0, 4, 7, 3, 0, 5, 6, 0, 4, 5, 0, 9, 0, 0, 1, 0]

    readable_data = [[0, 1, 0, 0, 4, 0, 5, 6, 0], [2, 3, 0, 6, 1, 5, 0, 8, 0],
                     [0, 0, 0, 8, 0, 0, 1, 0, 0], [0, 5, 0, 0, 2, 0, 0, 0, 8],
                     [6, 0, 0, 7, 8, 1, 0, 0, 5], [9, 0, 0, 0, 6, 0, 0, 2, 0],
                     [0, 0, 6, 0, 0, 8, 0, 0, 0], [0, 8, 0, 4, 7, 3, 0, 5, 6],
                     [0, 4, 5, 0, 9, 0, 0, 1, 0]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.300724637681)

    yield expected


@pytest.fixture
def med_data() -> data_tuple:
    """Returns a namedtuple containing all the Medium data needed for tests"""
    # read file and create puzzle object
    with open(join(DATA_DIR, 'medium')) as file:
        lines = file.readlines()

    instance = Puzzles('medium')

    # create data tuple
    fixed_data = clean_up_data(lines[0])[0]
    puzzle_tuple = instance.get_puzzle_tuple()
    data = data_tuple('Medium', lines, fixed_data, puzzle_tuple)

    yield data


@pytest.fixture
def med_expect() -> expected_tuple:
    """Returns a namedtuple containing all the expected results"""
    # create expected value variables
    fixed_data = [0, 0, 0, 8, 1, 5, 2, 3, 0, 0, 0, 0, 9, 0, 0, 0, 0, 8, 0, 0, 2,
                  4, 6, 0, 5, 1, 0, 3, 0, 6, 0, 0, 0, 1, 0, 0, 0, 5, 0, 1, 0, 6,
                  0, 2, 0, 0, 0, 4, 0, 0, 0, 6, 0, 3, 0, 9, 5, 0, 4, 1, 8, 0, 0,
                  6, 0, 0, 0, 0, 9, 0, 0, 0, 0, 8, 3, 6, 5, 2, 0, 0, 0]

    readable_data = [[0, 0, 0, 8, 1, 5, 2, 3, 0], [0, 0, 0, 9, 0, 0, 0, 0, 8],
                     [0, 0, 2, 4, 6, 0, 5, 1, 0], [3, 0, 6, 0, 0, 0, 1, 0, 0],
                     [0, 5, 0, 1, 0, 6, 0, 2, 0], [0, 0, 4, 0, 0, 0, 6, 0, 3],
                     [0, 9, 5, 0, 4, 1, 8, 0, 0], [6, 0, 0, 0, 0, 9, 0, 0, 0],
                     [0, 8, 3, 6, 5, 2, 0, 0, 0]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.55)

    yield expected


@pytest.fixture
def hard_data() -> data_tuple:
    """Returns a namedtuple containing all the Hard data needed for tests"""
    # read file and create puzzle object
    with open(join(DATA_DIR, 'hard')) as file:
        lines = file.readlines()

    instance = Puzzles('hard')

    # create data tuple
    fixed_data = clean_up_data(lines[0])[0]
    puzzle_tuple = instance.get_puzzle_tuple()
    data = data_tuple('Hard', lines, fixed_data, puzzle_tuple)

    yield data


@pytest.fixture
def hard_expect() -> expected_tuple:
    """Returns a namedtuple containing all the expected results"""
    # create expected value variables
    fixed_data = [3, 5, 0, 0, 0, 9, 4, 0, 0, 0, 9, 0, 4, 0, 0, 0, 0, 3, 0, 4, 0,
                  8, 6, 0, 0, 9, 0, 4, 7, 0, 0, 1, 0, 9, 0, 0, 0, 3, 0, 6, 0, 4,
                  0, 2, 0, 0, 0, 2, 0, 3, 0, 0, 7, 4, 0, 6, 0, 0, 8, 2, 0, 4, 0,
                  7, 0, 0, 0, 0, 1, 0, 5, 0, 0, 0, 4, 7, 0, 0, 0, 8, 1]

    readable_data = [[3, 5, 0, 0, 0, 9, 4, 0, 0], [0, 9, 0, 4, 0, 0, 0, 0, 3],
                     [0, 4, 0, 8, 6, 0, 0, 9, 0], [4, 7, 0, 0, 1, 0, 9, 0, 0],
                     [0, 3, 0, 6, 0, 4, 0, 2, 0], [0, 0, 2, 0, 3, 0, 0, 7, 4],
                     [0, 6, 0, 0, 8, 2, 0, 4, 0], [7, 0, 0, 0, 0, 1, 0, 5, 0],
                     [0, 0, 4, 7, 0, 0, 0, 8, 1]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.608865248227)

    yield expected


@pytest.fixture
def vhard_data() -> data_tuple:
    """Returns a namedtuple containing all the Easy data needed for tests"""
    # read file and create puzzle object
    with open(join(DATA_DIR, 'very_hard')) as file:
        lines = file.readlines()

    instance = Puzzles('very_hard')

    # create data tuple
    fixed_data = clean_up_data(lines[0])[0]
    puzzle_tuple = instance.get_puzzle_tuple()
    data = data_tuple('Very_hard', lines, fixed_data, puzzle_tuple)

    yield data


@pytest.fixture
def vhard_expect() -> expected_tuple:
    """ Returns a namedtuple containing all the expected results """
    # create expected value variables
    fixed_data = [0, 0, 4, 1, 0, 0, 3, 0, 0, 0, 7, 0, 0, 0, 8, 0, 0, 1, 0, 0, 0,
                  0, 0, 0, 7, 0, 9, 8, 0, 3, 0, 5, 9, 0, 0, 2, 0, 0, 9, 6, 0, 1,
                  5, 0, 0, 1, 0, 0, 8, 2, 0, 9, 0, 4, 6, 0, 1, 0, 0, 0, 0, 0, 0,
                  4, 0, 0, 3, 0, 0, 0, 9, 0, 0, 0, 8, 0, 0, 4, 2, 0, 0]

    readable_data = [[0, 0, 4, 1, 0, 0, 3, 0, 0], [0, 7, 0, 0, 0, 8, 0, 0, 1],
                     [0, 0, 0, 0, 0, 0, 7, 0, 9], [8, 0, 3, 0, 5, 9, 0, 0, 2],
                     [0, 0, 9, 6, 0, 1, 5, 0, 0], [1, 0, 0, 8, 2, 0, 9, 0, 4],
                     [6, 0, 1, 0, 0, 0, 0, 0, 0], [4, 0, 0, 3, 0, 0, 0, 9, 0],
                     [0, 0, 8, 0, 0, 4, 2, 0, 0]]

    # create expected tuple
    expected = expected_tuple(fixed_data, readable_data, 0.954248366013)

    yield expected


# Tests
def test_clean_up_data(ez_data, ez_expect, med_data, med_expect,
                       hard_data, hard_expect, vhard_data, vhard_expect):
    """ Test function for clean_up_data function """
    # easy data test
    assert ez_expect.fixed_data == clean_up_data(ez_data.data[0])[0]

    # medium data test
    assert med_expect.fixed_data == clean_up_data(med_data.data[0])[0]

    # hard data test
    assert hard_expect.fixed_data == clean_up_data(hard_data.data[0])[0]

    # very hard data test
    assert vhard_expect.fixed_data == clean_up_data(vhard_data.data[0])[0]


def test_create_readable_data(ez_data, ez_expect, med_data, med_expect,
                              hard_data, hard_expect, vhard_data, vhard_expect):
    """ Test function for create_readable_data function """
    # easy data teset
    assert ez_expect.clean_data == create_readable_data(ez_data.fixed_data)

    # medium data test
    assert med_expect.clean_data == create_readable_data(med_data.fixed_data)

    # hard data test
    assert hard_expect.clean_data == create_readable_data(hard_data.fixed_data)

    # very hard data test
    assert vhard_expect.clean_data == create_readable_data(vhard_data.fixed_data)


def test_create_list_data(ez_data, ez_expect, med_data, med_expect, hard_data,
                          hard_expect, vhard_data, vhard_expect):
    """ Test function for create_list_data function """
    # easy data test
    expect = ez_data.puzzle_tuple(ez_expect.rating, ez_expect.clean_data)
    assert expect in create_list_data(ez_data.data, ez_data.puzzle_tuple)

    # medium data test
    expect = med_data.puzzle_tuple(med_expect.rating, med_expect.clean_data)
    assert expect in create_list_data(med_data.data, med_data.puzzle_tuple)

    # hard data test
    expect = hard_data.puzzle_tuple(hard_expect.rating, hard_expect.clean_data)
    assert expect in create_list_data(hard_data.data, hard_data.puzzle_tuple)

    # very hard data test
    expect = vhard_data.puzzle_tuple(vhard_expect.rating, vhard_expect.clean_data)
    assert expect in create_list_data(vhard_data.data, vhard_data.puzzle_tuple)


if __name__ == '__main__':
    pytest.main(["test_puzzle_parser.py"])
