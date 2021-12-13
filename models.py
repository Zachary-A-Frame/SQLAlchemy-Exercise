"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

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
    posts = db.relationship('Post', backref="user", cascade="all, delete-orphan")


    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


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
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
