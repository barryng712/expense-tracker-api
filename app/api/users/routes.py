from flask import Blueprint, request, jsonify
from app import db
from app.api.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
import logging

users_bp = Blueprint('users', __name__)

# Initialize JWT
jwt = JWTManager()

@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    # Validate input data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Invalid input'}), 400

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], password=hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        logging.error(f"Error registering user: {e}")
        return jsonify({'message': 'Registration failed'}), 500

    return jsonify({'message': 'User registered successfully'}), 201

@users_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    # Validate input data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Invalid input'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

    return jsonify({'message': 'Invalid credentials'}), 401
