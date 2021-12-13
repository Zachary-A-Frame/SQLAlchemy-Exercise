"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

# Models Go Below!

class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        s = self
        return f"<User {s.id} {s.first_name} {s.last_name} {s.profile_url}>"

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
    posts = db.relationship('Post')

class Post(db.Model):
    __tablename__ = 'posts'

    def __repr__(self):
        s = self
        return f"<Post {s.id}, {s.title}, {s.content} {s.created_at} {s.user_id}"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(200),
                           nullable=False,
                           unique=False)
    content = db.Column(db.String(5000),
                        nullable=False,
                        unique=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))


