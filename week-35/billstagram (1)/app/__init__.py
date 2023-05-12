  
from flask import Flask
from .models import db
from .config import Configuration
from app.routes import app_routes
from flask_migrate import Migrate
from .seeds import seed_commands
import os

app = Flask(__name__)

app.config.from_object(Configuration)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.cli.add_command(seed_commands)

app.register_blueprint(app_routes, url_prefix="/")

db.init_app(app)
Migrate(app, db)