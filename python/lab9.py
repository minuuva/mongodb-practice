#!/usr/bin/env python3

import os
from pymongo import MongoClient

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
cluster_url = os.getenv("MONGODB_CLUSTER_URL")

connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/"
client = MongoClient(connection_string)

db = client["qce2dp"]
collection = db["baseball"]

documents = [
    {"position": "pitcher", "hometown": ["Virginia Beach", "Virginia"]},
    {"position": "catcher", "hometown": ["San Diego", "California"]},
    {"position": "infielder", "hometown": ["Chicago", "Illinois"]},
    {"position": "outfielder", "hometown": ["Seoul", "South Korea"]},
    {"position": "bullpen", "hometown": ["Tokyo", "Japan"]},
]
collection.insert_many(documents)

results = collection.find().limit(3)
for doc in results:
    print(doc)