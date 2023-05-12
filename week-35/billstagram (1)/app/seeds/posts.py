from app.models import db, Post
from sqlalchemy.sql import text
from datetime import datetime

def seed_posts():
    bill_post = Post(
        user_id=1,
        caption="Zuchs be sproutin!",
        image="img/zuchs.jpg",
    )
    finley_post = Post(
        user_id=4,
        caption="Here I am, enjoying some gourmet flour pasta with cheddar infused bechamel",
        image="img/macnchee.jpg",
    )
    maddy_post = Post(
        user_id=3,
        caption="wayne is a goofy kitty",
        image="img/wayne.jpg",
    )
    melissa_post = Post(
        user_id=2,
        caption="I think Maddy's cake turned out pretty good!",
        image="img/maddycake.jpg",
    )
    db.session.add_all([bill_post, melissa_post, maddy_post, finley_post])
    db.session.commit()

def undo_posts():
    db.session.execute(text("DELETE FROM posts"))
    db.session.commit()