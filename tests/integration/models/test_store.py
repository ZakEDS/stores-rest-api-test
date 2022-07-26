import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..",".."))
from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')
        self.assertListEqual(store.items.all(),[], "The store's length was non 0 despite no items added")
    
    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
        

            self.assertIsNone(StoreModel.find_by_name('test'), "Found a store with name {}, but expected not to.".format(store.name))
            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'), "Expected to find a store with name {}, but didn't.".format(store.name))
            store.delete_from_db()
            
            self.assertIsNone(StoreModel.find_by_name('test'), "Found a store with name {}, which should have been deleted.".format(store.name))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'id': None,
            'name': 'test',
            'items': []
        }
        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()
            expected = {
                'id': 1,
                'name': 'test',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }
            self.assertDictEqual(store.json(), expected)