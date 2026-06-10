import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User('John Doe', 'john@example.com', 'USR1')
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.user_id, 'USR1')
    
    def test_user_to_dict(self):
        user = User('Jane Smith', 'jane@example.com', 'USR2')
        user_dict = user.to_dict()
        self.assertEqual(user_dict['name'], 'Jane Smith')
        self.assertEqual(user_dict['email'], 'jane@example.com')
    
    def test_user_from_dict(self):
        data = {'name': 'Bob Wilson', 'email': 'bob@example.com', 'user_id': 'USR3'}
        user = User.from_dict(data)
        self.assertEqual(user.name, 'Bob Wilson')
        self.assertEqual(user.email, 'bob@example.com')
    
    def test_display_info(self):
        user = User('Alice Brown', 'alice@example.com', 'USR4')
        info = user.display_info()
        self.assertIn('Alice Brown', info)
        self.assertIn('alice@example.com', info)

if __name__ == '__main__':
    unittest.main()