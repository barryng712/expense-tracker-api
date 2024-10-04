import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import unittest
from app.api.expenses.models import Expense
from app import create_app, db
from flask_jwt_extended import create_access_token
from app.api.users.models import User  # Import the User model

class ExpenseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            # Create a test user
            user = User(id=1, username='testuser', password='testpassword')
            db.session.add(user)
            db.session.commit()
            self.access_token = create_access_token(identity=user.id)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_add_expense(self):
        response = self.client.post(
            '/api/expenses',
            json={
                'amount': 100.0,
                'category': 'Food',
                'date': '2023-01-01',
                'description': 'Dinner at restaurant'
            },
            headers={'Authorization': f'Bearer {self.access_token}'}
        )
        print(response.json)  # Add this line to inspect the response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Expense added successfully')

    def test_get_expenses(self):
        response = self.client.get(
            '/api/expenses',
            headers={'Authorization': f'Bearer {self.access_token}'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)
    
if __name__ == '__main__':
    unittest.main()

