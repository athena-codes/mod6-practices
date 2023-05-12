from app.models import db, User
from sqlalchemy.sql import text
from datetime import datetime

def seed_users():
    bill = User(
        username="Biff", 
        email="biff@biff.biff", 
        img="img/profile.jpg", 
        bio="Definitely not Bill :)"
    )
    finley = User(
        username="Fimbo",
        email="fimbo@magim.bo",
        img="img/profile2.jpg",
        bio="lil baby roomba"
    )
    maddy = User(
        username="Murgatroyyd",
        email="murg@troy.yd",
        img="img/profile3.jpg",
        bio="Songs, dancing, mac'n'cheese, livin my life"
    )
    melissa = User(
        username="momlissa",
        email="melissa@mom.best",
        img="img/profile4.jpg",
        bio="Three things motivate me, cheese, my family, and more cheese."
    )
    db.session.add_all([bill, melissa, maddy, finley])
    db.session.commit()

def undo_users():
    db.session.execute(text("DELETE FROM users"))
    db.session.commit()