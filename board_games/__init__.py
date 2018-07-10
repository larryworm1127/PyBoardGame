"""
Flask app factory

@date: 6/12/2018
@author: Larry Shi
"""

import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
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
    from .views import games
    app.register_blueprint(games.game)
    app.add_url_rule('/', endpoint='index')

    from .views import tic_tac_toe
    app.register_blueprint(tic_tac_toe.ttt)
    app.add_url_rule('/', endpoint='index')

    return app
