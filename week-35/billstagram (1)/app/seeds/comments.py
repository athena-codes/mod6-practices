from app.models import db, Comment
from sqlalchemy.sql import text
from datetime import datetime

def seed_comments():
    bill_comment = Comment(
        user_id=1,
        post_id=3,
        text="he sure is",
    )
    finley_comment = Comment(
        user_id=4,
        post_id=2,
        text="It sure does mama!"
    )
    maddy_comment = Comment(
        user_id=3,
        post_id=1,
        text="YUCK! ZUCCHINI IS DISGUSTING!"
    )
    melissa_comment = Comment(
        user_id=2,
        post_id=4,
        text="Just like her mama 🥰"
    )
    db.session.add_all([bill_comment, melissa_comment, maddy_comment, finley_comment])
    db.session.commit()

def undo_comments():
    db.session.execute(text("DELETE FROM comments"))
    db.session.commit()