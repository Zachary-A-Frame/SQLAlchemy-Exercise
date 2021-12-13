"""Seed file to make sample data!!!"""

from models import User, Post, db
from app import app

#create all tables
db.drop_all()
db.create_all()

# Data
zach = User(first_name="Zach", last_name="Frame",
            profile_url="https://cdn.iconscout.com/icon/free/png-256/discord-3464287-2903934.png")

donkey = User(first_name="Jason", last_name="Dunkey",
              profile_url="https://i.ytimg.com/vi/9odvzI1hnXY/maxresdefault.jpg")

teejay = User(first_name="Tim", last_name="Snyder",
              profile_url="https://www.fanbyte.com/wp-content/uploads/2019/06/fatchocobo.jpg")
# 1st Session add and commit
db.session.add(zach)
db.session.add(donkey)
db.session.add(teejay)

db.session.commit()

# 2nd Session add and commit
first_post = Post(title="Filler title", content="Lots of text weeeee haaaaa")
second_post = Post(title="Filler title numba 2", content="Lots of text weeeee haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
third_post = Post(title="Filler title numero 3", content="Lots of text weeeee haaaaaAAaaAAaaAaAaAaAAaAaAaAaaaAAaaaaaaA")

db.session.add(first_post)
db.session.add(second_post)
db.session.add(third_post)

db.session.commit()