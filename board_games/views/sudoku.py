"""
Flask "Sudoko" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template

# init blueprint
bp = Blueprint('sudoku', __name__, url_prefix='/games')


@bp.route('/sudoku')
def sudoku():
    dim = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return render_template('games/sudoku.html', dim=dim)
