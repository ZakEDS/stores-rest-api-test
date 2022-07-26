import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..",".."))
from models.store import StoreModel
from app import app
from unittest import TestCase

class StoreTest(TestCase):
    def test_create_store(self):
        store = StoreModel('test')
        self.assertEqual(store.name, 'test', "Name of store after creationn doesn't equal constructor arg")
