from flask import Flask
from .routes.routes import bp
from .config import Config


app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(bp)

# @app.route('/')
# def index():
#     return '<h1> I work :D </h1>'
