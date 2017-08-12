from config import BLOGS_COLLECTION
from config import DB_NAME

from jsonweb.validators import String
from jsonweb.schema import ObjectSchema

import config
import utils
import uuid
import time


class Schema(ObjectSchema):
	text = String(min_len=1)
	thumbnail = String(min_len=1)
	body = String(min_len=1)
	user = String(min_len=1)
	
	def get_defaults(self):
		return {
			'id': uuid.uuid4().hex, 
			'created_at': time.time(), 
			'updated_at': time.time()
		}


def create_new(data):
	mongo_db = utils.get_db_handler(DB_NAME, BLOGS_COLLECTION)
	mongo_db.insert(data)
	

def get_list(count=10):
	mongo_db = utils.get_db_handler(DB_NAME, BLOGS_COLLECTION)
	cursor = db.find().limit(count)



