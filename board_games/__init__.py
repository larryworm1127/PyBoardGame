"""
Flask app factory

@date: 6/12/2018
@author: Larry Shi
"""

# General imports
import os

from flask import Flask, render_template, send_from_directory

# Constant
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

# Load the instance config, if it exists
app.config.from_pyfile('config.py', silent=True)

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


# Register individual apps
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ads.txt')
def ads():
    return send_from_directory('static', 'ads.txt')


# Register blueprints
# 2048 game blueprint
from .views import twenty_forty_eight

app.register_blueprint(twenty_forty_eight.bp)
app.add_url_rule('/', endpoint='index')

# tic-tac-toe game blueprint
from .views import tic_tac_toe

app.register_blueprint(tic_tac_toe.bp)
app.add_url_rule('/', endpoint='index')

# blackjack game blueprint
from .views import blackjack

app.register_blueprint(blackjack.bp)
app.add_url_rule('/', endpoint='index')

# sudoku game blueprint
from .views import sudoku

app.register_blueprint(sudoku.bp)
app.add_url_rule('/', endpoint='index')

# about pages blueprint
from .views import about

app.register_blueprint(about.bp)
app.add_url_rule('/', endpoint='index')
