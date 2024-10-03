import unittest
from app import create_app, db
from app.api.expenses.models import Expense

class ExpenseTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app()
        self.app.config['TESTING']=True
        self.app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///:memory:'
        self.client=self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_add_expense(self):
        response=self.client.post('/api/expenses', json={
            'user_id':1,
            'amount':100.0,
            'category':'Food',
            'date':'2023-01-01',
            'description':'Dinner at restaurant'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Expense added successfully')

    def test_get_expenses(self):
        response=self.client.get('/api/expenses')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)
    
if __name__=='__main__':
    unittest.main()
        
        
