import unittest
from app import create_app, db

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_user(self):
        response = self.client.post('/api/users/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.client.post('/api/users/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.client.post('/api/users/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
