from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

list = sensors_col.find().sort("value") # default는 오름차순. 내림차순은 .sort("value", -1)

for x in list:
    print(x)