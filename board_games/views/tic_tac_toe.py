"""
Flask "Tic Tac Toe" game blueprint

@date: 7/10/2018
@author: Larry Shi
"""
from flask import Blueprint, render_template, jsonify, request

from ..tic_tac_toe.ttt_board import *
from ..util import ID_REF, get_id_from_pos

# Init blueprint
bp = Blueprint('ttt', __name__, url_prefix='/games')


# Blueprint routing
# loading tic-tac-toe-board game template
@bp.route('/ttt')
def tic_tac_toe():
    dim = ['one', 'two', 'three']
    return render_template('games/tic_tac_toe.html', dim=dim)


# ttt game board setup routing
@bp.route('/ttt/setup', methods=['GET', 'POST'])
def setup():
    global game

    human = request.args.get('human', 0, type=str)
    pvp = request.args.get('pvp', 0, type=bool)

    human = PLAYERX if human == 'X' else PLAYERO
    game = TTTSetUp(3, human, switch_player(human), pvp=pvp)
    return jsonify(result=str(game))


# ttt update game board routing
@bp.route('/ttt/update', methods=['GET', 'POST'])
def update():
    try:
        cell = ID_REF[request.args.get('id', 0, type=str)]
        symbol = request.args.get('symbol', 0, type=str)
        game.board.move(cell[0], cell[1], PLAYERX if symbol == 'X' else PLAYERO)
        return jsonify(result=str(game.board))
    except KeyError:
        return jsonify(result=False)


# ttt check win cases routing
@bp.route('/ttt/check_win', methods=['GET', 'POST'])
def check_win():
    state = game.board.check_win()

    if state == DRAW:
        return jsonify(result="It is a draw!", state='end')
    elif state is not None:
        return jsonify(result="Player " + STRMAP[state] + " wins!", state='end')

    return jsonify(state=None)


# ttt get COMPUTER move routing
@bp.route('/ttt/get_move', methods=['GET', 'POST'])
def get_move():
    move = game.get_comp_move()

    try:
        return jsonify(result=move, id=get_id_from_pos(move))
    except KeyError:
        return jsonify(result=move)
