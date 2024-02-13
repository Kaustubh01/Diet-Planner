from flask_pymongo import MongoClient
from flask import current_app, g

def get_db():
    if 'db' not in g:
        # Replace 'your_connection_string' with your MongoDB Atlas connection string
        client = MongoClient('mongodb+srv://kaustubhmayekar02:SpAuHfWTuPc35LF0@cluster0.nyt4h5y.mongodb.net/?retryWrites=true&w=majority')
        g.db = client['users']

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.client.close()

def init_app(app):
    app.teardown_appcontext(close_db)
