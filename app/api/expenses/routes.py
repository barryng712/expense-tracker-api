from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.api.expenses.models import Expense

expenses_bp =Blueprint('expenses', __name__)


@expenses_bp.route('/expenses', methods=['POST'])
@jwt_required()
def add_expense():
    user_id=get_jwt_identity()
    data=request.get_json()
    new_expense=Expense(user_id=user_id, **data)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'}), 201

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
    expense.amount=data['amount']
    expense.category=data['category']
    expense.date=data['date']
    expense.description=data['description']
    db.session.commit()
    return jsonify({'message': 'Expense updated successfully'}), 200

@expenses_bp.route('/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    expenses=Expense.query.all()
    return jsonify(expenses), 200

