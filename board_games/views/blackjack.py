"""
Flask "Blackjack" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template

# init blueprint
bp = Blueprint('blackjack', __name__, url_prefix='/games')


@bp.route('/blackjack')
def blackjack():
    return render_template('games/blackjack.html')
