from flask.cli import AppGroup

from app.models import db
from .users import seed_users, undo_users
from .comments  import seed_comments, undo_comments
from .posts import seed_posts, undo_posts

seed_commands = AppGroup("seed")

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_posts()
    seed_comments()

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_comments()
    undo_posts()
    undo_users()
    
