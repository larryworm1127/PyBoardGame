"""
Flask "Sudoko" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""
from random import randrange
from typing import Dict

from flask import Blueprint, render_template, request, jsonify

from ..sudoku.puzzle_parser import Puzzles, LINE_NUM
from ..sudoku.sudoku_board import Sudoku
from ..util import ID_REF, get_id_from_pos

# Init blueprint
bp = Blueprint('sudoku', __name__, url_prefix='/games')

# Other constants
game: Dict[str, Sudoku] = {}


# Blueprint routing
# loading sudoku game template
@bp.route('/sudoku')
def sudoku():
    dim = ['one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine']
    return render_template('games/sudoku.html', dim=dim)


# sudoku board setup routing
@bp.route('/sudoku/setup', methods=['GET', 'POST'])
def setup():
    puzzles = Puzzles('easy')
    board = puzzles.get_list_data()[randrange(0, LINE_NUM)].puzzle
    game['inst'] = Sudoku(9, board=board)
    return jsonify(board=game['inst'].get_board())


# sudoku save current move routing
@bp.route('/sudoku/save_move', methods=['GET', 'POST'])
def save_move():
    cell_id = request.args.get('id', 0, type=str)
    pencil = True if request.args.get('pencil') == 'true' else False

    if cell_id != 'None':
        pos = ID_REF[cell_id]
        if pencil:
            num = request.args.get('num', 0, type=int)
        else:
            num = game['inst'].get_square(pos[0], pos[1])

        game['inst'].add_move(pos, num, pencil)

    return jsonify(result=True)


# sudoku update board with new move routing
@bp.route('/sudoku/add_move', methods=['GET', 'POST'])
def add_move():
    cell_id = request.args.get('id', 0, type=str)
    num = request.args.get('num', 0, type=int)

    if cell_id != 'None':
        row = ID_REF[cell_id][0]
        col = ID_REF[cell_id][1]
        game['inst'].set_square(row, col, num)

    return jsonify(result=True)


# sudoku get previous move routing
@bp.route('/sudoku/get_move', methods=['GET', 'POST'])
def get_move():
    last_move = game['inst'].get_last_move()

    # only run following if there are previous moves
    if last_move and not last_move[2]:
        game['inst'].set_square(last_move[0][0], last_move[0][1], last_move[1])

        return jsonify(
            result=get_id_from_pos(last_move[0]),
            num=last_move[1],
            pencil=last_move[2]
        )

    # return False if there are no more moves to undo
    return jsonify(result=False)


# sudoku verify game board routing
@bp.route('/sudoku/verify', methods=['GET', 'POST'])
def verify():
    result = game['inst'].verify_board()

    # get all the incorrect numbers and their position
    pos_list = []
    if type(result) != bool:
        result = list(result)
        for num in result:
            pos_list.extend(game['inst'].get_pos_from_num(num))

    # get the corresponding id with the position
    id_list = []
    for pos in pos_list:
        id_list.append(get_id_from_pos(pos))

    return jsonify(result=result, id_list=id_list)
