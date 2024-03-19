from flask import Blueprint, render_template

games_bp = Blueprint('games', __name__, url_prefix="/games")

@games_bp.route('/')
def games():
    return render_template('games.html')
