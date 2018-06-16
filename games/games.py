from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

blue_print = Blueprint('games', __name__, url_prefix='/games')


@blue_print.route('/')
def index():
    return render_template('games/index.html')


@blue_print.route('/tic_tac_toe')
def tic_tac_toe():
    return render_template('games/tic_tac_toe.html')
