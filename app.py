"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vj4cxex6@localhost:5432/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzrcoolz"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template("home.html")

@app.route('/users')
def users():
    """Show All Users"""
    return

@app.route("/users/new")
def add_new_user():
    """Form for adding a new user"""
    return render_template("new_user.html")

@app.route("/users/new", methods=["POST"])
def post_new_user():
    """Post route for adding a new user. Redirect to /users."""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    profile_url = request.form["profile_url"]

    new_user = User(first_name=first_name, last_name=last_name, profile_url=profile_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")
    # return redirect(f"/{new_user.id}")

# @app.route("/users/<int:user_id>")
# def detailed_user_page():
#     """Show info about a given user, edit or delete user."""

# @app.route("/users/<int:user_id>/edit")
# def edit_page():
#     """Show us the edit page. Has a cancel button to return to the detail page, and a save button."""

# @app.route("/users/<int:[user-id]>/edit", methods=["POST"])
# def post_edit():
#     """POSTS our edit, sends to server to update information."""

# @app.route("/users/<int:user_id>/delete", methods=["POST"])
# def post_delete():
#     """DELETES our user, REDIRECTS to /users"""
