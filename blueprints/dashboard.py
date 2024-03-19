from flask import Blueprint, render_template, request, redirect, url_for, session
from database.database import *

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
        print(f"output: {output[0]}")

        return redirect(
            url_for('dashboard.dashboard', output=output))

    return render_template('dashboard.html', days_of_week=days_of_week)
