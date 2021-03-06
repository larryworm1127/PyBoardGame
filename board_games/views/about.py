"""
Flask "About" blueprint

@date: 8/1/2018
@author: Larry Shi
"""
from flask import Blueprint, render_template

# Init blueprint
bp = Blueprint('about', __name__, url_prefix='/about')


# Blueprint routing
# routing for tic-tac-toe about page
@bp.route('/ttt')
def ttt_about():
    return render_template('about/about_ttt.html')


# routing for sudoku about page
@bp.route('/sudoku')
def sudoku_about():
    return render_template('about/about_sudoku.html')


# routing for blackjack about page
@bp.route('/blackjack')
def blackjack_about():
    deal_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A']
    return render_template('about/about_blackjack.html', deal_cards=deal_cards)


# routing for 2048 about page
@bp.route('/2048')
def twenty_forty_eight_about():
    return render_template('about/about_2048.html')
