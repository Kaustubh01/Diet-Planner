from flask import Blueprint, render_template

result_blueprint = Blueprint('main',__name__)

result_blueprint.route('/result')
def result():
    return render_template('result.html')