from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
jwt = JWTManager()
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)  # Ensure this line is present
    jwt.init_app(app)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.main import main_bp
    app.register_blueprint(main_bp)

    return app
