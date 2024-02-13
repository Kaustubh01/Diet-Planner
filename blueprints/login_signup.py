from flask import Blueprint, render_template, request, redirect, url_for, session
from database.database import *

login_blueprint = Blueprint('login',__name__)

@login_blueprint.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = get_user(email)

        if verify_password(user, password):
            # Store user in the session
            session['user'] = email
            return redirect(url_for('dashboard.dashboard'))
        else:
            return 'Invalid username or password.'
    return render_template('login.html')

@login_blueprint.route('/signup' , methods = ['POST','GET'])
def signup():
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    password = request.form.get('password')
    
    insert_user(name, mobile, email, password)

    redirect(url_for('dashboard'))

    return render_template('signup.html')