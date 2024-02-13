from flask import Blueprint, render_template, request, redirect, url_for, session
from database.database import *

dashboard_blueprint = Blueprint('dashboard',__name__)

@dashboard_blueprint.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')