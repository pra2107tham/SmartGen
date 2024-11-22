from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "mongodb+srv://pratham:pratham@smartgen.xp4k1.mongodb.net/smartgen?retryWrites=true&w=majority"
mongo_client = MongoClient(MONGO_URI)
db = mongo_client.smartgen  # Replace `smartgen` with your database name
