"""
Main module that runs Flask app

@date: 7/27/2018
@author: Larry Shi
"""

# general imports
from board_games import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
