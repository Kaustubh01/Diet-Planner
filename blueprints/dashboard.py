import pickle

import numpy as np
from flask import Blueprint, render_template, request, redirect, url_for, session
from database.database import *

dashboard_blueprint = Blueprint('dashboard', __name__)


def calculate_bmi(weight_kg, height_cm):
    # Convert height from centimeters to meters
    height_m = height_cm / 100

    # Calculate BMI using the formula
    bmi = weight_kg / (height_m ** 2)

    return bmi


def calculate_tdee(age, gender, weight_kg, height_cm, activity_level):
    # Constants for activity levels
    activity_levels = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    # Convert height from centimeters to meters
    height_m = height_cm / 100

    # Calculate BMR (Basal Metabolic Rate) using the Harris-Benedict equation
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_m) - (5.677 * age)
    elif gender.lower() == 'female':
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_m) - (4.330 * age)
    else:
        raise ValueError('Invalid gender. Use "male" or "female".')

    # Calculate TDEE by multiplying BMR with activity level
    tdee = bmr * activity_levels.get(activity_level.lower(), 1.2)

    return tdee


@dashboard_blueprint.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        age = int(request.form['age'])
        gender = request.form['gender']
        activity_level = request.form['activity_level']
        weight = int(request.form['weight'])
        height = int(request.form['height'])

        bmi = calculate_bmi(weight_kg=weight, height_cm=height)
        tdee_result = calculate_tdee(age, gender, weight, height, activity_level)

        return redirect(
            url_for('dashboard.result', age=age, gender=gender, activity_level=activity_level, weight=weight,
                    height=height, bmi=bmi, tdee=tdee_result))

    return render_template('dashboard.html')


@dashboard_blueprint.route('/result')
def result():
    age = request.args.get('age', type=int)
    gender = request.args.get('gender')
    activity_level = request.args.get('activity_level')
    weight = request.args.get('weight', type=int)
    height = request.args.get('height', type=int)
    bmi = round(request.args.get('bmi', type=float),1)

    health_status = 'normal'

    if bmi < 18.5:
        health_status = 'underweight'
    elif 18.5 <= bmi <= 24.9:
        health_status = 'normal'
    elif 25 <= bmi <= 29.9:
        health_status = 'overweight'
    else:
        health_status = 'obese'

    tdee_result = request.args.get('tdee', type=float)

    with open('knn_classifier', 'rb') as file:
        loaded_model = pickle.load(file)
        predictions = loaded_model.predict(np.array([tdee_result]).reshape(1, -1))
    return render_template('result.html', age=age, gender=gender, activity_level=activity_level,
                           weight=weight, height=height, bmi=bmi, tdee=tdee_result, predictions=predictions[0],health_status=health_status)
