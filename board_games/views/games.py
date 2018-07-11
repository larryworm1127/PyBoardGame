"""
Flask "games" blueprint

@date: 6/16/2018
@author: Larry Shi
"""

from flask import Blueprint, render_template

game = Blueprint('board_games', __name__, url_prefix='/board_games')


@game.route('/2048')
def twenty_forty_eight():
    return render_template('games/2048.html')


@game.route('/blackjack')
def blackjack():
    return render_template('games/blackjack.html')
