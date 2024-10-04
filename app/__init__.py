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
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.api.expenses.routes import expenses_bp
    app.register_blueprint(expenses_bp, url_prefix='/api')

    from app.api.users.routes import users_bp
    app.register_blueprint(users_bp, url_prefix='/api/users')

    from app.main import main_bp
    app.register_blueprint(main_bp)

    return app
