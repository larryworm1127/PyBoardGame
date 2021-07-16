"""
Flask app factory

@date: 6/12/2018
@author: Larry Shi
"""
import os

from flask import Flask, render_template

# Constant
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_app():
    flask_app = Flask(__name__)
    if 'APP_SETTINGS' in os.environ:
        flask_app.config.from_object(os.environ['APP_SETTINGS'])
    else:
        flask_app.config.from_object('config.DevelopmentConfig')

    # Register individual apps
    @flask_app.route('/')
    def index():
        return render_template('index.html')

    # Register blueprints
    from board_games.views import (
        twenty_forty_eight, tic_tac_toe, blackjack, sudoku
    )
    flask_app.register_blueprint(twenty_forty_eight.bp)
    flask_app.register_blueprint(tic_tac_toe.bp)
    flask_app.register_blueprint(blackjack.bp)
    flask_app.register_blueprint(sudoku.bp)

    return flask_app


app = create_app()
