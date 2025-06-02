# -*- encoding: utf-8 -*-

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app.conditions import bp as conditions_bp
app.register_blueprint(conditions_bp)

from app import routes, models
