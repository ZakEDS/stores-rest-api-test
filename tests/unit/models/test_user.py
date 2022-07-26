import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..",".."))
import sys
import os
from models.user import UserModel
from tests.base_test import BaseTest

class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')
        self.assertEqual(user.username, 'test', "Name of user after creation doesn't equal constructor arg")
        self.assertEqual(user.password, 'abcd', "Password of user after creation doesn't equal constructor arg")
