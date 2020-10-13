from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

query = {"value": {"$gt":24}} # gt(greater than) <-> lt(lesser than), 55보다 큰 것
                                # gte, lte, ne(not equal)
projection = {"_id":0, "topic":1, "value":1} # topic과 value만 출력
# projection = {"_id":0, "reg_date":0}    # reg_date를 빼서 위와 같은 효과
slist = sensors_col.find(query,projection).sort("value") # .sort("value", -1)

for x in slist:
    print(x)
