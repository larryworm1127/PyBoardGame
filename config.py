"""
Production/Deployment config module for the Flask app

@date: 7/31/2018
@author: Larry Shi
"""

# general imports
import os

from board_games import app

# config variables
SECRET_KEY = os.environ('SECRET_KEY')
DATABASE = os.path.join(app.instance_path, 'board_games.sqlite')
DEBUG = False
