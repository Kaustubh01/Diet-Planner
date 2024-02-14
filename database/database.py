from flask_pymongo import MongoClient
from flask import current_app, g

def get_db():
    if 'db' not in g:
        # Replace 'your_connection_string' with your MongoDB Atlas connection string
        client = MongoClient('mongodb+srv://admin:pJAehpe7HyaN7klL@cluster0.r4svnil.mongodb.net/?retryWrites=true&w=majority')
        g.db = client['diet']

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.client.close()

def insert_user(username, mobile, email, password):
    db = get_db()
    user_data = {'username': username,'mobile': mobile, 'email': email, 'password': password}
    db.users.insert_one(user_data)

def get_user(email):
    db = get_db()
    return db.users.find_one({'email': email})

def verify_password(user, password):
    return user and user['password'] == password


def init_app(app):
    app.teardown_appcontext(close_db)


