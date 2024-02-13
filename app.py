from flask import Flask, render_template
from blueprints.login_signup import login_blueprint
from blueprints.result import result_blueprint
from database.database import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

app.register_blueprint(login_blueprint)
app.register_blueprint(result_blueprint)

@app.route('/')
def hello():
    db = get_db()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
