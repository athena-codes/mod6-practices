from flask import Flask, render_template
from .config import Config
from .routes.routes import bp, shipping_request
from .models.shipping_form import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(bp)
app.register_blueprint(shipping_request)
db.init_app(app)
migrate = Migrate(app, db)
