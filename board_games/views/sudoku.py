"""
Flask "Sudoko" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template, request, jsonify

from ..game_control.sudoku import *
from ..game_control.util import ID_REF, get_id_from_pos
from .auth import login_required

# init blueprint
bp = Blueprint('sudoku', __name__, url_prefix='/games')


@bp.route('/sudoku')
# @login_required
def sudoku():
    dim = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return render_template('games/sudoku.html', dim=dim)


@bp.route('/sudoku/setup')
def setup():
    global game

    game = Sudoku(9)
    return jsonify(result=True)


@bp.route('/sudoku/save_move')
def save_move():
    cell_id = request.args.get('id', 0, type=str)
    pencil = request.args.get('pencil', 0, type=bool)

    pos = ID_REF[cell_id]
    num = game.get_square(pos[0], pos[1])
    print("save move: ", num)
    game.add_move(ID_REF[cell_id], num, pencil)

    return jsonify(result=True)


@bp.route('/sudoku/add_move')
def add_move():
    cell_id = request.args.get('id', 0, type=str)
    num = request.args.get('num', 0, type=int)

    row = ID_REF[cell_id][0]
    col = ID_REF[cell_id][1]
    game.set_square(row, col, num)

    return jsonify(result=True)


@bp.route('/sudoku/get_move')
def get_move():
    last_move = game.get_last_move()
    print("last move: ", last_move)

    if last_move:
        game.set_square(last_move[0][0], last_move[0][1], last_move[1])
        return jsonify(result=get_id_from_pos(last_move[0]),
                       num=last_move[1],
                       pencil=last_move[2])

    return jsonify(result=False)


@bp.route('/sudoku/verify')
def verify():
    result = game.verify_board()

    pos_list = []
    if result is not True and result is not False:
        result = list(result)
        for num in result:
            pos_list.extend(game.get_pos_from_num(num))

    id_list = []
    for pos in pos_list:
        id_list.append(get_id_from_pos(pos))

    return jsonify(result=result, id_list=id_list)
