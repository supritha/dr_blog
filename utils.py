from pymongo import MongoClient

import config


def get_db_handler(db_name, collection_name):
	mongo_client = MongoClient(config.MONGO_DB_URL)
	return mongo_client[db_name]