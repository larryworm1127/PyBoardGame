"""
Flask "About" blueprint

@date: 8/1/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template

# init blueprint
bp = Blueprint('about', __name__, url_prefix='/about')


@bp.route('/')
def about():
    return render_template('about/about.html')


@bp.route('/ttt')
def ttt_about():
    return render_template('about/about_ttt.html')


@bp.route('/sudoku')
def sudoku_about():
    return render_template('about/about_sudoku.html')


@bp.route('/blackjack')
def blackjack_about():
    return render_template('about/about_blackjack.html')


@bp.route('/2048')
def twenty_forty_eight_about():
    return render_template('about/about_2048.html')
