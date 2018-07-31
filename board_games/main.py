"""
Main module that runs Flask app

@date: 7/27/2018
@author: Larry Shi
"""

import os

from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

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

if __name__ == '__main__':
    app.run()
