from flask import Blueprint, render_template

login_blueprint = Blueprint('main',__name__)

@login_blueprint.route('/login')
def login():
    return render_template('login.html')