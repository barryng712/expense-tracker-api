from flask import Blueprint

api_bp = Blueprint('api', __name__)

from app.api.expenses.routes import expenses_bp
from app.api.users.routes import users_bp

api_bp.register_blueprint(expenses_bp, url_prefix='/expenses')
api_bp.register_blueprint(users_bp, url_prefix='/users')

