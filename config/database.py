from pymongo import MongoClient

client = MongoClient("mongodb://0.0.0.0:55000/")
db = client["CustomPyLogs"]
collection_name = db["SystemInfoLogs"]
