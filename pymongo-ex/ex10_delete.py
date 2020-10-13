from pymongo import MongoClient
from datetime import datetime
import random
from bson.objectid import ObjectId

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

# query = {"value":{"$lt":55}}
query = {"_id":ObjectId("5f83e9ca6827b0a801859c7d")}    # objectID로 삭제
sensors_col.delete_one(query)

sensor_values = sensors_col.find(query)
for x in sensor_values:
    print(x)