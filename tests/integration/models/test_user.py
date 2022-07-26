import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..",".."))
from models.user import UserModel
from tests.base_test import BaseTest

class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')
            self.assertIsNone(UserModel.find_by_username('test'), "Found a user with name 'test' before save_to_db")
            self.assertIsNone(UserModel.find_by_id(1), "Found a user with id '1' before save_to_db")
            
            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'), "Could not find a user with name 'test' after save_to_db")
            self.assertIsNotNone(UserModel.find_by_id(1), "Could not find a user with id '1' after save_to_db")