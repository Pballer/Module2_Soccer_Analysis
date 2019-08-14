"""Wrapper module for MongoDB. """

import pymongo

class MongoDbStore(object):
    
    def __init__(self, host, data_base):
        self.host = host
        self.client = pymongo.MongoClient(host)
        self.mongo_data_base = self.client[data_base]
        
        
    def store(self, data, collection_name):
        collection = self.mongo_data_base[collection_name]
        obj_id = collection.insert_one(data)
        return obj_id
    
    
    def store_many(self, data, collection_name):
        collection = self.mongo_data_base[collection_name]
        obj_id = collection.insert_many(data)
        return obj_id

