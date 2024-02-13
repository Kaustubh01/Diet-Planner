from flask import Flask, render_template, session
from blueprints.login_signup import login_blueprint
from blueprints.result import result_blueprint
from blueprints.dashboard import dashboard_blueprint
from database.database import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

app.register_blueprint(login_blueprint)
app.register_blueprint(result_blueprint)
app.register_blueprint(dashboard_blueprint)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
