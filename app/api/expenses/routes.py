from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.api.expenses.models import Expense
from app.api.expenses.serializers import ExpenseSchema
from marshmallow.exceptions import ValidationError
import logging

expenses_bp =Blueprint('expenses', __name__)

expense_schema=ExpenseSchema()
expenses_schema=ExpenseSchema(many=True)

@expenses_bp.route('/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    user_id = get_jwt_identity()
    data = request.get_json()
    try:
        validated_data = expense_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    new_expense = Expense(user_id=user_id, **validated_data)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({
        'message': 'Expense added successfully',
        'expense': expense_schema.dump(new_expense)
    }), 201

@expenses_bp.route('/expenses/<int:expense_id>', methods=['DELETE'])
@jwt_required()
def remove_expense(expense_id):
    expense=Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense removed successfully'}), 200


@expenses_bp.route('/expenses/<int:expense_id>', methods=['PUT'])
@jwt_required()
def update_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    data = request.get_json()
    try:
        validated_data=expense_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    for key, value in validated_data.items():
        setattr(expense, key, value)
    db.session.commit()
    return jsonify(expense_schema.dump(expense)), 200

@expenses_bp.route('/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    logging.info("Received request for /api/expenses")
    expenses = Expense.query.all()
    return jsonify(expenses), 200

