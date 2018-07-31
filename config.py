"""
Production/Deployment config module for the Flask app

@date: 7/31/2018
@author: Larry Shi
"""

# general imports
import os

from board_games import app

# config variables
SECRET_KEY = b'c47da79190345efef83858ae4596dbaa4e04f7fc888a6f34'
DATABASE = os.path.join(app.instance_path, 'board_games.sqlite')
DEBUG = False
