"""
Flask "Sudoko" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template, request, jsonify

# init blueprint
bp = Blueprint('sudoku', __name__, url_prefix='/games')

# game variables
moves = []


@bp.route('/sudoku')
def sudoku():
    dim = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return render_template('games/sudoku.html', dim=dim)


@bp.route('/sudoku/save_move')
def save_move():
    cell_id = request.args.get('id', 0, type=str)
    moves.append(cell_id)

    return jsonify(result=moves)


@bp.route('/sudoku/get_move')
def get_move():
    if moves:
        cell_id = moves.pop()
        return jsonify(result=cell_id)

    return jsonify(result=None)
