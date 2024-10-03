import unittest
from app import create_app, db
from app.api.users.models import User

class UserTestCase(unittest.TestCase):
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

    def test_register_user(self):
        response=self.client.post('/api/users/register', json={
            'username':'testuser',
            'password':'testpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered', response.get_data(as_text=True))

    def test_login_user(self):
        self.client.post('/api/users/register', json={
            'username':'testuser',
            'password':'testpassword'
        })
        response=self.client.post('/api/users/login', json={
            'username':'testuser',
            'password':'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())

if __name__=='__main__':
    unittest.main()
