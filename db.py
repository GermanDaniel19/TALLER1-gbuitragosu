from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        # db.drop_all()
        db.create_all()


