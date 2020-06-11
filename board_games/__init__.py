"""
Flask app factory

@date: 6/12/2018
@author: Larry Shi
"""

# General imports
import os

from flask import Flask, render_template
from dotenv import load_dotenv

# Constant
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(os.environ['APP_SETTINGS'])

    # Register individual apps
    @flask_app.route('/')
    def index():
        return render_template('index.html')

    # Register blueprints
    from .views import twenty_forty_eight
    flask_app.register_blueprint(twenty_forty_eight.bp)
    flask_app.add_url_rule('/', endpoint='index')

    from .views import tic_tac_toe
    flask_app.register_blueprint(tic_tac_toe.bp)
    flask_app.add_url_rule('/', endpoint='index')

    from .views import blackjack
    flask_app.register_blueprint(blackjack.bp)
    flask_app.add_url_rule('/', endpoint='index')

    from .views import sudoku
    flask_app.register_blueprint(sudoku.bp)
    flask_app.add_url_rule('/', endpoint='index')

    from .views import about
    flask_app.register_blueprint(about.bp)
    flask_app.add_url_rule('/', endpoint='index')

    return flask_app


app = create_app()
