"""
Flask "Tic Tac Toe" game blueprint

@date: 7/10/2018
@author: Larry Shi
"""

# general imports
from flask import Blueprint, render_template, jsonify, request

from ..tic_tac_toe.ttt_setup import *
from .auth import login_required

# init blueprint
ttt = Blueprint('ttt', __name__, url_prefix='/games')


@ttt.route('/ttt')
@login_required
def tic_tac_toe():
    return render_template('games/tic_tac_toe.html', dim=['one', 'two', 'three'])


@ttt.route('/ttt/setup', methods=['GET', 'POST'])
def setup():
    global game

    human = request.args.get('human', 0, type=str)
    pvp = request.args.get('pvp', 0, type=bool)
    game = TTTSetUp(3, human, pvp=pvp)
    return jsonify(result=str(game))


@ttt.route('/ttt/update', methods=['GET', 'POST'])
def update():
    cell = ID[request.args.get('id', 0, type=str)]
    symbol = request.args.get('symbol', 0, type=str)
    game.board.move(cell[0], cell[1], PLAYERX if symbol == 'X' else PLAYERO)
    return jsonify(result=str(game.board))


@ttt.route('/ttt/check_win', methods=['GET', 'POST'])
def check_win():
    state = game.board.check_win()

    if state == DRAW:
        return jsonify(result="It is a draw!", state='end')
    elif state is not None:
        return jsonify(result="Player " + STRMAP[state] + " wins!", state='end')

    return jsonify(state=None)


@ttt.route('/ttt/get_move', methods=['GET', 'POST'])
def get_move():
    move = game.get_comp_move()

    try:
        return jsonify(result=move, id=row_num[move[0]] + '-' + row_num[move[1]])
    except KeyError:
        return jsonify(result=move)
