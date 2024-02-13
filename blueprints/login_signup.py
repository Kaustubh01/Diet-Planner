from flask import Blueprint, render_template
from database.database import *

login_blueprint = Blueprint('login',__name__)

@login_blueprint.route('/login')
def login():
    return render_template('login.html')

@login_blueprint.route('/signup')
def signup():
    return render_template('signup.html')