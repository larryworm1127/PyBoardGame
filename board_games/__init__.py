"""
Flask app factory

@date: 6/12/2018
@author: Larry Shi
"""

import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=b'c47da79190345efef83858ae4596dbaa4e04f7fc888a6f34',
        DATABASE=os.path.join(app.instance_path, 'board_games.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register apps and blueprints
    @app.route('/')
    def index():
        return render_template('index.html')

    from .views import auth
    app.register_blueprint(auth.bp)
    app.add_url_rule('/', endpoint='index')

    from .views import twenty_forty_eight
    app.register_blueprint(twenty_forty_eight.bp)
    app.add_url_rule('/', endpoint='index')

    from .views import tic_tac_toe
    app.register_blueprint(tic_tac_toe.bp)
    app.add_url_rule('/', endpoint='index')

    from .views import blackjack
    app.register_blueprint(blackjack.bp)
    app.add_url_rule('/', endpoint='index')

    from .views import sudoku
    app.register_blueprint(sudoku.bp)
    app.add_url_rule('/', endpoint='index')

    # register database
    from . import db
    db.init_app(app)

    return app
