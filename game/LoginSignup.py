from flask import Blueprint, render_template

login_bp = Blueprint('login', __name__, url_prefix="/login")

@login_bp.route('/')
def login():
    return render_template('login.html')

signup_bp = Blueprint('signup', __name__, url_prefix="/signup")

@signup_bp.route('/')
def signup():
    return render_template('signup.html')
 
