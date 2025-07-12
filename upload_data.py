from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://arushi:12345@cluster0.vewpniy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

DATABASE_NAME = "skills"
COLLECTION_NAME = 'waferfault'

df = pd.read_csv("C:\Users\user\OneDrive - IIT Kanpur\Desktop\Sensor Project\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unmanned: 0",axis =1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

