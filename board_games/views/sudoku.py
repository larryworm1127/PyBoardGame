"""
Flask "Sudoko" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template, request, jsonify

from ..tic_tac_toe.sudoku import *
from ..tic_tac_toe.ttt_board import id_ref
from .auth import login_required

# init blueprint
bp = Blueprint('sudoku', __name__, url_prefix='/games')


@bp.route('/sudoku')
@login_required
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
    game.add_move(cell_id)

    return jsonify(result=True)


@bp.route('/sudoku/add_move')
def add_move():
    cell_id = request.args.get('id', 0, type=str)
    num = request.args.get('num', 0, type=int)

    row = id_ref[cell_id][0]
    col = id_ref[cell_id][1]
    game.set_square(row, col, num)

    return jsonify(result=str(game))


@bp.route('/sudoku/get_move')
def get_move():
    last_move = game.get_last_move()
    if last_move:
        return jsonify(result=last_move)

    return jsonify(result=False)


@bp.route('/sudoku/get_board')
def get_board():
    board = game.get_board()

    return jsonify(result=board)
