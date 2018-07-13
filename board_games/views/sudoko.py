"""
Flask "Sudoko" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template

# init blueprint
bp = Blueprint('sudoko', __name__, url_prefix='/games')


@bp.route('/sudoko')
def sudoko():
    dim = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return render_template('games/sudoko.html', dim=dim)
