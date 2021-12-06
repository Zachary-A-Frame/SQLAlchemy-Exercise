"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

# Models Go Below!

class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        s = self
        return

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False,
                           unique=False)
    last_name = db.Column(db.String(50),
                          nullable=False,
                          unique=False)
    profile_url = db.Column(db.String(1000),
                          nullable=True,
                          unique=False,
                          default="https://i.imgur.com/ST5Q7hj.png")
