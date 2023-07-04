from pymongo import MongoClient
from Scripts.constants.app_configuration import config

mongo_uri = config.get('MONGODB', 'URI')
db = config.get('MONGODB', 'db_name')


class MongoLite:
    def __init__(self):
        self.connection = MongoClient(mongo_uri)
        self.db = self.connection[db]

    def for_insert_one(self, collection, dictionary):
        collection_1 = self.db[collection]
        if collection_1.insert_one(dictionary):
            return True
        else:
            return False

    def for_sign_insert_one(self, collection, dictionary):
        collection_1 = self.db[collection]
        if collection_1.insert_one(dictionary.dict()):
            return True
        else:
            return False

    def for_find_one(self, collection, data):
        collection_1 = self.db[collection]
        if collection_1.find_one(data):
            return True
        else:
            return False

    def for_delete_one(self, collection, data):
        collection_1 = self.db[collection]
        if collection_1.delete_one(data):
            return True
        else:
            return False

    def for_update_one(self, collection, data, set):
        collection_1 = self.db[collection]
        if collection_1.update_one(data, set):
            return True
        else:
            return False


mongo = MongoLite()
