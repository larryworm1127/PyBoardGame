"""
Flask "2048" game blueprint

@date: 7/11/2018
@author: Larry Shi
"""
from flask import Blueprint, render_template

# Init blueprint
bp = Blueprint('2048', __name__, url_prefix='/games')


# Blueprint routing
# loading 2048 game template
@bp.route('/2048')
def twenty_forty_eight():
    return render_template('games/2048.html')
