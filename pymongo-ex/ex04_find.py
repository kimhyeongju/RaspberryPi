from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

slist = sensors_col.find()

for x in slist:
    print(x)

print(type(slist))  # cursor..?