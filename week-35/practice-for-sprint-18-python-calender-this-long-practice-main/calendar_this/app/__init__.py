from flask import Flask
from .routes.routes import bp
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(bp)

# app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
# @app.route('/')
# def index():
#     return '<h1> I work :D </h1>'
