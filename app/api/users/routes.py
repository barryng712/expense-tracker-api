from flask import Blueprint, request, jsonify
from app import db
from flask_jwt_extended import create_access_token
from app.api.users.models import User

users_bp=Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
    data=request.get_json()
    new_user=User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered succesfully'}), 201

@users_bp.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    user=User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token=create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid username or password'}), 401
