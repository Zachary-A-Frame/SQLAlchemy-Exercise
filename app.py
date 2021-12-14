"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

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
    return render_template("root.html")

@app.route('/users')
def users():
    """Show All Users"""
    users = User.query.all()
    return render_template("home.html", users=users)

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

    return redirect(f"/users/{new_user.id}")

@app.route("/users/<int:user_id>")
def detailed_user_page(user_id):
    """Show info about a given user, edit or delete user."""
    user = User.query.get_or_404(user_id)

    posts = user.posts

    return render_template("user.html", user=user, posts=posts)


@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.profile_url = request.form['profile_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/")

# ######################################### PART 2 ############################################
# Some additions were made to the previous routes above, exclusive to part 2 routes will be below.


@app.route("/users/<int:user_id>/posts/new")
def view_new_post_form(user_id):
    """View new post form"""
    user = User.query.get_or_404(user_id)

    return render_template("posts/new_post.html", user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def new_post(user_id):
    """New post form"""
    title = request.form["title"]
    content = request.form["content"]
    user_id = user_id

    new_post = Post(title=title, content=content, user_id=user_id)

    db.session.add(new_post)
    db.session.commit()
    return redirect("/")


