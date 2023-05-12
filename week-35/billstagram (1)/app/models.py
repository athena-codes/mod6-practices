from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    img = db.Column(db.String(500), nullable=True)
    bio = db.Column(db.String(500), nullable=False)

    posts = db.relationship("Post", back_populates="user", cascade="all, delete")
    comments = db.relationship("Comment", back_populates="user", cascade="all, delete")

    def to_dict(self):
        return {
            'id':self.id,
            'username':self.username,
            'email':self.email,
            'img':self.img,
            'bio':self.img
        }



class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    caption = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=True)
    date_posted = db.Column(db.DateTime, server_default=func.now(),default=func.now())
    updatedat = db.Column(db.DateTime, onupdate=func.now(),default=func.now())

    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")

    def to_dict(self):
        return {
            "id":self.id,
            "image":self.image,
            "caption":self.caption,
            "author":self.user.to_dict()["username"],
            "author_id":self.user_id,
            "comments": [comment.to_dict() for comment in self.comments],
            "date_posted":self.date_posted
        }


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    text = db.Column(db.String(500), nullable=False)

    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

    def to_dict(self):
        return {
            "author": self.user.to_dict()["username"],
            "text":self.text,
            "author_id" : self.user_id,
        }
