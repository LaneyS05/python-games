from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Define your Blueprints
signup_bp = Blueprint('signup', __name__, url_prefix="/signup")
login_bp = Blueprint('login', __name__, url_prefix="/login")
games_bp = Blueprint('games', __name__, url_prefix="/games")

# Import view functions
from game.LoginSignup import signup, login
signup_bp.add_url_rule('/', view_func=signup)
login_bp.add_url_rule('/', view_func=login)

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/games'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    # Initialize SQLAlchemy with the app
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import models here to prevent circular imports
    from . import models

    # Register the Blueprints
    app.register_blueprint(signup_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(games_bp)  # Register the games Blueprint here

    @app.route('/')
    def hello():
        return render_template('index.html')

    @app.route('/games')
    def games():
        return render_template('games.html')

    return app
