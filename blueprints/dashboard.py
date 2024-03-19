from flask import Blueprint, render_template, request, redirect, url_for, session
import pandas as pd
from database.database import *
import json
from Model import execModel, finalModel

dashboard_blueprint = Blueprint('dashboard', __name__)


@dashboard_blueprint.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if request.method == 'POST':
        calories = int(request.form['calories'])
        gender = request.form['gender']
        selected_days = request.form.getlist('days')
        weight = int(request.form['weight'])
        height = int(request.form['height'])

        print(selected_days)
        diet = finalModel(weight, calories)

        output = execModel(diet, selected_days)
        session['result']= output
        return redirect(url_for('dashboard.result'))



    return render_template('dashboard.html', days_of_week=days_of_week)


@dashboard_blueprint.route('/result')
def result():
    result = session.get('result', [])
    return render_template('result.html', output=result)
